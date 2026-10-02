# -*- coding: utf-8 -*-
import json
import fitz

doc = fitz.open('uploads/1790952596400-Il Sole 24 Ore 02 Ottobre 2026.pdf')

newspaper_name = "Il Sole 24 Ore"
date_str = "2026-10-02"

articles = []

# ==========================================
# HIGHLIGHTS FIRST (Rule 7: highlights prima)
# ==========================================

# 1. Page 15: Brasile al voto (Highlight)
articles.append({
    "id": "art-1",
    "title": "Brasile al voto, testa a testa in un Paese diviso tra sinistra dogmatica e populismo",
    "subtitle": "Elezioni presidenziali. I sondaggi: pareggio tecnico tra Lula e Bolsonaro. Ballottaggio quasi certo",
    "body": """di Roberto Da Rin

L’aria che si respira lungo i viali geometrici di Brasilia, nelle congestionate arterie di San Paolo tra i grattacieli o ai piedi dei morros di Rio, condensa una promessa e una minaccia. La tensione che attraversa le famiglie e i quartieri si divide tra l’elettorato su due fazioni contrapposte. La campagna del primo turno delle elezioni presidenziali del Brasile, in programma domenica, si consuma in uno scontro all’ultimo voto tra due modelli politici, economici e persino antropologici: da una parte il presidente uscente, Luiz Inácio Lula da Silva, 80 anni, icona della sinistra e paladino della spesa sociale. Dall’altra il senatore Flavio Bolsonaro, 45 anni, erede politico del padre Jair e alfiere del conservatorismo e del liberismo economico.

I dati emersi dagli ultimi sondaggi fotografano un Paese letteralmente spaccato in due. Le rilevazioni di Datafolha e i dati freschi degli istituti Real Time Big Data e Meio/Ideia danno l’immagine chiara di pareggio tecnico. Al primo turno, Lula si attesta in una forbice compresa tra il 39% e il 41%, tallonato da Flavio Bolsonaro, che oscilla tra il 36% e il 38%. Con un margine di errore del due per cento e una quota di indecisi che supera ancora il 10%, la certezza matematica è una sola: nessuno dei due candidati riuscirà a superare la soglia fatidica del 50% più uno dei voti validi per chiudere la partita al primo turno. Il Brasile si prepara così a un mese di passione che culminerà nel ballottaggio di fine ottobre.

Sullo sfondo di questa trincea ideologica si staglia un quadro economico complesso, segnato da luci e ombre che alimentano le opposte narrazioni. Da un lato, il governo rivendica con orgoglio i risultati sul fronte della crescita del Pil, che quest'anno dovrebbe attestarsi attorno al 2,5%, superando le previsioni iniziali degli analisti. L'inflazione, pur risalita al 4,8% negli ultimi mesi a causa della siccità che ha colpito i prezzi alimentari e dell'energia elettrica, resta all'interno della banda di tolleranza della Banca Centrale. E il tasso di disoccupazione, sceso al 6,9%, tocca i minimi storici dal 2014, trainato dalla ripresa dei servizi e dal dinamismo del settore agricolo.

Dall'altro lato, però, l'opposizione bolsonarista punta il dito contro il deterioramento dei conti pubblici, diventato il tallone d'Achille della gestione Lula. Il debito pubblico ha subito un'impennata preoccupante, superando l'82,5% del Pil e sfondando la cifra nominale di 11mila miliardi di reais (circa 1.800 miliardi di euro). A pesare è soprattutto il disavanzo primario, che il ministro dell'Economia Fernando Haddad non è riuscito ad azzerare nonostante i ripetuti annunci e le nuove misure fiscali. I mercati guardano con crescente nervosismo alla spesa pubblica corrente, sostenuta dai generosi programmi di welfare come Bolsa Família e dall'aumento reale del salario minimo, entrambi pilastri del consenso lulista.

La polarizzazione non risparmia nemmeno il potente settore dell'agribusiness, che da solo rappresenta quasi un quarto del Pil brasiliano. Se i grandi produttori di soia e carne del Centro-Ovest guardano storicamente con favore alle ricette liberiste e alle deregulation ambientali promesse da Bolsonaro, una parte non trascurabile della filiera comincia a temere le ritorsioni commerciali internazionali e i rischi legati all'accordo Ue-Mercosur nel caso di un ritorno dell'estrema destra al potere.

Domenica oltre 156 milioni di elettori sono chiamati alle urne elettroniche. Il voto è obbligatorio tra i 18 e i 70 anni. La campagna elettorale, segnata da toni aspri e da una disinformazione martellante sui social network, si chiude senza che nessuno dei due schieramenti sia riuscito a piazzare il colpo decisivo. Il futuro del colosso sudamericano resta sospeso su un filo sottile.""",
    "category": "Economia e politica internazionale",
    "page": 15,
    "isHighlight": True
})

