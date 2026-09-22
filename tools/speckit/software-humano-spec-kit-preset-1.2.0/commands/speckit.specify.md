---
description: Deriva una especificación verificable preservando fuente, autoridad, estructura y alcance completo.
strategy: wrap
---

## Directiva vinculante de Software Humano

Aplica el comando nativo con estas precisiones, que prevalecen cuando exista conflicto:

- Identifica la fuente autorizada, la autoridad de alcance y todos los elementos obligatorios antes de especificar.
- Acepta PRD, Job Stories, épicas, capacidades, requisitos, reglas u otra estructura coherente; no la conviertas automáticamente en historias de usuario.
- Conserva las Job Stories cuando existan y su circunstancia, motivación y resultado. No las inventes cuando no existan.
- No asignes prioridad, MVP, independencia ni estrategia incremental salvo que producto las haya definido o autorizado.
- No selecciones una parte del fundamento como si fuera el alcance completo.
- Los supuestos solo pueden ser menores, reversibles, explícitos y estar dentro de la autoridad del agente.
- Toda ambigüedad material sobre alcance, reglas, derechos, seguridad o experiencia permanece como `NEEDS CLARIFICATION` y se deriva a la autoridad correspondiente.
- Deja sin efecto cualquier límite numérico del comando nativo que obligue a ocultar marcadores materiales o a reemplazarlos por conjeturas. El límite de preguntas organiza una ronda; no reduce la obligación de resolverlas.
- Conserva el checklist nativo de calidad de requisitos. No crees otro checklist propio del manifiesto.
- Completa la matriz de cobertura de `spec.md` sin generar un informe adicional.

## Alcance semántico de esta operación · comprobaciones

| Disposición | Comprobación verificable | Dónde se responde |
|---|---|---|
| `SH-FUND` | Fuente, autoridad, razón, resultado, condiciones y evidencia están identificadas | Fuente y autoridad |
| `P01` | Cada requisito declara el progreso que habilita. Ninguna Job Story pierde circunstancia, motivación ni resultado | Estructura de producto preservada |
| `P02` | **Al menos un criterio de aceptación por recorrido mide esfuerzo, claridad o confianza**, no solo corrección de salida | Evidencia y criterios de éxito |
| `P05` | Toda convención propia que la persona deba aprender está declarada y justificada frente a la convención conocida que reemplaza | Contrato de experiencia |
| `P06` | Cada elemento visible y cada decisión solicitada traza a un elemento del fundamento | Cobertura del alcance |
| `P07` | Cada acción está clasificada reversible o irreversible, y cada irreversible declara su consecuencia | Reglas, estados y excepciones |
| `P10` | Ningún dato solicitado a la persona carece de uso declarado | Requisitos y entidades clave |
| `D01` | Todos los elementos obligatorios del fundamento están inventariados antes de proponer nada | Cobertura del alcance |
| `D02` | Toda ambigüedad material permanece como `NEEDS CLARIFICATION`, sin cerrar por supuesto | Decisiones materiales pendientes |
| `F01`, `F02` | La matriz de cobertura no tiene elementos sin destino | Cobertura del alcance |
| `F04` | Las Job Stories existentes conservan su forma; ninguna fue inventada | Estructura preservada |
| `F05`, `A04`, `CR05` | El contrato de experiencia declara ruta principal, lenguaje, decisiones, feedback, control, recuperación y continuidad | Contrato de experiencia |
| `A01`, `A02` | El mapa del fundamento y el de cobertura viven en `spec.md`, sin documentos separados que dupliquen | `spec.md` |
| `A03` | Cada Job Story aplicable registra conducta actual, ansiedad, evidencia y supuestos | Estructura preservada |
| `CR03` | Ningún elemento obligatorio quedó sin destino ni postergado sin decisión | Cobertura del alcance |
| `CR04` | Cuando la decisión pertenece a producto, están las tres opciones: recomendada, más simple y no construir | Decisiones pendientes |

**Límite numérico anulado.** Cualquier tope del comando nativo que obligue a ocultar marcadores materiales o reemplazarlos por conjeturas queda sin efecto. Un límite organiza una ronda; no reduce la obligación de resolverlas.

### Lo que estas comprobaciones NO cubren

`P02` compila solo hasta la existencia del criterio: se puede verificar que **exista** un criterio sobre esfuerzo o confianza, no que la experiencia resultante **sea** clara o confiable. Esa parte exige pruebas moderadas con personas, y la especificación debe declararla como tal en su plan de validación.

### Entrega

`O01`–`O05` y `O09`, según el formato del núcleo.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

Antes de informar término, confirma en lenguaje natural: fuente y autoridad utilizadas; alcance cubierto; ambigüedades pendientes; supuestos reversibles; y decisiones humanas requeridas. Una especificación con decisiones materiales abiertas puede quedar preparada para `clarify`, pero no puede presentarse como inequívoca.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
