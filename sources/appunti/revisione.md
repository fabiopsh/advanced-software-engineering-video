# Revisione didattica — Advanced Software Engineering

## Versione 8 (2026-11-25)

Aggiunta la lezione 15 (Quantum Software Engineering 101, 102 slide) come capitolo 15, in coda alla Parte IV (secondo
parziale). Nessun capitolo esistente modificato. Guida: una frase nella Parte IV e cinque righe di simboli (QPU/QSE,
NISQ, $\ket{\Psi}$/$\alpha$/$\beta$, TVD, parametri di StableShots). In `macro.tex` aggiunta la macro `\ket`.

PDF: `ASE_Appunti_v8.pdf`, 153 pagine.

### Indici

| Cap. | Titolo | Parole | Gulpease prima | Gulpease dopo | Frasi > 30 prima | dopo | Comprensibilità |
|---|---|---|---|---|---|---|---|
| 15 | Quantum Software Engineering | 4361 | 64,1 | 64,8 | 2,4% | 1,0% | 8 |

Gulpease di tutto il documento: 62,8. Le frasi lunghe rimaste sono i due blocchi di codice (OpenQASM, requisiti del
Quantum Broker), la definizione di QSE (citazione di Zhao) e quella di BQP. La comprensibilità è un giudizio.

### Errori e dubbi sulle fonti

| # | Dove | Problema | Scelta | Origine |
|---|---|---|---|---|
| 1 | tabella 15.1 | La complessità quantistica di Shor è scritta $O(\log N)$. L'algoritmo è polinomiale in $\log N$ (circa $O((\log N)^3)$), non lineare | Scritto "polinomiale in $\log N$" | fonti (L15 p.7) |
| 2 | tabella 15.4 | La colonna TVD della tabella delle monete truccate (0,375; 0,450; 0,333; 0,161; …) non si riproduce con la formula della TVD su nessuna coppia di distribuzioni cumulative o di finestre di lanci (provate tutte con Python) | Conteggi presi dalla slide; TVD ricalcolate tra la distribuzione dopo $n$ e dopo $n-1$ lanci, con regola di arresto d'esempio ($\epsilon = 0{,}1$, $k = 2$) | fonti (L15 p.85) |
| 3 | tabella 15.1 | La formula classica usa $n$ e $\log n$ senza dire che cosa è $n$; la costante $32/9$ | Riportata com'è | fonti (L15 p.7) |
| 4 | figure 15.1, 15.3, 15.4, 15.5, 15.7, 15.9 | Etichette sovrapposte; archi della griglia non disegnati; tabella delle tecnologie con colonne che sbordano | Ridisegnate e riguardate a grandezza reale | stesura |

### Deduzioni che non compaiono nel testo come tali

- §15.5.4: "la fedeltà di ogni QPU usata deve essere almeno 0,85" interpreta `min(fidelity) >= 0.85`; "massimizza
  $-$costo" interpreta l'obiettivo `-sum(cost)`.
- §15.6.2: shot multiplier e shot divider sono descritti dal disegno della slide p.72 (circuiti e bicchierini).
- §15.6.2: lo schema del multiprogramming con shot-wise è descritto dal disegno della slide p.75 (cinque fasi).
- §15.4: gli strumenti del software classico che mancano al quantistico sono letti dai loghi della slide p.53 (Docker,
  Kubernetes, Jenkins, Chaos Monkey, Prometheus, …).
- Figura 15.4: topologie schematiche (linea, scala, griglia), non le mappe dei processori IBM della slide p.32.
- Figura 15.9 e figura 15.6: andamenti qualitativi; le altezze degli istogrammi non vengono da dati.
- I boxplot dei risultati (p.63, p.73) sono descritti a parole: i dati non sono disponibili per ridisegnarli.

### Aggiunte segnate con la nota "[contenuto aggiuntivo]"

| Dove | Contenuto |
|---|---|
| §15.1 | che cosa significa la tabella delle accelerazioni ($10^6$ contro $10^3$; minaccia alla cifratura asimmetrica) |
| §15.2.1 | dalle ampiezze alle probabilità ($\abs{\alpha}^2$, $\abs{\beta}^2$, esempio $\sqrt{0{,}6}$, $\sqrt{0{,}4}$) |
| §15.3.1 | stima del 60–40% con 10 shot |
| §15.5.2 | esempio di merge uniforme (numeri di esempio, 3\,000 shot) |
| tabella 15.4 | TVD ricalcolate e regola di arresto d'esempio |

