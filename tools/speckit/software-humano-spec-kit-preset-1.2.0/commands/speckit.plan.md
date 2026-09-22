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

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

Antes de cerrar, informa cobertura planificada, dependencias, bloqueantes, auxiliares creados o descartados con su razón, riesgos y decisiones humanas pendientes. No presentes la secuencia técnica como una estrategia de producto no autorizada.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
