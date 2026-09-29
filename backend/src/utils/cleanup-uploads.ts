import fs from 'fs';
import path from 'path';

const MAX_UPLOADS_BYTES = 500 * 1024 * 1024; // 500 MB

interface FileInfo {
  name: string;
  path: string;
  size: number;
  mtimeMs: number;
}

/**
 * Checks the /uploads directory size and deletes the oldest files
 * until total size is under the MAX_UPLOADS_BYTES limit.
 */
export function cleanupUploads(uploadsDir: string): void {
  if (!fs.existsSync(uploadsDir)) return;

  const files: FileInfo[] = fs
    .readdirSync(uploadsDir)
    .filter((f) => !f.startsWith('.'))
    .map((name) => {
      const filePath = path.join(uploadsDir, name);
      const stat = fs.statSync(filePath);
      return {
        name,
        path: filePath,
        size: stat.size,
        mtimeMs: stat.mtimeMs,
      };
    })
    .filter((f) => fs.statSync(f.path).isFile());

  let totalSize = files.reduce((sum, f) => sum + f.size, 0);

  if (totalSize <= MAX_UPLOADS_BYTES) {
    console.log(`   📦 Uploads: ${(totalSize / 1024 / 1024).toFixed(1)} MB / ${MAX_UPLOADS_BYTES / 1024 / 1024} MB — OK`);
    return;
  }

  // Sort oldest first
  files.sort((a, b) => a.mtimeMs - b.mtimeMs);

  let deleted = 0;
  for (const file of files) {
    if (totalSize <= MAX_UPLOADS_BYTES) break;

    try {
      fs.unlinkSync(file.path);
      totalSize -= file.size;
      deleted++;
      console.log(`   🗑️  Eliminato PDF vecchio: ${file.name} (${(file.size / 1024 / 1024).toFixed(1)} MB)`);
    } catch (err) {
      console.warn(`   ⚠️  Impossibile eliminare ${file.name}:`, err);
    }
  }

  if (deleted > 0) {
    console.log(`   📦 Pulizia completata: eliminati ${deleted} file, ora ${(totalSize / 1024 / 1024).toFixed(1)} MB`);
  }
}
