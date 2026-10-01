import { Link, useParams, useNavigate } from 'react-router-dom';
import { useJournal } from '../hooks/useJournals';
import { useEffect } from 'react';

export default function ArticlePage() {
  const { journalId, articleId } = useParams<{ journalId: string; articleId: string }>();
  const { journal, loading, error } = useJournal(journalId);
  const navigate = useNavigate();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [articleId]);

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
          Articolo non trovato.
        </p>
        <button onClick={() => navigate(-1)} style={{ fontFamily: 'var(--font-sans)', fontSize: '0.9rem', color: 'var(--color-accent)', background: 'none', border: 'none', cursor: 'pointer' }}>
          ← Torna indietro
        </button>
      </div>
    );
  }

  const currentIndex = journal.articles.findIndex((a) => a.id === articleId);
  const article = journal.articles[currentIndex];

  if (!article) {
    return (
      <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '1rem' }}>
        <p style={{ fontFamily: 'var(--font-display)', fontSize: '1.5rem', color: 'var(--color-ink)' }}>
          Articolo non trovato.
        </p>
        <button onClick={() => navigate(-1)} style={{ fontFamily: 'var(--font-sans)', fontSize: '0.9rem', color: 'var(--color-accent)', background: 'none', border: 'none', cursor: 'pointer' }}>
          ← Torna indietro
        </button>
      </div>
    );
  }

  const prevArticle = currentIndex > 0 ? journal.articles[currentIndex - 1] : null;
  const nextArticle = currentIndex < journal.articles.length - 1 ? journal.articles[currentIndex + 1] : null;

  const paragraphs = article.body.split('\n\n').filter((p) => p.trim().length > 0);

  return (
    <div style={{ backgroundColor: 'var(--color-paper)', minHeight: '100vh' }}>
      {/* Sticky top bar */}
      <div style={{ borderBottom: '1px solid var(--color-rule)', backgroundColor: 'var(--color-paper)', position: 'sticky', top: 0, zIndex: 50 }}>
        <div className="max-w-3xl mx-auto px-4 py-3 flex items-center justify-between">
          <button
            onClick={() => navigate(-1)}
            style={{ fontFamily: 'var(--font-sans)', fontSize: '0.75rem', letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--color-ink-muted)', display: 'flex', alignItems: 'center', gap: '0.4rem', background: 'none', border: 'none', cursor: 'pointer' }}
          >
            <span style={{ fontSize: '0.9rem' }}>←</span> Indietro
          </button>
          <Link
            to="/"
            style={{ fontFamily: 'var(--font-display)', fontSize: '1.1rem', fontWeight: 900, color: 'var(--color-ink)', textDecoration: 'none' }}
          >
            {journal.name}
          </Link>
          <div style={{ width: '80px' }} />
        </div>
      </div>

      <article className="max-w-3xl mx-auto px-4 py-8">
        {article.category && (
          <div style={{ marginBottom: '0.75rem' }}>
            <span style={{ fontFamily: 'var(--font-sans)', fontSize: '0.68rem', fontWeight: 600, letterSpacing: '0.16em', textTransform: 'uppercase', color: 'var(--color-accent)', borderBottom: '2px solid var(--color-accent)', paddingBottom: '2px' }}>
              {article.category}
            </span>
          </div>
        )}

        <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(1.8rem, 6vw, 3rem)', fontWeight: 700, lineHeight: 1.15, color: 'var(--color-ink)', marginBottom: '0.75rem' }}>
          {article.title}
        </h1>

        {article.subtitle && (
          <p style={{ fontFamily: 'var(--font-body)', fontSize: 'clamp(1rem, 2.5vw, 1.2rem)', fontStyle: 'italic', lineHeight: 1.55, color: 'var(--color-ink-muted)', marginBottom: '1.25rem', borderLeft: '3px solid var(--color-rule)', paddingLeft: '1rem' }}>
            {article.subtitle}
          </p>
        )}

        <div style={{ borderTop: '1px solid var(--color-rule)', borderBottom: '1px solid var(--color-rule)', padding: '0.75rem 0', marginBottom: '1.75rem', display: 'flex', flexWrap: 'wrap', gap: '0.5rem', alignItems: 'center', justifyContent: 'space-between' }}>
          {article.page && (
            <span style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', fontWeight: 600, color: 'var(--color-ink)' }}>
              Pagina {article.page}
            </span>
          )}
          <span style={{ fontFamily: 'var(--font-sans)', fontSize: '0.76rem', color: 'var(--color-ink-faint)' }}>
            {new Date(journal.date).toLocaleDateString('it-IT', { day: 'numeric', month: 'long', year: 'numeric' })}
          </span>
        </div>

        <div
          className="article-body"
          style={{ fontFamily: 'var(--font-body)', fontSize: 'clamp(1rem, 2.5vw, 1.1rem)', color: 'var(--color-ink)', maxWidth: '65ch', marginLeft: 'auto', marginRight: 'auto' }}
        >
          {article.media && article.media.length > 0 && (
            <div style={{ marginBottom: '2rem' }}>
              {article.media.map((m, i) => m.url && (
                <figure key={i} style={{ margin: '0 0 1.5rem 0' }}>
                  <img src={`${import.meta.env.BASE_URL}${m.url}`} alt={m.caption || ''} style={{ width: '100%', height: 'auto', display: 'block', borderRadius: '4px', border: '1px solid var(--color-rule)' }} />
                  {m.caption && (
                    <figcaption style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', color: 'var(--color-ink-muted)', marginTop: '0.5rem', textAlign: 'center' }}>
                      {m.caption}
                    </figcaption>
                  )}
                </figure>
              ))}
            </div>
          )}

          {paragraphs.map((text, i) => (
            <p key={i}>{text}</p>
          ))}
        </div>

        {/* Navigation Footer */}
        <div style={{ borderTop: '3px double var(--color-rule)', marginTop: '3rem', paddingTop: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', gap: '1rem', flexWrap: 'wrap' }}>
            {prevArticle ? (
              <Link
                to={`/articolo/${journal.id}/${prevArticle.id}`}
                style={{ flex: 1, textDecoration: 'none', minWidth: '200px' }}
                replace
              >
                <div style={{ fontFamily: 'var(--font-sans)', fontSize: '0.7rem', textTransform: 'uppercase', color: 'var(--color-ink-muted)', marginBottom: '0.25rem' }}>
                  ← Precedente
                </div>
                <div style={{ fontFamily: 'var(--font-display)', fontSize: '1.1rem', fontWeight: 700, color: 'var(--color-ink)' }}>
                  {prevArticle.title}
                </div>
              </Link>
            ) : <div style={{ flex: 1 }} />}

            {nextArticle ? (
              <Link
                to={`/articolo/${journal.id}/${nextArticle.id}`}
                style={{ flex: 1, textDecoration: 'none', textAlign: 'right', minWidth: '200px' }}
                replace
              >
                <div style={{ fontFamily: 'var(--font-sans)', fontSize: '0.7rem', textTransform: 'uppercase', color: 'var(--color-ink-muted)', marginBottom: '0.25rem' }}>
                  Successivo →
                </div>
                <div style={{ fontFamily: 'var(--font-display)', fontSize: '1.1rem', fontWeight: 700, color: 'var(--color-ink)' }}>
                  {nextArticle.title}
                </div>
              </Link>
            ) : <div style={{ flex: 1 }} />}
          </div>
          
          <div style={{ textAlign: 'center', marginTop: '2.5rem' }}>
            <button
              onClick={() => navigate(-1)}
              style={{ fontFamily: 'var(--font-sans)', fontSize: '0.8rem', letterSpacing: '0.1em', textTransform: 'uppercase', color: 'var(--color-ink-muted)', background: 'none', border: 'none', cursor: 'pointer' }}
            >
              ← Torna all'elenco
            </button>
          </div>
        </div>
      </article>
    </div>
  );
}