Aggiunte brevi non segnate: problema di decisione e P (§15.1); spiegazione riga per riga del programma OpenQASM e stato
dopo ogni porta (§15.3, preso dalla figura della slide); transpiler (§15.4); distanza di Hellinger (§15.5.3); hash chain
(§15.7.5); calcolo $18\,000 - 7\,650 = 10\,350$ (§15.7.4).

### Escluso dalle fonti

- Ritagli di giornale, risposta di ChatGPT, immagini decorative e meme (Homer, Dora, il gatto di Schrödinger, mani
  alzate, auto da corsa, sacchetti), elenco di 15 applicazioni di Forbes (riassunto per categorie).
- Schermata della demo di StableShots (p.94), vignetta "QSE: warning?" (p.97, senza testo).
- Tesi disponibili, gruppo di ricerca e sito quantum.unipi.it (p.99–101): organizzativo.
- Link al repository del Quantum Broker.

### Limiti

- Figure riguardate a grandezza reale; non riletto a schermo ogni pagina.
- Il quiz in `quiz/` non contiene domande sul capitolo 15.

## Versione 7 (2026-11-14)

Richiesta dell'utente: i capitoli del secondo parziale (dalla lezione 9, scomporre il monolite) devono stare tutti di
fila, separati da quelli del primo parziale, e i capitoli già esistenti non vanno modificati.
- La Parte III ("Cloud e microservizi") ora finisce con il capitolo 8. La Parte IV, "Dal monolite alla produzione:
  Kubernetes, testing, DevOps e sicurezza", contiene i capitoli 9–14. Numeri dei capitoli invariati.
- Tolti i tre rimandi aggiunti nella v6 ai capitoli 2 (§2.7), 6 (§6.3) e 7 (§7.9): i capitoli 1–8 sono di nuovo
  identici alla v5. I rimandi all'indietro dai capitoli nuovi verso quelli vecchi restano.
- Guida: descrizione delle parti aggiornata.

Contenuto, figure e indici di leggibilità dei capitoli 9–14 invariati rispetto alla v6.

## Versione 6 (2026-11-14)

Aggiunte le lezioni 10–14 (Testing, Kubernetes, DevOps, Security and Privacy, Security and microservices) come capitoli
10–14. Ordine di studio, non delle lezioni: Kubernetes (lezione 11) è il capitolo 10, in coda alla Parte III, perché
continua container e microservizi. La nuova Parte IV "Testing, DevOps e sicurezza" contiene Testing (cap. 11, lezione
10), DevOps (cap. 12, lezione 12), Sicurezza e privacy (cap. 13, lezione 13), Sicurezza dei microservizi (cap. 14,
lezione 14). I capitoli 1–9 non cambiano numero: il quiz (`quiz/src/data/chN.ts`) resta allineato.

Modifiche ai capitoli esistenti, solo rimandi: cap. 2 §2.7 (test automation e CI → §11.3, §12.3.1), cap. 6 §6.3
(identità federata → §13.3.2), cap. 7 §7.9 (DevOps → cap. 12). Guida: Parte IV e undici sigle nuove (K8s, TDD, CI/CD,
IaC/CM, APM, DoS/DDoS, XSS, ACL, TLS/CA, KMS, JWT).

PDF: `ASE_Appunti_v6.pdf`, 137 pagine.

### Indici

| Cap. | Titolo | Parole | Gulpease prima | Gulpease dopo | Frasi > 30 prima | dopo | Comprensibilità |
|---|---|---|---|---|---|---|---|
| 10 | Kubernetes | 2126 | 62,8 | 63,4 | 1,6% | 1,1% | 8 |
| 11 | Testing | 2171 | 66,0 | 66,5 | 1,5% | 0,5% | 8 |
| 12 | DevOps e code management | 3370 | 59,4 | 60,7 | 1,1% | 0,0% | 8 |
| 13 | Sicurezza e privacy | 3038 | 60,3 | 60,9 | 1,6% | 0,4% | 8 |
| 14 | Sicurezza dei microservizi | 2335 | 60,1 | 61,3 | 1,4% | 0,0% | 8 |

Gulpease di tutto il documento: 62,6. Le frasi lunghe rimaste nei capitoli 10, 11 e 13 sono blocchi di codice (manifest
YAML, test, query SQL), che lo script conta come frasi. La comprensibilità è un giudizio dato dopo la lettura, non una
misura.

### Errori corretti

