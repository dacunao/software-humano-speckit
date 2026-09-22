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

## Alcance semántico de esta operación · comprobaciones

`analyze` es la operación de **control**. No modifica archivos: la corrección vuelve al artefacto que posee la decisión.

### Verificación · `V01`–`V12`, una por una

Declara para cada dimensión: **hay evidencia**, **es parcial** o **falta**. No las agrupes ni las des por cubiertas en bloque.

`V01` cobertura · `V02` progreso · `V03` causalidad · `V04` comprensión · `V05` carga · `V06` profundidad · `V07` confianza · `V08` control · `V09` estados · `V10` accesibilidad · `V11` rendimiento · `V12` uso de IA

### Comprobación de activación doctrinal

| # | Comprobación verificable |
|---|---|
| 1 | La Comprobación de constitución de `plan.md` **existe y tiene filas** |
| 2 | Sus filas citan las disposiciones que el anexo asigna a `plan`, o declaran cuál no aplica y por qué |
| 3 | **Ninguna celda de consecuencia está vacía ni repite el enunciado.** «Se respetará `P07`» no es una consecuencia; «toda acción irreversible declara su consecuencia antes de ejecutarse» sí lo es |
| 4 | Cada artefacto declara qué disposiciones activó y **con qué consecuencia concreta** |
| 5 | `tasks.md` declara el estado esperado de las verificaciones por intervalo, o afirma que ninguna queda en rojo |
| 6 | Existe la puntuación `SH-SCORE` de entrada y ninguna dimensión crítica está en `0` sin bloqueo declarado |

Una disposición citada sin consecuencia, o una sección de activación ausente, **es un hallazgo**: significa que la doctrina no gobernó esa decisión aunque estuviera disponible.

### Cobertura y controles

| Disposición | Comprobación verificable |
|---|---|
| `F02`, `F08`, `A02`, `A07` | Correspondencia completa entre fundamento, especificación, plan, tareas y evidencia, **en ambas direcciones** |
| `SH-SCORE` | Presenta las dimensiones **sin evidencia**. Una dimensión crítica en `0` es un hallazgo, no una observación menor |
| `SH-AP` | Comprueba si algún antipatrón aparece en el resultado, en especial «el plan selecciona alcance», «la descomposición parece exclusión» y «la respuesta fluida parece verdadera» |
| `SH-GOV` | Cada decisión está en manos de la autoridad que le corresponde; ninguna aprobación humana fue simulada |
| `SH-STOP`, `STOP01`–`STOP07` | Ninguna razón de detención está activa sin haberse declarado |

### El límite de esta operación

`analyze` **lee artefactos**. No alcanza a lo que ocurrió en conversación: una propuesta hecha en el chat, una pregunta formulada fuera de un comando o un informe presentado de viva voz no pasan por aquí. Declara esa frontera en tu informe en lugar de dar por verificado lo que no pudiste mirar.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

El reporte final debe separar hechos, inferencias y decisiones humanas; identificar la fuente de cada hallazgo; y distinguir una brecha de producto, una brecha técnica y una falta de evidencia. No uses un puntaje o checklist como aceptación automática.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
