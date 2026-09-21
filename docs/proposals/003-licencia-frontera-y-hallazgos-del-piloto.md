# Propuesta 003 — Licencia del paquete, frontera código/texto, y evaluación de los hallazgos del piloto

**Fecha:** 2026-09-21
**Estado:** **Parte 1 (`L1`, `L2`, `L3`) RESUELTA y aplicada el 2026-09-21** por decisión de Damián Acuña. El resto sigue siendo propuesta sin aplicar.
**Sesión:** mantenimiento del método (`software-humano-70`)
**Fuente evaluada:** `docs/pilot/registro-del-piloto.md` del repositorio `sitio-software-humano`, secciones A, B, C, D y E — 25 entradas: `A1`–`A5`, `B1`–`B6`, `C1`–`C10`, `E1`–`E5` — más `A6`

## Qué es y qué no es este documento

Evalúa. No aplica. `AGENTS.md` y el propio registro del piloto lo establecen: cambiar el manifiesto, el anexo o el preset exige decisión humana separada, versionar el paquete y regenerar `SHA256SUMS`.

Distingo en todo el documento **hecho observado**, **inferencia mía** y **decisión humana requerida**.

Un aviso sobre el alcance de mi verificación: el registro del piloto fue producido por la sesión del sitio. Verifiqué mecánicamente sus afirmaciones estructurales —`E1` completo, `C1` y la divergencia de `specs/`—. Las afirmaciones sobre lo que ocurrió durante `implement` las tomo como reporte fiel de esa sesión; no las reproduje.

---

# Parte 1 · Licencia del paquete

> **RESUELTA el 2026-09-21.** Damián Acuña autorizó resolver `L1`, `L2` y `L3` juntas y versionar el preset a **1.0.2**. Aplicado en el paquete **v1.2.0**:
>
> - `LICENSE`, `LICENSE-CODE` y `LICENSE-CONTENT` declaran la frontera **por naturaleza y no por carpeta**;
> - **MIT** para el preset, las herramientas, las instrucciones y el **anexo v1.2** —la única pieza que nadie había decidido, resuelta aquí porque el anexo es documentación de la adaptación y no doctrina—;
> - **CC BY 4.0** para el texto del núcleo v2.1 dondequiera que aparezca, incluida su proyección dentro del preset, respetando la precedencia de `CL-05`;
> - el preset **v1.0.2** sustituye la licencia propietaria por MIT, **sin cambio doctrinal ni funcional**.
>
> Verificado: la proyección doctrinal de 1.0.2 es byte a byte la de 1.0.1, y **la constitución de este repositorio no necesitó rematerializarse**.
>
> Lo que sigue es el análisis que fundamentó la decisión, conservado como registro.

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

## `C1` · Verificabilidad local, no integridad

> **Corregido el 2026-09-21** tras un contraste con la sesión del sitio. Mi primera redacción calificó a `C1` como «el hallazgo más grave» y describió el problema como de integridad. **Ambas cosas eran imprecisas.** Lo que sigue es la versión verificada.

**Hecho, verificado por mí.** `SHA256SUMS` cubre `README.md`, y el paquete coloca ese archivo en la raíz del repositorio, que es donde cualquier proyecto necesita el suyo.

**Efecto medido, reproducido por mí en el repositorio del sitio.** Ese proyecto no tiene `SHA256SUMS`, su `preflight.sh` reporta «no se encontró SHA256SUMS en la raíz». `RQ-01` decidió que el texto canónico se lee de `docs/method/` y `T052` verifica su integridad contra esa constancia; el resultado real es `sin_referencia`, y **la evidencia de `AC-03` queda cubierta con reserva**.

**La precisión que cambia el diagnóstico.** Verifiqué los digests de los tres lados:

| Archivo | Declarado en mi `SHA256SUMS` | Mi copia | La del sitio |
|---|---|---|---|
| Núcleo v2.1 | `9beef610c0b1…` | `9beef610c0b1…` | `9beef610c0b1…` |
| Anexo v1.2 | `9bc3a6f3d9e1…` | `9bc3a6f3d9e1…` | `9bc3a6f3d9e1…` |

