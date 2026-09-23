# Fundamento de producto · Paquete de método Software Humano para SpecKit

**Autorizado por Damián Acuña el 2026-09-23.**

Es el fundamento de producto del paquete de método, en el sentido de `SH-FUND`. Toda modificación exige su decisión.

Este documento **no redacta decisiones nuevas**. Reúne las que ya fueron tomadas y están dispersas en instrucciones, decisiones registradas y propuestas, y las ordena según los cinco elementos que `SH-FUND` exige. Cada sección declara de dónde viene su contenido, para que pueda verificarse que nada fue inventado.

**Por qué existe.** El manifiesto declara su propio alcance: *«El marco sirve para productos donde la experiencia de uso influye directamente en el resultado: aplicaciones web y móviles, **herramientas internas**, sistemas de aprendizaje, servicios digitales, **productos con agentes** y soluciones asistidas por IA. Está dirigido a product managers, diseñadores, desarrolladores **y agentes de código**.»*

Este paquete es una herramienta interna, es un producto con agentes y se dirige a agentes de código. **Está dentro del alcance del manifiesto**, y por lo tanto su desarrollo se gobierna por él. Sin este documento estaría activa `STOP01`.

---

## 1 · Fuente y autoridad

> *¿De dónde proviene y quién puede modificarlo?* · Condición mínima: origen trazable y autoridad reconocida.

**Autoridad de producto:** Damián Acuña. Es quien puede modificar este documento y quien autoriza toda decisión que cambie alcance, reglas, licencias o publicación.

**Origen del contenido:** el *Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1*, del mismo autor, y las decisiones registradas en `docs/proposals/001` a `009`.

**Lo que este documento no gobierna:** la doctrina. El núcleo la gobierna, y este fundamento se subordina a él. Si alguna vez se contradicen, manda el núcleo.

*De dónde viene: `AGENTS.md`, sección de autoridad; propuestas 001–009.*

---

## 2 · Razón

> *¿Qué situación, necesidad, problema u oportunidad aborda?* · Condición mínima: justificación comprensible sin depender de la solución.

El problema de fondo no es de método. Lo enuncia el manifiesto:

> «¿Cómo construimos software que amplifique la capacidad de las personas para conseguir lo que buscan, sin transferirles la complejidad de la tecnología?»

Y se agravó con la IA: construir se abarató, la abundancia no garantiza un mejor producto, y **una decisión débil ahora se convierte en mucho código correcto**.

Frente a eso, la cadena de razones que llega hasta este paquete tiene tres eslabones:

1. **Una doctrina resuelve qué merece construirse y cómo debe sentirse.** El manifiesto la establece.
2. **Pero un manifiesto no se aplica solo.** Un agente de código con la doctrina disponible puede omitirla sin que nada lo detenga, y sin que nadie lo note hasta que el producto ya está construido.
3. **Y un método sin mecanismos de cumplimiento tampoco la aplica**: reproduce el mismo problema un nivel más abajo.

Este paquete existe por el eslabón segundo y tercero. **No existe por sí mismo: existe porque sin él la doctrina no llega al software.**

Eso no es una hipótesis. El piloto real —el sitio del manifiesto— lo produjo con el método instalado y verificado:

- tres fallos de juicio, **uno de ellos con su regla ya escrita** en las instrucciones del agente;
- el agente dejó de invocar los comandos del método y trabajó fuera de ellos;
- solo dos fallos, en todo el ejercicio, fueron evitados por una comprobación del método.

La formulación corta, de la autoridad:

> «Un manifiesto sin método es declaración de intenciones. Un método sin mecanismos de cumplimiento es documentación. Y un método que exige disciplina heroica es un método incompleto: **la disciplina debe ser el residuo, no el combustible**.»

*De dónde viene: instrucción de la autoridad; registro del piloto; propuestas 003 y 006.*

---

## 3 · Resultado

> *¿Qué cambio o progreso debe producir?* · Condición mínima: resultado reconocible para las personas o para el producto.

### El fin

**Mejor software. Software humano.** El manifiesto fija su propia unidad de medida:

> «Su **unidad de medida no es la cantidad de funcionalidades entregadas**. Es el **progreso que una persona puede lograr con claridad, confianza y control**.»

Y declara por qué importa ahora:

