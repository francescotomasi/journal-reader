import express from 'express';
import cors from 'cors';
import { fileURLToPath } from 'url';
import path from 'path';
import { uploadRouter } from './routes/upload.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3001;

// CORS — allow frontend dev server
app.use(
  cors({
    origin: ['http://localhost:5173', 'http://localhost:3000', 'http://127.0.0.1:5173'],
    methods: ['GET', 'POST'],
  })
);

app.use(express.json());

// Request logging
app.use((req, _res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
});

// Ensure temp directories exist
import { mkdirSync } from 'fs';
const uploadsDir = path.join(__dirname, '..', 'uploads');
const pageImagesDir = path.join(__dirname, '..', 'page-images');
mkdirSync(uploadsDir, { recursive: true });
mkdirSync(pageImagesDir, { recursive: true });

// Routes
app.use('/api', uploadRouter);

// Health check
app.get('/api/health', (_req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`\n📰 Journal Reader Backend`);
  console.log(`   Server attivo su http://localhost:${PORT}`);
  console.log(`   Health check: http://localhost:${PORT}/api/health\n`);
});