Los tres coinciden. **La copia del sitio está intacta, y es demostrablemente intacta.** El digest que su `T052` observa es exactamente el que mi `SHA256SUMS` declara.

Por tanto `C1` **no es un problema de integridad sino de verificabilidad local**: la demostración existe, pero solo mediante un contraste manual entre repositorios que una constancia versionada volvería innecesario y automático.

**Mi valoración corregida.** Sigue mereciendo corrección, por dos razones que se sostienen: una comprobación implementada que no puede resolverse sola es deuda técnica, y depender de un contraste manual entre dos máquinas no escala a un tercer proyecto. Pero **no es el hallazgo más grave del conjunto**: ese lugar corresponde a `L2`, la contradicción entre el `LICENSE` del preset y `CL-10`, que sí bloquea una decisión ya aprobada.

Lo que el registro sí capta bien, y mantengo: el sitio hizo su parte; el paquete no le dio el insumo.

**Nota sobre `docs/method/` duplicado.** La sesión del sitio precisó al cerrar `T008` que el núcleo y el anexo viven en ambos repositorios y **deben** hacerlo: `RQ-01` decidió leer el núcleo de su fuente protegida en lugar de copiarlo al contenido. No es una segunda autoridad sino una instalación, igual que `tools/speckit/` e `instructions/`. La duplicación no autorizada desapareció con `T007`; la que queda es por diseño, y es precisamente la que `C1` debería permitir verificar sin intervención humana.

Es además, en su forma, el mismo error que corregimos en v1.1.1 con `AGENTS.md`: un archivo del paquete ocupando un lugar que pertenece al proyecto. Entonces la salida fue excluirlo de la verificación. Aquí esa salida es peor, porque dejaría sin verificar el documento que explica el método.

## `C1` reformulado tras la re-sincronización del 2026-09-21

> **Esto reemplaza las tres opciones que yo había propuesto.** La sesión del sitio re-sincronizó a 1.0.2 y contrastó `SHA256SUMS` entrada por entrada antes de decidir si lo copiaba. No lo copió, y su razón reorienta la solución.

**El contraste, verificado por mí de forma independiente.**

| Resultado | Cuántos | Cuáles |
|---|---:|---|
| **Coinciden** | **10** | Núcleo v2.1, anexo v1.2, las dos instrucciones, `preflight.sh`, `specify`, `shim/python3`, `shim/README.md`, `CLAUDE.md`, `START_WITH_AI_AGENT.md` |
| **Difieren** | **3** | `README.md`, `LICENSE`, `LICENSE-CONTENT` |
| **Ausentes** | **20** | El árbol fuente del preset, su ZIP y la plantilla de fundamento: archivos del paquete que una instalación no debe tener |

Copiar la constancia entera produciría una verificación que **falla en 23 de 33** y un preflight que reporta errores donde no los hay. **Sería peor que no tenerla**, porque enseñaría a ignorarla — el mismo razonamiento que sacó a `AGENTS.md` de la verificación en v1.1.1.

**La reformulación, y es de la sesión del sitio.** `C1` no se resuelve publicando una constancia del paquete. Se resuelve **distinguiendo qué archivos de un proyecto instalado pertenecen al método y cuáles al proyecto**. Es la misma **frontera por naturaleza y no por carpeta** que `L1`–`L3` acaban de trazar para las licencias, aplicada ahora a la integridad en lugar de al derecho de uso.

Lo que hace convincente la reformulación es que **los 10 que coinciden no son un conjunto arbitrario**: son exactamente los archivos que un proyecto instalado copia y no debe modificar. Y los 3 que difieren son exactamente los que le pertenecen por naturaleza. La frontera ya existe en los hechos; lo que falta es declararla.

## Lo que empeoré al resolver `L1`–`L3`

**Antes de mi cambio, la colisión era de un archivo. Ahora es de tres.**

`README.md` colisionaba desde siempre. `LICENSE` y `LICENSE-CONTENT` no existían en el paquete hasta la v1.2.0: los agregué yo, y ambos repositorios tienen legítimamente los suyos.

