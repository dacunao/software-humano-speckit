# Specification Quality Checklist: Sitio público del Manifiesto de Software Humano

**Purpose**: Validate specification completeness and quality before proceeding to planning
**Created**: 2026-09-21
**Feature**: [spec.md](../spec.md)

## Content Quality

- [x] No implementation details (languages, frameworks, APIs) — **con excepción declarada, ver Nota 1**
- [x] Focused on user value and business needs
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

## Requirement Completeness

- [ ] No [NEEDS CLARIFICATION] markers remain — **falla deliberadamente, ver Nota 2**
- [x] Requirements are testable and unambiguous
- [x] Success criteria are measurable
- [x] Success criteria are technology-agnostic (no implementation details)
- [x] All acceptance scenarios are defined
- [x] Edge cases are identified
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified

## Feature Readiness

- [x] All functional requirements have clear acceptance criteria
- [x] User scenarios cover primary flows
- [x] Feature meets measurable outcomes defined in Success Criteria
- [x] No implementation details leak into specification — **con excepción declarada, ver Nota 1**

## Notes

### Nota 1 — Decisiones técnicas presentes por mandato de la fuente

La especificación nombra TypeScript, Astro, daisyUI, Tailwind CSS, YAML, JSON-LD y Schema.org en la sección "Restricciones técnicas aprobadas" y en `FR-021`.

Esto no es una filtración de detalle de implementación. El PRD §24.6 las aprueba como **decisiones de producto** y establece que "solo podrán reemplazarse mediante una decisión explícita de producto y un registro técnico que demuestre una incompatibilidad material". `AGENTS.md` obliga a preservarlas. `AC-16` es un criterio de aceptación que nombra TypeScript explícitamente.

Omitirlas para satisfacer el criterio genérico habría reducido el alcance autorizado. Están confinadas a una sección identificable y no contaminan las Job Stories, los requisitos funcionales ni los criterios de éxito, que permanecen agnósticos.

### Nota 2 — Los marcadores NEEDS CLARIFICATION permanecen por doctrina

Permanecen once marcadores, `CL-01` a `CL-11`. Es el resultado correcto, no un defecto.

Diez provienen del PRD §29, que las declara "decisiones abiertas que requieren autoridad humana" y ordena resolverlas durante `clarify`. La undécima (`CL-11`, plataforma de alojamiento) surge de requisitos no funcionales que no pueden planificarse sin ella.

La directiva vinculante de Software Humano del comando `specify` establece: "Deja sin efecto cualquier límite numérico del comando nativo que obligue a ocultar marcadores materiales o a reemplazarlos por conjeturas." El límite nativo de tres marcadores organiza una ronda de preguntas; no reduce la obligación de resolverlas. Reducirlos a tres mediante conjeturas habría violado `STOP04` del núcleo y §29 del PRD, que advierte que la presencia de estas decisiones "no autoriza al agente a elegir valores predeterminados".

Ninguna de las once impide planificar la arquitectura conceptual. Todas bloquean la publicación y cualquier implementación que las vuelva irreversibles o públicas. `CL-06`, `CL-08` y `CL-09` afectan además contenido y aceptación.

**Este checklist no se considera aprobado.** La especificación está preparada para `/speckit-clarify`, no para `/speckit-plan` directo, y en ningún caso para `implement`.

### Nota 3 — Ausencia de prioridad, MVP y fases

La especificación no asigna prioridad, MVP, independencia, incrementalidad, fases ni releases. El PRD no las autoriza y su §15 declara que el orden de las Job Stories "no expresa prioridad ni autoriza a omitir historias". `AC-10` exige verificar precisamente esa ausencia.

### Nota 4 — Cobertura verificada

La matriz de cobertura de `spec.md` da destino a los 9 `JS`, los 21 `FR`, los 16 `AC`, los 10 `P`, los objetivos de §12, los no objetivos de §13 y las secciones §18, §19, §21.5, §24 y §25 del PRD. Ningún elemento obligatorio quedó sin destino. Los marcados "Pendiente de aclaración" están cubiertos en la especificación y esperan una decisión humana, no una reducción de alcance.