# 2. Page 16: I cinque scenari che incalzano l’Unione Europea (Highlight)
articles.append({
    "id": "art-2",
    "title": "I cinque scenari che incalzano l’Unione Europea",
    "subtitle": "Le sfide della Ue",
    "body": """di Luigi Zanda

Il 16 settembre, a Strasburgo, Ursula von der Leyen ha svolto il discorso sullo stato dell'Unione. Un discorso solenne, molto politico, da capo di Stato. Nell'organigramma del potere europeo la posizione della presidente della Commissione la rende in qualche modo libera, super partes, al di sopra dei singoli Governi nazionali. E libera von der Leyen è apparsa nel delineare un quadro realistico e crudo delle sfide che attendono l'Europa. Sfide che possono essere riassunte in cinque scenari interconnessi, da cui dipenderà la sopravvivenza stessa del progetto europeo.

1. Sicurezza e difesa comune. Il ritorno della guerra sul continente europeo dopo l'aggressione russa all'Ucraina ha spazzato via trent'anni di illusioni sulla "fine della storia". L'Europa non può più delegare la propria sicurezza all'alleato americano, a prescindere da chi siederà alla Casa Bianca dopo le elezioni di novembre. Serve un vero pilastro europeo della Nato, investimenti coordinati nella difesa, appalti comuni per superare la frammentazione degli armamenti nazionali (in Europa si contano 27 diversi sistemi d'arma principali contro i 4 degli Stati Uniti) e la creazione di una capacità di reazione rapida realmente operativa.

2. Competitività e industria. Il rapporto di Mario Draghi ha certificato un divario drammatico di produttività e innovazione tra l'Unione Europea, gli Stati Uniti e la Cina. L'Europa sconta costi energetici doppi o tripli rispetto ai concorrenti, un mercato unico dei capitali ancora frammentato che costringe le nostre migliori startup a cercare finanziamenti oltreoceano, e un carico burocratico che asfissia le imprese. Per colmare questo gap servono investimenti congiunti per almeno 800 miliardi di euro all'anno, una parte consistente dei quali dovrà essere finanziata con debito comune europeo.

3. Transizione verde ed energetica. Il Green Deal resta la rotta strategica dell'Unione, ma deve fare i conti con la realtà sociale ed economica. Non si può fare la transizione contro l'industria o contro i cittadini. La deindustrializzazione di settori chiave, a partire dall'automotive, rischia di consegnare intere filiere alla Cina e di alimentare il risentimento popolare. Occorre pragmatismo tecnologico, neutralità nelle soluzioni e massicci incentivi pubblici per accompagnare la riconversione senza distruggere posti di lavoro.

4. Allargamento e riforme istituzionali. L'integrazione di Ucraina, Moldavia e dei Balcani occidentali è una necessità geopolitica inderogabile per sottrarre questi Paesi all'influenza russa e cinese. Ma un'Unione a oltre trenta Stati membri non può funzionare con le regole attuali. Il principio dell'unanimità nel Consiglio, soprattutto in materia di politica estera e di fiscalità, è diventato una trappola che paralizza le decisioni ed espone l'Unione al ricatto dei singoli veti nazionali. Serve il passaggio generalizzato al voto a maggioranza qualificata.

5. Tecnologia e sovranità digitale. Il cambiamento tecnologico e l'avvento dell'intelligenza artificiale stanno ridisegnando gli equilibri geopolitici e l'economia del pianeta. L'Europa rischia di ridursi a semplice colonia digitale, consumatrice passiva di tecnologie sviluppate in California o a Shenzhen. Il controllo delle infrastrutture critiche, dal cloud ai cavi sottomarini, dai semiconduttori avanzati alle reti di comunicazione quantistica, è una questione di sovranità nazionale ed europea. Senza campioni tecnologici europei e senza un mercato unico digitale integrato, l'autonomia strategica dell'Unione resterà una formula vuota.

Questi cinque scenari non sono capitoli separati ma tasselli di un unico mosaico. Richiedono una leadership coraggiosa e una cessione di sovranità che molti governi nazionali esitano ancora a compiere. Ma il tempo delle mezze misure è scaduto: o l'Europa compie il salto federale, oppure imboccherà la strada di un lento e inesorabile declino.""",
    "category": "Commenti",
    "page": 16,
    "isHighlight": True
})

