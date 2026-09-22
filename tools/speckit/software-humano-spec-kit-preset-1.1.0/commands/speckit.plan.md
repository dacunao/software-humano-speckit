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

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

Antes de cerrar, informa cobertura planificada, dependencias, bloqueantes, auxiliares creados o descartados con su razón, riesgos y decisiones humanas pendientes. No presentes la secuencia técnica como una estrategia de producto no autorizada.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
