# -*- coding: utf-8 -*-
import json
import fitz

doc = fitz.open('uploads/1790950591345-Il Sole 24 Ore 02 Ottobre 2026.pdf')

newspaper_name = "Il Sole 24 Ore"
date_str = "2026-10-02"

articles = []

# ==================== HIGHLIGHTS ====================

# 1. Page 8: In cinque anni -10% di alunni italiani e +8,3% di stranieri
articles.append({
    "id": "art-1",
    "title": "In cinque anni -10% di alunni italiani e +8,3% di stranieri",
    "subtitle": "Decreto scuola. Le relazioni allegate al Dl 170 inviato al Senato dopo la firma del Colle spiegano le ragioni della stretta del Governo e stimano 36mila adulti in più a lezione di lingua nei Cpia",
    "body": """di Eugenio Bruno e Claudio Tucci

ROMA
Se il testo definitivo del decreto scuola (il Dl 170/2026 che è stato pubblicato mercoledì sera sulla Gazzetta Ufficiale dopo la firma del Capo dello Stato) non riserva tante sorprese rispetto alle anticipazioni dei giorni scorsi, lo stesso non vale per le relazioni illustrativa e tecnica che lo accompagnano. Due documenti che aiutano a delineare meglio sia le ragioni che hanno portato il Governo a intervenire sulla presenza degli alunni stranieri nelle classi, sia gli effetti principali che possiamo attenderci dal provvedimento d'urgenza in 15 articoli che ha iniziato dal Senato il suo iter per la conversione in legge.

Ad esempio, scorrendo la relazione illustrativa scopriamo che gli alunni con cittadinanza non italiana hanno superato quota 911.578 (pari a quasi il 12% degli studenti totali) contro i 827.743 del 2019/20. In cinque anni sono cresciuti di 83.835, cioè del 10%, laddove gli alunni con cittadinanza italiana sono calati di oltre 612.000 unità (-8,3%), attestandosi a 6,78 milioni complessivi. Ed è in queste cifre che si annida - come spiegano i tecnici del Mim - «l'esigenza, non ulteriormente differibile, di dotare l'ordinamento di una disciplina uniforme volta a favorire un'equilibrata distribuzione degli studenti con cittadinanza non italiana tra le classi e, ove necessario, tra le istituzioni scolastiche». Come? Introducendo il tetto del 30% nelle prime classi, a partire dal 2027/28, per tutti gli scolari che provengono dall'estero e che non sono nati in Italia. Con due eccezioni, che non lo fanno scattare: vanno alla primaria e hanno già svolto due anni di scuola dell'infanzia oppure frequentano le medie e le superiori e di anni alle spalle ne hanno tre, con tanto di promozione. Regole che valgono anche per gli arrivi in corso d'anno del 2026/27, con la possibilità per i presidi che non riusciranno a trovare una sistemazione alternativa agli alunni eccedenti di utilizzare i 3,4 milioni per le attività extracurricolari di potenziamento linguistico (più altri 14,1 milioni nel 2028).

Altre informazioni degne di nota arrivano dalla relazione tecnica. A proposito di un'altra misura qualificante del Dl - la possibilità per le scuole di segnalare ai servizi sociali i casi di emergenza educativa degli alunni con genitori che non conoscono l'italiano e che vanno invitati a frequentare un corso di italiano presso i centri per gli adulti (Cpia) - scopriamo che sono circa 36.400 i possibili interessati. Alla stima si arriva prendendo le domande di ingresso in Italia accolte (circa 130mila nel 2025) e confrontandole con il numero di minori accompagnati (16.020 su 57.853, pari a circa il 28 %). Considerando anche gli alunni stranieri, la platea potenziale complessiva coinvolta dalle nuove norme, nel 2025/26, sarebbe stata di 216.895 soggetti, aggiungendo i 180.495 studenti stranieri che hanno già frequentato i percorsi erogati dai 130 Cpia sparsi nel Paese.

Del resto la conoscenza dell'italiano, oltre che per integrare, è fondamentale anche per una buona riuscita scolastica, visto che a fronte di un tasso di abbandono sceso al 6,2% per gli italiani, si sale al 16,9% tra gli studenti stranieri di prima generazione e al 12,7% tra quelli di seconda generazione. Non solo. Al termine del primo ciclo di istruzione, il rischio di dispersione implicita interessa il 22,5% degli studenti stranieri di prima generazione, a fronte dell'11,5% degli studenti italiani (dati Invalsi).

Sempre la relazione tecnica aiuta a chiarire meglio i contorni dei 21 milioni in più per il 2026 messi in campo per garantire la gratuità, totale o parziale, dei libri di testo, e il contestuale innalzamento della soglia Isee, da 30 a 40mila euro. La norma tuttavia circoscrive il beneficio alle sole prime classi della scuola media e alle prime e terze classi delle superiori (dove normalmente si cambiano più libri), e non più alle cinque classi delle superiori. L'effetto è una riduzione della platea dei beneficiari, dagli attuali 1.970.000 studenti si scende a 1.269.000 studenti, pari a circa il 35% in meno (quasi 700mila studenti e circa 540mila nuclei).

Una curiosità, infine, sul latino che dal 2027/28 sarà materia opzionale dalla seconda media (un'ora a settimana, per un totale di 33 annue). Non ci saranno prof in più, ma una rimodulazione dell'organico dell'autonomia, e le ore aggiuntive saranno retribuite con quelle risorse o con quelle del fondo per migliorare offerta formativa. Parliamo di 51,21 euro lordi per l'ora, che per il dipendente diventano 38,50 euro, sempre al lordo.""",
    "category": "Primo Piano",
    "page": 8,
    "isHighlight": True,
    "media": [
        {
            "type": "chart",
            "caption": "Le platee: dati del decreto scuola su studenti stranieri, adulti a lezione di lingua e libri gratuiti",
            "box": [342, 205, 512, 647],
            "page": 8
        }
    ]
})

# 2. Page 9: Generali e Luiss: Transformation Hub, per il lavoro del futuro
articles.append({
    "id": "art-2",
    "title": "Generali e Luiss: Transformation Hub, per il lavoro del futuro",
    "subtitle": "Partecipazione. Bollino Cnel al progetto che coinvolge azienda, sindacati e ateneo per gestire le sfide su AI, modelli Esg e competenze",
    "body": """di Giorgio Pogliotti e Claudio Tucci

Si chiamano Transformation Hub. Sono spazi di partecipazione attiva, di coprogettazione, pensati per coinvolgere azienda e rappresentanze sindacali in un percorso di analisi, ricerca e proposte sui principali fattori che stanno trasformando il lavoro e l'impresa. Con un ingrediente in più: la collaborazione scientifica con la Luiss Guido Carli che ha messo a disposizione i propri docenti coinvolti nei lavori dei Transformation Hub per arricchire il confronto sulle sfide più rilevanti nei contesti aziendali e, più in generale, nella società. Con questa la declinazione, piuttosto innovativa, Generali ha anticipato i contenuti della nuova normativa sulla partecipazione dei lavoratori (la legge n.76 del 2025) nel contratto integrativo siglato con First Cisl, Fisac Cgil, Uilca, Fna e Snfia, che ha ricevuto un riconoscimento significativo, il bollino blu assegnato dal Cnel alle buone pratiche di partecipazione aziendale.

Questo progetto è stato illustrato ieri pomeriggio, nella sede del Cnel, nel corso dell'evento “Costruire insieme il lavoro che verrà”, aperto dai saluti del presidente del Cnel Renato Brunetta, dell'AD di Generali Philippe Donnet e del presidente della Luiss Giorgio Fossa. «Per troppo tempo il nostro sistema produttivo ha guardato alla partecipazione dei lavoratori con diffidenza, come a un costo o a un vincolo all'autonomia dell'impresa - ha sottolineato il presidente Brunetta -. È arrivato il momento di cambiare prospettiva e di adottare il “paradigma partecipativo”, che trasforma quello che veniva percepito come un onere in un investimento in produttività, competenze, merito e qualità del lavoro. Mettere insieme capitale e lavoro, conoscenza e responsabilità significa creare valore per l'impresa e rafforzarne la capacità competitiva».

Nei Transformation Hub, composti in modo paritetico da rappresentanti dell'azienda e delle organizzazioni sindacali, si approfondiranno tre temi centrali: intelligenza artificiale e modelli di organizzazione del lavoro, sostenibilità e implementazione in azienda dei modelli ESG, demografia, invecchiamento attivo e gestione delle competenze. Il percorso è già operativo: nella prima fase di avvio, tra aprile e maggio, ha visto lo svolgimento di quattro sessioni di lavoro guidate dai docenti Luiss con circa 50 rappresentanti aziendali e sindacali, con l'obiettivo di tradurli in obiettivi di ricerca a supporto dell'evoluzione dell'organizzazione del lavoro.

Il progetto ha una durata triennale e punta ad essere un vero e proprio laboratorio permanente di partecipazione, pensato per accompagnare le società del Gruppo Generali nel governo delle trasformazioni future del lavoro, rafforzando un modello di relazioni industriali che promuove confronto e ricerca di soluzioni, con un approccio orientato alla qualità del lavoro, al benessere delle persone e alla competitività dell'impresa. «La collaborazione con Generali e il confronto promosso presso la prestigiosa sede del Cnel - ha aggiunto il presidente Fossa- rappresentano ad oggi un vero e proprio unicum e dimostrano la capacità della Luiss di porsi come ponte strategico tra ricerca scientifica avanzata e mondo del lavoro».

Entrando più nel dettaglio, nell'Hub sull'AI, Generali si confronterà con sindacati ed esperti su strumenti, criteri e scelte relative all'adozione dell'intelligenza artificiale. Il focus è posto soprattutto sull'impatto dell'innovazione tecnologica su processi di lavoro, modalità decisionali e competenze richieste alle persone. Nell'Hub su sostenibilità ed Esg si discuteranno soluzioni innovative su lavoro e sostenibilità sociale in linea con le migliori pratiche in giro per il mondo. È previsto l'approfondimento delle direttive Ue in materia di sostenibilità e dei loro effetti sull'organizzazione del lavoro. Nell'Hub su invecchiamento attivo e competenze la sfida è quella di valorizzare le skills presenti in tutte le fasce d'età favorendone lo scambio per accompagnare il ricambio generazionale e rendere efficace il passaggio di conoscenze tra lavoratori di generazioni diverse.

«Con questo progetto abbiamo scelto di riunire attorno allo stesso tavolo impresa, sindacati e mondo accademico per affrontare temi che stanno ridefinendo il lavoro e la società: dall'intelligenza artificiale alla sostenibilità sociale fino al cambiamento demografico - ha spiegato Gianluca Perin, Country General Manager di Generali Italia -. La collaborazione con l'università Luiss è centrale, perché ci consente di affiancare al confronto tra le parti il rigore della ricerca e una visione di lungo periodo. L'ambizione è contribuire a costruire una cultura della partecipazione capace di anticipare le trasformazioni e generare valore per il Paese». Il Dg della Luiss, Rita Carisano, ha sottolineato che «il Cnel ha creato il contesto perché questo progetto potesse decollare, noi abbiamo messo le competenze e il nostro metodo».

Sono 60 le pratiche aziendali raccolte, ha ricordato il presidente della commissione Partecipazione del Cnel, Emmanuele Massagli, 37 hanno ottenuto il bollino, 14 sono state respinte e 9 sono state segnalate senza ottenere il bollino. «Il 49% delle pratiche partecipative riconosciute riguardano modelli organizzativi come il Transformation Hub - ha detto Massagli -, ma solo tre, tra queste Generali, hanno previsto una formazione congiunta».""",
    "category": "Primo Piano",
    "page": 9,
    "isHighlight": True,
    "media": [
        {
            "type": "photo",
            "caption": "L’AI in azienda. Un’operaia al lavoro con l’AI: la digitalizzazione va diffondendosi in molte realtà produttive",
            "box": [123, 505, 364, 797],
            "page": 9
        }
    ]
})

