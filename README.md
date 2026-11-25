# Advanced Software Engineering — Videolezioni Interattive

Web app statica di **videolezioni interattive sincronizzate alla voce** per il corso di **Advanced Software Engineering** (*Laurea Magistrale in Informatica, Università di Pisa — A.A. 2026/2027*).

- **Appunti e realizzazione**: [Fabio Piscitelli](https://github.com/fabiopsh) (`fabiopsh`)
- **Docenti del corso**: Prof. Antonio Brogi & Prof. Alessandro Bocci (Dipartimento di Informatica, UNIPI)
- **Motore**: [Lectio Framework](https://github.com/fabiopsh/lectio-framework) (HTML + SVG + KaTeX + live-sync voce/slide, zero video MP4)
- **Tutor virtuale**: avatar pixel-art **Fabio** (spritesheet 6-frame sincronizzato al labiale) + voce **Ludo** (`gemini-3.8-flash-tts`)
- **Sito pubblicato (GitHub Pages)**: [fabiopsh.github.io/advanced-software-engineering-video](https://fabiopsh.github.io/advanced-software-engineering-video/)

---

## Programma del corso (15 capitoli · 137 scene · ~2h 48m)

Basato sugli appunti in [`sources/appunti/`](sources/appunti/README.md) (15 capitoli in 4 parti, derivati dalle slide ufficiali del corso e dal testo di Ian Sommerville, *Engineering Software Products*):

| Parte | Capitoli | Scene | Stato |
|---|---|---:|---|
| **Parte I · Prodotti software e sviluppo agile** | 01 Dal progetto al prodotto · 02 Sviluppo agile · 03 Feature, scenari e storie | 22 | Pronto |
| **Parte II · Architettura del software** | 04 Architettura del software | 9 | Pronto |
| **Parte III · Cloud e microservizi** | 05 Container e Docker · 06 Software sul cloud · 07 Microservizi · 08 Smell e refactoring | 36 | Pronto |
| **Parte IV · Dal monolite alla produzione** | 09 Scomporre il monolite · 10 Kubernetes · 11 Testing · 12 DevOps · 13 Sicurezza e privacy · 14 Sicurezza microservizi · 15 Quantum SE | 70 | Pronto |

---

## Funzionalità del player

- **Live-Sync voce ↔ slide**: evidenzia in tempo reale box, diagrammi architetturali SVG, righe di tabella, liste e formule KaTeX con sottotitoli parola per parola.
- **Avatar pixel-art Fabio**: lip-sync deterministico guidato dai timestamp parola per parola (MMS_FA), attivabile/disattivabile con `V`.
- **4 temi live**: `Studio` (default), `Carbon`, `Liquid Glass` e `16-bit`.
- **Ricerca globale `Ctrl+K`** su slide e trascrizioni, modalità Teatro (`T`), modalità Pulita, progresso locale e segnalazione errori via GitHub Issues.

---

## Avvio locale e pipeline di generazione

### 1. Anteprima locale

```bash
python videolezioni/scripts/serve.py
# Apri http://127.0.0.1:8080/
```

### 2. Dipendenze (una tantum)

```bash
pip install -r requirements.txt
npm install
```

### 3. Configurazione chiave TTS (mai committata)

```bash
python videolezioni/scripts/setup_tts.py --set-key LA_TUA_GEMINI_API_KEY --budget 5.0
```

### 4. Generazione audio, allineamento e verifica qualità

```bash
# Stima costi a 0 €
python videolezioni/scripts/generate_batch.py 01-prodotti --dry-run

# Generazione audio batch (voce Ludo, gemini-3.8-flash-tts) + allineamento MMS_FA
python videolezioni/scripts/generate_batch.py 01-prodotti --all-missing

# Rifinitura cue/intro e gate di regressione (7 invarianti = 0)
npm run polish
npm run verify

# Build sito statico (URL puliti, search-index.json, cover OG PNG)
python videolezioni/scripts/build_pages.py
```

---

## Struttura del repository

```text
├── course.config.json          # Metadati corso, avatar Fabio e voce Ludo
├── sources/appunti/            # Sorgenti LaTeX (capitoli 01–15) e testi slide
├── videolezioni/
│   ├── assets/                 # fabio-spritesheet.png, fabio-author.jpg, icone
│   ├── lessons/                # manifest.json e capitoli (lesson.json, audio, subtitles)
│   ├── js/ & css/              # Player, live-sync, temi e avatar engine
│   └── scripts/                # Pipeline Python/Node (TTS, MMS_FA, polish, verify, build)
└── .github/workflows/          # Deploy automatico su GitHub Pages
```
