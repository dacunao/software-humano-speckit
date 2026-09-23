#!/usr/bin/env python3
"""Comprueba que el preset conserva lo que el núcleo, el anexo y SpecKit exigen.

Esta prueba existe porque las versiones 1.x acumularon diez defectos y ninguna
capa podía detectar uno solo. Nueve de los diez no fueron errores de criterio:
fueron transcripciones y contratos rotos. Ver `docs/proposals/008`.

Seis comprobaciones, cada una atada a un defecto observado:

    C1  toda cita resuelve a una disposición real del núcleo
    C2  cada comando cubre el mapa mínimo que el anexo le asigna
    C3  el wrap conserva los metadatos que SpecKit no arrastra por su cuenta
    C4  las plantillas conservan los tokens nativos de SpecKit
    C5  las secciones que los comandos del core buscan por nombre existen
    C6  ningún texto se atribuye a un identificador que no lo contiene  (aviso)

Ni el núcleo ni el anexo se leen a mano: C1 usa el mapa de identificadores generado por
`extraer-identificadores.py` y C2 extrae la tabla del anexo. Teclear cualquiera de los
dos reintroduciría el modo de fallo que esta prueba busca cerrar.

Salida: código 1 si hay errores. Los avisos no detienen el build.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
MAPA_IDENTIFICADORES = RAIZ / "docs/method/identificadores-nucleo-v2.1.json"
def anexo_vigente() -> Path:
    """El anexo de versión más alta presente en el repositorio.

    Las versiones anteriores se conservan: siguen gobernando las instalaciones
    que las usan. La conformidad se comprueba siempre contra la vigente.
    """
    candidatos = sorted((RAIZ / "docs/method").glob("Anexo_Aplicacion_SpecKit_v*.md"))
    return candidatos[-1] if candidatos else RAIZ / "docs/method/Anexo_Aplicacion_SpecKit_v1.2.md"


ANEXO = anexo_vigente()

RX_ID = re.compile(r"`(SH-[A-Z]+|STOP\d{2}|CR\d{2}|[PDFAOV]\d{2})`")
RX_RANGO = re.compile(r"`([A-Z]+?)(\d{2})`\s*[–—-]+\s*`([A-Z]+?)(\d{2})`")

# Secciones que los comandos del core localizan por su nombre en la plantilla.
# Renombrarlas no rompe nada visible: rompe la instrucción del comando nativo,
# en silencio. Es el defecto 9.
CONTRATO_PLANTILLA = {
    "plan-template": ["Constitution Check"],
    "spec-template": ["Success Criteria", "Edge Cases"],
}

# SpecKit arrastra estas claves del comando nativo al compuesto por su cuenta
# (`presets/__init__.py`, rama `strategy == "wrap"`). Cualquier otra clave que el
# core declare y el wrap omita se pierde: el wrap sustituye el frontmatter
# completo. `handoffs` es el caso observado — el mecanismo de encadenamiento
# entre comandos, borrado en los cinco que lo declaran. Es el defecto 7.
CLAVES_QUE_SPECKIT_ARRASTRA = {"scripts", "agent_scripts", "argument-hint"}

PALABRAS_VACIAS = {
    "cada", "toda", "todo", "ningún", "ninguna", "ningun", "existe", "declara",
    "antes", "después", "sobre", "entre", "entre", "entre", "debe", "puede",
    "entre", "donde", "cuando", "según", "entre", "tiene", "tienen", "queda",
    "quedan", "estar", "están", "sin", "para", "como", "que", "con", "por",
    "aplica", "aplicable", "aplicables", "propio", "propia", "mismo", "misma",
    "operación", "comprobación", "comprobaciones", "disposición", "verificable",
    "artefacto", "artefactos", "proyecto", "resultado", "resultados", "decisión",
    "decisiones", "humana", "humano", "persona", "personas", "agente", "núcleo",
    "manifiesto", "anexo", "preset", "spec", "plan", "tasks", "implement",
}


def visible(ruta: Path) -> str:
    """Ruta relativa a la raíz cuando está dentro, absoluta cuando no.

    `--preset` puede apuntar a una copia fuera del repositorio, que es como se
    prueba esta misma herramienta contra un preset con defectos plantados.
    """
    try:
        return str(ruta.relative_to(RAIZ))
    except ValueError:
        return str(ruta)


def fallo(msg: str) -> None:
    raise SystemExit(f"conformidad: {msg}")


def expandir(texto: str) -> set[str]:
    """Identificadores citados en `texto`, con los rangos ya expandidos."""
    ids = {m.group(1) for m in RX_ID.finditer(texto)}
    for m in RX_RANGO.finditer(texto):
        p1, n1, p2, n2 = m.groups()
        if p1 == p2:
            ids.update(f"{p1}{i:02d}" for i in range(int(n1), int(n2) + 1))
    return ids


def leer_mapa_anexo() -> dict[str, set[str]]:
    """Extrae la tabla «Mapa mínimo por operación» del anexo.

    Se extrae en vez de teclearse por la misma razón que el mapa de identificadores: una
    lista copiada a mano es exactamente el defecto que esta prueba persigue.
    """
    if not ANEXO.exists():
        fallo(f"falta el anexo en {ANEXO.relative_to(RAIZ)}")
    lineas = ANEXO.read_text(encoding="utf-8").split("\n")
    try:
        inicio = next(
            i for i, l in enumerate(lineas)
            if l.strip().startswith("### Mapa mínimo por operación")
        )
    except StopIteration:
        fallo("el anexo no contiene «### Mapa mínimo por operación»")
    mapa: dict[str, set[str]] = {}
    for linea in lineas[inicio:]:
        s = linea.strip()
        if not s.startswith("|"):
            if mapa and not s:
                continue
            if mapa:
                break
            continue
        celdas = [c.strip() for c in s.strip("|").split("|")]
        if len(celdas) < 2:
            continue
        m = re.fullmatch(r"`([a-z]+)`", celdas[0])
        if not m:
            continue
        mapa[m.group(1)] = expandir(celdas[1])
    if not mapa:
        fallo("no se pudo extraer ninguna fila del mapa mínimo del anexo")
    return mapa


def frontmatter(texto: str) -> tuple[dict, str]:
    """Separa el frontmatter YAML de un comando sin depender de PyYAML.

    Solo necesita reconocer claves de primer nivel, que es lo que las
    comprobaciones miran.
    """
    if not texto.startswith("---\n"):
        return {}, texto
    fin = texto.find("\n---\n", 4)
    if fin == -1:
        return {}, texto
    bloque = texto[4:fin]
    cuerpo = texto[fin + 5:]
    claves: dict[str, str] = {}
    clave = None
    for linea in bloque.split("\n"):
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", linea)
        if m:
            clave = m.group(1)
            claves[clave] = m.group(2).strip()
        elif clave and linea.strip():
            claves[clave] += " " + linea.strip()
    return claves, cuerpo


def localizar_core(explicito: str | None) -> Path:
    if explicito:
        p = Path(explicito)
        if not (p / "commands").is_dir():
            fallo(f"{p} no parece un core_pack de SpecKit")
        return p
    candidatos = sorted(
        Path.home().glob(".cache/uv/archive-*/*/specify_cli/core_pack")
    )
    if not candidatos:
        fallo(
            "no se encontró el core_pack de SpecKit. Pásalo con --core "
            "o instala el paquete con tools/speckit/specify."
        )
    return candidatos[-1]


def localizar_preset(explicito: str | None) -> Path:
    if explicito:
        return Path(explicito)
    candidatos = sorted((RAIZ / "tools/speckit").glob("software-humano-*"))
    if not candidatos:
        fallo("no se encontró el directorio del preset en tools/speckit/")
    return candidatos[-1]


def palabras(texto: str) -> set[str]:
    crudo = re.findall(r"[a-záéíóúñü]{5,}", texto.lower())
    return {p for p in crudo if p not in PALABRAS_VACIAS}


class Informe:
    def __init__(self) -> None:
        self.errores: list[tuple[str, str]] = []
        self.avisos: list[tuple[str, str]] = []

    def error(self, comprobacion: str, msg: str) -> None:
        self.errores.append((comprobacion, msg))

    def aviso(self, comprobacion: str, msg: str) -> None:
        self.avisos.append((comprobacion, msg))


def c1_citas_existen(preset: Path, anclas: dict, inf: Informe) -> None:
    conocidos = set(anclas) | {"SH-INDEX"}
    for archivo in sorted((preset / "commands").glob("*.md")):
        for ident in sorted(expandir(archivo.read_text(encoding="utf-8"))):
            if ident not in conocidos:
                inf.error(
                    "C1",
                    f"{archivo.name} cita `{ident}`, que no existe en el núcleo",
                )


def c2_cobertura_mapa(preset: Path, mapa: dict[str, set[str]], inf: Informe) -> None:
    for operacion, minimo in sorted(mapa.items()):
        archivo = preset / "commands" / f"speckit.{operacion}.md"
        if not archivo.exists():
            if operacion == "checklist":
                continue  # el anexo lo conserva nativo, sin adaptar
            inf.error("C2", f"el anexo asigna `{operacion}` y el preset no lo provee")
            continue
        citados = expandir(archivo.read_text(encoding="utf-8"))
        faltan = sorted(minimo - citados)
        if faltan:
            inf.error(
                "C2",
                f"{archivo.name} no cita {', '.join('`%s`' % f for f in faltan)}, "
                f"que el mapa mínimo del anexo le asigna",
            )


def c3_metadatos_conservados(preset: Path, core: Path, inf: Informe) -> None:
    for archivo in sorted((preset / "commands").glob("*.md")):
        nombre = archivo.stem.replace("speckit.", "")
        origen = core / "commands" / f"{nombre}.md"
        if not origen.exists():
            continue
        fm_core, _ = frontmatter(origen.read_text(encoding="utf-8"))
        fm_wrap, _ = frontmatter(archivo.read_text(encoding="utf-8"))
        if fm_wrap.get("strategy") != "wrap":
            continue
        for clave in fm_core:
            if clave in ("description", "strategy"):
                continue
            if clave in CLAVES_QUE_SPECKIT_ARRASTRA:
                continue
            if clave not in fm_wrap:
                inf.error(
                    "C3",
                    f"{archivo.name} descarta `{clave}` del comando nativo; "
                    f"el wrap sustituye el frontmatter completo",
                )


def c4_tokens_plantillas(preset: Path, core: Path, inf: Informe) -> None:
    for archivo in sorted((preset / "templates").glob("*.md")):
        origen = core / "templates" / archivo.name
        if not origen.exists():
            continue
        t_core = origen.read_text(encoding="utf-8")
        t_preset = archivo.read_text(encoding="utf-8")
        tokens = set(re.findall(r"__SPECKIT_COMMAND_[A-Z0-9_]+__", t_core))
        perdidos = sorted(t for t in tokens if t not in t_preset)
        if perdidos:
            inf.error(
                "C4",
                f"{archivo.name} pierde {len(perdidos)} token(s) nativo(s): "
                f"{', '.join(perdidos)}",
            )


def c5_contrato_plantilla(preset: Path, inf: Informe) -> None:
    for nombre, secciones in sorted(CONTRATO_PLANTILLA.items()):
        archivo = preset / "templates" / f"{nombre}.md"
        if not archivo.exists():
            continue
        texto = archivo.read_text(encoding="utf-8")
        for seccion in secciones:
            if seccion.lower() not in texto.lower():
                inf.aviso(
                    "C5",
                    f"{archivo.name} no contiene la sección «{seccion}», que el "
                    f"comando nativo busca por su nombre",
                )


def c6_atribucion_cruzada(preset: Path, anclas: dict, inf: Informe) -> None:
    """Detecta texto citado bajo un identificador que pertenece a otro.

    Busca secuencias literales, y solo las **distintivas**: las que aparecen en
    una única disposición del núcleo. El vocabulario doctrinal compartido
    —«todos los elementos obligatorios»— no prueba nada, porque vive en media
    docena de disposiciones a la vez. Una frase que existe en un solo lugar sí.

    No se mide el solapamiento de vocabulario. Una comprobación compilada usa
    palabras propias: esa es la traducción que se le pide, y penalizarla sería
    medir al revés. Lo que sí es un defecto es reproducir una frase del núcleo
    bajo el identificador equivocado. Fue el defecto 4: los seis estados de
    `V09` rotulados `P08`, con pérdida de «recuperación».

    **Emite avisos y no errores, a propósito.** Sobre el preset 1.2.0 acierta en
    tres de siete: los cuatro restantes son colisiones morfológicas —«criterio»
    contra «criterios», «cubrirlo» contra «cubrir el alcance»—. Una comprobación
    que se equivoca la mitad de las veces enseña a ignorarla, que es el modo de
    fallo advertido en `docs/proposals/006`.

    La versión 2.0 la vuelve exacta sin heurística: si cada comprobación
    compilada declara su identificador **y el fragmento literal que cita**, verificar es
    comparar cadenas. Mientras ese formato no exista, esto es lo mejor
    disponible y no debe detener un build.
    """
    def trigramas(texto: str) -> set[tuple[str, ...]]:
        t = re.findall(r"[a-záéíóúñü]+", texto.lower())
        return {tuple(t[i:i + 3]) for i in range(len(t) - 2)}

    # Dueño de cada secuencia, cuando es única en todo el núcleo.
    conteo: dict[tuple[str, ...], list[str]] = {}
    for ident, entrada in anclas.items():
        for tri in trigramas(json.dumps(entrada, ensure_ascii=False)):
            conteo.setdefault(tri, []).append(ident)
    dueno = {tri: ids[0] for tri, ids in conteo.items() if len(ids) == 1}

    for archivo in sorted((preset / "commands").glob("*.md")):
        for linea in archivo.read_text(encoding="utf-8").split("\n"):
            ids = [i for i in expandir(linea) if i in anclas]
            if len(ids) != 1:
                continue  # con varias citas no se puede atribuir una frase
            citado = ids[0]
            # En una tabla de tres columnas la tercera es contexto —dónde se
            # comprueba—, no cita. Mirarla atribuye al identificador de la fila
            # un texto que solo nombra el objeto, y eso es un falso positivo.
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            if linea.strip().startswith("|") and len(celdas) >= 3:
                linea = celdas[1]
            ajenas: dict[str, list[str]] = {}
            for tri in trigramas(RX_ID.sub(" ", linea)):
                otro = dueno.get(tri)
                if otro and otro != citado:
                    ajenas.setdefault(otro, []).append(" ".join(tri))
            for otro, frases in sorted(ajenas.items()):
                if len(frases) >= 2:
                    inf.aviso(
                        "C6",
                        f"{archivo.name}: texto atribuido a `{citado}` cuya "
                        f"redacción solo existe en `{otro}` "
                        f"— «{'», «'.join(sorted(frases)[:3])}»",
                    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--preset", help="directorio del preset a comprobar")
    ap.add_argument("--core", help="core_pack de SpecKit")
    ap.add_argument("--estricto", action="store_true",
                    help="trata los avisos como errores")
    args = ap.parse_args()

    if not MAPA_IDENTIFICADORES.exists():
        fallo("falta el mapa de identificadores; ejecuta tools/method/extraer-identificadores.py --escribir")
    mapa_json = json.loads(MAPA_IDENTIFICADORES.read_text(encoding="utf-8"))
    anclas = {e["id"]: e for e in mapa_json["disposiciones"]}

    preset = localizar_preset(args.preset)
    core = localizar_core(args.core)
    mapa_anexo = leer_mapa_anexo()

    print(f"preset  {visible(preset)}")
    print(f"core    {visible(core)}")
    print(f"identificadores  {len(anclas)} disposiciones · anexo {len(mapa_anexo)} operaciones")
    print()

    inf = Informe()
    c1_citas_existen(preset, anclas, inf)
    c2_cobertura_mapa(preset, mapa_anexo, inf)
    c3_metadatos_conservados(preset, core, inf)
    c4_tokens_plantillas(preset, core, inf)
    c5_contrato_plantilla(preset, inf)
    c6_atribucion_cruzada(preset, anclas, inf)

    for etiqueta, entradas in (("ERROR", inf.errores), ("aviso", inf.avisos)):
        for comprobacion, msg in entradas:
            print(f"{etiqueta} {comprobacion} · {msg}")

    print()
    print(f"{len(inf.errores)} error(es), {len(inf.avisos)} aviso(s)")
    if inf.errores or (args.estricto and inf.avisos):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
