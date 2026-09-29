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

2. Per ogni articolo, estrai:
   - "title": il titolo principale dell'articolo (OBBLIGATORIO)
   - "subtitle": il sottotitolo, sommario o occhiello (OBBLIGATORIO se presente, stringa vuota se assente)
   - "body": il testo completo dell'articolo, trascritto fedelmente (OBBLIGATORIO)
   - "category": la sezione/rubrica (es. "Economia", "Cronaca", "Esteri") — spesso indicata nell'intestazione della pagina
   - "page": il numero di pagina (se visibile nell'immagine)
   - "isHighlight": true se l'articolo è uno dei pezzi principali/di apertura

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
export async function extractArticles(imagePaths: string[], onProgress?: (msg: string) => void): Promise<ExtractionResult> {
  const agyPath = await findAgyPath();
  const BATCH_SIZE = 8;
  const batches = [];
  
  for (let i = 0; i < imagePaths.length; i += BATCH_SIZE) {
    batches.push(imagePaths.slice(i, i + BATCH_SIZE));
  }

  console.log(`   Pagine totali: ${imagePaths.length}, diviso in ${batches.length} blocchi.`);
  
  let allArticles: any[] = [];
  let newspaperName = 'Sconosciuto';
  let date = new Date().toISOString().split('T')[0];
  let startBatch = 0;

  const stateFile = path.join(__dirname, '..', '..', 'page-images', 'state.json');
  if (existsSync(stateFile)) {
    try {
      const state = JSON.parse(readFileSync(stateFile, 'utf-8'));
      startBatch = state.completedBatches || 0;
      allArticles = state.allArticles || [];
      newspaperName = state.newspaperName || newspaperName;
      date = state.date || date;
      console.log(`   Ripresa estrazione dal blocco ${startBatch + 1}...`);
    } catch (e) {
      console.warn("   ⚠️ Impossibile leggere state.json, ricomincio da capo.");
    }
  }

  let totalArticlesFound = allArticles.length;

  for (let b = startBatch; b < batches.length; b++) {
    const batchImages = batches[b];
    if (onProgress) {
      onProgress(`Analisi blocco ${b + 1} di ${batches.length} (${batchImages.length} pagine)... [Articoli totali finora: ${totalArticlesFound}]`);
    }

    const imageRefs = batchImages.map((p, i) => `![Pagina ${i + 1 + (b * BATCH_SIZE)}](${p})`).join('\n\n');
    const fullPrompt = `${EXTRACTION_PROMPT}\n\n---\n\nATTENZIONE: Stai analizzando il blocco ${b + 1} di ${batches.length} del giornale. Le pagine incluse in questo blocco sono le pagine da ${1 + (b * BATCH_SIZE)} a ${batchImages.length + (b * BATCH_SIZE)}.\n\nLe pagine del giornale:\n\n${imageRefs}`;
    
    const promptFile = path.join(__dirname, '..', '..', 'page-images', `_prompt_${b}.md`);
    writeFileSync(promptFile, fullPrompt, 'utf-8');

    try {
      console.log(`   Analizzando blocco ${b + 1}/${batches.length}...`);
      const result = await new Promise<{ stdout: string; stderr: string }>((resolve, reject) => {
        import('child_process').then(({ spawn }) => {
          const agyProcess = spawn(agyPath, ['--model', 'Gemini 3.1 Pro (High)', '--dangerously-skip-permissions'], {
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
               onProgress(`Analisi blocco ${b + 1}/${batches.length}... [Articoli trovati: ${totalArticlesFound + currentBatchArticles}]`);
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

          // Timeout in case the network hangs (e.g. sleep mode)
          timeoutHandle = setTimeout(() => {
            agyProcess.kill('SIGKILL');
            reject(new Error(`Timeout: l'elaborazione del blocco ${b + 1} ha impiegato troppo tempo (possibile interruzione di rete).`));
          }, 10 * 60 * 1000); // 10 minutes timeout per batch
        }).catch(reject);
      });

      try {
        const batchJson = extractJsonFromResponse(result.stdout);
        
        if (b === 0 || newspaperName === 'Sconosciuto') {
          newspaperName = batchJson.newspaperName || newspaperName;
          date = batchJson.date || date;
        }

        allArticles.push(...batchJson.articles);
        totalArticlesFound = allArticles.length;

        // Save progress state
        writeFileSync(stateFile, JSON.stringify({
          completedBatches: b + 1,
          allArticles,
          newspaperName,
          date
        }), 'utf-8');

      } catch (parseErr) {
        console.warn(`   ⚠️ Errore parsing JSON per il blocco ${b + 1}:`, parseErr);
        throw parseErr; // Throw to trigger outer catch and avoid marking block as completed
      }
    } finally {
      try {
        unlinkSync(promptFile);
      } catch {
        // Ignore cleanup errors
      }
    }
  }

  // Se è arrivato alla fine senza errori, elimina il file di stato
  if (existsSync(stateFile)) {
    try {
      unlinkSync(stateFile);
    } catch {}
  }

  // Rimuovi duplicati (stesso titolo esatto)
  const uniqueArticles = allArticles.filter((article, index, self) =>
    index === self.findIndex((a) => a.title.toLowerCase().trim() === article.title.toLowerCase().trim())
  );

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

  // Try to find the JSON object directly
  const jsonStart = cleaned.indexOf('{');
  const jsonEnd = cleaned.lastIndexOf('}');

  if (jsonStart === -1 || jsonEnd === -1) {
    throw new Error('Nessun JSON trovato nella risposta dell\'AI. Risposta ricevuta:\n' + cleaned.substring(0, 500));
  }

  cleaned = cleaned.substring(jsonStart, jsonEnd + 1);

  try {
    const parsed = JSON.parse(cleaned);

    if (!parsed.newspaperName || !parsed.date || !Array.isArray(parsed.articles)) {
      throw new Error('Il JSON restituito non ha la struttura attesa (newspaperName, date, articles).');
    }

    parsed.articles = parsed.articles.map((article: Record<string, unknown>, index: number) => ({
      id: article.id || `art-${index + 1}`,
      title: article.title || 'Senza titolo',
      subtitle: article.subtitle || '',
      body: article.body || '',
      category: article.category || undefined,
      page: typeof article.page === 'number' ? article.page : undefined,
      isHighlight: Boolean(article.isHighlight),
    }));

    return parsed as ExtractionResult;
  } catch (err) {
    if (err instanceof SyntaxError) {
      throw new Error('JSON non valido nella risposta dell\'AI. Potrebbe essere necessario riprovare.\nErrore: ' + err.message);
    }
    throw err;
  }
}
