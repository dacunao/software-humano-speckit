# Instrucciones persistentes para agentes

Este archivo es la **fuente única** de las reglas que gobiernan el trabajo de cualquier agente en este repositorio. Es neutral respecto del agente: sirve para Claude Code, Codex, Cursor, Gemini, Copilot o cualquier otro que lea instrucciones persistentes del proyecto.

Si tu agente carga un archivo distinto —`CLAUDE.md`, por ejemplo—, ese archivo debe **referenciar** este, no duplicarlo. Dos copias de instrucciones rectoras divergen; el anexo lo prohíbe expresamente.

## Mandato

Este repositorio aplica el **Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1** mediante la adaptación Software Humano para SpecKit, y preserva íntegramente el fundamento de producto autorizado.

No conviertas estas instrucciones en una metodología adicional. Usa el flujo nativo de SpecKit y los artefactos que ya define el núcleo.

## Lectura obligatoria antes de actuar

Lee completos y en este orden:

1. `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`
2. El fundamento de producto autorizado de este proyecto — ver **Completar por proyecto**
3. `docs/method/Anexo_Aplicacion_SpecKit_v2.0.md`
4. `docs/method/GUIA_DE_IMPLEMENTACION_SPECKIT.md`
5. `instructions/00_REQUISITOS_DE_INSTALACION.md`
6. Los artefactos vigentes de `.specify/`, una vez que existan

No basta con buscar palabras o leer resúmenes. Los identificadores permiten navegar y citar; no sustituyen el pasaje completo.

## Autoridad

- El **núcleo** gobierna principios, doctrina, flujo, artefactos, contrato del agente, detenciones, verificación y gobernanza.
- El **fundamento de producto** gobierna visión, alcance completo, requisitos, no objetivos, decisiones aprobadas y aceptación.
- El **anexo** gobierna la correspondencia entre el núcleo y SpecKit.
- El **preset** gobierna la materialización técnica de esa correspondencia.
- **SpecKit** conserva su comportamiento nativo donde el preset no interviene.

El núcleo y el fundamento no compiten: el núcleo gobierna el método y los criterios; el fundamento gobierna el producto.

No alteres silenciosamente una fuente para acomodarla a otra. Si detectas incompatibilidad, cita ambas disposiciones, explica el impacto y detén la decisión afectada.

## Reglas de trabajo

1. Comprende la definición completa antes de proponer **cualquier cosa**: componentes, código, arquitectura, una dirección de diseño, una alternativa o un enfoque. Consulta la doctrina que gobierna esa decisión **antes de formular la propuesta**, no después de que alguien la cuestione.
2. Conserva todos los identificadores del fundamento de producto sin renumerarlos ni reagruparlos.
3. No asignes prioridad, MVP, releases, independencia ni incrementalidad salvo autorización expresa del fundamento.
4. Ordena el trabajo por dependencias, bloqueantes, integración y riesgo sin reducir alcance.
5. Distingue hechos, evidencia, supuestos, inferencias, recomendaciones y decisiones humanas.
6. Utiliza la solución más simple que satisfaga lo aprobado; no agregues modos, paneles, configuraciones, abstracciones ni documentos sin fundamento.
7. Trata experiencia, accesibilidad, rendimiento, confianza, continuidad y control como parte de la funcionalidad.
8. No confundas código correcto, build exitoso o pruebas verdes con aceptación del producto.
9. No te atribuyas revisión humana, excepción aprobada ni autoridad para modificar el fundamento.
10. Mantén trazabilidad bidireccional entre fuente, especificación, plan, tareas, código y evidencia.
11. **Antes de abrir una decisión a la persona, comprueba que las fuentes rectoras no la resuelvan ya.** Debes poder nombrar qué fuente consultaste. Una pregunta cuya respuesta ya está escrita no es deferencia: traslada a la persona un trabajo que te corresponde y gasta la atención que `P06` protege.

Las reglas 1 y 11 existen porque los comandos `speckit.*` solo gobiernan mientras uno de ellos corre. **Una propuesta hecha en conversación, una pregunta formulada en el chat o un informe presentado fuera de un artefacto no pasan por ninguno de ellos.** Este archivo es la única capa presente en ese territorio, y ahí ocurrieron los tres fallos de juicio del primer piloto real.