No me arrepiento de la decisión —el paquete no podía seguir sin licencia—, pero registro el efecto: **resolver las licencias amplió la superficie del problema de integridad**. Y descarta de paso mi opción A original, «renombrar el `README` del paquete»: renombrar `LICENSE` sería mucho peor, porque es un nombre convencional que herramientas y personas esperan en la raíz.

## Un hallazgo adicional, verificado hoy

**El preset que realmente se ejecuta no está cubierto por ninguna constancia.**

Vive en `.specify/presets/software-humano/` —25 archivos en el repositorio del sitio— y `SHA256SUMS` tiene **cero entradas** que lo alcancen. Mi árbol fuente tiene 17 archivos y una estructura distinta, porque la instalación agrega las composiciones.

O sea: la constancia cubre hoy el preset **como se distribuye**, no **como se ejecuta**. Un proyecto no puede demostrar que los ocho comandos que gobiernan su ciclo SDD son los que el paquete entregó.

Es, en su forma, el mismo problema que `C1` describe para el núcleo, un nivel más abajo y sin que nadie lo hubiera advertido.

## Forma de solución que propongo, sin redactarla

**Una constancia que declare su propio alcance.** La idea es de la sesión del sitio; la concreto sin decidirla:

- **`SHA256SUMS`** sigue cubriendo el paquete completo, que es lo correcto para verificar un ZIP descargado.
- **Un segundo manifiesto —o un subconjunto marcado dentro del mismo—** declara qué archivos deben ser idénticos **en una instalación**: hoy esos 10, más lo que se decida sobre el preset en ejecución.
- `preflight.sh` elige cuál verificar según detecte un paquete recién descomprimido o un proyecto instalado.

Eso resolvería las tres cosas a la vez: el sitio recuperaría la verificación local, `AC-03` dejaría de estar cubierta con reserva, y la re-sincronización pasaría de exigir criterio a ser mecánica.

**Decisión humana requerida.** Si se aborda, y con qué alcance: solo los 10 archivos de método, o también el preset en ejecución. Lo segundo es más valioso y más caro.

**Efecto sobre el piloto.** Ninguno inmediato. Hoy funciona sin la constancia, con su reserva sobre `AC-03` registrada y su `T052` reportando `sin_referencia` de forma honesta.

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

## `C9` · Una decisión aprobada puede ser correcta como intención y falsa como descripción

> **Agregado el 2026-09-21.** Registrado por la sesión del sitio a partir de `L2`, y verificado por mí. Es el hallazgo de mayor alcance doctrinal de todo el conjunto, y **no lo detectó ninguna capa del flujo**.

**El patrón.** Un `CL` es una decisión aprobada, y aguas abajo se trata como dato. Pero cuando esa decisión **describe un artefacto externo**, puede ser simultáneamente:

- **correcta como intención** — es lo que la autoridad decidió;
- **falsa como descripción** — el artefacto no dice eso.

`specify`, `clarify`, `plan`, `tasks` y `analyze` **no distinguen esos dos casos**. Tratan toda decisión aprobada como un hecho.

**Dos instancias verificadas, no una.**

| # | Afirmación del fundamento | Lo que dice el artefacto | Dónde apareció |
|---|---|---|---|
| 1 | `FR-009`: la adaptación «fue validada técnicamente en **versión 1.0.0**» | La instalada y verificada en ambos repositorios es la **1.0.1** | Al redactar el contenido que debía afirmarlo |
| 2 | `CL-10` / `licencia: MIT` en el contenido publicable | `LICENSE` del preset: «All rights reserved… **no permission is granted to… publish**» | Al redactar el contenido que debía afirmarlo |

Verifiqué ambas: `FR-009` en la línea 619 del PRD dice literalmente «fue validada técnicamente en versión 1.0.0», y `preset.yml` declara `version: "1.0.1"` tanto aquí como en la instalación del sitio.

**Lo que hizo la sesión del sitio, y es lo correcto.** No revirtió `CL-10` —MIT es decisión de la autoridad de producto— ni corrigió `FR-009`, que es texto del PRD. Declaró ambas como **limitaciones visibles** en `src/content/preset.yaml`, dejando la contradicción abierta en lugar de resolverla desde su autoridad. `P07` y `BR-009` habrían sido infringidos si el sitio publicaba «MIT» junto a «no publicado» sin más: haría creer que el paquete ya puede usarse cuando su propio archivo lo prohíbe.

