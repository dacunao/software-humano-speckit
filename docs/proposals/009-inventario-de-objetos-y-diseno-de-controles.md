# Propuesta 009 — Los objetos del manifiesto, y qué se revisa de ellos

**Fecha:** 2026-09-22
**Estado:** propuesta para revisión y aprobación de Damián Acuña. **Nada aplicado.**
**Objeto:** sobre qué cosas se construyen los controles del método
**Inventario:** `docs/method/inventario-de-objetos.md`, generado. Este documento **no lo repite**: explica cómo se construyó y qué hay que revisar de él.

---

# 1 · La regla que gobierna todo este trabajo

Dictada por la autoridad:

> **Un objeto entra al método solo si el manifiesto lo nombra.** No se compilan conceptos que el manifiesto no respalde, ni se crean objetos aparentemente representativos que no existan en el documento original.

De ahí se sigue el resto:

- **Las obligaciones se adhieren a cosas que el manifiesto ya nombra. No crean cosas nuevas.**
- El núcleo nombra cosas en tres lugares: sus **ocho artefactos**, sus **doce dimensiones de verificación** y el **fundamento de producto**.
- Las demás familias **no nombran cosas**: los principios nombran compromisos, el flujo nombra pasos, el contrato nombra momentos, la entrega nombra contenidos de informe y las detenciones nombran condiciones. Todas son **disposiciones** que se adhieren a un objeto.

---

# 2 · Por qué la unidad de control no es el identificador

El índice operativo del núcleo lo dice de sí mismo:

> «Esta capa de navegación permite que personas, agentes y adaptadores citen obligaciones del núcleo de manera estable. Los identificadores **no agregan doctrina**… solo señalan contenido ya aprobado.»

Son direcciones, no deberes. Y el núcleo enuncia el mismo deber varias veces, desde disposiciones distintos, para reforzarlo:

| Paso del flujo | Artefacto | Instrucción del contrato | Salida esperada |
|---|---|---|---|
| Comprender el fundamento | Mapa del fundamento | Antes de programar | Fuentes autorizadas |
| Establecer cobertura | Mapa de cobertura | Al planificar | Inventario de alcance |
| Establecer el contrato de experiencia | Contrato de experiencia | Al diseñar | Estados cubiertos |
| Construir, integrar y verificar | Plan de aceptación | Antes de declarar terminado | Pruebas y evidencia |

Cuatro familias, **un solo objeto por fila**. Si el control se construye por identificador, cada deber produce tres o cuatro controles que dicen lo mismo, y el agente los cuenta como protecciones distintas.

---

# 3 · Qué contiene el inventario, y qué garantiza cada parte

| Qué hay | Quién lo pone | ¿Hay que revisarlo? |
|---|---|---|
| El nombre de cada objeto | El núcleo | No |
| El texto literal de cada disposición | Extracción mecánica del mapa de identificadores | No |
| **Qué disposiciones corresponden a cada objeto** | **Esta propuesta** | **Sí. Es lo único** |

**Diecinueve objetos.** Nueve artefactos y el fundamento de producto; diez dimensiones de verificación; y dos objetos que el núcleo nombra dos veces y quedaron fusionados.

**Cómo se revisa un objeto:** leer las frases de su tabla y responder una sola pregunta — *¿hablan todas de esta misma cosa?* Si alguna no corresponde, o si falta una que debería estar, ese es el hallazgo. **No hay que ir a buscar ningún código.**

## 3.1 · La comprobación de completitud

Las **76 disposiciones del núcleo están cubiertas**: sesenta y ocho adheridas a un objeto, ocho declaradas en la conjunto sin objeto propio. Y las **treinta reglas de diseño de los diez principios** están todas adheridas.

Esa comprobación la ejecuta el propio generador. No es una afirmación: si una disposición quedara suelta, aparecería.

## 3.2 · La regla que resolvió las cosas nombradas dos veces

> Un artefacto y una dimensión de verificación son el **mismo** objeto cuando la dimensión verifica exactamente lo que el artefacto registra. Son **dos** objetos cuando el artefacto registra más de lo que la dimensión verifica, o cuando la dimensión abarca más de un artefacto.

