# Propuesta 011 — El paquete reclama archivos que pertenecen al proyecto que lo instala

**Fecha:** 2026-09-30
**Estado:** propuesta para revisión y aprobación de Damián Acuña. **Nada aplicado.**
**Objeto:** qué archivos deja el paquete en la raíz del proyecto, y cuáles no le corresponden
**Origen:** observado por la sesión del sitio al resolver su propio README; medido en `website-software-humano`

---

# 1 · El hecho

Instalar el paquete es copiar su contenido sobre la raíz del proyecto. Entre lo que llega hay archivos que **son del método** y archivos que **son del proyecto**:

| Archivo | ¿De quién es? |
|---|---|
| `AGENTS.md` | del método, con una sección que cada proyecto completa |
| `CLAUDE.md` | del método |
| `PARA_QUIEN_DECIDE.md` | del método |
| `START_WITH_AI_AGENT.md` | del método |
| `LICENSING.md` | del método |
| `LICENSE-CONTENT` | del método |
| `SHA256SUMS` | del método |
| **`README.md`** | **del proyecto** |
| **`LICENSE`** | **del proyecto** |

Los dos últimos no le pertenecen al método, y hasta la versión 2.2.3 `SHA256SUMS` los fijaba a ambos. Un proyecto que cambiara cualquiera de los dos veía fallar su verificación de integridad.

## 1.1 · Cómo se manifestó

En `website-software-humano` los nueve archivos entraron en el commit base sobre un directorio vacío. **No sobrescribieron nada: llenaron un vacío, y después nadie los reemplazó.** El repositorio del sitio quedó con un `README.md` que describe el paquete de método y con las licencias del método, mientras su propio fundamento declara en `§29.5` una exclusión —los nombres «Software Humano» y «Manifiesto» y el logotipo quedan fuera de ambas licencias— que esos archivos no mencionan.

La sesión del sitio lo resolvió poniendo su README en `.github/README.md`, que GitHub muestra antes que el de la raíz. **Funciona, y es el rodeo a un defecto del paquete.**

En un repositorio que ya existe el efecto sería peor: los mismos archivos sobrescribirían los del proyecto.

## 1.2 · Qué ya se corrigió, y qué no

La versión **2.2.4 dejó de fijar `README.md`** en `SHA256SUMS`. Un proyecto ya puede tener el suyo. Comprobado sobre una instalación real: reemplazarlo no produce discrepancias.

**`LICENSE` sigue fijado**, y su caso es más difícil que el del README, porque no basta con dejar de fijarlo.

---

# 2 · Por qué `LICENSE` no se arregla igual

Si el proyecto reemplaza `LICENSE` por el suyo, **el código del método que vive dentro de ese proyecto se queda sin su aviso de licencia**. Y el método sí necesita que su licencia viaje con él: MIT exige que el aviso se incluya en todas las copias.

O sea, hay dos requisitos legítimos en conflicto:

- el proyecto necesita declarar **su** licencia en la raíz, que es donde GitHub y todo el mundo la buscan;
- el método necesita que **la suya** acompañe a sus archivos.

*Inferencia mía:* el conflicto solo existe porque los archivos del método viven en la raíz del proyecto. Si vivieran bajo un directorio propio, cada licencia estaría junto a lo que cubre y no habría colisión.

---

# 3 · Las opciones

## `A` · No cambiar nada más

`README.md` ya está libre desde 2.2.4. `LICENSE` sigue fijado, y quien quiera el suyo rodea como rodeó el sitio.

**Costo:** cada proyecto descubre el problema solo, y el rodeo depende de que su agente o su alojamiento tengan algo como `.github/README.md`. Un proyecto que no use GitHub no lo tiene.

## `B` · Dejar de fijar también `LICENSE`, sin mover nada

Una línea, la misma que se aplicó al README.

