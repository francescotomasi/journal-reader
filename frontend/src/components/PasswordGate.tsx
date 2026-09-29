import { useState, useEffect } from 'react';

const PASSWORD_KEY = 'journal_reader_auth';
const CORRECT_PASSWORD = 'giornale2026';

interface PasswordGateProps {
  children: React.ReactNode;
}

export default function PasswordGate({ children }: PasswordGateProps) {
  const [authenticated, setAuthenticated] = useState(false);
  const [password, setPassword] = useState('');
  const [error, setError] = useState(false);
  const [checking, setChecking] = useState(true);

  useEffect(() => {
    const stored = localStorage.getItem(PASSWORD_KEY);
    if (stored === 'true') {
      setAuthenticated(true);
    }
    setChecking(false);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (password === CORRECT_PASSWORD) {
      localStorage.setItem(PASSWORD_KEY, 'true');
      setAuthenticated(true);
      setError(false);
    } else {
      setError(true);
    }
  };

  if (checking) return null;

  if (authenticated) {
    return <>{children}</>;
  }

  return (
    <div
      style={{
        backgroundColor: 'var(--color-paper)',
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '1rem',
      }}
    >
      <form
        onSubmit={handleSubmit}
        style={{ width: '100%', maxWidth: '360px', textAlign: 'center' }}
      >
        <div
          style={{
            width: '3rem',
            height: '3rem',
            borderRadius: '50%',
            backgroundColor: 'var(--color-paper-warm)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            margin: '0 auto 1.5rem',
            fontSize: '1.5rem',
          }}
        >
          🔒
        </div>
        <h1
          style={{
            fontFamily: 'var(--font-display)',
            fontSize: '1.8rem',
            fontWeight: 700,
            color: 'var(--color-ink)',
            marginBottom: '0.5rem',
          }}
        >
          Rassegna Giornali
        </h1>
        <p
          style={{
            fontFamily: 'var(--font-sans)',
            fontSize: '0.9rem',
            color: 'var(--color-ink-muted)',
            marginBottom: '2rem',
          }}
        >
          Inserisci la password per accedere
        </p>
        <input
          type="password"
          className="password-input"
          value={password}
          onChange={(e) => {
            setPassword(e.target.value);
            setError(false);
          }}
          placeholder="Password"
          autoFocus
          style={{ marginBottom: '1rem' }}
        />
        {error && (
          <p
            style={{
              fontFamily: 'var(--font-sans)',
              fontSize: '0.8rem',
              color: 'var(--color-accent)',
              marginBottom: '1rem',
            }}
          >
            Password non corretta
          </p>
        )}
        <button type="submit" className="btn-primary">
          Accedi →
        </button>
      </form>
    </div>
  );
}
