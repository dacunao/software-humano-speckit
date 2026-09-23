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
COMPILACION = RAIZ / "docs/method/inventario-de-objetos.md"
SALIDA = RAIZ / "docs/method/mapa-de-cobertura.md"

# Secciones cuyo contenido no puede cambiar una decisión de construcción. Viajan
# en el paquete como documentación; no entran al método.
EDITORIALES = ("PROPÓSITO DEL DOCUMENTO", "EJEMPLO APLICADO", "TEXTO CANÓNICO",
               "INFLUENCIAS Y NOTAS", "(preámbulo)")

# Decisiones de la autoridad del 2026-09-23 sobre qué queda fuera y por qué.
FUERA = {
    "SH-POCKET": "Preguntas dirigidas a una persona. Su destino es el documento de quien decide, no los comandos.",
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


def estado(entrada: dict, compilado: str) -> tuple[str, str]:
    dir_ = entrada["direccion"]
    ident = dir_.split(" · ")[0]
    if norm(entrada["texto"])[:70] in compilado:
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
    compilado = norm(COMPILACION.read_text(encoding="utf-8"))

    filas = []
    for e in censo(d):
        est, razon = estado(e, compilado)
        filas.append((e, est, razon))
    for p in m["pasajes"]:
        seccion = p["titulo"].split(" § ")[0]
        e = {"direccion": p["titulo"], "clase": "pasaje", "texto": " ".join(p["texto"].split()), "sub": ""}
        if seccion in EDITORIALES:
            filas.append((e, "editorial", "Sección sin consecuencia sobre una decisión de construcción."))
        elif norm(e["texto"])[:70] in compilado:
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
