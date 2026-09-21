# Propuesta 003 — Licencia del paquete, frontera código/texto, y evaluación de los hallazgos del piloto

**Fecha:** 2026-09-21
**Estado:** propuesta para decisión de Damián Acuña. **Ninguna parte está aplicada.**
**Sesión:** mantenimiento del método (`software-humano-70`)
**Fuente evaluada:** `docs/pilot/registro-del-piloto.md` del repositorio `sitio-software-humano`, secciones A, B, C, D y E — 24 entradas: `A1`–`A5`, `B1`–`B6`, `C1`–`C8`, `E1`–`E5`

## Qué es y qué no es este documento

Evalúa. No aplica. `AGENTS.md` y el propio registro del piloto lo establecen: cambiar el manifiesto, el anexo o el preset exige decisión humana separada, versionar el paquete y regenerar `SHA256SUMS`.

Distingo en todo el documento **hecho observado**, **inferencia mía** y **decisión humana requerida**.

Un aviso sobre el alcance de mi verificación: el registro del piloto fue producido por la sesión del sitio. Verifiqué mecánicamente sus afirmaciones estructurales —`E1` completo, `C1` y la divergencia de `specs/`—. Las afirmaciones sobre lo que ocurrió durante `implement` las tomo como reporte fiel de esa sesión; no las reproduje.

---

# Parte 1 · Licencia del paquete

## `L1` · Hecho: este repositorio no tiene `LICENSE`

Verificado: no existe ningún archivo `LICENSE*` en la raíz.

**Consecuencia.** Por omisión, el paquete queda como «todos los derechos reservados». Eso contradice materialmente lo que el paquete dice de sí mismo: su `README.md` lo describe como «un paquete autocontenido que instala el Manifiesto de Software Humano… **en cualquier proyecto**», y la instrucción 00 prevé instalarlo en repositorios de terceros.

Un artefacto que invita a instalarse sin conceder permiso para hacerlo es una contradicción entre su conducta declarada y su estado legal. En los términos del núcleo, es una falla de `P07`: el producto no puede prometer una apertura que no otorga.

**Inferencia mía.** La ausencia no parece deliberada. La sesión de producto creó un `LICENSE` con MIT en esta raíz y lo **retiró** al advertir que su autoridad alcanzaba solo al código del sitio (`CL-12`). Esa retirada fue correcta: la licencia del paquete de método no es una decisión de producto del sitio.

**Decisión humana requerida.** Bajo qué licencia se distribuye el paquete de método.

## `L2` · Hecho nuevo, no registrado en el piloto: el `LICENSE` del preset contradice `CL-10`

Este hallazgo no aparece en el registro del piloto. Lo encontré al reunir la evidencia de licencias.

`tools/speckit/software-humano-spec-kit-preset-1.0.1/LICENSE` dice hoy, textualmente:

> Copyright (c) 2026 Damián Acuña. All rights reserved.
>
> This package and its contents are proprietary. **No permission is granted to copy, modify, distribute, sublicense, publish, or use this package outside projects explicitly authorized by the copyright holder.**

Y `preset.yml` declara `license: "Proprietary"`.

`CL-10`, decidida por la autoridad de producto el 2026-09-21, establece que el preset se publicará **bajo MIT**, en `https://github.com/dacunao/spec-kit-preset-software-humano`, y que el catálogo de comunidad de SpecKit **exige un archivo de licencia open source**.

**La contradicción es directa y operativa.** El archivo de licencia vigente prohíbe expresamente publicar; la decisión aprobada obliga a publicar bajo MIT. No es un matiz de redacción: el catálogo rechazaría el preset tal como está.

**Impacto adicional.** La cláusula «no permission… to use this package outside projects explicitly authorized» significa que, hoy, ningún tercero puede instalar el paquete legítimamente. El README del paquete lo invita a hacerlo.

**Decisión humana requerida.** Sustituir el `LICENSE` del preset y el campo `license` de `preset.yml`. Es un cambio al preset: exige versionarlo.

## `L3` · La frontera entre código y texto citado

**Hecho.** El paquete mezcla dos naturalezas bajo licencias distintas.