# 3. Page 17: Francesco e l’economia: semi di responsabilità sociale e fiscale per il futuro (Highlight)
articles.append({
    "id": "art-3",
    "title": "Francesco e l’economia: semi di responsabilità sociale e fiscale per il futuro",
    "subtitle": "Gli ottocento anni dalla morte del santo/1",
    "body": """di Marco Allena

San Francesco non ha parlato di fisco. Né avrebbe potuto farlo nei termini nei quali oggi intendiamo il fenomeno tributario, che, soprattutto nella sua dimensione moderna, presuppone assetti istituzionali, funzioni pubbliche e meccanismi di redistribuzione della ricchezza evidentemente estranei alla società del XIII secolo.

Eppure, nell’ottavo centenario della sua morte, tra i molti profili che testimoniano la straordinaria modernità del Santo di Assisi, ve ne è uno che interessa la fiscalità. Il collegamento passa dall’economia e, più precisamente, dal modo di concepire la ricchezza. Come evidenziato in letteratura (da ultimo, tra gli altri, S. Ionta e P. Santori, L’economia di San Francesco. La profezia del poverello d’Assisi e le sfide del presente, Edizioni Città Nuova, 2026), Francesco e la tradizione francescana hanno offerto importanti contributi a quella riflessione sui fenomeni economici che, secoli più tardi, avrebbe trovato sistematizzazione nella scienza economica (e a questo proposito si è anche parlato di una sorta di eterogenesi dei fini, Luigino Bruni). In questa prospettiva, è stato efficacemente rilevato il “paradosso” che accompagna l’esperienza francescana: un carisma che – nel porre al centro “sorella povertà” e il distacco materiale dai beni – diviene, attraverso la successiva elaborazione francescana, una vera e propria scuola economica, dalla quale sarebbero emersi alcuni dei presupposti del moderno spirito dell’economia di mercato (L. Bruni, A. Smerilli, Benedetta economia, Edizioni Città Nuova, 2009). È significativo, ad esempio, che nell’ambito della riflessione francescana del secondo Duecento trovi progressivamente spazio l’idea della “scarsità”, quale elemento rilevante nella determinazione del valore dei beni: un’intuizione destinata ad assumere, molti secoli più tardi, un ruolo centrale nell’elaborazione economica moderna (G. Todeschini, Ricchezza Francescana, il Mulino, 2004) – anche se non mancano prospettive opposte, di carattere economico e metastorico (A. Orain, La confisca del mondo. Storia del capitalismo della finitudine, Einaudi, 2026). Uno degli aspetti più significativi di tale contributo riguarda il modo di concepire il rapporto con i beni e con la ricchezza. L’esperienza di Francesco ha contribuito ad affermare una visione nella quale il possesso e l’impiego dei beni non rilevano soltanto nella sfera individuale, ma anche in rapporto alle esigenze della comunità. La ricchezza assume, così, una dimensione sociale, nella misura in cui il suo impiego produce effetti che trascendono la posizione di chi ne dispone.

La fraternità, l’attenzione agli ultimi e la cura del Creato costituiscono, in questa prospettiva, espressioni diverse di una medesima impostazione. Il rapporto con i beni implica una responsabilità che supera l’interesse di chi ne dispone, e che, secondo categorie proprie della riflessione contemporanea, può essere proiettata anche nel tempo, considerando le conseguenze che le scelte economiche della generazione presente producono su quelle future. È su questo terreno che San Francesco ha gettato alcuni semi dei quali la successiva elaborazione della dottrina sociale della Chiesa avrebbe fatto tesoro, e che, attraverso tale sviluppo, interessano oggi profondamente la fiscalità. È soprattutto nel Magistero più recente che questa eredità assume una specifica rilevanza sul piano tributario. Papa Francesco ha riservato ai temi fiscali un’attenzione – come già osservato su queste colonne – senza pari, collocandoli nel più ampio quadro della solidarietà, della giustizia sociale, della tutela dell’ambiente e del bene comune. In linea con tale prospettiva, il tributo non deve assolvere alla sola funzione di procurare le risorse necessarie alla copertura delle spese pubbliche, ma può e deve concorrere alla redistribuzione della ricchezza, alla correzione degli squilibri economici e sociali e all’orientamento dei comportamenti verso finalità di interesse generale.

Non a caso, nel noto discorso del 2022 a una delegazione dell’Agenzia delle Entrate, Papa Francesco affermava che «il fisco, quando è giusto, è in funzione del bene comune». Tale impostazione emerge con particolare evidenza in due ambiti. Da un lato, nella critica ai paradisi fiscali, e all’evasione in generale, anche in ragione degli effetti che la sottrazione di risorse alla potestà impositiva degli Stati produce sul finanziamento dei servizi pubblici e sull’equa distribuzione degli oneri. Dall’altro, nella tutela dell’ambiente: nella Laudato si’, la “cura della casa comune” porta in primo piano la responsabilità per le conseguenze delle scelte economiche sull’ambiente e sulle generazioni future, rispetto alle quali la leva tributaria può concorrere a orientare i comportamenti. Fiscalità internazionale e fiscalità ambientale costituiscono così manifestazioni diverse di un medesimo principio: le decisioni relative alla produzione, alla disponibilità e all’impiego della ricchezza producono conseguenze che trascendono la posizione del singolo e investono la collettività, anche nella sua proiezione intergenerazionale. È su questo piano che va individuato il collegamento con San Francesco: non tanto nell’anticipazione di soluzioni proprie della fiscalità contemporanea, quanto nell’idea che il rapporto con i beni e con la ricchezza implichi una responsabilità che va oltre la dimensione individuale e si estende alla comunità.

Letta in questa chiave, la funzione extrafiscale del tributo acquista una precisa collocazione: oltre ad assicurare il gettito necessario al finanziamento delle spese pubbliche, la fiscalità può e deve concorrere, nel rispetto dei principi e dei limiti costituzionali, al perseguimento di finalità economiche, sociali e ambientali.

Nel magistero di Leone XIV questa impostazione ha trovato immediatamente ulteriore sviluppo. La Magnifica Humanitas, di fronte alle trasformazioni determinate dall’innovazione tecnologica, e alle nuove forme di concentrazione della ricchezza e del potere economico, richiama espressamente la fiscalità, insieme alle protezioni sociali e alle politiche industriali, tra gli strumenti attraverso i quali intervenire sugli squilibri generati da tali processi. Pur nella radicale diversità dei contesti storici, emerge così una continuità nell’interrogativo di fondo sul rapporto tra economia, ricchezza e bene comune.

Ottocento anni dopo, sarebbe ovviamente improprio attribuire a San Francesco un pensiero fiscale che non ebbe e che non avrebbe potuto avere. È però possibile riconoscere come alcuni principi riconducibili alla sua esperienza siano stati progressivamente sviluppati dalla dottrina sociale della Chiesa, sino ad assumere, nel Magistero più recente, una specifica rilevanza anche sul terreno tributario. Nella straordinarietà del Santo di cui celebriamo gli ottocento anni, anche l’economia e, indirettamente, il fisco restituiscono così la misura della modernità del suo insegnamento: San Francesco non parlò di tributi, ma gettò semi dei quali, a distanza di otto secoli, continuiamo a raccogliere i frutti.

Marco Allena
Preside della Facoltà di Economia e Giurisprudenza, Professore di Diritto Tributario, Università Cattolica del Sacro Cuore""",
    "category": "Commenti",
    "page": 17,
    "isHighlight": True
})

