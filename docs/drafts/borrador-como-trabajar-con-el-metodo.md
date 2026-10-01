> **Borrador no aplicado.** Pertenece al [issue #9](https://github.com/dacunao/software-humano-speckit/issues/9) de la hoja de ruta y **no está autorizado como documentación del método**. Se guarda aquí para que no se pierda, no para que se siga. Lo que gobierna sigue siendo el núcleo, el anexo y las instrucciones.

# Cómo trabajar con el método · las tres formas y cuál te conviene

**Este documento no es doctrina ni instala nada.** Describe las tres formas de usar el método una vez instalado, qué exige cada una y qué pierdes con cada una, para que elijas según cómo trabajas y no según lo que parezca más riguroso.

**Ninguna es la correcta.** El método hace lo mismo en las tres; lo que cambia es quién decide que cada paso ocurra.

---

## En una tabla

| | **Conversar** | **Invocar** | **Workflow** |
|---|---|---|---|
| Cómo se dispara | Describes la situación; el agente reconoce el comando | Escribes `/speckit-plan` tú | El motor corre el ciclo entero |
| Dónde trabajas | En la conversación con tu agente | En la conversación con tu agente | En la terminal, con `specify` |
| Quién decide cuándo | El agente, según lo que pides | Tú | El workflow, con compuertas |
| Qué necesitas saber | Nada del método | Los ocho comandos y cuándo aplican | La terminal y el estado de una corrida |
| Riesgo principal | Que un comando nunca se dispare | Que olvides invocar uno | Que la corrida se pause y no sepas seguir |
| Estado hoy | Probado en un proyecto real | Probado en un proyecto real | **Ver la advertencia al final** |

---

## 1 · Conversar

Describes lo que necesitas en lenguaje natural. El agente reconoce cuál de los ocho comandos corresponde y lo invoca.

**No tienes que aprender ningún comando.** Los comandos del método conservan la descripción nativa de SpecKit, que nombra artefactos y momentos concretos, y por eso el agente reconoce la situación cuando la describes.

**Para quién es.** Para quien decide turno a turno, cambia de opinión a mitad de camino y quiere ver lo que se produce antes de seguir. Si no quieres lidiar con comandos, esta es tu forma.

**Qué exige de ti.** Estar en la conversación. El método funciona porque tú estás ahí decidiendo, no a pesar de eso.

**Qué pierdes.** Que un comando se dispare depende de que la conversación lo evoque. En el primer sitio construido con el método, `clarify` **no corrió nunca** — y estaba bien: cuando la autoridad está en la conversación, aclarar *es* la conversación. Pero lo aclarado se quedó en el chat y no llegó a `spec.md`.

**Cómo se compensa.** La comprobación de conformidad detecta que una fuente rectora cambió después que `spec.md` o `plan.md`, y detiene diciendo qué quedó atrás. No reconcilia: avisa.

**Evidencia.** Es la forma que usó el primer sitio. `workflow run` no se usó ni una vez, y aun así corrieron diez `analyze` y siete `converge`, elegidos por el agente turno a turno. Seis de los siete casos en que el método cambió una decisión salieron de ahí.

## 2 · Invocar

Escribes el comando tú: `/speckit-specify`, `/speckit-plan`, `/speckit-tasks`.

**Para quién es.** Para quien ya conoce el ciclo SDD y prefiere decidir explícitamente cuándo corre cada paso, en vez de confiar en que el agente lo reconozca. También para retomar un proyecto ajeno, donde no sabes qué se corrió y qué no.

**Qué exige de ti.** Conocer los ocho comandos y en qué momento aplica cada uno. El mapa está en el anexo.

**Qué pierdes.** Nada respecto de conversar, salvo la comodidad. Es la misma mecánica con el disparo en tus manos.

**Se mezcla con la anterior.** Nada impide conversar la mayor parte del tiempo e invocar explícitamente cuando quieres asegurarte. Es lo que la mayoría termina haciendo.

## 3 · Workflow

Ejecutas el ciclo completo desde la terminal:

```bash
specify workflow run software-humano
```

El motor corre los pasos en orden, **ejecuta el CLI de tu agente por cada uno**, y se detiene en cuatro compuertas que corresponden a los puntos de control que el manifiesto especifica. Un rechazo aborta la corrida.

**Para quién es.** Para integración continua, y para quien quiere el ciclo cerrado sin decidir paso a paso.

**Qué exige de ti.** La terminal. Y aceptar que **el agente corre fuera de tu conversación**: el motor lo lanza como subproceso, ves su salida al terminar cada paso, y no dialogas con él mientras trabaja.

**Qué ganas.** Las compuertas y la comprobación de conformidad las ejecuta el motor, no el agente. **El agente no puede saltárselas**, que es la diferencia real con las otras dos formas.

**Qué pierdes.** El ida y vuelta. Si a mitad de `plan` quieres cambiar el rumbo, no hay dónde decirlo hasta la siguiente compuerta.

> ### Advertencia · estado real de esta forma
>
> **El workflow se instala y su estructura es correcta, pero nunca se ejecutó de principio a fin en un proyecto real.** Los ensayos del paquete comprueban que queda instalado, no que corra.
>
> Y hay un defecto conocido: **sus compuertas solo preguntan si hay una terminal interactiva.** Si la entrada viene por tubería, en integración continua, o si un agente corre el workflow por ti, la corrida **se pausa y no puede reanudarse** — falta declarar `verdict_input` en las cuatro compuertas.
>
> Está registrado como [issue #8](https://github.com/dacunao/software-humano-speckit/issues/8) y en la hoja de ruta. **Hasta que se cierre, usa esta forma solo desde una terminal interactiva.**

---

## Cómo elegir

**Si no quieres aprender comandos** → conversar. Es la forma probada y la que menos te pide.

**Si ya conoces el ciclo SDD y quieres control del disparo** → invocar, mezclando con conversar cuando convenga.

**Si necesitas que nadie pueda saltarse una compuerta** —integración continua, o un equipo donde el rigor no puede depender de que alguien se acuerde— → workflow, leyendo antes la advertencia.

**Se puede cambiar de forma en cualquier momento.** Las tres están instaladas desde el principio y ninguna excluye a las otras. No hay que declarar cuál usas.

---

## Lo que ninguna de las tres te da

Las tres comprueban que lo que el manifiesto exige **esté presente y sea trazable**. Ninguna comprueba que el producto esté bien.

En el primer sitio, cuatro defectos de experiencia los encontró una persona usando el producto, y los cuatro habían pasado todas las comprobaciones. Los comandos revisan la coherencia entre artefactos y del código contra las tareas. **Ninguno mira la pantalla.**

Elijas la forma que elijas, esa parte sigue siendo tuya.