> «El software gana capacidad con rapidez. La inteligencia artificial acelera todavía más ese proceso: hoy resulta barato generar pantallas, opciones, automatizaciones y capas de abstracción. **Esa abundancia no garantiza un mejor producto.** También permite convertir una decisión débil en mucho código correcto y una idea innecesaria en una funcionalidad terminada.»

Las barreras para programar se derrumbaron. Eso no produjo mejor software: produjo más software. **El fin de este paquete es que una persona, frente a lo que se construye con él, progrese con claridad, confianza y control.**

### Los medios

Todo lo que este paquete produce está subordinado a ese fin y no lo sustituye:

1. Que el método se instale en cualquier proyecto y opere sin intervención de quien lo construyó.
2. Que el agente aplique la doctrina sin depender de recordarla, y que el incumplimiento se detecte solo.
3. Que el método adaptado adhiera al manifiesto de forma inequívoca y verificable.
4. Que los equipos lo adopten.
5. Que un repositorio que nació sin conocer el manifiesto pueda reconvertirse y converger gradualmente.

### La consecuencia operativa de esta distinción

**Un medio alcanzado sin el fin es un fracaso, no un éxito parcial.**

Un método fielmente compilado que nadie usa no cumple. Un método ampliamente adoptado que produce el mismo software de antes tampoco cumple. Una cobertura del cien por ciento del manifiesto, si el producto resultante no deja a la persona progresar con claridad, confianza y control, **no cumple**.

Ninguno de los cinco medios puede presentarse como evidencia del fin.

*De dónde viene: el manifiesto, §Propósito del documento; corrección de la autoridad del 2026-09-22.*

---

## 4 · Condiciones y límites

> *¿Qué reglas, restricciones y exclusiones deben respetarse?* · Condición mínima: límites suficientes para evitar decisiones silenciosas.

### Sobre la doctrina

- **El manifiesto es la única fuente de verdad.** Nada entra al método que no trace al manifiesto, o a una necesidad técnica de SpecKit declarada como tal.
- **Ninguna disposición se reformula: se cita literalmente.** No hay campo de redacción propia. Una paráfrasis es un texto nuevo que nada puede contrastar con la fuente.
- **Las obligaciones se adhieren a cosas que el manifiesto nombra; no crean cosas nuevas.**
- **El núcleo no se modifica** para acomodar la adaptación.

### Sobre SpecKit

- **Apego estricto a las guías oficiales** de SpecKit para presets, extensiones, workflows y bundles.
- **Solo mecanismos nativos.** No se sustituye ni se modifica el core.
- **Lo nativo se conserva y se comprueba que se conservó**: metadatos, handoffs, tokens de invocación, secciones que los comandos localizan por su nombre.
- **El checklist nativo de requisitos se conserva sin intervención.**

### Sobre el uso

- **Dos modos legítimos**: bajo workflow, y por comandos sueltos. El workflow es el camino recomendado, **no un requisito**: un método que solo corre bajo workflow excluye a quien no lo usa, y la adopción es el objetivo.
- **No ser obstáculo para un repositorio que ya existía.** El método no rechaza lo incompleto; rechaza lo que falta sin que nadie lo sepa.

### Sobre la distribución

- **Licencias por naturaleza y no por carpeta**: MIT para preset, herramientas, instrucciones y anexo; CC BY 4.0 para el texto del núcleo y su proyección.
- **Versionado semántico independiente** para paquete, preset, núcleo y anexo.
- **La integridad se verifica**: un paquete cuya comprobación no pasa no es distribuible.

### No objetivos

- **No es un framework sustituto de SpecKit.** Es un complemento nativo.
- **No agrega etapas, artefactos ni controles metodológicos** al flujo del núcleo.
- **La cobertura del manifiesto no es un fin en sí.** Entra al método lo que puede cambiar una decisión, detener una implementación o exigir evidencia — criterio del propio manifiesto.
- **El sitio del manifiesto no es el producto.** Es el piloto que pone a prueba el método.

*De dónde viene: instrucciones de la autoridad; `AGENTS.md`, decisiones técnicas aprobadas; propuestas 004, 008 y 009; anexo v2.0.*

---

## 5 · Evidencia