| Naturaleza | Archivos | Licencia pertinente |
|---|---|---|
| **Texto del manifiesto** | `docs/method/Manifiesto_..._v2.1.md` · `templates/constitution-template.md` del preset, que son 82.576 bytes de ese mismo texto | **CC BY 4.0** por `CL-05` |
| **Texto del método sobre el método** | `docs/method/Anexo_..._v1.2.md` | Sin decidir |
| **Código y operación** | `preset.yml`, los ocho comandos, las tres plantillas no doctrinales, `preflight.sh`, `specify`, `shim/python3`, `build-package.sh`, las instrucciones | **MIT** por `CL-10`, al menos para el preset |

**El punto incómodo.** `constitution-template.md` **es** el texto del manifiesto, reorganizado para la jerarquía nativa de SpecKit. Su contenido doctrinal es byte a byte el del núcleo. Si el preset se publica bajo MIT, ese archivo viajaría dentro de un repositorio MIT siendo texto CC BY 4.0.

MIT y CC BY 4.0 no se contradicen —ambas permiten redistribución con atribución— pero **atribuyen de forma distinta** y una licencia única sobre todo el repositorio afirmaría algo falso sobre la mitad de su contenido.

**`CL-05` tiene precedencia.** Fue una decisión de la autoridad de producto, y la sesión del sitio la registró como límite explícito en `E4.2` de su registro. No la reabro. La tomo como dato.

**Inferencia mía, para la decisión de Damián.** La salida coherente con `CL-05` y con lo que el sitio ya hizo es **declarar dos licencias con frontera por naturaleza, no por carpeta**, exactamente como resolvió el repositorio del sitio con `LICENSE` y `LICENSE-CONTENT`. Eso permitiría:

- el preset publicable bajo MIT, satisfaciendo `CL-10` y el catálogo;
- el texto del manifiesto bajo CC BY 4.0 dondequiera que aparezca, incluido dentro del preset, satisfaciendo `CL-05`;
- una nota en el `LICENSE` del preset que identifique `templates/constitution-template.md` como contenido CC BY 4.0 incorporado.

**Qué queda sin resolver aun aceptando eso.** El **anexo** no está cubierto por `CL-05`, que nombra «el texto canónico y el contenido editorial del sitio». El anexo no es ninguno de los dos: es documentación del método. Su licencia es una decisión abierta que nadie ha tomado.

**Decisión humana requerida.** Tres, relacionadas: licencia del paquete como conjunto; licencia del anexo; y la redacción de la frontera.

---

# Parte 2 · Evaluación de los hallazgos del piloto

## `C1` · La única con daño ya medido

**Hecho, verificado por mí.** `SHA256SUMS` cubre `README.md`, y el paquete coloca ese archivo en la raíz del repositorio, que es donde cualquier proyecto necesita el suyo.

**Daño medido, reproducido por mí en el repositorio del sitio.** Ese proyecto no tiene `SHA256SUMS`, su `preflight.sh` reporta «no se encontró SHA256SUMS en la raíz», y por tanto **no puede verificar la integridad del método que lo gobierna**. La sesión del sitio agravó el efecto: `RQ-01` decidió que el texto canónico se lee de `docs/method/` y `T052` verifica su integridad contra `SHA256SUMS`; el resultado real es `sin_referencia`, y **la evidencia de `AC-03` queda cubierta con reserva**.

**Mi valoración.** Es el hallazgo más grave, y lo es por una razón que el registro no subraya: no es que falte una comprobación, es que **la comprobación existe, está implementada, y no tiene contra qué comparar**. El sitio hizo su parte; el paquete no le dio el insumo.

Es además, en su forma, el mismo error que corregimos en v1.1.1 con `AGENTS.md`: un archivo del paquete ocupando un lugar que pertenece al proyecto. Entonces la salida fue excluirlo de la verificación. Aquí esa salida es peor, porque dejaría sin verificar el documento que explica el método.

**Opciones, con su consecuencia.**

