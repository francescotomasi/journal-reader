import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// GitHub Pages deploys to https://<user>.github.io/<repo>/
// Set base to '/<repo-name>/' for GitHub Pages, or '/' for custom domains
const base = process.env.GITHUB_ACTIONS ? '/journal-reader/' : '/';

export default defineConfig({
  base,
  plugins: [react()],
  server: {
    port: 5173,
    host: true,
  },
});
