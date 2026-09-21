---
description: Planifica la cobertura completa por dependencias y genera auxiliares solo cuando responden una pregunta necesaria.
strategy: wrap
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

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

Antes de cerrar, informa cobertura planificada, dependencias, bloqueantes, auxiliares creados o descartados con su razón, riesgos y decisiones humanas pendientes. No presentes la secuencia técnica como una estrategia de producto no autorizada.