| # | Dove | Problema | Correzione | Origine |
|---|---|---|---|---|
| 1 | cap. 10–14, figure 10.5, 10.6, 11.4, 11.5, 12.3, 12.4, 12.5, 12.8, 12.9, 13.1, 13.2, 13.6, 13.7, 14.1 | Etichette sovrapposte a frecce, bordi o altre etichette; testo fuori dalla piramide | Ridisegnate e riguardate a grandezza reale | stesura |
| 2 | cap. 13 §13.4 | Le due risorse dell'esempio dei permessi erano chiamate "cartelle", ma il primo carattere `-` indica un file normale | "risorse"; il primo carattere "indica il tipo di risorsa" | stesura |
| 3 | cap. 11 §11.3 | "il test automation" (genere diverso dal cap. 2) e doppia definizione in grassetto | "la test automation", con rimando al cap. 2 | stesura |
| 4 | cap. 12 §12.1.2 | DevOps definito in grassetto per la seconda volta (già nel cap. 7) | Grassetto tolto; la definizione rimanda al cap. 7 | stesura |
| 5 | cap. 10–14 | 14 frasi oltre 30 parole (elenchi dentro una frase nei punti chiave e nella cultura di Spotify) | Trasformate in elenchi o spezzate | stesura |

### Deduzioni che non compaiono nel testo come tali

- Cap. 14, figura 14.1 e tabella 14.1: le percentuali accanto a cinque smell (43, 43, 55, 34, 33%) sono descritte come
  "quanto ciascuno è citato nella rassegna", come nel cap. 8. La slide (L14 p.24) non lo spiega.
- Cap. 14, figura 14.1: quali smell colpiscono quale proprietà è letto dalle barre della slide p.24, ed è coerente con
  il titolo di ogni slide p.14–23.
- Cap. 12, figura 12.8: le metriche di processo e di servizio sono divise come nella slide (metà superiore e inferiore
  del cerchio); "mean time to recovery", a metà altezza nella slide, è messo tra quelle di processo. Il grafico delle
  tendenze settimanali è qualitativo (lo dice la didascalia): i punti seguono a occhio la forma della slide.
- Cap. 10 §10.1.1: l'esempio del worker perso ricostruisce la lavagna della slide p.10 (fermo immagine di un video):
  `App1.yaml`, Pod 1 con due container e 3 repliche, Pod 2 con un container e 2 repliche, tre worker di cui uno barrato.
- Cap. 12 §12.1.2: le "radici di DevOps" sono il contenuto della slide p.7, che è solo un'immagine senza commento.
- Cap. 13 §13.5.1: i due usi della cifratura asimmetrica (riservatezza e autenticità) sono letti dai due disegni della
  slide p.26.

### Aggiunte segnate con la nota "[contenuto aggiuntivo]"

| Dove | Contenuto |
|---|---|
| §10.1.1 | desired state management e l'esempio del worker perso, raccontati in prosa a partire dalle parole chiave della slide |
| §11.1 | perché il testing non dimostra la correttezza (input enormi, verifica formale) |
| §11.2.1 | esempio di partizioni e confini sull'intervallo 1–99 (−5, 45, 150; 0, 1, 99, 100; errore `<` al posto di `<=`) |
| §13.2.5 | perché un carattere in più conta tanto ($k^n$; $10^4$ e $10^5$ combinazioni con le sole cifre) |
| §13.4 | lettura dei permessi Unix `-rwxr--r--` e `-rwxrwxrwx` |

Aggiunte brevi non segnate (glosse inline): K8s come numeronimo e definizione di cluster (§10.1); etcd come
key-value store replicato (§10.4.1); Ingress controller (§10.3.4); mock object (§11.3); stub (§11.4); penetration
testing (§11.5); perché la query SQL con `'1'='1'` restituisce tutte le righe e la validazione del numero di conto
(§13.2.1); come funziona l'attacco DoS sul three-way handshake del TCP (§13.2.4); ransomware come cifratura dei dati
con riscatto (§13.1); data controller e data subject (§13.6); superficie d'attacco, zero-trust networking, security
token service, confused deputy problem, mutual TLS, elevation of privileges, man-in-the-middle (cap. 14); provisioning
e workaround (§12.3.3); il calcolo del caso Puppet (75% di 20\,000 = 15\,000 server; 700/300 ≈ 2,3), fatto con Python;
la frase che spiega che con TLS l'asimmetrica serve a concordare la chiave e la simmetrica, più veloce, a cifrare i dati
(§13.5.2).

### Escluso dalle fonti