**Costo:** el aviso de licencia del método deja de estar garantizado en los proyectos instalados. Si alguien reemplaza `LICENSE`, el preset, la extensión, el workflow y las herramientas quedan sin licencia visible dentro de ese repositorio. `LICENSING.md` seguiría ahí, pero no es un texto legal.

*No la recomiendo.* Cambia un problema de propiedad por uno de licenciamiento, y el segundo es peor.

## `C` · Los archivos del método dejan la raíz

Todo lo que es del método pasa bajo un directorio propio —`metodo/`, o dentro del `docs/method/` que ya existe—, incluidas su licencia y su `LICENSING.md`. En la raíz quedan solo los que el proyecto debe tener o completar:

- `AGENTS.md`, porque es el único archivo que toda sesión de agente carga automáticamente, y ahí está su valor;
- `CLAUDE.md`, por lo mismo;
- `SHA256SUMS`, porque debe poder ejecutarse desde la raíz.

`README.md` y `LICENSE` dejan de existir en el paquete: son del proyecto y el paquete no los toca.

**Costo:** cambia la forma del paquete. Hay que reescribir las rutas de la instrucción 01, del prompt de arranque, del README del paquete y de los dos ensayos; incrementar la versión mayor o menor según se decida; y avisar a los proyectos instalados, que son uno.

**Beneficio:** el conflicto desaparece en vez de administrarse. Cada licencia queda junto a lo que cubre. Y un repositorio existente puede adoptar el método sin que nada suyo sea sobrescrito, que es el caso que todavía no probamos con nadie.

## `D` · `C`, y además el paquete no escribe en la raíz sin avisar

Igual que `C`, y la instrucción 01 agrega un paso que **lista qué archivos va a crear o sobrescribir y se detiene** hasta que la persona lo confirme.

**Costo:** un paso más en la instalación.

**Beneficio:** `STOP03` del núcleo dice que hay que detenerse cuando «se pretende omitir, modificar o postergar una parte sin una decisión autorizada», y `P10` que la persona conserva control y propiedad. **Sobrescribir archivos de alguien sin decírselo es exactamente lo que `P10` describe**, y el método lo hizo durante cuatro versiones sin que ninguna comprobación lo señalara.

---

# 4 · Lo que recomiendo

**`C` ahora, `D` cuando haya un segundo proyecto real que instale sobre algo existente.**

`C` resuelve el conflicto y es trabajo acotado. `D` es correcto doctrinalmente y su costo solo se justifica cuando exista el caso que protege: hoy el único proyecto instalado nació vacío, y el aviso no habría cambiado nada.

**Lo que no recomiendo es `B`**, y conviene dejarlo escrito: resuelve lo visible y rompe lo legal.

---

# 5 · Decisión requerida

**`D-011-1` — ¿Los archivos del método salen de la raíz del proyecto?**

Si la respuesta es sí, quedan por decidir dos cosas que no propongo resueltas:

- **Dónde**. `docs/method/` ya existe y contiene el núcleo y el anexo; meter ahí también las licencias del método y `PARA_QUIEN_DECIDE.md` es lo más simple, pero mezcla doctrina con operación. Un `metodo/` nuevo separa mejor y agrega un directorio.
- **Qué número de versión**. Cambiar dónde viven los archivos rompe toda ruta escrita en un proyecto instalado. *Inferencia mía:* es un cambio mayor y debería ser **3.0.0**, no un incremento menor.

---

# 6 · Lo que esta propuesta no establece

- **No hay evidencia de daño.** Ningún proyecto perdió un archivo por esto: el único instalado nació vacío. El caso grave —sobrescribir el README o la licencia de un repositorio existente— es una inferencia sobre lo que haría el instalador, no algo observado.
- **No mide el costo de `C`.** No conté las rutas que habría que reescribir.
- **No resuelve el caso de quien ya instaló.** Un proyecto con 2.2.4 que actualice a una versión que mueve los archivos se encuentra con los viejos en la raíz y los nuevos en su directorio. Qué hace el método con eso es parte de `D-011-1` y no está pensado.