| Pareja | Veredicto |
|---|---|
| Fundamento de producto ↔ Mapa del fundamento | **dos** — el flujo exige un «mapa fiel… sin reformularla», y no se exige fidelidad de una cosa consigo misma. Ver 9.1: sus disposiciones quedaron repartidos sin solapamiento |
| Mapa de cobertura ↔ Cobertura | **uno** — fusionados |
| Modelo de estados ↔ Estados | **dos** — el artefacto abarca eventos, reglas, permisos y persistencia; la dimensión verifica una propiedad sobre situaciones repartidas entre dos objetos |
| Presupuesto de complejidad ↔ Carga | **uno** — fusionados |

La regla se sostiene también donde no la apliqué: el contrato de experiencia registra seis contenidos y las dimensiones de comprensión y profundidad verifican dos de ellos, así que son objetos distintos. Lo mismo con la ficha de Job Story frente a progreso y causalidad.

---

# 4 · El criterio para admitir un control, que es del propio núcleo

> «Los principios no describen aspiraciones decorativas. Cada uno debe ser capaz de **cambiar una decisión, detener una implementación o exigir evidencia adicional**. Si una frase no tiene consecuencias prácticas, no cumple una función dentro del marco.»

Se aplica igual a los controles de esta adaptación. **Un control que nunca cambiaría una decisión es carga, no protección**, y no entra.

Esa frase está en la sección de principios de diseño del núcleo y **no tiene identificador**. Es una de las cuatro obligaciones sin dirección de la sección 8.

---

# 5 · Cómo se comporta un control

El núcleo define **dos estados admisibles**, y no hay que inventar más. Su definición de terminado exige que todo elemento obligatorio tenga:

> «una implementación y una evidencia verificable, **o una excepción explícita y aprobada**»

| Estado | ¿Detiene el trabajo? |
|---|---|
| Tiene implementación y evidencia verificable | No |
| Tiene excepción explícita y aprobada | No |
| Ninguna de las dos | **Sí** |

**El método no rechaza lo incompleto. Rechaza lo que falta sin que nadie lo sepa.**

Esto resuelve por sí solo la adopción en un repositorio que nació antes del manifiesto: entra declarando excepciones aprobadas, y la operación de convergencia las va transformando en evidencia. **No hacen falta niveles de conformidad**: el núcleo ya lo había resuelto.

---

# 6 · Términos que conviene declarar

Aporte de esta propuesta, **no doctrina**. Son los puntos donde el término del manifiesto y el término corriente de la industria no significan lo mismo, y confundirlos cambia el trabajo.

| Término del núcleo | Qué conviene aclarar |
|---|---|
| **Fundamento de producto** | El núcleo enumera sus formas: Job Story, Jobs to Be Done, épica, capacidad, requisito, regla de negocio, recorrido, criterio de aceptación o una combinación. Y es explícito: **«no es un nuevo tipo de documento ni una plantilla obligatoria»**. Sus elementos «no necesitan utilizar estos nombres ni este orden» |
| **Job Story** | *No es* una historia de usuario. La historia empieza por un rol y suele prescribir una función, que el núcleo registra como antipatrón. Existe solo si la definición de producto ya la trae; el agente no la inventa, y un producto puede no tener ninguna |
| **Contrato de experiencia** | Término propio del manifiesto **sin equivalente extendido**. Es una sección de la especificación, no un documento aparte |
| **Presupuesto de complejidad** | Término propio del manifiesto **sin equivalente extendido**. Es el instrumento que registra la carga; la dimensión de carga agrega un criterio que la tabla no contiene: si el sistema podía resolverlo de forma segura |
| **Definición de terminado** | En uso corriente significa «pasó las pruebas técnicas». En el núcleo incluye además que **las personas alcancen los resultados previstos**. No son lo mismo |
| **Determinismo donde importa** | «Crítica» no significa importante: significa que **de la regla depende certeza, cumplimiento o seguridad**. Ese es el umbral |
| **IA**, como dimensión de verificación | Trata de la inteligencia artificial **dentro del producto que se construye**, no de la que lo construye |
| Fases, *sprints*, *releases*, producto mínimo viable | Formas legítimas **solo cuando el proyecto las adopta**. El núcleo dice que «no es una obligación del núcleo» |