# 4. Page 18: «Maire lancia il primo Its sulla transizione energetica» (Highlight)
articles.append({
    "id": "art-4",
    "title": "«Maire lancia il primo Its sulla transizione energetica»",
    "subtitle": "Lavoro. Il corso parte in novembre a Roma, per colmare il gap tra domanda e offerta. Di Amato: «Valenza sociale enorme per il contributo che può dare sui Neet»",
    "body": """di Cristina Casadei

Non è che «il primo tassello di un grande progetto di formazione sulla transizione energetica». Il presidente e azionista di Maire, Fabrizio Di Amato, ci racconta così il corso Its per diventare Energy transition specialist, che partirà in novembre a Roma e sarà presentato il 6 ottobre, prima alle istituzioni e poi in un open day dedicato ai giovani e alle loro famiglie. Di Amato pensa già oltre questa tappa e spiega il progetto che ha in mente di un grande polo formativo in più regioni: «Partiamo dal Lazio ma poi l’obiettivo è di estendere il progetto anche al nord, in Lombardia e al sud, in Sicilia, a Catania, dove abbiamo recentemente aperto un centro di ingegneria». In Maire l’età media è 42 anni e i dipendenti laureati sono il 74%. Circa il 73% di questi, 6.068 sono ingegneri. Negli ultimi 3 anni sono state fatte 5.150 assunzioni.

Il gruppo ha «collaborazioni e interazioni con oltre venti università, due cattedre finanziate, una in Open innovation and sustainability alla Luiss e una in Chemical Projects Engineering and Management al Politecnico di Milano – continua Di Amato -. Sulla transizione energetica non esistono nel nostro Paese corsi specifici e, proprio per questo, ispirandoci sia ad esperienze italiane, come la Motor valley university dell’Emilia Romagna, sia ad esperienze internazionali come quelle di Harvard e dell’Mit che ho personalmente visitato proprio in vista di questo progetto, abbiamo pensato di creare un ecosistema concentrato su temi strategici, come la transizione energetica, sia per noi che per la società più in generale».

Riferendosi a Maire, Di Amato spiega che «in azienda ci sono due asset, uno è rappresentato dalle persone e dalla loro intelligenza, l’altro dalla proprietà intellettuale. Con il nostro progetto valorizziamo entrambi e diamo il via a un percorso di formazione unico nel nostro Paese. Il nostro elemento distintivo è di essere in grado di attrarre giovani e convincerli a frequentare due anni di un percorso di formazione, che dobbiamo rendere attrattivo». Il percorso vuole avere anche una dimensione internazionale ed attirare giovani di altri Paesi, sulla scia di accordi con tante organizzazioni sociali ed educative impegnate nell’integrazione degli immigrati, per promuovere percorsi di orientamento, formazione e sensibilizzazione sui temi della transizione energetica, per avvicinare i ragazzi e le loro famiglie alle competenze e alle professioni della sostenibilità.

La fondazione Green Innovation ITS Academy nasce su forte impulso del gruppo Maire e risponderà all’esigenza di formare tecnici altamente specializzati nella decarbonizzazione e nell’economia circolare, colmando il divario tra domanda e offerta di lavoro. Per capire meglio cosa stia accadendo, Di Amato dice che bisogna «tornare un po’ indietro, a 20-25 anni fa quando il nostro gruppo in termini dimensionali era molto più piccolo. Contava meno di 1.600 persone contro le 11.400 di oggi di 85 nazionalità, in 50 Paesi. All’epoca l’ossatura dell’organizzazione era molto articolata ed era fatta di molti periti e molti ingegneri delle diverse discipline, dalla chimica alla meccanica, nonché da altre figure di supporto in ambito amministrativo e finanziario. Nel tempo abbiamo visto crescere nell’organizzazione alcune figure tecniche di cui c’è carenza sul mercato: all’aumentare delle nostre dimensioni bisognava aumentare la presenza di determinate risorse e allora abbiamo cominciato a vedere il gap sul mercato. Nella nostra strategia abbiamo fatto un’analisi delle competenze per portare avanti il piano industriale, un piano decennale che richiede uno sforzo enorme. In questo esercizio è stato sviluppato l’Its sulla figura dell’ energy transition specialist».

La collaborazione tra pubblico e privato, in questo caso con la Regione Lazio, rappresenta il grande valore aggiunto, tanto più che l’Its consentirà a chi lo frequenta di ricevere i crediti formativi. Nella Fondazione Green Innovation Its Academy rientrano molti partners: sul fronte industriale Maire, Acea, Kuwait petroleum Italia e Orange Branded, oltre a diverse scuole e università, tra cui il campus biomedico di Roma, Unindustria perform e i Salesiani. Nella partnership da cui è nato l’Its «il pubblico coinvolge in modo attivo il privato che in qualche modo è l’utente della formazione e dà la possibilità di rendere attrattive le professioni. L’accreditamento pubblico consente il riconoscimento dei crediti formativi, per cui se i ragazzi dopo i due anni decidessero di proseguire il percorso all’Università avrebbero già dei crediti. Sono certo che chi intraprenderà questo percorso verrà poi inserito subito in azienda, ma nel caso volesse proseguire gli studi potrà farlo già con un importante bagaglio di crediti. Io stesso arrivo da un percorso di alternanza tra lavoro e studio, ma meno strutturato rispetto a quello che proponiamo noi ai ragazzi. L’obiettivo sociale che ci siamo dati è anche quello di dare il nostro contributo a ridurre i bacini dei Neet e incoraggiare una generazione di ragazzi spesso demotivati dal fatto che il lavoro è difficile da trovare, sull’ambiente non si fa abbastanza per trovare soluzioni e risolvere i problemi, c’è la crisi finanziaria ed uno scenario geopolitico incerto a causa dei conflitti. Personalmente, negli ultimi 3 anni abbiamo assunto più di 5mila persone e questo dimostra che noi crediamo nello sviluppo e vogliamo dare un contributo su questo tema».

Il corso è gratuito e biennale e prevede 1.000 ore di didattica in aula oltre a uno stage in azienda di 800 ore. Si svolgerà nella sede di Maire nell’area Tiburtina, a Roma, vicino al centro di ricerca industriale Nextchem che sarà una delle palestre per gli allievi dei corsi e sarà utilizzata anche per spiegare alle istituzioni la produzione di idrogeno verde e le altre soluzioni tecnologiche per la transizione energetica, grazie a numerosi impianti pilota e laboratori di ricerca. «È una vera formazione didattica e applicata che porterà alla formazione di super periti con un accreditamento pubblico - conclude Di Amato -. Il percorso ha un valore sociale molto importante. Nel nostro mondo ci sono periti o ingegneri. Spesso ci sono ragazzi che non si sentono pronti per intraprendere un percorso universitario sia che provengano da istituti tecnici che da licei. Avere frequentato il nostro Its consente di avere crediti, trovare un posto di lavoro e magari proseguire il proprio percorso di formazione».""",
    "category": "Imprese & Territori",
    "page": 18,
    "isHighlight": True,
    "media": [
        {
            "type": "photo",
            "caption": "Le Torri. La sede Maire a Milano",
            "box": [270, 640, 459, 730],
            "page": 18
        }
    ]
})

# ==========================================
# NON-HIGHLIGHT ARTICLES (Order of appearance)
# ==========================================

