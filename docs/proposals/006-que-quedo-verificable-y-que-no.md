# Análisis 006 — Qué quedó verificable en el preset 1.2.0, qué no, y cómo abordar la brecha

**Fecha:** 2026-09-22
**Estado:** análisis del trabajo aplicado. La compilación está **aplicada** en el preset 1.2.0; **las opciones para cerrar la brecha no lo están**.
**Origen:** instrucción de Damián Acuña tras contrastar el método con un análisis externo sobre compilar el manifiesto a reglas accionables.

---

# 1 · El criterio de compilación

Una disposición **compila** cuando puede expresarse en una de estas tres formas:

| Forma | Ejemplo |
|---|---|
| **X existe** | «Cada componente especifica los seis estados» |
| **X traza a Y** | «Cada elemento visible traza a un requisito» |
| **Ninguna X sin Z** | «Ningún campo capturado carece de uso declarado» |

Se **resiste** cuando se expresa como un adjetivo de calidad: *proporcional*, *honesto*, *claro*, *comprensible*, *la cantidad correcta de*.

**El patrón que emergió:** las disposiciones que nombran **artefactos y estados** compilan. Las que nombran **cualidades de la experiencia** no.

## 1.1 · Antes y después, cuatro casos reales

| Disposición | En 1.1.0 | En 1.2.0 |
|---|---|---|
| `P07` | «recuperación proporcional al riesgo» | Toda acción **irreversible** declara su consecuencia antes de ejecutarse; toda **reversible** declara cómo se revierte |
| `P09` | «progreso honesto» | Cada interacción crítica declara su presupuesto de respuesta; todo trabajo en curso declara su punto de persistencia |
| `P06` | «cada elemento debe justificarse» | Cada elemento visible traza a un requisito o Job Story. **Un elemento sin traza se elimina** |
| `P10` | «confirmación proporcional al impacto» | Ningún campo capturado carece de uso declarado; toda acción de alto impacto exige autorización registrada |

La operación que hizo compilar a `P07` es la que más se repite: **sustituir una escala continua —«proporcional»— por una clasificación binaria** —reversible o irreversible—. Lo mismo con `P10`: «alto impacto» exige una lista, no un juicio caso a caso.

---

# 2 · Qué quedó verificable, medido

**79 comprobaciones** repartidas en siete comandos. El preset 1.0.2 tenía cero; citaba tres identificadores y hoy cita 69.

| Comando | Comprobaciones |
|---|---:|
| `plan` | 19 |
| `specify` | 16 |
| `implement` | 12 |
| `analyze` | 11 |
| `converge` | 8 |
| `clarify` | 7 |
| `tasks` | 6 |

## 2.1 · Las que compilaron del todo

**Estructura y cobertura** — se responden contando filas y cruzando tablas.

- `F01`, `F02`, `A01`, `A02`, `CR03` — la matriz de cobertura no tiene elementos sin destino
- `A07` — cada criterio de aceptación tiene tarea de verificación con evidencia nombrada
- `A06` — la tabla de presupuesto de complejidad tiene sus cinco columnas sin celdas vacías
- `A08` — cada decisión registra alternativas, tradeoffs y evidencia pendiente

**Estados y acciones** — se responden con un inventario.

- `P08` — los **seis** estados por componente y por ruta: vacío, carga, error, éxito, interrupción, retorno
- `A05` — todo estado que aparezca y no esté en el inventario se declara antes de usarse
- `P07` — cada acción clasificada reversible o irreversible, cada irreversible con su consecuencia declarada
- `P10` — ningún campo capturado sin uso declarado; toda acción de alto impacto con autorización registrada

**Trazabilidad** — se responden cruzando dos listas.

- `P01` — cada requisito declara el progreso que habilita
- `P06` — cada elemento visible traza a un requisito. **Sin traza, se elimina**
- `P03` — ningún término del esquema aparece en texto visible

**Determinismo y evidencia**

- `D04` — cada regla crítica tiene prueba automatizada y no depende de salida generativa
- `D05` — ningún entregable se declara terminado sin evidencia enlazada
- `D06` — toda salida generativa declara su incertidumbre
- `V01`–`V12` — cada dimensión declara si tiene evidencia, parcial o ninguna

**Conducta del agente** — se responden leyendo el informe.

- `CR02` — antes de abrir una pregunta, la fuente consultada está nombrada. **Sin fuente, no se formula**
- `CR04` — ninguna recomendación presentada como decisión tomada
- `CR07` — ningún archivo agrega capacidades sin fundamento
- `SH-SCORE` — puntuación de entrada con ninguna dimensión crítica en `0` sin bloqueo declarado

## 2.2 · Cómo se responden, en la práctica

| Tipo | Mecanismo | ¿Automatizable? |
|---|---|---|
| Existencia de sección o tabla | Buscar el encabezado y contar filas | **Sí** |
| Celda vacía o marcador | Detectar `[…]`, `TBD`, cadenas cortas | **Sí** |
| Trazabilidad cruzada | Cruzar dos listas de identificadores | **Sí** |
| Seis estados por componente | Contar contra el inventario | **Sí** |
| Términos del esquema en texto visible | Lista de términos contra cadenas de interfaz | **Sí** |
| Consecuencia que repite el enunciado | Comparar la celda con el texto del identificador | **Parcial** — heurística |
| Fuente nombrada antes de preguntar | Leer el informe | **No** — lo lee una persona o `analyze` |

Seis de las siete son automatizables. **Eso es lo que vuelve posible el script de la propuesta 005**, que antes de esta compilación no tenía qué comprobar.

---

# 3 · La brecha: qué NO compila

Seis comandos de ocho declaran ahora su propio límite. Esto es lo que ninguna comprobación alcanza.