---

# 7 · Qué queda fuera del inventario, y por qué

**Ocho disposiciones forman una conjunto sin objeto propio**: no se adhieren a un objeto porque se aplican a todos. Están declaradas en el inventario con su momento de actuación —la regla de detención antes de generar, el scorecard al valorar el conjunto, los antipatrones como señales, la gobernanza, la definición de terminado, el informe de lo que queda abierto, la guía de bolsillo y el índice operativo—.

Dos de ellas **no se compilan**, y conviene decir por qué:

- La **guía de bolsillo** es una lista de preguntas dirigida a una persona. No es ejecutable.
- El **índice operativo** explica cómo se citan los identificadores. No es una obligación.

---

# 8 · Decisiones humanas

## Ya resueltas

**Cuándo dos formulaciones distintas son la misma cosa.** Resuelto por la autoridad el 2026-09-22, a propósito de que el texto canónico dice «absorber complejidad, **no multiplicarla**» y la doctrina dice «absorber complejidad, **no producirla**». Son sinónimos: una sola tesis.

La regla que queda, para los casos que vuelvan a aparecer:

> Cuando el núcleo enuncia lo mismo dos veces con palabras distintas, es **reforzamiento y no contradicción** — salvo que las dos versiones cambien lo que hay que hacer.

Aplicada: «no multiplicarla» y «no producirla» son sinónimos porque la acción exigida es idéntica. Las dos tríadas del segundo principio **no** lo son, porque nombran términos distintos a incluir en los criterios de aceptación, y por eso siguen abajo. Las dos listas de estados tampoco, y se resolvieron aparte: enuncian objetos distintos.

**Cómo se citan las obligaciones sin identificador.** Resuelto por la autoridad el 2026-09-22.

Cuatro frases normativas del núcleo no tienen identificador. Dos resultaron ya cubiertas por disposiciones identificadas y no requieren nada:

| Frase sin dirección | Ya identificada en |
|---|---|
| «Cada elemento debe justificar la atención que consume» | *La atención es un recurso del producto* |
| «comprender dónde estamos, qué podemos hacer y qué ocurrirá después» | *Comprensión*, casi palabra por palabra |
| «La IA debe absorber complejidad, no producirla» | *La complejidad pertenece al sistema*, la instrucción «al implementar» y dos antipatrones |

Las dos restantes **se direccionan por su sección**: el mapa de identificadores les da dirección usando el encabezado que el propio documento ya tiene. No se toca el núcleo y no se inventa ningún concepto; la cita sigue siendo literal y verificada por el ensamblado.

| Frase | Por qué necesita dirección |
|---|---|
| «Cada uno debe ser capaz de cambiar una decisión, detener una implementación o exigir evidencia adicional» | Es el criterio con el que este método admite o rechaza un control |
| «Cada artefacto existe para responder una pregunta… si no cambia una decisión ni ayuda a verificarla, debe simplificarse o eliminarse» | El preset vigente ya la compiló, sin poder citarla |

**Contrapartida aceptada:** una dirección por encabezado es menos estable que un identificador. Si el núcleo se reorganiza, se rompe — y la comprobación de conformidad lo detecta, porque la cita literal deja de encontrarse. Eso es exactamente lo que debe ocurrir.

**Cuál formulación del segundo principio es la citable.** Resuelto por la autoridad el 2026-09-22.

El principio *La experiencia también es funcionalidad* está enunciado dos veces, y no coinciden:

| Dónde | Qué dice |
|---|---|
| Reglas de diseño del principio | «Incluir **esfuerzo, claridad y confianza** dentro de los **criterios de aceptación**» |
| Tabla de los diez compromisos | «Incluye **esfuerzo, emoción y fricción** en la **definición de calidad**» |

**Se cita la regla de diseño.** La tabla es una columna llamada «Consecuencia principal»: una síntesis. El cuerpo normativo de un principio son sus reglas de diseño, que es de donde se compila todo el resto del núcleo.

