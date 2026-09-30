**Español** · [English](README.md) · [Português (BR)](README.pt-BR.md)

# Software Humano para SpecKit

> Construimos herramientas para ampliar las capacidades de las personas, no para exhibir las capacidades del software.

Paquete de método que aplica el **Manifiesto de Software Humano** al ciclo de desarrollo guiado por especificación de [SpecKit](https://github.com/github/spec-kit), en cualquier proyecto.

**Manifiesto completo:** [manifiesto.softwarehumano.com](https://manifiesto.softwarehumano.com)

> **Sobre el idioma.** El manifiesto está publicado en inglés, español y portugués de Brasil en el sitio. **Este paquete —sus documentos, instrucciones, mensajes de las herramientas y comentarios— está escrito solo en español.** Si trabajas con un equipo que no lo lee, el manifiesto sí está traducido; el paquete no.

---

## El manifiesto

El **Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial**, de **Damián Acuña**, responde una pregunta:

> ¿Cómo construimos software que amplifique la capacidad de las personas para conseguir lo que buscan, **sin transferirles la complejidad de la tecnología**?

Construir un producto tiene un costo, y ese costo no desaparece: se reparte. Una parte la paga el equipo; la otra se la pasa a quien usa el producto, en atención, en aprendizaje y en decisiones que no vino a tomar. Ese traspaso casi nunca se decide.

De ahí se siguen sus afirmaciones menos habituales: que un producto sin errores puede fracasar por saturación, que la complejidad pertenece al sistema y no a la interfaz, y que la atención tiene presupuesto y se verifica como se verifica el rendimiento.

El texto completo está en [`docs/method/`](docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md) y en [el sitio](https://manifiesto.softwarehumano.com). Es la fuente de autoridad de todo lo demás.

## Para qué tipo de productos

El propio manifiesto declara su alcance:

> «El marco sirve para productos donde la experiencia de uso influye directamente en el resultado: **aplicaciones web y móviles, herramientas internas, sistemas de aprendizaje, servicios digitales, productos con agentes y soluciones asistidas por IA**. Está dirigido a product managers, diseñadores, desarrolladores y agentes de código que participan en decisiones de producto.»

Si la experiencia de uso no cambia el resultado de lo que construyes, este método te va a cobrar más de lo que te devuelve.

## Qué hace este paquete

Un manifiesto no se aplica solo. Un agente con la doctrina disponible puede omitirla sin que nada lo detenga, y sin que nadie lo note hasta que el producto ya está construido.

Este paquete pone las disposiciones del manifiesto **dentro de los comandos que el equipo ya ejecuta**, citando su texto literal, sin reformularlo. De 300 enunciados comprobables del núcleo, 210 están compilados; 40 quedan declarados fuera y 50 son editoriales.

No modifica SpecKit: usa cuatro de sus mecanismos de extensión documentados.

## Qué NO hace

**No es un sistema de diseño ni una guía visual.** No trae componentes, tipografías, paletas ni opiniones sobre cómo debe verse un producto. Fija criterios —accesibilidad, estados, carga, rendimiento, trazabilidad—, no estética. La dirección visual la decide el equipo.

**No comprueba que el producto esté bien.** Comprueba que lo que el manifiesto exige esté presente y sea trazable. Los comandos revisan la coherencia entre artefactos y del código contra las tareas; ninguno mira la pantalla. Si la experiencia cumple los principios lo juzga una persona usando el producto.

**El método no sustituye la prueba con personas: la vuelve exigible.**

## Empezar

Necesitas [SpecKit](https://github.com/github/spec-kit) `>=1.0.0,<2.0.0`, Python 3 con PyYAML, git y un agente de IA con integración de SpecKit.

```bash
# Descarga el paquete desde Releases y descomprímelo en tu proyecto
unzip software-humano-speckit-starter-vX.Y.Z.zip -d /tmp/sh
cp -R /tmp/sh/software-humano-speckit-starter-vX.Y.Z/. .

# Comprueba que llegó íntegro y que el entorno sirve
shasum -a 256 -c SHA256SUMS
tools/speckit/preflight.sh
```

Después completa la sección **Completar por proyecto** al final de `AGENTS.md` y entrega a tu agente el prompt de [`START_WITH_AI_AGENT.md`](package/START_WITH_AI_AGENT.md). El procedimiento verificable, paso a paso, está en [`instructions/01`](package/instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md).

> La instalación suele requerir **dos sesiones**: muchos agentes cargan su catálogo de comandos al iniciar, así que los recién instalados no existen hasta reabrir. Es lo esperado.

## Qué incluye

| Capa | Mecanismo de SpecKit | Qué aporta |
|---|---|---|
| Preset | `preset` | La doctrina dentro de los ocho comandos y las tres plantillas |
| Conformidad | `extension` | Comprueba que lo exigido esté presente, y detiene si falta sin declarar |
| Compuertas | `workflow` | Los puntos de control que el propio manifiesto especifica, ejecutados por el motor |
| Distribución | `bundle` | Compone y fija las tres anteriores |

Y la documentación: el núcleo, el anexo que traza cada disposición hasta SpecKit, la guía de implementación, las instrucciones de instalación y [`PARA_QUIEN_DECIDE.md`](package/PARA_QUIEN_DECIDE.md), escrito para quien aprueba y no para el agente.

## Dos modos, según cómo trabajes

**Comandos sueltos.** El agente invoca los comandos al reconocer la situación que cada uno nombra, desde lenguaje natural. Habilita la doctrina en los artefactos sin que nadie teclee nada; depende de que el agente reconozca el momento.

**Workflow.** Se ejecuta el ciclo completo de una vez. Habilita además las compuertas y la comprobación de conformidad, que ejecuta el motor y el agente no puede saltarse.

Ninguno es «el correcto». Quien trabaja conversando y decidiendo turno a turno se apoyará en el primero; quien quiere el ciclo cerrado, o lo corre en integración continua, en el segundo. Los dos están instalados y puedes alternarlos.

## Licencias

El paquete mezcla dos naturalezas, y la frontera se define por naturaleza y no por carpeta:

| Qué | Licencia |
|---|---|
| Preset, extensión, workflow, bundle, herramientas e instrucciones | [MIT](LICENSE) |
| Texto del núcleo del manifiesto, incluida su proyección como constitución | [CC BY 4.0](LICENSE-CONTENT) |

Qué archivo cae de qué lado está explicado en [`LICENSING.md`](LICENSING.md). Atribución sugerida para el texto:

> «Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1», de Damián Acuña, bajo licencia CC BY 4.0.

## Autoría

Manifiesto y método de **Damián Acuña**. El desarrollo del paquete se hizo con asistencia de Claude, bajo su autoría y decisión.

## Cómo se mantiene

`docs/proposals/` es el registro de mantenimiento: se agrega, no se reescribe. Cada propuesta distingue hecho observado, inferencia y decisión humana requerida, y ninguna se aplica sin decisión de la autoridad de producto.

El método se valida sobre proyectos reales, y sus hallazgos se evalúan aquí antes de cambiar nada.