## Flujo SpecKit obligatorio

1. Comprueba el entorno con `instructions/00_REQUISITOS_DE_INSTALACION.md` y `tools/speckit/preflight.sh`.
2. Instala y verifica el preset siguiendo `instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md`.
3. Materializa la constitución v2.1 completa.
4. Ejecuta `specify` usando el fundamento completo como fuente autorizada.
5. Ejecuta `clarify` en rondas focalizadas hasta resolver las decisiones materiales necesarias.
6. Ejecuta `plan` para todo el alcance; crea auxiliares solo cuando respondan una pregunta necesaria.
7. Ejecuta `tasks` con cobertura completa y evidencia trazable.
8. Ejecuta `analyze` sin modificar los artefactos examinados.
9. Presenta los resultados en lenguaje natural y espera revisión humana.
10. Ejecuta `implement` solo después de autorización explícita.
11. Ejecuta `converge` para cerrar brechas del alcance aprobado; no para agregar producto nuevo.

## Condiciones de detención

Detente cuando:

- una ambigüedad pueda cambiar alcance, reglas, derechos, seguridad, contenido o experiencia;
- una fuente autorizada contradiga otra;
- falte autoridad para una decisión irreversible o sensible;
- un requisito, principio, idioma o criterio de aceptación pierda cobertura;
- el plan o una tarea agregue una capacidad sin fundamento;
- exista riesgo de sobrescribir cambios humanos en `.specify/`, documentos rectores o código;
- la constitución no pueda verificarse completa;
- una acción requiera modificar el core de SpecKit o el preset para continuar;
- el resultado solo tenga evidencia técnica y se intente declarar aceptación humana.

Una detención útil indica: el hecho, la evidencia, el impacto, la decisión requerida y la acción que no ejecutaste.

## Archivos protegidos por autoridad

No modifiques sin instrucción humana explícita:

- `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`
- `docs/method/Anexo_Aplicacion_SpecKit_v2.0.md`
- El fundamento de producto autorizado
- El directorio del preset en `tools/speckit/`
- `SHA256SUMS`

Si una implementación revela una mejora posible, regístrala como propuesta separada. No la incorpores retroactivamente a las fuentes.

## Notas de entorno que ahorran tiempo

Estas no son doctrina. Son fricciones reales observadas en instalaciones anteriores.

- **Scripts de SpecKit y PyYAML.** `.specify/scripts/bash/common.sh` usa el primer `python3` del `PATH`. Si no tiene PyYAML, toda resolución de plantillas falla. Antepón el shim del repositorio: `PATH="$PWD/tools/speckit/shim:$PATH"`. No modifiques `.specify/scripts/`: son copias generadas y una actualización las reescribiría.
- **Versión de SpecKit.** Si la instalación global está fuera del rango del preset, usa `tools/speckit/specify`, que fija una instancia aislada sin tocar otros proyectos.
- **Constancia de procedencia.** No modifiques `.specify/memory/.constitution-template.json`. Su desajuste tras materializar la constitución es deliberado: hace que el CLI trate la constitución como documento humano y no la sobrescriba.
- **Estado de la integración.** Tras instalar el preset, `integration status` reporta `warning` con 8 archivos modificados. Es el resultado esperado: son los ocho comandos que el preset compone. Verifica que sean exactamente esos ocho y que no incluyan `checklist` ni `taskstoissues`.

## Comunicación con la persona

- Explica resultados, decisiones, riesgos y evidencia en lenguaje natural.
- Cuando muestres código o comandos, acompáñalos con la consecuencia que producen.
- No ocultes pendientes bajo un estado exitoso.
- Distingue avance técnico, cobertura del alcance y aceptación humana.
- Antes de solicitar autorización para implementar, resume fuente, cobertura, decisiones, riesgos y evidencia esperada.

---

# Completar por proyecto

**Todo lo anterior es invariante y se aplica a cualquier proyecto que use este método. Lo que sigue es específico de este repositorio y debe completarse antes de ejecutar `specify`.**

