import { Routes, Route } from 'react-router-dom';
import PasswordGate from './components/PasswordGate';
import Home from './pages/Home';
import Upload from './pages/Upload';
import Archive from './pages/Archive';
import Article from './pages/Article';

export default function App() {
  return (
    <PasswordGate>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/archivio" element={<Archive />} />
        <Route path="/archivio/:journalId" element={<Archive />} />
        <Route path="/articolo/:journalId/:articleId" element={<Article />} />
      </Routes>
    </PasswordGate>
  );
}
