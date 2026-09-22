---
description: Analiza doctrina, cobertura y trazabilidad sin modificar los artefactos examinados.
strategy: wrap
---

## Directiva vinculante de Software Humano

Además de los controles nativos, el análisis debe comprobar:

- correspondencia entre la fuente autorizada y todos los elementos de `spec.md`;
- preservación de Job Stories existentes y ausencia de Job Stories impuestas;
- requisitos sin tareas y tareas sin fundamento;
- prioridades, MVP, exclusiones, releases o independencia no autorizados;
- dependencias e integración representadas sin pérdida de alcance;
- experiencia, estados, recuperación, accesibilidad, rendimiento y control aplicables;
- evidencia necesaria para cada criterio de aceptación;
- cumplimiento de las razones de detención `STOP01`–`STOP07`.

Una contradicción con la constitución es crítica. La corrección debe volver al artefacto que posee la decisión; `analyze` no modifica archivos ni reinterpreta el núcleo para acomodar los valores predeterminados de SpecKit.

## Alcance semántico de esta operación

`analyze` es la operación de **control**. El anexo le asigna las disposiciones siguientes, y comprobarlas es su trabajo, no un añadido.

**Verificación · `V01`–`V12`, una por una**

Recorre las doce dimensiones y declara para cada una si hay evidencia, si es parcial o si falta. No las agrupes ni las des por cubiertas en bloque.

`V01` cobertura · `V02` progreso · `V03` causalidad · `V04` comprensión · `V05` carga · `V06` profundidad · `V07` confianza · `V08` control · `V09` estados · `V10` accesibilidad · `V11` rendimiento · `V12` uso de IA.

**Controles transversales**

- **`SH-SCORE`** — presenta las dimensiones **sin evidencia**. Una dimensión crítica en 0 es un hallazgo, no una observación menor.
- **`SH-AP`** — comprueba si algún antipatrón aparece en el resultado, en especial «el plan selecciona alcance», «la descomposición parece exclusión» y «la respuesta fluida parece verdadera».
- **`SH-GOV`** — comprueba que cada decisión esté en manos de la autoridad que le corresponde y que ninguna aprobación humana haya sido simulada.
- **`SH-DONE`**, **`SH-STOP`**, **`STOP01`**–**`STOP07`** — comprueba si alguna razón de detención está activa sin haberse declarado.

**Cobertura y evidencia**

- **`F02`**, **`F08`**, **`A02`**, **`A07`** — correspondencia completa entre fundamento, especificación, plan, tareas y evidencia, en ambas direcciones.

**Comprobación de activación doctrinal**

Verifica que cada artefacto declare **qué disposiciones del núcleo activó y con qué consecuencia concreta**. Una disposición citada sin consecuencia, o una sección de activación ausente, es un hallazgo: significa que la doctrina no gobernó esa decisión aunque estuviera disponible.

**Límite.** `analyze` no modifica archivos. La corrección vuelve al artefacto que posee la decisión.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

El reporte final debe separar hechos, inferencias y decisiones humanas; identificar la fuente de cada hallazgo; y distinguir una brecha de producto, una brecha técnica y una falta de evidencia. No uses un puntaje o checklist como aceptación automática.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
