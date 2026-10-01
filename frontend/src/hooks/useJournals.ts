import { useState, useEffect, useCallback } from 'react';
import type { Journal, JournalIndex, JournalIndexEntry } from '../types/article';

const BASE_URL = import.meta.env.BASE_URL || '/';

// Simple in-memory cache to prevent re-fetching on back navigation
const indexCache: { data: JournalIndexEntry[] | null; timestamp: number } = { data: null, timestamp: 0 };
const journalCache: Record<string, { data: Journal | null; timestamp: number }> = {};
const CACHE_TTL = 1000 * 60 * 5; // 5 minutes

export function useJournalIndex() {
  const [index, setIndex] = useState<JournalIndexEntry[]>(indexCache.data || []);
  const [loading, setLoading] = useState(!indexCache.data);
  const [error, setError] = useState<string | null>(null);

  const refresh = useCallback(async (force = false) => {
    if (!force && indexCache.data && Date.now() - indexCache.timestamp < CACHE_TTL) {
      setIndex(indexCache.data);
      setLoading(false);
      return;
    }

    try {
      if (!indexCache.data) setLoading(true);
      const res = await fetch(`${BASE_URL}data/journals/index.json`);
      if (!res.ok) throw new Error('Impossibile caricare l\'indice dei giornali');
      const data: JournalIndex = await res.json();
      indexCache.data = data.journals;
      indexCache.timestamp = Date.now();
      setIndex(data.journals);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Errore sconosciuto');
      setIndex([]);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { refresh(); }, [refresh]);

  return { index, loading, error, refresh };
}

export function useJournal(journalId: string | undefined) {
  const cachedJournal = journalId ? journalCache[journalId]?.data : null;
  const [journal, setJournal] = useState<Journal | null>(cachedJournal || null);
  const [loading, setLoading] = useState(journalId ? !cachedJournal : false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!journalId) {
      setLoading(false);
      return;
    }

    const load = async () => {
      if (journalCache[journalId]?.data && Date.now() - journalCache[journalId].timestamp < CACHE_TTL) {
        setJournal(journalCache[journalId].data);
        setLoading(false);
        return;
      }

      try {
        if (!journalCache[journalId]?.data) setLoading(true);
        const res = await fetch(`${BASE_URL}data/journals/${journalId}.json`);
        if (!res.ok) throw new Error('Giornale non trovato');
        const data: Journal = await res.json();
        journalCache[journalId] = { data, timestamp: Date.now() };
        setJournal(data);
        setError(null);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Errore sconosciuto');
        setJournal(null);
      } finally {
        setLoading(false);
      }
    };

    load();
  }, [journalId]);

  return { journal, loading, error };
}

export function useLatestJournal() {
  const { index, loading: indexLoading, error: indexError } = useJournalIndex();
  const latestId = index.length > 0 ? index[0].id : undefined;
  const { journal, loading: journalLoading, error: journalError } = useJournal(latestId);

  return {
    journal,
    loading: indexLoading || journalLoading,
    error: indexError || journalError,
    hasJournals: index.length > 0,
  };
}

export function isLocalhost(): boolean {
  return (
    window.location.hostname === 'localhost' ||
    window.location.hostname === '127.0.0.1' ||
    window.location.hostname === '0.0.0.0'
  );
}
