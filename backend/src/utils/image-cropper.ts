import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

/**
 * Crop an image using normalized [ymin, xmin, ymax, xmax] coordinates (0-1000)
 */
export async function cropImage(
  sourcePath: string,
  destPath: string,
  box: [number, number, number, number]
): Promise<void> {
  if (!fs.existsSync(sourcePath)) {
    throw new Error(`Source image not found: ${sourcePath}`);
  }

  const [ymin, xmin, ymax, xmax] = box;
  
  // Validate coordinates
  if (ymin < 0 || xmin < 0 || ymax > 1000 || xmax > 1000 || ymin >= ymax || xmin >= xmax) {
    throw new Error(`Invalid bounding box: ${box}`);
  }

  const metadata = await sharp(sourcePath).metadata();
  const width = metadata.width || 0;
  const height = metadata.height || 0;

  if (width === 0 || height === 0) {
    throw new Error('Could not read image dimensions');
  }

  const left = Math.floor((xmin / 1000) * width);
  const top = Math.floor((ymin / 1000) * height);
  const extractWidth = Math.floor(((xmax - xmin) / 1000) * width);
  const extractHeight = Math.floor(((ymax - ymin) / 1000) * height);

  // Ensure crop is within bounds
  const safeLeft = Math.max(0, left);
  const safeTop = Math.max(0, top);
  const safeWidth = Math.min(extractWidth, width - safeLeft);
  const safeHeight = Math.min(extractHeight, height - safeTop);

  // Ensure directory exists
  fs.mkdirSync(path.dirname(destPath), { recursive: true });

  await sharp(sourcePath)
    .extract({ left: safeLeft, top: safeTop, width: safeWidth, height: safeHeight })
    .webp({ quality: 80 })
    .toFile(destPath);
}
