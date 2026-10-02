**Español** · [English](ROADMAP.md) · [Português (BR)](ROADMAP.pt-BR.md)

# Hoja de ruta

Lo que sabemos que falta, a la vista. Cada tema tiene su issue para discutirlo y, cuando corresponde, la propuesta donde está analizado.

Esta lista **no promete fechas**. Ninguno de sus temas está comprometido: están identificados, medidos y abiertos.

Se publica por la misma razón que el método existe. La definición de terminado del manifiesto admite dos estados y no más: cumplido con evidencia verificable, **o** excepción explícita y aprobada. Esta hoja de ruta es lo segundo. Esconderla sería incumplir la doctrina en el repositorio que la distribuye.

---

## Abierto

| Tema | Por qué importa | Dónde |
|---|---|---|
| **El paquete reclama la raíz del proyecto** | Instalar el método deja siete archivos suyos en la raíz ajena, y uno de ellos —`LICENSE`— sigue fijado por la verificación de integridad | [#1](https://github.com/dacunao/software-humano-speckit/issues/1) · [propuesta 011](docs/proposals/011-el-paquete-reclama-la-raiz-del-proyecto.md) |
| **Costo de ejecución** | Una invocación de `plan` carga ~36.500 tokens de método antes de tocar el proyecto. Dos tercios son la constitución, y nunca se optimizó | [#2](https://github.com/dacunao/software-humano-speckit/issues/2) · [análisis 007](docs/proposals/007-analisis-de-costo-de-ejecucion-del-metodo.md) |
| **Editar el archivo que lee el agente no se detecta** | Es la cuarta de cuatro vías por las que el método puede quedar sin efecto. Las otras tres están cerradas | [#3](https://github.com/dacunao/software-humano-speckit/issues/3) · [propuesta 010](docs/proposals/010-evaluacion-del-piloto-del-sitio.md) |
| **Las compuertas del workflow no se pueden reanudar** | Sin terminal —integración continua, o un agente corriéndolo por ti— la corrida pausa y no hay forma de darle la decisión | [#8](https://github.com/dacunao/software-humano-speckit/issues/8) |
| **El bundle no se puede instalar** | El catálogo comunitario de SpecKit es solo de descubrimiento: estar listado no habilita instalar por nombre. Y el bundle no está en ningún catálogo. La cuarta capa existe y no funciona | [#4](https://github.com/dacunao/software-humano-speckit/issues/4) |
| **La entrada del catálogo fija una versión y nada la actualiza** | Cada versión nueva de un componente deja al catálogo de SpecKit apuntando a la anterior, y corregirlo exige reenviar el formulario completo | [#10](https://github.com/dacunao/software-humano-speckit/issues/10) |
| **Ningún comando propaga un cambio del fundamento** | En el primer sitio, el fundamento cambió seis veces y la especificación y el plan se rehicieron a mano las seis | [#5](https://github.com/dacunao/software-humano-speckit/issues/5) · [propuesta 010](docs/proposals/010-evaluacion-del-piloto-del-sitio.md) |
| **El paquete existe solo en español** | Es deliberado —la doctrina tiene su autoridad en español— y es un límite real de adopción | [#6](https://github.com/dacunao/software-humano-speckit/issues/6) |
| **La comprobación de entorno y el atajo no prueban los mismos intérpretes** | El entorno puede quedar aprobado con un aviso en una máquina donde el atajo después falla; en Mac Intel es el caso normal | [#11](https://github.com/dacunao/software-humano-speckit/issues/11) |
| **El atajo depende de un Python del sistema** | Hoy el único que trae PyYAML es el de Apple, y que siga trayéndola no lo garantiza nada del paquete | [#12](https://github.com/dacunao/software-humano-speckit/issues/12) |
| **Falta una guía de inicio rápido** | El método admite tres formas de trabajar —conversar, invocar, workflow— y nada le dice a quien llega cuál le conviene según su estilo | [#9](https://github.com/dacunao/software-humano-speckit/issues/9) |

## Cómo se decide qué entra

Un tema entra a esta lista cuando **algo lo midió**: un piloto, un ensayo, o un análisis con su evidencia. No entra por parecer una buena idea.

Y sale de la lista cuando se aplica **con decisión de la autoridad de producto**. El registro de cada decisión vive en [`docs/proposals/`](docs/proposals/), que se agrega y no se reescribe.

## Cómo participar

Los [issues](https://github.com/dacunao/software-humano-speckit/issues) están abiertos. Si usas el método y algo te estorba, cuéntalo ahí: **lo que se mide entra a esta lista.**

Los cuatro temas que más dicen del método salieron de un proyecto real usándolo, no de planificarlo.