# 3. Page 10: La maggioranza supera lo scoglio del voto segreto
articles.append({
    "id": "art-3",
    "title": "La maggioranza supera lo scoglio del voto segreto",
    "subtitle": "Legge elettorale. Secondo e ultimo passaggio a rischio l’8 ottobre con il sì finale alla Camera. Il governo tira un sospiro di sollievo. Il nodo delle firme per i centristi del campo largo",
    "body": """di Emilia Patta

ROMA
Sono le 13.27 quando il presidente della Camera Lorenzo Fontana proclama il risultato del voto a scrutinio segreto sulle pregiudiziali alla legge elettorale. E la maggioranza può tirare un sospiro di sollievo. Dopo giorni di tensioni, retroscena, ministri precettati e avvertimenti («se si va sotto si va a casa», la linea di Giorgia Meloni e Fdi) il risultato è migliore delle previsioni: 229 no contro 151 sì. Gli assenti sono complessivamente 17 e si contano, nei partiti, sulle dita di una mano. I quasi 80 voti di scarto con le opposizioni allontanano lo spettro dei franchi tiratori e blindano il testo - salvo incidenti sempre possibili - anche in vista del voto finale previsto per l’8 ottobre.

Se qualcuno nel campo largo sperava in un inciampo per poter evitare le primarie di coalizione, visto l’obbligo di indicare il nome del candidato premier al momento del deposito del contrassegno elettorale, è rimasto deluso. Le speranze delle opposizioni sembrano avere più chance sulla questione della quadruplicazione delle firme necessarie per presentare le liste (da 750 a 3mila a collegio), una misura fortemente voluta da Fratelli d'Italia e Lega che penalizza soprattutto i partiti minori e i nuovi soggetti politici di centro che si stanno formando nel campo largo. «Non a caso ho iniziato lo sciopero della fame proprio per questa legge elettorale - dice il radicale di Più Europa Riccardo Magi -. Non si possono chiedere 6mila firme a collegio, 450mila firme in tutto, ad un partito nuovo che si vuole presentare alle elezioni, una cifra superiore ai voti di alcuni partiti che ora siedono alla Camera e al Senato». Solo i partiti che hanno una componente dentro un gruppo parlamentare hanno uno “sconto” sulle firme, che scendono a 1.500/2mila a collegio, ma occorre appoggiarsi a un simbolo presentatosi alle ultime elezioni. Fuori dunque anche Alessandro Onorato, l’assessore capitolino che ha fondato Progetto Civico Italia sotto l’egida del leader del M5s Giuseppe Conte, ostile alla presenza del solo Matteo Renzi alla destra del campo largo. Intanto Bruno Tabacci, leader e proprietario del simbolo Centro democratico, attende l’inizio della prossima settimana per formare il “suo” sottogruppo: nelle intenzioni tabacciane la nuova casa centrista è aperta ai socialisti di Enzo Maraio, a Magi e a Ernesto Maria Ruffini, ma non a Onorato. Un bel ginepraio che certo le nuove regole non aiutano a districare.""",
    "category": "Politica",
    "page": 10,
    "isHighlight": True,
    "media": [
        {
            "type": "photo",
            "caption": "Votazioni in Aula. L’Aula della Camera ha respinto ieri, con scrutinio segreto (229 i no e 151 i sì), le questioni pregiudiziali di costituzionalità presentate dalle opposizioni rispetto sulla legge elettorale",
            "box": [236, 430, 355, 797],
            "page": 10
        }
    ]
})

# 4. Page 12: Parigi, scure sul welfare nel budget di Lecornu
articles.append({
    "id": "art-4",
    "title": "Parigi, scure sul welfare nel budget di Lecornu",
    "subtitle": "La proposta del governo. Dimezzato il deficit dello Stato sociale, sacrifici per pensionati, ospedali, disoccupati. L’obiettivo della manovra da 54 miliardi è riportare il disavanzo al 5%",
    "body": """di Riccardo Sorrentino

Dimezzare quasi il deficit della Sécurité Sociale. Ha un obiettivo ambizioso la parte previdenziale e sanitaria della manovra di bilancio da 54 miliardi complessivi presentata ieri dal Governo guidato da Sébastien Lecornu. Una manovra che promette sacrifici un po' per tutti, compresi i pensionati, e che ha già provocato forti tensioni sociali e proteste nelle piazze.

«Non ci saranno nuove tasse, né un aumento delle imposte sui redditi o dell'Iva, ma diverse misure mirate», ha spiegato il ministro dell'Economia Roland Lescure illustrando l'impianto della manovra finanziaria per il 2027. Il cuore dell'intervento - che in Francia riguarda due bilanci pubblici distinti: quello dello Stato e quello della Sécurité Sociale - punta a riportare il disavanzo pubblico dal 6,1% stimato per quest'anno al 5% nel 2027, rispettando la traiettoria di rientro concordata con l'Unione europea.

Il 60% della manovra è composto da tagli della spesa pubblica, mentre il restante 40% deriverà da maggiori entrate. Tra i tagli più significativi figurano il contenimento della spesa farmaceutica e sanitaria, la revisione di alcune agevolazioni per le imprese e un giro di vite sulle indennità di disoccupazione. Per quanto riguarda le pensioni, resteranno indicizzate al 100% solo quelle di importo più basso, mentre per gli assegni superiori scatterà una rivalutazione parziale, ferma al 50% dell'inflazione registrata. Misure che hanno immediatamente scatenato la dura reazione delle opposizioni e dei sindacati, pronti a dare battaglia sia in Parlamento sia nelle piazze del Paese.""",
    "category": "Economia e politica internazionale",
    "page": 12,
    "isHighlight": True
})

# 5. Page 12: Esplode la protesta dei liceali: decine di scontri in Francia
articles.append({
    "id": "art-5",
    "title": "Esplode la protesta dei liceali: decine di scontri in Francia",
    "subtitle": "Quasi 2mila fermi. Preside e tre dirigenti aggrediti e cosparsi di benzina a Marsiglia",
    "body": """di Riccardo Sorrentino

Diventano più violente le proteste dei liceali francesi, che alimentano anche lo scontro politico mentre il Parlamento si appresta a discutere la manovra economica del governo Lecornu. Molte le manifestazioni nelle principali città del Paese. Anche una trentina di minorenni sono state trattenute in custodia di polizia, su 200 licei coinvolti nei blocchi e nelle manifestazioni di protesta.

A Marsiglia si sono registrati gli episodi più gravi, dove un preside e tre dirigenti scolastici sono stati aggrediti e cosparsi di benzina da alcuni manifestanti incappucciati durante il tentativo di impedire il blocco dell'istituto. La vicenda ha assunto immediato rilievo politico. Secondo Matignon, la sede del primo ministro, le proteste studentesche sarebbero cavalcate e alimentate ad arte dalla sinistra radicale di La France Insoumise. «Sosteniamo la mobilitazione dei liceali», ha rivendicato il coordinatore di Lfi Manuel Bompard: «È un movimento legittimo contro una manovra ingiusta che toglie risorse all'istruzione e al futuro delle nuove generazioni». Dal canto suo il leader socialista Olivier Faure, pur criticando le scelte del governo, ha richiamato alla «calma e alla distensione da ogni parte», condannando fermamente qualsiasi atto di violenza fisica contro il personale scolastico.""",
    "category": "Economia e politica internazionale",
    "page": 12,
    "isHighlight": True,
    "media": [
        {
            "type": "photo",
            "caption": "Scontri e incendi. La protesta studentesca a Saint-Denis",
            "box": [446, 355, 591, 797],
            "page": 12
        }
    ]
})

