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

## Alcance semántico de esta operación

El anexo asigna a `plan` las disposiciones siguientes. La **Comprobación de constitución** de `plan-template.md` es donde viven: cada una debe aparecer con su consecuencia concreta para este proyecto y su estado. Una fila sin consecuencia concreta no cuenta como cumplida.

**Complejidad y atención**

- **`P03`** — el sistema absorbe la complejidad del dominio. El plan justifica cada estructura y no traslada el modelo interno a la persona.
- **`P04`** — revelación progresiva con capacidad suficiente: ni un inicio que oculte lo necesario ni una superficie que lo muestre todo a la vez. **Sin callejones sin salida.**
- **`P06`** — cada elemento y cada decisión que el plan introduce compite con el propósito de la persona y debe justificarse.
- **`A06`** — **presupuesto de complejidad**: registra los conceptos nuevos, decisiones, pasos, excepciones y opciones visibles que la solución agrega. Es el artefacto del núcleo que con más frecuencia queda sin casa.

**Confianza, continuidad y control**

- **`P07`**–**`P09`** — estados, consecuencias, feedback, recuperación, respuesta, persistencia y retorno son decisiones del plan, no detalles de implementación.
- **`P10`** — permisos, revisión, reversibilidad y uso de datos bajo autoridad humana proporcional.
- **`A05`** — modelo de estados cuando estados y transiciones sean relevantes; en `spec.md` o en `data-model.md`, no en un documento por rutina.

**Decisión y riesgo**

- **`D03`** — simplicidad deliberada: la solución con menos conceptos, decisiones y memoria para la persona cuando ambas logran el resultado. Menos código no es la medida.
- **`D04`** — determinismo donde importa: separa la regla verificable del comportamiento generativo.
- **`F03`**, **`F06`**, **`F07`** — dependencias y orden; reglas, permisos y acciones irreversibles; exploración solo en la profundidad que el riesgo exige.
- **`CR03`**–**`CR06`** — cobertura completa; alternativa recomendada, más simple y no construir; lenguaje y jerarquía del usuario; límites explícitos al uso de IA.
- **`A07`**, **`A08`** — plan de aceptación y registro de decisiones con sus alternativas y tradeoffs.

**Controles de entrada** *(el anexo declara su mapa un mínimo y no una lista excluyente; estas activaciones lo exceden donde el riesgo lo justifica)*

- **`SH-SCORE` como entrada** — antes de comprometer una estrategia, una arquitectura o una dirección de diseño, puntúa la propuesta. Una dimensión crítica en **0** significa que no está lista para proponerse, y **«progreso del usuario» en 0 impide avanzar**. El puntaje orienta la conversación y no reemplaza el juicio: filtra lo que no debe presentarse, no decide lo que sí.
- **`SH-AP`** — comprueba los antipatrones antes de fijar el plan, en particular «más opciones se confunden con más valor», «el agente agrega por si acaso» y «el plan selecciona alcance».
- **`SH-POCKET`** — úsalo como recordatorio en una decisión relevante, nunca como formulario a completar.

**Entrega**

- **`O05`**, **`O09`** — alternativa elegida y razón de descarte; riesgos, pendientes y decisiones que requieren juicio humano.

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
