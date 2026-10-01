import React from 'react';
import ReactDOM from 'react-dom/client';
import { HashRouter } from 'react-router-dom';
import App from './App';
import './index.css';

if ('scrollRestoration' in window.history) {
  window.history.scrollRestoration = 'manual';
}

// HashRouter uses URL hash (#) for routing, which works perfectly
// with GitHub Pages since all routes resolve to the same index.html
ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <HashRouter>
      <App />
    </HashRouter>
  </React.StrictMode>
);
