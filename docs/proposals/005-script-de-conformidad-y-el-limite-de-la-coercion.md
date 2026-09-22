# Propuesta 005 — Script de conformidad, y dónde está el límite real de la coerción

**Fecha:** 2026-09-22
**Estado:** propuesta para decisión de Damián Acuña. **Nada aplicado.**
**Origen:** la pregunta «¿no es posible una configuración de manera que el agente no pueda omitir el manifiesto aunque quiera?»

## Respuesta corta

**Dentro de SpecKit, no.** Y no por una limitación del paquete: por cómo está construido SpecKit.

Fuera de SpecKit, **sí, parcialmente**, y solo para la forma. Este documento dice exactamente cuánto.

---

# 1 · El hallazgo que reorienta todo: en SpecKit no existe nivel mecánico

Verificado sobre SpecKit 1.0.8.

## 1.1 · Los hooks los ejecuta el agente, no el arnés

`.specify/extensions.yml` permite declarar hooks `before_*` y `after_*`, incluidos **obligatorios** (`optional: false`). Parece coerción. No lo es. El texto del comando nativo dice, literalmente:

> After emitting the block above **you MUST actually invoke the hook** and wait for it to finish before continuing… Emitting the block alone does not run the hook.

Es una **instrucción dirigida al agente**. Nada la impone. Un agente que no la siga no es detenido por nada: simplemente no ejecuta el hook, y el flujo continúa.

## 1.2 · Un script de preset tampoco se ejecuta solo

El esquema admite `provides` de tipo `script` —`VALID_PRESET_TEMPLATE_TYPES = {"template", "command", "script"}`—, de modo que el preset **puede entregar** un script. Pero entregarlo no lo ejecuta. Quien lo invoca sigue siendo el agente, salvo que alguien más lo llame.

## 1.3 · Consecuencia

| Nivel | Mecanismo | ¿Lo puede omitir el agente? |
|---|---|---|
| **Persuasión** | Núcleo, `AGENTS.md`, `wrap` de los comandos | Sí, en silencio |
| **Trazabilidad** | Declaración de activación, huecos en plantillas, `analyze` | Sí, pero deja rastro |
| **Mecánica** | — | **No existe dentro de SpecKit** |

La adaptación v1.1.0 llevó el método del primer nivel al segundo. **El tercero no puede construirse con las piezas de SpecKit.**

---

# 2 · Dónde sí existe coerción real

Solo hay dos lugares, y ninguno pertenece a SpecKit.

## 2.1 · El build del propio proyecto

Un script que forma parte de la suite de pruebas, del *pre-commit* o de la integración continua se ejecuta **cuando lo corre una persona o una máquina**, no cuando el agente decide. Si falla, el trabajo se detiene de verdad.

Esta es la vía recomendada, y define la división de responsabilidades:

- **El paquete entrega** el script, neutral de agente.
- **El proyecto lo conecta** a algo que el agente no controla.
- **`analyze` comprueba** que esté conectado y que pase.

Sin el segundo paso el script es decorativo. Por eso la conexión debe declararse en `AGENTS.md`, «Completar por proyecto», donde `analyze` puede verla.

## 2.2 · El botón rojo: `settings.json` del agente

En Claude Code, los hooks de `settings.json` **sí los ejecuta el arnés**, no el agente. Un `PreToolUse` puede **bloquear** una llamada a herramienta. Es coerción genuina, disponible hoy, sin tocar el preset.

**Queda reservado como último recurso, por decisión de Damián Acuña del 2026-09-22.** Las razones de no adoptarlo ahora:

- **Rompe la neutralidad de agente.** El paquete sirve a Claude Code, Codex, Cursor y cualquier otro. Un hook de `settings.json` solo protege a uno.
- **Comprueba archivos, no doctrina.** Puede exigir que `plan.md` tenga la tabla llena antes de permitir escribir en `src/`. No puede verificar que se consultó `P04` antes de proponer una paleta.
- **Es configuración de la persona, no del proyecto.** Vive fuera del repositorio y fuera de `SHA256SUMS`.
- **Bloquear una herramienta es contundente y ciego.** Un falso positivo detiene trabajo legítimo sin conocer el contexto.

