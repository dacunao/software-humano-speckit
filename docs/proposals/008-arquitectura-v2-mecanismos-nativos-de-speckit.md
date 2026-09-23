# Propuesta 008 — Arquitectura de la versión 2.0: los mecanismos nativos que no habíamos evaluado

**Fecha:** 2026-09-22
**Estado:** propuesta de arquitectura para decisión de Damián Acuña. **Nada aplicado.**
**Objeto:** con qué mecanismos de SpecKit debe construirse la versión 2.0 del método
**Origen:** principio general dictado por la autoridad — *«la experiencia adquirida en el piloto del sitio son inputs a tener en cuenta, no restricciones»*; y la instrucción de evaluar qué elementos más allá del preset son pertinentes, en tanto estén descritos en las guías de la propia SpecKit

---

# 1 · El hallazgo que obliga a rehacer, no a parchar

**El nivel mecánico existe en SpecKit. La propuesta 005 afirmó que no, y esa afirmación es falsa.**

Su tabla central decía:

| Nivel | Mecanismo | ¿Lo puede omitir el agente? |
|---|---|---|
| Persuasión | Núcleo, `AGENTS.md`, `wrap` | Sí, en silencio |
| Trazabilidad | Declaración de activación, `analyze` | Sí, pero deja rastro |
| **Mecánica** | — | **No existe dentro de SpecKit** |

Ese hallazgo se verificó sobre los hooks de `extensions.yml` y sobre `provides: script` del esquema de presets. **Ambas verificaciones eran correctas.** La conclusión que se extrajo de ellas no lo era: se generalizó desde dos mecanismos a todo SpecKit, sin mirar el tercero.

## 1.1 · Lo que dice el código, verificado sobre SpecKit 1.0.8

`specify_cli/workflows/steps/shell/__init__.py`:

> ```python
> class ShellStep(StepBase):
>     """Run a local shell command (non-agent).
>
>     Captures exit code and stdout/stderr.
>     """
> ```

Lo ejecuta `subprocess.run` desde el motor de workflows. **No lo ejecuta el agente, y el agente no puede omitirlo.**

`specify_cli/workflows/steps/gate/__init__.py`:

> ```python
> class GateStep(StepBase):
>     """Interactive review gate.
>
>     When running in an interactive terminal, prompts the user to choose
>     an option (e.g. approve / reject).  Falls back to ``PAUSED`` when
>     stdin is not a TTY (CI, piped input) so the run can be resumed
>     later with ``specify workflow resume``.
>     """
> ```

`specify_cli/workflows/_commands.py`:

> ```python
> def _run_outcome_exit_code(status_value: str) -> int:
>     """Exit code for a finished run/resume: non-zero on terminal failure.
>
>     ``failed`` and ``aborted`` map to 1 so scripts and orchestrators can
>     rely on the process exit code…
>     """
> ```

## 1.2 · Los tipos de paso disponibles

`command`, `shell`, `prompt`, `gate`, `if`, `init`, `switch`, `while`, `do-while`, `fan-out`, `fan-in`.

Tres importan de manera directa al núcleo:

| Paso | Qué hace | Qué disposición del núcleo vuelve ejecutable |
|---|---|---|
| `shell` | Ejecuta un comando local **fuera del agente** | La comprobación de conformidad que la propuesta 005 diseñó sin poder conectar |
| `gate` | Detiene y pide una elección humana; `on_reject: abort` termina el run | `SH-GOV`, `SH-STOP` y `STOP01`–`STOP07`: **detenciones que hoy nada puede imponer** |
| `while` / `do-while` | Repite mientras la condición sea cierta, con `max_iterations` | *«Conservar rondas nativas de hasta cinco preguntas y repetirlas hasta resolver toda ambigüedad material»* — anexo, línea 150 |

## 1.3 · Y esto es lo que sostiene la tesis de la disciplina

> *Un manifiesto sin método es declaración de intenciones. Un método sin mecanismos de cumplimiento es documentación. Y un método que exige disciplina heroica es un método incompleto: la disciplina debe ser el residuo, no el combustible.*

