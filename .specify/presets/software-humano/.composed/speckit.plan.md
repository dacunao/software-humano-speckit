---
description: Planifica la cobertura completa por dependencias y genera auxiliares
  solo cuando responden una pregunta necesaria.
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
  py: scripts/python/setup_plan.py --json
---


## Directiva vinculante de Software Humano

Aplica el comando nativo con estas precisiones, que prevalecen cuando exista conflicto:

- Planifica todo el alcance de `spec.md`; una fase, bloque o ejecución parcial no autoriza a seleccionar alcance.
- Ordena por dependencias, bloqueantes, integración y riesgo. Usa prioridades o releases solo cuando producto los haya definido.
- La comprobación de constitución debe citar disposiciones aplicables y explicar su consecuencia concreta.
- Compara enfoque recomendado, alternativa más simple y opción de no construir cuando exista una decisión real; no presentes la recomendación como aprobación.
- Genera `research.md`, `data-model.md`, `contracts/` o `quickstart.md` únicamente cuando el documento responda una pregunta necesaria identificada en `plan.md`.
- Deja sin efecto cualquier instrucción nativa que obligue a producir todos los documentos auxiliares por rutina.
- No resuelvas una decisión material de producto mediante investigación técnica ni la traslades silenciosamente a una tarea.
- Define evidencia proporcional a criterios de aceptación y riesgo, incluidas experiencia, estados, accesibilidad, rendimiento y control cuando correspondan.

## Alcance semántico de esta operación · comprobaciones

El anexo asigna a `plan` las disposiciones siguientes. **Cada una está expresada como una comprobación que se responde sí o no mirando el artefacto.** Su lugar es la Comprobación de constitución de `plan-template.md`: una fila por disposición, con su consecuencia concreta para este proyecto.

Una fila cuya consecuencia repite el enunciado —«se respetará `P07`»— no cuenta como cumplida.

| Disposición | Comprobación verificable | Dónde se responde |
|---|---|---|
| `P03` | Ningún nombre de entidad, tabla, estado interno o código de error del esquema aparece en texto visible para la persona | Lista de términos del esquema contrastada con las cadenas de interfaz |
| `P04` | Cada superficie declara qué muestra en su estado inicial y qué revela a demanda. **Ninguna ruta termina sin una acción siguiente disponible** | Inventario de superficies y de rutas terminales |
| `P06` | Cada elemento visible y cada decisión solicitada traza a un requisito o Job Story. Un elemento sin traza se elimina | Matriz de cobertura |
| `P07` | Toda acción irreversible declara su consecuencia antes de ejecutarse. Toda acción reversible declara cómo se revierte | Inventario de acciones clasificadas reversible / irreversible |
| `P08` | Cada componente y cada ruta especifica **seis estados**: vacío, carga, error, éxito, interrupción y retorno | Modelo de estados |
| `P09` | Cada interacción crítica declara su presupuesto de respuesta. Todo trabajo en curso declara su punto de persistencia | Contexto técnico y modelo de estados |
| `P10` | Ningún campo capturado carece de uso declarado. Toda acción de alto impacto exige autorización registrada | Modelo de datos y de acciones |
| `D03` | Existe la comparación entre enfoque recomendado, alternativa más simple y opción de no construir, con su razón de descarte | Estrategia técnica |
| `D04` | Cada regla que afecta permisos, cálculos, límites o transiciones de estado se implementa como lógica verificable con prueba, no como salida generativa | Inventario de reglas críticas |
| `F03` | Cada bloque declara de qué depende, qué desbloquea y su criterio para avanzar | Tabla de dependencias |
| `F06` | Cada regla determinista, permiso y acción irreversible está identificada y separada del comportamiento generativo | Inventario de reglas críticas |
| `F07` | Cada alternativa explorada registra su razón de elección o descarte | Registro de decisiones |
| `A05` | Existe el inventario de estados y transiciones válidas | `spec.md` o `data-model.md`, solo si hay estados relevantes |
| `A06` | La tabla de presupuesto de complejidad registra conceptos nuevos, decisiones solicitadas, pasos, excepciones expuestas y opciones visibles. **Ninguna celda vacía** | Presupuesto de complejidad |
| `A07` | Cada criterio de aceptación tiene al menos una tarea de verificación con evidencia nombrada | Plan de aceptación |
| `A08` | Cada decisión registra alternativas, tradeoffs y evidencia pendiente | Registro de decisiones |
| `CR03` | Todo elemento obligatorio de `spec.md` tiene destino en un bloque | Cobertura y trazabilidad |
| `CR04` | Ninguna recomendación se presenta como decisión tomada | Estrategia técnica |
| `CR06` | Cada uso de IA declara sus límites, su revisión y su reversibilidad | Estrategia técnica |

### Puntuación de entrada · `SH-SCORE`

Antes de comprometer una estrategia, una arquitectura o una dirección de diseño, puntúa la propuesta.

- **Una dimensión crítica en `0` significa que no está lista para proponerse.**
- **«Progreso del usuario» en `0` impide avanzar**, por la regla del propio núcleo.
- Un `1` que se repite por la misma razón —«argumentado y no observado»— indica que la propuesta descansa en razonamiento y no en evidencia.

El puntaje orienta la conversación y no reemplaza el juicio: filtra lo que no debe presentarse, no decide lo que sí.

### `SH-AP` · antipatrones a comprobar antes de fijar el plan

«Más opciones se confunden con más valor» · «el agente agrega por si acaso» · «el plan selecciona alcance» · «la descomposición parece exclusión».

