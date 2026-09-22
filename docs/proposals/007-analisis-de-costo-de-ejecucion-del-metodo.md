# Análisis 007 — Costo de ejecución del método: de dónde viene el texto y qué se puede optimizar

**Fecha:** 2026-09-22
**Estado:** análisis. **Nada modificado.**
**Objeto:** lo que un agente carga realmente al ejecutar una operación del método
**Origen:** instrucción de Damián Acuña tras observar que el texto creció versión tras versión mientras el argumento sostenía que compilar reduce el costo

---

# 1 · El hallazgo, primero

**Optimicé la capa equivocada, y la hice crecer mientras tanto.**

Una invocación típica de `plan` carga aproximadamente **36.500 tokens de método** antes de tocar una sola línea del proyecto:

| Qué se carga | Tokens | % |
|---|---:|---:|
| **Constitución completa** | **24.280** | **66%** |
| `AGENTS.md` (al iniciar sesión) | 5.650 | 15% |
| Comando compuesto `plan` (core + wrap) | 4.320 | 12% |
| `plan-template` | 1.440 | 4% |
| `CLAUDE.md` | 820 | 2% |

Las tres versiones del preset que produje —1.0.2 → 1.1.0 → 1.2.0— trabajaron sobre el **12%**. La constitución, que es **dos tercios del costo**, no la toqué nunca.

Y los ocho comandos la cargan entera. Verificado: los ocho referencian `memory/constitution.md`.

---

# 2 · De dónde vino el crecimiento que observaste

## 2.1 · Los wraps, medidos

| Comando | 1.0.2 | 1.1.0 | 1.2.0 | Factor |
|---|---:|---:|---:|---:|
| `plan` | 1.686 | 5.379 | **7.020** | ×4,2 |
| `implement` | 1.527 | 5.275 | 5.659 | ×3,7 |
| `specify` | 1.949 | 5.310 | 5.348 | ×2,7 |
| `analyze` | 1.349 | 3.720 | 4.534 | ×3,4 |

**El salto real fue 1.0.2 → 1.1.0**, cuando nombré las disposiciones en prosa: entre ×2,7 y ×3,9. La compilación de 1.2.0 fue casi plana —entre 0% y 7%— salvo `plan` (+30%) y `analyze` (+21%).

Es decir: **la compilación no fue la causa del crecimiento. Lo detuvo.** Una tabla de comprobaciones es más densa que la prosa sobre esas mismas comprobaciones. Pero llegó después de que el daño ya estuviera hecho.

## 2.2 · Cuánto pesa mi capa dentro de cada comando

| Comando | core | wrap | wrap % |
|---|---:|---:|---:|
| `plan` | 8.047 | **7.020** | **47%** |
| `implement` | 12.779 | 5.659 | 30% |
| `analyze` | 11.764 | 4.534 | 28% |
| `clarify` | 19.507 | 3.269 | 14% |

`plan` es el caso atípico: mi wrap casi iguala al comando nativo que envuelve.

## 2.3 · Lo que NO es el problema

Dos cosas que verifiqué y descarté como causa:

**El wrap no copia la constitución.** Busqué las frases doctrinales características —«revelación progresiva», «estados vacíos», «la atención es un recurso», «progreso honesto»— y aparecen en la constitución y **cero veces** en los ocho wraps. La regla del anexo —*«referenciar el identificador y describir el comportamiento exigido; no copiar una versión abreviada»*— se respetó.

**La duplicación entre wraps es marginal.** Nueve bloques repetidos, 4.624 bytes en total. Pero **solo un wrap se carga por invocación**, así que el ahorro real sería de unos 170 tokens. Irrelevante para el costo; relevante solo para mantenimiento.

---

# 3 · Dónde está el costo de verdad

## 3.1 · Composición de la constitución

| Sección | Bytes | Tokens | % |
|---|---:|---:|---:|
| `Core Principles` (`P01`–`P10`) | 16.841 | 4.950 | 20% |
| `SH-FUND` | 10.350 | 3.040 | 12% |
| `SH-GOV` | 7.946 | 2.330 | 9% |
| Flujo de trabajo | 6.718 | 1.970 | 8% |
| **Propósito del documento** | **6.105** | **1.790** | **7%** |
| Verificación | 5.894 | 1.730 | 7% |
| Doctrina para desarrollo con IA | 5.683 | 1.670 | 7% |
| **Ejemplo aplicado** | **4.565** | **1.340** | **5%** |
| `SH-AP` | 4.123 | 1.210 | 5% |
| Contrato reutilizable | 3.803 | 1.110 | 4% |
| Texto canónico | 2.735 | 800 | 3% |
| **Influencias y notas** | **2.316** | **680** | **2%** |
| `SH-POCKET` | 1.806 | 530 | 2% |
| `SH-INDEX` | 1.666 | 490 | 2% |

## 3.2 · Cuánto de eso necesita una operación

El mapa del anexo dice qué activa cada comando. `plan` necesita `P03`, `P04`, `P06`–`P10`, `D03`, `D04`, `F03`, `F06`, `F07`, `A05`–`A08`, `CR03`–`CR06`.

Eso es **siete de los diez principios y partes de cuatro secciones**. Estimado: entre el 30% y el 40% de la constitución.

**Se carga el 100% para usar el 35%.**

## 3.3 · Y hay un 19% que ninguna operación necesita

Cuatro secciones son **aparato explicativo dirigido a personas**, no instrucciones ejecutables:

| Sección | Qué hace | Tokens |
|---|---|---:|
| Propósito del documento | Explica el documento, sus rutas de lectura y su arquitectura | 1.790 |
| Ejemplo aplicado | El tutor de cálculo, ilustración pedagógica | 1.340 |
| Texto canónico | La prosa del manifiesto: el «por qué», no el «qué hacer» | 800 |
| Influencias y notas | Bibliografía y créditos | 680 |
| **Total** | | **4.610** |

