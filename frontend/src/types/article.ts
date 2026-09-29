export interface Article {
  id: string;
  title: string;
  subtitle: string;
  body: string;
  category?: string;
  page?: number;
  isHighlight: boolean;
}

export interface Journal {
  id: string;
  name: string;
  date: string;
  extractedAt: string;
  articles: Article[];
}

export interface JournalIndexEntry {
  id: string;
  name: string;
  date: string;
  articleCount: number;
  file: string;
}

export interface JournalIndex {
  journals: JournalIndexEntry[];
}