Las versiones 1.x pidieron disciplina heroica porque **el único capaz de hacer cumplir el método era el mismo que debía cumplirlo**. Un `gate` en un workflow invierte eso: el run lo inicia una persona o un build, y aborta sin consultar al agente.

---

# 2 · Por qué el anexo no lo había visto, y por qué eso no fue un error suyo

El anexo v1.2, líneas 95 a 97, evaluó los tres mecanismos y los pospuso. Sus razones, textuales:

> - «Las extensiones agregan capacidades, comandos, integraciones o fases nuevas. Como este anexo **no agrega capacidades ni fases**, una extensión no es el mecanismo **inicial** adecuado.»
> - «Los workflows automatizan secuencias y **pueden introducir condiciones, ciclos y aprobaciones**. El núcleo no exige una nueva secuencia automatizada; por ello, este anexo no define un workflow.»
> - «Los bundles distribuyen componentes existentes como una unidad versionada. Solo tendrían sentido al empaquetar **posteriormente** una combinación real de componentes.»

Tres observaciones honestas sobre este pasaje:

1. **No son prohibiciones. Son aplazamientos.** «Mecanismo inicial», «posteriormente», «no son necesarios para definir la adaptación». El anexo dejó la puerta abierta y fijó la condición para cruzarla: *«mientras no exista una necesidad técnica demostrada que el preset no pueda resolver»* (línea 107).
2. **La línea 96 nombró la capacidad exacta —«aprobaciones»— y la descartó con un argumento sobre otra cosa.** El núcleo, en efecto, no exige una secuencia automatizada nueva. Pero exige **detenciones**, y en la v1.x nada puede imponer una. El razonamiento confundió *no hace falta una fase nueva* con *no hace falta hacer cumplir nada*.
3. **La condición de la línea 107 está cumplida, y por dos vías independientes.** Ver §3.

---

# 3 · Lo que la guía oficial asigna a cada mecanismo

