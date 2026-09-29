import { useState, useRef, useCallback, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { isLocalhost } from '../hooks/useJournals';

type UploadStatus = 'idle' | 'uploading' | 'converting' | 'extracting' | 'saving' | 'done' | 'error';

const STATUS_MESSAGES: Record<UploadStatus, string> = {
  idle: '',
  uploading: 'Caricamento del PDF...',
  converting: 'Conversione delle pagine in immagini...',
  extracting: 'Analisi AI in corso — lettura del giornale...',
  saving: 'Salvataggio degli articoli...',
  done: 'Estrazione completata!',
  error: 'Si è verificato un errore.',
};

export default function Upload() {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState<UploadStatus>('idle');
  const [extractProgress, setExtractProgress] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [dragover, setDragover] = useState(false);
  const [articleCount, setArticleCount] = useState(0);
  const [canResume, setCanResume] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const isLocal = isLocalhost();

  useEffect(() => {
    if (isLocal) {
      fetch('http://localhost:3001/api/status')
        .then(res => res.json())
        .then(data => {
          if (data.canResume) setCanResume(true);
        })
        .catch(() => {});
    }
  }, [isLocal]);

  const handleFileChange = useCallback((selectedFile: File | null) => {
    if (selectedFile && selectedFile.type === 'application/pdf') {
      if (selectedFile.size > 25 * 1024 * 1024) {
        setErrorMessage('Il file supera il limite di 25 MB.');
        return;
      }
      setFile(selectedFile);
      setErrorMessage('');
      setExtractProgress('');
      setStatus('idle');
    } else if (selectedFile) {
      setErrorMessage('Seleziona un file PDF valido.');
    }
  }, []);

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      setDragover(false);
      const droppedFile = e.dataTransfer.files[0];
      handleFileChange(droppedFile);
    },
    [handleFileChange]
  );

  const handleSubmit = async () => {
    if (!file) return;

    try {
      setStatus('uploading');
      setExtractProgress('');
      const formData = new FormData();
      formData.append('pdf', file);

      const res = await fetch('http://localhost:3001/api/upload', {
        method: 'POST',
        body: formData,
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({ error: 'Errore del server' }));
        throw new Error(data.error || 'Errore del server');
      }

      // Poll for status updates via SSE or just wait for the response
      const reader = res.body?.getReader();
      const decoder = new TextDecoder();

      if (reader) {
        let result = '';
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          result += decoder.decode(value, { stream: true });

          // Try to parse status updates
          const lines = result.split('\n').filter((l) => l.trim());
          for (const line of lines) {
            try {
              const update = JSON.parse(line);
              if (update.status === 'extracting_progress') {
                setExtractProgress(update.message);
              } else if (update.status) {
                setStatus(update.status as UploadStatus);
              }
              if (update.articleCount) setArticleCount(update.articleCount);
              if (update.error) {
                setErrorMessage(update.error);
                setStatus('error');
                return;
              }
            } catch {
              // Not JSON yet, continue
            }
          }
          // Clear processed lines from buffer
          result = '';
        }
      }

      setStatus('done');
    } catch (err) {
      setErrorMessage(err instanceof Error ? err.message : 'Errore sconosciuto');
      setStatus('error');
    }
  };

  const handleResume = async () => {
    try {
      setStatus('extracting');
      setExtractProgress('Ripresa estrazione interrotta...');
      setCanResume(false);

      const res = await fetch('http://localhost:3001/api/resume', {
        method: 'POST',
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({ error: 'Errore del server' }));
        throw new Error(data.error || 'Errore del server');
      }

      const reader = res.body?.getReader();
      const decoder = new TextDecoder();

      if (reader) {
        let result = '';
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          result += decoder.decode(value, { stream: true });

          const lines = result.split('\n').filter((l) => l.trim());
          for (const line of lines) {
            try {
              const update = JSON.parse(line);
              if (update.status === 'extracting_progress') {
                setExtractProgress(update.message);
              } else if (update.status) {
                setStatus(update.status as UploadStatus);
              }
              if (update.articleCount) setArticleCount(update.articleCount);
              if (update.error) {
                setErrorMessage(update.error);
                setStatus('error');
                return;
              }
            } catch {}
          }
          result = '';
        }
      }

      setStatus('done');
    } catch (err) {
      setErrorMessage(err instanceof Error ? err.message : 'Errore sconosciuto');
      setStatus('error');
    }
  };

  if (!isLocal) {
    return (
      <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '2rem', textAlign: 'center' }}>
        <p style={{ fontFamily: 'var(--font-display)', fontSize: '1.5rem', fontWeight: 700, color: 'var(--color-ink)', marginBottom: '0.75rem' }}>
          Caricamento non disponibile
        </p>
        <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.9rem', color: 'var(--color-ink-muted)', marginBottom: '2rem' }}>
          Il caricamento dei giornali è disponibile solo dalla versione locale dell'app.
        </p>
        <Link to="/" style={{ fontFamily: 'var(--font-sans)', fontSize: '0.9rem', color: 'var(--color-accent)', textDecoration: 'none' }}>
          ← Torna alla rassegna
        </Link>
      </div>
    );
  }

  return (
    <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh' }}>
      <div className="max-w-md mx-auto px-4" style={{ paddingTop: 'max(3rem, env(safe-area-inset-top, 3rem))' }}>
        {/* Back link */}
        <Link to="/" style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', color: 'var(--color-ink-muted)', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '0.3rem', marginBottom: '2rem' }}>
          ← Torna alla rassegna
        </Link>

        {/* Dot accent */}
        <div style={{ width: '0.6rem', height: '0.6rem', borderRadius: '50%', backgroundColor: 'var(--color-accent)', marginBottom: '0.75rem' }} />

        {/* Title */}
        <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(2rem, 7vw, 3rem)', fontWeight: 700, lineHeight: 1.1, color: 'var(--color-ink)', marginBottom: '0.75rem' }}>
          Carica il tuo giornale.
        </h1>
        <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.95rem', lineHeight: 1.5, color: 'var(--color-ink-muted)', marginBottom: '3rem' }}>
          Il tuo file resta privato. Viene usato solo per importare gli articoli e non viene mai condiviso.
        </p>

        {/* Upload area */}
        <div
          className={`upload-area ${dragover ? 'dragover' : ''}`}
          onDragOver={(e) => { e.preventDefault(); setDragover(true); }}
          onDragLeave={() => setDragover(false)}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
          style={{ padding: '3rem 2rem', textAlign: 'center', cursor: 'pointer', marginBottom: '0.75rem' }}
        >
          <input
            ref={fileInputRef}
            type="file"
            accept=".pdf"
            onChange={(e) => handleFileChange(e.target.files?.[0] || null)}
            style={{ display: 'none' }}
          />

          <div style={{ width: '3.5rem', height: '3.5rem', borderRadius: '50%', backgroundColor: 'var(--color-paper-warm)', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 1.25rem', fontSize: '1.5rem' }}>
            📄
          </div>

          <p style={{ fontFamily: 'var(--font-display)', fontSize: '1.2rem', fontWeight: 600, color: 'var(--color-ink)', marginBottom: '0.3rem' }}>
            {file ? file.name : 'Scegli il file del giornale'}
          </p>
          <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.85rem', color: 'var(--color-ink-muted)', marginBottom: '1rem' }}>
            {file
              ? `${(file.size / 1024 / 1024).toFixed(1)} MB`
              : 'Tocca per sfogliare o trascinalo qui'}
          </p>

          {!file && (
            <span style={{ display: 'inline-block', padding: '0.4rem 1.2rem', borderRadius: '0.5rem', backgroundColor: 'var(--color-paper-warm)', fontFamily: 'var(--font-sans)', fontSize: '0.85rem', fontWeight: 500, color: 'var(--color-ink-muted)' }}>
              Seleziona file
            </span>
          )}
        </div>

        <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.75rem', color: 'var(--color-ink-faint)', display: 'flex', alignItems: 'center', gap: '0.4rem', marginBottom: '1.5rem' }}>
          📎 PDF · massimo 25 MB
        </p>

        {/* Status messages */}
        {status !== 'idle' && (
          <div style={{ marginBottom: '1rem', padding: '0.75rem 1rem', borderRadius: '0.5rem', backgroundColor: status === 'error' ? '#fef2f2' : status === 'done' ? '#f0fdf4' : 'var(--color-paper-warm)' }}>
            <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.85rem', color: status === 'error' ? 'var(--color-accent)' : status === 'done' ? '#166534' : 'var(--color-ink-muted)' }}>
              {status === 'error' ? errorMessage : STATUS_MESSAGES[status]}
            </p>
            {status === 'extracting' && extractProgress && (
              <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', color: 'var(--color-ink-muted)', marginTop: '0.25rem', fontStyle: 'italic' }}>
                {extractProgress}
              </p>
            )}
            {status === 'done' && articleCount > 0 && (
              <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', color: '#166534', marginTop: '0.25rem' }}>
                {articleCount} articoli estratti con successo.
              </p>
            )}
          </div>
        )}

        {errorMessage && status === 'idle' && (
          <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', color: 'var(--color-accent)', marginBottom: '1rem' }}>
            {errorMessage}
          </p>
        )}

        {/* Submit button */}
        {status !== 'done' ? (
          <button
            className="btn-primary"
            onClick={handleSubmit}
            disabled={!file || (status !== 'idle' && status !== 'error')}
          >
            {status !== 'idle' && status !== 'error' ? STATUS_MESSAGES[status] : 'Carica giornale →'}
          </button>
        ) : (
          <Link to="/" className="btn-primary" style={{ textDecoration: 'none' }}>
            Vai alla rassegna →
          </Link>
        )}
      </div>
    </div>
  );
}