# 6. Page 13: Volo FlyDubai, per Netanyahu il copilota «è stato radicalizzato»
articles.append({
    "id": "art-6",
    "title": "Volo FlyDubai, per Netanyahu il copilota «è stato radicalizzato»",
    "subtitle": "Le indagini. Il premier israeliano insiste sulla pista del terrorismo di matrice islamica. Tutte le compagnie aeree emiratine sospendono i voli per Tel Aviv",
    "body": """di Micaela Cappellini

Continuano le indagini sui motivi che martedì hanno spinto il copilota omanita del volo FlyDubai per Tel Aviv ad accoltellare il comandante, rischiando lo schianto del velivolo e la morte dei passeggeri. Il governo degli Emirati arabi uniti - dove ha sede la compagnia aerea - ha avviato le indagini per verificare «se vi sia un collegamento con eventuali scopi terroristici». La legge degli Emirati si applica ai reati commessi a bordo degli aerei con sede nel Paese, ma allo stesso tempo a indagare sono anche le autorità dell’Arabia saudita, dove il velivolo è riuscito a fare un atterraggio di emergenza, evitando il peggio.

Israele però continua a rimanere convinta del movente terroristico. «È evidente che il copilota nutrisse odio verso gli israeliani - ha detto ieri il primo ministro israeliano, Benjamin Netanyahu, durante un’intervista a Fox News - l’attentatore è stato radicalizzato dall’Islam. Lui dice all’equipaggio: “Uccidetemi”, è chiaro che intendesse suicidarsi, far schiantare l’aereo». Il presidente Usa si è addirittura spinto a ipotizzare un coinvolgimento dell’Iran: «In base a quanto sto sentendo, penso ci sia un collegamento tra l’Iran e il pilota omanita», ha detto ieri. Ma un funzionario israeliano intervistato da Ynet al momento lo ha escluso: «L’attività online del copilota e la radicalizzazione religiosa sono oggetto di esame, ma probabilmente ha agito da solo».

Già ieri mattina l’uomo responsabile dell’aggressione nella cabina di pilotaggio del volo FZ 1073, che si trovava in arresto in Arabia Saudita, è stato trasferito ad Abu Dhabi dalle autorità saudite. Per il ministro della Sicurezza nazionale di Tel Aviv, il falco Itamar Ben Gvir, Israele chiederà l’estradizione del copilota: «Chi ha pianificato di far precipitare un aereo e uccidere 180 israeliani deve essere estradato in Israele e pagare qui il prezzo più alto».

Le autorità dell’Arabia Saudita stanno già collaborando con diversi Paesi, tra cui Israele, per cercare di determinare il movente di quanto accaduto ieri. Nelle indagini sarebbero già stati coinvolti gli Emirati Arabi Uniti, gli Stati Uniti e l’Oman, Paese di origine del copilota. Al vaglio degli inquirenti ci sono ancora tutti gli scenari possibili, dal terrorismo ai disturbi mentali. In particolare, i servizi di intelligence e di sicurezza israeliani stanno indagando sul copilota in Arabia Saudita: per quanto Riad non intrattenga relazioni diplomatiche formali con Israele, esiste una cooperazione di lunga data in materia di sicurezza e intelligence attraverso canali alternativi. L’Arabia Saudita ha comunque già fatto sapere che consegnerà l’uomo agli Emirati una volta conclusa l’indagine.

Al momento, sia Emirates - la compagnia aerea di bandiera degli Emirati - che FlyDubai hanno sospeso tutti i voli per Tel Aviv.""",
    "category": "Economia e politica internazionale",
    "page": 13,
    "isHighlight": True
})

# 7. Page 15: Brasile al voto, testa a testa in un Paese diviso tra sinistra dogmatica e populismo
articles.append({
    "id": "art-7",
    "title": "Brasile al voto, testa a testa in un Paese diviso tra sinistra dogmatica e populismo",
    "subtitle": "Elezioni presidenziali. I sondaggi: pareggio tecnico tra Lula e Bolsonaro. Ballottaggio quasi certo",
    "body": """di Roberto Da Rin

L’aria che si respira lungo i viali geometrici di Brasilia, nelle congestionate arterie di San Paolo tra i grattacieli o ai piedi dei morros di Rio, condensa una promessa e una minaccia. La tensione che attraversa le famiglie e i quartieri si divide tra l’elettorato su due fazioni contrapposte. La campagna del primo turno delle elezioni presidenziali del Brasile, in programma domenica, si consuma in uno scontro all’ultimo voto tra due modelli politici, economici e persino antropologici: da una parte il presidente uscente, Luiz Inácio Lula da Silva, 80 anni, icona della sinistra e paladino della spesa sociale. Dall’altra il senatore Flavio Bolsonaro, 45 anni, erede politico del padre Jair e alfiere del conservatorismo e del liberismo economico.

I dati emersi dagli ultimi sondaggi fotografano un Paese letteralmente spaccato in due. Le rilevazioni di Datafolha e i dati freschi degli istituti Real Time Big Data e Meio/Ideia danno l’immagine chiara di pareggio tecnico. Al primo turno, Lula si attesta in una forbice compresa tra il 39% e il 41%, tallonato da Flavio Bolsonaro, che oscilla tra il 36% e il 39%. La prospettiva del ballottaggio di fine ottobre si delinea come quasi certa.

Sullo sfondo di questa trincea ideologica si staglia un quadro economico complesso, segnato da luci e ombre macroeconomiche che alimentano le opposte narrazioni dei comitati elettorali. La crescita del Pil mostra segnali di frenata rispetto ai picchi passati: le stime del Banco Central do Brasil nel suo ultimo rapporto Focus hanno rivisto al ribasso la crescita 2026, posizionandola in una forchetta compresa tra l’1,6% e l’1,8%, per effetto dei tassi di interesse elevati che frenano gli investimenti industriali. A preoccupare mercati ed elettori è la piccola fiammata dell’inflazione, che ha rotto il tetto programmato spingendosi al 5,1%, erodendo il potere d’acquisto reale delle classi meno abbienti e surriscaldando i prezzi dei beni di consumo quotidiano.

Se sul fronte del mercato del lavoro si registra una nota positiva, con un tasso di disoccupazione stabile attorno al 6% grazie alla solidità del settore dei servizi e delle materie prime, la vera spina nel fianco del governo di sinistra riguarda i conti pubblici. Il debito pubblico lordo ha subito un’impennata preoccupante, superando l’82,5% del Pil e sfondando la cifra nominale di 11mila miliardi di reais. Questo deficit strutturale viene brandito da Flavio Bolsonaro come la prova del «fallimento fiscale del lulismo, mentre l’attuale presidente difende la spesa pubblica sostenendo che la vera ricchezza del Brasile passi per il riscatto sociale della sua gente. A questa frattura sociale si affianca l’emergenza ambientale e geopolitica legata alla gestione dell’Amazzonia. La foresta tropicale, devastata dagli incendi e dalla pressione costante della deforestazione illegale e delle miniere clandestine, garimpos, è divenuta un terreno di scontro ideologico. Lula rivendica gli impegni internazionali per la transizione ecologica e la tutela delle riserve indigene, Flavio Bolsonaro intercetta il consenso dei grandi proprietari terrieri difendendo l’espansione della frontiera agricola in nome della sovranità produttiva del Paese. Comunque vada, non saranno i decimali dell’inflazione o la geometria dei sondaggi a ricomporre la faglia profonda che attraversa questa terra. Domenica, nel silenzio della cabina elettorale, un intero popolo depositerà nell’ombra la propria scommessa sul futuro.""",
    "category": "Economia e politica internazionale",
    "page": 15,
    "isHighlight": True
})

