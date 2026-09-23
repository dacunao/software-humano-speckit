#!/usr/bin/env python3
"""Genera los ocho comandos del preset desde la compilación.

Ningún cuerpo se redacta. Cada comprobación es una cita literal del manifiesto,
tomada del inventario de objetos, y se incluye en una operación si el mapa
mínimo del anexo le asigna ese identificador.

**Estos comandos no declaran frontmatter, y eso es la decisión de diseño.**

La composición de SpecKit, en `presets/__init__.py`, hace esto con cada capa:

    fm, layer_body = _split_frontmatter(layer_content)
    if strategy == "replace":
        top_frontmatter_text = fm
    elif fm:
        top_frontmatter_text = fm

Una capa que declara frontmatter reemplaza el del core. Una capa que no lo
declara **conserva el del core entero**: descripción, `handoffs` y `scripts`.

La versión 1.2.0 declaraba frontmatter y con eso borró los `handoffs` —el
encadenamiento nativo entre comandos— en los cinco que los traen. El defecto no
se arregla redeclarando esas claves, porque entonces hay que acordarse de cada
una para siempre. Se arregla no declarando ninguna.

Consecuencia aceptada: la descripción queda en su forma nativa. Es la superficie
por la que un agente reconoce cuándo invocar el comando, y la evidencia dice que
las nativas funcionan —nombran verbo, artefacto y entrada— y que el agente dejó
de invocar cuando la adaptación las reemplazó por garantías.

La estrategia se declara en `preset.yml`, no en el archivo, así que prescindir
del frontmatter no cuesta nada.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "tools/speckit/software-humano-spec-kit-preset-2.0.0/commands"

# Las ocho operaciones que el preset compone. No llevan descripción: la nativa
# sobrevive porque esta capa no declara frontmatter.
OPERACIONES = [
    "constitution", "specify", "clarify", "plan",
    "tasks", "analyze", "implement", "converge",
]

# Lo que la adaptación agrega a `constitution` es maquinaria, no doctrina: el
# manifiesto no habla de SpecKit ni de dónde vive una constitución. Se declara
# como tal en lugar de presentarse entre las citas.
MAQUINARIA_CONSTITUTION = """\
## Maquinaria de la adaptación · no es doctrina del manifiesto

El manifiesto no habla de SpecKit ni de dónde vive una constitución. Lo que
sigue lo exige el anexo de aplicación, y se declara aparte para que no se
confunda con lo que exige el núcleo.

- La plantilla resuelta contiene la proyección completa del núcleo aprobado y es
  la única fuente autorizada para su contenido.
- Un prompt circunstancial no puede resumir, mejorar, contextualizar ni enmendar
  esa proyección.
- Si la constitución existente contiene una versión distinta o cambios humanos no
  reconciliados, informa la diferencia y detente antes de sobrescribirla.
- Informa si las quince familias de identificadores están presentes y si algún
  marcador quedó sin resolver.
