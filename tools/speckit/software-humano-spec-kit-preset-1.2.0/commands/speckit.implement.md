---
description: Implementa dentro del alcance y la autoridad, manteniendo visibles cobertura, estados y evidencia.
strategy: wrap
---

## Directiva vinculante de Software Humano

Conserva la ejecución nativa y aplica estas reglas:

- Mantén visible el inventario completo aunque trabajes por segmentos o en paralelo.
- No agregues funcionalidades, modos, configuraciones o abstracciones sin fundamento aprobado.
- Respeta dependencias, reglas deterministas, permisos, estados y recuperación descritos.
- Produce la evidencia requerida por cada tarea y criterio; una prueba verde no sustituye el resultado humano.
- El checklist de requisitos y los checklists personalizados controlan calidad de requisitos, no completitud de implementación.
- Una ejecución parcial se informa como avance parcial y nunca como reducción del alcance o aceptación final.
- Detente ante contradicción material, pérdida de cobertura, autoridad insuficiente o una acción sensible sin autorización y recuperación.
- El agente no puede otorgarse revisión humana, excepción aprobada ni aceptación de producto.

## Alcance semántico de esta operación · comprobaciones

**Esta es la operación donde se toman las decisiones reales de producto.**

### Antes de decidir

1. **Lee la Comprobación de constitución de `plan.md`.** Esa tabla ya tradujo la doctrina a comprobaciones concretas de este proyecto. **Una decisión que esa tabla ya adjudica no se reabre ni se traslada a la persona como pendiente.**
2. **Antes de abrir una decisión a la persona, nombra la fuente que consultaste** para confirmar que no está ya resuelta. Sin fuente nombrada, no formules la pregunta (`CR02`, `P06`).
3. **Antes de proponer una solución, puntúala con `SH-SCORE`.** Una dimensión crítica en `0` significa que no está lista para presentarse. Sirve además para lo que a un agente le cuesta solo: **separar «lo razoné» de «lo observé»**. Un argumento sólido no es evidencia.

### Comprobaciones durante la ejecución

| Disposición | Comprobación verificable |
|---|---|
| `P03` | Ningún nombre de entidad, tabla, estado interno ni código de error del esquema aparece en texto visible para la persona |
| `P07` | Toda acción irreversible declara su consecuencia **antes** de ejecutarse. Toda acción reversible tiene su camino de reversión implementado |
| `P08` | Cada componente entregado implementa los **seis estados**: vacío, carga, error, éxito, interrupción y retorno |
| `P09` | Cada interacción crítica cumple su presupuesto de respuesta o muestra progreso. Todo trabajo en curso persiste en el punto declarado |
| `P10` | Ningún campo se captura sin uso declarado. Ninguna acción de alto impacto se ejecuta sin autorización registrada |
| `D04` | Cada regla crítica —permisos, cálculos, límites, transiciones— tiene prueba automatizada. Ninguna depende de salida generativa |
| `D05` | Ningún entregable se declara terminado sin evidencia enlazada por cada criterio de aceptación |
| `D06` | Toda salida generativa del producto declara su incertidumbre |
| `A05` | Todo estado que aparezca y no esté en el inventario **se declara antes de usarse**, no se resuelve en silencio |
| `A07` | Cada criterio de aceptación tiene su evidencia producida o su ausencia declarada |
| `CR06` | Ninguna acción sensible se autoejecuta; revisión y reversibilidad conservadas |
| `CR07` | Ningún archivo agrega capacidades, modos, configuraciones ni abstracciones sin fundamento aprobado |

### `SH-AP` · antipatrones a vigilar

«El agente agrega por si acaso» · «el happy path define el producto» · «la estética maquilla la fricción» · «la respuesta fluida parece verdadera».

### No edites el contenido para que pase una validación

La regla que prohíbe modificar el paquete para satisfacer una comprobación **se aplica igual a lo que el proyecto produce**. Redactar esquivando lo que un validador marca mal produce una suite verde y un resultado peor. Si una validación está equivocada, corrígela y declara la corrección.

### Lo que estas comprobaciones NO cubren

Ninguna verifica si la persona **comprende, confía o progresa**. Verifican que el artefacto exista y que la regla esté implementada. La diferencia entre «los seis estados están implementados» y «la experiencia es buena» no la cierra ningún control automático: la cierran las pruebas moderadas con personas.

Cuando entregues, **declara qué quedó verificado por comprobación y qué espera verificación humana**. No presentes lo primero como si fuera lo segundo.

### Entrega

`O06` archivos y componentes tocados · `O07` estados cubiertos · `O08` pruebas y su resultado · `O09` riesgos, pendientes y decisiones que requieren juicio humano.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

El reporte final debe indicar qué se implementó, qué evidencia se obtuvo, qué cobertura permanece, qué supuestos y excepciones existen, qué riesgos continúan y qué requiere juicio humano. Solo usa la palabra "terminado" cuando todas las tareas aplicables estén reconciliadas con la definición completa y la definición de terminado del núcleo.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
