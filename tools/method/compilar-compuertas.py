#!/usr/bin/env python3
"""Compila las compuertas del método desde `SH-GOV § Puntos de control`.

El manifiesto especifica seis momentos, cada uno con su decisión requerida. No
hay que diseñarlos: hay que citarlos. El anexo v2.0 decía que las compuertas
mínimas eran dos, y esas dos las había elegido el agente.

Lo único que este archivo aporta es la CORRESPONDENCIA con SpecKit: en qué punto
del flujo nativo cae cada momento del manifiesto. Es una necesidad técnica de la
adaptación —el manifiesto no habla de SpecKit— y está sujeta a revisión. El
texto de cada decisión requerida se extrae y no se redacta.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
IDENTIFICADORES = RAIZ / "docs/method/identificadores-nucleo-v2.1.json"
SALIDA = RAIZ / "docs/method/compuertas-del-metodo.md"

# Correspondencia entre el momento que el manifiesto nombra y el punto del flujo
# nativo de SpecKit donde cae. Aporte de la adaptación, no del manifiesto.
CORRESPONDENCIA = {
    "Antes de diseñar": (
        "después de `specify` y `clarify`, antes de `plan`",
        "El fundamento de producto · Mapa del fundamento · Ficha de Job Story cuando aplique",
    ),
    "Antes de generar código": (
        "después de `tasks` y `analyze`, antes de `implement`",
        "Cobertura · Modelo de estados · IA · Registro de decisiones · Plan de aceptación",
    ),
    "Durante la construcción": (
        "dentro de `implement`, entre bloques",
        "Cobertura · Estados · Confianza · Control",
    ),
    "Antes de integrar": (
        "`analyze`, antes de incorporar el cambio",
        "Cobertura · Estados · Carga",
    ),
    "Antes de liberar": (
        "`converge`, antes de declarar terminado",
        "Plan de aceptación · Progreso · Comprensión · Control · las doce dimensiones",
    ),
    "Después de liberar": (
        "**fuera del flujo de SpecKit**: no hay operación nativa que lo cubra",
        "Progreso · Causalidad · Carga",
    ),
}


def puntos_de_control(d: dict) -> list[tuple[str, str]]:
    m = re.search(r"#### Puntos de control\n(.*?)(?=\n####|\Z)", d["SH-GOV"]["texto"], re.S)
    if not m:
        raise SystemExit("`SH-GOV` ya no contiene «Puntos de control»; el núcleo cambió")
    filas = []
    for l in m.group(1).split("\n"):
        s = l.strip()
        if s.startswith("|") and not re.match(r"^\|[\s|:-]+\|$", s):
            c = [x.strip() for x in s.strip("|").split("|")]
            if len(c) >= 2 and not c[0].startswith("**"):
                filas.append((c[0], c[1]))
    return filas


def main() -> int:
    d = {e["id"]: e for e in json.loads(IDENTIFICADORES.read_text(encoding="utf-8"))["disposiciones"]}
    filas = puntos_de_control(d)

    faltan = [m for m, _ in filas if m not in CORRESPONDENCIA]
    if faltan:
        raise SystemExit(
            "el manifiesto nombra momentos sin correspondencia declarada: " + ", ".join(faltan)
        )

    L = ["# Compuertas del método\n",
         "**Generado por** `tools/method/compilar-compuertas.py` desde `SH-GOV § Puntos de control`. **No se edita a mano.**\n",
         "El manifiesto especifica seis momentos con su decisión requerida. **Ninguna compuerta se diseña: se cita.**\n",
         "| Qué pone la adaptación | Qué pone el manifiesto |",
         "|---|---|",
         "| Dónde cae cada momento en el flujo de SpecKit, y qué objetos se comprueban ahí | El momento y su decisión requerida, literal |",
         "\n---\n"]
    for momento, decision in filas:
        donde, objetos = CORRESPONDENCIA[momento]
        L += [f"\n## {momento}\n",
              f"> **Decisión requerida.** {decision}\n",
              f"*Cita de `SH-GOV § Puntos de control`, literal.*\n",
              f"**Dónde cae en SpecKit:** {donde}",
              f"\n**Objetos que se comprueban:** {objetos}\n"]
    L += ["\n---\n\n## Lo que esta compilación deja visto\n",
          "**El último momento no tiene operación nativa.** El manifiesto exige observar resultado, fricción, "
          "abandono y errores después de liberar, y revisar el fundamento y sus supuestos cuando corresponda. "
          "El flujo de SpecKit termina antes. Es una brecha de la herramienta, no del método, y queda declarada "
          "en lugar de resolverse en silencio.\n",
          "**La adaptación no elige cuántas compuertas hay.** Son seis porque el manifiesto escribe seis.\n"]
    SALIDA.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"escrito {SALIDA.relative_to(RAIZ)} · {len(filas)} compuertas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
