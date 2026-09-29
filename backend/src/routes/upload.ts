import { Router } from 'express';
import multer from 'multer';
import path from 'path';
import { fileURLToPath } from 'url';
import { convertPdfToImages } from '../services/pdf-to-images.js';
import { extractArticles } from '../services/ai-extractor.js';
import { saveJournal } from '../utils/save-journal.js';
import { gitPush } from '../utils/git-push.js';
import { cleanupUploads } from '../utils/cleanup-uploads.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const uploadsDir = path.join(__dirname, '..', '..', 'uploads');

const storage = multer.diskStorage({
  destination: uploadsDir,
  filename: (_req, file, cb) => {
    const uniqueName = `${Date.now()}-${file.originalname}`;
    cb(null, uniqueName);
  },
});

const upload = multer({
  storage,
  limits: { fileSize: 25 * 1024 * 1024 }, // 25 MB
  fileFilter: (_req, file, cb) => {
    if (file.mimetype === 'application/pdf') {
      cb(null, true);
    } else {
      cb(new Error('Solo file PDF sono accettati.'));
    }
  },
});

export const uploadRouter = Router();

uploadRouter.post('/upload', upload.single('pdf'), async (req, res) => {
  const file = req.file;
  if (!file) {
    res.status(400).json({ error: 'Nessun file caricato.' });
    return;
  }

  console.log(`\n📄 PDF ricevuto: ${file.originalname} (${(file.size / 1024 / 1024).toFixed(1)} MB)`);

  // Set headers for streaming status updates
  res.setHeader('Content-Type', 'application/x-ndjson');
  res.setHeader('Transfer-Encoding', 'chunked');

  const sendStatus = (status: string, extra?: Record<string, unknown>) => {
    res.write(JSON.stringify({ status, ...extra }) + '\n');
  };

  try {
    // Step 0: Cleanup old uploads if over 500 MB
    cleanupUploads(uploadsDir);

    // Step 1: Convert PDF to images
    sendStatus('converting');
    console.log('🖼️  Conversione pagine in immagini...');
    const imagePaths = await convertPdfToImages(file.path);
    console.log(`   ✅ ${imagePaths.length} pagine convertite`);

    // Step 2: Extract articles via AI
    sendStatus('extracting');
    console.log('🤖 Estrazione AI in corso...');
    const extractionResult = await extractArticles(imagePaths);
    console.log(`   ✅ ${extractionResult.articles.length} articoli estratti`);

    // Step 3: Save to frontend data directory
    sendStatus('saving');
    console.log('💾 Salvataggio dati...');
    const journalId = await saveJournal(extractionResult);
    console.log(`   ✅ Salvato come ${journalId}`);

    // Step 4: Git push
    sendStatus('pushing');
    console.log('📤 Push su GitHub...');
    try {
      await gitPush(extractionResult.newspaperName, extractionResult.date);
      console.log('   ✅ Push completato');
    } catch (gitErr) {
      console.warn('   ⚠️  Git push fallito (non critico):', gitErr instanceof Error ? gitErr.message : gitErr);
    }

    // Done
    sendStatus('done', {
      journalId,
      articleCount: extractionResult.articles.length,
      newspaperName: extractionResult.newspaperName,
    });
    console.log(`\n✅ Elaborazione completata: ${extractionResult.articles.length} articoli da "${extractionResult.newspaperName}"\n`);

    res.end();
  } catch (err) {
    console.error('❌ Errore durante l\'elaborazione:', err);
    sendStatus('error', { error: err instanceof Error ? err.message : 'Errore sconosciuto' });
    res.end();
  }
});
