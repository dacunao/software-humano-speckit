# Instrucciones del proyecto

Las reglas persistentes que gobiernan este repositorio están en `AGENTS.md` y se cargan desde aquí. `AGENTS.md` es la fuente única: este archivo la referencia, no la duplica ni la reinterpreta.

@AGENTS.md

## Entorno de este repositorio

Lo siguiente describe cómo está montado el entorno. No agrega doctrina, no altera el alcance del PRD y no sustituye ninguna disposición de `AGENTS.md`.

### Raíz del proyecto

`PROJECT_ROOT` es la raíz de este repositorio Git. El contenido del paquete de inicio v1.0.0 vive directamente en ella, como indica `README.md`.

La integridad del paquete se comprueba desde la raíz:

```bash
shasum -a 256 -c SHA256SUMS
```

Deben verificar 25 de 25 archivos. Un resultado menor significa que un archivo del paquete fue modificado o eliminado, e invalida la evidencia de integridad.

### SpecKit

Este proyecto usa **SpecKit v1.0.8 en una instancia aislada**, fijada mediante `uvx`. El preset Software Humano v1.0.0 exige el rango `>=1.0.0,<2.0.0`.

Usa siempre el envoltorio del repositorio:

```bash
tools/speckit/specify <subcomando>
```

No uses el `specify` instalado globalmente. Ese ejecutable permanece en **0.15.0** —fuera del rango exigido por el preset— y da servicio a otros proyectos del usuario cuyo `.specify/` fue generado con esa versión. Actualizarlo o reemplazarlo excede la autoridad de este proyecto y requiere una decisión humana separada.

### Scripts de SpecKit: shim de python3 obligatorio

`.specify/scripts/bash/common.sh` usa el primer `python3` del `PATH`. En este equipo es el de Homebrew, que **no tiene PyYAML**, y entonces la resolución de plantillas falla:

```
Error: PyYAML is required to resolve preset template composition
```

Instalar PyYAML en el python3 de Homebrew está bloqueado por PEP 668, y forzarlo con `--break-system-packages` puede romper la instalación de Homebrew. Por eso el repositorio incluye `tools/speckit/shim/python3`, que delega en un intérprete que sí tiene PyYAML.

**Invoca siempre los scripts de SpecKit con el shim antepuesto al `PATH`:**

```bash
PATH="$PWD/tools/speckit/shim:$PATH" .specify/scripts/bash/resolve-template.sh spec-template
```

Esto aplica a `resolve-template.sh`, `check-prerequisites.sh`, `create-new-feature.sh`, `setup-plan.sh` y `setup-tasks.sh`. Si un comando `speckit.*` falla al resolver una plantilla, esta es la primera causa a descartar.

No modifiques `.specify/scripts/` para evitar el shim: son copias generadas por SpecKit y una actualización las reescribiría.

### Constancia de procedencia de la constitución

**No modifiques `.specify/memory/.constitution-template.json`.**

Ese archivo pertenece al mecanismo `constitution-sync`, que el README del preset prohíbe adoptar en este proyecto. El CLI compara su campo `sha256` contra el sha del **contenido vivo** de `constitution.md`. Hoy no coinciden, y esa discrepancia es deliberada: hace que `_constitution_is_generated()` devuelva `False`, de modo que el CLI trata la constitución como redactada por una persona y **no la sobrescribe**.

Actualizar esa constancia invertiría la protección: el CLI pasaría a considerarla un archivo generado sin cambios y podría reemplazarla.

### Gestor de paquetes

**`bun` es el único gestor de paquetes y ejecutor de este proyecto.** Aplica a instalación de dependencias, scripts, pruebas, herramientas de línea de comandos y ejecución local.

| En lugar de | Usa |
|---|---|
| `npm install` | `bun install` |
| `npm run <script>` | `bun run <script>` |
| `npx <paquete>` | `bunx <paquete>` |
| `npm test` | `bun test` |

No introduzcas `npm`, `yarn` ni `pnpm`, y no generes ni versiones sus archivos de bloqueo. El bloqueo del proyecto es el de `bun`.

Esta es una decisión humana de Damián Acuña, reversible, adoptada el 21 de septiembre de 2026. No altera alcance, contenido, experiencia, seguridad, derechos ni posicionamiento del producto, por lo que se ajusta al artículo 2.3 del PRD. Debe quedar registrada en `plan.md` cuando se planifique, junto con su consecuencia sobre la reproducibilidad de dependencias exigida por el artículo 24.5 del PRD.

### Integración de agente

La integración activa de SpecKit es **Claude Code**. Los comandos `speckit.*` compuestos por el preset se invocan a través de ella.