Se activa si el script de conformidad resulta insuficiente y la evidencia lo demuestra. No antes.

---

# 3 · Qué comprobaría el script, exactamente

Todo lo que sigue es **verificable mecánicamente**: se cumple o no, sin juicio.

## 3.1 · Sobre `plan.md`

| # | Comprobación | Falla cuando |
|---|---|---|
| 1 | Existe la sección «Comprobación de constitución» | Falta |
| 2 | Tiene al menos una fila de datos | La tabla está vacía o solo tiene el ejemplo |
| 3 | Sus filas citan los identificadores que el anexo asigna a `plan` | Falta alguno de `P03`, `P04`, `P06`–`P10`, `D03`, `D04`, `F03`, `F06`, `F07`, `A05`–`A08`, `CR03`–`CR06` sin declararlo no aplicable |
| 4 | Ninguna celda de consecuencia está vacía o es un marcador | Contiene `[…]`, `TBD`, `N/A` sin justificación, o menos de N caracteres |
| 5 | Ninguna consecuencia es una repetición del enunciado | «se respetará `P07`» en lugar de una conducta verificable |
| 6 | Existe la tabla de `SH-SCORE` de entrada con dimensiones puntuadas | Falta o está sin puntuar |
| 7 | Ninguna dimensión crítica está en `0` sin bloqueo declarado | Hay un 0 y el plan sigue adelante |

## 3.2 · Sobre `tasks.md`

| # | Comprobación | Falla cuando |
|---|---|---|
| 8 | Declara el estado esperado de las verificaciones por intervalo, o afirma explícitamente que ninguna queda en rojo | Silencio |

## 3.3 · Sobre `spec.md`

| # | Comprobación | Falla cuando |
|---|---|---|
| 9 | La matriz de cobertura no tiene elementos sin destino | Hay filas sin sección, requisito o escenario asignado |
| 10 | No quedan marcadores `NEEDS CLARIFICATION` al entrar a `implement` | Los hay y la implementación empezó |

## 3.4 · Sobre la conexión

| # | Comprobación | Falla cuando |
|---|---|---|
| 11 | `AGENTS.md` declara dónde está conectado el script | El campo está vacío |

---

# 4 · Qué NO puede comprobar, y por qué importa

- **Si una consecuencia es buena.** Puede exigir que la celda no esté vacía; no puede evaluar su calidad.
- **Si el agente consultó la doctrina o escribió texto plausible.** Son indistinguibles desde un script.
- **Nada de lo que ocurre en conversación.** Los tres fallos de juicio del piloto —`C12`, `C13`, `C14`— ocurrieron en el chat, fuera de todo artefacto. **Ningún script los alcanza.** Para ese territorio solo existen las reglas 1 y 11 de `AGENTS.md`, que son persuasión.

## 4.1 · Por qué alcanza más de lo que parece

El modo de fallo del piloto fue **omisión**, no mal juicio. `C13` y `C14` ocurrieron porque la doctrina **no se consultó**, no porque se consultara y se aplicara mal.

**Una comprobación de forma atrapa la omisión.** Eso cubre el modo de fallo observado, aunque no cubra el que no ocurrió.

## 4.2 · Y por qué hay que diseñarlo contra el juego

Una comprobación de forma **invita a satisfacerla en falso**: llenar la tabla con consecuencias plausibles y huecas. Es exactamente el segundo hallazgo de `C8`, donde redactar esquivando al validador habría producido una suite verde y una prosa peor.

Dos mitigaciones, y ninguna es completa:

1. **Que cumplir cueste menos que simular.** Si la comprobación exige lo que un plan bien hecho ya contiene, escribirlo de verdad es el camino corto.
2. **Que `analyze` siga siendo la capa de juicio.** El script comprueba que la declaración exista; `analyze` comprueba que sea concreta. Son dos pasadas distintas y ninguna reemplaza a la otra.

