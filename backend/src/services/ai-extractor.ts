import { writeFileSync, unlinkSync, createReadStream, existsSync, readFileSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ... (keep ExtractionResult and EXTRACTION_PROMPT as they were) ...
interface ExtractionResult {
  newspaperName: string;
  date: string;
  articles: Array<{
    id: string;
    title: string;
    subtitle: string;
    body: string;
    category?: string;
    page?: number;
    isHighlight: boolean;
    media?: Array<{ type: "photo" | "chart" | "map"; caption: string; box: [number, number, number, number]; page: number }>;
  }>;
}

const EXTRACTION_PROMPT = `Sei un analista esperto di quotidiani italiani. Ti vengono fornite le IMMAGINI di tutte le pagine di un quotidiano italiano. Devi analizzare visivamente ogni pagina, leggere il contenuto rispettando il layout a colonne, e identificare tutti gli articoli presenti.

COME LEGGERE LE PAGINE:
- I quotidiani italiani usano un layout MULTI-COLONNA (tipicamente 5-6 colonne per pagina).
- Leggi ogni colonna dall'alto verso il basso, poi passa alla colonna successiva a destra.
- Un articolo può svilupparsi su PIÙ COLONNE nella stessa pagina.
- Un articolo può CONTINUARE SU PIÙ PAGINE (cerca indicazioni come "segue a pagina X", "continua a pagina X", "→", o frecce). In questo caso, unisci le parti in un unico articolo.
- I TITOLI degli articoli sono tipicamente in carattere grande e in grassetto.
- I SOTTOTITOLI (occhielli, sommari) sono in un font intermedio, spesso in corsivo o sotto il titolo.

REGOLE IMPORTANTI:
1. La PRIMA PAGINA del giornale è tipicamente una pagina di sommario/anteprima con i titoli degli articoli principali e brevi anticipazioni. La maggior parte di questi articoli viene ripresa nelle pagine successive con il testo completo. Solo 1-2 articoli della prima pagina sono pezzi unici che NON si ripetono nel resto del giornale.

2. FOTO, GRAFICI E MAPPE:
   - Trova e includi le FOTO, i GRAFICI o le MAPPE pertinenti all'articolo (es. foto di cronaca, mappe geopolitiche, grafici economici).
   - IGNORA COMPLETAMENTE le foto che mostrano solo volti o primi piani di persone (es. ritratti di politici, giornalisti o intervistati).
   - ECCEZIONE: Puoi includere foto di persone/volti SOLO se l'articolo appartiene palesemente alle rubriche "Moda", "Spettacoli" o "Cultura".
   - IGNORA COMPLETAMENTE le pubblicità, i loghi decorativi e i contenuti non giornalistici.
   - Quando associ un'immagine (foto/grafico/mappa) a un articolo, devi restituire il suo bounding box nel formato [ymin, xmin, ymax, xmax] espresso in valori normalizzati da 0 a 1000 rispetto all'intera pagina.
   - Il bounding box [0,0,1000,1000] indica l'intera pagina. Calcola le coordinate esatte dell'immagine all'interno della pagina.

3. Per ogni articolo, estrai:
   - "title": il titolo principale dell'articolo (OBBLIGATORIO)
   - "subtitle": il sottotitolo, sommario o occhiello (OBBLIGATORIO se presente, stringa vuota se assente)
   - "body": il testo completo dell'articolo, trascritto fedelmente (OBBLIGATORIO)
   - "category": la sezione/rubrica (es. "Economia", "Cronaca", "Esteri") — spesso indicata nell'intestazione della pagina
   - "page": il numero di pagina (se visibile nell'immagine)
   - "isHighlight": true se l'articolo è uno dei pezzi principali/di apertura
   - "media": array di oggetti { type: "photo" | "chart" | "map", caption: "didascalia o breve descrizione", box: [ymin, xmin, ymax, xmax], page: numero_di_pagina }. Il campo "page" DEVE corrispondere al numero di pagina in cui si trova l'immagine (es. 2). Inserisci qui foto, grafici e mappe pertinenti all'articolo. Se non ce ne sono, ometti il campo.

3. NON duplicare articoli: se un articolo della prima pagina viene ripreso nelle pagine interne con più testo, crea UN SOLO articolo usando il testo più completo delle pagine interne, ma mantenendo il titolo più prominente.

4. IGNORA completamente: pubblicità, inserzioni, avvisi legali, indici, numeri di pagina, intestazioni ripetute del giornale, informazioni editoriali, necrologi, annunci.

5. ATTENZIONE alle COLONNE: non mescolare il testo di colonne diverse che appartengono ad articoli diversi. Usa la posizione visiva e le separazioni grafiche (linee, filetti, spazi bianchi) per capire i confini tra articoli.

6. Restituisci SOLO un JSON valido (senza markdown code blocks, senza commenti) con questa struttura esatta:
{
  "newspaperName": "Nome del giornale (leggilo dalla testata in prima pagina)",
  "date": "YYYY-MM-DD (leggila dalla prima pagina)",
  "articles": [
    {
      "id": "art-1",
      "title": "...",
      "subtitle": "...",
      "body": "...",
      "category": "...",
      "page": 1,
      "isHighlight": false
    }
  ]
}

7. Ordina gli articoli per importanza (highlights prima, poi per ordine di apparizione nel giornale).

Analizza ora le immagini delle pagine del giornale fornite e restituisci il JSON.`;

/**
 * Calls the Antigravity CLI (agy) with page images to extract articles via Gemini Vision.
 * Uses --print to run non-interactively, piping the prompt via stdin.
 */
import { statSync } from 'fs';

function getPageNum(p: string): number {
  const m = path.basename(p).match(/\d+/);
  return m ? parseInt(m[0], 10) : 1;
}

export async function extractArticles(imagePaths: string[], onProgress?: (msg: string) => void, originalFileName: string = ''): Promise<ExtractionResult> {
  const agyPath = await findAgyPath();
  const batches: string[][] = [];
  
  const isSole24Ore = originalFileName.toLowerCase().includes('sole 24 ore') || originalFileName.toLowerCase().includes('sole24ore');

  if (isSole24Ore) {
    console.log('📰 Rilevato "Sole 24 Ore": applicazione logica di suddivisione speciale (blocchi da 1 pagina SENZA overlap, pag 2-3 unite).');
    let i = 0;
    while (i < imagePaths.length) {
      const pageNum = getPageNum(imagePaths[i]);
      if (pageNum === 2) {
        // Find page 3 if it exists
        const p2 = imagePaths[i];
        let nextIndex = i + 1;
        const batch = [p2];
        if (nextIndex < imagePaths.length && getPageNum(imagePaths[nextIndex]) === 3) {
          batch.push(imagePaths[nextIndex]);
          nextIndex++;
        }
        batches.push(batch);
        i = nextIndex;
      } else {
        const batch = [imagePaths[i]];
        batches.push(batch);
        i++;
      }
    }
  } else {
    const MAX_BATCH_SIZE_BYTES = 5 * 1024 * 1024; // 5 MB
    let currentBatch: string[] = [];
    let currentBatchSize = 0;

    for (let i = 0; i < imagePaths.length; i++) {
      const p = imagePaths[i];
      const size = statSync(p).size;
      
      // Se aggiungendo questa pagina superiamo i 5MB e il batch ha ALMENO 2 pagine
      if (currentBatchSize + size > MAX_BATCH_SIZE_BYTES && currentBatch.length >= 2) {
        batches.push([...currentBatch]);
        // Nuovo blocco: inizia con l'ultima pagina del blocco precedente (sovrapposizione)
        const lastPage = currentBatch[currentBatch.length - 1];
        const lastPageSize = statSync(lastPage).size;
        
        currentBatch = [lastPage, p];
        currentBatchSize = lastPageSize + size;
      } else {
        currentBatch.push(p);
        currentBatchSize += size;
      }
    }
    if (currentBatch.length > 0) {
      batches.push([...currentBatch]);
    }
  }

  console.log(`   Pagine totali: ${imagePaths.length}, diviso in ${batches.length} blocchi.`);
  
  const workDir = path.join(__dirname, '..', '..', 'page-images');
  let startBatch = 0;
  
  for (let b = 0; b < batches.length; b++) {
    const batchFile = path.join(workDir, `batch_${b}.json`);
    if (existsSync(batchFile)) {
      startBatch = b + 1;
    } else {
      break;
    }
  }

  if (startBatch > 0 && startBatch < batches.length) {
    console.log(`   Ripresa estrazione dal blocco ${startBatch + 1}...`);
  }

  for (let b = startBatch; b < batches.length; b++) {
    const batchImages = batches[b];
    if (onProgress) {
      onProgress(`Analisi blocco ${b + 1} di ${batches.length} (${batchImages.length} pagine)...`);
    }

    const startPageNum = getPageNum(batchImages[0]);
    const endPageNum = getPageNum(batchImages[batchImages.length - 1]);

    const imageRefs = batchImages.map(p => `![Pagina ${getPageNum(p)}](${p})`).join('\n\n');
    const fullPrompt = `${EXTRACTION_PROMPT}\n\n---\n\nATTENZIONE: Stai analizzando il blocco ${b + 1} di ${batches.length} del giornale. Le pagine incluse in questo blocco sono le pagine da ${startPageNum} a ${endPageNum}.\n\nLe pagine del giornale:\n\n${imageRefs}`;
    
    const promptFile = path.join(workDir, `_prompt_${b}.md`);
    writeFileSync(promptFile, fullPrompt, 'utf-8');

    try {
      console.log(`   Analizzando blocco ${b + 1}/${batches.length}...`);
      const result = await new Promise<{ stdout: string; stderr: string }>((resolve, reject) => {
        import('child_process').then(({ spawn }) => {
          const agyProcess = spawn(agyPath, ['--model', 'Gemini 3.8 Flash (High)', '--dangerously-skip-permissions'], {
            env: { ...process.env },
          });

          const readStream = createReadStream(promptFile);
          readStream.pipe(agyProcess.stdin);

          let stdout = '';
          let stderr = '';
          let timeoutHandle: NodeJS.Timeout;

          agyProcess.stdout.on('data', (data) => {
            const chunk = data.toString();
            stdout += chunk;
            
            if (onProgress) {
               const currentBatchArticles = (stdout.match(/"title"\s*:/g) || []).length;
               onProgress(`Analisi blocco ${b + 1}/${batches.length}... [Articoli parziali trovati nel blocco: ${currentBatchArticles}]`);
            }
          });

          agyProcess.stderr.on('data', (data) => {
            stderr += data.toString();
          });

          agyProcess.on('close', (code) => {
            clearTimeout(timeoutHandle);
            if (code !== 0 && code !== null) {
              console.error(`\n[AGY EXEC ERROR BLOCCO ${b + 1}]`);
              console.error(`Code: ${code}`);
              console.error(`STDOUT:\n${stdout.substring(0, 1000)}`);
              console.error(`STDERR:\n${stderr.substring(0, 1000)}\n`);
              reject(new Error(`agy fallito con codice ${code}.\nStderr: ${stderr}`));
            } else {
              resolve({ stdout, stderr });
            }
          });

          agyProcess.on('error', (err) => {
            clearTimeout(timeoutHandle);
            reject(err);
          });

          timeoutHandle = setTimeout(() => {
            agyProcess.kill('SIGKILL');
            reject(new Error(`Timeout: l'elaborazione del blocco ${b + 1} ha impiegato troppo tempo (possibile interruzione di rete).`));
          }, 10 * 60 * 1000);
        }).catch(reject);
      });

      try {
        const batchJson = extractJsonFromResponse(result.stdout);
        const batchFile = path.join(workDir, `batch_${b}.json`);
        writeFileSync(batchFile, JSON.stringify(batchJson, null, 2), 'utf-8');
      } catch (parseErr) {
        console.warn(`   ⚠️ Errore parsing JSON per il blocco ${b + 1}:`, parseErr);
        throw parseErr;
      }
    } finally {
      try {
        unlinkSync(promptFile);
      } catch {
        // Ignore cleanup errors
      }
    }
  }

  let allArticles: any[] = [];
  let newspaperName = 'Sconosciuto';
  let date = new Date().toISOString().split('T')[0];

  for (let b = 0; b < batches.length; b++) {
    const batchFile = path.join(workDir, `batch_${b}.json`);
    if (existsSync(batchFile)) {
      const data = JSON.parse(readFileSync(batchFile, 'utf-8'));
      if (b === 0) {
        newspaperName = data.newspaperName || newspaperName;
        date = data.date || date;
      }
      allArticles.push(...(data.articles || []));
      try { unlinkSync(batchFile); } catch {}
    }
  }

  const stateFile = path.join(workDir, 'state.json');
  if (existsSync(stateFile)) {
    try { unlinkSync(stateFile); } catch {}
  }

  const mergedMap = new Map<string, any>();
  for (const article of allArticles) {
    const key = article.title.toLowerCase().trim();
    const existing = mergedMap.get(key);
    if (!existing || ((article.body?.length || 0) > (existing.body?.length || 0))) {
      mergedMap.set(key, article);
    }
  }

  const uniqueArticles = Array.from(mergedMap.values());

  return {
    newspaperName,
    date,
    articles: uniqueArticles.map((a, i) => ({ ...a, id: `art-${i + 1}` }))
  };
}

/**
 * Find the agy CLI binary path.
 */
async function findAgyPath(): Promise<string> {
  const { execFile } = await import('child_process');
  const { promisify } = await import('util');
  const execFileAsync = promisify(execFile);

  try {
    const { stdout } = await execFileAsync('which', ['agy']);
    return stdout.trim();
  } catch {
    throw new Error(
      'Comando "agy" non trovato. Assicurati che Antigravity CLI sia installato e nel PATH.\n' +
      'Installazione: https://antigravity.dev'
    );
  }
}

/**
 * Extract valid JSON from the AI response, handling markdown code blocks.
 */
function extractJsonFromResponse(response: string): ExtractionResult {
  let cleaned = response.trim();

  // Remove markdown code blocks if present
  const jsonBlockMatch = cleaned.match(/```(?:json)?\s*\n?([\s\S]*?)\n?\s*```/);
  if (jsonBlockMatch) {
    cleaned = jsonBlockMatch[1].trim();
  }

  const jsonStart = cleaned.indexOf('{');
  if (jsonStart === -1) {
    throw new Error('Nessun JSON trovato nella risposta dell\'AI. Risposta ricevuta:\n' + cleaned.substring(0, 500));
  }

  const candidates = [
    cleaned.substring(jsonStart),
    cleaned.substring(jsonStart, cleaned.lastIndexOf('}') + 1)
  ];

  let parsed: any = null;

  for (let candidate of candidates) {
    try {
      parsed = JSON.parse(candidate);
      break;
    } catch (e) {
      try {
        parsed = repairJSON(candidate);
        break;
      } catch (repairErr) {
        continue;
      }
    }
  }

  if (!parsed) {
    throw new Error('JSON non valido nella risposta dell\'AI. Potrebbe essere necessario riprovare.');
  }

  if (!parsed.newspaperName || !parsed.date || !Array.isArray(parsed.articles)) {
    parsed.newspaperName = parsed.newspaperName || 'Sconosciuto';
    parsed.date = parsed.date || new Date().toISOString().split('T')[0];
    parsed.articles = Array.isArray(parsed.articles) ? parsed.articles : [];
  }

  parsed.articles = parsed.articles.map((article: Record<string, unknown>, index: number) => ({
    id: article.id || `art-${index + 1}`,
    title: article.title || 'Senza titolo',
    subtitle: article.subtitle || '',
    body: article.body || '',
    category: article.category || undefined,
    page: typeof article.page === 'number' ? article.page : undefined,
    isHighlight: Boolean(article.isHighlight),
    media: Array.isArray(article.media) ? article.media : undefined,
  }));

  return parsed as ExtractionResult;
}

function repairJSON(str: string): any {
  let current = str.trim();
  const stringCount = (current.match(/(?<!\\)"/g) || []).length;
  if (stringCount % 2 !== 0) {
    current += '"';
  }
  
  const suffixes = ['', '}', ']}', '}]}', '}}]}'];
  
  for (const suffix of suffixes) {
    try {
      return JSON.parse(current + suffix);
    } catch (e) {}
  }
  
  const lastComma = current.lastIndexOf(',');
  if (lastComma !== -1) {
    let truncated = current.substring(0, lastComma);
    for (const suffix of suffixes) {
      try {
        return JSON.parse(truncated + suffix);
      } catch (e) {}
    }
  }
  
  throw new Error("Cannot repair JSON");
}