> **Por eso este archivo queda fuera de `SHA256SUMS`.** Está diseñado para que cada proyecto lo edite, de modo que no es un archivo invariante del método. `SHA256SUMS` verifica el manifiesto, el anexo, el preset, las instrucciones y las herramientas: todo lo que **no** debe cambiar. Si la verificación de integridad falla, hay un problema real; completar esta sección nunca la rompe.

Si un campo está sin completar, el agente debe detenerse y solicitarlo. No lo infiera.

## Producto

- **Nombre del proyecto**: Software Humano para SpecKit — paquete de método
- **Qué construye este repositorio**: el **paquete de método** distribuible que aplica el Manifiesto de Software Humano al ciclo SDD nativo de SpecKit, en cualquier proyecto. Aquí viven el núcleo, el anexo, el preset, las instrucciones de instalación, las herramientas de apoyo y el ensamblador de la distribución.

**Este repositorio NO construye el sitio del Manifiesto.** Hasta el 2026-09-21 lo hizo. La decisión `CL-13` separó el sitio a su propio repositorio, `https://github.com/dacunao/sitio-software-humano`, que desde entonces es **el autoritativo** para el PRD del sitio, sus `specs/`, su código y su registro del piloto. No trabajes aquí sobre el producto del sitio ni asumas que sus artefactos viven en este repositorio.

## Fundamento de producto autorizado

**`docs/product/FUNDAMENTO_DEL_PAQUETE_DE_METODO.md`**, autorizado por Damián Acuña el 2026-09-23.

Hasta esa fecha este archivo afirmaba que el repositorio no necesitaba fundamento porque «no construye un producto para usuarios finales». **La afirmación era falsa**: el manifiesto declara que su marco sirve para «herramientas internas» y «productos con agentes», y está dirigido también a «agentes de código». El paquete está dentro de su alcance, y por lo tanto su desarrollo se gobierna por él.

El fundamento se subordina a la doctrina que el paquete distribuye:

- `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md` — núcleo v2.1
- `docs/method/Anexo_Aplicacion_SpecKit_v2.0.md` — anexo v2.0
- **Autoridad**: Damián Acuña

La regla del anexo gobierna toda incorporación al paquete: *«Si una disposición de la adaptación no puede trazarse al núcleo v2.1 o a una necesidad técnica inevitable de SpecKit, no pertenece a la adaptación.»*

## Identificadores que deben preservarse

Los del propio núcleo, porque son el contenido que el paquete distribuye y las direcciones que citan el preset, el anexo y las instrucciones:

- `P01`–`P10`, `SH-FUND`, `D01`–`D06`, `F01`–`F08`, `A01`–`A08`
- `SH-STOP` y `STOP01`–`STOP07`, `CR01`–`CR08`, `O01`–`O09`, `V01`–`V12`
- `SH-INDEX`, `SH-SCORE`, `SH-AP`, `SH-GOV`, `SH-DONE`, `SH-POCKET`

Una constitución materializada debe contener las quince familias completas. `instructions/01` §6 lo verifica.

## Decisiones técnicas aprobadas