> *¿Cómo sabremos que se cumplió?* · Condición mínima: criterios, observaciones o pruebas proporcionales al riesgo.

La distinción entre fin y medios se traslada a la evidencia: se miden en objetos distintos y en momentos distintos.

### Evidencia del fin · se mide sobre el producto construido

Las **doce dimensiones de verificación** del núcleo y las pruebas moderadas con personas. Se aplican al software que alguien construya con este método, no al paquete, y por lo tanto **solo pueden obtenerse una vez que exista ese software**.

Lo que este fundamento fija es que **esa es la evidencia que cuenta**, y que ninguna otra la sustituye.

### Evidencia de los medios · se mide sobre el paquete

| Medio | Con qué se demuestra |
|---|---|
| El método refleja el manifiesto | Comprobación de conformidad: toda cita aparece literalmente en su dirección |
| Nada del manifiesto quedó fuera sin declararlo | Mapa de cobertura |
| Lo nativo de SpecKit se conservó | Comprobaciones de metadatos, tokens y contratos de plantilla |
| El paquete se instala y opera | Instalación de prueba y verificación |
| Los equipos lo adoptan | Registro de proyectos que lo instalan y lo ejecutan |

### La trampa que esta distinción evita

Medir solo los medios **invita a optimizarlos**. Es barato subir la cobertura y declarar fidelidad, y ambas producen números que suben mientras el fin queda sin tocar.

Por eso ningún informe de este paquete puede presentar fidelidad o adopción como evidencia de que el software resultante es mejor. **Son evidencia de que el método está bien construido, no de que sirve.**

---

## Identificadores que deben preservarse

Los del núcleo, porque son el contenido que el paquete distribuye y las direcciones que citan el preset, el anexo y las instrucciones: las quince familias declaradas en `SH-INDEX`, más las direcciones por sección de los pasajes normativos sin identificador.

---

## Decisiones resueltas

### Qué se descompone del núcleo, y qué no · 2026-09-23

Seis bloques del núcleo son extensos y hasta ahora contaban como una unidad cada uno. El criterio para descomponerlos es el del propio manifiesto: **entra lo que puede cambiar una decisión, detener una implementación o exigir evidencia.** La cobertura no es razón suficiente.

| Bloque | Se descompone | Razón |
|---|---|---|
| Fundamento de producto | **Sí, casi entero** | Identificabilidad, alcance y autoridad, relación entre niveles, evidencia mínima de la historia, pruebas de calidad antes de diseñar y cadena de trazabilidad son controles |
| Regla de detención | **Sí** | Sus preguntas son la compuerta previa a generar |
| Antipatrones | **Sí** | Cada uno es una señal con su respuesta |
| Gobernanza | **Parcial** | Responsabilidades y puntos de control, sí. **El control de cambios de las versiones 2.0 y 2.1, no**: es historia del manifiesto |
| Scorecard de decisión | **Sí**, con destino acotado | Criterio de salida: actúa al liberar, no en cada comando |
| Guía de bolsillo | **No** | Son preguntas para una persona; su destino es el documento de quien decide |

**Hallazgo que esta decisión hace disponible.** `Gobernanza § Puntos de control` especifica seis momentos con su decisión requerida —antes de diseñar, antes de generar código, durante la construcción, antes de integrar, antes de liberar, después de liberar—. **Es la secuencia de compuertas del método, escrita por el manifiesto.** Ninguna compuerta se diseña: se cita.

### El piloto se reinicia desde cero · 2026-09-23

El piloto actual está contaminado: se le aplicaron cambios sobre la marcha mientras el método se corregía, de modo que no puede distinguirse qué resultado produjo el método y qué produjo la intervención.

**Se reinicia desde cero bajo la versión 2.0.** Podrán rescatarse prototipos y elementos equivalentes, pero no su registro como evidencia.

Consecuencia para la sección 5: la evidencia del fin se obtendrá sobre el piloto reiniciado, no sobre el actual.

---

## Decisiones abiertas

Ninguna. Las dos que quedaban se resolvieron el 2026-09-23.

---

## Lo que este documento no hace

No declara la doctrina; la cita. No sustituye al núcleo ni al anexo, que conservan su autoridad sobre el método y sobre su correspondencia con SpecKit. Si alguna vez se contradicen, manda el núcleo.
