import simpleGit from 'simple-git';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const REPO_ROOT = path.join(__dirname, '..', '..', '..'); // journal_reader/

/**
 * Commits and pushes the updated journal data to GitHub.
 */
export async function gitPush(newspaperName: string, date: string): Promise<void> {
  const git = simpleGit(REPO_ROOT);

  // Check if this is a git repo
  const isRepo = await git.checkIsRepo();
  if (!isRepo) {
    throw new Error('La directory del progetto non è un repository Git.');
  }

  // Stage the frontend data files
  const dataPath = path.join('frontend', 'public', 'data', 'journals');
  await git.add(dataPath);

  // Check if there are changes to commit
  const status = await git.status();
  if (status.staged.length === 0) {
    console.log('   Nessuna modifica da committare.');
    return;
  }

  // Commit
  const commitMessage = `📰 Aggiunto giornale: ${newspaperName} - ${date}`;
  await git.commit(commitMessage);
  console.log(`   Commit: "${commitMessage}"`);

  // Push
  try {
    await git.push('origin', 'main');
  } catch {
    // Try 'master' branch if 'main' fails
    try {
      await git.push('origin', 'master');
    } catch (pushErr) {
      throw new Error(
        `Push fallito. Verifica che il remote "origin" sia configurato.\nErrore: ${pushErr instanceof Error ? pushErr.message : pushErr}`
      );
    }
  }
}