# 8. Page 16: I cinque scenari che incalzano l’Unione Europea
articles.append({
    "id": "art-8",
    "title": "I cinque scenari che incalzano l’Unione Europea",
    "subtitle": "Le sfide della Ue",
    "body": """di Luigi Zanda

Il 16 settembre, a Strasburgo, Ursula von der Leyen ha svolto il discorso sullo stato dell'Unione. Un discorso solenne, molto politico, da capo di Stato. Nell'organigramma del potere europeo la posizione della presidente della Commissione la rende in qualche modo libera, super partes, a differenza dei capi di Stato e di governo che partecipano al Consiglio Europeo, ciascuno con la propria chiara connotazione politica. In alcuna passaggi del suo discorso ha sottolineato l'obiettivo ambizioso di «un'Europa indipendente che abbia il potere di agire», con una voce autorevole nelle alleanze internazionali, in grado di operare con efficacia sui grandi nodi del nostro tempo. Dunque, un ottimo discorso venuto dal pulpito più alto.

Con una riserva. C'erano parole che mancavano e c'era qualche concetto espresso con troppa diplomazia. Quale remora può aver trattenuto von der Leyen dal chiedere esplicitamente l'abolizione di quel diritto di veto che lei sa bene quanto pesi in un'Unione di 27 Paesi? E perché in un discorso di così alto spessore nemmeno un cenno alla prospettiva di un'Europa federale o confederale, con un suo governo e un Parlamento titolare del potere legislativo? Von der Leyen ha sorvolato e si può capire perché. Avrà considerato che oggi non ci sono le condizioni politiche e geopolitiche per l'ampio consenso che servirebbe. E, probabilmente, alla presidente non piace apparire velleitaria. Da quel silenzio viene, però, una domanda importante: se chi è a capo di una grande organizzazione internazionale come l'Unione Europea, non abbia il dovere di proporre una visione, una prospettiva, un obiettivo strategico e di farlo persino prescindendo dal consenso contingente. Di farlo cercando il consenso su qualcosa in cui crede fortemente e non solo quando i calcoli di schieramento la rassicurano. Se i giovani europei amano poco l'Europa, se cresce il favore verso le formazioni euroscettiche, forse un briciolo di responsabilità ce l'ha anche una classe dirigente che da tempo non è più capace di illuminare il futuro con quelle utopie sulle quali sempre, in tutti i tempi e in tutte le latitudini, sono state costruite le grandi democrazie.

Per governare una nazione, da che mondo è mondo, non è mai bastato occuparsi del giorno per giorno, ma è stato necessario saper vedere lontano e capire prima quel che accadrà dopo. Oggi i nostri errori e la nostra miopia hanno reso più difficile prevedere il futuro. A furia di rinviare la soluzione dei grandi nodi che incombono sull'umanità, i problemi hanno assunto dimensioni imponenti e sembra che non ci siano più né il tempo, né il modo per affrontarli. Le singole nazioni non hanno le dimensioni che servirebbero e la cooperazione internazionale è frenata dalle ambizioni delle grandi potenze e da un nuovo capitalismo predatorio. Dopo aver ascoltato Ursula von der Leyen a Strasburgo, resta senza risposta la domanda di chi abbia il dovere, se non la presidente della Commissione, di mettere sul tavolo la urgente necessità di completare il progetto di De Gasperi, Adenauer e Schuman. L'arte della politica ha bisogno di concretezza, ma per poter immaginare un futuro di ragionevole speranza, la politica deve saper aggiungere alla concretezza anche molta utopia e molta fantasia.

Sull'umanità incombono cinque scenari molto reali e poco governati, sui quali un'Europa politica potrebbe dir molto, mentre l'Europa degli Stati è completamente assente. Sono scenari che hanno un andamento molto veloce che sta infliggendo ferite profonde al pianeta:

1. Il clima. Le grandi catastrofi ambientali sono sempre più frequenti e violente. Se le temperature continueranno ad aumentare, presto verranno colpite anche quelle aree del mondo che sinora sono state risparmiate. Il calore sta radicalmente modificando le condizioni di vita di tutti gli esseri viventi. Sale il livello dei mari e le coste vengono sommerse, i ghiacciai si sciolgono, gli incendi distruggono foreste secolari, vulcani e terremoti si mettono in movimento, intere regioni si desertificano. Colpisce la velocità con cui il clima sta cambiando e il fatalismo con cui lo stiamo osservando.

2. La pace. I rapporti tra gli Stati non sono più regolati dal diritto internazionale, ma dalla forza. Droni e aerei russi sorvolano nazioni europee, Trump stravolge le tradizionali alleanze degli Usa, Netanyahu prosegue con la violenza, Turchia, Egitto e Arabia Saudita si alleano, l'Indo Pacifico è appeso alle decisioni della Cina su Taiwan. La chiusura di Hormuz e la semichiusura di Bab El Mandeb stanno destabilizzando l'economia del pianeta. La guerra ibrida viola quotidianamente i confini e la sovranità delle nazioni. L'Ucraina e il Medio Oriente non sono gli unici teatri di guerra. Gli Usa, la Cina, la Russia e l'Europa partecipano alle due guerre con armi e informazioni. La nuova guerra mondiale è già in atto.

3. Economia. Il rischio di una crisi economica globale è reale. Inflazione, aumento dei tassi, dazi abnormi. Jp Morgan alza le mani e dice «i modelli sono saltati, non sappiamo più dire dove andrà il petrolio», «difficile sostenere che le guerre siano temporanee». Benzina, gas di città e sulle autostrade, gasolio per i mezzi di trasporto, gasolio per il riscaldamento, hanno avuto importanti aumenti generalizzati. La prosecuzione delle guerre avrà ulteriori effetti su inflazione, tassi e energia, con conseguenze su tutta l'economia del globo e preoccupanti ricadute sociali. Il gigantesco debito pubblico che gran parte delle nazioni ha accumulato, impedirà agli stati di intervenire efficacemente.

4. Migrazioni. Nei prossimi anni la crescente povertà, la fame, la paura delle guerre e della grande criminalità, la desertificazione di intere regioni, il clima invivibile, moltiplicheranno l'entità delle migrazioni. Oggi si stima che in un anno 8-10 milioni di persone migrino da un mondo povero fatto di giovani affamati, verso un mondo ricco abitato da vecchi sazi. In un futuro prossimo l'istinto di sopravvivenza farà sì che quei 10 milioni diventino presto 100 o anche più. Il mondo non è pronto ad accogliere migrazioni di massa di queste dimensioni.

5. Tecnologia. Il cambiamento tecnologico e l'intelligenza artificiale stanno modificando la realtà e ingigantendo le disuguaglianze. Oltre a un'immensa disponibilità finanziaria, le Big Tech possiedono tutte le componenti tecnologiche necessarie all'industria civile e militare. Il loro potere è tale che tengono sotto scacco l'economia di gran parte del pianeta. I padroni delle grandi società tecnologiche temono che l'intelligenza artificiale, su cui hanno investito miliardi di dollari, possa sfuggire di mano sino a mettere a rischio la sopravvivenza dell'umanità. Da qui la richiesta di un rallentamento. Ma Trump vuole andare avanti per paura del sorpasso cinese.

Questi cinque scenari riassumono i gravi rischi che sta correndo il pianeta. Sono cinque mega problemi molto diversi, ma con molto in comune. Sono fortemente interconnessi e si muovono in un contesto privo di regole. Ma, soprattutto, sono scenari sui quali nessun Paese, tantomeno europeo, è in grado di intervenire da solo sperando in un buon risultato. A Strasburgo Ursula von der Leyen ha mostrato di avere una piena consapevolezza dell'entità della sfida e dell'inadeguatezza di un'Unione Europea di 27 singoli Stati. Peccato. Perché se, pensando al futuro dell'Europa, oltre all'analisi dei problemi, avesse proposto un assetto delle istituzioni europee più democratico e con la forza di una vera Unione politica, avrebbe messo in movimento il piccolo cabotaggio della politica europea e in tanti l'avrebbero applaudita con maggior convinzione.

Chi in futuro studierà la storia europea di questi decenni avrà difficoltà a capire le ragioni del mancato completamento dell'Unione. Perché dal dopoguerra ad oggi i rischi che il mondo corre si sono aggravati e moltiplicati e la necessità di un'Europa forte non è più soltanto il lungimirante progetto di tre grandi statisti e di tre straordinari pensatori politici, ma è diventata un'urgenza strategica di sopravvivenza dell'Europa. La mancata unità politica pesa sulla nostra vita quotidiana, alimenta le paure, rende volatile il consenso. Ciò nonostante la politica delle nazioni europee non riesce a darsi una visione e vive come se il tempo a sua disposizione fosse infinito. Ma decidere quando finisce il tempo non è nei suoi poteri, perché è il susseguirsi degli avvenimenti che lo deciderà.""",
    "category": "Commenti",
    "page": 16,
    "isHighlight": True
})


# ==================== NON-HIGHLIGHT ARTICLES ====================

# 9. Page 8: Valutazione a tempo (quasi) di record per i bandi di ricerca
articles.append({
    "id": "art-9",
    "title": "Valutazione a tempo (quasi) di record per i bandi di ricerca",
    "subtitle": "Il ministero di Bernini. Scelti nei termini i vincitori di Prin, Hybrid e Synergy Grant da 364,4 milioni",
    "body": """ROMA
Se non è un record poco ci manca. In meno di quattro mesi il ministero dell'Università ha concluso la valutazione di tutti i progetti di ricerca emanati a fine aprile per distribuire la prima annualità del “fondone” triennale da 1,2 miliardi istituito con la manovra 2026. Tra Prin, Prin Hybrid e Synergy Grant, tutti relativi al 2026, stiamo parlando di 364,4 milioni di risorse nazionali che andranno a enti pubblici e privati.

La prima notizia è che, stando al cronoprogramma emanato a inizio anno dalla ministra Anna Maria Bernini, la selezione dei vincitori doveva arrivare entro il 30 settembre e la scadenza, di fatto, può dirsi rispettata. La seconda è che la scelta delle proposte aggiudicatarie si è conclusa in un arco di tempo decisamente inferiore rispetto al recente passato. Prendiamo i progetti di rilevante interesse nazionale (i Prin 2026) che sono destinati ai consorzi tra più ricercatori appartenenti a università, enti di ricerca e istituzioni dell'Alta formazione artistica e musicale (Afam) e rappresentano anche la “fetta” più cospicua di finanziamenti in palio nel 2026: 259,8 milioni di cui 38,8 milioni riservati agli scienziati under 40.

Se consideriamo che le domande si chiudevano il 1° giugno scorso vuole dire per esaminare le 4.279 proposte arrivate ci sono voluti circa 120 giorni, peraltro con l'estate di mezzo. Per i Prin 2022 passarono invece oltre 15 mesi tra la scadenza del bando e l'individuazione degli ammessi. E il fatto che i progetti da valutare fossero molti di più (7.809) non basta a giustificare le lungaggini di allora. I Prin successivi, finanziati sempre nel 2022 grazie al Pnrr, aveva visto un numero di candidature molto simile all'ultima edizione (4.472 anziché 4.279), ma aveva richiesto comunque quasi nove mesi tra la il termine per candidarsi e la conclusione delle valutazioni.

Chissà se un ruolo di primo piano stavolta lo ha giocato il fatto che l'87% dei revisori provenga dall'estero (contro il 67,7 e il 57,2% delle due precedenti tornate citate poc'anzi). Una percentuale che per un altro bando appena aggiudicati (i Synergy Grant 2026), pensato per incentivare le collaborazioni pubblico-private e le competenze maturate con il Pnrr e Pnc (Piano nazionale complementare), è arrivato addirittura al 100 per cento.

I risultati dei Prin 2026
Tornando ai Prin 2026, le idee reputate finanziabili sono state 199. Di queste, 70 si riferiscono al macrosettore Scienze della vita, 69 a Scienze fisiche e ingegneria e 60 a Scienze sociali e umanistiche. Adesso i prossimi step in programma riguardano, da un lato, la pubblicazione degli esiti del bando e, dall'altro, l'emanazione del decreto di ammissione a finanziamento.

Prin Hybrid
Allo stesso punto si trova un'altra selezione bandita anch'essa a fine aprile: i nuovi Prin Hybrid che foraggia i progetti triennali su cinque aree tematiche considerate strategiche dall'Ue (tecnologie quantistiche, Hpc, AI, cybersicurezza e sanità innovativa) e valorizza, come dice il nome, l'ibridazione dei saperi, integrando competenze scientifiche, tecnologiche, umanistiche, sociali e artistiche. In risposta al bando, che si è chiuso il 4 luglio scorso, sono arrivate 395 candidature. Il compito di selezionarle è toccato a 180 revisori, per il 50% provenienti dall'estero. Le proposte scelte sono state 30. Così suddivise tra i cinque temi eleggibili: 10 per tecnologie e percorsi innovativi in ambito sanitario, 10 per l'intelligenza Artificiale, quattro per le tecnologie quantistiche, tre per la cybersicurezza e tre per l'High performance computing.

Synergy Grant
Completano il tris di bandi giunti al traguardo i Synergy Grant da 48 milioni, rivolti alle proposte di ricerca applicata, innovativa e di frontiera, che per ambizione scientifica e complessità richiedano modelli avanzati di cooperazione pubblico-privata e competenze multidisciplinari. In questa direzione un ruolo di primo piano è stato ritagliato agli hub creati da Pnrr o Pnc che sono chiamati ad agire come catalizzatori e aggregatori di alte competenze scientifiche e industriali, sviluppando ricerche ad alto impatto sociale ed economico. Qui su dieci proposte arrivate sono state “promosse” e, dunque, otterranno un finanziamento tutte e dieci.""",
    "category": "Primo Piano",
    "page": 8,
    "isHighlight": False,
    "media": [
        {
            "type": "chart",
            "caption": "Le selezioni al traguardo: dotazione ed esiti della valutazione per Prin 2026, Prin Hybrid 2026 e Synergy Grant 2026",
            "box": [129, 666, 303, 946],
            "page": 8
        }
    ]
})

