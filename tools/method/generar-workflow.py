#!/usr/bin/env python3
"""Genera el workflow del método desde las compuertas compiladas.

Ninguna compuerta se diseña. `SH-GOV § Puntos de control` especifica seis
momentos con su decisión requerida, y el mensaje de cada `gate` es esa decisión
citada al pie de la letra.

Lo único que este archivo aporta, y está sujeto a revisión: **dónde cae cada
momento en el flujo nativo de SpecKit**. Es una necesidad técnica —el manifiesto
no habla de SpecKit— y se declara como tal.

**Por qué el workflow y no un hook.** El texto del comando nativo de SpecKit dice
«you MUST actually invoke the hook»: es una instrucción dirigida al agente, que
puede omitirla en silencio. Los pasos de un workflow los ejecuta el motor:
`shell` corre por `subprocess` y `gate` aborta con código distinto de cero. Es el
único lugar de SpecKit donde el cumplimiento no depende del agente.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
IDENTIFICADORES = RAIZ / "docs/method/identificadores-nucleo-v2.1.json"
SALIDA = RAIZ / "tools/speckit/workflow-software-humano-2.0.0/workflow.yml"

CONFORMIDAD = ".specify/extensions/conformidad/scripts/conformidad.sh"

# Dónde cae cada momento del manifiesto en el flujo nativo. Aporte de la
# adaptación. `None` significa que SpecKit no tiene dónde ponerlo, y eso se
# declara en lugar de resolverse en silencio.
UBICACION = {
    "Antes de diseñar":        {"despues_de": "clarify",   "id": "antes-de-disenar"},
    "Antes de generar código": {"despues_de": "analyze",   "id": "antes-de-generar-codigo",
                                "conformidad": True},
    "Durante la construcción": {"despues_de": None,
                                "razon": "ocurre dentro de `implement`, y una operación de SpecKit "
                                         "no admite una compuerta en su interior"},
    "Antes de integrar":       {"despues_de": "implement", "id": "antes-de-integrar"},
    "Antes de liberar":        {"despues_de": "converge",  "id": "antes-de-liberar",
                                "conformidad": True},
    "Después de liberar":      {"despues_de": None,
                                "razon": "el flujo de SpecKit termina antes; no hay operación nativa "
                                         "que observe resultado, fricción, abandono y errores"},
}

# El flujo nativo, en su orden. El workflow no inventa operaciones.
SECUENCIA = ["specify", "clarify", "plan", "tasks", "analyze", "implement", "converge"]


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
    puntos = dict(puntos_de_control(d))
    faltan = [m for m in puntos if m not in UBICACION]
    if faltan:
        raise SystemExit("momentos sin ubicación declarada: " + ", ".join(faltan))

    L = ['schema_version: "1.0"', "", "workflow:",
         '  id: "software-humano"',
         '  name: "Ciclo SDD con las compuertas del manifiesto"',
         '  version: "2.0.0"',
         '  author: "Damián Acuña"',
         '  description: "Ejecuta el ciclo nativo de SpecKit con las compuertas que el Manifiesto de '
         'Software Humano especifica, y la comprobación de conformidad en los momentos que el propio '
         'manifiesto nombra."', "",
         "requires:",
         "  # 1.0.0 es la primera versión donde la composición conserva el frontmatter",
         "  # del core cuando la capa del preset no declara uno.",
         '  speckit_version: ">=1.0.0,<2.0.0"', "",
         "inputs:",
         "  fundamento:",
         "    type: string",
         "    required: true",
         '    prompt: "Ruta del fundamento de producto autorizado, en la forma que ya tenga"',
         "  integration:",
         "    type: string",
         '    default: "auto"',
         '    prompt: "Integración a usar; auto toma la del proyecto"', "",
         "steps:"]

    for op in SECUENCIA:
        L += [f"  - id: {op}",
              f"    command: speckit.{op}",
              '    integration: "{{ inputs.integration }}"',
              "    input:",
              '      args: "{{ inputs.fundamento }}"', ""]
        for momento, ubic in UBICACION.items():
            if ubic.get("despues_de") != op:
                continue
            if ubic.get("conformidad"):
                L += [f"  - id: conformidad-{ubic['id']}",
                      "    type: shell",
                      "    # Lo ejecuta el motor, no el agente. Sale con 1 si falta algo",
                      "    # sin excepción aprobada, y el workflow se detiene.",
                      f"    run: \"{CONFORMIDAD}\"", ""]
            L += [f"  - id: compuerta-{ubic['id']}",
                  "    type: gate",
                  f"    # `SH-GOV § Puntos de control` · {momento}. Mensaje citado al pie de la letra.",
                  f"    message: \"{momento}. {puntos[momento]}\"",
                  "    # `approve` y `reject` son los valores que el motor reconoce: con",
                  "    # cualquier otro, `on_reject` no se aplica y la compuerta no detiene",
                  "    # nada. Son tokens del mecanismo, no prosa.",
                  "    options: [approve, reject]",
                  "    on_reject: abort", ""]

    L += ["# Momentos que el manifiesto especifica y este workflow no puede expresar.",
          "# Se declaran para que la brecha sea visible y no se descubra a medio camino."]
    for momento, ubic in UBICACION.items():
        if ubic.get("despues_de") is None:
            L.append(f"#   {momento}: {ubic['razon']}.")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text("\n".join(L) + "\n", encoding="utf-8")
    expresadas = sum(1 for u in UBICACION.values() if u.get("despues_de"))
    print(f"escrito {SALIDA.relative_to(RAIZ)}")
    print(f"  {expresadas} de {len(UBICACION)} compuertas expresables · "
          f"{sum(1 for u in UBICACION.values() if u.get('conformidad'))} comprobaciones de conformidad")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
