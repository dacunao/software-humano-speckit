# Para quien decide

**Este es el único documento del paquete escrito para vos y no para el agente.** Es corto a propósito.

## Por qué existe

El método traduce el manifiesto a comprobaciones que el agente debe cumplir: setenta y nueve, repartidas en los ocho comandos. Todo lo que se podía volver verificable, se volvió verificable.

Lo que no se pudo **aterrizó en vos**. Y hasta ahora ningún documento te lo decía.

Un método que transfiere obligaciones a alguien que no sabe que las tiene no las transfirió: las perdió. Esto lo corrige.

## Lo que NO es tuyo

Para que esto no se convierta en vigilancia permanente, conviene empezar por lo que el método ya absorbió:

- **No** tenés que recordar qué principios aplican en cada momento. Cada comando los nombra.
- **No** tenés que verificar la cobertura. La matriz existe o no existe.
- **No** tenés que comprobar que la doctrina esté en los artefactos. `analyze` lo hace.
- **No** tenés que conocer las setenta y nueve comprobaciones. Son del agente.

Tu trabajo es más chico que todo eso. Son cuatro momentos.

---

## Los cuatro momentos

### 1 · Cuando te presenta una propuesta

Una dirección de diseño, una arquitectura, una alternativa técnica.

**Lo que puede fallar:** que te la traiga sin haber consultado la doctrina que la gobierna. Ocurrió en el primer piloto: dos direcciones visuales presentadas sin mirar los principios que las descartaban.

### 2 · Cuando te abre una decisión

Te pregunta algo y espera que elijas.

**Lo que puede fallar:** que la respuesta ya esté escrita en el manifiesto o en tu propio fundamento de producto. También ocurrió. Una pregunta cuya respuesta ya existe no es deferencia: te traslada un trabajo que no es tuyo.

### 3 · Cuando declara algo terminado

Un bloque, una tarea, una entrega.

**Lo que puede fallar:** que confunda «las comprobaciones pasaron» con «el producto sirve». Son cosas distintas y el método las separa; el informe tiene que separarlas también.

### 4 · Cuando toca decidir si se prueba con personas

**Esto no lo puede hacer ningún agente.** Es el único punto donde no hay nada que delegar.

Si el producto nunca se prueba con personas reales, el método puede estar en verde y el producto puede no servirle a nadie. Ninguna comprobación cubre esa distancia.

---

## Cómo se ve una respuesta hueca

Esta es la parte que hace accionable el momento 3, y se aprende con ejemplos.

**La prueba es una sola pregunta: ¿puedo saber si se cumplió mirando algo?**

| Hueca | Real |
|---|---|
| «Se respetará `P07`» | «Toda acción irreversible declara su consecuencia antes de ejecutarse» |
| «El diseño será simple» | «Ninguna ruta termina sin una acción siguiente disponible» |
| «Se cuidará la carga cognitiva» | «Cada elemento visible traza a un requisito; sin traza, se elimina» |
| «Se considerará la accesibilidad» | «Los recorridos principales pasan revisión por teclado y lector de pantalla, con la salida archivada» |
| «Se harán las pruebas necesarias» | «Ocho casos negativos comprueban que cada regla detiene el build» |

La columna izquierda **repite el enunciado**. La derecha **dice qué va a pasar**.

Una consecuencia hueca pasa cualquier comprobación automática: la celda no está vacía. Que diga algo, solo lo verificás vos.

---

## Las cinco preguntas

No tenés que recordar la doctrina. Tenés que recordar cinco preguntas. Cada una activa una comprobación que ya existe.

| Cuándo | Qué preguntás |
|---|---|
| Te presenta una propuesta | **¿Qué puntuación de `SH-SCORE` le diste antes de traérmela?** |
| Te abre una decisión | **¿Qué fuente consultaste para confirmar que no está ya resuelta?** |
| Te muestra un plan | **Mostrame la Comprobación de constitución.** |
| Una fila te suena vacía | **Esa consecuencia repite el enunciado. Reescribila.** |
| Declara algo terminado | **¿Qué quedó verificado por comprobación y qué espera verificación humana?** |

Si el agente no puede responder alguna, esa es la señal. No hace falta que sepas por qué.

---

## Las dos cosas que nadie puede hacer por vos

**No aprobar un gate que una comprobación rechazó porque tenés prisa.** El método puede detectar el problema y señalártelo. No puede impedirte que lo pases por alto.

**Correr las pruebas con personas.** Es la mitad del método que mide si el producto sirve, y la única que no se automatiza.

---

## Un dato que conviene conocer

En el primer piloto real hubo tres fallos de juicio. **Uno de ellos ya tenía su regla escrita** en las instrucciones del agente, y no sirvió: la regla estaba y se ignoró.

No se cuenta como advertencia moral. Se cuenta porque explica para qué sirve este documento: **ninguna cantidad de reglas reemplaza a alguien leyendo lo que tiene delante.** Lo que las reglas hacen es volver ese trabajo pequeño y ubicable, en lugar de continuo y difuso.

---

## Este documento debe seguir siendo corto

Si crece, deja de leerse — y entonces vuelve a no tener dueño lo que describe.

Antes de agregarle algo, comprobá que no pertenezca a `AGENTS.md`, que es donde van las reglas del agente. Aquí solo va lo que **no se puede delegar**.
