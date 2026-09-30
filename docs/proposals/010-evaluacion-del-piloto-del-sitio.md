# Propuesta 010 — Evaluación del piloto del sitio: el método disparado desde conversación

**Fecha:** 2026-09-29
**Estado:** propuesta para revisión y aprobación de Damián Acuña. **Nada aplicado.**
**Objeto:** qué mostró el segundo piloto sobre cómo se usa el método de verdad
**Fuentes observadas:** `docs/pilot/informe-del-metodo-2026-09-29.md` y `docs/pilot/registro-del-piloto.md` del repositorio `website-software-humano`, commit `c50bfe6`

---

# 1 · Qué es y qué no es este documento

El deber `DP-01` reparte el trabajo en tres, y este documento ocupa el del medio:

| | Quién | Dónde |
|---|---|---|
| **Observar** | la sesión del sitio | su bitácora e informe |
| **Evaluar** | esta sesión | este documento |
| **Decidir** | Damián Acuña | ninguna parte de este documento |

**Evaluar no es aplicar.** Nada de lo que sigue toca el núcleo, el anexo, el preset ni el paquete.

Distingo en todo el texto: **hecho observado** (del informe, con su evidencia), *inferencia mía* (marcada así), y **decisión requerida**.

---

# 2 · El hallazgo principal, y corrige lo que este repositorio creía

## 2.1 · El hecho

El método se ejecutó **íntegramente en modo de comandos sueltos**. `workflow run` no se usó nunca.

Y aun así los comandos corrieron:

| Comando | Veces | Cómo se disparó |
|---|---:|---|
| `analyze` | 10 | el agente lo eligió según lo que pedía cada turno |
| `converge` | 7 | igual |
| `speckit-conformidad-comprobar` | antes de cada implementación | gancho `before_implement`, casi siempre a mano |
| `constitution`, `specify`, `plan`, `tasks` | 1 cada uno | igual |
| `clarify` | **0** | — |

El informe lo dice así: *«el agente eligió el comando siguiente según lo que pedía cada turno».*

Y **seis de los siete casos** en que el método cambió una decisión salieron de `analyze` y `converge` — es decir, de comandos que nadie tecleó.

## 2.2 · Por qué funcionó, y esto es lo que no debe romperse

El preset 1.2.0 declaraba frontmatter propio en cada comando. El de `analyze` decía:

> `description: Analiza doctrina, cobertura y trazabilidad sin modificar los artefactos examinados.`

Una capa que declara frontmatter **reemplaza el del core**. Esa descripción no nombra un solo artefacto ni dice cuándo aplica, y el agente dejó de invocar los comandos.

El preset 2.0.0 no declara frontmatter: empieza en `{CORE_TEMPLATE}`. La descripción nativa sobrevive entera:

> `description: Perform a non-destructive cross-artifact consistency and quality analysis across spec.md, plan.md, and tasks.md after task generation.`

Nombra `spec.md`, `plan.md` y `tasks.md`, y dice **cuándo**: después de generar tareas. Lo mismo `converge`, cuya descripción nativa dice qué evalúa y qué produce.

*Inferencia mía:* un agente en conversación reconoce «revisar coherencia entre spec, plan y tasks después de generar tareas». No reconoce «analiza doctrina, cobertura y trazabilidad». **Lo que hizo invocable el método no fue agregar precisión doctrinal: fue dejar de tapar la descripción que ya nombraba artefactos y momentos.**

## 2.3 · Lo que este repositorio tenía mal

La decisión de componer sin frontmatter está registrada en `AGENTS.md` como una decisión **técnica**, justificada por preservar `handoffs`, descripción y `scripts`. El ensayo de instalación la comprueba como tal: cinco aserciones sobre frontmatter.

*Inferencia mía:* su efecto más importante es **de comportamiento**, no técnico, y no estaba registrado en ninguna parte. Es lo que hace que el método se dispare desde lenguaje natural, que es el único modo en que la autoridad de este proyecto trabaja.

El riesgo concreto: alguien podría redeclarar frontmatter en una versión futura para «mejorar las descripciones» —y las aserciones actuales sobre `handoffs` **seguirían pasando en cuatro de los ocho comandos**, porque `analyze`, `converge` e `implement` no traen `handoffs` en el core.

## 2.4 · Decisión requerida

**`D-010-1` — ¿Se registra el modo de comandos sueltos como el modo previsto, y no como el degradado?**

Hoy la instrucción 01 dice que el workflow es «el camino recomendado, no un requisito», con una tabla que le atribuye la garantía fuerte. El piloto mostró que el camino recomendado no se usa y que el otro funcionó.

Opciones:

- **`A`** · No cambiar nada. El texto queda diciendo que lo recomendado es lo que nadie hace.
- **`B`** · Reescribir esa tabla para describir los dos modos sin jerarquía, y decir qué garantiza cada uno de verdad. *Costo: versionar el paquete.*
- **`C`** · Además de `B`, agregar al ensayo de instalación una aserción que compruebe que **ningún** comando del preset declara frontmatter, y documentar por qué en el propio preset. *Costo: una aserción y un comentario.*

