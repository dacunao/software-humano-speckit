# Compuertas del método

**Generado por** `tools/method/compilar-compuertas.py` desde `SH-GOV § Puntos de control`. **No se edita a mano.**

El manifiesto especifica seis momentos con su decisión requerida. **Ninguna compuerta se diseña: se cita.**

| Qué pone la adaptación | Qué pone el manifiesto |
|---|---|
| Dónde cae cada momento en el flujo de SpecKit, y qué objetos se comprueban ahí | El momento y su decisión requerida, literal |

---


## Antes de diseñar

> **Decisión requerida.** Fuentes, autoridad, alcance, resultados, evidencia, supuestos y no objetivos están claros; las Job Stories se comprenden cuando existen.

*Cita de `SH-GOV § Puntos de control`, literal.*

**Dónde cae en SpecKit:** después de `specify` y `clarify`, antes de `plan`

**Objetos que se comprueban:** El fundamento de producto · Mapa del fundamento · Ficha de Job Story cuando aplique


## Antes de generar código

> **Decisión requerida.** El plan cubre la definición completa y establece dependencias, respuesta elegida, rutas, estados, reglas críticas, riesgos y aceptación.

*Cita de `SH-GOV § Puntos de control`, literal.*

**Dónde cae en SpecKit:** después de `tasks` y `analyze`, antes de `implement`

**Objetos que se comprueban:** Cobertura · Modelo de estados · IA · Registro de decisiones · Plan de aceptación


## Durante la construcción

> **Decisión requerida.** La descomposición organiza el trabajo sin alterar el alcance; bloqueos, pendientes y excepciones permanecen visibles.

*Cita de `SH-GOV § Puntos de control`, literal.*

**Dónde cae en SpecKit:** dentro de `implement`, entre bloques

**Objetos que se comprueban:** Cobertura · Estados · Confianza · Control


## Antes de integrar

> **Decisión requerida.** Cada cambio conserva trazabilidad con su fundamento, respeta alcance, cubre estados y pasa pruebas técnicas.

*Cita de `SH-GOV § Puntos de control`, literal.*

**Dónde cae en SpecKit:** `analyze`, antes de incorporar el cambio

**Objetos que se comprueban:** Cobertura · Estados · Carga


## Antes de liberar

> **Decisión requerida.** La implementación completa demuestra resultados, cobertura, comprensión, control y calidad de experiencia.

*Cita de `SH-GOV § Puntos de control`, literal.*

**Dónde cae en SpecKit:** `converge`, antes de declarar terminado

**Objetos que se comprueban:** Plan de aceptación · Progreso · Comprensión · Control · las doce dimensiones


## Después de liberar

> **Decisión requerida.** Se observan resultado, fricción, abandono y errores; se revisan el fundamento, las historias y sus supuestos cuando corresponda.

*Cita de `SH-GOV § Puntos de control`, literal.*

**Dónde cae en SpecKit:** **fuera del flujo de SpecKit**: no hay operación nativa que lo cubra

**Objetos que se comprueban:** Progreso · Causalidad · Carga


---

## Lo que esta compilación deja visto

**El último momento no tiene operación nativa.** El manifiesto exige observar resultado, fricción, abandono y errores después de liberar, y revisar el fundamento y sus supuestos cuando corresponda. El flujo de SpecKit termina antes. Es una brecha de la herramienta, no del método, y queda declarada en lugar de resolverse en silencio.

**La adaptación no elige cuántas compuertas hay.** Son seis porque el manifiesto escribe seis.