# 5. Page 15: Lula, il vecchio leone della sinistra punta al quarto mandato
articles.append({
    "id": "art-5",
    "title": "Lula, il vecchio leone della sinistra punta al quarto mandato",
    "subtitle": "L’uomo della continuità. Il leader del Partito dei lavoratori, 80 anni, rilancia il suo modello sociale. Dalle lotte operaie al boom del Brasile, dal carcere fino all’ultima candidatura",
    "body": """di Roberto Da Rin

Nelle piazze affollate di San Paolo così come nei talk show delle tv brasiliane non si percepisce soltanto il confronto tra due candidati, ma lo scontro tra due epoche. Un leader la cui biografia si intreccia con la storia stessa del Paese: Luiz Inácio Lula da Silva.

A 80 anni compiuti, l'ex sindacalista dall'iconica voce roca cerca il suo quarto mandato presidenziale. Una parabola politica senza eguali in America Latina: dalle lotte operaie negli stabilimenti automobilistici dell'ABC paulista durante la dittatura militare alla fondazione del Partido dos Trabalhadores (PT); dalla travolgente vittoria del 2002 che portò alla presidenza il primo operaio brasiliano, artefice del boom economico e dei programmi sociali che hanno sottratto oltre 30 milioni di persone alla povertà estrema, fino alla rovinosa caduta nell'inchiesta Lava Jato, con 580 giorni di carcere a Curitiba prima dell'annullamento delle condanne per vizi procedurali da parte del Supremo Tribunale Federale.

Sul tavolo del presidente, il dossier più delicato: lo scandalo del Banco Master che fa tremare i palazzi del potere. L'inchiesta sulle presunte irregolarità finanziarie ha lambito figure di primo piano delle istituzioni, compreso il giudice della Corte Suprema Alexandre de Moraes. De Moraes, storicamente percepito come un bastione della sinistra contro le spinte dell'estrema destra bolsonarista e garante della transizione democratica dopo l'assalto ai palazzi del potere dell'8 gennaio 2023, si trova oggi al centro di un fuoco incrociato. L'opposizione cavalca le ombre sul magistrato per denunciare un presunto patto di potere tra magistratura e governo, erodendo la fiducia dei ceti medi nella legalità repubblicana e offrendo munizioni retoriche letali ai detrattori del governo.

Per arginare l'emorragia di voti che nelle ultime settimane ha ridimensionato il numero di consensi a favore del governo, Lula ha calato l'asso della politica sociale: un massiccio pacchetto di aiuti economici mirati alle fasce più vulnerabili della popolazione. Più soldi nelle tasche dei poveri, più sussidi per le famiglie. Nelle favelas di Rio e nelle comunità rurali del Nordest, il programma Bolsa Família, con assegni mensili saliti a una media di 680 reais (circa 118 euro), garantisce un bacino elettorale compatto e fedele. È la rete di sicurezza sociale che spinge milioni di dimenticati a rinnovare la fiducia al vecchio leader. L'ultimo annuncio prevede l'esenzione totale dell'imposta sul reddito per chi guadagna fino a 5mila reais al mese, una misura pensata per sedurre anche la classe media impoverita.

Ma i soldi non bastano a conquistare l'anima di un Brasile profondamente mutato nella sua composizione demografica e culturale rispetto agli anni d'oro del primo mandato lulista. La straordinaria espansione delle chiese evangeliche neopentecostali, che oggi raccolgono oltre il 30% dei brasiliani e promuovono un'etica fondata sul successo individuale, sulla prosperità e sulla difesa intransigente della famiglia tradizionale, rappresenta un ostacolo quasi insormontabile per la sinistra laica. I fedeli evangelici guardano a Lula con diffidenza, spesso condizionati dai sermoni dei pastori che dipingono il PT come il partito del comunismo e del relativismo morale.

Lula ne è consapevole: vincere senza di loro è matematicamente impossibile. Per questo, la strategia elettorale delle ultime settimane si è concentrata su un dialogo serrato con i leader religiosi moderati e su una comunicazione pubblica intrisa di riferimenti alla fede e a Dio. È una guerra di simboli e di parole d'ordine, dove ogni dichiarazione può spostare centinaia di migliaia di preferenze in una sfida che si preannuncia sul filo dei millesimi.""",
    "category": "Economia e politica internazionale",
    "page": 15,
    "isHighlight": False
})

# 6. Page 15: Bolsonaro Jr recupera nei sondaggi e prova la scalata ultraliberista
articles.append({
    "id": "art-6",
    "title": "Bolsonaro Jr recupera nei sondaggi e prova la scalata ultraliberista",
    "subtitle": "Il figlio del golpista. Flavio raccoglie i voti di quella fascia di elettori moderati ma anti-Lula. Una candidatura vista come aggregatrice contro l’egemonia della sinistra",
    "body": """di Roberto Da Rin

Non è facile seguire le orme di un gigante del populismo latinoamericano, specialmente se quel gigante è il proprio padre. Flavio Bolsonaro, 45 anni, primogenito dell'ex presidente Jair Bolsonaro dichiarato ineleggibile dalla giustizia elettorale fino al 2030, affronta la sfida più ambiziosa e rischiosa della sua carriera politica.

La destra conservatrice brasiliana ha scelto lui, ex deputato statale e attuale senatore di Rio de Janeiro, come alfiere per sbarrare la strada a un nuovo quadriennio progressista. Una scommessa che, contro ogni previsione iniziale, sta pagando. Negli ultimi due mesi, la macchina elettorale bolsonarista ha impresso una marcia decisa, rosicchiando punti preziosi nei sondaggi e accorciando il distacco da Lula fino a portarlo entro i margini dell'errore statistico.

La benzina che alimenta il motore della sua rimonta è un sentimento viscerale, profondo e mai sopito: l'antipetismo. Quella miscela esplosiva di risentimento verso gli scandali di corruzione del passato, insofferenza per la spesa pubblica assistenziale e timore dell'ingerenza dello Stato nella vita economica e morale dei cittadini. Flavio ha saputo intercettare i voti di quella fascia di elettori moderati, imprenditori, professionisti e ceto medio produttivo che, pur non amando i toni aggressivi e militareschi del padre, considerano la sconfitta di Lula una priorità assoluta per il futuro del Paese.

A blindare la sua ascesa non c'è però solo l'ideologia, ma il pilastro più pesante dell'economia nazionale: la potente lobby dell'agroindustria, i cosiddetti ruralistas. I grandi proprietari terrieri del Mato Grosso, del Paraná e di Goiás hanno versato fiumi di denaro nei comitati elettorali del candidato conservatore. A questo robusto sostegno interno si aggiunge un prestigioso sigillo internazionale: l'asse preferenziale con Donald Trump. I legami diretti con i vertici repubblicani statunitensi e con il movimento MAGA garantiscono a Bolsonaro Jr una proiezione globale e la promessa di un riallineamento strategico di Brasilia con Washington in caso di vittoria congiunta dei conservatori.

Eppure, dietro la lucida facciata della rimonta, i critici intravedono crepe profonde. Il peccato originale di Flavio resta la sua matrice dinastica: un politico proiettato ai vertici solo per ragioni di sangue. Senza il cognome Bolsonaro, la sua parabola politica non avrebbe mai raggiunto simili altezze. I detrattori gli rimproverano una scarsa caratura intellettuale, una modesta capacità oratoria e l'ombra mai del tutto dissipata delle vecchie inchieste giudiziarie su presunte appropriazioni indebite di stipendi dei dipendenti (lo scandalo delle cosiddette rachadinhas) all'epoca in cui sedeva nell'Assemblea legislativa di Rio.

Un altro limite strutturale della sua candidatura è rappresentato dal suo elettorato: nonostante le aperture centriste, il nucleo duro resta ancorato a posizioni radicali che allontanano l'elettorato moderato, specialmente tra le donne e i giovani. Il punto più scoperto del suo programma è l'assenza totale di un'idea di sviluppo organica per il Paese. La sua proposta economica appare schiacciata sugli interessi immediati dei suoi grandi investitori: una ricetta che promette i giganti dell'export agricolo ma che non offre risposte strutturali alla complessa crisi industriale o alle storiche disuguaglianze delle metropoli. Una visione subordinata alle dinamiche esterne e al desiderato geopolitico di Trump, che rischia di trasformare il colosso sudamericano nel backyard americano, quello smisurato cortile di casa a lungo temuto dai nazionalisti brasiliani. Tra presente e futuro, sospeso dal vento dell'anti-populismo, ma sospeso sul dubbio più grande: la capacità di essere un vero statista alla guida di un grande Paese.""",
    "category": "Economia e politica internazionale",
    "page": 15,
    "isHighlight": False
})