## Mi responsabilidad en la primera instancia

**La causé yo, y ningún mecanismo lo señaló.**

Cuando incrementé el preset a 1.0.1 para corregir las dos anclas desplazadas —propuesta 001—, la afirmación fáctica de `FR-009` quedó obsoleta. Yo verifiqué entonces que el texto doctrinal era byte a byte idéntico, que la constitución se rematerializaba correctamente y que la integridad pasaba 30/30. **No verifiqué si alguna afirmación de un fundamento aguas abajo dependía del número de versión que acababa de mover.**

No existe hoy ningún mecanismo que lo hubiera detectado:

- `SHA256SUMS` comprueba que los archivos no cambiaron, no que las afirmaciones sobre ellos sigan siendo ciertas;
- `analyze` recorre los artefactos del proyecto, no las versiones de un paquete instalado desde otro repositorio;
- `preflight.sh` comprueba el entorno, no la coherencia entre el fundamento y el artefacto que describe.

**Es la contracara aguas arriba de `E1`.** `E1` establece que nada de lo que corrija aquí se propaga solo hacia el proyecto instalado, y eso es correcto y deseable para los **archivos**. Pero significa también que **nada avisa cuando un cambio aquí falsifica una afirmación de allá**. El desacoplamiento protege de la propagación involuntaria y, por el mismo mecanismo, oculta la invalidación.

> La sesión del sitio aceptó esto como corrección y no como complemento, y enmendó `E1` en consecuencia (su commit `4565f8e`, verificado por mí). `E1` presentaba el desacoplamiento solo por su lado tranquilizador; ahora registra que **no es solo una garantía sino una responsabilidad de ida y vuelta, y que hoy ninguna de las dos direcciones tiene mecanismo**. La de este repositorio es `DP-02`, extendido abajo. La de un proyecto instalado es contrastar antes de publicar, que es lo que hizo aparecer las dos instancias de `C9`. La conclusión de `E5` no cambia.

**Consecuencia para el mantenimiento.** Versionar el paquete no es solo regenerar `SHA256SUMS`. Es comprobar si algún proyecto instalado afirma algo sobre la versión que se está moviendo. He extendido `DP-02` de `AGENTS.md` en consecuencia.

> **`DP-02` ya se validó, y en su modo útil.** Al versionar a 1.0.2 encontré en el `README.md` del preset un párrafo que acababa de quedar falso en dos de sus tres afirmaciones: «antes de publicarla en un catálogo se debe definir un repositorio público, una URL de descarga versionada y una licencia de distribución aprobada. **No se ha supuesto una autorización de código abierto**». Lo corregí antes de construir el paquete.
>
> La sesión del sitio hizo la distinción que lo vuelve significativo, y es suya: **`FR-009` fue un hallazgo forense** —apareció cuando alguien tuvo que escribir el dato— **y el del README fue preventivo** —apareció porque `DP-02` obliga a buscarlo—. Un mecanismo que solo produce hallazgos forenses documenta bien y no protege. Este ya hizo las dos cosas.
>
> Sin `C9`, el paquete v1.2.0 se habría publicado afirmando que no existía autorización de código abierto, dentro de la misma versión que la concede.

**Decisión humana requerida.** Dos, y son de distinta naturaleza:

1. **`FR-009` afirma una versión que ya no es la vigente.** Corregirlo es modificar el PRD, que solo la autoridad de producto puede hacer. La alternativa —que el requisito no fije un número y remita al estado verificado— es una mejora de redacción del fundamento, no del método.
2. **Si el flujo debe distinguir «decisión aprobada» de «afirmación fáctica verificable».** Esto sí es método, y es doctrinal: tocaría el anexo. No lo propongo redactado.

## `C10` · Un orden de bloques puede dejar una compuerta roja durante un intervalo, y nadie lo declara

> **Agregado el 2026-09-21.** Registrado por la sesión del sitio al cerrar `B03`. Evaluado aquí por `DP-01`.