- **Versionado semántico independiente** para el paquete, el preset, el núcleo y el anexo. La versión del preset no sigue a la del núcleo. **Las cinco capas del método salen alineadas en 2.0.0** —paquete, preset, extensión, workflow y bundle—, y eso no las acopla: cuando una necesite un parche se mueve sola, y esa divergencia significará que esa capa cambió.
- **Cuatro mecanismos nativos, no uno.** Preset para la doctrina en los artefactos, extensión para la conformidad, workflow para el cumplimiento y bundle para la distribución. Hasta la propuesta 008 este archivo decía que solo se usaban presets; la condición que el propio anexo fijó para salir de ahí —«una necesidad técnica demostrada que el preset no pueda resolver»— se cumplió por dos vías: su guía oficial dice que un preset no puede agregar capacidades, y el motor de workflows es el único lugar de SpecKit donde un paso lo ejecuta el motor y no el agente.
- **Composición `wrap` sin frontmatter** para los ocho comandos. Una capa que declara frontmatter reemplaza el del core y borra sus `handoffs`; una que no lo declara lo conserva entero. **Adición, no sustitución, en las plantillas**: sustituir borra las secciones que los comandos nativos buscan por su nombre. La sustitución queda reservada a la plantilla de constitución, cuyo contenido es por definición propio.
- **El checklist nativo se conserva sin intervención.**
- **Compatibilidad declarada** con SpecKit `>=1.0.0,<2.0.0`, verificada sobre 1.0.8.
- **`SHA256SUMS` cubre los archivos invariantes**, y deliberadamente **no** cubre `AGENTS.md`, que cada proyecto completa.
- **Etiquetas de release con prefijo por componente**, aprobado el 2026-10-01. El paquete se publica como `vX.Y.Z`; un componente que se publica por separado lleva su capa y su nombre en la etiqueta: `preset-software-humano-v2.0.3`, `extension-conformidad-v2.2.3`.

  **Por qué existe.** El catálogo comunitario de SpecKit exige que la versión declarada de un componente coincida con el número de su etiqueta de descarga, y rechaza el envío cuando no coincide —sin descargar el archivo—. Con etiquetas desnudas eso obliga a elegir entre alinear las cinco capas en un número, que destruye lo que informa el versionado independiente de arriba, o publicar etiquetas `v2.0.3` que al lado de `v2.3.3` se leen como un retroceso del paquete. El prefijo evita las dos cosas: el validador acepta «scoped tags whose version suffix matches», y la lista de releases queda legible porque cada entrada dice de qué componente es.

  **Cómo se publica.** El título de la release nombra el componente y su versión —«Extensión Conformidad 2.2.3»—, no solo la etiqueta: es el título, y no la etiqueta, lo que hace que la lista no se lea como números desordenados. Y la release del paquete queda marcada como `Latest`: GitHub se la otorga a la última creada, de modo que publicar componentes después obliga a devolverla con `gh release edit <paquete> --latest`.

  **Lo que un componente no reemplaza.** Quien llega al método instala la release del paquete completo. Los ZIP por componente instalan una sola capa y existen para el catálogo.

  **Y el ZIP no es reproducible**: dos ensamblados de fuentes idénticas dan huellas distintas, porque `zip` guarda fechas. La huella de una release vale para el archivo publicado y no se obtiene reensamblando. El catálogo fija la del archivo que descargó, así que reemplazar un asset ya catalogado la invalida: una versión nueva se publica como etiqueta nueva, nunca sobrescribiendo una existente.

## Contrato lingüístico

No aplica como contrato de producto. El paquete se redacta íntegramente en **español**, incluidos documentos, comentarios y mensajes de las herramientas. El núcleo en español conserva la autoridad doctrinal.

## Este repositorio no ejecuta el ciclo SDD sobre sí mismo

**El «Flujo SpecKit obligatorio» de más arriba no aplica acá, y conviene saber por qué antes de instalar nada.**

Este proyecto **construye** el método; no construye un producto con `specs/`. No tiene especificación, ni plan, ni tareas, ni feature activa, y nunca invocó un comando `speckit.*`. Instalar el preset sobre este repositorio no verificaría nada que las herramientas de `tools/method/` no verifiquen mejor.

Por eso `.specify/` **no se versiona** y está en `.gitignore`. Si aparece en tu copia de trabajo, es tuya y local.

**Esto no significa que el repositorio esté fuera del manifiesto.** Se gobierna por él de otra manera, y esa sí se usa: las reglas de trabajo y las condiciones de detención de este archivo, las propuestas de `docs/proposals/` antes de aplicar cualquier cambio, y las comprobaciones que corren en cada ensamblado.

**Cómo se verifica este repositorio**, que es lo que reemplaza al ciclo:

- `tools/build-package.sh` — conformidad con el núcleo, vocabulario, integridad y el ensayo de instalación completo
- `tools/method/ensayo-de-instalacion.sh` — instala el paquete en un proyecto desechable y comprueba cada afirmación de la instrucción 01
- `tools/method/ensayo-de-resistencia.sh` — tres escenarios adversos sobre una instalación correcta

## Herramientas del proyecto

