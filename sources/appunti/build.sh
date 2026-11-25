#!/usr/bin/env bash
# Compila gli appunti. Uso (da questa cartella):
#   ./build.sh            compila soltanto (usa i dati già presenti in dati/)
#   ./build.sh dati       rigenera prima i dati delle figure con script/genera_dati.py (richiede uv)
# Il PDF si chiama <NOME>_v<N>.pdf, con N letto da versione.tex: i PDF delle versioni precedenti restano intatti.
set -euo pipefail
cd "$(dirname "$0")"
NOME="ASE_Appunti"

if [ "${1:-}" = "dati" ] && [ -f script/genera_dati.py ]; then
  uv run script/genera_dati.py
fi

VERSIONE=$(sed -n 's/.*\\newcommand{\\versione}{\([0-9][0-9]*\)}.*/\1/p' versione.tex)
if [ -z "$VERSIONE" ]; then
  echo "Numero di versione non trovato in versione.tex" >&2
  exit 1
fi

tectonic -X compile main.tex
cp main.pdf "${NOME}_v${VERSIONE}.pdf"
echo "PDF: $(pwd)/${NOME}_v${VERSIONE}.pdf"