De la [guía de personalización](https://github.github.io/spec-kit/guides/customization.html) y las referencias de [presets](https://github.github.io/spec-kit/reference/presets.html), [extensiones](https://github.github.io/spec-kit/reference/extensions.html), [workflows](https://github.github.io/spec-kit/reference/workflows.html) y [bundles](https://github.github.io/spec-kit/reference/bundles.html):

| Mecanismo | Puede | **No** puede |
|---|---|---|
| **Preset** | «Change the format or terminology of specs, plans, or tasks» · **«Enforce organizational or regulatory standards in existing templates»** | **«Cannot add entirely new capabilities or integrate external services»** |
| **Extension** | «Add a new command, capability, or process» · lleva comandos, plantillas, **scripts** y hooks | «Does not change format or terminology of existing artifacts» |
| **Workflow** | «Automate a multi-step process» · condiciones, ciclos y aprobaciones | Modificar plantillas |
| **Bundle** | **«Provision a complete role-based setup in one operation»** · pinea extensiones, presets, workflows y pasos | Personalizar plantillas por sí mismo |

**La primera consecuencia es incómoda:** la mitad de lo que la v1.2 metió en el preset no le corresponde. Una comprobación de conformidad es *a new capability*, y la guía dice expresamente que un preset no puede llevarla.

**La segunda es la que reorienta el diseño:** la forma documentada de distribuir «un método» es un **bundle**. No un preset.

## 3.1 · Hay una implementación de referencia de «un proceso como extensión»

`core_pack/extensions/assess/`, publicada por `spec-kit-core`, agrega cinco comandos, vive en su propio directorio `.specify/assessments/<slug>/`, aplica una compuerta `go / needs-clarification / kill` y entrega el resultado a `speckit.specify`. Es el patrón exacto que la versión 2.0 necesita, escrito por los autores de SpecKit.

---

# 4 · La arquitectura propuesta

Cuatro capas, cada una en el mecanismo que la guía le asigna.

| Capa | Mecanismo | Qué lleva | Por qué ahí |
|---|---|---|---|
| **Doctrina en los artefactos** | `preset` | Plantillas y el `wrap` de los ocho comandos | *«Enforce standards in existing templates»* es su caso de uso textual |
| **Comprobación de conformidad** | `extension` | El script de conformidad, sus comandos y su configuración por proyecto | Es una capacidad nueva; el preset no puede llevarla |
| **Coerción** | `workflow` | `shell` (conformidad) · `gate` (autoridad humana) · `while` (clarify hasta cerrar) | Único lugar donde existe un paso que el agente no ejecuta |
| **Distribución** | `bundle` | Pinea las tres versiones; una sola instalación | *«Complete role-based setup in one operation»* |

## 4.1 · Qué haría el workflow, concretamente

Un borrador de secuencia, no una especificación:

1. `command: speckit.specify`
2. `while` con condición sobre marcadores sin resolver → `command: speckit.clarify` (tope de seguridad por `max_iterations`)
3. `command: speckit.plan`
4. **`shell`**: conformidad sobre `plan.md` — existencia de la Comprobación de constitución, filas, identificadores del mapa, celdas sin consecuencia
5. **`gate`**: revisión humana del plan, `on_reject: abort`
6. `command: speckit.tasks` · **`shell`**: conformidad sobre `tasks.md`
7. `command: speckit.analyze`
8. **`gate`**: autorización explícita antes de implementar — hoy es una regla de `AGENTS.md` que el agente puede saltarse
9. `command: speckit.implement`
10. `command: speckit.converge` · **`shell`**: conformidad final

Los pasos 5 y 8 son los que «muerden sin soltar». El paso 8 es, además, la primera vez que la autorización humana previa a `implement` deja de depender de que el agente la recuerde.

## 4.2 · Lo que esta arquitectura **no** resuelve

- **Nada de lo que ocurre en conversación.** Una propuesta hecha en el chat sigue sin pasar por ningún control. Para ese territorio solo existen las reglas 1 y 11 de `AGENTS.md`. El workflow no lo alcanza.
- **La calidad de una respuesta.** Sigue vigente el límite de la propuesta 006: se verifica que la pregunta se hizo, no que la respuesta sea buena.
- **La mitad del método que mide resultado humano.** `V01`–`V12` y las pruebas moderadas con personas siguen sin ejecutarse nunca. Sigue siendo `G3` de la propuesta 006, y sigue siendo el camino más importante.
- **La adopción.** Un método que solo corre bajo workflow excluye a quien invoca comandos sueltos. La versión 2.0 debe funcionar en los dos modos, con el workflow como camino recomendado y no como requisito.

---

# 5 · Los defectos de la v1.x y qué los produjo

Medido sobre el preset 1.2.0, contra el núcleo v2.1 y el anexo v1.2.

| # | Defecto | Causa |
|---|---|---|
| 1 | `SH-SCORE` invertido de criterio de salida a criterio de entrada, propagado a cinco artefactos | Compilación desde la memoria del texto, no desde el texto |
| 2 | Una regla inventada —«Progreso del usuario en 0 impide avanzar»— atribuida al núcleo | Ídem, agravado por la atribución |
| 3 | `P02` debilitado de «esfuerzo, claridad **y** confianza» a «**o**» | Ídem |
| 4 | Los seis estados de `V09` rotulados `P08`, con pérdida de «recuperación» | Ídem |
| 5 | `CR02` y `CR03` citados para disposiciones que no contienen | Ídem |
| 6 | Seis identificadores del mapa mínimo del anexo sin citar | Nada comprobaba la cobertura del mapa |
| 7 | `handoffs` del core borrados en los cinco comandos que los declaran | El `wrap` sustituye el frontmatter completo |
| 8 | `__SPECKIT_COMMAND_*__` perdidos: 8 ocurrencias del core, 0 en nuestras plantillas | Las plantillas son `replaces` y nadie comparó |
| 9 | Secciones que los comandos nativos buscan por nombre, renombradas o ausentes | El anexo exige esa comprobación antes de distribuir; **nunca se ejecutó** |
| 10 | Disposiciones del piloto presentadas como doctrina | No existía una capa donde ponerlas con etiqueta |

**Nueve de diez son errores de transcripción o de contrato, no de criterio.** Ninguno requería mejor juicio. Todos requerían una comprobación que no existía.

## 5.1 · Cómo la arquitectura los previene

| Causa | Mecanismo que la cierra |
|---|---|
| Compilar de memoria (1–5) | **Mapa de identificadores**: cada comprobación declara identificador y cita literal del núcleo; el build falla si la cita no existe o no coincide |
| Cobertura del mapa (6) | Comprobación automática comando × mapa del anexo, en el build |
| Frontmatter y tokens (7, 8) | Comprobación de conservación: `handoffs`, `description`, `__SPECKIT_COMMAND_*__` y placeholders del core presentes en el compuesto |
| Contrato comando↔plantilla (9) | La comprobación que el anexo ya exigía, esta vez ejecutada en el build |
| Piloto mezclado con doctrina (10) | Dos capas declaradas: `doctrina` traza al núcleo; `práctica` traza al registro del piloto y se marca como tal |

**Ese es el residuo.** `tools/build-package.sh` no produce ZIP si la trazabilidad no cierra.

---

# 6 · Lo que se rescata y lo que se descarta

## Se rescata

- El **criterio de compilación**: *X existe* / *X traza a Y* / *ninguna X sin Z*, y el patrón de que las disposiciones sobre artefactos y estados compilan y las que nombran cualidades de la experiencia no.
- La mayoría de las **79 comprobaciones**. Verificadas como fieles: `P06`, `P07`, `P10`, `D04`, `D05`, `A06`, `A08`, `F03`, `F06`, `F07`, `CR07`, `CR03`, `CR06`, las citas de `SH-AP`, `SH-DONE` en `converge`. `tasks` y `converge` cubren su mapa completo.
- El análisis de **qué no compila** (propuesta 006, §3) y **qué cuesta ejecutar el método** (propuesta 007).
- Las **reglas 1 y 11 de `AGENTS.md`**, que cubren el territorio donde ningún comando gobierna.
- **`PARA_QUIEN_DECIDE.md`**, salvo su pregunta 1, que enseña a exigir el defecto 1.
- Los **hallazgos del piloto**, ahora como capa etiquetada.

## Se descarta

- La **constitución como transporte del manifiesto completo**. Ver §7: es la decisión doctrinal y es de la autoridad.
- El **preset como único mecanismo**.
- Las **descripciones con forma de garantía**, que no contienen situación que el agente pueda reconocer. Los cinco comandos de `lean` siguen la forma *verbo + artefacto + entrada*; los ocho nuestros nombran **cero artefactos**.
- Los **comandos reescritos tres veces** sin una fuente de verdad mecánica.

---

# 7 · La decisión doctrinal, que no puedo tomar

La versión 2.0 propone que **el manifiesto deje de ser el artefacto de ejecución sin dejar de ser la fuente**: permanece completo, canónico, versionado y licenciado en el paquete, y cada instrucción ejecutable traza a él con cita verificable. Lo que se carga en cada operación es el producto compilado.

El anexo v1.2 lo impide hoy, en tres lugares:

> - Línea 104: «una proyección estructuralmente nativa del **núcleo completo** v2.1 ocupará `.specify/memory/constitution.md`».
> - Línea 111: «La constitución de SpecKit debe contener el núcleo completo, **no un resumen, una selección de principios ni una referencia que el agente pueda omitir**.»
> - Línea 327: «No debe utilizarse para pedir al agente que genere una versión resumida, mejorada o contextualizada del manifiesto.»

**La preocupación del anexo es correcta y hay que respetarla:** un resumen es cómo muere una doctrina. La diferencia que propongo es que aquí no habría resumen ni selección, sino **compilación trazada y verificada**, con el texto íntegro conservado y citable. Pero la distinción entre «compilar» y «resumir» **es doctrinal, no técnica**, y no me corresponde declararla.

Hay un dato que la informa, de la propuesta 007: la constitución es el **66%** del costo de cada operación, y el **19%** de ella —propósito, ejemplo aplicado, texto canónico, influencias— no lo usa ninguna operación.

**Esta decisión gobierna todas las demás.** Si la respuesta es que la constitución debe seguir conteniendo el núcleo completo, la arquitectura de §4 sigue siendo válida y valiosa, pero la versión 2.0 será un método correcto y caro en vez de un método correcto y afilado.

---

# 8 · Conformidad con `PUBLISHING.md`, que nunca comprobamos

Requisitos oficiales incumplidos hoy:

| Requisito | Estado |
|---|---|
| `repository` en `preset.yml`, «valid and public» | **Ausente** |
| Probado con `specify preset add --dev` | No ejecutado |
| `specify preset resolve spec-template` verificado | No ejecutado como validación previa |
| `specify preset info` verificado | No ejecutado |
| Instalación desde el archivo de un release etiquetado | No ejecutado |
| Registro de comandos en los directorios del agente, verificado | Verificado en el piloto, no como validación de publicación |
| Repositorio público y release de GitHub | No existen |

Se cumplen: `id`, `name`, `version`, `description`, `author`, `license`, `requires.speckit_version`, y las convenciones de nombres.

---

# 9 · Consecuencias y costo

- **El piloto del sitio.** Tiene el preset 1.2.0 instalado y verificado, con `T052` cerrado. Una v2.0 obliga a reinstalar o a fijar la versión. Por el principio general dictado por la autoridad, **esto es un input y no una restricción**: si el sitio se rehace, se rehace.
- **`DP-02`.** El incremento invalida afirmaciones fácticas de proyectos instalados. `FR-009` del PRD del sitio ya está obsoleto y se aleja otro paso. Corregirlo sigue siendo decisión de la autoridad de producto del sitio.
- **Alcance real del trabajo.** No es una versión del preset. Son un preset, una extensión, un workflow, un bundle, un anexo v2.0 y un ensamblador con pruebas de conformidad.
- **El riesgo principal.** Cuatro mecanismos son más superficie que uno. La mitigación es que tres de los cuatro son *declarativos* —YAML pineado— y solo el script de conformidad es código que hay que mantener y calibrar. La advertencia de la propuesta 006 sigue vigente: una comprobación mal calibrada produce falsos positivos que enseñan a ignorarla.

---

# 10 · Orden de trabajo propuesto

1. **Mapa de identificadores del núcleo** — cada disposición, su identificador, su texto literal, su ubicación. Es la fuente de verdad de todo lo demás y no existe hoy.
2. **Prueba de conformidad del paquete** — antes del preset, no después. Comprueba citas, cobertura del mapa del anexo, conservación de frontmatter y tokens, y contrato comando↔plantilla.
3. **Anexo v2.0** — recoge la decisión de §7, la arquitectura de §4 y la condición cumplida de la línea 107.
4. **Preset** — plantillas y `wrap`, con descripciones en forma de disparador y `handoffs` conservados.
5. **Extensión** de conformidad.
6. **Workflow** con sus compuertas.
7. **Bundle** que pinea las cuatro piezas.

**No empezar por reescribir los ocho comandos.** Es lo que se hizo tres veces y es lo que produjo los diez defectos de §5.

---

# 11 · Decisión humana requerida

1. **La de §7**, que gobierna todo: si la constitución sigue transportando el núcleo completo, o si pasa a ser el producto compilado con el núcleo conservado como fuente trazable.
2. **Si se adopta la arquitectura de cuatro capas** de §4, dando por cumplida la condición que el propio anexo fijó en su línea 107.
3. **Si el workflow es camino recomendado o requisito.** Recomiendo lo primero: un método que solo corre bajo workflow excluye a quien invoca comandos sueltos, y la adopción es el objetivo.

---

## Nota sobre cómo se produjo este documento

El hallazgo de §1 corrige un error mío. La propuesta 005 declaró inexistente un mecanismo que existe, porque verifiqué dos de tres y generalicé. Ese error sobrevivió tres versiones del preset y orientó toda la discusión sobre coerción, incluida la reserva del «botón rojo» de `settings.json` como último recurso — reserva que ahora puede revisarse, porque el workflow ofrece coerción real sin romper la neutralidad de agente.

Es el mismo modo de fallo que §5 describe: no un juicio equivocado, sino una comprobación que no se hizo.
