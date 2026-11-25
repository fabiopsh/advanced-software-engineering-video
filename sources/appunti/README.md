# Advanced Software Engineering — appunti

Appunti di Advanced Software Engineering (Laurea Magistrale in Informatica, Università di Pisa, prof. Brogi)
riorganizzati per lo studio con la skill appunti-pro. Ogni concetto è definito una sola volta, le figure utili sono
ridisegnate (TikZ), le informazioni organizzative e le immagini decorative delle slide sono escluse.

## Versioni

| PDF | Data | Contenuto |
|---|---|---|
| `ASE_Appunti_v1.pdf` | 2026-10-21 | prima versione: lezioni 2–7 (la lezione 1 è solo organizzativa) |
| `ASE_Appunti_v2.pdf` | 2026-10-21 | copertina: autore Fabio Piscitelli, A.A. 2026/2027 confermato; contenuto invariato |
| `ASE_Appunti_v3.pdf` | 2026-10-22 | aggiunta la lezione 8 (capitolo 8, smell architetturali e refactoring per microservizi) |
| `ASE_Appunti_v4.pdf` | 2026-10-22 | tolti i riferimenti alle slide dal testo; aggiunti approfondimenti con nota "[contenuto aggiuntivo]" |
| `ASE_Appunti_v5.pdf` | 2026-10-23 | aggiunta la lezione 9 (capitolo 9, scomporre il monolite) |
| `ASE_Appunti_v6.pdf` | 2026-11-14 | aggiunte le lezioni 10–14: Kubernetes (cap. 10), nuova Parte IV con testing, DevOps, sicurezza e privacy, sicurezza dei microservizi (cap. 11–14) |
| `ASE_Appunti_v7.pdf` | 2026-11-14 | Parte IV "Dal monolite alla produzione" con i cap. 9–14 (programma del secondo parziale); capitoli 1–8 di nuovo identici alla v5 |
| `ASE_Appunti_v8.pdf` | 2026-11-25 | aggiunta la lezione 15 (capitolo 15, Quantum Software Engineering) in coda alla Parte IV |

Il numero di versione sta in `versione.tex` ed è scritto in copertina. `build.sh` produce
`ASE_Appunti_v<N>.pdf` e non tocca i PDF precedenti: per una nuova versione si aumenta il numero.

## Contenuto della cartella

- `main.tex`, `preambolo.tex`, `lingua.tex`, `macro.tex`, `versione.tex` — documento, stile, lingua, simboli del corso.
- `capitoli/` — un file per capitolo (00 guida, poi 01–15).
- `fonti/` — testo estratto dalle slide (`*.md`) e `inventario.md` (cosa deve comparire negli appunti). Le immagini
  delle pagine non si conservano (escluse da git con `.gitignore`): servono solo mentre si scrive un capitolo e si
  rigenerano dai PDF, dalla cartella del progetto, con
  `uv run <skill appunti-pro>/scripts/estrai.py "Slide Teoria/<lezione>.pdf" --out appunti/fonti --png`.
- `script/genera_dati.py`, `dati/` — non usati: nessuna figura è calcolata da dati.
- `revisione.md` — revisione didattica: indici di leggibilità, errori corretti, aggiunte, esclusioni, limiti.

## Come si compila

1. Compilare (serve [tectonic](https://tectonic-typesetting.github.io)):

   ```bash
   ./build.sh
   ```

   Uscita attesa: l'ultima riga è `PDF: .../ASE_Appunti_v<N>.pdf`.

## Corrispondenza con le fonti

| Capitolo | Fonti |
|---|---|
| 1 Dal progetto al prodotto | Lezione 2 (Software products) |
| 2 Sviluppo agile | Lezione 3 (Agile Software Engineering) |
| 3 Feature, scenari e storie | Lezione 4 (Features, Scenarios, and Stories) |
| 4 Architettura del software | Lezione 5 (Software architecture) |
| 5 Cloud computing, container e Docker | Lezione 6, pp. 2–16 |
| 6 Software basato sul cloud | Lezione 6, pp. 17–45 |
| 7 Architettura a microservizi | Lezione 7 (Microservices architecture) |
| 8 Smell architetturali e refactoring | Lezione 8 (Architectural smells and refactorings for microservices) |
| 9 Scomporre il monolite | Lezione 9 (Splitting the monolith) |
| 10 Kubernetes | Lezione 11 (Kubernetes) |
| 11 Testing | Lezione 10 (Testing) |
| 12 DevOps e code management | Lezione 12 (DevOps) |
| 13 Sicurezza e privacy | Lezione 13 (Security and Privacy) |
| 14 Sicurezza dei microservizi | Lezione 14 (Security and microservices) |
| 15 Quantum Software Engineering | Lezione 15 (Quantum Software Engineering 101) |
| — (esclusa) | Lezione 1 (Course introduction: organizzazione del corso) |
