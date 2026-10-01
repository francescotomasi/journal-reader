import { Link, useParams } from 'react-router-dom';
import { useJournalIndex, useJournal } from '../hooks/useJournals';
import { isLocalhost } from '../hooks/useJournals';
import { useScrollRestoration } from '../hooks/useScrollRestoration';

export default function Archive() {
  const { journalId } = useParams<{ journalId: string }>();

  if (journalId) {
    return <JournalDetail journalId={journalId} />;
  }

  return <ArchiveList />;
}

function ArchiveList() {
  const { index, loading, error } = useJournalIndex();
  
  useScrollRestoration(loading);

  if (loading) {
    return (
      <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <p style={{ fontFamily: 'var(--font-sans)', color: 'var(--color-ink-muted)' }}>Caricamento...</p>
      </div>
    );
  }

  return (
    <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh' }}>
      <div className="max-w-4xl mx-auto px-4" style={{ paddingTop: 'max(2rem, env(safe-area-inset-top, 2rem))' }}>
        {/* Header */}
        <Link to="/" style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', color: 'var(--color-ink-muted)', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '0.3rem', marginBottom: '2rem' }}>
          ← Torna alla rassegna
        </Link>

        <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(2rem, 6vw, 3rem)', fontWeight: 900, color: 'var(--color-ink)', marginBottom: '0.5rem' }}>
          Archivio
        </h1>
        <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.9rem', color: 'var(--color-ink-muted)', marginBottom: '2rem', borderBottom: '1px solid var(--color-rule)', paddingBottom: '1.5rem' }}>
          Tutte le edizioni dei giornali analizzati
        </p>

        {error && (
          <p style={{ fontFamily: 'var(--font-sans)', color: 'var(--color-accent)' }}>{error}</p>
        )}

        {index.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '3rem 1rem' }}>
            <p style={{ fontFamily: 'var(--font-display)', fontSize: '1.2rem', color: 'var(--color-ink-muted)', marginBottom: '1rem' }}>
              Nessun giornale nell'archivio
            </p>
            {isLocalhost() && (
              <Link to="/upload" className="btn-primary" style={{ maxWidth: '280px', margin: '0 auto', textDecoration: 'none' }}>
                Carica il primo giornale →
              </Link>
            )}
          </div>
        ) : (
          <div className="flex flex-col gap-0">
            {index.map((entry, i) => (
              <Link
                key={entry.id}
                to={`/archivio/${entry.id}`}
                className="block py-5"
                style={{ borderBottom: i < index.length - 1 ? '1px solid var(--color-rule)' : 'none', textDecoration: 'none' }}
              >
                <div className="flex justify-between items-start">
                  <div>
                    <h2 style={{ fontFamily: 'var(--font-display)', fontSize: '1.25rem', fontWeight: 700, color: 'var(--color-ink)', marginBottom: '0.25rem' }}>
                      {entry.name}
                    </h2>
                    <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.85rem', color: 'var(--color-ink-muted)' }}>
                      {new Date(entry.date).toLocaleDateString('it-IT', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })}
                    </p>
                  </div>
                  <span style={{ fontFamily: 'var(--font-sans)', fontSize: '0.75rem', color: 'var(--color-ink-faint)', backgroundColor: 'var(--color-paper-warm)', padding: '0.25rem 0.6rem', borderRadius: '1rem', whiteSpace: 'nowrap' }}>
                    {entry.articleCount} articoli
                  </span>
                </div>
              </Link>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function JournalDetail({ journalId }: { journalId: string }) {
  const { journal, loading, error } = useJournal(journalId);
  
  useScrollRestoration(loading);

  if (loading) {
    return (
      <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <p style={{ fontFamily: 'var(--font-sans)', color: 'var(--color-ink-muted)' }}>Caricamento...</p>
      </div>
    );
  }

  if (error || !journal) {
    return (
      <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '1rem' }}>
        <p style={{ fontFamily: 'var(--font-display)', fontSize: '1.5rem', color: 'var(--color-ink)' }}>
          Giornale non trovato.
        </p>
        <Link to="/archivio" style={{ fontFamily: 'var(--font-sans)', fontSize: '0.9rem', color: 'var(--color-accent)', textDecoration: 'none' }}>
          ← Torna all'archivio
        </Link>
      </div>
    );
  }

  const categories = [...new Set(journal.articles.map((a) => a.category).filter(Boolean))] as string[];

  return (
    <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh' }}>
      {/* Masthead */}
      <header style={{ borderBottom: '3px solid var(--color-ink)' }}>
        <div className="max-w-4xl mx-auto px-4 pb-4" style={{ paddingTop: 'max(2rem, env(safe-area-inset-top, 2rem))' }}>
          <Link to="/archivio" style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', color: 'var(--color-ink-muted)', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '0.3rem', marginBottom: '1rem' }}>
            ← Archivio
          </Link>
          <div className="text-center" style={{ borderBottom: '1px solid var(--color-rule)', paddingBottom: '0.75rem', marginBottom: '0.5rem' }}>
            <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.7rem', letterSpacing: '0.15em', textTransform: 'uppercase', color: 'var(--color-ink-muted)' }}>
              {new Date(journal.date).toLocaleDateString('it-IT', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
            </p>
          </div>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(2rem, 7vw, 3.5rem)', fontWeight: 900, lineHeight: 1, textAlign: 'center', letterSpacing: '-0.02em', color: 'var(--color-ink)' }}>
            {journal.name}
          </h1>
        </div>

        {categories.length > 0 && (
          <nav style={{ backgroundColor: 'var(--color-ink)' }}>
            <div className="max-w-4xl mx-auto px-4">
              <ul className="flex gap-0 overflow-x-auto">
                {categories.map((cat) => (
                  <li key={cat}>
                    <span style={{ display: 'block', padding: '0.55rem 0.9rem', fontFamily: 'var(--font-sans)', fontSize: '0.72rem', letterSpacing: '0.1em', textTransform: 'uppercase', color: 'var(--color-paper)', whiteSpace: 'nowrap' }}>
                      {cat}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          </nav>
        )}
      </header>

      <main className="max-w-4xl mx-auto px-4 py-6">
        <div className="flex flex-col gap-0">
          {journal.articles.map((article, i) => (
            <Link
              key={article.id}
              to={`/articolo/${journal.id}/${article.id}`}
              className="block py-5"
              style={{ borderBottom: i < journal.articles.length - 1 ? '1px solid var(--color-rule)' : 'none', textDecoration: 'none' }}
            >
              {article.category && (
                <span style={{ fontFamily: 'var(--font-sans)', fontSize: '0.65rem', fontWeight: 600, letterSpacing: '0.14em', textTransform: 'uppercase', color: 'var(--color-accent)' }}>
                  {article.category}
                </span>
              )}
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: article.isHighlight ? '1.4rem' : '1.15rem', fontWeight: 700, lineHeight: 1.3, color: 'var(--color-ink)', marginTop: '0.3rem', marginBottom: '0.3rem' }}>
                {article.title}
              </h3>
              {article.subtitle && (
                <p style={{ fontFamily: 'var(--font-body)', fontSize: '0.87rem', lineHeight: 1.5, color: 'var(--color-ink-muted)' }}>
                  {article.subtitle}
                </p>
              )}
            </Link>
          ))}
        </div>
      </main>
    </div>
  );
}