---

# 5 · Lo que esto cuesta en doctrina

El anexo decidió que la adaptación usara **solo presets**:

> No se crea una extensión, un workflow ni un bundle **mientras no exista una necesidad técnica demostrada que el preset no pueda resolver**.

Su razón para descartar extensiones fue de alcance, no una prohibición: *«como este anexo no agrega capacidades ni fases, una extensión no es el mecanismo inicial adecuado»*.

**La condición se cumplió.** El piloto demostró que la capa de texto es insuficiente, con medición: tres fallos de juicio, y solo dos fallos en todo el ejercicio evitados por una comprobación del método.

Un script de conformidad **no agrega etapas ni artefactos metodológicos**, que es lo que el anexo prohíbe. Comprueba que los artefactos que ya existen contengan lo que la doctrina ya exige. Cabe dentro de `provides: script` del propio esquema de presets.

Aun así, **es una decisión de la autoridad**, porque cambia qué es la adaptación: pasa de *«solo presets»* a *«presets más una comprobación que puede detener el trabajo»*. Y sería el primer componente del paquete capaz de bloquear a alguien.

---

# 6 · Alcance, versión y consecuencias

**Qué toca:** un archivo nuevo en el preset, `scripts/conformidad.sh`; una entrada `script` en `preset.yml`; un campo en la plantilla de `AGENTS.md` para declarar dónde se conecta; una comprobación añadida a `analyze`.

**Qué NO toca:** el núcleo, el anexo, la constitución materializada, el core de SpecKit.

**Versión:** preset **1.2.0**, paquete **1.5.0**.

**Consecuencia para el piloto:** una re-sincronización más, y una tarea nueva —conectar el script a su suite—. Su contenido publicable declararía `version: 1.2.0`. `FR-009` se aleja otro paso.

## Alternativa más simple

Entregar el script **sin** declararlo en `preset.yml` y sin que `analyze` exija la conexión: una herramienta disponible en `tools/` que cada proyecto usa si quiere.

Cuesta mucho menos, no cambia qué es la adaptación, y **no coerce a nadie**: vuelve al nivel de trazabilidad. Es honesta si se acepta que el objetivo no era la coerción sino tener la herramienta.

## Opción de no construir

Defendible. La adaptación v1.1.0 ya llevó el método de persuasión a trazabilidad, y eso **no se ha probado todavía en un ciclo real**. Construir el nivel mecánico antes de medir si el nivel de trazabilidad alcanza es optimizar sin evidencia — y el propio piloto advierte que ninguna corrección propuesta ha sido probada.

**Es la alternativa que recomendaría si no existiera una razón de plazo.** La v1.1.0 es nueva y aún no se ejecutó un ciclo bajo ella.

---

# 7 · Decisión humana requerida

1. **Si se construye el script de conformidad** —preset 1.2.0— o se espera a medir si la trazabilidad de la v1.1.0 alcanza.
2. **Si se entrega conectado** —`preset.yml`, `analyze` exige la conexión— o **suelto** en `tools/`, disponible sin obligar.
3. **Qué umbral usa la comprobación 5**, la que detecta consecuencias que solo repiten el enunciado. Es la más útil y la más fácil de calibrar mal: demasiado estricta bloquea planes correctos; demasiado laxa no detecta nada.

El botón rojo de `settings.json` queda **reservado y documentado**, sin activar, por decisión del 2026-09-22.

---

## Nota sobre cómo se produjo este documento

Redactado antes de escribir una línea del script, para que la autoridad vea qué detendría el trabajo antes de que exista algo capaz de detenerlo. Es la misma regla que estableció `M1`.

El hallazgo de §1 —que los hooks de SpecKit los ejecuta el agente— se verificó sobre el código de SpecKit 1.0.8 instalado, y **cambió la propuesta**: sin él, este documento habría propuesto un hook obligatorio creyéndolo coerción.
