---
description: Reconcilia implementación y alcance aprobado sin introducir decisiones nuevas de producto.
strategy: wrap
---

## Directiva vinculante de Software Humano

Conserva el proceso nativo de convergencia y aplica estas reglas:

- Recorre desde la fuente autorizada hasta `spec.md`, `plan.md`, `tasks.md`, código y evidencia, y vuelve desde cada decisión implementada hasta su fundamento.
- Solo agrega tareas para cerrar brechas del alcance aprobado.
- Una capacidad nueva, un cambio de producto o una excepción sin aprobación se informa para decisión humana; no se incorpora como trabajo autorizado.
- Distingue brechas de comportamiento, experiencia, estados, accesibilidad, rendimiento, confianza, control y evidencia.
- La convergencia técnica no equivale a aceptación humana ni permite autoaprobar excepciones.
- Declara terminado únicamente cuando se cumple `SH-DONE`; de lo contrario informa con precisión el estado de avance.

## Alcance semántico de esta operación

El anexo asigna a `converge` las disposiciones siguientes. Es la operación que separa cierre técnico de aceptación humana.

- **`F08`**, **`A02`**, **`A07`** — recorre desde la fuente autorizada hasta la evidencia y vuelve desde cada decisión implementada hasta su fundamento.
- **`V01`**–**`V12`** — reconcilia las doce dimensiones contra el resultado real, no contra lo planificado. Declara cuáles tienen evidencia, cuáles la tienen parcial y cuáles no la tienen.
- **`SH-SCORE`** — puedes presentar una valoración provisional respaldada por evidencia. **No fija el umbral del proyecto ni convierte un puntaje en aceptación.**
- **`SH-AP`** — comprueba si algún antipatrón sobrevivió al resultado.
- **`SH-DONE`** — declara terminado únicamente cuando todo elemento obligatorio tiene implementación y evidencia, o excepción aprobada; las personas alcanzan los resultados previstos; y la calidad de la experiencia fue verificada con rigor proporcional al riesgo.
- **`STOP01`**–**`STOP07`** — comprueba si alguna razón de detención quedó activa.
- **`CR08`** — reconcilia contra la definición completa y entrega evidencia, pendientes y excepciones aprobadas.
- **`O01`**–**`O09`** — los nueve elementos, en la medida necesaria para explicar cobertura, evidencia, brechas, excepciones y juicio humano pendiente.

**Solo puedes agregar tareas para cerrar brechas del alcance aprobado.** Una capacidad nueva o un cambio de producto se informa para decisión humana; no se incorpora como trabajo autorizado.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

El resultado debe incluir cobertura reconciliada, evidencia, brechas, tareas agregadas, cambios no autorizados detectados, excepciones aprobadas y decisiones humanas pendientes. Si la única evidencia disponible demuestra funcionamiento técnico, informa que la aceptación de producto sigue abierta.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