# 7. Page 16: La certezza del diritto è vitale per le imprese
articles.append({
    "id": "art-7",
    "title": "La certezza del diritto è vitale per le imprese",
    "subtitle": "Made in Italy",
    "body": """di Claudia Eccher

Quando si parla di competitività del Made in Italy, l’attenzione va quasi sempre alla qualità del prodotto, al design e alla tradizione manifatturiera. C’è però un fattore immateriale ma decisivo che incide direttamente sulla fiducia e sulla tenuta delle relazioni commerciali: la certezza del diritto e l’efficienza della giustizia.

In un contesto geopolitico frammentato e complesso, dove le imprese operano su catene globali del valore sempre più instabili, la prevedibilità delle decisioni giuridiche e la celerità nella risoluzione delle controversie non rappresentano un mero dettaglio procedurale, ma un vero e proprio fattore di produzione. L’incertezza normativa e le oscillazioni interpretative generano costi di transazione aggiuntivi, che vanno dalle garanzie fideiussorie più onerose fino ai premi assicurativi per tutelarsi da eventuali vertenze all’estero.

Per questo le riforme della giustizia legate al Pnrr non sono un mero adempimento burocratico per ottenere i fondi europei, ma una profonda ristrutturazione dell’infrastruttura economica nazionale. I target fissati per il 2026 sono stati raggiunti: meno 40% del disposition time nel civile, meno 25% nel penale e arretrato ultratriennale abbattuto del 90 per cento. Il punto, ora, è consolidare questi risultati nel tempo. L’Ufficio per il processo ha introdotto una modalità di lavoro in équipe, affiancando stabilmente il giudice nell’attività preparatoria e organizzativa. La digitalizzazione conta soprattutto per l’accessibilità della giurisprudenza: orientamenti stabili e la piena conoscibilità delle banche dati garantiscono la prevedibilità delle decisioni. A ciò contribuiscono anche le Sezioni specializzate per l’impresa e l’arbitrato internazionale, le cui decisioni sono eseguibili in oltre 170 Paesi.

La certezza del diritto, però, non dipende soltanto dall’efficienza dei tribunali. Anche le imprese possono ridurre il rischio giuridico nelle proprie strategie di internazionalizzazione, trasformando la gestione del rischio legale da costo in asset strategico. Lo dimostrano le recenti missioni di sistema in America Latina, dove l’area Mercosur vale già 14 miliardi per l’Italia. Gli strumenti vanno dalla tutela della proprietà intellettuale, dal Brevetto unitario all’impiego di tecnologie come la Blockchain e alle clausole contro l’Italian sounding, ai contratti standardizzati, con clausole di hardship e forza maggiore contro sanzioni e dazi, fino al rafforzamento della compliance aziendale.

Sul piano istituzionale, sarebbe utile affiancare alla diplomazia economica una vera e propria diplomazia giuridica, rafforzando la cooperazione con i Paesi extra-Ue. Resta la direttiva europea sulla due diligence di sostenibilità, la CS3D, che impone obblighi trasversali lungo tutta la catena del valore. L’efficienza della giustizia non è una questione confinata nei tribunali: è politica economica. Tempi certi, decisioni prevedibili e tutele efficaci sono la garanzia che il Sistema Paese deve offrire a chi esporta e a chi investe in Italia, per tutelare l’eccellenza del Made in Italy e consolidare il nostro ruolo nel commercio globale.

Claudia Eccher
Componente laico del Csm""",
    "category": "Commenti",
    "page": 16,
    "isHighlight": False
})