| Opción | Qué resuelve | Qué cuesta |
|---|---|---|
| **A · Renombrar el README del paquete** a un nombre que no colisione, por ejemplo `METODO-SOFTWARE-HUMANO.md`, y mantenerlo en `SHA256SUMS` | El proyecto conserva su `README.md`; el método conserva su documento verificado | Quien descomprima el ZIP suelto ya no encuentra un `README.md` de entrada. Se mitiga con un `README.md` **solo dentro del ZIP**, fuera de `SHA256SUMS` y no copiado a la raíz |
| **B · Excluir `README.md` de `SHA256SUMS`**, como se hizo con `AGENTS.md` | Elimina el fallo | Deja sin verificar el documento que describe el método. Repetir la exclusión erosiona lo que `SHA256SUMS` significa |
| **C · Mover todo el método a un subdirectorio**, por ejemplo `method/` | Elimina la clase entera de colisiones, no solo esta | Cambia todas las rutas de las instrucciones, del preflight y del envoltorio. Rompe la compatibilidad con instalaciones existentes |

**Mi recomendación, como recomendación y no como decisión: opción A.** Resuelve el daño medido, conserva la verificación, y es la de menor superficie de cambio. La opción C es la correcta a largo plazo si aparecen más colisiones; hoy no hay evidencia de que existan.

**Efecto sobre el piloto si se aplica A.** Ninguno inmediato. Es la re-sincronización que el propio piloto identificó como `E4.3`: tarea de seguimiento, no interrupción.

## `C2`, `C3`, `C4` y `C8` · La verificación se detiene en los artefactos

**Hecho.** Cuatro hallazgos con una raíz común: `analyze` verifica consistencia **entre** `spec.md`, `plan.md` y `tasks.md`, y no alcanza a

- la realidad física del repositorio que los contiene (`C2`: identidad, archivos protegidos, colisiones de rutas);
- el orden de ejecución respecto de la publicación (`C3`: `B11` antes de `B12` habría servido un sitio sin validar);
- la coherencia entre una tarea y las dependencias de su bloque (`C4`: `T042` era inejecutable donde estaba);
- el estado real del código de un bloque dado por terminado (`C8`: `B02` verde dejaba `B03` imposible).

**Quién los detectó.** Ninguno lo detectó el flujo. `C2`, `C4` y `C8` aparecieron **al intentar ejecutar**. `C3` lo detectó **una pregunta humana**.

**Mi valoración, y aquí discrepo del encuadre del registro.** El registro los presenta como límites de `analyze`. Creo que solo `C4` lo es propiamente.

- `C2` y `C3` son límites del **anexo**, no del preset. El anexo define para `analyze` un foco —`F02`, `F08`, `A02`, `A07`, `SH-STOP`, `V01`–`V12`, `SH-SCORE`, `SH-AP`, `SH-GOV`, `SH-DONE`— que es enteramente documental. Nada en esa lista dirige la mirada al repositorio ni al calendario de ejecución. Ampliarlo es una decisión doctrinal sobre el anexo, no un ajuste del preset.
- `C8` no es un límite de verificación sino de **secuencia**: ninguna capa comprueba que un bloque terminado deje ejecutable al siguiente. Eso no es análisis de consistencia; es una condición de integración que hoy no tiene dueño.
- `C4` sí es abordable desde el preset: la directiva de `tasks` podría exigir que cada tarea declare el bloque del que depende y que se compruebe la coherencia.

**Decisión humana requerida.** Si se amplía el foco de `analyze` en el anexo. **Advertencia:** tocar el anexo es tocar doctrina. La regla del propio anexo lo gobierna: si una disposición no se traza al núcleo v2.1 o a una necesidad técnica inevitable de SpecKit, no pertenece a la adaptación. `C2` y `C3` **sí** se trazan al núcleo —`STOP07` y `SH-DONE` cubren publicar antes de aceptar— así que la ampliación sería legítima. No la propongo redactada: excede lo que una sesión de mantenimiento debe decidir.

**El segundo hallazgo de `C8` merece atención aparte.** El registro señala que el defecto del validador tenía «una salida silenciosa: redactar esquivando las palabras que el validador marcaba mal», que habría producido «una suite verde y una prosa peor», y que **nada en el flujo lo habría detectado nunca**. Observa que la regla del paquete «no edites el paquete para hacer que pase una validación» cubre el método pero no tiene equivalente para el contenido.

