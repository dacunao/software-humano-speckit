# Propuesta 011 — El paquete reclama la raíz del proyecto que lo instala

**Fecha:** 2026-09-30 · **reescrita el mismo día**
**Estado:** propuesta para revisión y aprobación de Damián Acuña. **Nada aplicado.**
**Objeto:** dónde deben vivir los archivos que el método instala
**Origen:** observado por la sesión del sitio al resolver su propio README; medido en `website-software-humano`

> **Por qué se reescribió.** La primera versión ofrecía cuatro opciones y recomendaba una de compromiso, que dejaba `SHA256SUMS` en la raíz «porque debe ejecutarse desde ahí». Damián preguntó cuál era el deber ser, y al responderlo quedó claro que esa razón era falsa: `shasum -c metodo/SHA256SUMS` funciona igual. Era comodidad presentada como requisito técnico. Esta versión parte del criterio y no del catálogo de opciones.

---

# 1 · El hecho

Instalar el paquete es copiar su contenido sobre la raíz del proyecto. Hoy quedan ahí seis archivos del método, más `SHA256SUMS`:

```
CLAUDE.md   LICENSE   LICENSE-CONTENT   LICENSING.md
PARA_QUIEN_DECIDE.md   START_WITH_AI_AGENT.md   SHA256SUMS
```

Hasta la versión 2.2.3, `SHA256SUMS` fijaba además el `README.md`, de modo que un proyecto que pusiera el suyo veía fallar su verificación de integridad. Eso ya se corrigió; `LICENSE` sigue fijado.

**Cómo se manifestó.** En `website-software-humano` los archivos entraron sobre un directorio vacío: no sobrescribieron nada, llenaron un vacío, y nadie los reemplazó. El repositorio del sitio quedó con un `README.md` que describe el paquete de método y con las licencias del método, mientras su propio fundamento declara en `§29.5` una exclusión —los nombres «Software Humano» y «Manifiesto» y el logotipo— que esos archivos no mencionan. La sesión del sitio lo resolvió poniendo su README en `.github/README.md`. Funciona, y es el rodeo a un defecto del paquete.

En un repositorio que ya existe, los mismos archivos sobrescribirían los del proyecto.

---

# 2 · El criterio

**La raíz de un repositorio pertenece al proyecto.** Es donde declara quién es: su nombre, su README, su licencia. Un paquete que se instala ahí es un huésped.

De ahí la regla:

> **Todo lo que trae el método vive bajo un directorio que el método posee. En la raíz queda solo lo que el proyecto va a editar y a considerar suyo.**

## 2.1 · Qué queda en la raíz, y por qué

`AGENTS.md` y `CLAUDE.md`, y **no porque sean del método**. Son archivos de configuración **del proyecto** que el método siembra, como un `.editorconfig` o un `tsconfig.json`: el proyecto los completa y son suyos desde ese momento. Los agentes los cargan desde la raíz por convención del ecosistema, no por decisión nuestra.

Todo lo demás entra al directorio del método. **Incluido `SHA256SUMS`**: las rutas de adentro se ajustan y se verifica con `shasum -a 256 -c <directorio>/SHA256SUMS` desde la raíz.

## 2.2 · La prueba que verifica el criterio

**¿Se puede describir cómo se desinstala el método?**

Con la regla: borrar su directorio, y revertir `AGENTS.md` y `CLAUDE.md` si se quiere. Dos frases.

Hoy: no se puede. Hay siete archivos del método mezclados con los del proyecto en la raíz y ninguna lista dice cuáles son. **Un paquete cuya remoción no se puede describir no definió su frontera: la ocupó.**

## 2.3 · Dónde lo ancla el manifiesto

`P03` — *«La complejidad pertenece al sistema»*. Un paquete que esparce sus archivos por la raíz ajena le transfiere a la persona el trabajo de saber cuál archivo es de quién. *Inferencia mía:* es la misma carga que el manifiesto se propone no transferir, cometida por el paquete que lo distribuye.

`P10` — *«La persona conserva control y propiedad»*. No hay forma más literal de propiedad que la raíz del propio repositorio.