# 10. Page 8: l’alunno premiato
articles.append({
    "id": "art-10",
    "title": "l’alunno premiato",
    "subtitle": "",
    "body": "«Siamo orgogliosi di te». Lo ha detto il ministro dell'Istruzione e del Merito, Giuseppe Valditara, consegnando ieri una medaglia al merito allo studente di origine congolese, che lo scorso 18 settembre è intervenuto durante l'aggressione alla professoressa Isabella Marsilio, alla scuola media Giovanni Verga di Roma.",
    "category": "Primo Piano",
    "page": 8,
    "isHighlight": False
})

# 11. Page 10: Meloni incassa l’applauso degli artigiani «Avanti con la riforma del settore»
articles.append({
    "id": "art-11",
    "title": "Meloni incassa l’applauso degli artigiani «Avanti con la riforma del settore»",
    "subtitle": "Agli 80 anni della Cna. «Un riassetto per la crescita» Ma sulla legge delega in corso una mediazione",
    "body": """di Manuela Perrone

La platea è di quelle più calorose che mai. All’evento per gli 80 anni della Cna a Roma Giorgia Meloni è di casa. Ma intanto la premier conferma che «il Governo intende andare avanti con la legge delega per consentire all'artigianato di crescere restando quello che è».

Poco prima, perorando la legge, il presidente della Cna, Dario Costantini, le ha domandato: «Presidente, Giorgia, tu vuoi bene agli artigiani?». Dal «sì, voglio bene agli artigiani» Meloni parte per un lungo intervento che elogia il mondo artigiano («siete voi che mandate avanti l’Italia») e rivendica i risultati delle misure a sostegno: la proroga della decontribuzione Sud nella manovra e le norme anti evasione che «hanno portato alla chiusura di oltre 30mila partite Iva apri e chiudi». «Non lo considero un favore», precisa. «Lo considero una misura che rafforza il nostro sistema produttivo e i nostri territori, che aumenta l’occupazione, che arricchisce l’Italia nel suo complesso». Perché, chiarisce, «io penso che un’impresa artigiana abbia diritto di crescere restando quello che è».

Da qui Meloni annuncia l’invio della lettera a Ursula von der Leyen sulla flessibilità aggiuntiva legata all’inflazione: «Se i prezzi dell'energia aumentano oltre l'80% non è colpa di nessuno Stato membro, le regole europee devono tenerne conto».

L’abbraccio con la Cna segue quello andato in scena al mattino a Genova, più agitato: la premier ha inaugurato il 66° Salone nautico, ma sul palco erano seduti solo con lei, il presidente di Confindustria nautica Piero Formenti e il governatore Marco Bucci. La sindaca Silvia Salis, che qualcuno a sinistra sogna leader del campo largo, è rimasta seduta in prima fila accanto alla vicepresidente del Senato Licia Ronzulli. Un’esclusione che ha suscitato imbarazzo. «Non voglio fare polemica», ha commentato Salis. «Vorrei solo ricordare che noi siamo in prestito alle istituzioni, le istituzioni non sono “nostre”. Ma devo dire che se l’obiettivo, come si vocifera, era quello di togliermi l’attenzione non credo sia stato raggiunto». Una nota di Palazzo Chigi si è affrettata a sottolineare come Meloni fosse «rimasta sorpresa e dispiaciuta» per l’assenza della prima cittadina, dispiacere poi espresso anche al telefono, e come avesse chiesto spiegazioni. Un errore dell’organizzazione del Salone, la risposta. Il Salone stesso ha tenuto a precisare che Palazzo Chigi era «completamente estraneo all’accaduto».

Fatto sta che, secondo il cerimoniale dell’inaugurazione, non avrebbe dovuto salire sul palco neanche il presidente della Liguria. «Quando mi hanno chiamato mi sono stupito», ha detto Bucci. Il centrosinistra, sulle barricate, parla di «sgarbo istituzionale» e invoca chiarezza. Meloni considera chiuso l’incidente. Che però, assieme alla ridda di appuntamenti cui la premier sta prendendo parte, conferma il clima: da campagna elettorale.""",
    "category": "Politica",
    "page": 10,
    "isHighlight": False
})

# 12. Page 10: Calcoli e profili sulla figura di un federatore evocata da Conte
articles.append({
    "id": "art-12",
    "title": "Calcoli e profili sulla figura di un federatore evocata da Conte",
    "subtitle": "Politica 2.0",
    "body": """di Lina Palmerini

Chissà se quella di Conte è una vera apertura oppure una finta visto che sa bene quanto Schlein non intenda rinunciare alle primarie. E, allora, quella frase in cui si dice disponibile – e non da ora – a una figura terza per «tentare una massima concordia» forse non si potrà mai verificare ma resterà agli atti come una mano tesa, un’opzione che il leader 5 Stelle non aveva scartato. Anche questo appartiene a una tattica di gioco che l’ex premier mostra di dominare molto più della leader Dem.

Lei appare, invece, arroccata con i suoi a difendere il suo percorso di ascesa e impegnata a chiudere ogni strada a terzi o ad altri esponenti del suo partito. Ecco, già queste due narrazioni sono diventate parte della corsa, perché nel momento in cui si andrà a votare ai gazebo, al di là dell’appartenenza partitica, conteranno i profili. E il più urgente da trovare è chi sappia mettere insieme idee differenti ma anche personalismi e talvolta narcisismi.

Non c’è dubbio, guardando a ciò che accade in Parlamento, che la tara del centro-sinistra resti quella della dis-unione. Nessuno che faccia un passo verso l’altro, che cerchi dialogo e mediazione. L’ultimo caso è il Ddl sull’antisemitismo: voti in ordine sparso. Ma anche sulla politica estera si rimane in un vicolo cieco con Conte che boccia la mediazione di Bettini su Kiev. Eppure, se c’è un mantello sotto cui si riparano tutti a sinistra, è quello della Costituzione che mostrano, però, di non conoscere. Perché la Carta non è solo articoli ma è stata soprattutto un metodo politico in cui – padri e madri costituenti - riuscirono a trovare l’intesa e una base di valori comune nonostante appartenenze ideologiche molto diverse: i comunisti, i cattolici, i liberali. Ora, di questo metodo non c’è proprio traccia nel campo largo e questo raffredda i consensi.

L’incapacità di stare insieme è il virus che infetta anche le buone idee e, in effetti, uno si chiede: ma che senso hanno primarie e programma se poi, nella quotidianità, riemergono divisioni? E non emergono – invece – figure che sappiano mettere il mastice dove serve. In questo senso, una figura terza avrebbe un senso, se fosse riconosciuta la sua attitudine a comporre, più che a dettare la linea. «Non un nome qualsiasi ma che garantisca un cambio. Non una figura morbida». Questo è l’identikit tracciato da Conte e c’è chi ci vede un autoritratto. Altri, invece, vogliono vederci il profilo di Bersani. La sua popolarità, misurata nelle piazze o in Tv sta - forse - non solo negli affondi alla destra o nelle proposte che lancia ma in quell’inclinazione che mostra a non strappare, a non sbattere le porte o i pugni. Questa sarebbe una vera novità per la politica, trasversalmente.""",
    "category": "Politica",
    "page": 10,
    "isHighlight": False
})

