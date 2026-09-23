#!/usr/bin/env python3
"""Extrae el mapa de identificadores del núcleo del manifiesto.

Este script es la fuente de verdad de toda la compilación del método. Ninguna
comprobación del preset puede citar una disposición que no aparezca aquí, y
ninguna cita puede diferir del texto que aquí se registra.

Se generó como respuesta a los diez defectos documentados en
`docs/proposals/008`, nueve de los cuales fueron errores de transcripción: el
texto del núcleo se citó de memoria en lugar de leerse. Un mapa generado no
puede equivocarse al transcribir.

No usa dependencias externas a propósito. `PyYAML` no está disponible en todos
los entornos donde el paquete se construye —es la fricción registrada en
`AGENTS.md`— y una comprobación de integridad que no puede ejecutarse no
protege nada. Por eso la salida es JSON de la biblioteca estándar.

Uso:
    extraer-identificadores.py --escribir    regenera el mapa
    extraer-identificadores.py --comprobar   falla con código 1 si el mapa quedó obsoleto
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NUCLEO = RAIZ / "docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md"
MAPA = RAIZ / "docs/method/identificadores-nucleo-v2.1.json"

VERSION_NUCLEO = "2.1"

# Qué identificadores debe haber NO se declara aquí: se lee de `SH-INDEX`, que
# es donde el núcleo los enumera. Una lista escrita en este archivo sería una
# afirmación del extractor validándose contra sí misma, que es exactamente la
# clase de error que este mapa existe para impedir.
#
# `SH-INDEX` dice de sí mismo: «Los identificadores no agregan doctrina… solo
# señalan contenido ya aprobado. Una referencia por identificador nunca
# sustituye la lectura del pasaje citado.» De ahí se sigue que este mapa es una
# capa de navegación sobre el núcleo, y no un inventario de sus obligaciones.

# Secciones de los principios cuyo contenido es normativo, es decir, el que una
# comprobación del preset puede compilar. Se seleccionan por nombre de
# encabezado y no por juicio: el extractor no decide qué es una obligación.
SUBSECCIONES_NORMATIVAS = ("Reglas de diseño", "Pruebas de decisión")


def sha(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def celdas(linea: str) -> list[str]:
    """Divide una fila de tabla Markdown en sus celdas, ya recortadas."""
    return [c.strip() for c in linea.strip().strip("|").split("|")]


class Nucleo:
    def __init__(self, ruta: Path):
        self.ruta = ruta
        self.texto = ruta.read_text(encoding="utf-8")
        self.lineas = self.texto.split("\n")
        self.anclas = self._anclas()
        self.h2 = [i for i, l in enumerate(self.lineas, 1) if l.startswith("## ")]

    def _anclas(self) -> dict[str, int]:
        salida = {}
        for i, l in enumerate(self.lineas, 1):
            m = re.match(r'<a id="([^"]+)"></a>', l.strip())
            if m:
                salida[m.group(1)] = i
        return salida

    def bloque(self, inicio: int) -> tuple[int, int]:
        """Límites de la sección que empieza en el identificador de la línea `inicio`.

        Termina en el identificador siguiente o en el encabezado H2 siguiente, lo que
        ocurra primero. Ambos hacen falta: `SH-STOP` vive dentro de una sección
        cuyo H2 llega antes que el identificador siguiente, y `SH-SCORE` al revés.

        El ancla precede a su propio encabezado, de modo que la búsqueda empieza
        después de ese encabezado. Sin eso, cada sección se cerraría en su
        propio título y devolvería un cuerpo vacío.
        """
        propio = next(
            (i for i in range(inicio + 1, len(self.lineas) + 1)
             if self.lineas[i - 1].startswith("#")),
            inicio,
        )
        candidatos = [v for v in self.anclas.values() if v > propio]
        candidatos += [v for v in self.h2 if v > propio]
        fin = min(candidatos) if candidatos else len(self.lineas) + 1
        return inicio, fin

    def extraer(self, inicio: int, fin: int) -> str:
        return "\n".join(self.lineas[inicio - 1 : fin - 1]).strip()


def subsecciones(texto: str) -> dict[str, list[str]]:
    """Agrupa el cuerpo de un principio por sus encabezados de cuarto nivel."""
    salida: dict[str, list[str]] = {}
    actual = None
    for linea in texto.split("\n"):
        if linea.startswith("#### "):
            actual = linea[5:].strip()
            salida[actual] = []
        elif actual and linea.strip():
            salida[actual].append(linea.strip())
    return salida


def principios(n: Nucleo) -> list[dict]:
    salida = []
    for i in range(1, 11):
        ident = f"P{i:02d}"
        ancla = ident.lower()
        if ancla not in n.anclas:
            raise SystemExit(f"{ident}: falta el identificador HTML <a id=\"{ancla}\">")
        ini, fin = n.bloque(n.anclas[ancla])
        cuerpo = n.extraer(ini, fin)
        # El título es el H3 que sigue al H2 «PRINCIPIO N · `Pnn`».
        titulo = next(
            (l[4:].strip() for l in cuerpo.split("\n") if l.startswith("### ")), ""
        )
        subs = subsecciones(cuerpo)
        # La última subsección de cada principio termina con un párrafo en negrita
        # —«**Señal de incumplimiento.** …»— que ilustra el principio y no es una
        # comprobación. Se excluye por su marca, no por juicio sobre su contenido.
        normativo = {
            k: [x for x in v if not x.lstrip("- ").startswith("**Señal de incumplimiento")]
            for k, v in subs.items()
            if k in SUBSECCIONES_NORMATIVAS
        }
        salida.append(
            {
                "id": ident,
                "familia": "principios",
                "titulo": titulo,
                "ancla": ancla,
                "linea_inicio": ini,
                "linea_fin": fin - 1,
                "texto": cuerpo,
                "sha256": sha(cuerpo),
                "normativo": normativo,
            }
        )
    return salida


def filas_tabla(n: Nucleo, prefijo: str, cuantos: int, familia: str,
                columnas: list[str]) -> list[dict]:
    """Extrae identificadores definidos como filas de tabla.

    Solo acepta la fila cuya PRIMERA celda empieza por el identificador. Así el
    índice operativo —que cita `P01`–`P10` en la segunda celda— no puede
    confundirse con una definición.
    """
    salida = []
    for i in range(1, cuantos + 1):
        ident = f"{prefijo}{i:02d}"
        encontrada = None
        for num, linea in enumerate(n.lineas, 1):
            if not linea.strip().startswith("|"):
                continue
            c = celdas(linea)
            if c and c[0].startswith(f"`{ident}`"):
                encontrada = (num, c)
                break
        if encontrada is None:
            raise SystemExit(f"{ident}: no se encontró su fila de definición")
        num, c = encontrada
        campos = dict(zip(columnas, c))
        # El título vive pegado al identificador en la primera celda, salvo en
        # el flujo, donde la celda contiene solo el identificador.
        titulo = c[0].replace(f"`{ident}`", "").strip()
        if not titulo and len(c) > 1:
            titulo = c[1]
        salida.append(
            {
                "id": ident,
                "familia": familia,
                "titulo": titulo,
                "ancla": None,
                "linea_inicio": num,
                "linea_fin": num,
                "texto": linea.strip(),
                "sha256": sha(linea.strip()),
                "campos": campos,
            }
        )
    return salida


def parrafos(n: Nucleo, prefijo: str, cuantos: int, familia: str,
             patron: str) -> list[dict]:
    """Extrae identificadores definidos como párrafo, lista o viñeta."""
    salida = []
    for i in range(1, cuantos + 1):
        ident = f"{prefijo}{i:02d}"
        rx = re.compile(patron.format(id=re.escape(ident)))
        encontrada = None
        for num, linea in enumerate(n.lineas, 1):
            m = rx.match(linea.strip())
            if m:
                encontrada = (num, linea.strip(), m)
                break
        if encontrada is None:
            raise SystemExit(f"{ident}: no se encontró su definición")
        num, linea, m = encontrada
        grupos = m.groupdict()
        salida.append(
            {
                "id": ident,
                "familia": familia,
                "titulo": (grupos.get("titulo") or "").strip(),
                "ancla": None,
                "linea_inicio": num,
                "linea_fin": num,
                "texto": linea,
                "sha256": sha(linea),
                "cuerpo": (grupos.get("cuerpo") or "").strip(),
            }
        )
    return salida


def controles(n: Nucleo) -> list[dict]:
    """Extrae los controles transversales, que son secciones con ancla."""
    salida = []
    for ident, ancla in (
        ("SH-INDEX", "sh-index"),
        ("SH-FUND", "sh-fund"),
        ("SH-STOP", "sh-stop"),
        ("SH-SCORE", "sh-score"),
        ("SH-AP", "sh-ap"),
        ("SH-GOV", "sh-gov"),
        ("SH-DONE", "sh-done"),
        ("SH-POCKET", "sh-pocket"),
    ):
        if ancla not in n.anclas:
            raise SystemExit(f"{ident}: falta el identificador HTML <a id=\"{ancla}\">")
        ini, fin = n.bloque(n.anclas[ancla])
        cuerpo = n.extraer(ini, fin)
        titulo = next(
            (
                re.sub(r"^#+\s*", "", l).split("·")[0].strip()
                for l in cuerpo.split("\n")
                if l.startswith("#")
            ),
            "",
        )
        salida.append(
            {
                "id": ident,
                "familia": "controles",
                "titulo": titulo,
                "ancla": ancla,
                "linea_inicio": ini,
                "linea_fin": fin - 1,
                "texto": cuerpo,
                "sha256": sha(cuerpo),
            }
        )
    return salida


def identificadores_declarados(n: Nucleo) -> set[str]:
    """Los identificadores que `SH-INDEX` enumera, con sus rangos expandidos.

    Es la única declaración que el núcleo hace de sí mismo sobre qué contiene.
    Comprobar contra ella, y no contra una lista de este archivo, es lo que
    convierte el recuento en verificación en vez de en tautología.
    """
    ini, fin = n.bloque(n.anclas["sh-index"])
    bloque = n.extraer(ini, fin)
    ids: set[str] = set()
    for m in re.finditer(r"`([A-Z-]+\d*)`\s*[–—-]+\s*`([A-Z-]+?)(\d{2})`", bloque):
        pref = re.match(r"([A-Z]+)", m.group(1)).group(1)
        desde = int(re.search(r"(\d{2})$", m.group(1)).group(1))
        for i in range(desde, int(m.group(3)) + 1):
            ids.add(f"{pref}{i:02d}")
    for m in re.finditer(r"`(SH-[A-Z]+|STOP\d{2}|[A-Z]{1,2}\d{2})`", bloque):
        ids.add(m.group(1))
    # Los extremos de un rango ya quedaron incluidos por el segundo barrido.
    return ids


def pasajes_por_seccion(n: "Nucleo", cubiertas: set[int]) -> list[dict]:
    """Los párrafos normativos del núcleo que ninguna disposición cubre.

    Se direccionan por el encabezado que el propio documento tiene, sin
    inventar identificadores ni tocar el núcleo. Decisión de la autoridad del
    2026-09-22: el 27% del núcleo queda fuera de toda disposición, y parte de
    ese texto es normativo —«cada artefacto existe para responder una pregunta,
    no para satisfacer una plantilla», por ejemplo— de modo que sin dirección
    no se puede citar.

    La selección es mecánica: se toma todo párrafo de prosa fuera de una
    disposición. No se juzga cuál es normativo; eso lo decide quien compila, y
    el buscador los ordena por pertinencia.
    """
    import re as _re
    seccion = "(preámbulo)"
    sub = ""
    salida = []
    for i, l in enumerate(n.lineas, 1):
        s_ = l.strip()
        if l.startswith("## "):
            seccion, sub = _re.sub(r"^##\s*", "", l).split(" · ")[0].strip(), ""
            continue
        if l.startswith("###"):
            sub = _re.sub(r"^#+\s*", "", l).split(" · ")[0].strip()
            continue
        if i in cubiertas or not s_ or s_.startswith(("|", "<a id=", "#")):
            continue
        if len(s_) < 60:
            continue
        direccion = f"{seccion} § {sub}" if sub else seccion
        salida.append({
            "id": direccion,
            "familia": "pasaje",
            "titulo": direccion,
            "linea_inicio": i,
            "linea_fin": i,
            "texto": s_,
            "sha256": sha(s_),
        })
    return salida


def construir() -> dict:
    n = Nucleo(NUCLEO)
    entradas = []
    entradas += principios(n)
    entradas += filas_tabla(n, "D", 6, "directivas",
                            ["identificador", "definicion", "limite"])
    entradas += filas_tabla(n, "F", 8, "flujo",
                            ["identificador", "paso", "que_hace", "resultado"])
    entradas += filas_tabla(n, "A", 8, "artefactos",
                            ["identificador", "pregunta", "contenido"])
    entradas += filas_tabla(n, "V", 12, "verificacion",
                            ["identificador", "criterio"])
    entradas += parrafos(n, "CR", 8, "contrato",
                         r"^\*\*`{id}` (?P<titulo>[^.]+)\.\*\* (?P<cuerpo>.+)$")
    entradas += parrafos(n, "O", 9, "entrega",
                         r"^\d+\\?\. `{id}` (?P<cuerpo>.+)$")
    entradas += parrafos(n, "STOP", 7, "detenciones",
                         r"^- `{id}` (?P<cuerpo>.+)$")
    entradas += controles(n)

    # Comprobación contra lo que el propio núcleo enumera en `SH-INDEX`.
    declarados = identificadores_declarados(n)
    extraidos = {e["id"] for e in entradas}
    faltan = sorted(declarados - extraidos)
    sobran = sorted(extraidos - declarados)
    if faltan:
        raise SystemExit(
            f"`SH-INDEX` declara {', '.join(faltan)} y no se extrajeron"
        )
    if sobran:
        raise SystemExit(
            f"se extrajeron {', '.join(sobran)}, que `SH-INDEX` no declara"
        )

    conteo: dict[str, int] = {}
    for e in entradas:
        conteo[e["familia"]] = conteo.get(e["familia"], 0) + 1

    fuente = NUCLEO.read_bytes()
    cubiertas = {i for e in entradas for i in range(e["linea_inicio"], e["linea_fin"] + 1)}
    pasajes = pasajes_por_seccion(n, cubiertas)

    return {
        "version_nucleo": VERSION_NUCLEO,
        "fuente": str(NUCLEO.relative_to(RAIZ)),
        "sha256_fuente": hashlib.sha256(fuente).hexdigest(),
        "generado_por": "tools/method/extraer-identificadores.py",
        "total": len(entradas),
        "conteo_por_familia": conteo,
        "disposiciones": entradas,
        "total_pasajes": len(pasajes),
        "pasajes": pasajes,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--escribir", action="store_true")
    g.add_argument("--comprobar", action="store_true")
    args = ap.parse_args()

    mapa = construir()
    serializado = json.dumps(mapa, ensure_ascii=False, indent=2) + "\n"

    if args.escribir:
        MAPA.write_text(serializado, encoding="utf-8")
        print(f"escrito {MAPA.relative_to(RAIZ)} · {mapa['total']} disposiciones")
        for f, c in sorted(mapa["conteo_por_familia"].items()):
            print(f"  {f:14s} {c:3d}")
        return 0

    if not MAPA.exists():
        print(f"falta {MAPA.relative_to(RAIZ)}; ejecuta --escribir", file=sys.stderr)
        return 1
    actual = MAPA.read_text(encoding="utf-8")
    if actual != serializado:
        print(
            f"{MAPA.relative_to(RAIZ)} no corresponde al núcleo vigente.\n"
            "El núcleo cambió o el mapa se editó a mano. Regenera con --escribir "
            "y revisa qué disposición se movió antes de confirmar.",
            file=sys.stderr,
        )
        return 1
    print(f"mapa al día · {mapa['total']} disposiciones")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