**Hecho.** Al fusionar `B03` —contenido real en español— la integración continua del sitio falló con 313 hallazgos de `VB-04`: faltan las traducciones y los registros de aprobación. **Es la conducta correcta**: `BR-007` exige detener el build ante traducciones requeridas incompletas, y `A5` ya registró que ese mismo mecanismo impidió que el agente se atribuyera aprobación editorial.

Pero el plan ordena `B03` antes que `B05`, así que la rama principal queda **en rojo durante todo el intervalo entre ambos**, y ningún artefacto declara qué se espera de la compuerta mientras tanto.

**La formulación de la sesión del sitio, que comparto.** No se decidió mal: **no se decidió**. El riesgo no es el rojo sino su duración, porque una compuerta permanentemente roja por una razón conocida deja de señalar, y un fallo nuevo llega a una rama que ya estaba rota.

Es, punto por punto, el mismo mecanismo de `B2` —el `WARNING` permanente de `integration status` que entrena a ignorar avisos— en un lugar más caro.

**Dónde pongo el límite, y difiero del encuadre.** La sesión del sitio lo presenta condicionado a que el paquete recomiende una integración continua de referencia. Verifiqué que **no recomienda ninguna**, y no propongo que empiece a hacerlo: un paquete de método que prescriba infraestructura de CI excedería la regla del anexo, que descarta toda disposición no trazable al núcleo o a una necesidad técnica inevitable de SpecKit.

**Lo que sí es del método, y es más pequeño y más útil.** La plantilla de plan ya tiene el lugar exacto donde esto debía declararse: la tabla de «Dependencias, bloqueantes y orden de ejecución», con sus columnas `Depende de`, `Desbloquea` y `Criterio para avanzar`.

Lo que no pide es el **estado esperado de las verificaciones durante el intervalo**. Un plan que ordena los bloques de modo que una regla de detención **no pueda satisfacerse todavía** debería declararlo: qué comprobación quedará en rojo, desde qué bloque hasta cuál, y por qué razón conocida.

Eso no prescribe CI, no debilita ninguna regla y no crea un artefacto nuevo. Añade una columna o una nota a una tabla que ya existe.

**La reformulación que lo reordena, y es de la sesión del sitio.** Aceptó el reencuadre y retiró la condicional sobre la CI, observando que «al sugerir que el paquete previera el caso *si llegara a recomendar una CI de referencia* estaba proponiendo que empezara a hacerlo, con una condicional que disimulaba la propuesta». Y agregó la frase que cambia cómo debe leerse todo el hallazgo:

> **No describe un problema de la compuerta: describe una omisión del plan que la compuerta reveló. La compuerta hizo su trabajo, incluido señalar lo que nadie había previsto.**

Eso es exacto y conviene tenerlo presente al decidir. `C10` **no es evidencia de que `BR-007` sea demasiado estricta** ni de que la detención esté mal calibrada: es evidencia de que el plan omitió declarar una consecuencia de su propio orden, y de que la regla de detención fue lo único que lo hizo visible. La salida correcta **refuerza el plan, no relaja la compuerta**.

**Relación con `C3`.** Misma familia y mismo eje. `C3` observó que el orden puede exponer el producto **antes de la aceptación**; `C10` observa que el orden puede dejar una compuerta **inútil durante un intervalo**. En ambos casos la consecuencia es del orden en el tiempo, y en ambos ninguna capa la examina. Si se aborda `C3`, conviene abordar `C10` en el mismo cambio.

**Lo que la sesión del sitio hizo bien.** No tocó la CI. Distinguir los hallazgos esperados del resto debilitaría `BR-007` si se hace mal, y esa es una decisión de la autoridad de producto del sitio, no del método.

**Decisión humana requerida, y son dos en planos distintos.**

1. **Del método**: si la plantilla de plan pide declarar el estado esperado de las verificaciones por intervalo. Toca el preset —es su plantilla— y por tanto lo versiona.
2. **Del producto del sitio**: si esa sesión puede agregar a su `plan.md` la línea que declara el rojo de `B03` a `B05`. No la escribió, y con razón: `plan.md` es un artefacto rector revisado, y modificarlo durante `implement` —aunque sea para documentar un hecho que ya existe— es autoridad de producto.

