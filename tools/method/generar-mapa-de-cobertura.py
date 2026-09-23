#!/usr/bin/env python3
"""Genera el mapa de cobertura entre el manifiesto y su compilación.

Es el artefacto `A02` del núcleo aplicado al propio paquete: *«¿cómo se dará
cuenta de todo el alcance?»*. Su alcance es el manifiesto; su cobertura, lo que
la compilación refleja.

Cada enunciado comprobable del manifiesto queda en uno de cuatro estados:

    compilado   su texto literal está en la compilación
    fuera       queda fuera del método, con la razón decidida y escrita
    editorial   no puede cambiar una decisión de construcción
    pendiente   debería estar y no está

**No se escribe: se genera.** El censo sale del mapa de identificadores y el
estado se decide con reglas, no a mano. Un enunciado nuevo en el manifiesto
aparece como pendiente sin que nadie tenga que acordarse de agregarlo.

El criterio que separa `editorial` de lo demás es del propio manifiesto: entra
lo que puede «cambiar una decisión, detener una implementación o exigir
evidencia adicional».
"""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
IDENTIFICADORES = RAIZ / "docs/method/identificadores-nucleo-v2.1.json"
# Todo artefacto que compile el manifiesto cuenta como cobertura. Agregar uno
# aquí es lo único que hay que recordar al compilar una parte nueva.
COMPILACION = [
    RAIZ / "docs/method/inventario-de-objetos.md",
    RAIZ / "docs/method/compuertas-del-metodo.md",
]
SALIDA = RAIZ / "docs/method/mapa-de-cobertura.md"

# Secciones cuyo contenido no puede cambiar una decisión de construcción. Viajan
# en el paquete como documentación; no entran al método.
EDITORIALES = ("PROPÓSITO DEL DOCUMENTO", "EJEMPLO APLICADO", "TEXTO CANÓNICO",
               "INFLUENCIAS Y NOTAS", "(preámbulo)")

# Decisiones de la autoridad del 2026-09-23 sobre qué queda fuera y por qué.
FUERA = {
    "SH-POCKET": "Preguntas dirigidas a una persona. Su destino es el documento de quien decide, no los comandos.",
    "SH-INDEX": "Capa de navegación. El propio núcleo dice que sus identificadores «no agregan doctrina, "
                "prioridad, etapas, artefactos ni criterios: solo señalan contenido ya aprobado».",
}
# Pasajes normativos cuyo destino no es un control. La razón se escribe; no se
# omiten en silencio.
FUERA_POR_PASAJE = {
    "CONTRATO REUTILIZABLE § Instrucciones para un agente de desarrollo":
        "Su destino es el paquete, no un control: el contrato se incorpora en la plantilla de `AGENTS.md`.",
    "CONTRATO REUTILIZABLE § Prompt breve para iniciar una tarea":
        "Su destino es el paquete: es el prompt de `START_WITH_AI_AGENT.md`.",
    "PRINCIPIOS DE DISEÑO § Diez compromisos que gobiernan las decisiones":
        "Gobierna la adaptación y no el producto. El anexo lo cita como criterio para admitir un control.",
}
EDITORIAL_POR_PASAJE = {
    "DOCTRINA PARA DESARROLLO CON IA § Cuando construir cuesta menos la decisión importa más":
        "Expone por qué la doctrina importa ahora. No cambia una decisión de construcción.",
    "FLUJO DE TRABAJO § Del propósito a una solución verificable":
        "Explica qué evita el flujo. Los pasos que lo componen sí están compilados.",
}

FUERA_POR_SUBSECCION = {
    ("SH-GOV", "Control de cambios"): "Historia de versiones del manifiesto. No cambia una decisión de construcción.",
}


def norm(t: str) -> str:
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return " ".join(re.findall(r"[a-z0-9]+", t))


def censo(d: dict) -> list[dict]:
    """Los enunciados comprobables del manifiesto, con su dirección."""
    out = []

    def add(direccion, clase, texto, sub=""):
        t = " ".join(texto.split())
        if len(t) > 25:
            out.append({"direccion": direccion, "clase": clase, "texto": t, "sub": sub})

    for i, e in d.items():
        fam = e["familia"]
        if fam == "principios":
            for k, items in e["normativo"].items():
                for x in items:
                    add(f"{i} · {k}", k, x.lstrip("- "))
        elif fam in ("directivas", "contrato", "entrega", "detenciones"):
            if e.get("cuerpo"):
                add(i, fam, e["cuerpo"])
        elif fam in ("artefactos", "verificacion", "flujo"):
            campos = list((e.get("campos") or {}).values())[1:]
            if campos:
                add(i, fam, " · ".join(campos))
        elif fam in ("controles", "fundamento"):
            sub = ""
            for l in e["texto"].split("\n"):
                s = l.strip()
                if s.startswith("#"):
                    sub = re.sub(r"^#+\s*", "", s).split(" · ")[0]
                elif s.startswith("|") and not re.match(r"^\|[\s|:-]+\|$", s):
                    celdas = [c.strip() for c in s.strip("|").split("|")]
                    if celdas and not celdas[0].startswith("**"):
                        add(f"{i} · {sub}" if sub else i, "tabla", " · ".join(celdas), sub)
                elif re.match(r"^(-|\d+\\?\.)\s", s):
                    add(f"{i} · {sub}" if sub else i, "lista", s.lstrip("-0123456789\\. "), sub)
    return out