- Titoli e slide di navigazione (foglietti gialli, elenchi di sezione) in tutte e cinque le lezioni.
- Link a video e il loro contenuto: incidente di un lanciatore (L10 p.3), automated deployment e K8s in 5 minuti
  (L11 p.4, 9), video su DevOps, Jenkins, Puppet, Chef, New Relic, Spotify (L12 p.3, 30, 35, 37, 44, 46). Della
  lavagna del video K8s (L11 p.10) restano le parole chiave scritte nella slide.
- La metafora del direttore d'orchestra (L11 p.6): resta il concetto (l'architetto definisce i container, la
  piattaforma li realizza).
- Immagini decorative: foto di Dijkstra (la citazione resta), Tetris, puzzle, foto "moron of the day" (resta lo stigma
  di rompere la build), loghi (git, Docker, Kubernetes, Spotify, NYSE/ICE), siringa, Gioconda, biglietto dei Beatles,
  foto di un telefono, schermata del sito di verifica delle password (restano i tempi della tabella), assi e ipercubo
  della slide sul triage.
- Riferimenti al libro di testo (Sommerville, cap. 7, 9, 10). Restano i due riferimenti di L14 (Siriwardena e Dias;
  Ponce et al.), come per il cap. 8.
- La citazione completa del caso Puppet (L12 p.36) è resa a parole, non tradotta alla lettera.

### Dubbi sulle fonti

- Alcune slide hanno un pallino rosso nell'angolo in alto a destra (per esempio L10 p.3, 6, 7, 33; L12 p.3, 4, 7, 36,
  47–49). Il significato non è spiegato. Il loro contenuto è trattato come il resto; se il pallino indica parti non
  d'esame, si possono segnare.

### Limiti

- Figure nuove riguardate a grandezza reale, insieme a guida e aperture dei capitoli. Non riletto a schermo ogni pagina
  del PDF.
- Il quiz in `quiz/` non contiene domande sui capitoli 10–14: non è stato toccato.

## Versione 5 (2026-10-23)

Aggiunta la lezione 9 (Splitting the monolith, 34 slide) come capitolo 9, in coda alla Parte III. Capitoli 0–8
invariati salvo la guida (una riga per il capitolo 9). Il capitolo segue l'ordine della lezione, che è già un ordine
di studio: monolite e seam, da dove iniziare, database, transazioni, reporting. È messo dopo il capitolo 8 per non
rinumerare i capitoli esistenti; dipende solo dal capitolo 7. In `macro.tex` sono state aggiunte le macro di disegno
`\tabdb` e gli stili TikZ `sv`, `dbs`, `contenitore`.

PDF: `ASE_Appunti_v5.pdf`, 82 pagine.

### Indici

| Cap. | Titolo | Parole | Gulpease prima | Gulpease dopo | Frasi > 30 prima | dopo | Comprensibilità |
|---|---|---|---|---|---|---|---|
| 9 | Scomporre il monolite | 3015 | 63,3 | 63,4 | 0,4% | 0,0% | 8 |

Gulpease di tutto il documento: 62,8. La comprensibilità è un giudizio dato dopo la lettura, non una misura.

### Errori corretti

| # | Dove | Problema | Correzione | Origine |
|---|---|---|---|---|
| 1 | cap. 9 §9.4 | Lo strumento è scritto "Hybernate" | "Hibernate" | fonti (L9 p.13) |
| 2 | cap. 9 figure 9.2, 9.6, 9.7, 9.8 | Riquadri più larghi del contenitore, riquadri sovrapposti, etichette attraversate dal tratteggio, etichetta "Fase 1" sopra la linea della vita | Ridisegnate e riguardate a grandezza reale | stesura |
| 3 | cap. 9 §9.3 | Una frase di 31 parole (pace of change) | Spezzata in due | stesura |
| 4 | cap. 9 §9.7.2 | "a due condizioni" presentava come condizioni due raccomandazioni | "Per tenerlo sotto controllo" | stesura |

### Deduzioni che non compaiono nel testo come tali

- §9.5.2 e §9.6.3: "è la soluzione preferita" per i dati statici come configurazione e per *try again later* è
  dedotto dal colore verde con cui le slide evidenziano quelle due soluzioni (p.17, p.25). Le slide non lo dicono a
  parole.
- §9.5.5: "è più facile tornare indietro perché la struttura del codice non è stata toccata" spiega la frase in verde
  della slide p.20.
- §9.7.2: "il backup che il servizio produce comunque diventa la sorgente dei dati per il reporting" spiega la frase
  "can be piggybacked by backup operations (Netflix backup data pumps)". Interpretazione coerente con il libro di
  riferimento (Newman, cap. 5), non verificata sul testo del libro.

