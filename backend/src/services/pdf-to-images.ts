import { fromPath } from 'pdf2pic';
import path from 'path';
import { fileURLToPath } from 'url';
import { readdirSync, rmSync, existsSync } from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const pageImagesDir = path.join(__dirname, '..', '..', 'page-images');

/**
 * Converts each page of a PDF into a PNG image at high resolution.
 * Returns an array of absolute paths to the generated images.
 */
export async function convertPdfToImages(pdfPath: string): Promise<string[]> {
  // Clean up old images
  if (existsSync(pageImagesDir)) {
    const oldFiles = readdirSync(pageImagesDir).filter((f) => f.endsWith('.png'));
    for (const f of oldFiles) {
      rmSync(path.join(pageImagesDir, f), { force: true });
    }
  }

  const converter = fromPath(pdfPath, {
    density: 200, // DPI — good balance between quality and file size
    saveFilename: 'page',
    savePath: pageImagesDir,
    format: 'png',
    width: 2000, // Pixel width — enough for multi-column newspaper text
    height: 2800,
  });

  // First, get the number of pages by converting page 1 and checking
  // pdf2pic's bulk method to convert all pages
  const results = await converter.bulk(-1, { responseType: 'image' });

  const imagePaths: string[] = [];
  for (const result of results) {
    if (result.path) {
      imagePaths.push(result.path);
    }
  }

  if (imagePaths.length === 0) {
    throw new Error('Nessuna pagina estratta dal PDF. Verifica che il file sia un PDF valido.');
  }

  // Sort by page number
  imagePaths.sort((a, b) => {
    const numA = parseInt(path.basename(a).match(/\d+/)?.[0] || '0');
    const numB = parseInt(path.basename(b).match(/\d+/)?.[0] || '0');
    return numA - numB;
  });

  return imagePaths;
}
