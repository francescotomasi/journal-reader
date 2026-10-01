import os
import json
from google import genai
from google.genai import types

# Initialize the client
client = genai.Client()

image_paths = [
    "/Users/macpro/Desktop/Antigravity/journal_reader/backend/page-images/page.24.png",
    "/Users/macpro/Desktop/Antigravity/journal_reader/backend/page-images/page.25.png",
    "/Users/macpro/Desktop/Antigravity/journal_reader/backend/page-images/page.26.png",
    "/Users/macpro/Desktop/Antigravity/journal_reader/backend/page-images/page.27.png",
    "/Users/macpro/Desktop/Antigravity/journal_reader/backend/page-images/page.28.png",
    "/Users/macpro/Desktop/Antigravity/journal_reader/backend/page-images/page.29.png",
    "/Users/macpro/Desktop/Antigravity/journal_reader/backend/page-images/page.30.png",
    "/Users/macpro/Desktop/Antigravity/journal_reader/backend/page-images/page.31.png",
    "/Users/macpro/Desktop/Antigravity/journal_reader/backend/page-images/page.32.png",
]

prompt = """
Sei un analista esperto di quotidiani italiani. Ti vengono fornite le IMMAGINI di tutte le pagine di un quotidiano italiano. Devi analizzare visivamente ogni pagina, leggere il contenuto rispettando il layout a colonne, e identificare tutti gli articoli presenti.

COME LEGGERE LE PAGINE:
- I quotidiani italiani usano un layout MULTI-COLONNA (tipicamente 5-6 colonne per pagina).
- Leggi ogni colonna dall'alto verso il basso, poi passa alla colonna successiva a destra.
- Un articolo può svilupparsi su PIÙ COLONNE nella stessa pagina.
- Un articolo può CONTINUARE SU PIÙ PAGINE (cerca indicazioni come "segue a pagina X", "continua a pagina X", "→", o frecce). In questo caso, unisci le parti in un unico articolo.
- I TITOLI degli articoli sono tipicamente in carattere grande e in grassetto.
- I SOTTOTITOLI (occhielli, sommari) sono in un font intermedio, spesso in corsivo o sotto il titolo.

REGOLE IMPORTANTI:
1. La PRIMA PAGINA del giornale è tipicamente una pagina di sommario/anteprima con i titoli degli articoli principali e brevi anticipazioni. La maggior parte di questi articoli viene ripresa nelle pagine successive con il testo completo. Solo 1-2 articoli della prima pagina sono pezzi unici che NON si ripetono nel resto del giornale.

2. Per ogni articolo, estrai:
   - "title": il titolo principale dell'articolo (OBBLIGATORIO)
   - "subtitle": il sottotitolo, sommario o occhiello (OBBLIGATORIO se presente, stringa vuota se assente)
   - "body": il testo completo dell'articolo, trascritto fedelmente (OBBLIGATORIO)
   - "category": la sezione/rubrica (es. "Economia", "Cronaca", "Esteri") — spesso indicata nell'intestazione della pagina
   - "page": il numero di pagina (se visibile nell'immagine)
   - "isHighlight": true se l'articolo è uno dei pezzi principali/di apertura

3. NON duplicare articoli: se un articolo della prima pagina viene ripreso nelle pagine interne con più testo, crea UN SOLO articolo usando il testo più completo delle pagine interne, ma mantenendo il titolo più prominente.

4. IGNORA completamente: pubblicità, inserzioni, avvisi legali, indici, numeri di pagina, intestazioni ripetute del giornale, informazioni editoriali, necrologi, annunci.

5. ATTENZIONE alle COLONNE: non mescolare il testo di colonne diverse che appartengono ad articoli diversi. Usa la posizione visiva e le separazioni grafiche (linee, filetti, spazi bianchi) per capire i confini tra articoli.

6. Restituisci SOLO un JSON valido (senza markdown code blocks, senza commenti) con questa struttura esatta:
{
  "newspaperName": "Nome del giornale (leggilo dalla testata in prima pagina)",
  "date": "YYYY-MM-DD (leggila dalla prima pagina)",
  "articles": [
    {
      "id": "art-1",
      "title": "...",
      "subtitle": "...",
      "body": "...",
      "category": "...",
      "page": 1,
      "isHighlight": false
    }
  ]
}

7. Ordina gli articoli per importanza (highlights prima, poi per ordine di apparizione nel giornale).

Analizza ora le immagini delle pagine del giornale fornite e restituisci il JSON.
ATTENZIONE: Stai analizzando il blocco 4 di 6 del giornale. Le pagine incluse in questo blocco sono le pagine da 24 a 32.
"""

contents = []
for path in image_paths:
    # We can upload the file or pass the raw bytes. With new sdk upload_file is usually better for large files.
    # Let's just upload them.
    file_obj = client.files.upload(file=path)
    contents.append(file_obj)

contents.append(prompt)

response = client.models.generate_content(
    model='gemini-2.5-pro',
    contents=contents,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        temperature=0.0
    )
)

print(response.text)