# 8. Page 17: Patti Smith: un ponte tra rock e spiritualità sui passi del poverello
articles.append({
    "id": "art-8",
    "title": "Patti Smith: un ponte tra rock e spiritualità sui passi del poverello",
    "subtitle": "Gli ottocento anni della morte del santo/2",
    "body": """di Cristiana Gattoni

Dal CBGB di New York alla basilica di San Francesco ad Assisi c’è la stessa distanza che separa una bestemmia da una preghiera. Il primo era un buco sudicio e assordante sulla Bowery, popolato negli anni 70 da Ramones, Television, Talking Heads e da una cantante magrissima che recitava Rimbaud sopra tre accordi. La seconda custodisce in silenzio la tomba del santo della povertà e della fraternità con ogni creatura. Eppure Patti Smith ha abitato entrambi questi mondi, senza che l’uno cancellasse l’altro. La ragazza che esordì nel 1975 con Gloria, cantando Gesù è morto per i peccati di qualcuno, ma non per i miei, è la stessa donna che – cinquant’anni dopo – è stata chiamata dai frati del Sacro Convento a comporre una poesia per l’ottavo centenario della morte del santo: così è nata Where Francis Walked, scritta da Patti Smith proprio mentre era in tour per celebrare il cinquantesimo anniversario dell’album Horses e poi pubblicata sulla rivista San Francesco patrono d’Italia, con la traduzione italiana del gesuita Antonio Spadaro.

Da quei versi prende il titolo Words and Music – Where Francis Walked, spettacolo che intreccia canzoni, poesia e memoria autobiografica, e che Smith porterà in Italia tra novembre e dicembre. C’è qualcosa in questo incontro che è al contempo eccitante e commovente ma, per capire perché i frati hanno bussato alla sua porta, non basta ricordare che nel 2012 Smith arrivò ad Assisi, pregò a lungo sulla tomba di Francesco e pranzò con la comunità, né il suo entusiasmo per l’elezione del papa che aveva scelto quel nome. Bisogna andare più indietro.

Nell’autobiografia Il pane degli angeli (Bompiani, 2025), l’artista, nata nel 1946, ripercorre le tappe della sua vita: l’infanzia poverissima nel South Jersey, segnata dalle malattie e trascorsa a divorare libri e fumetti; i giochi di una ragazzina dall’immaginazione febbrile, che la portò a immedesimarsi in una sorta di Alice che riusciva a trovare meraviglie dove c’erano solo case sgangherate infestate dai ratti; e poi, ventenne, l’arrivo a New York, il Chelsea Hotel, la passione divorante per Robert Mapplethorpe e la sintonia di sensi e di intelletto con Tom Verlaine, le chiacchierate con William Burroughs, la devozione per Bob Dylan, il tour di Horses accompagnata da Paul Getty e Maria Schneider. Vita immersa nella mitologia del rock e pervasa allo stesso tempo dalla religione: la Bibbia nella casa dei genitori, la fascinazione per il buddhismo fin da giovanissima, la madre, diventata Testimone di Geova, che la portava con sé di casa in casa a evangelizzare: «Spesso ci venivano tirati addosso secchi di urina ed escrementi quando persone ostili aprivano la porta il sabato pomeriggio. Era proprio questo trattamento ad attrarmi maggiormente verso di loro, perché la mia inclinazione a schierarmi dalla parte degli oppressi», scrive nel suo memoir.

Nel 1977, costretta a letto in seguito a un incidente sul palco, guardò più volte Il Vangelo secondo Matteo di Pasolini. Francesco riaffiora nel libro a più riprese, quasi incidentalmente. Prima di partire per l’Europa, sul finire degli anni 90, Smith scrive di aver visto il padre nel cortile mentre dava da mangiare agli uccelli. Quelli gli volarono incontro, e lei pensò immediatamente agli affreschi di Giotto ad Assisi. Non gli attribuì miracoli: riconobbe in lui la semplicità di un santo, l’appartenenza a una «tribù sacra», definendo se stessa come la «figlia vagabonda del santo». Bisogna aver letto tutto questo, e aver ascoltato Dancing Barefoot, dove l’amore umano arriva a sfiorare quello per il Creatore, o Constantine’s Dream, che da Piero della Francesca si allarga alla vita, alla morte e alla devastazione della natura, prima di accostarsi a Where Francis Walked: «Smarrita in una selva / invocando una guida / ho ascoltato il grido / di un lupo ferito / rannicchiato su un tumulo / un tempo stimato sacro». Solo allora quell’epiteto, “la sacerdotessa del rock”, recupera qualcosa del suo significato più autentico.""",
    "category": "Commenti",
    "page": 17,
    "isHighlight": False
})

# 9. Page 17: Un numero monografico della «Domenica» sul santo di Assisi
articles.append({
    "id": "art-9",
    "title": "Un numero monografico della «Domenica» sul santo di Assisi",
    "subtitle": "L’iniziativa",
    "body": """di Stefano Salis

Sono passati esattamente 800 anni. Una coincidenza fortuita ha voluto che il momento del trapasso del più grande santo della cristianità – anzi, la figura stessa, per antonomasia, di cosa sia essere santo, cioè Francesco d’Assisi – facesse cadere di Domenica il giorno della morte e quello della celebrazione a otto secoli di distanza. Celebrazioni che, dal punto di vista religioso, laico e “ibrido” (il santo è pur sempre il patrono d’Italia e in questa veste sarà anche ricordato nel solenne discorso che terrà il presidente Mattarella domenica) fondono le molte anime del poverello e alle quali ci uniamo con un numero speciale del nostro supplemento, interamente dedicato alla multiforme figura, colma di iridescenze e riverberi, del santo di Assisi.

In questa pagina, per esempio, anticipiamo la nostra iniziativa con due possibili modi di trattare la grandezza di Francesco: e per due vie che ci appartengono allo stesso modo, l’economia e l’arte, in questo caso la musica. Gli interventi di Marco Allena sull’«economia di Francesco» e di Cristiana Gattoni su come la figura del santo si ritrovi nell’immaginario pop e rock di una star come Patti Smith sono il naturale prologo ai contenuti che, su carta, online e in video saranno proposti ai nostri lettori domenica.

Sul supplemento esploreremo il lascito di Francesco con articoli del cardinale Gianfranco Ravasi che, dalla copertina, ci racconta lo spirito con il quale va affrontata una figura così complessa. L’immagine che accompagna la nostra copertina la vedete anche in questa pagina: è san Francesco così come ritratto a Subiaco nel 1223. L’unico ritratto del futuro santo mentre è ancora vivo, fatto dal vivo e che saluta in maniera traslata quanto è vivo di lui. Marina Mojana, storica dell’arte, ripercorre la storia di quella potente immagine, che ci dice anche delle condizioni fisiche del poverello, tornato dall’Egitto con un tracoma oculare e menomato all’occhio sinistro.

Avremo interventi, tra gli altri, di Davide Rondoni, poeta, studioso e ammiratore di Francesco, in qualità di presidente del comitato nazionale delle celebrazioni francescane, di Luigino Bruni, l’economista che con più metodo si è trattenuto sui rapporti tra fede ed economia, di Carlo Ossola, presidente della Treccani (la quale pubblica in questa occasione una Enciclopedia di Francesco) sul Cantico delle creature e sui riflessi sulla letteratura del Novecento, di altri letterati e filologi come Piero Boitani, Lorenzo Tomasin, Giuseppe Lupo e Gino Ruozzi, e mentre Francesca Rigotti si sofferma sul portato del pensiero filosofico del francescanesimo, Sara Boffito indaga la dimensione psicoanalitica della rinuncia ai beni, Pietro Del Soldà ci porta su quella della protoecologia propugnata dal santo di Assisi.

E ancora: largo al cinema con le analisi dei film su Francesco di Cristina Battocletti, si parla di teatro con Maddalena Giovannelli, di musical con Angelo Curtolo, di partiture con Carla Moreni, di comunità francescane e no, con articoli di Stefano De Matteis, Roberto Escobar e Alessandro Zaccuri, di cucina povera con Luca Cesari, del ruolo che ebbero i suoi fraticelli con il nuovo libro dello studioso francesce Sylvain Piron, di camminate in montagna con Claudio Visentin e Carlo Ratti, di rapporto con le donne negli articoli di Eliana Di Caro e Maria Giuseppina Muzzarelli, di arte e territorio con Cristina Acidini. Ciascuno, insomma, ha il suo Francesco da raccontare, non banalizzando il suo messaggio ma cercando di cogliere gli spunti di attualità che offre.

È la stessa cosa che hanno fatto gli ospiti del Festival francescano recentemente tenutosi a Bologna, con enorme successo di pubblico. Stefano Biolchini è andato a intervistare i vari protagonisti, a partire dal cardinale Pizzaballa, e le video interviste saranno disponibili domenica sul sito ilsole24ore.com, nella sezione Cultura. Sullo stesso sito e sulle altre piattaforme, da domani, il podcast Start, firmato da chi scrive, vi proporrà, in anteprima, tre degli articoli del supplemento, quelli di Ossola, di Del Soldà e di Cesari. Dunque buone letture, buon ascolto e buona visione.""",
    "category": "Commenti",
    "page": 17,
    "isHighlight": False,
    "media": [
        {
            "type": "photo",
            "caption": "Francesco vivo. Un dettaglio dell’affresco di Subiaco",
            "box": [266, 280, 583, 805],
            "page": 17
        }
    ]
})