def esta_compilado(texto: str, compilado: str) -> bool:
    """Un enunciado está compilado si su texto aparece literalmente.

    Se compara también por segmento: una fila de tabla se censa unida —«Antes de
    diseñar · Fuentes, autoridad…»— y en la compilación el rótulo y su contenido
    pueden ir separados. Comparar solo la fila unida daba por pendiente lo que
    estaba compilado.
    """
    for segmento in [texto] + texto.split(" · "):
        n = norm(segmento)
        # El piso es bajo a propósito: un enunciado corto como «Estados y casos
        # extremos cubiertos» es comprobable, y un piso alto lo dejaba fuera de
        # toda comparación, es decir, pendiente para siempre.
        if len(n) >= 25 and n[:70] in compilado:
            return True
    return False


def estado(entrada: dict, compilado: str) -> tuple[str, str]:
    dir_ = entrada["direccion"]
    ident = dir_.split(" · ")[0]
    if esta_compilado(entrada["texto"], compilado):
        return "compilado", ""
    if ident in FUERA:
        return "fuera", FUERA[ident]
    for (i, sub), razon in FUERA_POR_SUBSECCION.items():
        if ident == i and entrada["sub"].startswith(sub):
            return "fuera", razon
    return "pendiente", ""


def main() -> int:
    m = json.loads(IDENTIFICADORES.read_text(encoding="utf-8"))
    d = {e["id"]: e for e in m["disposiciones"]}
    compilado = norm(" ".join(p.read_text(encoding="utf-8") for p in COMPILACION if p.exists()))

    filas = []
    for e in censo(d):
        est, razon = estado(e, compilado)
        filas.append((e, est, razon))
    for p in m["pasajes"]:
        seccion = p["titulo"].split(" § ")[0]
        e = {"direccion": p["titulo"], "clase": "pasaje", "texto": " ".join(p["texto"].split()), "sub": ""}
        if p["titulo"] in FUERA_POR_PASAJE:
            filas.append((e, "fuera", FUERA_POR_PASAJE[p["titulo"]]))
        elif p["titulo"] in EDITORIAL_POR_PASAJE:
            filas.append((e, "editorial", EDITORIAL_POR_PASAJE[p["titulo"]]))
        elif seccion in EDITORIALES:
            filas.append((e, "editorial", "Sección sin consecuencia sobre una decisión de construcción."))
        elif esta_compilado(e["texto"], compilado):
            filas.append((e, "compilado", ""))
        else:
            filas.append((e, "pendiente", ""))

    cuenta = Counter(est for _, est, _ in filas)
    total = len(filas)
    L = ["# Mapa de cobertura · manifiesto → método\n",
         "**Generado por** `tools/method/generar-mapa-de-cobertura.py`. **No se edita a mano.**\n",
         "Es el artefacto `A02` del núcleo aplicado al propio paquete: *«¿cómo se dará cuenta de todo el alcance?»*. "
         "El alcance es el manifiesto; la cobertura, lo que la compilación refleja.\n",
         "## Totales\n", "| Estado | Enunciados | |", "|---|---:|---|"]
    etiquetas = {"compilado": "su texto literal está en la compilación",
                 "fuera": "queda fuera del método, con razón decidida",
                 "editorial": "no puede cambiar una decisión de construcción",
                 "pendiente": "debería estar y no está"}
    for k in ("compilado", "fuera", "editorial", "pendiente"):
        n = cuenta.get(k, 0)
        L.append(f"| **{k}** | {n} | {etiquetas[k]} · {100*n//total}% |")
    L.append(f"| | **{total}** | enunciados comprobables del manifiesto |")

    aplicable = cuenta.get("compilado", 0) + cuenta.get("pendiente", 0)
    if aplicable:
        L.append(f"\n**Cobertura de lo que debe compilarse: {cuenta.get('compilado',0)} de {aplicable} "
                 f"({100*cuenta.get('compilado',0)//aplicable}%).** Lo editorial y lo declarado fuera no cuentan "
                 "en el denominador: no faltan, fueron decididos.\n")

    for k in ("pendiente", "fuera", "editorial", "compilado"):
        sel = [(e, r) for e, est, r in filas if est == k]
        if not sel:
            continue
        L.append(f"\n---\n\n## {k.capitalize()} · {len(sel)}\n")
        if k == "editorial":
            L.append("Secciones que el paquete distribuye como documentación y no como método.\n")
        L.append("| Dirección | Texto del manifiesto | Razón |" if k in ("fuera", "editorial")
                 else "| Dirección | Texto del manifiesto |")
        L.append("|---|---|---|" if k in ("fuera", "editorial") else "|---|---|")
        for e, r in sorted(sel, key=lambda x: x[0]["direccion"]):
            t = e["texto"].replace("|", "·")[:190]
            L.append(f"| `{e['direccion']}` | {t} | {r} |" if k in ("fuera", "editorial")
                     else f"| `{e['direccion']}` | {t} |")
    SALIDA.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"escrito {SALIDA.relative_to(RAIZ)}")
    for k in ("compilado", "pendiente", "fuera", "editorial"):
        print(f"  {cuenta.get(k,0):4d}  {k}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