### Aggiunte segnate con la nota "[contenuto aggiuntivo]"

| Dove | Contenuto |
|---|---|
| §9.2 | che cosa sta dentro un bounded context e che cosa passa la membrana (esempio del magazzino) |
| §9.3, figura 9.1 | esempio del seam meno dipeso, con un grafo di dipendenze *ipotetico* tra i package di MusicCorp |
| §9.5.4 | riquadro che distingue dati modificabili condivisi (stesso concetto) e tabelle condivise (concetti diversi) |
| §9.6.2, figura 9.8 | esempio del two-phase commit sul nuovo ordine, con diagramma di sequenza |
| §9.6.3 | come funziona *try again later* (operazione in coda e ritentata, finestra di incoerenza) |
| tabella 9.1 | confronto delle tre soluzioni per il reporting |

Aggiunte brevi non segnate (glosse inline): *lead time* (§9.1), Hibernate come libreria di object-relational mapping e
SchemaSpy come strumento che disegna lo schema (§9.4), *foreign key* (§9.4), *read replica* (§9.7), che cosa mostra
il grafo di Structure 101 (§9.2.1), la conseguenza di un ordine senza prelievo (§9.6), perché 5 operazioni complicano
le compensazioni (§9.6.1), perché recuperare i clienti uno per uno è inefficiente (§9.7.1). Figura 9.3: i tre
pannelli delle soluzioni sono disegnati dal testo della slide (la slide ha solo la situazione iniziale).

### Escluso dalle fonti

- Titolo e slide di navigazione con la lavagna (p.1, 5, 14, 21, 26, 31).
- Immagini decorative: blocco grigio, tessuto cucito, roccia spaccata, mani alzate, Jenga, shanghai, persone, schermata
  di errore di PayPal, martello e bottiglia (p.3, 6, 10, 11, 12, 17, 23, 24, 25, 34).
- Annuncio dei prossimi laboratori (p.34).
- Le schermate di Structure 101, Hibernate e SchemaSpy (p.9, 13): sono esempi di interfaccia degli strumenti, non
  schemi del corso. Il loro contenuto è descritto a parole.

### Limiti

- Figure nuove riguardate a grandezza reale, insieme all'apertura del capitolo e alla guida. Non riletto a schermo ogni
  pagina del PDF.
- Il quiz in `quiz/` non contiene domande sul capitolo 9: non è stato toccato.

## Versione 4 (2026-10-22)

Nel testo non compaiono più riferimenti alle slide o alle fonti. Gli approfondimenti aggiunti portano accanto al
titolo la nota piccola "[contenuto aggiuntivo]" (macro `\aggiunta`). L'origine di ogni aggiunta e di ogni
deduzione è registrata solo qui.

Indici: Gulpease di tutto il documento 62,7 (capitolo 8: 62,8; frasi oltre 30 parole 0,5%). 70 pagine.

### Aggiunte segnate con la nota (non presenti nelle fonti)

| Cap. | Dove | Contenuto |
|---|---|---|
| 1 | tabella 1.1 | confronto progetto/prodotto |
| 2 | §2.4.1 | le cinque pratiche XP non descritte (simple design, pair programming, collective ownership, sustainable pace, on-site customer) |
| 2 | §2.7 | test automation e continuous integration; esempio numerico di sprint planning (5 persone, 2 settimane, voci da 8, 15, 12, 10, 9 person-day) |
| 3 | §3.4 | esempio di epic spezzata (Tic Tac Toe, giocare contro il computer) |
| 4 | §4.5, §4.6 | esempio MVC (negozio online); esempio di scelta tra database relazionale e NoSQL |
| 5 | §5.5, §5.6 | spiegazione di istruzioni Dockerfile, comandi `docker build`/`run` e voci di docker-compose.yml |
| 6 | §6.1, §6.3, §6.6 | FaaS; autenticazione federata e information leakage; esempio numerico di scaling out/up (450 richieste/s, istanze da 100) |
| 6 | tabella 6.1 | chi gestisce che cosa nei tre modelli |
| 7 | §7.6 | esempio di coerenza eventuale; esempio di saga (viaggio con auto, hotel, aereo); esempio di quorum con 5 repliche |
| 8 | §8.3 | per ogni smell, perché lo è e come agiscono i refactoring; service discovery, router e broker; bulkhead; throttling; team per strato; ESB e rightsize ESB; esempio di due servizi sulla stessa tabella |
| 8 | §8.4 | viste per team: spiegazione del loro scopo |