# 10. Page 18: Frenano gli occupati ad agosto, più disoccupati ma meno inattivi
articles.append({
    "id": "art-10",
    "title": "Frenano gli occupati ad agosto, più disoccupati ma meno inattivi",
    "subtitle": "ISTAT",
    "body": """di Giorgio Pogliotti

L'occupazione ad agosto resta sui massimi (24 milioni e 352mila occupati), ma rallenta rispetto a luglio (-5mila), tornando sotto i livelli di aprile. La crescita dei disoccupati (+48mila unità) è accompagnata dal calo degli inattivi (-21mila).

Il tasso di occupazione per l’Istat si attesta al 63%, diminuisce tra i 25-34enni e i 35-49enni, cresce tra chi ha almeno 50 anni d’età ed è stabile nella fascia 15-24 anni. Il tasso di disoccupazione (6,2%) sempre su base mensile cresce tra i 15-24enni e i 25-34enni ed è stabile tra chi ha almeno 35 anni di età; il tasso di inattività (32,7%) rispetto a luglio diminuisce in tutte le classi d’età, ad eccezione dei 35-49enni per i quali è in crescita.

Spostando invece il confronto con agosto 2025, su base annua si contano 291mila occupati in più, ma anche il numero di disoccupati cresce di 129mila unità e quello degli inattivi diminuisce di 381mila unità. Si assiste ad una ricomposizione dell’occupazione con più lavoro stabile sia nel confronto tendenziale che in quello congiunturale, tendenza che probabilmente è il frutto della difficoltà da parte delle imprese di reperire i profili cercati, che spinge a stabilizzare. Rispetto ad agosto 2025 gli occupati permanenti sono 370mila in più, quelli a termine 157mila in meno e gli indipendenti crescono di 78mila unità. Anche rispetto a luglio 2026 gli occupati permanenti sono in crescita (+48mila), quelli a termine calano (-48mila) così come gli indipendenti (-5mila). Resta ampio il divario di genere nei tassi di occupazione: 71,6% per gli uomini e 54,3% per le donne, con una distanza di quasi 17,3 punti percentuali.

Allargando lo sguardo all’Europa, il nostro tasso di disoccupazione al 6,2% si confronta con il 6,4% dell’Eurozona e al 6,1% di media della Ue. Per la disoccupazione giovanile, il nostro 20,3% resta ben al di sopra sia del tasso della Ue (15,4%) che dell’area euro (15%) e continua a collocare l’Italia agli ultimi posti. «Gli ultimi dati confermano che la fase di forte crescita dell’occupazione sembra essersi arrestata - commenta il presidente di Adapt, Francesco Seghezzi -, ma il quadro non è necessariamente negativo perché l’aumento della disoccupazione non può essere letto isolatamente come un segnale di peggioramento. Parte di questa crescita si accompagna infatti alla riduzione dell’inattività: più persone entrano o rientrano nel mercato del lavoro e iniziano a cercare un’occupazione».

Seghezzi sottolinea che rispetto ad agosto 2025 «si registrano 122mila occupati in meno tra i 35-49enni e 367mila in più tra gli over 50. Il calo nella fascia 35-49 anni è condizionato dalla riduzione della popolazione: al netto della componente demografica, l’occupazione crescerebbe dello 0,6%». Confcommercio evidenzia come tra gli occupati «i dipendenti a tempo indeterminato, che ormai rappresentano il 68,5% dell’occupazione totale, siano un segmento ancora in crescita. Ciò indicherebbe che le imprese non prevedono a breve un rallentamento significativo dell’attività economica».""",
    "category": "Imprese & Territori",
    "page": 18,
    "isHighlight": False
})

# 11. Page 18: L’Oréal Italia: dieci anni di collaborazione con Valemour
articles.append({
    "id": "art-11",
    "title": "L’Oréal Italia: dieci anni con Valemour per l’inclusione lavorativa",
    "subtitle": "Inclusione e sostenibilità sociale",
    "body": """Lo stabilimento di Settimo Torinese festeggia 10 anni di collaborazione con l’associazione Valemour per favorire l’inserimento lavorativo di giovani con disabilità intellettiva.""",
    "category": "Imprese & Territori",
    "page": 18,
    "isHighlight": False
})

result = {
    "newspaperName": newspaper_name,
    "date": date_str,
    "articles": articles
}

with open("page-images/batch_3.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"Generated {len(articles)} articles. Written to page-images/batch_3.json")