## 3.1 · Las cualidades de la experiencia

| Disposición | Qué sí compila | Qué **no** |
|---|---|---|
| `P02` | Que **exista** un criterio de aceptación sobre esfuerzo, claridad o confianza | Que la experiencia **sea** clara o confiable |
| `P04` | Que la declaración de profundidad progresiva exista, y que ninguna ruta sea un callejón sin salida | Que la **cantidad** de profundidad sea la correcta |
| `P05` | Que toda convención propia esté declarada y justificada | Que un elemento **se comprenda** sin leyenda |
| `V02`, `V04`, `V05` | Que exista evidencia registrada | Que las personas **progresen, comprendan o no se sobrecarguen** |

El patrón es uno solo: **se puede verificar que la pregunta fue hecha; no que la respuesta sea buena.**

## 3.2 · Lo que ocurre en conversación

`analyze` lee artefactos. Una propuesta hecha en el chat, una pregunta formulada fuera de un comando o un informe presentado de viva voz **no pasan por ninguna comprobación**. Los tres fallos de juicio del piloto ocurrieron exactamente ahí.

Para ese territorio solo existen las reglas 1 y 11 de `AGENTS.md`, que son persuasión.

## 3.3 · La sinceridad de la declaración

Se puede verificar que nombraste una fuente antes de preguntar. **No que la consultaras de verdad, ni que la leyeras bien.** Una declaración plausible y hueca pasa toda comprobación de forma.

Es el segundo hallazgo de `C8` aplicado a este nivel: una comprobación de forma invita a satisfacerla en falso.

---

# 4 · Cómo abordar la brecha, con su tradeoff

Cuatro caminos. **Ninguno está aplicado.**

## `G1` · Script de conformidad — propuesta 005

Automatiza las seis comprobaciones automatizables de §2.2.

**A favor.** Es lo único que detiene trabajo de verdad, si el proyecto lo conecta a su build. La compilación acaba de volverlo posible: antes no había qué comprobar.

**Tradeoff.** Solo alcanza a la forma. **Invita a satisfacerla en falso** — llenar la tabla con consecuencias plausibles y huecas. Y añade una superficie que hay que mantener y calibrar: demasiado estricto bloquea planes correctos, demasiado laxo no detecta nada.

**Costo:** preset 1.3.0, una re-sincronización, y la primera pieza del paquete capaz de bloquear a alguien.

## `G2` · Verificador independiente

Un segundo agente, que no escribió el trabajo, aplica las 79 comprobaciones y reporta.

**A favor.** Alcanza lo que un script no: puede juzgar si una consecuencia repite el enunciado o dice algo. Es barato y no requiere versionar el preset. Y **es portable**: funciona igual en Claude Code, Cowork o Cursor.

**Tradeoff.** Es un agente revisando a un agente. Comparte el punto ciego: `M1` demostró que dos agentes de acuerdo no detectan lo que ambos omiten. Reduce el riesgo; no lo elimina.

**Costo:** ninguno en el paquete. Es una práctica, no un artefacto.

## `G3` · Ejecutar la mitad sin estrenar

El informe del piloto lo dice: `B12` está en **0 de 13**. `V01`–`V12`, `SH-SCORE` y las pruebas moderadas con personas **nunca se ejecutaron**.

**A favor.** Es el único camino que cierra la brecha de verdad, porque lo no verificable —comprensión, progreso, carga— **solo lo verifica una persona**. Y ya está especificado y planificado: no hay que construir nada.

**Tradeoff.** Es el más caro en tiempo humano y el único que no puede delegarse a ningún agente. Requiere reclutar personas de las audiencias reales.

**Costo:** cero en el paquete. Todo el costo es tuyo y de tu tiempo.

## `G4` · Botón rojo — `settings.json`

Hooks del arnés que bloquean llamadas a herramientas.

**A favor.** Es la única coerción real que no depende de que el proyecto conecte nada.

**Tradeoff.** Protege **un** stack de los tres que usas. Comprueba archivos, no doctrina. Vive fuera del repositorio y de `SHA256SUMS`. Y bloquear una herramienta es contundente y ciego: un falso positivo detiene trabajo legítimo.

**Costo:** reservado como último recurso por decisión del 2026-09-22.

---

# 5 · Lo que recomiendo, y en qué orden

**`G3` primero, `G2` en paralelo, `G1` después, `G4` solo si hace falta.**

La razón es una sola: **la brecha real no es que falten comprobaciones automáticas. Es que la mitad del método que mide resultado humano no se ha ejecutado nunca.**

Construir `G1` antes de `G3` es automatizar la verificación de la forma mientras la verificación del fondo sigue sin estrenarse. Se puede tener un script en verde y un producto que nadie comprende.

`G2` no cuesta nada y puede empezar ya: aplicar las 79 comprobaciones desde una sesión que no escribió el trabajo.

## Y una advertencia sobre esta compilación

**No está probada.** Se escribió hoy y ningún ciclo se ejecutó bajo ella. Las 79 comprobaciones son una hipótesis sobre qué se puede verificar, no un resultado medido.

El riesgo concreto: **una comprobación mal calibrada produce falsos positivos que enseñan a ignorarla**, que es el mismo mecanismo de `B2` y de `C10`. La más frágil es la que detecta consecuencias que solo repiten el enunciado — la más útil y la más fácil de calibrar mal.

---

# 6 · Decisión humana requerida

1. **Si se empieza por `G3`** —ejecutar `B12` en el piloto— o por otro camino.
2. **Si se adopta `G2`** como práctica: un verificador independiente que aplique las 79 comprobaciones.
3. **Si `G1` espera** a que un ciclo bajo 1.2.0 muestre qué comprobaciones sobran o faltan.

`G4` queda reservado y no requiere decisión hoy.