*Recomiendo `C`.* `B` sin `C` deja escrita la razón y sin proteger el mecanismo.

---

# 3 · Los dos huecos, y ninguno se cierra con más ceremonia

## 3.1 · El hecho

**`clarify` no consta en ningún artefacto.** El informe: *«`spec.md` no tiene sección de aclaraciones y ningún commit lo menciona. Las decisiones materiales se tomaron en la conversación y se registraron en `AGENTS.md` y en el PRD.»*

**Las fases 29, 31 y 32 y las tareas `T205`, `T218` y `T219` no pasaron por `analyze` ni por un `converge` posterior.** Tienen tareas, pruebas y commits. Y `plan.md` y `spec.md` no reflejan la navegación estándar ni la página Acerca: esas decisiones viven en `AGENTS.md` y `tasks.md`.

## 3.2 · Qué tienen en común

*Inferencia mía:* no son el mismo fallo que «el agente omitió un paso». Son el mismo fallo que **una decisión tomada hablando y que ningún artefacto recogió.**

Y sobre `clarify` en particular: que no se disparara **es correcto**. `clarify` existe para resolver ambigüedades materiales cuando la autoridad no está disponible. Si la autoridad está dictando en la conversación, aclarar **es** la conversación. Forzar el comando sería ceremonia.

Lo que falló no fue la ausencia del comando. Fue que la decisión aclarada quedó en `AGENTS.md` y en el PRD, y **`spec.md` nunca la recibió**. La regla 10 pide trazabilidad bidireccional; hoy no la hay para esas decisiones.

## 3.3 · Decisión requerida

**`D-010-2` — ¿Qué recoge una decisión tomada en conversación?**

Opciones:

- **`A`** · Nada. Se acepta que las decisiones dictadas vivan en `AGENTS.md` y que `spec.md` quede atrás. *Costo: la trazabilidad bidireccional deja de ser cierta, y conviene entonces dejar de afirmarla.*
- **`B`** · La conformidad comprueba la **frescura**: si `AGENTS.md` o el fundamento son más recientes que `spec.md`, lo reporta y detiene. No obliga a invocar nada; avisa que algo se decidió y no llegó. *Costo: una comparación de fechas en la extensión; versionarla.*
- **`C`** · Un comando nuevo que propague la decisión. *Costo: alto, y se superpone con `D-010-3`.*

*Recomiendo `B`.* Es lo único que funciona sin pedirte que invoques nada: la comprobación ya corre antes de cada implementación, y ahí es donde el hueco duele.

---

# 4 · La brecha del fundamento que cambia

## 4.1 · El hecho

El PRD pasó de v1.0 a v1.6. `spec.md` y `plan.md` se reescribieron **a mano seis veces**. El informe lo registra como `B4`: *«no hay un comando para propagar un cambio del fundamento»*, y supone que fue el costo recurrente más alto del método —suposición suya, no medida.

El desajuste `I2`–`I6` que encontró `analyze` tras la aprobación lingüística es consecuencia directa: referencias viejas sobrevivieron en `T099`, `T101`, `T102` y en la nota de dependencias.

## 4.2 · Qué observo

*Inferencia mía:* el flujo de SpecKit supone un fundamento estable. `specify` lee la fuente una vez y produce `spec.md`; de ahí en adelante todo deriva de `spec.md`. **No hay camino de vuelta cuando la fuente cambia**, y este piloto la cambió seis veces.

Esto no es un defecto de la adaptación: es del ciclo nativo, y la adaptación no lo cubrió. El anexo exige que toda disposición trace al núcleo o a una necesidad técnica inevitable de SpecKit. *Esta es una necesidad técnica inevitable de SpecKit*, así que hay lugar para atenderla.

## 4.3 · Decisión requerida

**`D-010-3` — ¿El método atiende el cambio del fundamento?**

Opciones:

- **`A`** · No. Se documenta como límite conocido en la instrucción 01, para que nadie lo descubra a la sexta vez. *Costo: un párrafo.*
- **`B`** · La conformidad detecta el desfase —es la misma comprobación de `D-010-2`— y nombra qué artefactos quedaron atrás. Reconciliar sigue siendo a mano. *Costo: compartido con `D-010-2`.*
- **`C`** · Un comando de la extensión que tome la diferencia entre dos versiones del fundamento y liste qué secciones de `spec.md`, `plan.md` y `tasks.md` la citan. No reescribe: señala. *Costo: comando nuevo, y hay que decidir cómo se comparan dos versiones del fundamento.*

*Recomiendo `A` + `B` ahora, y `C` solo si un segundo proyecto vuelve a pagarlo.* `C` es la única que ahorra trabajo de verdad, y es la única que no puedo justificar con un caso.

---

# 5 · Hasta dónde llega la verificación, y hasta dónde debe decir que no llega

## 5.1 · El hecho

Cuatro defectos los encontró Damián usando el sitio, no el método:

