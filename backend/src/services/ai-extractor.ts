import { exec } from 'child_process';
import { writeFileSync, unlinkSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

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
export async function extractArticles(imagePaths: string[]): Promise<ExtractionResult> {
  const imageRefs = imagePaths
    .map((p, i) => `![Pagina ${i + 1}](${p})`)
    .join('\n\n');

  const fullPrompt = `${EXTRACTION_PROMPT}\n\n---\n\nLe pagine del giornale:\n\n${imageRefs}`;

  // Write prompt to a temp file (too long for command line args)
  const promptFile = path.join(__dirname, '..', '..', 'page-images', '_prompt.md');
  writeFileSync(promptFile, fullPrompt, 'utf-8');

  try {
    const agyPath = await findAgyPath();

    console.log(`   Usando agy: ${agyPath}`);
    console.log(`   Pagine da analizzare: ${imagePaths.length}`);

    // Pipe the prompt file directly into agy via stdin.
    // --dangerously-skip-permissions to run non-interactively without prompting
    const command = `cat "${promptFile}" | ${agyPath} --model "Gemini 3.8 Flash (High)" --dangerously-skip-permissions`;

    const result = await new Promise<{ stdout: string; stderr: string }>((resolve, reject) => {
      exec(command, {
        timeout: 10 * 60 * 1000, // 10 minutes for large newspapers
        maxBuffer: 50 * 1024 * 1024, // 50 MB buffer
        env: { ...process.env },
      }, (error, stdout, stderr) => {
        if (error) {
          console.error(`\n[AGY EXEC ERROR]`);
          console.error(`Code: ${error.code}`);
          console.error(`Message: ${error.message}`);
          console.error(`STDOUT:\n${stdout.substring(0, 1000)}`);
          console.error(`STDERR:\n${stderr.substring(0, 1000)}\n`);
          reject(new Error(`agy fallito con codice ${error.code}.\nMessage: ${error.message}\nStderr: ${stderr}`));
        } else {
          resolve({ stdout, stderr });
        }
      });
    });

    if (result.stderr) {
      console.warn('   agy stderr:', result.stderr.substring(0, 500));
    }

    const jsonResult = extractJsonFromResponse(result.stdout);
    return jsonResult;
  } finally {
    try {
      unlinkSync(promptFile);
    } catch {
      // Ignore cleanup errors
    }
  }
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