Son **4.610 tokens en cada una de las ocho operaciones**, siempre, sin que ninguna los use.

Esto confirma con medición lo que el análisis externo planteaba: *un manifiesto es el género literario equivocado para instruir a un agente*. La constitución **es** el manifiesto completo, con su aparato de persuasión incluido.

---

# 4 · Opciones, con su tradeoff

## `O1` · Lectura selectiva dirigida por el wrap

El wrap ya nombra los identificadores que cada operación activa. Podría además indicar **las anclas** correspondientes, de modo que el agente lea las secciones asignadas en lugar del archivo entero, y escale a la lectura completa cuando el anexo lo exige: contradicción, regla indeterminada, decisión de alto riesgo o revisión transversal.

**Ahorro estimado:** hasta 15.000 tokens por invocación — el 41% del costo total de método.

**Por qué es legítimo.** El anexo ya lo diseñó. Su modelo de tres niveles existe exactamente para esto, y su texto dice que *«no exige crear resúmenes, fragmentos ni copias parciales»*. **Leer selectivamente no es crear un fragmento.** El archivo permanece completo.

**Tradeoff.** El agente puede omitir una disposición aplicable por contexto que el mapa no le asignó. El anexo prevé el caso con su nivel 3, pero esa escalada depende de que el agente reconozca que la necesita — y `M1` mostró que los agentes no detectan bien lo que no saben que les falta. **Cambia un costo cierto por un riesgo probabilístico.**

**Costo:** el wrap crece un poco. Versiona el preset.

## `O2` · Separar el aparato explicativo de la constitución

Mover propósito, ejemplo aplicado, texto canónico e influencias a un documento acompañante, dejando como constitución el núcleo operativo.

**Ahorro:** 4.610 tokens en cada operación, garantizado y sin riesgo de omisión, porque nada de eso es ejecutable.

**Tradeoff, y es serio.** Esto **sí es fragmentar el núcleo**, y el anexo lo prohíbe: *«la constitución de SpecKit debe contener el núcleo completo, no un resumen, una selección de principios ni una referencia que el agente pueda omitir»*.

Requeriría decisión doctrinal tuya y, probablemente, una versión del núcleo. **No lo recomiendo sin esa decisión.** Lo registro porque es el único ahorro sin contrapartida técnica.

## `O3` · Comprimir el wrap de `plan`

Es el atípico: 47% de su comando compuesto. Sus tres apartados finales —`SH-SCORE`, `SH-AP`, «lo que no cubren»— podrían condensarse un 25%.

**Ahorro:** ~500 tokens, solo en `plan`.

**Tradeoff.** Condensar acerca al problema que veníamos de resolver: la prosa apretada vuelve a ser menos verificable que la tabla. **Bajo rendimiento, riesgo de retroceso.**

## `O4` · Deduplicar los ocho wraps

Nueve bloques repetidos, 4.624 bytes.

**Ahorro real: ~170 tokens por invocación.** Solo un wrap se carga cada vez.

**Tradeoff:** ninguno técnico, pero el beneficio es de mantenimiento —un solo lugar que editar—, no de costo. **No vale versionar el preset por esto solo.**

## `O5` · No optimizar

El costo de método es de ~36.500 tokens por operación. En una ventana grande eso es tolerable, y **ninguna de las optimizaciones está probada**: el preset 1.2.0 acaba de instalarse y no corrió un ciclo.

**Tradeoff:** el costo se paga en cada operación de cada proyecto, indefinidamente. Pero optimizar antes de medir el rendimiento real es el mismo error que construir el script de conformidad antes de ejecutar `B12`.

---

# 5 · Lo que recomiendo

**`O1` cuando haya evidencia de un ciclo bajo 1.2.0. Nada antes.**

Tres razones:

1. **Es el único ahorro grande que no cruza doctrina.** 41% del costo, con el mecanismo ya diseñado en el anexo.
2. **Su riesgo es medible con el ciclo que está por empezar.** Si el sitio ejecuta `B04` en adelante bajo 1.2.0 y ninguna disposición se pierde, la lectura completa está sobrando. Si algo se pierde con la constitución entera delante, la lectura selectiva lo empeoraría.
3. **`O2` es más barato y más seguro técnicamente, pero es tuyo y es doctrinal.** Puedo dejarlo planteado; no lo redacto.

`O3` y `O4` no justifican una versión por sí solos. Si alguna vez se toca el preset por otra razón, conviene incluirlos ahí.

---

# 6 · Lo que este análisis no responde

**Si más texto degrada realmente la adherencia.** Es la premisa del análisis externo y la asumí, pero **no la medí**: no tengo datos que comparen cumplimiento bajo 1.0.2 contra 1.2.0. El piloto los va a producir.

**Si la estimación de tokens es exacta.** Usé una aproximación de 3,4 bytes por token para español. El orden de magnitud es correcto; el número exacto depende del tokenizador.

**Si el 35% estimado que `plan` necesita es el correcto.** Lo derivé del mapa del anexo, no midiendo qué consultó realmente un agente. Esa medición sí es posible y sería el insumo que `O1` necesita para calibrarse.

---

# 7 · La conclusión incómoda

Tu observación era correcta y más profunda de lo que parecía.

Durante tres versiones optimicé el 12% del costo y lo hice crecer ×4 en el peor caso. El 66% —la constitución completa cargada en cada operación— **nunca lo miré**, y es el único lugar donde hay algo grande que ganar.

La compilación de 1.2.0 fue lo correcto por razones de cumplimiento, y frenó el crecimiento. Pero **no fue una optimización de costo, y yo la presenté como si lo fuera.**
