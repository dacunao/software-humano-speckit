---
description: Deriva tareas para todo el alcance según dependencias, integración y evidencia requerida.
strategy: wrap
---

## Directiva vinculante de Software Humano

Aplica el comando nativo con estas precisiones, que prevalecen cuando exista conflicto:

- Crea tareas para todos los elementos obligatorios de `spec.md` y `plan.md`.
- Agrupa por historia, Job Story, capacidad, componente o bloque técnico según la estructura real; no impongas historias de usuario.
- No asignes P1/P2/P3, MVP, independencia ni entrega incremental salvo autorización expresa de producto.
- Conserva dependencias legítimas y ordénalas para destrabar el resultado completo.
- Incluye pruebas técnicas o evidencia equivalente cuando sean necesarias por aceptación o riesgo, aunque no se hayan pedido con la palabra "prueba".
- Toda tarea debe trazar a una fuente, requisito, regla o decisión aprobada; toda obligación debe tener tareas de implementación y verificación.
- No agregues capacidades, abstracciones, configuraciones, controles ni documentos que no cambien una decisión necesaria.
- Una tarea o bloque completado representa avance; no redefine ni reduce el alcance comprometido.

## Alcance semántico de esta operación

El anexo asigna a `tasks` las disposiciones siguientes. **Declara en tu informe cuáles aplicaste y con qué consecuencia.**

- **`F02`**, **`A02`** — el inventario de cobertura es la obligación central: todo elemento obligatorio del fundamento y del plan tiene tareas de implementación **y** de verificación, o una excepción aprobada y visible.
- **`F03`** — ordena por dependencias, bloqueantes e integración. El orden es secuencia de ejecución, nunca selección de alcance.
- **`F08`**, **`CR07`** — cada tarea produce trabajo reconciliable con su fundamento; ninguna agrega capacidades, modos ni abstracciones sin autorización.
- **`CR03`** — si las restricciones impiden cubrir el alcance, hazlo visible y solicita decisión; no lo resuelvas postergando en silencio.
- **`A07`** — la evidencia que cada criterio de aceptación exige debe tener tarea propia, incluidas experiencia, estados, accesibilidad, rendimiento y control cuando apliquen.
- **`O02`**, **`O07`**–**`O09`** — informa inventario y cobertura, estados y casos extremos cubiertos, pruebas previstas, y lo que requiere juicio humano.

**Estado esperado de las verificaciones.** Cuando el orden que produzcas deje una comprobación imposible de satisfacer durante un intervalo —porque el bloque que la satisface viene después—, **declara ese intervalo**: qué comprobación queda en rojo, entre qué bloques y por qué razón conocida. Una compuerta roja sin declarar deja de señalar y oculta los fallos nuevos.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

Antes de informar término, verifica la matriz de cobertura, las tareas sin fundamento, los requisitos sin tareas, las dependencias, la integración y la evidencia. Sustituye el reporte nativo de "MVP sugerido" por una descripción neutral del orden técnico, salvo que el fundamento autorice un MVP.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