Eso sí es incorporable al preset sin tocar doctrina: es la misma regla, aplicada al objeto que el proyecto produce. Lo registro como la mejora de mejor relación entre costo y valor de todo el conjunto.

## `C5` · El ítem del checklist

**Hecho.** «No [NEEDS CLARIFICATION] markers remain» debe fallar mientras existan decisiones reservadas a la autoridad humana, y falló durante todo `specify` y dos rondas de `clarify`.

**Mi valoración.** El paquete v1.1.1 ya lo mitiga: la instrucción 01 §9 anticipa el caso y explica por qué el fallo indica fidelidad a la fuente. El costo residual es real pero menor: hay que explicarlo por escrito cada vez.

No recomiendo tocar el checklist nativo. Conservarlo intacto es una decisión correcta del anexo, y su valor como control depende de no editarlo. La mitigación documental es proporcional al problema.

**Nota de cierre observada.** El checklist del sitio quedó finalmente aprobado, dieciséis de dieciséis, cuando las doce decisiones se resolvieron. El ítem no es inutilizable: es inaplicable **durante una fase**, y lo dice el propio registro.

## `C6` y `C7` · La plantilla de fundamento no captura lo que debe sobrevivir a una sesión

**Hecho.** Dos cosas necesarias quedaron fuera de todo artefacto: la **licencia del código** del proyecto (`C6`, detectada por el agente durante `clarify` y resuelta como `CL-12`) y los **deberes permanentes** del proyecto (`C7`, que viajaban en un prompt).

**Por qué `C7` es el más importante de los dos.** Un prompt muere con la sesión. La obligación de registrar los hallazgos del piloto —que PRD §12.8 y §23.4 imponen— existía solo porque alguien la repetía. **Este mismo documento existe porque la autoridad de producto lo preguntó, no porque el método lo señalara.**

**Ya aplicado en este repositorio, y es lo único de esta propuesta que sí ejecuté**, porque el prompt de esta sesión lo autorizó expresamente: `AGENTS.md` incorpora ahora «Deberes permanentes de este repositorio», con `DP-01` a `DP-03`. El repositorio del sitio hizo lo equivalente con su apartado «Obligación de registro del piloto».

**Lo que falta, y es la propuesta.** Ambos proyectos lo resolvieron **en el proyecto**, no en el método. La plantilla `PLANTILLA_FUNDAMENTO_DE_PRODUCTO.md` y la sección «Completar por proyecto» de `AGENTS.md` siguen sin preguntar por ninguna de las dos cosas. El próximo proyecto volverá a descubrirlas por accidente o no las descubrirá.

**Recomendación, como recomendación.** Agregar dos apartados a la plantilla de `AGENTS.md` del paquete:

1. **Licencias del proyecto** — del código, del contenido, y la frontera entre ambos.
2. **Deberes permanentes** — obligaciones que no son historia, requisito ni tarea, y que deben sobrevivir a cualquier sesión.

Es un cambio **solo a `package/AGENTS.md`**. No toca el manifiesto, el anexo ni el preset. Por tanto no versiona el preset, solo el paquete.

## `B1`–`B6` · Fricciones

No son defectos de doctrina. Mi lectura de cuáles merecen atención:

- **`B2`** es la más peligrosa de las seis, y el registro lo dice bien: «un aviso permanente entrena a ignorar avisos, y el día que aparezca un noveno archivo modificado nadie lo notará». El paquete ya mitiga esto en la instrucción 01 §4.4, que convierte el aviso en verificación de alcance —comprobar que sean exactamente los ocho—. **Lo que falta es automatizarlo**: `preflight.sh` podría hacer esa comprobación y reportar «los 8 esperados» o «ATENCIÓN: 9». Cambio pequeño, valor alto.
- **`B5`** es nueva y no tiene mitigación: los scripts no resuelven la feature cuando `specs/` llega desde otro repositorio, y el mensaje de error sugiere `run the specify command`, que es precisamente lo que **no** debe hacerse. Merece un apartado en la instrucción 00 o 01. **Observación mía:** encontré hoy su contracara. Al retirar `specs/` de este repositorio, `.specify/feature.json` quedó apuntando a un directorio inexistente. Es la misma pieza de estado que no viaja con los archivos, en las dos direcciones.
- **`B6`** —el flujo exige evidencia y no dice dónde se archiva— no es defecto del preset, como el propio registro señala. Pero una convención en la instrucción 01 costaría un párrafo y evitaría que cada sesión elija un lugar distinto.
- **`B1`**, **`B3`** y **`B4`** están documentadas y sin salida mejor conocida. `B4` además se cerró: la segunda sesión materializó la constitución sin fricción adicional.