### Lo que estas comprobaciones NO cubren

`P04` y `P05` compilan solo en parte. Se puede verificar que la declaración de profundidad progresiva exista y que ninguna ruta sea un callejón sin salida; **no se puede verificar que la cantidad de profundidad sea la correcta**, ni que un elemento se comprenda sin leyenda. Eso exige una persona.

Cuando una decisión dependa de esa parte no verificable, **decláralo en el plan y asígnale una verificación humana**. No la des por cumplida porque la parte verificable pasó.

### Entrega

`O05` alternativa elegida y razón de descarte · `O09` riesgos, pendientes y decisiones que requieren juicio humano.

---


## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Pre-Execution Checks

**Check for extension hooks (before planning)**:
- Check if `.specify/extensions.yml` exists in the project root.
- If it exists, read it and look for entries under the `hooks.before_plan` key
- If the YAML cannot be parsed or is invalid, do not skip silently: tell the user that `.specify/extensions.yml` could not be read (include the parser error) and that no hooks were checked, including any mandatory (`optional: false`) hooks registered there, then continue normally
- Filter out hooks where `enabled` is explicitly `false`. Treat hooks without an `enabled` field as enabled by default.
- For each remaining hook, do **not** attempt to interpret or evaluate hook `condition` expressions:
  - If the hook has no `condition` field, or it is null/empty, treat the hook as executable
  - If the hook defines a non-empty `condition`, skip the hook and leave condition evaluation to the HookExecutor implementation
- For each executable hook, output the following based on its `optional` flag:
  - **Optional hook** (`optional: true`):
    ```
    ## Extension Hooks

    **Optional Pre-Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```
  - **Mandatory hook** (`optional: false`):
    ```
    ## Extension Hooks

    **Automatic Pre-Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    Wait for the result of the hook command before proceeding to the Outline.
    ```
    After emitting the block above you MUST actually invoke the hook and wait for it to finish before continuing. Run it the same way you would run the command yourself in this agent/session (the invocation may differ from the literal `{command}` id shown above, e.g. a skills-mode agent runs it as `/skill:speckit-...` or `$speckit-...`). Emitting the block alone does not run the hook.
- If no hooks are registered or `.specify/extensions.yml` does not exist, skip silently

## Outline

1. **Setup**: Run `{SCRIPT}` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, FEATURE_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Re-evaluate Constitution Check post-design

## Mandatory Post-Execution Hooks

**You MUST complete this section before reporting completion to the user.**

Check if `.specify/extensions.yml` exists in the project root.
- If it does not exist, or no hooks are registered under `hooks.after_plan`, skip to the Completion Report.
- If it exists, read it and look for entries under the `hooks.after_plan` key.
- If the YAML cannot be parsed or is invalid, do not skip silently: tell the user that `.specify/extensions.yml` could not be read (include the parser error) and that no hooks were checked, including any mandatory (`optional: false`) hooks registered there, then continue to the Completion Report.
- Filter out hooks where `enabled` is explicitly `false`. Treat hooks without an `enabled` field as enabled by default.
- For each remaining hook, do **not** attempt to interpret or evaluate hook `condition` expressions:
  - If the hook has no `condition` field, or it is null/empty, treat the hook as executable
  - If the hook defines a non-empty `condition`, skip the hook and leave condition evaluation to the HookExecutor implementation
- For each executable hook, output the following based on its `optional` flag:
  - **Mandatory hook** (`optional: false`) — **You MUST emit `EXECUTE_COMMAND:` for each mandatory hook**:
    ```
    ## Extension Hooks

    **Automatic Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}
    ```
    After emitting the block above you MUST actually invoke the hook and wait for it to finish before continuing. Run it the same way you would run the command yourself in this agent/session (the invocation may differ from the literal `{command}` id shown above, e.g. a skills-mode agent runs it as `/skill:speckit-...` or `$speckit-...`). Emitting the block alone does not run the hook.
  - **Optional hook** (`optional: true`):
    ```
    ## Extension Hooks

    **Optional Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```

## Completion Report

Command ends after Phase 1 design. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Define interface contracts** (if project has external interfaces) → `/contracts/`:
   - Identify what interfaces the project exposes to users or other systems
   - Document the contract format appropriate for the project type
   - Examples: public APIs for libraries, command schemas for CLI tools, endpoints for web services, grammars for parsers, UI contracts for applications
   - Skip if project is purely internal (build scripts, one-off tools, etc.)

3. **Create quickstart validation guide** → `quickstart.md`:
   - Document runnable validation scenarios that prove the feature works end-to-end
   - Include prerequisites, setup commands, test/run commands, and expected outcomes
   - Use links or references to contracts and data model details instead of duplicating them
   - Do not include full implementation code, model/service/controller bodies, migrations, or complete test suites
   - Keep this artifact as a validation/run guide; implementation details belong in `tasks.md` and the implementation phase

**Output**: data-model.md, /contracts/*, quickstart.md

## Key rules

- Use absolute paths for filesystem operations; use project-relative paths for references in documentation
- ERROR on gate failures or unresolved clarifications

## Done When

- [ ] Plan workflow executed and design artifacts generated
- [ ] Extension hooks dispatched or skipped according to the rules in Mandatory Post-Execution Hooks above
- [ ] Completion reported to user with branch, plan path, and generated artifacts


## Confirmación de aplicación Software Humano

Antes de cerrar, informa cobertura planificada, dependencias, bloqueantes, auxiliares creados o descartados con su razón, riesgos y decisiones humanas pendientes. No presentes la secuencia técnica como una estrategia de producto no autorizada.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