`STOP03` — detenerse cuando *«se pretende omitir, modificar o postergar una parte sin una decisión autorizada»*. Sobrescribir archivos de alguien sin decírselo cae ahí, y el método lo hizo durante cuatro versiones sin que ninguna comprobación lo señalara.

---

# 3 · Qué cambia

## 3.1 · Los archivos

| Hoy, en la raíz | Después |
|---|---|
| `AGENTS.md` | se queda — es del proyecto |
| `CLAUDE.md` | se queda — es del proyecto |
| `README.md` | **el paquete deja de traerlo** |
| `LICENSE` | **el paquete deja de traerlo** |
| `LICENSE-CONTENT`, `LICENSING.md` | al directorio del método |
| `PARA_QUIEN_DECIDE.md`, `START_WITH_AI_AGENT.md` | al directorio del método |
| `SHA256SUMS` | al directorio del método |
| `docs/method/`, `instructions/`, `tools/speckit/` | al directorio del método |

El método deja de traer `README.md` y `LICENSE` **porque son del proyecto**, no porque estorben. Su propia licencia viaja con sus archivos, que es lo que MIT exige, y el proyecto declara la suya donde corresponde.

## 3.2 · La instalación avisa antes de escribir

La instrucción 01 gana un paso que **lista qué archivos va a crear o sobrescribir y se detiene** hasta que la persona confirme.

En la primera versión de esta propuesta pospuse esto para «cuando haya un segundo proyecto real». Con el criterio del punto 2 deja de ser un extra: si el método solo escribe en su directorio y en dos archivos de configuración, la lista es corta y avisar cuesta casi nada. Y es lo que `P10` y `STOP03` piden.

## 3.3 · El costo, medido

Diecisiete referencias a reescribir, repartidas así:

| Archivo | Referencias |
|---|---:|
| `START_WITH_AI_AGENT.md` | 5 |
| `CLAUDE.md` | 4 |
| `LICENSE` | 3 |
| `LICENSE-CONTENT` | 2 |
| `PARA_QUIEN_DECIDE.md` | 2 |
| `LICENSING.md` | 1 |

Más las rutas de `SHA256SUMS`, el ensamblado y los dos ensayos. **Es media tarde de trabajo**, no una refactorización. La primera versión de esta propuesta decía que no lo había medido; medido, es barato.

---

# 4 · Decisión requerida

**`D-011-1` — ¿Se adopta el criterio del punto 2?**

Si la respuesta es sí, quedan dos cosas por decidir que no propongo resueltas:

- **Cómo se llama el directorio.** `docs/method/` ya existe y contiene el núcleo y el anexo, pero mezclaría doctrina con operación y con herramientas. Un directorio nuevo separa mejor y agrega uno a la raíz. *Inclinación mía, sin datos que la respalden:* un directorio nuevo, porque lo que entra no es solo documentación.
- **Qué versión.** Mover archivos rompe toda ruta escrita en un proyecto instalado. *Inferencia mía:* es un cambio mayor, **3.0.0**.

---

# 5 · Cuándo

**No ahora.** Decisión de Damián Acuña del 2026-09-30: el paquete se publica tal como está, sin cambio estructural, y esta propuesta entra al roadmap público.

La razón es buena y conviene dejarla escrita: **el problema todavía no lo sufrió nadie.** El único proyecto instalado nació vacío, así que el caso grave —sobrescribir el README o la licencia de un repositorio existente— sigue siendo una inferencia sobre lo que haría el instalador, no algo observado. Cambiar la forma del paquete antes de que un adoptante real choque con ella es adivinar la forma correcta sin evidencia, y esa evidencia va a llegar sola.

---

# 6 · Lo que esta propuesta no establece

- **No hay evidencia de daño.** Ningún proyecto perdió un archivo por esto.
- **No resuelve la actualización.** Un proyecto instalado con 2.x que pase a una versión que mueve los archivos se encontrará con los viejos en la raíz y los nuevos en el directorio. Qué hace el método con eso es parte de `D-011-1` y no está pensado.
- **No mide el efecto sobre quien ya escribió rutas.** El sitio tiene rutas al método en su documentación; habría que avisarle, y eso es `DP-02`.
