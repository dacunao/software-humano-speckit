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

## Alcance semántico de esta operación · comprobaciones

| Disposición | Comprobación verificable |
|---|---|
| `F02`, `A02` | Todo elemento obligatorio del fundamento y del plan tiene **tarea de implementación y tarea de verificación**, o excepción aprobada y visible |
| `F03` | Cada tarea declara de qué depende. El orden es secuencia de ejecución, nunca selección de alcance |
| `F08`, `CR07` | Ninguna tarea agrega capacidades, modos, configuraciones ni abstracciones sin fundamento aprobado |
| `A07` | Cada criterio de aceptación tiene tarea de verificación con **evidencia nombrada**, incluidas experiencia, estados, accesibilidad, rendimiento y control cuando apliquen |
| `CR03` | Si las restricciones impiden cubrir el alcance, está declarado y solicitada la decisión; no postergado en silencio |
| `O02`, `O07`–`O09` | El informe cubre inventario, estados, pruebas previstas y lo que requiere juicio humano |

### Estado esperado de las verificaciones por intervalo

**Comprobación obligatoria.** Si el orden que produces deja una comprobación imposible de satisfacer durante un intervalo —porque el bloque que la satisface viene después—, **decláralo**: qué comprobación queda en rojo, entre qué bloques y por qué razón conocida.

Si ninguna queda en rojo, **decláralo también**. El silencio no distingue «no hay» de «no se miró».

Una compuerta roja sin declarar deja de señalar, y un fallo nuevo llega a una rama ya rota sin distinguirse del ruido.

### Prohibición explícita

No asignes `P1`/`P2`/`P3`, MVP, independencia ni entrega incremental salvo autorización expresa del fundamento.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

Antes de informar término, verifica la matriz de cobertura, las tareas sin fundamento, los requisitos sin tareas, las dependencias, la integración y la evidencia. Sustituye el reporte nativo de "MVP sugerido" por una descripción neutral del orden técnico, salvo que el fundamento autorice un MVP.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
