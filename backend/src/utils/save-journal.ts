import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { cropImage } from './image-cropper.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

interface ArticleMedia {
  type: 'photo' | 'chart' | 'map';
  caption: string;
  box?: [number, number, number, number];
  page?: number;
  url?: string;
}

interface ArticleData {
  id: string;
  title: string;
  subtitle: string;
  body: string;
  category?: string;
  page?: number;
  isHighlight: boolean;
  media?: ArticleMedia[];
}

interface ExtractionResult {
  newspaperName: string;
  date: string;
  articles: ArticleData[];
}

interface JournalIndexEntry {
  id: string;
  name: string;
  date: string;
  articleCount: number;
  file: string;
}

interface JournalIndex {
  journals: JournalIndexEntry[];
}

const FRONTEND_DATA_DIR = path.join(__dirname, '..', '..', '..', 'frontend', 'public', 'data', 'journals');

/**
 * Saves extracted journal data to the frontend's public data directory.
 * Updates the index.json file with the new entry.
 * Also crops requested media images and saves them in the public directory.
 */
export async function saveJournal(extraction: ExtractionResult, imagePaths: string[] = []): Promise<string> {
  // Ensure data directory exists
  mkdirSync(FRONTEND_DATA_DIR, { recursive: true });

  // Generate journal ID from name and date
  const slugName = extraction.newspaperName
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
  const journalId = `${extraction.date}_${slugName}`;
  const fileName = `${journalId}.json`;
  const imagesDirName = `${journalId}_images`;
  const imagesDirPath = path.join(FRONTEND_DATA_DIR, imagesDirName);

  // Process media and crop images
  for (const article of extraction.articles) {
    if (article.media && article.media.length > 0) {
      for (let i = 0; i < article.media.length; i++) {
        const media = article.media[i];
        if (media.box && media.page && typeof media.page === 'number') {
          // Identify the source image. page is 1-indexed.
          const sourcePath = imagePaths.find(p => {
             const m = path.basename(p).match(/\d+/);
             return m && parseInt(m[0], 10) === media.page;
          }) || imagePaths[media.page - 1];

          if (sourcePath && existsSync(sourcePath)) {
            const imageName = `${article.id}_media_${i}.webp`;
            const destPath = path.join(imagesDirPath, imageName);
            try {
              await cropImage(sourcePath, destPath, media.box);
              // Set the public URL relative to frontend
              media.url = `data/journals/${imagesDirName}/${imageName}`;
            } catch (err) {
              console.warn(`   ⚠️ Errore ritaglio immagine per articolo ${article.id}:`, err);
            }
          }
        }
      }
    }
  }

  // Build the journal JSON
  const journal = {
    id: journalId,
    name: extraction.newspaperName,
    date: extraction.date,
    extractedAt: new Date().toISOString(),
    articles: extraction.articles,
  };

  // Save journal file
  const journalPath = path.join(FRONTEND_DATA_DIR, fileName);
  writeFileSync(journalPath, JSON.stringify(journal, null, 2), 'utf-8');
  console.log(`   Salvato: ${journalPath}`);

  // Update index.json
  const indexPath = path.join(FRONTEND_DATA_DIR, 'index.json');
  let index: JournalIndex = { journals: [] };

  if (existsSync(indexPath)) {
    try {
      const raw = readFileSync(indexPath, 'utf-8');
      index = JSON.parse(raw);
    } catch {
      console.warn('   ⚠️  index.json corrotto, ricreato da zero');
      index = { journals: [] };
    }
  }

  // Remove existing entry with same ID (overwrite)
  index.journals = index.journals.filter((j) => j.id !== journalId);

  // Add new entry at the beginning (newest first)
  index.journals.unshift({
    id: journalId,
    name: extraction.newspaperName,
    date: extraction.date,
    articleCount: extraction.articles.length,
    file: fileName,
  });

  // Sort by date descending
  index.journals.sort((a, b) => b.date.localeCompare(a.date));

  // Save index
  writeFileSync(indexPath, JSON.stringify(index, null, 2), 'utf-8');
  console.log(`   Indice aggiornato: ${index.journals.length} giornali`);

  return journalId;
}
