#!/usr/bin/env python3
"""Busca en el núcleo antes de abrir una decisión a la persona.

Existe porque la regla 11 de `AGENTS.md` —«antes de abrir una decisión a la
persona, comprueba que las fuentes rectoras no la resuelvan ya; debes poder
nombrar qué fuente consultaste»— se incumplió siete veces en una sola sesión.
Una regla que depende de que el agente la recuerde es combustible. Esto la
vuelve residuo: la consulta se ejecuta y su salida se pega, o la pregunta no
se formula.

    tools/method/consultar.py "cuántos estados debe cubrir un componente"

Devuelve los pasajes del núcleo que tratan el asunto, con su dirección. Si
alguno lo resuelve, no hay decisión que trasladar: hay una cita que aplicar.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
IDENTIFICADORES = RAIZ / "docs/method/identificadores-nucleo-v2.1.json"

VACIAS = set(
    "para como que con por los las del una uno pero cuando donde este esta esto "
    "sobre entre debe deben cada toda todo sin mas ser sus esta estan puede "
    "pueden cual cuales cuanto cuantos hay son era fue han sino solo tambien "
    "desde hasta segun ante bajo tras".split()
)


def normalizar(t: str) -> list[str]:
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return [p for p in re.findall(r"[a-z]{4,}", t) if p not in VACIAS]


def pasajes(d: dict) -> list[tuple[str, str, str]]:
    """Cada pasaje del núcleo con su dirección: (direccion, clase, texto)."""
    salida = []
    for ident, e in d.items():
        for clase, items in (e.get("normativo") or {}).items():
            for x in items:
                salida.append((f"{ident} · {clase}", clase, x.lstrip("- ").strip()))
        if e.get("cuerpo"):
            salida.append((ident, "cuerpo", e["cuerpo"]))
        for k, v in (e.get("campos") or {}).items():
            if k != "identificador" and len(str(v)) > 20:
                salida.append((ident, k, str(v)))
        if e["familia"] in ("controles", "fundamento"):
            for l in e["texto"].split("\n"):
                s = l.strip()
                if s.startswith("|") and not re.match(r"^\|[\s|:-]+\|$", s):
                    for c in [x.strip() for x in s.strip("|").split("|")][1:]:
                        if len(c) > 30:
                            salida.append((f"{ident} · tabla", "tabla", c))
                elif re.match(r"^(-|\d+\\?\.)\s", s) and len(s) > 30:
                    salida.append((f"{ident} · lista", "lista", s.lstrip("-0123456789\\. ")))
    return salida


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    if not IDENTIFICADORES.exists():
        raise SystemExit("falta el mapa de identificadores; ejecuta extraer-identificadores.py --escribir")
    pregunta = set(normalizar(" ".join(sys.argv[1:])))
    if not pregunta:
        raise SystemExit("la consulta no tiene términos buscables")
    mapa = json.loads(IDENTIFICADORES.read_text(encoding="utf-8"))
    d = {e["id"]: e for e in mapa["disposiciones"]}
    fuentes = pasajes(d)
    # Los pasajes normativos sin identificador se citan por su sección. Sin
    # ellos la búsqueda es ciega al 27% del núcleo.
    for x in mapa.get("pasajes", []):
        fuentes.append((x["id"], "pasaje sin identificador", x["texto"]))
    marcados = []
    for direccion, clase, texto in fuentes:
        t = set(normalizar(texto))
        if not t:
            continue
        # Cobertura de la pregunta, no similitud: importa cuánto de lo preguntado
        # aparece en el pasaje, no cuánto se parecen los dos textos.
        puntaje = len(pregunta & t) / len(pregunta)
        if puntaje > 0:
            marcados.append((puntaje, direccion, clase, texto))
    marcados.sort(key=lambda x: (-x[0], x[1]))
    if not marcados or marcados[0][0] < 0.2:
        print("El núcleo no trae un pasaje que trate esto directamente.")
        print("Revisa igualmente los más cercanos antes de abrir la decisión:\n")
    for puntaje, direccion, clase, texto in marcados[:8]:
        t = " ".join(texto.split())
        print(f"[{puntaje:.2f}] {direccion}  ({clase})")
        print(f"        {t[:220]}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
