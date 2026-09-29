import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

interface ArticleData {
  id: string;
  title: string;
  subtitle: string;
  body: string;
  category?: string;
  page?: number;
  isHighlight: boolean;
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
 */
export async function saveJournal(extraction: ExtractionResult): Promise<string> {
  // Ensure data directory exists
  mkdirSync(FRONTEND_DATA_DIR, { recursive: true });

  // Generate journal ID from name and date
  const slugName = extraction.newspaperName
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
  const journalId = `${extraction.date}_${slugName}`;
  const fileName = `${journalId}.json`;

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
