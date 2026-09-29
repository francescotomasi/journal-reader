# 📰 Journal Reader — Rassegna Stampa Personale

App web privata per estrarre e leggere articoli da quotidiani italiani in PDF.
Carica un PDF → l'AI estrae gli articoli → leggili in un layout giornalistico su iPhone.

---

## Requisiti

- **Node.js** v18+
- **GraphicsMagick + Ghostscript** (per il backend, conversione PDF → immagini):
  ```bash
  brew install graphicsmagick ghostscript
  ```
- **Antigravity CLI** (`agy`) installato e nel PATH (per l'estrazione AI)

---

## Avvio Rapido

### 1. Frontend (Rassegna Stampa)
```bash
cd frontend
npm install
npm run dev
```
Apri **http://localhost:5173/** nel browser.

**Password:** `giornale2026`

Da **iPhone** sulla stessa rete Wi-Fi: `http://192.168.1.251:5173/`

### 2. Backend (Upload e Estrazione AI)
```bash
cd backend
npm install
npm run dev
```
Il server parte su **http://localhost:3001**

### 3. Caricare un Giornale
1. Apri http://localhost:5173/upload
2. Trascina o seleziona un PDF di un quotidiano italiano
3. Attendi l'estrazione AI (Gemini Pro Vision via `agy`)
4. Gli articoli appariranno nella home page
5. Il risultato viene automaticamente pushato su GitHub

---

## Struttura del Progetto

```
journal_reader/
├── frontend/                   # PWA React (Vite + TypeScript)
│   ├── src/
│   │   ├── components/
│   │   │   └── PasswordGate.tsx    # 🔒 Gate password
│   │   ├── pages/
│   │   │   ├── Home.tsx            # 📰 Ultimo giornale
│   │   │   ├── Upload.tsx          # 📤 Carica PDF (solo localhost)
│   │   │   ├── Archive.tsx         # 📚 Archivio edizioni passate
│   │   │   └── Article.tsx         # 📖 Lettore articolo
│   │   ├── hooks/
│   │   │   └── useJournals.ts      # Hook per dati JSON
│   │   └── types/
│   │       └── article.ts          # Interfacce TypeScript
│   └── public/data/journals/       # JSON dei giornali estratti
│
├── backend/                    # Server Node.js (Express)
│   └── src/
│       ├── server.ts               # Server porta 3001
│       ├── routes/upload.ts        # POST /api/upload
│       ├── services/
│       │   ├── pdf-to-images.ts    # PDF → PNG (200 DPI)
│       │   └── ai-extractor.ts     # agy + Gemini Pro Vision
│       └── utils/
│           ├── save-journal.ts     # Salva JSON nel frontend
│           └── git-push.ts         # Auto push su GitHub
│
└── design/                     # Design Figma di riferimento
```

---

## Come Funziona

```
PDF Upload → Conversione Pagine in PNG → Gemini Pro Vision (via agy)
    → Estrazione Articoli (titolo, sottotitolo, testo) → JSON
    → Frontend Rassegna Stampa → Git Push → iPhone via GitHub Pages
```

L'approccio **Vision** è fondamentale: i quotidiani italiani usano layout multi-colonna
(5-6 colonne per pagina). L'estrazione di testo puro perde l'informazione spaziale.
Convertendo le pagine in immagini, Gemini Pro Vision "vede" il layout come un lettore umano.

---

## Deploy su GitHub Pages (per iPhone)

```bash
cd frontend
npm run build
# Copia il contenuto di dist/ nel branch gh-pages
```

---

## Comandi Utili

| Comando | Descrizione |
|---|---|
| `cd frontend && npm run dev` | Avvia frontend di sviluppo |
| `cd frontend && npm run build` | Build di produzione |
| `cd backend && npm run dev` | Avvia backend locale |
| `cd backend && npm run build` | Compila TypeScript |
