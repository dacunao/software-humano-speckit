# Propuesta 004 — Brecha de conformidad del preset con el anexo v1.2

**Fecha:** 2026-09-22
**Estado:** propuesta para decisión de Damián Acuña. **Nada aplicado.**
**Objeto:** preset `software-humano` v1.0.2, sus ocho comandos compuestos
**Origen:** pregunta de la autoridad de producto sobre cómo lograr que el manifiesto gobierne efectivamente el proyecto, y el informe de retroalimentación del piloto del 2026-09-22

## Resumen en una frase

**El anexo v1.2 diseñó el mecanismo que se necesita, exige al preset incorporarlo, y el preset no lo incorporó.**

No es una mejora marginal ni un replanteamiento del diseño. Es un **incumplimiento de conformidad** del preset contra su propio documento rector.

---

# 1 · Lo que el anexo exige

## 1.1 · El mecanismo ya está diseñado

El anexo define un modelo de lectura en tres niveles. El segundo es exactamente lo que falta:

> **Nivel de operación.** Cada comando **enfoca los identificadores indicados en el mapa siguiente** y los pasajes del producto relacionados con su tarea.

Y trae el mapa, que asigna a cada comando qué principios, directivas, pasos de flujo, artefactos, cláusulas del contrato y controles debe activar.

## 1.2 · Y exige al preset materializarlo

Línea 516 del anexo, textual:

> El futuro paquete técnico debe limitarse a convertir este anexo en archivos instalables… **El preset deberá incorporar las referencias por operación**, el contrato distribuido, el formato de salida y la activación de controles descritos aquí.

Criterio de conformidad 14:

> Cada comando **activa como mínimo el alcance semántico definido para su operación** y escala a la lectura completa cuando corresponde.

Criterio 15:

> El contrato `CR01`–`CR08`, la entrega `O01`–`O09` y los controles transversales **se aplican en las operaciones indicadas**.

---

# 2 · Lo que el preset hace

## 2.1 · Identificadores citados, medido

De aproximadamente **cien asignaciones** que el anexo reparte entre los ocho comandos, el preset cita **tres**.

| Comando | Identificadores que cita |
|---|---|
| `constitution` | ninguno |
| `specify` | ninguno |
| `clarify` | ninguno |
| `plan` | ninguno |
| `tasks` | ninguno |
| `analyze` | `STOP01`, `STOP07` |
| `implement` | **ninguno** |
| `converge` | `SH-DONE` |

## 2.2 · Cobertura por familia del núcleo

Citar no es lo único que importa: una regla puede cumplir una disposición sin nombrarla. Evalué cada asignación por **sustancia**, no por mención.

| Familia | Asignada a | Cubierta en sustancia | Ausente |
|---|---|---|---|
| **`P01`–`P10`** principios | `specify`, `plan`, `implement` | **`P01`** solo, vía la preservación de Job Stories | **Nueve de diez.** `P02`–`P10` no aparecen ni por nombre ni por exigencia en ningún comando |
| **`D01`–`D06`** directivas | `specify`, `clarify`, `plan`, `implement` | `D01`, `D02`, `D03` parcialmente | `D04` determinismo, `D05` verificación antes que aceptación, `D06` IA subordinada |
| **`F01`–`F08`** flujo | todos | `F01`, `F02`, `F03`, `F08` | `F04`, `F05` contrato de experiencia, `F06` reglas y riesgos, `F07` explorar y prototipar |
| **`A01`–`A08`** artefactos | `specify`, `plan`, `tasks`, `analyze`, `converge` | `A01`, `A02`, `A07`, `A08` | `A03`, `A04` contrato de experiencia, `A05` modelo de estados, **`A06` presupuesto de complejidad** |
| **`CR01`–`CR08`** contrato | todos | `CR02`, `CR03`, `CR04`, `CR07`, `CR08` | `CR01`, **`CR05` al diseñar**, `CR06` al usar IA |
| **`V01`–`V12`** verificación | `analyze`, `converge` | Aludidas sin nombrar en `analyze` | **Ninguna nombrada.** Ni en `analyze` ni en `converge` |
| **`SH-SCORE`** | `analyze`, `converge` | — | **Ausente en ambos** |
| **`SH-AP`** antipatrones | `plan`, `implement`, `analyze`, `converge` | — | **Ausente en los cuatro** |
| **`SH-POCKET`** | decisiones relevantes | — | **Ausente** |
| **`STOP01`–`STOP07`** | **todos** | `analyze` los nombra | Ausentes en los otros siete |

## 2.3 · El patrón, y es lo más importante de este documento

> **El preset es sólido donde el anexo le pide proteger el alcance y la autoridad. Es débil o inexistente donde le pide aplicar los principios de experiencia y los controles de verificación.**