- **SpecKit**: `tools/speckit/specify`, que fija una instancia aislada en 1.0.8. La instalación global está en 0.15.0 al servicio de otros proyectos y **no debe actualizarse desde aquí**.
- **Scripts de SpecKit**: antepón siempre el shim, o la resolución de plantillas compuestas falla: `PATH="$PWD/tools/speckit/shim:$PATH" .specify/scripts/bash/<script>`
- **Ensamblado de la distribución**: `tools/build-package.sh`. Es idempotente, toma las fuentes canónicas, regenera `SHA256SUMS` y produce el ZIP en `dist/`.
- **Comprobación de entorno**: `tools/speckit/preflight.sh`.
- No hay gestor de paquetes: el repositorio no compila nada.

## Protocolo de coordinación entre sesiones

Este proyecto **sí** usa más de una sesión: esta mantiene el paquete de método, y otra construye el sitio del Manifiesto en `https://github.com/dacunao/sitio-software-humano`.

**Por qué existe este apartado.** Durante el desarrollo de este método, ocho rondas de mensajes cruzados entre ambas sesiones produjeron diecisiete de veinticinco commits sin que ninguna instrucción humana los originara, y la autoridad de producto quedó fuera de su propio proyecto. Está registrado como `M1` en `docs/proposals/003`. Dos agentes que se verifican mutuamente son ciegos a lo que ambos omiten.

- **Sesiones y autoridad**: esta sesión mantiene el manifiesto, el anexo, el preset, las instrucciones y el paquete distribuible. La del sitio construye el producto. Ninguna decide sobre el objeto de la otra.
- **Archivos que ambas pueden tocar**: en condiciones normales, **ninguno**. Los repositorios están separados desde `CL-13`. La única colisión observada fue `specs/001-sitio-manifiesto/tasks.md` durante `T007`, y se resolvió acordando que lo marcara su propia sesión.
- **Exige aprobación humana previa**: versionar el paquete o el preset; modificar el manifiesto, el anexo o cualquier artefacto rector; escribir en el repositorio de la otra sesión; y registrar un hallazgo sobre la conducta de las propias sesiones.
- **A quién reporta cada sesión**: a Damián Acuña. Nunca solo a la otra sesión.

**Regla de confirmación.** Ningún commit antes de que la autoridad haya visto de qué se trata.

**Estado vigente desde el 2026-09-21.** El diálogo directo entre sesiones está terminado por decisión de Damián. Si surge algo que exija coordinación, va primero a él.


## Archivos protegidos adicionales

Más allá de los protegidos por el método:

- `package/` y `tools/build-package.sh` — fuentes de la distribución. Modificarlas implica versionar el paquete y regenerar su `SHA256SUMS`.
- `docs/proposals/` — registro de mantenimiento. Se agrega, no se reescribe.

## Decisiones abiertas conocidas

No pueden cerrarse con un valor predeterminado. Requieren decisión de Damián Acuña.

- **Hallazgos del piloto.** Registrados en `docs/pilot/registro-del-piloto.md` del repositorio del sitio, evaluados en `docs/proposals/003`. Una propuesta no es una autorización.
- **`FR-009` del PRD del sitio** afirma que la adaptación «fue validada técnicamente en versión 1.0.0». La instalada y verificada es la 1.0.2. Corregirlo es decisión de la autoridad de producto del sitio, no de este repositorio.

## Decisiones ya resueltas

- **`docs/proposals/` se publica** — resuelto el 2026-09-30 por Damián Acuña, con el repositorio ya público y a la vista. El registro de mantenimiento queda accesible **incluido lo incómodo**: el costo de ejecución medido del análisis 007, los hallazgos negativos del piloto en la 010, `M1` de la 003 —donde la coordinación entre agentes desplazó a la autoridad de producto— y la 011, que registra que el paquete se apropia de archivos del proyecto que lo instala. No se retira nada ni se suaviza. `SH-DONE` rechaza «lo que falta sin que nadie lo sepa», y ocultar este registro sería incumplirlo en el propio repositorio que lo distribuye.

