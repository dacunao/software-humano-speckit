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

- [x] No [NEEDS CLARIFICATION] markers remain — **resueltos en tres rondas, ver Nota 2**
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

### Nota 2 — Los marcadores NEEDS CLARIFICATION se resolvieron por decisión humana

Tras tres rondas de `clarify` el 2026-09-21 **no queda ningún marcador**. `CL-01`–`CL-11` fueron resueltas por la autoridad de producto, y `CL-12` —licencia del código fuente del sitio, ausente del PRD y de la lista original— fue detectada durante `clarify` y resuelta en la misma sesión. Las doce quedaron registradas con su consecuencia en la sección `Clarifications` de `spec.md`.

Que ahora pase no invalida por qué antes fallaba. Las once nacieron así deliberadamente: diez del PRD §29, que las declara "decisiones abiertas que requieren autoridad humana" y ordena resolverlas durante `clarify`, y `CL-11` (plataforma de alojamiento) de requisitos no funcionales que no podían planificarse sin ella. **Ninguna se cerró con un valor predeterminado, una inferencia o una recomendación del agente**, conforme a PRD §29 y a `STOP04` del núcleo. Cada una conserva la fecha, la autoridad que la tomó y su consecuencia sobre requisitos, evidencia y plan.

La directiva vinculante de Software Humano del comando `specify` establece: "Deja sin efecto cualquier límite numérico del comando nativo que obligue a ocultar marcadores materiales o a reemplazarlos por conjeturas." El límite nativo de tres marcadores organiza una ronda de preguntas; no reduce la obligación de resolverlas. Reducirlos a tres mediante conjeturas habría violado `STOP04` del núcleo y §29 del PRD, que advierte que la presencia de estas decisiones "no autoriza al agente a elegir valores predeterminados".

Dos consecuencias quedan condicionadas a hechos futuros y no a decisiones pendientes: el mapeo `SoftwareSourceCode` de PRD §25.2 solo se emite cuando exista publicación real y URL verificable, y los campos `download_url` y `sha256` del preset solo existirán cuando haya un *release*. El esquema los admite nulos mientras el estado sea `no-publicado` y detiene el build si el estado pasa a `publicado` sin ellos.

**Este checklist se considera aprobado para pasar a `/speckit-plan`**, con dieciséis de dieciséis ítems satisfechos. La especificación cubre todo el alcance del PRD y no conserva decisiones materiales abiertas.

Aprobado para planificar **no significa aprobado para implementar ni aceptado como producto**. `/speckit-implement` requiere autorización humana explícita y posterior. La aceptación de la versión 1.0 exige además la evidencia de PRD §26.4 y §32, que ningún checklist de especificación puede sustituir: revisión de contenido contra el núcleo, pruebas moderadas de comprensión, revisión por teclado y lector de pantalla, auditoría de rendimiento, revisión lingüística humana aprobada en los tres idiomas y revisión humana del recorrido completo.

### Nota 3 — Ausencia de prioridad, MVP y fases

La especificación no asigna prioridad, MVP, independencia, incrementalidad, fases ni releases. El PRD no las autoriza y su §15 declara que el orden de las Job Stories "no expresa prioridad ni autoriza a omitir historias". `AC-10` exige verificar precisamente esa ausencia.

### Nota 4 — Cobertura verificada

La matriz de cobertura de `spec.md` da destino a los 9 `JS`, los 21 `FR`, los 16 `AC`, los 10 `P`, los objetivos de §12, los no objetivos de §13 y las secciones §18, §19, §21.5, §24 y §25 del PRD. Tras las rondas 1 y 2, **ninguna fila de la matriz permanece en "Pendiente de aclaración"**. Las trece que lo estaban —`JS-07`, `JS-09`, `FR-010`, `FR-012`, `FR-018`, `AC-09`, `AC-12`, `AC-13`, PRD §19.4, §24.2, §24.3, §25.2 y §27— quedaron cubiertas por decisiones registradas. Ningún elemento obligatorio quedó sin destino, y ninguna decisión se cerró reduciendo alcance.