# 13. Page 10: Il Pd si compatta su Schlein, ma Conte punge su primarie e Ucraina
articles.append({
    "id": "art-13",
    "title": "Il Pd si compatta su Schlein, ma Conte punge su primarie e Ucraina",
    "subtitle": "Oggi la direzione dem",
    "body": """di Emilia Patta

Punto numero uno, le primarie: «Io ho dichiarato fin dall’inizio di essere pronto a valutare la possibilità di un nome terzo, autenticamente progressista e competitivo, rispetto a quello dei leader. Ma non c’è stata la disponibilità a valutare questa strada, la proposta è stata respinta e oggi abbiamo di fronte le primarie». Punto numero due, quello essenziale, la questione dell’invio di armi all’Ucraina: «La proposta di Goffredo Bettini di lavorare a una tregua e inviare nel frattempo solo armi difensive? Serve un cambio di passo, non si può invocare una svolta e continuare a inviare armi come sempre». Il leader del M5s mette due bei bastoni tra le ruote di Elly Schlein, che oggi riunisce la direzione del Pd per affrontare la proroga del suo mandato a dopo le elezioni (sarà l’assemblea nazionale convocata domenica 18 ottobre a votare in tal senso), ribadire la sua disponibilità a fare le primarie e la sua indisponibilità al passo indietro, invocare l’allargamento dell’alleanza Pd-M5s-Avs al centro e quindi la piena cittadinanza di Matteo Renzi con la sia Casa riformista/Italia Viva nell’alleanza. Insomma, la segretaria chiede al Pd di compattarsi sulla sua leadership interna e sulla sua candidatura alle primarie di coalizione. Ma Conte sa benissimo che mezzo Pd vorrebbe evitare le primarie e indicare un non meglio specificato ”federatore”. E sa benissimo che la questione dell’invio di armi all’Ucraina è principio non negoziabile per la minoranza dei riformisti dem che fa capo al presidente del Copasir Lorenzo Guerini. Continua insomma l’estate arrembante all’indirizzo del Pd dell’ex premier, anche se l’estate è ormai finita.""",
    "category": "Politica",
    "page": 10,
    "isHighlight": False
})

# 14. Page 10: Enti locali, ok al contratto: aumenti da 151 euro
articles.append({
    "id": "art-14",
    "title": "Enti locali, ok al contratto: aumenti da 151 euro",
    "subtitle": "In Consiglio dei ministri",
    "body": """di Gianni Trovati

Dal consiglio dei ministri di domani dovrebbe arrivare il via libera al contratto 2025/2027 per i 403.617 dipendenti di Regioni ed enti locali. La preintesa, firmata all’Aran il 21 luglio scorso, ha infatti superato (senza intoppi) le verifiche alla Ragioneria generale dello Stato. E dopo il passaggio in consiglio dei ministri potrà dunque andare alla Corte dei conti per la certificazione, da assicurare in 15 giorni lavorativi, e poi alla firma definitiva tra l’Agenzia negoziale del pubblico impiego e i sindacati. Gli effetti potrebbero quindi farsi sentire sulla busta paga di novembre, o al più tardi su quella successiva.

I 989 milioni di euro mossi a regime dal contratto si tradurranno in un aumento medio mensile da 151 euro lordi nei Comuni, gli enti largamente maggioritari nel comparto, e da 141 euro nelle altre amministrazioni. La differenza si spiega con l’attivazione del fondo di perequazione (50 milioni sul 2027, 100 dal 2028) riservato al supporto degli stipendi nei municipi. Gli arretrati medi valgono poco meno di 1.200 euro. Con la firma al contratto delle Funzioni locali si chiuderà il rinnovo 2025/27 nei comparti del pubblico impiego, traguardo raggiunto per la prima volta nel corso del periodo di riferimento. Con la conseguenza, dunque, che la strada degli aumenti si completerà il prossimo anno.""",
    "category": "Politica",
    "page": 10,
    "isHighlight": False
})

# 15. Page 10: Concessioni balneari, l’Ue: procedura ancora aperta
articles.append({
    "id": "art-15",
    "title": "Concessioni balneari, l’Ue: procedura ancora aperta",
    "subtitle": "La partita con l’Europa",
    "body": """La Commissione europea monitora l’applicazione del decreto legge sulle concessioni balneari sulle quali la procedura di infrazione, arrivata allo stadio del parere motivato, è «tuttora in corso». A sottolinearlo è stato ieri un portavoce di Bruxelles rispondendo a una domanda sulle linee guida per i bandi di gara per le concessioni balneari che il ministero delle Infrastrutture e dei Trasporti pubblicherà a breve (si veda Il Sole 24 Ore di ieri): «Siamo in costante dialogo con le autorità competenti. È stato adottato un decreto-legge, partendo dal presupposto che tali concessioni balneari termineranno entro il 30 settembre del prossimo anno. Naturalmente stiamo seguendo da vicino l’attuazione di quella legge». Intanto la bozza di bando-tipo suscita pareri negativi da parte degli operatori: «Il provvedimento - afferma il sindacato dei balneari Sib - si inserisce in un contesto legislativo ancora poco chiaro, che non assicura né l’esercizio ordinato delle funzioni amministrative né la corretta applicazione della cosiddetta Direttiva Bolkestein». Serve perciò «un intervento normativo chiarificatore». Critiche arrivano anche dall’assessora regionale al Turismo in Emilia-Romagna, Roberta Frisoni, per la quale «non possono essere scaricate in maniera confusa a Regioni e Comuni adempimenti, responsabilità o decisioni che per loro natura e competenza devono trovare una chiara definizione a livello statale. Il bando-tipo deve servire esattamente al contrario».""",
    "category": "Politica",
    "page": 10,
    "isHighlight": False
})

# 16. Page 10: Sgarbi in terapia intensiva, «condizioni critiche ma stabili»
articles.append({
    "id": "art-16",
    "title": "Sgarbi in terapia intensiva, «condizioni critiche ma stabili»",
    "subtitle": "Apprensione per il critico d’arte",
    "body": "Apprensione per Vittorio Sgarbi. Trasportato d’urgenza mercoledì al policlinico Gemelli di Roma a causa di una «insufficienza respiratoria», è ricoverato in terapia intensiva. In serata il primo bollettino medico in cui è stato reso noto che le sue condizioni «pur critiche sono attualmente stabili».",
    "category": "Politica",
    "page": 10,
    "isHighlight": False
})

# 17. Page 12: Alla Volkswagen riparte lo scontro sul costo del lavoro
articles.append({
    "id": "art-17",
    "title": "Alla Volkswagen riparte lo scontro sul costo del lavoro",
    "subtitle": "Germania. Il gruppo disdetta quasi tutti gli accordi e attacca la settimana corta",
    "body": """di Gianluca Di Donfrancesco

Torna ad accendersi lo scontro sul costo del lavoro della Volkswagen e dell'auto tedesca. Il gruppo automobilistico ha disdetto quasi tutti gli accordi aziendali vigenti con il sindacato Ig Metall, compreso lo storico accordo sulla settimana corta di quattro giorni e sui premi di risultato, chiedendo tagli retributivi nell'ordine del 10% per salvaguardare la competitività dei propri impianti produttivi.

Ancora una volta, la distanza delle posizioni fa presagire uno scontro muro contro muro. Il capo negoziatore di Ig Metall, Thorsten Gröger, ha definito la decisione dell'azienda un nuovo «tentativo di mettere le mani nelle tasche dei lavoratori». Secondo la rappresentanza dei lavoratori, gli accordi disdetti sarebbero dieci e riguarderebbero circa 120mila dipendenti impiegati nei sei principali stabilimenti tedeschi del marchio Volkswagen. Non sarebbe stata toccata, invece, la garanzia occupazionale, contrattata con il consiglio di fabbrica, che blinda gli stabilimenti tedeschi da licenziamenti collettivi fino al 2030. Nell'interpretazione del sindacato, questa intesa sarebbe inderogabile.

Il piano di ristrutturazione dell'amministratore delegato, Oliver Blume, che prevede una riduzione dei costi operativi per miliardi di euro e la possibile chiusura di alcuni impianti in Germania, si scontra frontalmente con le richieste sindacali. Ig Metall ha infatti chiesto un aumento salariale del 5% per il settore elettrico e metalmeccanico. La crisi dell'auto (e dell'industria) tedesca, stretta tra la difficile transizione all'elettrico, il crollo delle vendite sul mercato cinese e la concorrenza asiatica, rischia di innescare una stagione di scioperi a partire dall'autunno. Prima di Volkswagen, già Mercedes-Benz aveva aperto il confronto, chiedendo sacrifici e flessibilità per difendere i margini operativi.""",
    "category": "Economia e politica internazionale",
    "page": 12,
    "isHighlight": False
})

# 18. Page 12: Attacco a base Raf, arrestato britannico-iraniano
articles.append({
    "id": "art-18",
    "title": "Attacco a base Raf, arrestato britannico-iraniano",
    "subtitle": "",
    "body": "Un uomo di 27 anni con doppia cittadinanza britannica e iraniana è stato arrestato nel quartiere di Westminster a Londra con l’accusa di aver preparato atti terroristici in relazione all’incidente avvenuto presso la base Raf di Fairford. Lo ha riferito la polizia antiterrorismo britannica. Un secondo uomo, un cittadino britannico di 26 anni, è stato interrogato in presenza del suo avvocato, e due proprietà nella zona sono state perquisite.",
    "category": "Economia e politica internazionale",
    "page": 12,
    "isHighlight": False
})

# 19. Page 12: Putin: esercitazioni nel Baltico escalation
articles.append({
    "id": "art-19",
    "title": "Putin: esercitazioni nel Baltico escalation",
    "subtitle": "Tensione Russia-Nato",
    "body": "Il presidente russo Vladimir Putin ha definito le esercitazioni militari occidentali nel Mar Baltico e i tentativi di fermare le navi russe «un’escalation» durante il 23esimo incontro del think thank Valdai. Qualora la sua exclave di Kaliningrad (territorio russo fortemente militarizzato racchiuso tra Polonia, Lituania e Mar Baltico) fosse attaccata, Putin ha ribadito che «diventerebbe inevitabile l’uso da parte russa di tutte le armi disponibili», aggiungendo però che Mosca «non ha intenzione di attaccare nessuno».",
    "category": "Economia e politica internazionale",
    "page": 12,
    "isHighlight": False
})

