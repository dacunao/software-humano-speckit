#!/usr/bin/env python3
"""Genera los addenda de plantilla desde los artefactos que el núcleo define.

**Adición, no sustitución.** Medido sobre la herramienta: sustituir la plantilla
nativa de especificación borra `## Success Criteria` y `### Edge Cases` —las dos
secciones que el comando `analyze` busca por su nombre— y la mitad de los
marcadores `NEEDS CLARIFICATION`. La adición conserva todo eso y agrega lo que
el manifiesto exige.

La sustitución queda reservada a la plantilla de constitución, cuyo contenido es
por definición propio: es la proyección del núcleo.

Cada sección de un addendum es **un artefacto que el núcleo define**, con su
pregunta de control y su contenido mínimo citados. No hay secciones inventadas.
"""

from __future__ import annotations

import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
IDENTIFICADORES = RAIZ / "docs/method/identificadores-nucleo-v2.1.json"
SALIDA = RAIZ / "tools/speckit/software-humano-spec-kit-preset-2.0.0/templates"

# Qué artefactos del núcleo tienen su lugar en cada plantilla nativa. El reparto
# sigue el mapa mínimo por operación del anexo, que asigna A05–A08 a `plan` y
# A02/A07 a `tasks`.
REPARTO = {
    "spec": ["A01", "A02", "A03", "A04"],
    "plan": ["A05", "A06", "A07", "A08"],
    "tasks": ["A02", "A07"],
}

# Advertencias que la adición no puede resolver borrando: la plantilla nativa
# permanece y trae valores que el anexo vuelve condicionales.
ADVERTENCIAS = {
    "tasks": "**Sobre las fases y las prioridades de la plantilla nativa.** Sus rótulos `P1`, `P2`, `P3` y "
             "`MVP` solo se usan **cuando el fundamento de producto los haya definido o autorizado**. Si no "
             "los autoriza, la numeración de fases es orden de ejecución y nada más: no asigna prioridad, no "
             "declara un producto mínimo y no autoriza postergar alcance.",
}


def main() -> int:
    d = {e["id"]: e for e in json.loads(IDENTIFICADORES.read_text(encoding="utf-8"))["disposiciones"]}
    SALIDA.mkdir(parents=True, exist_ok=True)
    for plantilla, artefactos in REPARTO.items():
        L = ["", "---", "",
             "## Lo que el manifiesto exige en este artefacto", "",
             "Cada sección responde una pregunta del núcleo. Si una sección no cambia una decisión ni ayuda a "
             "verificarla, el propio núcleo dice que debe simplificarse o eliminarse: no se llena por rutina.", ""]
        for a in artefactos:
            e = d[a]
            campos = e["campos"]
            pregunta = campos.get("pregunta", "")
            contenido = campos.get("contenido", "")
            L += [f"### {e['titulo']}", "",
                  f"<!-- `{a}` · {pregunta} -->",
                  f"<!-- Contenido mínimo que el núcleo declara: {contenido} -->", ""]
            partes = [p.strip() for p in contenido.split(";") if p.strip()]
            L += ["| " + " | ".join(partes) + " |",
                  "|" + "---|" * len(partes), "|" + " |" * len(partes), ""]
        if plantilla in ADVERTENCIAS:
            L += ["### Nota sobre la plantilla nativa", "", ADVERTENCIAS[plantilla], ""]
        f = SALIDA / f"{plantilla}-addendum.md"
        f.write_text("\n".join(L), encoding="utf-8")
        print(f"  {f.name} · {len(artefactos)} artefactos: {', '.join(artefactos)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