Los ocho `wrap` suman unas sesenta reglas vinculantes. Casi todas hablan de fuente, autoridad, cobertura, trazabilidad, prioridad no autorizada y aceptación. **Ninguna dice qué debe comprender, decidir o sentir una persona**, que es lo que `P02`, `P04`–`P07` y `P10` exigen.

El caso más nítido es `implement`. El anexo le asigna `P03`, `P07`–`P10`, `D04`–`D06`, `A05`, `A07`, `CR06`, `CR07`. Sus ocho reglas vinculantes cubren `CR07` y parte de `A07`. **Los cinco principios y las tres directivas no aparecen.** Es el comando donde se toman las decisiones reales de producto, y es el que menos doctrina tiene delante.

El segundo es `analyze`. El anexo le asigna `V01`–`V12`, `SH-SCORE`, `SH-AP`, `SH-GOV` y `SH-DONE`: es la operación de **control**. Nombra `STOP01`–`STOP07` y **ninguno de los otros quince**.

---

# 3 · Por qué esto explica lo que el piloto observó

La correlación es exacta y no requiere interpretación.

| Lo que el piloto midió | Lo que predice esta brecha |
|---|---|
| `A1`–`A5`: el preset impidió prioridades inventadas, MVP no autorizado, cierre de decisiones sin autoridad y autoaprobación editorial | Son **todas** de alcance y autoridad, que es donde el preset sí cumple |
| `C13`: se propusieron dos direcciones visuales sin consultar la doctrina | `plan` e `implement` debían activar `P03`, `P04`, `P06`–`P10`. No los tienen |
| `C14`: se abrió a la persona una decisión que la doctrina ya cerraba | `clarify` debía activar `CR02` —identificar las fuentes autorizadas— antes de preguntar. No lo tiene |
| `C12`: una derivación argumentada se presentó como investigación | `implement` debía activar `D05` y `D06`. No los tiene |
| «Solo **dos** fallos en todo el piloto fueron evitados por una comprobación del método» | Las dos (`A5`, `A7`) son de autoridad y trazabilidad. Ninguna de experiencia, porque no hay comprobación de experiencia |
| `SH-SCORE` puntuó 12 de 22, con «Progreso del usuario» en 0 | `SH-SCORE` no está en ningún comando. Se aplicó porque la autoridad de producto lo pidió, no porque el método lo activara |
| `SH-POCKET` no se usó nunca; `SH-AP` una sola vez, informalmente; `A06` es el único artefacto sin casa | Los tres están asignados por el anexo y ausentes del preset |

**El piloto no descubrió una debilidad del manifiesto. Descubrió que una parte del manifiesto nunca llegó al agente.**

---

# 4 · Forma de la corrección

No la redacto. Describo qué tendría que lograr, porque redactarla sin que la autoridad vea antes el mapa sería repetir el error de `M1`.

## 4.1 · Un apartado por comando

Cada `wrap` gana una sección que nombra los identificadores que el anexo le asigna y traduce cada uno a **qué exige en ese momento**. No un listado: una obligación operativa.

El anexo ya advierte cómo hacerlo sin deformar la doctrina:

> Si una plantilla necesita una instrucción, debe **referenciar el identificador y describir el comportamiento exigido**; no copiar una versión abreviada que pueda divergir del núcleo.

## 4.2 · Mapeado a los tres momentos

| Momento | Operaciones | Lo que el anexo ya asigna y falta conectar |
|---|---|---|
| **Asegurar** — principios aplicados al diseño y la planificación | `specify`, `clarify`, `plan` | `P02`, `P05`–`P07`, `P10` y el contrato de experiencia `F05`/`A04`/`CR05` en `specify`; `CR02` antes de **abrir** una pregunta en `clarify`; `P03`, `P04`, `P06`–`P10`, `D04`, `F06`, `F07`, `A05`, `A06` en `plan` |
| **Construir** — principios aplicados al desarrollo | `tasks`, `implement` | `P03`, `P07`–`P10`, `D04`–`D06`, `A05`, `CR06` en `implement`. Y que consulte la **Comprobación de constitución** de `plan.md`, que el propio preset crea y nunca vuelve a mirar |
| **Controlar** — principios aplicados al control de calidad | `analyze`, `converge` | `V01`–`V12` nombradas una por una, `SH-SCORE`, `SH-AP`, `SH-GOV` en `analyze`; `V01`–`V12`, `SH-SCORE`, `SH-AP`, `STOP01`–`STOP07` en `converge` |

## 4.3 · La asimetría de `clarify`, que es barata y tiene efecto medido

El preset tiene seis reglas para **no cerrar** una decisión sin autoridad. **Ninguna para no abrir** una que las fuentes ya deciden.