## `A1`–`A5` · Lo que confirma que el preset funciona

No requieren acción. Los registro porque una evaluación que solo lista defectos no permite decidir sobre un preset.

El preset **impidió un MVP no autorizado** (`A1`), **sostuvo once decisiones abiertas frente a un límite numérico de tres** (`A2`), **mantuvo cuatro puertas humanas sin que ninguna fuera franqueada** (`A3`), **produjo una prueba que encontró un defecto real en una regla** (`A4`), y **impidió que el agente se atribuyera aprobación editorial cuando falsificar un dato de gobernanza habría puesto la suite en verde** (`A5`).

`A5` es, a mi juicio, la observación más valiosa del registro entero: el camino corto estaba disponible, era técnicamente impecable y sustantivamente falso, y la compuerta funcionó **sin que ninguna persona interviniera**.

---

# Parte 3 · Impacto sobre el piloto

La pregunta que el prompt me pide responder con verificación mecánica: **si el paquete se corrige, ¿el piloto debe rehacer o interrumpir algo?**

**No.** Verificado por mí, de forma independiente del registro.

| Comprobación | Resultado |
|---|---|
| Enlaces simbólicos en `.specify/` del sitio | **0** |
| Enlaces en su `docs/method/` y `tools/` | **0** |
| `docs/method/` del sitio | directorio real, no enlace |
| Referencias a la ruta de este repositorio en su `.specify/`, `docs/method/`, `tools/`, `instructions/` | **0** |
| Archivos propios del preset instalado allí | **25** |
| Su núcleo y su anexo frente a los míos | idénticos |

**Conclusión mecánica.** La instalación del sitio es una copia autocontenida. `instructions/01` §3 lo anticipa para `--dev`: «produce una copia real… no un enlace». **Nada de lo que se corrija aquí se propaga solo hacia allá.**

Adoptar una versión nueva del paquete sería una decisión de producto posterior y explícita de esa sesión, con la lógica de PRD §27.3.

Coincido con `E2` en que ningún hallazgo invalida un artefacto ya producido, y con `E5`: el piloto ya pagó el costo de estos hallazgos, el método aún no cobra el beneficio, y ese proyecto no debe nada.

## Los tres puntos de contacto entre ambas sesiones

Coincido con `E4` del registro. Los enumero desde este lado, con su estado real hoy:

1. **`specs/001-sitio-manifiesto/tasks.md` del repositorio del sitio.** El único archivo que ambas sesiones tocan. **Resuelto por coordinación**: la sesión del sitio eligió marcar `T007` y `T008` ella misma, con la evidencia que le envié, porque su copia de trabajo tiene cambios sin confirmar en ese archivo. No lo modifiqué.
2. **La frontera entre código y texto citado.** Único punto donde una decisión del método puede alcanzar al proyecto. **`CL-05` tiene precedencia.** La tomo como dato en `L3`. Si una conclusión mía chocara con ella, es contradicción para Damián y detiene la decisión; no se cierra desde aquí.
3. **Re-sincronizar tras corregir `C1`.** Tarea de seguimiento para recuperar la verificación de integridad del método en el repositorio del sitio. No interrumpe nada: hoy ese proyecto funciona sin ella, con el aviso registrado.

---

# Parte 4 · Qué merece una versión nueva y qué no

Ninguna de estas está aplicada. Requieren decisión de Damián Acuña.

## Requieren decisión urgente, por contradicción viva