# 20. Page 12: Trump non esclude stato di emergenza
articles.append({
    "id": "art-20",
    "title": "Trump non esclude stato di emergenza",
    "subtitle": "Verso il midterm",
    "body": "Il presidente Usa Donald Trump non esclude di dichiarare un’emergenza nazionale o di ricorrere all’Insurrection Act durante le elezioni di metà mandato a novembre. Interpellato dal Time, ha dichiarato: «Non escludo né confermo nulla. Non l’ho mai usato. Potrei usarlo. Molti pensano che dovrei usarlo ogni tanto». Parole che arrivano mentre il suo gradimento è ai minimi storici e i repubblicani rischiano di perdere le elezioni.",
    "category": "Economia e politica internazionale",
    "page": 12,
    "isHighlight": False
})

# 21. Page 12: Donna sopravvive a due iniezioni letali
articles.append({
    "id": "art-21",
    "title": "Donna sopravvive a due iniezioni letali",
    "subtitle": "Tennessee",
    "body": "Fallita l’esecuzione di Christa Pike, 50enne condannata a morte negli Usa. Mercoledì la donna è sopravvissuta a due tentativi di iniezione letale in un carcere di Nashville ed è stata trasportata in ospedale. Per ora non ci sono aggiornamenti sulle sue condizioni. Negli anni 90 Pike era stata giudicata colpevole di omicidio. Se fosse morta, sarebbe stata la prima donna giustiziata dal Tennessee in oltre due secoli. Sospese per il resto dell’anno le esecuzioni programmate nello stato. Terze parti revisioneranno quanto accaduto a Pike.",
    "category": "Economia e politica internazionale",
    "page": 12,
    "isHighlight": False
})

# 22. Page 12: Inchiesta su stupro di gruppo al campus
articles.append({
    "id": "art-22",
    "title": "Inchiesta su stupro di gruppo al campus",
    "subtitle": "Cornell University",
    "body": "Riaperta l’inchiesta sul presunto stupro di gruppo di una studentessa della Cornell University di Ithaca, nello Stato di New York. La donna denunciò il fatto, avvenuto sotto influenza di droghe e alcol, nel 2024. Le violenze sarebbero durate 7 ore, durante cui un messaggio di invito, volgare e sessista, fu condiviso sul gruppo Snapchat della confraternita. L’università aprì un’inchiesta interna: due studenti furono espulsi, gli altri coinvolti dovettero scrivere dei saggi. Lei, che aveva 20 anni, lasciò l’università.",
    "category": "Economia e politica internazionale",
    "page": 12,
    "isHighlight": False
})

# 23. Page 13: Google maps fotografa la distruzione a Gaza dopo tre anni di guerra
articles.append({
    "id": "art-23",
    "title": "Google maps fotografa la distruzione a Gaza dopo tre anni di guerra",
    "subtitle": "Le immagini satellitari. I raid israeliani hanno ridisegnato la Striscia in macerie e tendopoli",
    "body": """di Rosalba Reggio

È una fotografia di devastazione quella offerta da Google maps su Gaza. L’ha pubblicata il Guardian, mettendo a confronto le immagini di diverse zone della Striscia prima dell’azione militare israeliana e dopo tre anni di guerra.

Nel 2023, per esempio, ad Al-Mawasi, nell’area costiera vicino a Rafah, si potevano osservare ampie aree agricole e costruzioni sparse: un insieme di campi, serre, frutteti, dune sabbiose e vegetazione, dove ogni tanto si distingueva un edificio. A giugno 2026 l’immagine dall’alto mostra una densissima distesa di tende e ricoveri temporanei che arriva fino alla costa.

A Tel al-Sultan, a nord ovest di Rafah, prima del 7 ottobre 2023 le immagini documentavano un quartiere residenziale densamente popolato, con abitazioni, strade, negozi e servizi. Si trattava di un progetto abitativo per rifugiati palestinesi. Nell’area sorgeva anche un centro sanitario dell’Unrwa che prima della guerra forniva centinaia di visite al giorno. Oggi vaste porzioni dell’area sono rase al suolo, con ampie superfici di macerie e terreno spianato.

Nel quartiere di Ma’an, nella parte orientale di Khan Younis, si alzava una grande moschea circondata da un quartiere residenziale. L’edificio contava una cupola e un minareto. Oggi il luogo di culto è stato distrutto e anche intorno numerosi edifici risultano crollati o gravemente danneggiati.

Nel 2023, a nord di Gaza, esisteva una città con densi quartieri residenziali e una forte componente agricola, Beit Lahiya. L’area era famosa per le fragole, gli ortaggi e i frutteti. Nelle foto satellitari del 2023, si vedevano abitazioni, strade e appezzamenti agricoli intervallati da costruzioni. Una città, insomma, con case, condomini, negozi, scuole, moschee, strutture sanitarie. L’ospedale, il Kamal Adwan Hospital, era una delle principali strutture della zona. Le fotografie del 2026 mostrano ampie porzioni del tessuto urbano frammentate o cancellate; molti isolati sono diventati cumuli di macerie, mentre restano visibili solo i tracciati stradali che danno qualche indicazione della struttura precedente della città.

Già nel 2024, dopo poco più di un anno di guerra, l’Organizzazione Mondiale della Sanità aveva dichiarato l’ospedale Kamal Faori fuori servizio, in seguito a un raid israeliano e ripetuti attacchi che avevano gravemente danneggiato laboratorio, sala operatoria, reparti tecnici e magazzino medico.""",
    "category": "Economia e politica internazionale",
    "page": 13,
    "isHighlight": False,
    "media": [
        {
            "type": "photo",
            "caption": "Gaza prima e dopo la guerra. Le immagini di Google Maps di Al-Mawasi a Rafah nel 2023 (a sinistra) e nel 2026 (a destra), pubblicate dal Guardian",
            "box": [797, 56, 945, 347],
            "page": 13
        }
    ]
})

# 24. Page 13: I bulli dell’amministrazione Usa
articles.append({
    "id": "art-24",
    "title": "I bulli dell’amministrazione Usa",
    "subtitle": "Nuove regole al Pentagono e la guerra del futuro con il ruolo di Musk",
    "body": """Al Pentagono soffia il vento della restaurazione trumpiana con le nuove regole annunciate dal segretario alla Difesa Pete Hegseth: «Non siamo più il Dipartimento “woke”, né dei deboli: niente ciccioni, trans, barbuti, tipi strani, smidollati, radicali. Solo guerrieri».

Nel contempo Elon Musk, boss di SpaceX e Tesla già responsabile del Doge, torna ad assumere un ruolo operativo di primo piano nell'amministrazione: guiderà il Project Meridian del Pentagono, incentrato sull'esercito, l'intelligenza artificiale e le nuove tecnologie per permettere agli Stati Uniti di mantenere il dominio strategico globale.""",
    "category": "Economia e politica internazionale",
    "page": 13,
    "isHighlight": False
})

# 25. Page 13: Palestinese ucciso dai coloni
articles.append({
    "id": "art-25",
    "title": "Palestinese ucciso dai coloni",
    "subtitle": "",
    "body": "Un palestinese di 51 anni, secondo l’agenzia Wafa, è stato ucciso dopo essere stato colpito da coloni israeliani durante un attacco al villaggio di Yasuf, nella Cisgiordania centrale. Quattro attivisti sono stati feriti dai coloni a sud di Betlemme. L’Idf ha invece reso noto ieri di aver ucciso mercoledì un membro della Jihad islamica a Gaza.",
    "category": "Economia e politica internazionale",
    "page": 13,
    "isHighlight": False
})

# 26. Page 15: Lula, il vecchio leone della sinistra punta al quarto mandato
articles.append({
    "id": "art-26",
    "title": "Lula, il vecchio leone della sinistra punta al quarto mandato",
    "subtitle": "L’uomo della continuità. Il leader del Partito dei lavoratori, 80 anni, rilancia il suo modello sociale. Dalle lotte operaie al boom del Brasile, dal carcere fino all’ultima candidatura",
    "body": """di Roberto Da Rin

Nelle piazze affollate di San Paolo così come nei talk-show delle tv brasiliane sonoriprotagonisti i vecchi fantasmi: una campagna elettorale giocata senza esclusione di colpi, ma di senso profondamente storico. Al centro di questo immenso palcoscenico c'è un uomo che per decenni è stato l'emblema del riscatto e per altre decine di milioni l'immagine più difficile da battere. Un leader la cui biografia si intreccia indissolubilmente con la storia del Brasile: Luiz Inácio Lula da Silva.

A 80 anni compiuti, l'ex sindacalista dall'iconica voce rauca cerca il suo quarto mandato presidenziale. Ha attraversato tutte le stagioni della politica brasiliana: dalle lotte operaie contro la dittatura ai fronti degli anni Duemila, dalle polveri del carcere all'incredibile resurrezione che lo ha riportato al Planalto. Eppure, per il vecchio leone della sinistra, questa campagna elettorale somiglia a una traversata nel deserto più insidiosa delle precedenti. Nonostante una solida base di partenza nei sondaggi, la sensazione diffusa è che il Paese reale sia spaccato in due blocchi speculari e inconciliabili.

Sul tavolo del presidente, il dossier più delicato è lo scandalo del Banco Master che fa tremare i palazzi del potere a Brasilia. Quella che era nata come un'indagine su una colossale frode bancaria orchestrata dal finanziere Daniel Vorcaro si è trasformata, a poche settimane dal voto, in un terremoto istituzionale che lambisce la Corte Suprema. I messaggi criptati estratti dai telefoni degli indagati hanno scoperchiato nel fango persino Alexandre de Moraes, il potente giudice simbolo della lotta della difesa democratica brasiliana, offrendo munizioni retoriche letali ai detrattori del governo.

Per arginare l'emorragia di voti che nelle ultime settimane ha ridimensionato il numero di consensi a suo favore, Lula gioca l'asso, quello che in altre occasioni ha suggellato il suo legame forte con le masse popolari: la Bolsa Família. Il programma di assistenza sociale, simbolo storico dei governi del Partido dos Trabalhadores, è stato potenziato da 102 a 118 euro al mese. Più soldi nelle tasche dei poveri, più sussidi per le famiglie. Nelle favelas di Rio e nelle comunità rurali, questo incremento non è solo una statistica economica, ma una rete di salvataggio vitale che spinge milioni di dimenticati a rinnovare la fiducia al vecchio leader. L'ultimo annuncio è la distribuzione gratuita, nell'ambito del Sistema sanitario nazionale, dei farmaci antiobesità. Un'altra scelta ad effetto della sua campagna elettorale riguarda lo stop alle scommesse online che «distruggono i redditi delle famiglie e danneggiano la salute mentale dei brasiliani». Lo ha dichiarato lo stesso Lula.

Ma i soldi non bastano a conquistare l'anima di un Brasile profondamente mutato nella sua composizione sociale e spirituale. La vera trincea di questa campagna elettorale si gioca nei banchi delle numerosissime chiese evangeliche che punteggiano il territorio nazionale. Gli elettori evangelici, un tempo marginali e oggi blocco demografico e politico decisivo, rappresentano l'ago della bilancia per conquistare la maggioranza assoluta. Storicamente vicini alle posizioni conservatrici della destra sul piano dei valori familiari e sociali, questi fedeli sono l'oggetto di una contesa spietata.

Lula ne è consapevole: vincere senza di loro è matematicamente impossibile. Per questo, la strategia della sinistra ha dovuto smussare gli angoli ideologici, tentando un dialogo difficile e a tratti contraddittorio con i pastori e le comunità di fede, cercando di dimostrare che la lotta alla povertà cammina di pari passo con il rispetto della fede cristiana. È una guerra di simboli e di parole d'ordine, dove ogni dichiarazione può spostare centinaia di migliaia di voti. Lula, instancabile navigatore di mille tempeste, si prepara alla sua ultima traversata politica.""",
    "category": "Economia e politica internazionale",
    "page": 15,
    "isHighlight": False
})