`CR02` —«identifica las fuentes autorizadas… antes de programar»— está asignado a `clarify` por el anexo y no aparece. `P06` declara la atención un recurso del producto y exige justificar cada decisión solicitada.

Es una regla, y `C14` es su caso.

## 4.4 · El puente que el preset construye y no cruza

`plan-template.md` crea la sección **«Comprobación de constitución»**: una puerta con una tabla que traduce cada disposición del núcleo a una restricción concreta del proyecto.

Es el artefacto más valioso del preset para este problema. **El `wrap` de `implement` no lo menciona. Cero referencias a `plan.md`.**

---

# 5 · Lo que esta corrección no va a lograr

Conviene decirlo antes y no después.

**No garantiza que el agente consulte la doctrina.** Sube la probabilidad; no la asegura. El informe del piloto lo dice con precisión: «ningún método impide que alguien no lo lea».

**No automatiza el juicio, y no debe.** El propio núcleo lo desaconseja: `SH-SCORE` declara de sí mismo que «orienta la conversación; no reemplaza el juicio».

**No alcanza a lo que ocurre en conversación.** Los tres fallos de juicio del piloto ocurrieron en el chat, no en artefactos. Que `implement` cite `P07` no hace que `analyze` pueda auditar una propuesta de diseño hecha de viva voz.

Lo que sí cambia es **la naturaleza del fallo**. Hoy el instrumento no está puesto. Después, un fallo será haber ignorado algo que estaba delante. Son dos problemas distintos, y solo el primero es responsabilidad del preset.

---

# 6 · Alcance, costo y versión

**Qué toca:** los ocho archivos de `commands/` del preset. Posiblemente `plan-template.md`, si se decide que la Comprobación de constitución liste las disposiciones asignadas en lugar de dejarlas a criterio.

**Qué NO toca:**

- el **núcleo** — ninguna palabra de doctrina cambia;
- el **anexo** — ya dice todo esto desde la v1.2;
- el **core de SpecKit** — sigue siendo composición `wrap`;
- la **constitución materializada** — la proyección doctrinal no cambia, así que un proyecto instalado **no necesita rematerializarla**.

**Versión propuesta: preset 1.1.0**, no 1.0.3. No es una corrección: es una capacidad que faltaba. Paquete a 1.4.0.

**Consecuencia para el piloto**, verificada según `DP-02`: el sitio tendría una re-sincronización más. Su contenido publicable declara `version: 1.0.2`, que quedaría desfasado, y `FR-009` se aleja un paso más. Ninguna otra afirmación suya depende de esto.

## Alternativa más simple

Aplicar solo las dos reglas de mayor efecto medido: `CR02` en `clarify` —antes de abrir una pregunta— y la consulta a la Comprobación de constitución en `implement`.

Cubre `C13` y `C14`, que son dos de los tres fallos de juicio, y cuesta dos líneas en lugar de ocho apartados. **Deja el incumplimiento de conformidad sin resolver**: el preset seguiría sin cumplir los criterios 14 y 15 del anexo.

Es defendible como paso intermedio si la prioridad es el efecto inmediato sobre el piloto en curso. No lo es como solución.

## Opción de no construir

Sostenible solo si se acepta que el preset no cumple su documento rector y se documenta como excepción aprobada. No la recomiendo: el anexo es el documento que define qué es esta adaptación, y un preset que no lo cumple no es la adaptación que el paquete dice distribuir.

---

# 7 · Decisión humana requerida

1. **Si se corrige la conformidad completa** —ocho apartados, preset 1.1.0— o solo las dos reglas de mayor efecto.
2. **Cuándo**, dado que el método está congelado y el piloto va por la tarea 99 de 174. Corregirlo le genera una re-sincronización.
3. **Si la Comprobación de constitución de `plan-template.md`** debe listar las disposiciones asignadas por operación en lugar de dejarlas a criterio del agente.

Una cuarta, que no es del preset y por eso va aparte: el informe del piloto propone colocar `SH-SCORE` **también como entrada de decisión y no solo como verificación final**. Eso no es incumplimiento del anexo —el anexo lo asigna a `analyze` y `converge`, que son verificación— sino una propuesta de cambiar dónde se usa. Tocaría el anexo, y por tanto es doctrina. **No forma parte de esta propuesta.**

---

## Nota sobre cómo se produjo este documento

Se redactó **antes** de tocar el preset y para que la autoridad de producto vea el mapa completo antes de autorizar cualquier cambio, conforme al hallazgo `M1` de la propuesta 003: ningún commit antes de que quien decide haya visto de qué se trata.

Toda medición de este documento se hizo sobre los archivos del preset v1.0.2 instalado en este repositorio y sobre `docs/method/Anexo_Aplicacion_SpecKit_v1.2.md`, y es reproducible.