Aggiunte brevi non segnate (glosse inline): definizione di *velocity* (cap. 2), *stateless*, *monolitico* e *ACID* con
rimando (cap. 6), calcolo della disponibilità al 99% (cap. 7, esempio della domanda a risposta multipla).

### Deduzioni che non compaiono nel testo come tali

- Cap. 8: il numero accanto a ogni smell e la percentuale accanto a ogni refactoring sono descritti come "quanto
  ciascuno è citato nella rassegna": le slide non lo spiegano.
- Cap. 8: i due gruppi dell'esperimento controllato sono descritti come "con e senza lo strumento": le slide non lo
  dicono.
- Cap. 7: per Uber è scritto "oltre 5\,000 microservizi" senza anno; le slide riportano "2053", probabile refuso.
- Cap. 8: team "single-layer", refactoring "let it be" e viste per team sono descritti dai disegni delle slide, quasi
  senza testo.

## Versione 3 (2026-10-22)

Aggiunta la lezione 8 come capitolo 8 (Parte III), 37 slide. Capitoli 0–7 invariati salvo la guida (un rigo per il
capitolo 8).

### Indici (capitolo nuovo)

| Cap. | Titolo | Parole | Gulpease | Frasi > 30 | Comprensibilità |
|---|---|---|---|---|---|
| 8 | Smell architetturali e refactoring per microservizi | 1615 | 63,2 (prima 61,2) | 0,0% (prima 2,5%) | 8 |

Gulpease di tutto il documento: 62,7. La comprensibilità è un giudizio, non una misura.

### Errori e dubbi sulle fonti

- La figura delle slide non spiega i numeri nelle bolle degli smell (16, 18, 28, 19, 9, 6) né le percentuali dei refactoring.
  Sono riportati come nelle slide, con l'avvertenza che il significato è dedotto (numero di riferimenti della rassegna).
- Nelle slide delle viste per team e dell'esperimento controllato mancano le spiegazioni: ho descritto solo ciò che
  il disegno mostra e ho segnalato nel testo che non è commentato.
- Nella notazione degli archi la lettera barrata significa "meccanismo assente": l'ho dedotto dagli esempi (la lettera
  barrata diventa verde quando il refactoring la aggiunge).

### Aggiunte (spiegazioni non presenti nelle fonti)