- **Qué se retira del repositorio antes de publicar** — resuelto el 2026-09-30 por Damián Acuña. Se retiraron el preset 1.2.0 y su ZIP, superados por el 2.0.1; `Software_Humano_Manifesto_Site_Starter_v1.0.0.zip`, que es la distribución del starter específico del sitio y **embebe el PRD de otro proyecto**; y los artefactos generados por la instalación —`.specify/` y `.claude/skills/`—, que estaban dos versiones atrás. Todo queda en la historia de git.

- **Licencias del paquete** — resueltas el 2026-09-21 por Damián Acuña. Frontera **por naturaleza y no por carpeta**: MIT para el preset, las herramientas, las instrucciones y el anexo v1.2; CC BY 4.0 para el texto del núcleo v2.1, incluida su proyección en `templates/constitution-template.md`. Ver `LICENSE`, `LICENSE` y `LICENSE-CONTENT`.
- **Licencia del preset** — MIT desde la v1.0.2. La versión 1.0.1 y anteriores declaraban una licencia propietaria que prohibía publicar, lo que volvía inejecutable `CL-10`.

---

# Deberes permanentes de este repositorio

Estos deberes **no son historias, requisitos ni tareas**, y por eso no tienen destino en ningún artefacto del flujo. Viven aquí porque `AGENTS.md` es el único archivo que toda sesión carga automáticamente.

La razón está en el hallazgo `C7` del registro del piloto: la obligación de registrar hallazgos viajó en el prompt de una sesión, y **un prompt muere con la sesión**. Al abrir la siguiente, el deber desaparece sin que nada lo señale. Si estos deberes solo viven en un prompt, dejan de existir en cuanto alguien abra una sesión sin repetirlos.

## `DP-01` · Evaluar los hallazgos del piloto

El sitio del Manifiesto es el piloto real de este paquete y mantiene su registro en `docs/pilot/registro-del-piloto.md` de su propio repositorio. Ese documento **observa y no propone**: evaluarlo corresponde a este repositorio.

Al abrir una sesión de mantenimiento, comprueba si el registro creció desde la última evaluación. Las entradas nuevas se evalúan en `docs/proposals/`, distinguiendo hecho observado, inferencia y decisión humana requerida.

**Evaluar no es aplicar.** Cambiar el manifiesto, el anexo o el preset exige decisión humana separada.

## `DP-02` · Regenerar `SHA256SUMS` al versionar el paquete

Cualquier cambio en `package/`, en `docs/method/` o en el preset obliga a:

1. incrementar la versión que corresponda, con entrada en el `CHANGELOG.md` del preset cuando sea él quien cambia;
2. ejecutar `tools/build-package.sh`, que regenera `SHA256SUMS` y el ZIP;
3. verificar que la integridad pasa antes de confirmar.

Un paquete cuya integridad no verifica no es distribuible. `SHA256SUMS` es el único mecanismo que permite a un proyecto instalado demostrar que su método no fue alterado.

**Y comprueba a quién invalida el número de versión que estás moviendo.** Un proyecto instalado puede tener en su fundamento una afirmación fáctica sobre el paquete —«validado técnicamente en la versión X», «licencia Y»— que el incremento vuelve falsa. `SHA256SUMS` comprueba que los archivos no cambiaron, no que las afirmaciones sobre ellos sigan siendo ciertas, y el desacoplamiento que protege al proyecto de propagaciones involuntarias **oculta también esa invalidación**.

Ocurrió: al incrementar el preset a 1.0.1 quedó obsoleto el `FR-009` del PRD del sitio, que afirma la validación «en versión 1.0.0». Ninguna capa lo detectó; apareció al redactar el contenido que debía afirmarlo. Antes de cerrar un incremento, identifica los proyectos instalados conocidos y avisa qué afirmación suya deja de ser cierta. Corregirla es decisión de su autoridad de producto, no tuya.

## `DP-03` · Mantener definida la frontera entre código y texto citado

El paquete mezcla dos naturalezas bajo licencias distintas: **código** —preset, scripts, herramientas, instrucciones— y **texto del manifiesto**, que el preset materializa como constitución.

Toda decisión de licencia, publicación o redistribución debe declarar de qué lado cae cada archivo. La frontera se define por naturaleza y no por carpeta. Mientras la decisión siga abierta, ninguna sesión puede resolverla por inferencia ni publicar el paquete.
