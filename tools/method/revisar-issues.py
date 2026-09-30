#!/usr/bin/env python3
"""Resumen de lo que espera respuesta.

Existe porque la responsabilidad de responder es de una persona, y una persona
no puede sostenerla mirando una bandeja de notificaciones donde el ruido y lo
que exige respuesta llegan iguales.

Distingue lo único que importa para decidir a qué mirar:

  · abierto por un tercero y sin contestar → exige respuesta
  · abierto por un tercero y ya contestado → esperando al otro
  · abierto por nosotros                   → es el roadmap, no una urgencia

No responde nada ni marca nada como leído. Solo mira.

Uso:  python3 tools/method/revisar-issues.py [--dias N]
"""
import json
import subprocess
import sys
from datetime import datetime, timezone

REPO = "dacunao/software-humano-speckit"
DUENO = "dacunao"
ENVIOS = [("github/spec-kit", 4802), ("github/spec-kit", 4803)]


def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return json.loads(r.stdout) if r.stdout.strip() else None


def dias(iso):
    return (datetime.now(timezone.utc) - datetime.fromisoformat(iso.replace("Z", "+00:00"))).days


def main():
    ventana = 7
    if "--dias" in sys.argv:
        ventana = int(sys.argv[sys.argv.index("--dias") + 1])

    if subprocess.run(["gh", "auth", "status"], capture_output=True).returncode != 0:
        print("gh sin sesión. Ejecuta: gh auth login")
        return 2

    print(f"\n  Revisión de {REPO} · {datetime.now():%Y-%m-%d %H:%M}")
    print("  " + "─" * 58 + "\n")

    issues = gh("issue", "list", "--repo", REPO, "--state", "open", "--limit", "100",
                "--json", "number,title,author,createdAt,updatedAt,comments") or []

    sin_respuesta, contestados, propios = [], [], []
    for i in issues:
        if i["author"]["login"] == DUENO:
            propios.append(i)
            continue
        # ¿Habló alguien de casa después del último mensaje del autor?
        ultimo = i["comments"][-1]["author"]["login"] if i["comments"] else i["author"]["login"]
        (contestados if ultimo == DUENO else sin_respuesta).append(i)

    if sin_respuesta:
        print("  EXIGE RESPUESTA · abierto por otra persona, sin contestar")
        for i in sorted(sin_respuesta, key=lambda x: x["createdAt"]):
            print(f"    #{i['number']}  {i['title'][:62]}")
            print(f"          de @{i['author']['login']} · hace {dias(i['createdAt'])} días"
                  f" · {len(i['comments'])} comentarios")
        print()
    else:
        print("  Nada de terceros esperando respuesta.\n")

    if contestados:
        print("  YA CONTESTADO · esperando a la otra persona")
        for i in contestados:
            print(f"    #{i['number']}  {i['title'][:62]} · sin novedad hace {dias(i['updatedAt'])} días")
        print()

    movidos = [i for i in propios if dias(i["updatedAt"]) <= ventana]
    cola = f", {len(movidos)} con movimiento en {ventana} días" if movidos else ", sin movimiento"
    print(f"  Hoja de ruta: {len(propios)} temas abiertos{cola}")
    for i in movidos:
        print(f"    #{i['number']}  {i['title'][:62]}")

    print("\n  Envíos al catálogo de comunidad de SpecKit")
    for repo, n in ENVIOS:
        d = gh("issue", "view", str(n), "--repo", repo,
               "--json", "number,title,state,comments,updatedAt")
        if not d:
            print(f"    #{n}  no se pudo leer")
            continue
        # El bot que etiqueta no cuenta como revisión.
        humanos = [c for c in d["comments"] if c["author"]["login"] != "github-actions"]
        estado = "REVISADO" if humanos else "sin revisar"
        print(f"    #{d['number']}  {d['state']:6}  {estado:11}  hace {dias(d['updatedAt'])} días"
              f"  {d['title'][:38]}")
        for c in humanos[-2:]:
            print(f"          @{c['author']['login']}: {c['body'][:110]}")

    print("\n  Nada de esto responde ni marca como leído: responder es de una persona.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
