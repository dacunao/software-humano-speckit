#!/usr/bin/env python3
"""Comprueba que ningún término se use como doctrina sin estar en el núcleo.

Implementa la comprobación 13 del anexo v2.0:

    Todo término que un artefacto use como doctrina aparece en el núcleo, o
    está declarado como maquinaria de la adaptación.

Existe porque en una sola sesión se inventaron cuatro conceptos —«ángulo»,
«capa transversal», «libro mayor», «nivel de conformidad»— que no nombraban
doctrina, porque el manifiesto no los tiene, ni nombraban maquinaria, porque no
describen nada técnico. Eran conceptos inventados para ordenar el manifiesto, y
ordenar el manifiesto no le corresponde a la adaptación.

**Qué mira, y por qué solo eso.** No toda la prosa: solo los términos en
posición de definición —encabezados, cabeceras de tabla, rótulos de fila y
negritas—, que es donde un concepto se instituye. Mirar toda la prosa produce
ciento treinta y cuatro candidatos, casi todos palabras corrientes del español
ausentes de un documento de mil líneas; mirar las posiciones de definición
produce catorce. Una comprobación con ese ruido enseña a ignorarla, que es el
modo de fallo advertido en `docs/proposals/006`.

**La carga está invertida a propósito.** La herramienta no adivina qué término
es sospechoso: exige que la maquinaria esté declarada. Lo que no esté ni en el
núcleo ni en el glosario, se detiene.

    tools/method/comprobar-vocabulario.py
    tools/method/comprobar-vocabulario.py --candidatos   # para poblar el glosario
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
IDENTIFICADORES = RAIZ / "docs/method/identificadores-nucleo-v2.1.json"
GLOSARIO = RAIZ / "docs/method/vocabulario-de-maquinaria.md"

# Artefactos que gobiernan la adaptación o viajan al proyecto. Las propuestas no
# entran: son análisis y registro, no distribuyen doctrina.
ARTEFACTOS = [
    "docs/method/Anexo_Aplicacion_SpecKit_v2.0.md",
    "docs/product/FUNDAMENTO_DEL_PAQUETE_DE_METODO.md",
    "docs/method/inventario-de-objetos.md",
    "package/AGENTS.md",
    "package/CLAUDE.md",
    "package/README.md",
    "package/START_WITH_AI_AGENT.md",
    "package/PARA_QUIEN_DECIDE.md",
    "package/instructions/00_REQUISITOS_DE_INSTALACION.md",
    "package/instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md",
]

ARTICULOS = re.compile(r"^(el|la|los|las|un|una|de|del|al)\b\s*")

# Una frase que empieza por interrogativo describe una relación; no instituye un
# término. Quitar el interrogativo —como se hacía antes— convertía «Qué
# compromiso lo gobierna» en algo con forma de concepto, y era la señal misma de
# que no lo era.
INTERROGATIVA = re.compile(r"^(que|como|cuando|donde|quien|cuanto|cual|cuales|por que|para que)\b")

# Un término inventado es una frase nominal corta. Lo más largo que apareció en
# la sesión que motivó esta comprobación fue «nivel de conformidad», tres
# palabras. Por encima de eso son títulos y oraciones.
MAX_PALABRAS = 3


def normalizar(t: str) -> str:
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9ñ·]", " ", t)).strip()


def en_el_nucleo(termino: str, nuc: str) -> bool:
    """Si el término aparece en el núcleo, tolerando el número gramatical.

    «punto de control» es del manifiesto, que lo escribe «Puntos de control».
    Exigir coincidencia exacta marcaba como invención un término que la fuente
    trae en plural, y deformar la prosa para que coincida sería peor que el
    falso positivo.
    """
    palabras = termino.split()
    variantes = {termino}
    for i, w in enumerate(palabras):
        for alt in (w + "s", w[:-1] if w.endswith("s") else None):
            if alt:
                variantes.add(" ".join(palabras[:i] + [alt] + palabras[i + 1:]))
    return any(v in nuc for v in variantes)


def nucleo() -> str:
    m = json.loads(IDENTIFICADORES.read_text(encoding="utf-8"))
    return normalizar(
        " ".join([e["texto"] for e in m["disposiciones"]] + [p["texto"] for p in m["pasajes"]])
    )


def glosario() -> set[str]:
    """Los términos de maquinaria declarados, con su justificación, en su propio archivo."""
    if not GLOSARIO.exists():
        return set()
    terminos = set()
    for l in GLOSARIO.read_text(encoding="utf-8").split("\n"):
        s = l.strip()
        if s.startswith("|") and "---" not in s:
            primera = [c.strip() for c in s.strip("|").split("|")][0]
            t = normalizar(primera.strip("*` "))
            if t and t != "termino":
                terminos.add(t)
    return terminos


def en_posicion_de_definicion(texto: str) -> list[str]:
    """Frases que instituyen un término: encabezados, cabeceras y rótulos de tabla, negritas."""
    salida = []
    lineas = texto.split("\n")
    for i, l in enumerate(lineas):
        s = l.strip()
        if s.startswith("#"):
            salida.append(re.sub(r"^#+\s*", "", s))
        if s.startswith("|") and "---" not in s:
            celdas = [c.strip() for c in s.strip("|").split("|")]
            # De la cabecera se toman todas las celdas: cada una nombra una
            # columna. Del resto, solo la primera: las demás son valores, no
            # términos, y tomarlas produce ruido como «fusionados» o «dos objetos».
            siguiente = lineas[i + 1].strip() if i + 1 < len(lineas) else ""
            salida.extend(celdas if re.match(r"^\|[\s|:-]+\|$", siguiente) else celdas[:1])
        # Negrita solo al principio de la línea: es el patrón con que se
        # instituye un término —«**Nombre.** Explicación»—. La negrita a media
        # frase es énfasis —«**no instales**», «**detente**»— y tomarla produce
        # falsos positivos sobre cualquier documento con prosa enfática.
        m = re.match(r"^(?:[-*]\s+|\d+\.\s+)?\*\*(.+?)\*\*", s)
        if m:
            salida.append(m.group(1))
    return salida


def resolver(r: str) -> Path:
    """Una ruta dada a mano se toma tal cual; una de la lista, contra la raíz.

    Sin esto, probar la herramienta contra copias con defectos plantados lee en
    silencio los archivos reales, y la prueba parece pasar sin haber mirado nada.
    """
    p = Path(r)
    if p.is_absolute() or p.exists():
        return p
    return RAIZ / r


def terminos_de(rutas: list[str]) -> Counter:
    cuenta: Counter = Counter()
    for r in rutas:
        p = resolver(r)
        if not p.exists():
            continue
        for frase in en_posicion_de_definicion(p.read_text(encoding="utf-8")):
            # Un encabezado suele llevar el término y luego su glosa, separados
            # por «·». Se parte por ahí. No se emiten prefijos de frases largas:
            # se probó, y sube la detección de un caso a costa de pasar de veinte
            # candidatos a ciento noventa. Una comprobación con ese ruido enseña
            # a ignorarla.
            for segmento in normalizar(re.sub(r"`[^`]*`", "", frase)).split("·"):
                segmento = segmento.strip()
                if INTERROGATIVA.match(segmento):
                    continue
                f = ARTICULOS.sub("", segmento)
                if 4 <= len(f) <= 40 and len(f.split()) <= MAX_PALABRAS and not f.replace(" ", "").isdigit():
                    cuenta[f] += 1
    return cuenta


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidatos", action="store_true",
                    help="lista los términos no declarados, para poblar el glosario")
    ap.add_argument("--artefactos", nargs="*", help="rutas alternativas a comprobar")
    args = ap.parse_args()

    if not IDENTIFICADORES.exists():
        raise SystemExit("falta el mapa de identificadores; ejecuta extraer-identificadores.py")
    nuc, glo = nucleo(), glosario()
    rutas = args.artefactos or ARTEFACTOS
    cuenta = terminos_de(rutas)

    sin_declarar = sorted(
        ((n, t) for t, n in cuenta.items()
         if n >= 2 and not en_el_nucleo(t, nuc) and t not in glo),
        reverse=True,
    )
    print(f"artefactos comprobados: {len([r for r in rutas if resolver(r).exists()])}")
    print(f"maquinaria declarada:   {len(glo)} términos")
    print()
    if args.candidatos:
        for n, t in sin_declarar:
            print(f"| {t} | | {n} |")
        return 0
    for n, t in sin_declarar:
        print(f"ERROR C13 · «{t}» se usa como término definido {n} veces; "
              f"no está en el núcleo ni declarado como maquinaria")
    print(f"\n{len(sin_declarar)} término(s) sin declarar")
    return 1 if sin_declarar else 0


if __name__ == "__main__":
    raise SystemExit(main())