- «En esta página» dejaba fuera secciones;
- al cambiar de idioma se perdía la posición;
- «Enlace a esta sección» se enlazaba a sí mismo;
- la búsqueda no permitía navegar con el teclado.

La conformidad nunca detuvo nada en todo el piloto: siempre «9 con contenido · 0 sin declarar», y **ninguna excepción declarada**.

El informe supone —correctamente, en mi lectura— que estos defectos no podían aparecer en `analyze`, `converge` ni en la conformidad, porque *«los comandos revisan la coherencia entre artefactos y el código contra las tareas, no si la experiencia coincide con los principios».*

## 5.2 · Qué confirma

Esto confirma empíricamente lo que el análisis 006 estableció por construcción: de 300 enunciados comprobables, 210 compilan, 50 son editoriales y **40 quedan fuera**, y lo que resiste la compilación son **las cualidades de la experiencia**.

*Inferencia mía, y es incómoda:* **la parte distintiva del manifiesto es la parte que no compila.** Lo que hace único a este marco —que la carga transferida a la persona es una cantidad que se presupuesta y se verifica— es exactamente lo que ninguna comprobación automática alcanza. Los cuatro defectos son cuatro casos de carga transferida, y los cuatro los detectó una persona usando el producto.

Esto no invalida el método. Lo acota: **el método hace llegar la pregunta al momento de decidir; no la responde.** Cuatro de los siete casos en que cambió una decisión ocurrieron porque una pregunta apareció a tiempo.

Lo que sí es un problema es que hoy **nada en el paquete dice esto con claridad a quien lo instala.** La tabla de los dos modos de la instrucción 01 atribuye al workflow «las compuertas y la conformidad, que el agente no ejecuta y no puede saltarse» — lo que un lector razonable puede leer como que el workflow cubre la calidad del resultado. No la cubre, y este piloto lo muestra.

## 5.3 · Decisión requerida

**`D-010-4` — ¿El paquete declara dónde no llega?**

Opciones:

- **`A`** · No cambiar nada. *Costo: el paquete deja creer que cubre más de lo que cubre, y el próximo proyecto lo descubre igual que este.*
- **`B`** · Un apartado breve en `PARA_QUIEN_DECIDE.md` —que ya es el documento escrito para la persona— diciendo qué comprueba el método y qué sigue dependiendo de alguien mirando el producto, con estos cuatro defectos como ejemplo. *Costo: media página; versionar el paquete.*

*Recomiendo `B`.* Es coherente con `SH-DONE`: el método no rechaza lo incompleto, rechaza lo que falta sin que nadie lo sepa. **Un límite del método no declarado es exactamente eso.**

---

# 6 · Lo que esta evaluación no establece

- **`n=2`.** Dos pilotos, el mismo producto, la misma autoridad, el mismo agente. Nada de esto establece que ocurra en general. `A6` de la propuesta 003 ya fijó ese límite y me lo aplico.
- **No hay medición de costo ni de tiempo.** El informe lo dice: no se midieron. La afirmación de que reescribir `spec.md` y `plan.md` fue el costo más alto es suposición de la sesión del sitio, no un hecho.
- **No hay evidencia sobre el fin.** La ronda final con personas (`T103`–`T104`) no se ha hecho. Nada acá dice que el sitio sea mejor producto por haber usado el método.
- **No comprobé las afirmaciones del informe ejecutando los comandos.** Leí sus documentos y los artefactos que cita. La suposición del propio informe —que un `analyze` ahora encontraría los desajustes de las fases 29, 31 y 32— **no está verificada por nadie**.

---

# 7 · Las cuatro decisiones, juntas

| | Decisión | Recomiendo | Costo |
|---|---|---|---|
| `D-010-1` | Registrar el modo de comandos sueltos como el previsto, y proteger la composición sin frontmatter | `C` | una aserción, un comentario, versionar |
| `D-010-2` | Qué recoge una decisión tomada en conversación | `B` · la conformidad comprueba frescura | comparación de fechas en la extensión |
| `D-010-3` | Si el método atiende el cambio del fundamento | `A` + `B` ahora | un párrafo, compartido con `D-010-2` |
| `D-010-4` | Si el paquete declara dónde no llega | `B` | media página en `PARA_QUIEN_DECIDE.md` |

`D-010-2` y `D-010-3` comparten la misma comprobación: si el fundamento o `AGENTS.md` son más recientes que `spec.md`, algo se decidió y no llegó. Es una sola pieza de trabajo.

**Ninguna de las cuatro propone hacer obligatorio el workflow**, y esa ausencia es deliberada: la autoridad de este proyecto trabaja dictando en lenguaje natural, no ejecutando comandos. Un mecanismo que exige ser invocado no resuelve un problema de lo que no se invoca.

---

# 8 · Lo que este documento no hace

No modifica el núcleo, el anexo, el preset, la extensión, el workflow ni el paquete. No incrementa ninguna versión. No cierra ninguna de las cuatro decisiones.

Una propuesta no es una autorización.
