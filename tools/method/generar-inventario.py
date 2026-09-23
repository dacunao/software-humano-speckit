#!/usr/bin/env python3
"""Genera el inventario de objetos a partir del mapa de identificadores del núcleo.

Regla que gobierna este archivo, dictada por la autoridad:

    Un objeto entra al método solo si el manifiesto lo nombra. Las obligaciones
    se adhieren a cosas que el manifiesto ya nombra; no crean cosas nuevas.

Por eso los objetos no se redactan aquí: son los que el núcleo nombra como
cosas. El núcleo nombra cosas en dos lugares —sus ocho artefactos y sus doce
dimensiones de verificación— más el fundamento de producto, que nombra aparte.
Las demás familias no nombran cosas: los principios nombran compromisos, el
flujo nombra pasos, el contrato nombra momentos, la entrega nombra contenidos
de informe y las detenciones nombran condiciones. Todas ellas se adhieren a un objeto
que el manifiesto sí nombra.

Lo único que este archivo aporta es el REPARTO: qué disposiciones del núcleo
hablan de cada objeto. Ese reparto es juicio y está sujeto a revisión humana. El texto de cada disposición se extrae y no se redacta.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
IDENTIFICADORES = RAIZ / "docs/method/identificadores-nucleo-v2.1.json"
SALIDA = RAIZ / "docs/method/inventario-de-objetos.md"

# Qué puede aportar una disposición sobre un objeto, en orden de lectura.
APORTES = [
    ("que_es", "Qué es"),
    ("compromiso", "Qué compromiso lo gobierna"),
    ("directiva", "Qué exige antes de implementar"),
    ("paso", "Qué paso del flujo lo produce"),
    ("artefacto", "Dónde vive"),
    ("instruccion", "Qué debe hacer el agente"),
    ("informe", "Qué debe informar"),
    ("evidencia", "Qué evidencia exige"),
    ("detencion", "Cuándo detenerse"),
]

# REPARTO DE DISPOSICIONES POR OBJETO · aporte de esta propuesta, sujeto a revisión.
# Una entrada `("P08", 0)` significa: la primera regla de diseño de ese principio.
OBJETOS = [
    # El fundamento entra desde afuera: lo escribe producto. Las disposiciones que le corresponden son las
    # que hablan de leerlo y de detenerse si no existe, no los de producirlo.
    ("SH-FUND", "El fundamento de producto", {
        "que_es": ["SH-FUND"], "compromiso": [("P01", 0)], "directiva": ["D01"],
        "detencion": ["STOP01"]}),
    # El mapa lo produce el método. Las disposiciones que le corresponden son las de producirlo, informarlo
    # y detenerse si una ambigüedad material se cierra sin autorización.
    ("A01", "Mapa del fundamento", {
        "que_es": ["A01"], "paso": ["F01"], "instruccion": ["CR02"],
        "informe": ["O01"], "detencion": ["STOP04"]}),
    ("A02 · V01", "Cobertura", {
        "que_es": ["V01"], "paso": ["F02", "F03"], "artefacto": ["A02"],
        "instruccion": ["CR03", "CR07"], "informe": ["O02", "O06"],
        "detencion": ["STOP02", "STOP03"]}),
    ("A03", "Ficha de Job Story cuando aplique", {
        "que_es": ["A03"], "compromiso": [("P01", 2), ("P02", 2)], "paso": ["F04"],
        "instruccion": ["CR02"], "informe": ["O03"], "evidencia": ["V02", "V03"]}),
    ("A04", "Contrato de experiencia", {
        "que_es": ["A04"], "compromiso": [("P05", 2)], "paso": ["F05"],
        "instruccion": ["CR05"], "informe": ["O07"], "evidencia": ["V04", "V06"]}),
    ("A05", "Modelo de estados", {
        "que_es": ["A05"], "compromiso": [("P08", 0)], "directiva": ["D02"],
        "paso": ["F06"], "instruccion": ["CR07"], "informe": ["O07"],
        "evidencia": ["V09"]}),
    ("A06 · V05", "Carga", {
        "que_es": ["V05"], "compromiso": [("P06", 0), ("P06", 1), ("P06", 2),
                                          ("P03", 1), ("P03", 2)],
        "directiva": ["D03"], "artefacto": ["A06"], "instruccion": ["CR07"]}),
    ("A07", "Plan de aceptación", {
        "que_es": ["A07"], "compromiso": [("P02", 0), ("P02", 1), ("P08", 2)],
        "directiva": ["D05"], "paso": ["F08"], "instruccion": ["CR08"],
        "informe": ["O08", "O04"], "evidencia": ["V01"], "detencion": ["STOP07"]}),
    ("A08", "Registro de decisiones", {
        "que_es": ["A08"], "directiva": ["D03"], "paso": ["F07"],
        "instruccion": ["CR04", "CR01"], "informe": ["O05"]}),
    ("V02", "Progreso", {
        "que_es": ["V02"], "compromiso": [("P01", 1)], "paso": ["F04"],
        "artefacto": ["A03"], "detencion": ["STOP07"]}),
    ("V03", "Causalidad", {
        "que_es": ["V03"], "compromiso": [("P01", 3)], "artefacto": ["A03"]}),
    ("V04", "Comprensión", {
        "que_es": ["V04"], "compromiso": [("P05", 0), ("P05", 1), ("P08", 1),
                                          ("P03", 0)],
        "instruccion": ["CR05"], "artefacto": ["A04"], "detencion": ["STOP05"]}),
    ("V06", "Profundidad", {
        "que_es": ["V06"], "compromiso": [("P04", 0), ("P04", 1), ("P04", 2)],
        "instruccion": ["CR05"], "artefacto": ["A04"]}),
    ("V07", "Confianza", {
        "que_es": ["V07"], "compromiso": [("P07", 0), ("P07", 2), ("P10", 0)],
        "instruccion": ["CR06"]}),
    ("V08", "Control", {
        "que_es": ["V08"], "compromiso": [("P10", 1), ("P10", 2), ("P07", 1)],
        "directiva": ["D06"], "instruccion": ["CR06"]}),
    ("V09", "Estados", {
        "que_es": ["V09"], "compromiso": [("P09", 2)], "artefacto": ["A05"],
        "informe": ["O07"]}),
    ("V10", "Accesibilidad", {
        "que_es": ["V10"], "directiva": ["D05"], "artefacto": ["A07"]}),
    ("V11", "Rendimiento", {
        "que_es": ["V11"], "compromiso": [("P09", 0), ("P09", 1)], "artefacto": ["A05"]}),
    ("V12", "IA", {
        "que_es": ["V12"], "directiva": ["D04", "D06"],
        "paso": ["F06"], "instruccion": ["CR06"], "detencion": ["STOP06"]}),
]

# El núcleo nombra tres cosas dos veces. Afirmar que son una sola cosa es una
# interpretación, no un dato, así que se listan separadas y la equivalencia se
# somete a revisión en vez de aplicarse.
# El núcleo nombra cuatro cosas dos veces. La regla que resolvió los cuatro casos:
#
#   Un artefacto y una dimensión de verificación son el MISMO objeto cuando la
#   dimensión verifica exactamente lo que el artefacto registra. Son DOS objetos
#   cuando el artefacto registra más de lo que la dimensión verifica, o cuando la
#   dimensión abarca más de un artefacto.
#
# Decidido por la autoridad el 2026-09-22.
NOMBRADAS_DOS_VECES = [
    ("SH-FUND", "A01", "dos objetos",
     "El fundamento entra desde afuera; el mapa es lo que el método produce para "
     "reflejarlo. `F01` exige un «mapa fiel de la definición de producto, sin "
     "reformularla»: no se exige fidelidad de una cosa consigo misma."),
    ("A02", "V01", "un objeto",
     "Mismo sujeto. El artefacto es dónde se registra; la dimensión es qué debe "
     "resultar cierto. **Fusionados.**"),
    ("A05", "V09", "dos objetos",
     "`A05` abarca seis contenidos, de los cuales los estados son uno. `V09` "
     "verifica una sola propiedad sobre situaciones que se reparten entre dos "
     "objetos. Ni uno contiene al otro ni coinciden."),
    ("A06", "V05", "un objeto",
     "La pregunta del artefacto —«¿qué carga estamos agregando?»— es literalmente "
     "el nombre de la dimensión. **Fusionados.** La dimensión agrega un criterio "
     "que la tabla no contiene: si el sistema podía resolverlo de forma segura."),
]

# Ocho disposiciones no se adhieren a un objeto porque se aplican a todos. No es
# un vacío del inventario: el núcleo las escribe para aplicarse a todos, y
# dejarlas implícitas sería tan malo como omitirlas.
SIN_OBJETO_PROPIO = [
    ("SH-STOP", "Antes de generar, sobre cualquier objeto"),
    ("SH-SCORE", "Al valorar el conjunto antes de liberar"),
    ("SH-AP", "Señales de que algún objeto se está incumpliendo"),
    ("SH-GOV", "Quién decide sobre cualquier objeto"),
    ("SH-DONE", "Cuándo el conjunto está terminado"),
    ("O09", "Qué informar sobre cualquier objeto que quede abierto"),
    ("SH-POCKET", "Preguntas para una persona; no es ejecutable"),
    ("SH-INDEX", "Cómo se citan los identificadores; no es una obligación"),
]


def pruebas_de(d, objeto_angulos) -> list[tuple[str, str]]:
    """Las «Pruebas de decisión» de los principios que este objeto ya cita.

    El núcleo escribió una bateria de comprobaciones por principio. No hay que
    redactarlas ni elegirlas: hay que mostrarlas donde aplican. Se heredan del
    reparto de reglas ya revisado, así que no introducen juicio nuevo.
    """
    principios: list[str] = []
    for refs in objeto_angulos.values():
        for r in refs:
            if isinstance(r, tuple) and r[0].startswith("P") and r[0] not in principios:
                principios.append(r[0])
    salida = []
    for p in principios:
        for prueba in d[p]["normativo"].get("Pruebas de decisión", []):
            salida.append((p, prueba.lstrip("- ").strip()))
    return salida


def cargar():
    return {e["id"]: e for e in json.loads(IDENTIFICADORES.read_text(encoding="utf-8"))["disposiciones"]}


def texto(d, ref):
    """Fragmento literal de una referencia. Nunca redactado."""
    if isinstance(ref, tuple):
        ident, n = ref
        reglas = d[ident]["normativo"].get("Reglas de diseño", [])
        if n < len(reglas):
            return d[ident]["titulo"], reglas[n].lstrip("- ").strip()
        return d[ident]["titulo"], ""
    e = d[ref]
    if e.get("cuerpo"):
        return e.get("titulo", ""), e["cuerpo"]
    if e.get("campos"):
        v = list(e["campos"].values())[1:]
        return e.get("titulo", ""), " · ".join(v)
    if ref == "SH-FUND":
        m = re.search(r"El fundamento de producto es (.*?)(?:\n\n)", e["texto"], re.S)
        return e["titulo"], "El fundamento de producto es " + " ".join(m.group(1).split())
    if e["familia"] == "controles":
        # Un control extenso se resume por su propio subtítulo cuando lo tiene:
        # es lo que el núcleo escribió para decir de qué trata la sección. Sin
        # eso, la primera línea de prosa puede ser una nota de cierre y engañar
        # sobre el contenido, como ocurre con los antipatrones.
        lineas = [l.rstrip() for l in e["texto"].split("\n")
                  if l.strip() and not l.startswith("<a id=")]
        lineas = lineas[1:]  # el encabezado propio de la sección
        for l in lineas:
            if l.startswith("#"):
                return e.get("titulo", ""), l.lstrip("# ").strip()
            if not l.startswith("|"):
                return e.get("titulo", ""), l.strip()
        return e.get("titulo", ""), ""
    return e.get("titulo", ""), " ".join(e["texto"].split())[:300]


def main() -> int:
    d = cargar()
    L = []
    L.append("# Inventario de objetos del manifiesto\n")
    L.append("**Generado por** `tools/method/generar-inventario.py` desde el mapa de identificadores del núcleo v2.1. **No se edita a mano.**\n")
    L.append("""## Qué es esto y qué garantiza

