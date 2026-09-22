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

## Alcance semántico de esta operación

El anexo asigna a `specify` las disposiciones siguientes. **Actívalas: nómbralas donde cambien una decisión y declara en tu informe cuáles aplicaste y con qué consecuencia concreta.** Una disposición citada sin consecuencia no cuenta como aplicada.

**Fundamento y alcance**

- **`SH-FUND`** — establece fuente, autoridad, razón, resultado, condiciones y evidencia antes de especificar. Si falta una definición capaz de cambiar materialmente la solución, expón el vacío; no lo completes por inferencia.
- **`D01`** — comprende la definición completa antes de proponer componentes.
- **`F01`**, **`F02`** — mapea fielmente el fundamento e inventaría todos sus elementos obligatorios.
- **`A01`**, **`A02`** — el mapa del fundamento y el de cobertura viven dentro de `spec.md`; no generes documentos separados si la información ya está.
- **`CR01`**–**`CR03`** — la solución más simple que produzca el resultado definido; fuentes y alcance identificados; todo elemento obligatorio con destino.

**Progreso y experiencia** — esta familia es la que con más frecuencia se omite. No la trates como requisitos secundarios.

- **`P01`** — cada requisito se vincula al progreso que habilita. Conserva circunstancia, motivación y resultado cuando el fundamento use Job Stories; no las inventes cuando no las use.
- **`P02`** — esfuerzo, claridad, confianza y recorrido completo **son parte de la funcionalidad**. Deben aparecer en los criterios de aceptación, no en una sección aparte.
- **`P05`** — los escenarios comprueban lenguaje, orientación y ausencia de aprendizaje incidental.
- **`P06`** — cada elemento y cada decisión que la especificación exige a la persona debe tener relación trazable con el fundamento, o no existir.
- **`P07`** — estado, consecuencia, evidencia y recuperación forman parte de la especificación.
- **`P10`** — revisión, corrección, reversibilidad y uso de datos permanecen bajo autoridad humana proporcional.
- **`F04`**, **`F05`**, **`A03`**, **`A04`**, **`CR05`** — el **contrato de experiencia** es obligatorio cuando la experiencia afecta el resultado: ruta principal, lenguaje, decisiones, feedback, control, recuperación y continuidad. Su profundidad depende de ese efecto, no del tamaño del documento.

**Ambigüedad y detención**

- **`D02`**, **`SH-STOP`** — una ambigüedad material detiene; no se cierra con un supuesto.
- **`CR04`** — cuando la decisión aún pertenece a producto, presenta alternativa recomendada, alternativa más simple y opción de no construir, sin presentar la recomendación como aprobación.

**Entrega**

- **`O01`**–**`O05`**, **`O09`** — tu informe expresa fuentes y fundamento, inventario de cobertura, Job Stories cuando apliquen, evidencia y supuestos, alternativas comparadas, y lo que requiere juicio humano.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

Antes de informar término, confirma en lenguaje natural: fuente y autoridad utilizadas; alcance cubierto; ambigüedades pendientes; supuestos reversibles; y decisiones humanas requeridas. Una especificación con decisiones materiales abiertas puede quedar preparada para `clarify`, pero no puede presentarse como inequívoca.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