**No se pierde nada.** «Emoción» está cubierta por el campo *ansiedad* de la ficha de Job Story, donde ya está adherida la regla que manda considerar el estado emocional y cognitivo. «Fricción» está cubierta por la dimensión *Carga*. Lo que se decidió aquí es únicamente cuál de las dos frases se cita, no qué queda dentro del método.

No requiere modificar el núcleo.


**El reparto de disposiciones quedó resuelto.** Las siete asignaciones en duda se decidieron una por una; están registradas en la sección 9 con su razón.

## Pendientes

**Ninguna.** Las tres decisiones que esta propuesta requería están resueltas y ninguna exigió modificar el núcleo.

---

# 9 · Las siete asignaciones que estaban en duda, y cómo se resolvieron

Resueltas por la autoridad el 2026-09-22, una por una, con el texto del núcleo a la vista.

| Regla del núcleo | Queda en | Por qué |
|---|---|---|
| «Diferenciar con claridad recomendaciones, decisiones automáticas y resultados confirmados» | **Confianza** | Viene del principio *La confianza se diseña*, y «confirma resultados» aparece literalmente en esa dimensión. Un producto sin IA también debe distinguir una recomendación de un resultado confirmado |
| «Usar buenos valores predeterminados, siempre editables cuando la decisión importa» | **Profundidad** | Cubre las dos mitades de la regla: el predeterminado da la ruta clara al principiante, la editabilidad conserva la capacidad del avanzado. Control habla de acciones ya ejecutadas |
| «Considerar el estado emocional y cognitivo que acompaña la situación» | **Ficha de Job Story** | La ficha tiene un campo llamado «ansiedad», y la regla nombra la Job Story explícitamente |
| «Guardar trabajo, contexto y estado con una frecuencia proporcional» | **Estados** | Rendimiento habla solo de tiempo de respuesta y no menciona persistencia. Guardar el trabajo es lo que permite que interrupción y retorno mantengan contexto |
| «Mantener lenguaje, jerarquía y comportamiento consistentes» | **Comprensión** | El contrato de experiencia es dónde se declara; comprensión es lo que debe resultar cierto |
| «Traducir conceptos internos al lenguaje y al modelo mental de la persona» | **Comprensión** | Por simetría con la anterior. Viajó con ella su condición de detención: «la interfaz expone una complejidad interna que el sistema podría absorber» |

## 9.1 · El fundamento de producto y su mapa

El solapamiento que había señalado —siete de ocho disposiciones compartidos— **era un error mío de asignación, no evidencia de que fueran una sola cosa.** Repartidos correctamente, la tensión desaparece:

| | El fundamento de producto | Mapa del fundamento |
|---|---|---|
| Qué es | su definición y las formas que puede tomar | ¿qué construir, por qué y con qué autoridad? |
| Qué compromiso lo gobierna | identificar el fundamento y la fuente autorizada antes de diseñar | — |
| Qué exige antes de implementar | comprender la definición antes de proponer | — |
| Qué paso lo produce | — | comprender el fundamento, cuyo resultado es un **mapa fiel, sin reformularla** |
| Qué debe hacer el agente | — | identificar las fuentes, explicar el fundamento, confirmar el alcance |
| Qué debe informar | — | fuentes y fundamento que justifican el desarrollo |
| Cuándo detenerse | no existe un fundamento identificable | una ambigüedad material se está resolviendo sin autorización |

Ningún disposición se repite. Son **dos controles distintos**: uno pregunta *¿existe y es identificable?*, el otro *¿el mapa es fiel y completo?*

## 9.2 · Qué queda por revisar del reparto de disposiciones

Nada señalado. El reparto restante no presentó alternativas razonables al asignarlo. Si al usar el método aparece una asignación que estorba, se corrige en el generador y el inventario se regenera: **no hay nada escrito a mano que mantener sincronizado.**

---

## Nota sobre el alcance de esta propuesta

Este documento **no compila nada**. Establece sobre qué objetos se compilará y con qué granularidad. La compilación —cada objeto con sus citas literales verificadas por el ensamblado, según el formato que fija el anexo v2.0— viene después de que el reparto de disposiciones esté aprobado, porque compilar sobre un reparto equivocado multiplicaría el error por diecinueve.
