# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy==2.5.4"]
# ///
# Versioni fissate: con versioni diverse i numeri possono cambiare di poco. Aggiungere qui altre librerie se servono
# (ad esempio "scipy==1.18.1", "scikit-learn==1.9.1", "matplotlib==3.11.2"), sempre con versione esatta.
"""Genera i dati numerici delle figure "calcolate" (cartella dati/).

Ogni figura che mostra dati veri (curve adattate, confini di decisione, simulazioni, ...) legge da qui le sue
coordinate; i numeri citati in didascalie ed esempi finiscono in dati/valori.tex come macro LaTeX \\val<Nome>.
Tutto è deterministico (semi fissi).

Uso (dalla cartella degli appunti):  uv run script/genera_dati.py
"""
from __future__ import annotations

import os
from pathlib import Path

import numpy as np

OUT = Path(__file__).resolve().parent.parent / "dati"
OUT.mkdir(exist_ok=True)
MACRO: dict[str, str] = {}


def save(name: str, rows, header: str):
    """Scrive una tabella per pgfplots (prima riga = nomi delle colonne); None diventa una riga vuota (salto)."""
    with open(OUT / name, "w", encoding="utf-8") as f:
        f.write(header + "\n")
        for r in rows:
            if r is None:
                f.write("\n")
            else:
                f.write(" ".join(f"{v:.6g}" if isinstance(v, (float, np.floating)) else str(v) for v in r) + "\n")


def num(v, d=3):
    """Numero in formato italiano per LaTeX: 0{,}253."""
    return f"{v:.{d}f}".replace(".", "{,}")


# --------------------------------------------------------------------------- una funzione per figura
def esempio():
    rng = np.random.default_rng(0)
    x = np.linspace(0, 1, 50)
    save("esempio.dat", zip(x, x ** 2 + 0.05 * rng.standard_normal(50)), "x y")
    MACRO["esempioMedia"] = num(float(np.mean(x ** 2)))


def main():
    esempio()
    with open(OUT / "valori.tex", "w", encoding="utf-8") as f:
        f.write("% generato da script/genera_dati.py: non modificare a mano\n")
        for k, v in MACRO.items():
            f.write(f"\\newcommand{{\\val{k}}}{{{v}}}\n")
    print("dati scritti in", OUT)
    for k, v in MACRO.items():
        print(f"  {k} = {v}")


if __name__ == "__main__":
    os.chdir(Path(__file__).resolve().parent.parent)
    main()