- Cap. 8: breve spiegazione di *bulkhead* ("compartimento stagno che separa le parti del sistema, così che un guasto non
  si propaghi"), di *ESB* ("enterprise service bus") e del perché lo smell *endpoint-based* ostacola le repliche. Le slide
  usano i termini senza definirli.
- Cap. 8: *single-layer teams* descritti dall'immagine (team omogenei per strato contro team misti per servizio):
  le slide non lo spiegano a parole.
- Cap. 8: refactoring "let it be" descritto come "lo smell può essere accettato e lasciato com'è", dalla figura.

### Escluso dalle fonti

- Immagini decorative e metafore (naso che annusa, sardine, effetto domino, diavoletti, jam band contro orchestra, elenco di
  aziende nel richiamo).
- Titoli di sezione e slide di navigazione.
- Elenco completo dei riferimenti bibliografici: restano i due principali.

### Limiti

- Figure nuove riguardate a grandezza reale; non riletto a schermo ogni pagina.
- Le figure delle slide con schemi molto piccoli (p. 24, 31, 32) sono state interpretate dal disegno.

## Versione 2 (2026-10-21)

Solo copertina e metadati del PDF: autore "Fabio Piscitelli" (cognome dato dall'utente), anno accademico 2026/2027
confermato dall'utente. Contenuto, indici e figure invariati rispetto alla versione 1. I limiti sull'autore e
sull'anno accademico della versione 1 sono superati.

## Versione 1 (2026-10-21)

Fonti: sette PDF di "Slide Teoria" (lezioni 1–7, prof. Brogi). PDF: `ASE_Appunti_v1.pdf`, 60 pagine, 7 capitoli più la guida.

### Indici

Gulpease: prima = prima stesura, dopo = dopo la revisione. Frasi > 30 parole in percentuale. I blocchi di codice del
capitolo 5 sono contati dallo script come frasi lunghe: per questo il capitolo resta al 4,3%.

| Cap. | Titolo | Parole | Gulpease prima | Gulpease dopo | Frasi > 30 prima | dopo | Comprensibilità |
|---|---|---|---|---|---|---|---|
| 0 | Guida alla lettura | 238 | 65,7 | 70,5 | 9,1% | 0,0% | 9 |
| 1 | Dal progetto al prodotto | 891 | 63,5 | 65,3 | 3,7% | 0,0% | 9 |
| 2 | Sviluppo agile | 1900 | 61,7 | 61,6 | 0,6% | 0,6% | 8 |
| 3 | Feature, scenari e storie | 1888 | 64,7 | 64,6 | 0,6% | 0,6% | 8 |
| 4 | Architettura del software | 1528 | 58,4 | 60,1 | 3,0% | 0,7% | 8 |
| 5 | Cloud computing, container e Docker | 1188 | 62,3 | 62,6 | 5,4% | 4,3% | 8 |
| 6 | Software basato sul cloud | 1986 | 62,2 | 62,2 | 1,7% | 1,7% | 8 |
| 7 | Architettura a microservizi | 2345 | 62,4 | 62,4 | 0,9% | 0,9% | 8 |
| | Totale | 11964 | 62,3 | 62,7 | | | |

La comprensibilità è un giudizio dato dopo la lettura su sei criteri (termini definiti prima dell'uso, esempi con
numeri, dimostrazioni senza salti, figure coerenti con il testo, notazione coerente, carico sostenibile). Non è una
misura.

### Errori corretti

| # | Dove | Problema | Correzione | Origine |
|---|---|---|---|---|
| 1 | cap. 7 §7.6 (teorema CAP) | Le ultime due equivalenze della derivazione sono etichettate "De Morgan" | Giustificate con la definizione di implicazione ($X \to Y \equiv \neg X \vee Y$) | fonti (L7 p.22) |
| 2 | cap. 7 §7.6 | Il convegno è scritto "PDOC" | Tolto il nome del convegno, lasciato l'anno (2000) | fonti (L7 p.22) |
| 3 | cap. 5 §5.6 (index.php) | Il sito legge `$obj->products`, ma il servizio restituisce la chiave `product` | Scritto `$obj->product` | fonti (L6 p.14–15) |
| 4 | cap. 5 §5.2 (figura) | La figura delle VM mostra un Host OS sotto l'hypervisor, ma il testo dice che l'hypervisor "di tipo 1" è caricato direttamente sull'hardware | Figura disegnata come dice il testo (hypervisor sull'hardware, niente Host OS) | fonti (L6 p.4) |
| 5 | cap. 3 §3.5 (storie Tic Tac Toe) | "See an update board" | "see an updated board" | fonti (L4 p.28) |
| 6 | cap. 2 §2.1 | "Formal quality insurance" | Reso come "controllo formale della qualità" | fonti (L3 p.3) |
| 7 | cap. 1 §1.5 | Il prototipo era indicato come mezzo per "verificare le idee della vision": non è scritto nella slide sul prototipo | Tolto; il legame è reso come origine della vision (§1.3) | stesura |
| 8 | cap. 1 tabella 1.1 | "Documentati nei dettagli" per il project-based: la slide dice solo che il product-based ne richiede meno | "più documentazione dei requisiti" | stesura |
| 9 | cap. 4 §4.4 | Il testo attribuiva alle slide un motivo per l'evidenziazione dei due componenti di validazione | Riportato solo che le slide li evidenziano | stesura |
| 10 | cap. 6 §6.8, tabella 6.5 | "Stateless", "monolitico" e "ACID" usati prima della definizione (definiti nel cap. 7) | Aggiunta una frase di spiegazione e il rimando | stesura |
| 11 | cap. 2 §2.7 | "Velocity" usata senza spiegazione | Aggiunta la definizione (vedi Aggiunte) | stesura |
| 12 | cap. 3, 7, figure | Figure 2.1, 2.2, 3.2, 4.4, 4.6, 5.2, 6.1, 7.2, 7.5, 7.7–7.10: frecce che attraversano etichette, etichette sovrapposte ai riquadri, ellissi sovrapposte | Ridisegnate e riguardate a grandezza reale | stesura |
| 13 | cap. 3, 7 | Errori di battitura ("una azienda", doppio punto nei titoli, `update(d,v2)` in corsivo matematico) | Corretti | stesura |

Dubbi sulle fonti lasciati come sono, ma segnalati nel testo o qui:
- cap. 7 §7.3: le slide scrivono "2053: 5,000+ microservices" per Uber. L'anno è probabilmente un refuso. È riportato com'è,
  con l'avvertenza nel testo.
- cap. 2: la durata di uno sprint è "2–4 settimane" nella terminologia di Scrum (L3 p.16) e "1–4 settimane" nella
  slide sugli sprint con tempo fisso (L3 p.21). Sono riportate entrambe, con rimando.

### Notazione

Il corso non usa formule. Gli unici simboli sono quelli della logica nel teorema CAP ($C$, $A$, $P$, $\neg$, $\wedge$,
$\vee$, $\rightarrow$), usati con un solo significato e descritti nella tabella della guida. Nessuna unificazione necessaria.

### Aggiunte (spiegazioni non presenti nelle fonti)

- cap. 1 tabella 1.1: confronto project-based / product-based. Sintesi di L2 p.4 e p.6 e di L4 p.4.
- cap. 2 §2.7: definizione di *velocity* ("la quantità di lavoro che il team riesce a completare in uno sprint"). Le slide
  usano il termine senza definirlo.
- cap. 5 §5.5–5.6: spiegazione riga per riga dei comandi `docker build`, `docker run` e delle istruzioni di Dockerfile e
  docker-compose.yml (`FROM`, `COPY`, `EXPOSE`, `ports`, `volumes`, `depends_on`). Le slide mostrano solo il codice.
- cap. 6 tabella 6.1: chi gestisce che cosa (infrastruttura, sistema operativo, software abilitante, applicazione) nei tre
  modelli. Ricavata dal testo di L6 p.19; la riga del "software abilitante" per l'IaaS è dedotta da "il cliente è
  responsabile di tutti gli altri aspetti".
- cap. 6 §6.2: i problemi per i clienti sono elencati tutti insieme come svantaggi, compresa la conformità alla privacy
  (nelle slide è mescolata ai vantaggi).
- cap. 7 §7.8: calcolo della disponibilità di due servizi al 99% ($0{,}99^2 = 0{,}9801$, indisponibilità 1,99% di 86\,400 s
  = circa 1\,719 s, circa 29 minuti). Le slide pongono solo la domanda a risposta multipla. Calcolato con Python.
- cap. 7 §7.6: la dimostrazione di $A \to \neg C$ è accompagnata dalla spiegazione in prosa dei due diagrammi di sequenza.
- cap. 7 figura 7.7 (circuit breaker): le slide descrivono il meccanismo solo a parole; lo schema a tre fasi è una
  ridisegno del testo, con le stesse parole.
- esempi persona (Emma, Pierfrancesco) e scenario (Fishing in Ullapool): riassunti e tradotti in italiano, non
  riportati alla lettera.

### Escluso dalle fonti

- Lezione 1: intera (presentazione del corso: motivazione, colloqui di lavoro, AI, orari, docenti, date d'esame,
  modalità d'esame, valutazione continua, FAQ). La mappa degli argomenti è ripresa dalla struttura degli appunti.
- Cronologia dei container (L6 p.6: chroot, FreeBSD jail 1998, cgroups 2005, LXC 2008, Docker 2013): nota storica.
  Restano Docker Engine e Docker Hub.
- Immagini decorative e metafore: orologio, lattine Campbell, foto di mischia di rugby, "Pizza as a Service", orchestra e
  danzatori per orchestration/choreography, semaforo e rotatoria, Chaos Monkey, bilancia dei compromessi, altalena
  per il prototipo, fumetti e screenshot di video.
- Rimandi a video (tutorial MVC, "Why NoSQL databases", Docker in 12 minuti, Docker Compose in 12 minuti, video sulle
  user stories) e il loro contenuto: sono solo link nelle slide.
- Titoli di sezione e slide di navigazione (lavagne con elenco delle sezioni).

### Limiti

- Il contenuto dei video segnalati come "Homework" nelle slide (splitting user stories, Why NoSQL databases) non è
  nelle slide e non è nelle note.
- Ho riguardato a grandezza reale le figure nuove o modificate e alcune pagine campione (copertina, indice, aperture dei
  capitoli, tabelle principali). Non ho riletto a schermo ogni pagina del PDF.
- Le tabelle riprodotte dalle slide (L5, L6, L7) sono state lette dalle immagini, in alcuni casi a risoluzione
  ridotta: le cifre di Spotify sono state riguardate ad alta risoluzione, il resto è stato rimesso in forma di testo con
  attenzione ma non confrontato con il libro di testo.
- L'anno accademico 2026/2027 in copertina è dedotto dal codice "ASE2627" presente nella slide della lezione 1.
- L'autore in copertina è "Fabio": il cognome non risulta dalle fonti. Va completato in `main.tex` (copertina e
  `pdfauthor`).
- Gulpease e comprensibilità sono indici di sostegno: non sostituiscono la lettura.