| # | Qué | Alcance | Versiona |
|---|---|---|---|
| 1 | **`LICENSE` del preset contradice `CL-10`** (`L2`) | `LICENSE` y `preset.yml` del preset | **preset → 1.0.2** |
| 2 | **El paquete no tiene `LICENSE`** (`L1`) | Raíz del paquete | paquete |
| 3 | **Frontera código/texto**, incluida la licencia del anexo (`L3`) | Documentación de licencias | paquete |

La primera es la más urgente de las tres: mientras el `LICENSE` del preset diga «no permission is granted to… publish», `CL-10` es inejecutable.

## Merecen versión del paquete, sin tocar doctrina

| # | Qué | De dónde | Alcance |
|---|---|---|---|
| 4 | Resolver la colisión del `README.md` | `C1` | `build-package.sh`, instrucciones, `preflight.sh` |
| 5 | Preguntar por licencias y deberes permanentes en la plantilla de `AGENTS.md` | `C6`, `C7` | `package/AGENTS.md` |
| 6 | Automatizar en `preflight.sh` la verificación de los ocho archivos | `B2` | `preflight.sh` |
| 7 | Documentar `SPECIFY_FEATURE_DIRECTORY` al mover `specs/` entre repositorios, en ambas direcciones | `B5` | instrucción 00 o 01 |
| 8 | Fijar una convención para archivar evidencia | `B6` | instrucción 01 |
| 9 | Extender al contenido la regla «no edites para que pase una validación» | `C8`, segundo hallazgo | directiva de `implement` del preset → versiona el preset |

Los puntos 4 a 8 son paquete; el 9 toca el preset y por tanto lo versiona.

## Requieren decisión doctrinal separada, y no las propongo redactadas

| # | Qué | De dónde |
|---|---|---|
| 10 | Ampliar el foco de `analyze` al repositorio y al orden de ejecución | `C2`, `C3` |
| 11 | Exigir coherencia entre tarea y dependencias de su bloque | `C4` |
| 12 | Una condición de integración que compruebe que un bloque terminado deja ejecutable al siguiente | `C8` |

Tocan el **anexo**. La regla del anexo las admite —`C2` y `C3` se trazan a `STOP07` y `SH-DONE`—, pero redactarlas excede lo que una sesión de mantenimiento debe decidir.

## No recomiendo cambiar

| Qué | Por qué |
|---|---|
| El ítem `NEEDS CLARIFICATION` del checklist nativo (`C5`) | La mitigación documental de v1.1.1 es proporcional. Conservar intacto el checklist nativo es una decisión correcta del anexo |
| `B1`, `B3`, `B4` | Documentadas, sin salida mejor conocida. `B4` además ya se cerró en la práctica |

---

# Lo que sí se ejecutó en esta sesión

Para que quede separado de todo lo anterior, que es propuesta:

1. **`AGENTS.md` corregido**, autorizado expresamente por el prompt de esta sesión. Su sección «Completar por proyecto» describía el sitio y era falsa desde `CL-13`. Ahora describe el paquete de método, e incorpora `DP-01` a `DP-03`.
2. **`T007` ejecutado**: retirados `specs/001-sitio-manifiesto/` y el PRD del sitio, verificados antes como idénticos o superados por el repositorio del sitio. Conservada la plantilla de fundamento.
3. **`.specify/feature.json` retirado**, por quedar colgante tras la retirada.
4. **Restos de la sesión de producto eliminados**, verificado antes que ningún archivo fuera exclusivo de este repositorio.

Nada de esto tocó el manifiesto, el anexo ni el preset.

# Un pendiente que no resolví

`Software_Humano_Manifesto_Site_Starter_v1.0.0.zip` sigue rastreado en la raíz. Es la distribución **v1.0.0 del starter específico del sitio**, superada por el paquete genérico v1.1.1, y contiene el PRD del sitio embebido.

No lo retiré porque es contenido rastreado que el prompt de esta sesión no autorizó a tocar: su autorización cubría `AGENTS.md` y la retirada del PRD, nada más. Lo dejo como decisión: conservarlo como artefacto histórico, o retirarlo por coherencia con `T007`, dado que embebe el mismo PRD que acabo de retirar.