Si la segunda se aprueba, el proyecto habrá aplicado la lección **antes** de que el método la codifique, igual que ocurrió con `C2` y `C3` según `E3`. Eso no anticipa la decisión del método: la informa, porque habrá una redacción concreta que evaluar en lugar de una hipótesis.

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

## `A6` · La separación de autoridades produjo verificación, no solo coordinación

> **Agregado al cierre del contraste.** Registrado por la sesión del sitio, verificado por mí (su commit `780336d`). Evaluado aquí por obligación de `DP-01`.

**Hecho.** Cuatro correcciones salieron de que ninguna de las dos sesiones aceptó la evidencia de la otra sin comprobarla: la precisión de `C1`, el matiz de `T008`, la contracara de `E1` y la procedencia de `FR-009`. Dos las produjo cada lado, y **dos de ellas son autocorrecciones**: cada sesión corrigió algo propio al ser contrastada.

**Mi valoración, y coincido en cuál es la que más dice.** La cuarta. Atribuir `FR-009` a falta de cuidado habría producido «verificar mejor», que no es accionable; atribuirlo al mecanismo produjo `DP-02` extendido. La sesión del sitio agrega la condición que lo hace posible, y creo que es correcta: **eso solo aparece cuando quien cometió el error puede describirlo sin que le cueste autoridad**. Con una sola sesión, quien se equivoca es también quien evalúa.

**Lo más interesante, y es suyo.** `CL-13` se decidió para evitar duplicar artefactos rectores, **no** para obtener revisión cruzada. El beneficio no estaba en el motivo.

**Dónde pongo el límite, y por eso no lo propongo como práctica.** Esto es **n=1**. Un piloto no establece que la separación de autoridades produzca verificación en general; establece que la produjo aquí, con dos sesiones que eligieron contrastar. Nada garantiza que dos sesiones cualesquiera lo hagan: podrían aceptarse mutuamente sin comprobar, y entonces el costo del protocolo se pagaría sin el beneficio.

Recomendar la separación como práctica del método sería exactamente el antipatrón `SH-AP` de «la circunstancia fue inventada»: generalizar desde un caso plausible sin evidencia de que se repita.

**Lo que sí propongo**, y es modesto: que `A6` se conserve como **observación registrada** para contrastarla contra el segundo proyecto que use el paquete. Si vuelve a ocurrir, hay base para documentarlo; si no, quedará como una particularidad de este piloto. No requiere cambio alguno en el paquete hoy.

> **Ya aplicado en el origen.** La sesión del sitio aceptó el límite y acotó la entrada (su commit `aab45c8`, verificado): el título pasó a «produjo verificación **en este caso**», se eliminó la frase «lo que compra vale más que lo que cuesta» —que era una conclusión de costo-beneficio presentada como hecho observado—, se sustituyó el contrafáctico «ninguna la habría producido una sesión sola» por lo que sí consta, que ninguna apareció dentro de una sola sesión, y la sección `D` advierte ahora que `A6` debe leerse con su límite. Conservó sin acotar lo único que no depende de la muestra: que la revisión cruzada no figuraba entre los motivos de `CL-13`.
>
> Con eso, esta propuesta no pide nada sobre `A6`: pide **no** convertirla en práctica, y el registro ya no lo insinúa.

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

La primera es la más urgente **de toda esta propuesta**, no solo de las tres: mientras el `LICENSE` del preset diga «no permission is granted to… publish», `CL-10` es inejecutable. Supera en gravedad a `C1`, que tras el contraste de digests resultó ser un problema de verificabilidad y no de integridad.

## Merecen versión del paquete, sin tocar doctrina

| # | Qué | De dónde | Alcance |
|---|---|---|---|
| 4 | Resolver la colisión del `README.md`, para que la verificación de integridad sea local y automática en cada proyecto instalado | `C1` | `build-package.sh`, instrucciones, `preflight.sh` |
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
| 12b | Pedir en la plantilla de plan el **estado esperado de las verificaciones por intervalo**: qué comprobación queda en rojo, entre qué bloques y por qué. Versiona el preset | `C10`, junto con `C3` |
| 13 | Distinguir «decisión aprobada» de «afirmación fáctica verificable» cuando un `CL` describe un artefacto externo | `C9` |

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