Un objeto entra aquí **solo si el manifiesto lo nombra**. El núcleo nombra cosas
en tres lugares: sus ocho artefactos, sus doce dimensiones de verificación y el
fundamento de producto. Las demás familias no nombran cosas —los principios
nombran compromisos, el flujo nombra pasos, el contrato nombra momentos, la
entrega nombra contenidos de informe y las detenciones nombran condiciones—:
**se adhieren** a un objeto que el manifiesto sí nombra.

| Qué hay aquí | Quién lo pone | Se revisa |
|---|---|---|
| El nombre de cada objeto | El núcleo | No hace falta |
| El texto literal de cada disposición | Extracción mecánica del núcleo | No hace falta |
| **Qué disposiciones corresponden a cada objeto** | **Esta propuesta** | **Sí. Es lo único que hay que revisar** |

**Cómo revisar cada objeto:** leer las frases de su tabla y responder una sola
pregunta — *¿hablan todas de esta misma cosa?* Si alguna no corresponde, o si
falta una que debería estar, eso es el hallazgo.
\n""")
    L.append(f"**{len(OBJETOS)} objetos.**\n\n---\n")
    for ident, nombre, angulos in OBJETOS:
        L.append(f"\n## {ident} · {nombre}\n")
        L.append("| Qué aporta | Disposición del núcleo | Texto literal |")
        L.append("|---|---|---|")
        for clave, etiqueta in APORTES:
            for ref in angulos.get(clave, []):
                titulo, t = texto(d, ref)
                origen = f"`{ref[0]}` regla {ref[1] + 1}" if isinstance(ref, tuple) else f"`{ref}`"
                if titulo and not isinstance(ref, tuple):
                    origen += f" {titulo}"
                elif isinstance(ref, tuple):
                    origen += f" · {titulo}"
                t = t.replace("|", "·").strip()
                L.append(f"| {etiqueta} | {origen} | {t} |")
        L.append("")
    # Las «Pruebas de decisión» son del principio, no del objeto: el núcleo las
    # escribe una vez por principio. Repetirlas en cada objeto que cita una de
    # sus reglas las multiplicaría sin agregar nada.
    L.append("\n---\n\n## Las comprobaciones que el núcleo ya escribe\n")
    L.append("Cada principio trae su propia batería, bajo el encabezado «Pruebas de decisión». **No hay que redactarlas ni elegirlas**: el manifiesto las escribió. Se listan por principio, con los objetos donde cayeron sus reglas de diseño.\n")
    donde = {}
    for ident, nombre, ang in OBJETOS:
        for refs in ang.values():
            for r in refs:
                if isinstance(r, tuple):
                    donde.setdefault(r[0], []).append(nombre)
    for n in range(1, 11):
        pid = f"P{n:02d}"
        pruebas = d[pid]["normativo"].get("Pruebas de decisión", [])
        if not pruebas:
            continue
        objetos = sorted(set(donde.get(pid, [])))
        L.append(f"\n### `{pid}` {d[pid]['titulo']}\n")
        L.append(f"*Sus reglas de diseño están en: {', '.join(objetos) if objetos else '—'}.*\n")
        for prueba in pruebas:
            L.append(f"- {prueba.lstrip('- ').strip()}")
        L.append("")
    L.append("\n---\n\n## Ocho disposiciones que no pertenecen a un objeto\n")
    L.append("No se adhieren a un objeto porque **se aplican a todos**. Declararlo es parte del inventario: dejarlo implícito sería tan malo como omitirlas.\n")
    L.append("| De dónde | Cuándo actúa | Qué dice el núcleo, literal |")
    L.append("|---|---|---|")
    for ident, cuando in SIN_OBJETO_PROPIO:
        titulo, t = texto(d, ident)
        t = " ".join(t.replace("|", "·").split())[:300]
        L.append(f"| `{ident}` {titulo} | {cuando} | {t} |")
    L.append("\n---\n\n## Nombradas dos veces por el núcleo\n")
    L.append("El núcleo nombra cuatro cosas dos veces. La regla que resolvió los cuatro casos:\n")
    L.append("> Un artefacto y una dimensión de verificación son el **mismo** objeto cuando la dimensión verifica exactamente lo que el artefacto registra. Son **dos** objetos cuando el artefacto registra más de lo que la dimensión verifica, o cuando la dimensión abarca más de un artefacto.\n")
    for a, b, veredicto in [(x[0], x[1], x[2]) for x in NOMBRADAS_DOS_VECES]:
        razon = next(x[3] for x in NOMBRADAS_DOS_VECES if x[0] == a and x[1] == b)
        ta, txa = texto(d, a)
        tb, txb = texto(d, b)
        L.append(f"\n### `{a}` {ta} ↔ `{b}` {tb} → **{veredicto}**\n")
        L.append("| De dónde | Qué dice el núcleo, literal |")
        L.append("|---|---|")
        L.append(f"| `{a}` | {' '.join(txa.replace('|', '·').split())[:320]} |")
        L.append(f"| `{b}` | {' '.join(txb.replace('|', '·').split())[:320]} |")
        L.append(f"\n{razon}\n")
    SALIDA.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"escrito {SALIDA.relative_to(RAIZ)} · {len(OBJETOS)} objetos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
