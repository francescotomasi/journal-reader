import { Link } from 'react-router-dom';
import { useLatestJournal, isLocalhost } from '../hooks/useJournals';
import { useScrollRestoration } from '../hooks/useScrollRestoration';
import type { Article } from '../types/article';

export default function Home() {
  const { journal, loading, error, hasJournals } = useLatestJournal();
  
  useScrollRestoration(loading);

  if (loading) {
    return (
      <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <p style={{ fontFamily: 'var(--font-sans)', color: 'var(--color-ink-muted)' }}>Caricamento...</p>
      </div>
    );
  }

  if (error || !hasJournals || !journal) {
    return (
      <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '2rem', textAlign: 'center' }}>
        <p style={{ fontFamily: 'var(--font-display)', fontSize: '1.5rem', fontWeight: 700, color: 'var(--color-ink)', marginBottom: '0.75rem' }}>
          Nessun giornale caricato
        </p>
        <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.9rem', color: 'var(--color-ink-muted)', marginBottom: '2rem' }}>
          Carica il primo giornale per iniziare la tua rassegna stampa.
        </p>
        {isLocalhost() && (
          <Link to="/upload" className="btn-primary" style={{ maxWidth: '280px', textDecoration: 'none' }}>
            Carica giornale →
          </Link>
        )}
      </div>
    );
  }

  const highlights = journal.articles.filter((a) => a.isHighlight);
  const others = journal.articles.filter((a) => !a.isHighlight);
  const categories = [...new Set(journal.articles.map((a) => a.category).filter(Boolean))] as string[];

  return (
    <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh' }}>
      {/* Masthead */}
      <header style={{ borderBottom: '3px solid var(--color-ink)' }}>
        <div className="max-w-4xl mx-auto px-4 pb-4" style={{ paddingTop: 'max(2rem, env(safe-area-inset-top, 2rem))' }}>
          <div className="text-center" style={{ borderBottom: '1px solid var(--color-rule)', paddingBottom: '0.75rem', marginBottom: '0.5rem' }}>
            <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.7rem', letterSpacing: '0.15em', textTransform: 'uppercase', color: 'var(--color-ink-muted)' }}>
              {new Date(journal.date).toLocaleDateString('it-IT', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
            </p>
          </div>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(2.4rem, 8vw, 4.5rem)', fontWeight: 900, lineHeight: 1, textAlign: 'center', letterSpacing: '-0.02em', color: 'var(--color-ink)' }}>
            {journal.name}
          </h1>
          <div className="text-center mt-2" style={{ borderTop: '1px solid var(--color-rule)', paddingTop: '0.5rem' }}>
            <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.7rem', letterSpacing: '0.12em', textTransform: 'uppercase', color: 'var(--color-ink-muted)' }}>
              Rassegna Stampa
            </p>
          </div>
        </div>

        {/* Category nav */}
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
        {/* Action bar */}
        <div className="flex justify-between items-center" style={{ marginBottom: '1.5rem' }}>
          <Link to="/archivio" style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', color: 'var(--color-accent)', textDecoration: 'none' }}>
            📚 Archivio
          </Link>
          {isLocalhost() && (
            <Link to="/upload" style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', color: 'var(--color-accent)', textDecoration: 'none' }}>
              📤 Carica giornale
            </Link>
          )}
        </div>

        {/* Highlight articles */}
        {highlights.length > 0 && (
          <div style={{ borderBottom: '1px solid var(--color-rule)', paddingBottom: '2rem', marginBottom: '2rem' }}>
            {highlights.map((article, i) => (
              <HighlightCard key={article.id} article={article} journalId={journal.id} isFirst={i === 0} />
            ))}
          </div>
        )}

        {/* Other articles */}
        <div className="flex flex-col gap-0">
          {others.map((article, i) => (
            <Link
              key={article.id}
              to={`/articolo/${journal.id}/${article.id}`}
              className="block py-5"
              style={{ borderBottom: i < others.length - 1 ? '1px solid var(--color-rule)' : 'none', textDecoration: 'none' }}
            >
              {article.category && <CategoryLabel category={article.category} />}
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '1.15rem', fontWeight: 700, lineHeight: 1.3, color: 'var(--color-ink)', marginTop: '0.3rem', marginBottom: '0.3rem' }}>
                {article.title}
              </h3>
              {article.subtitle && (
                <p style={{ fontFamily: 'var(--font-body)', fontSize: '0.87rem', lineHeight: 1.5, color: 'var(--color-ink-muted)', marginBottom: '0.4rem' }}>
                  {article.subtitle}
                </p>
              )}
              {article.page && (
                <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.72rem', color: 'var(--color-ink-faint)' }}>
                  Pagina {article.page}
                </p>
              )}
            </Link>
          ))}
        </div>
      </main>

      {/* Footer */}
      <footer style={{ borderTop: '3px solid var(--color-ink)', marginTop: '3rem', padding: '2rem 1rem', textAlign: 'center' }}>
        <p style={{ fontFamily: 'var(--font-display)', fontSize: '1.2rem', fontWeight: 700, color: 'var(--color-ink)', marginBottom: '0.25rem' }}>
          {journal.name}
        </p>
        <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.72rem', letterSpacing: '0.08em', color: 'var(--color-ink-muted)' }}>
          Rassegna generata automaticamente
        </p>
      </footer>
    </div>
  );
}

function HighlightCard({ article, journalId, isFirst }: { article: Article; journalId: string; isFirst: boolean }) {
  return (
    <Link
      to={`/articolo/${journalId}/${article.id}`}
      className="block"
      style={{ marginBottom: isFirst ? '1.5rem' : '0', textDecoration: 'none' }}
    >
      {article.category && <CategoryLabel category={article.category} />}
      <h2 style={{ fontFamily: 'var(--font-display)', fontSize: isFirst ? 'clamp(1.6rem, 5vw, 2.6rem)' : '1.25rem', fontWeight: 700, lineHeight: 1.2, color: 'var(--color-ink)', marginTop: '0.5rem', marginBottom: '0.6rem' }}>
        {article.title}
      </h2>
      {article.subtitle && (
        <p style={{ fontFamily: 'var(--font-body)', fontSize: isFirst ? '1.05rem' : '0.9rem', lineHeight: 1.6, color: 'var(--color-ink-muted)', marginBottom: '0.5rem' }}>
          {article.subtitle}
        </p>
      )}
      {article.page && (
        <p style={{ fontFamily: 'var(--font-sans)', fontSize: '0.72rem', color: 'var(--color-ink-faint)' }}>
          Pagina {article.page}
        </p>
      )}
    </Link>
  );
}

function CategoryLabel({ category }: { category: string }) {
  return (
    <span style={{ fontFamily: 'var(--font-sans)', fontSize: '0.65rem', fontWeight: 600, letterSpacing: '0.14em', textTransform: 'uppercase', color: 'var(--color-accent)' }}>
      {category}
    </span>
  );
}
