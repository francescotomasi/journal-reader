1. Voglio che il mio sito viva nel web, e non su questo computer. Stavo pensando che gli uploads potrebbero essere gestiti su un google drive, o su github. I pdf presenti nella cartella /uploads possono essere scartati dopo che superano il limite massimo di spazio di archiviazione, e vorrei che si facesse automaticamente. Questo sito web deve avere una chiave di accesso, cossicchè solo io possa vederlo (stavo pensando a rendere il progetto privato su github, e cosi solo chi ha la mail può accedervi)
2. Aggiungere le foto ove possibile
3. Fare la prima pagina in una sezione a parte all'inizio degli articoli, invece di ignorarla completamente.

> Secondo te, ha senso fare tutte le foto? appesantirà l'ai?

  3. Appesantirà l'Archivio / GitHub? (Il VERO problema)

  Attualmente le stavo salvando come .png (che garantisce qualità altissima per i grafici, ma crea file enormi per le foto a colori).
  Se sei d'accordo, trasformo istantaneamente lo script di ritaglio per salvare le foto in formato WebP compresso all'80%. In questo modo:
  
  • La qualità visiva rimane perfetta per un sito web.
  • Il peso di ogni foto passa da ~2-3 MB a circa ~100-200 KB.
  • Il tuo repository GitHub rimarrà leggero per moltissimo tempo.
  