# 27. Page 15: Bolsonaro Jr recupera nei sondaggi e prova la scalata ultraliberista
articles.append({
    "id": "art-27",
    "title": "Bolsonaro Jr recupera nei sondaggi e prova la scalata ultraliberista",
    "subtitle": "Il figlio del golpista. Flavio raccoglie i voti di quella fascia di elettori moderati ma anti-Lula. Una candidatura vista come aggregatrice contro l’egemonia della sinistra",
    "body": """di Roberto Da Rin

Non è facile seguire le orme di un gigante del populismo latinoamericano, specialmente se quel gigante è tuo padre. Eppure, a 45 anni, Flavio Nantes Bolsonaro, primogenito di Jair Bolsonaro, ineleggibile, ci prova.

La destra conservatrice brasiliana ha scelto lui, ex deputato statale e attuale senatore di Rio de Janeiro. Flavio cercherà di riconquistare il Brasile. Corporatura massiccia, stile decisamente più felpato rispetto alle ruvidezze paterne, incarna il tentativo di istituzionalizzare il bolsonarismo, trasformando la rabbia incendiaria della piazza in una strategia di potere fredda e calcolata. Una scommessa che, contro ogni previsione iniziale, sta pagando. Negli ultimi due mesi, la macchina dei sondaggi elettorali ha registrato un forte recupero a suo vantaggio: il distacco siderale, più di 15 punti percentuali, che lo separava da Lula si è progressivamente accorciato, trasformandosi, a ridosso del voto, in un serratissimo testa a testa strategico.

La benzina che alimenta il motore della sua rimonta è un sentimento viscerale, profondo e mai sopito: la galassia dell'elettorato anti-Lula. Per milioni di brasiliani, Flavio non è semplicemente un candidato, ma l'unico scudo disponibile contro il ritorno dell'egemonia della sinistra, un aggregatore di voti disposto a tutto pur di sbarrare la strada al Partido dos Trabalhadores.

A blindare la sua ascesa non c'è però solo l'ideologia, ma il pilastro più pesante dell'economia nazionale. La sua linea politica ultraliberista, fatta di promesse di deregolamentazione selvaggia, privatizzazioni e tagli fiscali radicali, continua a sedurre la potentissima lobby dell'agribusiness, i re della soia e del bestiame che dominano le sterminate pianure del Brasile. Per i grandi proprietari terrieri, Flavio rappresenta il via libera definitivo alle frontiere agricole, la garanzia che lo Stato non interferirà con i profitti della terra. A questa robusta macchina di consenso interno si aggiunge un prestigioso sigillo internazionale: l'asse preferenziale con Donald Trump. Il legame con il leader americano, ostentato come una medaglia d'oro, conferisce a Bolsonaro Jr lo status di interlocutore globale della nuova destra.

Eppure, dietro la lucida facciata della rimonta, i critici intravedono crepe profonde. Il peccato originale della sua candidatura è l'eredità dinastica: per molti, Flavio resta un leader dimezzato, un clone politico privo del carisma magnetico del padre e catapultato ai vertici solo per ragioni di sangue. Senza il cognome Bolsonaro, la sua parabola politica difficilmente avrebbe superato i confini dello Stato di Rio de Janeiro.

Un altro limite strutturale della sua candidatura è rappresentato dal suo elettorato: nonostante le aperture centriste, il nucleo duro resta ancorato a posizioni radicali che allontanano l'elettorato moderato, specialmente tra le donne e i giovani. Il punto più scoperto del suo programma è l'assenza totale di un'idea di sviluppo organica per il Paese. La sua proposta economica appare schiacciata sugli interessi immediati dei suoi grandi investitori: una ricetta che promette i giganti dell'export agricolo ma che non offre risposte strutturali alla complessa crisi industriale o alle storiche disuguaglianze delle metropoli. Una visione subordinata alle dinamiche esterne e al desiderato geopolitico di Trump, che rischia di trasformare il colosso sudamericano nel backyard americano, quello smisurato cortile di casa a lungo temuto dai nazionalisti brasiliani. Tra presente e futuro, sospeso dal vento dell'anti-populismo, ma sospeso sul dubbio più grande: la capacità di essere un vero statista alla guida di un grande Paese.""",
    "category": "Economia e politica internazionale",
    "page": 15,
    "isHighlight": False
})

# 28. Page 16: La certezza del diritto è vitale per le imprese
articles.append({
    "id": "art-28",
    "title": "La certezza del diritto è vitale per le imprese",
    "subtitle": "Made in Italy",
    "body": """di Claudia Eccher

Quando si parla di competitività del Made in Italy, l’attenzione va quasi sempre alla qualità del prodotto, al design e alla tradizione manifatturiera. C’è però un fattore immateriale ma decisivo che incide direttamente sulla fiducia e sulla tenuta delle relazioni commerciali: la certezza del diritto.

Nelle transazioni internazionali, la prevedibilità delle regole e la celerità della loro applicazione costituiscono una vera e propria variabile economica fondamentale. Per un’impresa che opera all’estero, il rischio giuridico è rischio finanziario. L’incertezza normativa e le oscillazioni interpretative generano costi di transazione aggiuntivi, che vanno dalle garanzie fideiussorie più onerose fino ai premi assicurativi per tutelarsi da eventuali vertenze all’estero.

Per questo le riforme della giustizia legate al Pnrr non sono un mero adempimento burocratico per ottenere i fondi europei, ma una profonda ristrutturazione dell’infrastruttura economica nazionale. I target fissati per il 2026 sono stati raggiunti: meno 40% del disposition time nel civile, meno 25% nel penale e arretrato ultratriennale abbattuto del 90 per cento. Il punto, ora, è consolidare questi risultati nel tempo. L’Ufficio per il processo ha introdotto una modalità di lavoro in équipe, affiancando stabilmente il giudice nell’attività preparatoria e organizzativa. La digitalizzazione conta soprattutto per l’accessibilità della giurisprudenza: orientamenti stabili e la piena conoscibilità delle banche dati, prevedibilità delle decisioni. A ciò contribuiscono anche le Sezioni specializzate per l’impresa e l’arbitrato internazionale, le cui decisioni sono eseguibili in oltre 170 Paesi.

La certezza del diritto, però, non dipende soltanto dall’efficienza dei tribunali. Anche le imprese possono ridurre il rischio giuridico nelle proprie strategie di internazionalizzazione, trasformando la gestione del rischio legale da costo in asset strategico. Lo dimostrano le recenti missioni di sistema in America Latina, dove l’area Mercosur vale già 14 miliardi per l’Italia.

Gli strumenti vanno dalla tutela della proprietà intellettuale, dal Brevetto unitario all’impiego di tecnologie come la Blockchain e alle clausole contro l’Italian sounding ai contratti standardizzati, con clausole di hardship e forza maggiore contro sanzioni e dazi, fino al rafforzamento della compliance aziendale. Sul piano istituzionale, sarebbe utile affiancare alla diplomazia economica una vera e propria diplomazia giuridica, rafforzando la cooperazione con i Paesi extra-Ue.

Resta la direttiva europea sulla due diligence di sostenibilità, la CS3D, che impone obblighi trasversali lungo tutta la catena del valore. L’efficienza della giustizia non è una questione confinata nei tribunali: è politica economica. Tempi certi, decisioni prevedibili e tutele efficaci sono la garanzia che il Sistema Paese deve offrire a chi esporta e a chi investe in Italia, per tutelare l’eccellenza del Made in Italy e consolidare il nostro ruolo nel commercio globale.""",
    "category": "Commenti",
    "page": 16,
    "isHighlight": False
})

result = {
    "newspaperName": newspaper_name,
    "date": date_str,
    "articles": articles
}

with open('/tmp/batch_1_generated.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Generated {len(articles)} articles. Testing valid JSON...")
with open('/tmp/batch_1_generated.json', 'r', encoding='utf-8') as f:
    test = json.load(f)
print("Valid JSON! Total articles:", len(test['articles']))