"""

_DESCRIPCIONES_RETIRADAS = {
    "specify": "Crea o actualiza la especificación de la funcionalidad a partir del fundamento de producto "
               "autorizado, en la forma que ese fundamento ya tenga.",
    "clarify": "Identifica en la especificación lo que quedó indeterminado y lo resuelve con la autoridad de "
               "producto, en rondas de hasta cinco preguntas.",
    "plan": "Ejecuta la planificación usando la plantilla de plan para generar los artefactos de diseño de todo "
            "el alcance especificado.",
    "tasks": "Genera un tasks.md accionable y ordenado por dependencias, a partir de los artefactos de diseño "
             "disponibles y con cobertura del alcance completo.",
    "implement": "Ejecuta el plan de implementación procesando las tareas definidas en tasks.md, dentro del "
                 "alcance y la autoridad aprobados.",
    "analyze": "Analiza la consistencia entre spec.md, plan.md y tasks.md sin modificarlos, y comprueba su "
               "correspondencia con la constitución.",
    "constitution": "Instala o verifica la constitución del proyecto desde la proyección aprobada del núcleo, "
                    "sin reinterpretarla.",
    "converge": "Reconcilia la implementación y su evidencia contra el alcance aprobado, y cierra únicamente "
                "las brechas de ese alcance.",
}


def core_pack() -> Path:
    c = sorted(Path.home().glob(".cache/uv/archive-*/*/specify_cli/core_pack"))
    if not c:
        raise SystemExit("no se encontró el core_pack de SpecKit")
    return c[-1]


def frontmatter_nativo(core: Path, nombre: str) -> dict[str, str]:
    """Bloques de primer nivel del frontmatter nativo, como texto."""
    f = core / "commands" / f"{nombre}.md"
    if not f.exists():
        return {}
    m = re.match(r"---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
    if not m:
        return {}
    bloques, clave = {}, None
    for l in m.group(1).split("\n"):
        k = re.match(r"^([a-z_-]+):(.*)$", l)
        if k:
            clave = k.group(1)
            bloques[clave] = l
        elif clave:
            bloques[clave] += "\n" + l
    return bloques


def comprobaciones(g, d) -> list[tuple[str, str, str, str]]:
    """(identificador, objeto, qué aporta, texto literal) de todo el inventario."""
    out = []
    for _, nombre, ang in g.OBJETOS:
        for clave, etiqueta in g.APORTES:
            for ref in ang.get(clave, []):
                if isinstance(ref, tuple) and len(ref) == 3:
                    out.append((ref[0], nombre, etiqueta, g.fila_de_subseccion(d, *ref)))
                elif isinstance(ref, tuple) and isinstance(ref[1], str):
                    for f in g.filas_de_subseccion(d, ref[0], ref[1]):
                        out.append((ref[0], nombre, etiqueta, f))
                else:
                    _, t = g.texto(d, ref)
                    out.append((ref[0] if isinstance(ref, tuple) else ref, nombre, etiqueta, t))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--solo", help="genera un único comando, para revisarlo")
    args = ap.parse_args()

    import importlib.util

    def cargar_modulo(nombre, ruta):
        s = importlib.util.spec_from_file_location(nombre, RAIZ / ruta)
        m = importlib.util.module_from_spec(s)
        s.loader.exec_module(m)
        return m

    g = cargar_modulo("g", "tools/method/generar-inventario.py")
    c = cargar_modulo("c", "tools/method/comprobar-conformidad.py")
    d = g.cargar()
    mapa = c.leer_mapa_anexo()
    comps = comprobaciones(g, d)
    core = core_pack()

    SALIDA.mkdir(parents=True, exist_ok=True)
    operaciones = [o for o in OPERACIONES if not args.solo or o == args.solo]
    for op in operaciones:
        minimo = mapa.get(op, set())
        sel = [x for x in comps if x[0] in minimo]
        falta = sorted(i for i in minimo if not any(x[0] == i for x in comps))

        # El core va primero, como en el preset de referencia de SpecKit: sus
        # instrucciones son lo que el agente ejecuta, y las comprobaciones son
        # lo último que lee antes de actuar.
        L = ["{CORE_TEMPLATE}", "", "---", ""]
        if op == "constitution":
            L += [MAQUINARIA_CONSTITUTION, ""]
        L.append("## Lo que el manifiesto exige en esta operación\n")
        L.append("Cada fila es una cita literal del núcleo. No hay redacción propia: si una fila no puede "
                 "responderse mirando un artefacto, eso es el hallazgo.\n")
        # Agrupado por identificador y no por objeto. Un identificador lo citan
        # varios objetos —`CR07` lo citan carga, cobertura y modelo de estados—,
        # y agrupar por objeto repetía la misma exigencia dos y tres veces. La
        # exigencia es una; los objetos son el contexto donde se comprueba.
        por_ident: dict[str, tuple[str, set]] = {}
        for ident, objeto, _etiqueta, texto in sel:
            t = " ".join(texto.split()).replace("|", "·")
            clave = (ident, t)
            por_ident.setdefault(clave, set()).add(objeto)
        L.append("| Dónde lo dice el manifiesto | Qué exige | Dónde se comprueba |")
        L.append("|---|---|---|")
        for (ident, t), objetos in por_ident.items():
            L.append(f"| `{ident}` | {t} | {' · '.join(sorted(objetos))} |")
        if falta:
            for i in falta:
                e = d.get(i, {})
                t = e.get("cuerpo") or e.get("titulo", "")
                L.append(f"| `{i}` | {' '.join(str(t).split())} | todos los objetos |")
        L.append("")
        (SALIDA / f"speckit.{op}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
        print(f"  speckit.{op}.md · {len(por_ident) + len(falta)} exigencias · "
              f"{len(sel)} apariciones antes de deduplicar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
