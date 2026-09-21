# Especificación: Sitio público del Manifiesto de Software Humano

**Rama**: `001-sitio-manifiesto`
**Creada**: 2026-09-21
**Estado**: Borrador — con decisiones materiales abiertas
**Entrada**: `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md` v1.0, como fundamento de producto autorizado

## Fuente y autoridad

- **Fuente autorizada**: `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md`, versión 1.0, fecha 2026-09-21, estado "Definición de producto para revisión".
- **Autoridad para modificar alcance**: Damián Acuña, autoridad de producto declarada en el PRD. Ni esta especificación ni ningún agente pueden aprobar cambios de alcance, resultados, exclusiones o estado de publicación (PRD §2.3).
- **Alcance declarado**: la totalidad de `JS-01`–`JS-09`, `FR-001`–`FR-021`, `AC-01`–`AC-16`, los objetivos de §12, los no objetivos de §13, el modelo de contenido de §19, los requisitos de UX/UI de §21, los requisitos no funcionales de §24, el descubrimiento de §25, la gobernanza editorial de §27 y la definición de terminado de §32. El PRD no declara prioridad, MVP, fases ni releases, y esta especificación no los introduce.
- **No objetivos explícitos** (PRD §13): enseñar exhaustivamente SpecKit; competir con su documentación oficial; publicar o distribuir el preset; afirmar respaldo, certificación o afiliación de GitHub; crear comunidad, academia, foro o red social; ofrecer certificaciones; generar un blog o sistema editorial complejo; personalizar el manifiesto por visitante; incluir un chatbot para demostrar IA; reemplazar la revisión humana por un score automático; permitir que el framework o la biblioteca de componentes dicten experiencia, identidad o arquitectura de información; construir un CMS si el contenido versionado puede administrarse de manera más simple.
- **Evidencia disponible**: el PRD declara en §26.3 que sus métricas cuantitativas son "hipótesis para calibración, no criterios universales de aceptación". La evidencia de comprensión aún no existe: debe producirse mediante las pruebas moderadas de §26.4. Esta especificación no presenta como observada ninguna conducta que todavía no haya sido medida.

**Fuentes rectoras subordinadas.** El núcleo v2.1 (`.specify/memory/constitution.md`) gobierna el método y es además contenido publicado del sitio (`FR-003`). El anexo v1.2 gobierna la correspondencia con SpecKit. El preset v1.0.0 gobierna su materialización técnica. Ante contradicción real o aparente entre el núcleo y el PRD, la decisión afectada se detiene; no se concilia por iniciativa del agente.

## Progreso y resultado esperado

- **Situación de partida**: una persona que concibe, diseña o construye software observa que la IA le permite producir más y más rápido, y sospecha que esa velocidad no está produciendo productos más comprensibles ni más útiles. Carece de un marco compartido para distinguir capacidad técnica de progreso humano (PRD §6.1, §6.2).
- **Motivación o tensión**: necesita criterios capaces de cambiar una decisión, exigir evidencia o detener una implementación, no una lista de consignas inspiracionales (PRD §12.2).
- **Resultado buscado**: al terminar el recorrido la persona puede explicar el problema que origina el manifiesto, expresar su tesis con palabras propias, reconocer los diez principios y cuándo aplican, utilizar sus preguntas para evaluar una decisión real, distinguir doctrina de método y de implementación, explicar qué aporta SpecKit y qué no representa, y acceder al texto canónico completo para citarlo (PRD §11.3).
- **Personas afectadas**: product managers, diseñadores de producto y UX, ingenieros y líderes técnicos, fundadores, y creadores de agentes y automatizaciones (PRD §14.1). El rol no gobierna el diseño; se registra porque el PRD define para cada audiencia un progreso distinto. El sitio no exige experiencia previa en SpecKit, SDD, Jobs to Be Done ni Job Stories (PRD §14.3).

**Condición transversal.** El sitio es la primera aplicación pública del propio manifiesto y el primer proyecto real desarrollado con la adaptación Software Humano para SpecKit (PRD §1, §12.7, §12.8). Su comportamiento debe demostrar lo que su texto sostiene. Un incumplimiento de experiencia, accesibilidad, rendimiento o control no es un defecto secundario: contradice el contenido publicado.

## Estructura de producto preservada

Las nueve Job Stories se conservan con la circunstancia, la motivación y el resultado que establece el PRD §15. El orden permite construir una narrativa y **no expresa prioridad ni autoriza a omitir ninguna historia** (PRD §15, encabezado).

### `JS-01` Comprender el problema

- **Tipo en la fuente**: Job Story.
- **Definición**: **Cuando** observo que la IA permite construir más software y más rápido, pero sospecho que eso no necesariamente produce mejores productos, **quiero** comprender qué riesgo humano y de producto aparece detrás de esa velocidad, **para poder** distinguir progreso real de producción técnica.
- **Dependencias**: ninguna. Es la entrada del recorrido.
- **Reglas y límites**: la explicación no puede recurrir al miedo tecnológico ni presentar la IA como enemiga; el problema no es que la IA construya, sino construir sin fundamento, límites ni evidencia (PRD §7).
- **Resultado verificable**: la persona explica por qué "más capacidad para construir" no equivale a "más capacidad para progresar".

#### Escenarios de aceptación

1. **Dado** un visitante sin contexto previo que llega a la portada, **cuando** recorre el Acto 1 y el Acto 2 del recorrido narrativo, **entonces** puede enunciar el riesgo sin nombrar primero una funcionalidad del sitio (PRD §26.1).
2. **Dado** un visitante que desactivó JavaScript, **cuando** abre la portada, **entonces** el contenido que sostiene esta comprensión sigue disponible (`FR-015`).

### `JS-02` Descubrir la tesis

- **Tipo en la fuente**: Job Story.
- **Definición**: **Cuando** reconozco que muchas interfaces me obligan a administrar la herramienta en vez de resolver mi necesidad, **quiero** encontrar una afirmación clara que reoriente el diseño, **para poder** evaluar el software desde el progreso de la persona.
- **Dependencias**: `JS-01` establece la tensión que la tesis resuelve.
- **Reglas y límites**: la tesis se presenta junto al texto canónico breve del manifiesto (PRD §16, Acto 3); la explicación editorial no puede sustituir ni parafrasear el texto canónico dentro de la superficie canónica (PRD §19.1).
- **Resultado verificable**: la persona formula la tesis del manifiesto con sus propias palabras.

#### Escenarios de aceptación

1. **Dado** un visitante que alcanzó el Acto 3, **cuando** se le pide explicar la tesis, **entonces** expresa que el progreso humano y la experiencia forman parte del producto (`AC-02`).
2. **Dado** un visitante que llega directamente a la superficie de la tesis por un enlace compartido, **cuando** la abre, **entonces** conserva contexto suficiente y acceso al texto completo (`JS-08`, `FR-011`).

### `JS-03` Comprender cada principio

- **Tipo en la fuente**: Job Story.
- **Definición**: **Cuando** una decisión de producto parece razonable pero no sé qué efecto tendrá sobre la experiencia, **quiero** comprender qué observa, exige y permite probar cada principio, **para poder** utilizarlo como criterio y no solo como inspiración.
- **Dependencias**: `JS-02`. Cada principio debe poder abrirse también sin recorrer la narrativa (`FR-002`).
- **Reglas y límites**: cada principio `P01`–`P10` mantiene el mismo contrato de contenido de PRD §17 —declaración, tensión, significado, consecuencia, ejemplo, contraejemplo, prueba de decisión y fuente— sin alterar su identidad ni su orden canónico. La narrativa puede enmarcarlos en los cuatro capítulos de presentación de PRD §16 (Propósito `P01`–`P02`; Complejidad y atención `P03`–`P06`; Confianza y continuidad `P07`–`P09`; Agencia humana `P10`), y ese encuadre no crea una jerarquía nueva.
- **Resultado verificable**: la persona relaciona una situación con el principio aplicable y explica por qué.

#### Escenarios de aceptación

1. **Dado** un visitante en la superficie de principios, **cuando** abre cualquiera de `P01`–`P10`, **entonces** encuentra las ocho secciones del contrato de contenido y el vínculo al pasaje canónico con su identificador (`FR-004`, `FR-006`, `AC-04`).
2. **Dado** un visitante al que se le presentan tres principios cercanos, **cuando** se le pide distinguirlos, **entonces** lo hace sin confundirlos (PRD §26.1).

### `JS-04` Experimentar la diferencia

- **Tipo en la fuente**: Job Story.
- **Definición**: **Cuando** un concepto abstracto no basta para cambiar mi manera de diseñar, **quiero** comparar respuestas centradas en el sistema y respuestas centradas en la persona, **para poder** reconocer la diferencia en decisiones concretas.
- **Dependencias**: `JS-03`.
- **Reglas y límites**: los ejemplos interactivos deben tener alternativa textual equivalente (PRD §21.3); la comparación no puede convertirse en regla doctrinal nueva (`FR-005`); debe funcionar con movimiento reducido (`FR-013`).
- **Resultado verificable**: la persona identifica qué complejidad, carga o pérdida de control introduce una alternativa.

#### Escenarios de aceptación

1. **Dado** un visitante con `prefers-reduced-motion` activo, **cuando** usa la comparación del Acto 2, **entonces** obtiene la misma información sin movimiento no esencial (`FR-013`, `AC-06`).
2. **Dado** un visitante que navega solo con teclado, **cuando** recorre la comparación, **entonces** alcanza y opera todos sus estados con foco visible (`AC-07`).

### `JS-05` Consultar y citar la fuente

- **Tipo en la fuente**: Job Story.
- **Definición**: **Cuando** necesito estudiar, discutir o utilizar el manifiesto en un proyecto, **quiero** acceder al texto canónico, su versión y anclas estables, **para poder** verificar el significado y citarlo sin depender de un resumen.
- **Dependencias**: ninguna. Debe alcanzarse desde cualquier superficie (PRD §18.2).
- **Reglas y límites**: el núcleo v2.1 se publica íntegro, con índice, identificadores y enlaces estables (`FR-003`); el texto canónico traducido debe distinguirse del original en español, que conserva la autoridad doctrinal (PRD §19.4).
- **Resultado verificable**: cualquier principio o sección canónica se alcanza directamente y posee una URL o ancla estable.

#### Escenarios de aceptación

1. **Dado** un visitante que conoce un identificador del núcleo, **cuando** abre su ancla, **entonces** llega a la sección correcta y ve versión, fecha y procedencia (`FR-012`, `AC-11`).
2. **Dado** un visitante en `/es/`, **cuando** consulta el texto canónico traducido, **entonces** reconoce que es traducción y encuentra la referencia al original en español (PRD §19.4).

### `JS-06` Pasar de doctrina a práctica

- **Tipo en la fuente**: Job Story.
- **Definición**: **Cuando** estoy de acuerdo con los principios pero no sé cómo incorporarlos al desarrollo cotidiano, **quiero** comprender el flujo, los artefactos, el contrato del agente y la verificación, **para poder** convertir el manifiesto en decisiones y evidencia.
- **Dependencias**: `JS-03`.
- **Reglas y límites**: la explicación cubre fundamento de producto, Job Stories como forma de referencia, flujo, artefactos, contrato reutilizable, razones de detención y definición de terminado (`FR-007`); debe traducir los conceptos antes de mostrar detalles técnicos y no abrir con rutas, archivos, YAML o comandos (PRD §17, `P03`).
- **Resultado verificable**: la persona explica al menos un punto donde el manifiesto puede cambiar o detener el desarrollo.

#### Escenarios de aceptación

1. **Dado** un visitante sin experiencia en SDD, **cuando** recorre la superficie de aplicación, **entonces** identifica una razón de detención concreta sin haber leído documentación técnica previa (`FR-007`, PRD §14.3).

### `JS-07` Comprender la implementación en SpecKit

- **Tipo en la fuente**: Job Story.
- **Definición**: **Cuando** utilizo o evalúo desarrollo guiado por especificaciones con agentes, **quiero** ver cómo la constitución y el preset adaptan SpecKit sin sustituirlo, **para poder** entender qué permanece nativo y qué cambia por el manifiesto.
- **Dependencias**: `JS-06`. SpecKit se introduce después del método y con papel subordinado (PRD §28).
- **Reglas y límites**: la superficie debe declarar que la adaptación es independiente, usa presets nativos, no modifica el core, fue validada técnicamente en la versión 1.0.0, **no está publicada todavía** y no constituye integración oficial ni respaldo de GitHub (`FR-009`). Mientras el preset no esté publicado no debe mostrarse una instalación pública operativa (`FR-010`).
- **Resultado verificable**: la persona distingue núcleo, anexo, preset y SpecKit, y no interpreta la adaptación como oficial.

#### Escenarios de aceptación

1. **Dado** un visitante en la superficie de SpecKit, **cuando** la lee, **entonces** puede nombrar las cuatro capas y su relación de autoridad, y afirma que la adaptación no está publicada (`AC-09`).
2. **Dado** el preset sin publicar, **cuando** el visitante busca cómo instalarlo, **entonces** encuentra estado y arquitectura pero ninguna instrucción de instalación pública operativa (`FR-010`).

### `JS-08` Compartir una idea precisa

- **Tipo en la fuente**: Job Story.
- **Definición**: **Cuando** quiero conversar con otra persona sobre un principio o una decisión, **quiero** compartir una sección autocontenida con contexto suficiente, **para poder** iniciar la conversación sin enviar un documento completo ni perder rigor.
- **Dependencias**: `JS-05` para las URLs estables.
- **Reglas y límites**: la copia o compartición usa contenido preciso y no atribuye una explicación editorial al texto canónico (`FR-011`); compartir o copiar no puede capturar datos innecesarios (`P10`, PRD §17).
- **Resultado verificable**: el enlace compartido abre el principio o sección correcta, conserva contexto y ofrece acceso al texto completo.

#### Escenarios de aceptación

1. **Dado** un visitante que comparte el enlace de `P07`, **cuando** el destinatario lo abre, **entonces** llega a `P07` con contexto y con acceso al texto canónico (`AC-11`).
2. **Dado** un visitante que copia una cita, **cuando** la pega, **entonces** el texto distingue cita canónica de explicación editorial (`FR-017`).

### `JS-09` Comprender en mi idioma y conservar mi elección

- **Tipo en la fuente**: Job Story.
- **Definición**: **Cuando** accedo al manifiesto desde un contexto lingüístico distinto o prefiero leerlo en otro idioma, **quiero** elegir entre inglés general, español neutro latinoamericano y portugués de Brasil y mantener esa preferencia durante mi recorrido, **para poder** comprender, navegar y compartir el contenido sin perder contexto ni quedar atrapado en una versión incorrecta.
- **Dependencias**: atraviesa todas las superficies. Toda `JS-01`–`JS-08` debe cumplirse en los tres idiomas.
- **Reglas y límites**: rutas sin prefijo sirven inglés; `/es/` español neutro latinoamericano; `/pt-br/` portugués de Brasil con código `pt-BR` en metadatos; sin redirección automática por idioma del navegador en la primera visita; una URL localizada explícita siempre prevalece sobre la preferencia guardada (`FR-019`, `FR-020`).
- **Resultado verificable**: sin preferencia previa, la persona recibe inglés en una ruta sin prefijo; luego puede cambiar de idioma desde cualquier superficie, llegar a la sección equivalente, conservar su elección de manera local y reconocer qué versión lingüística está leyendo.

#### Escenarios de aceptación

1. **Dado** un visitante sin preferencia guardada y con navegador en portugués, **cuando** abre `/`, **entonces** recibe inglés sin redirección automática (`FR-020`, `AC-14`).
2. **Dado** un visitante leyendo `P05` en `/es/`, **cuando** cambia a portugués, **entonces** llega a `P05` en `/pt-br/` y no a la portada (`AC-14`).
3. **Dado** un visitante con preferencia guardada en español, **cuando** abre una URL `/pt-br/` compartida, **entonces** ve portugués y la preferencia no sustituye la URL explícita (`FR-019`, `AC-14`).

## Cobertura del alcance

Todo elemento obligatorio del PRD aparece al menos una vez. **Pendiente de aclaración** señala que el elemento está representado pero depende de una decisión material abierta; no significa que quede fuera del alcance.

### Job Stories

| ID de fuente | Elemento obligatorio | Destino en esta especificación | Evidencia de aceptación | Estado |
|---|---|---|---|---|
| `JS-01` | Comprender el problema | Estructura preservada · `JS-01` | Explicación con palabras propias; prueba moderada | Cubierto |
| `JS-02` | Descubrir la tesis | Estructura preservada · `JS-02` | Comprensión sin asistencia | Cubierto |
| `JS-03` | Comprender cada principio | Estructura preservada · `JS-03` | Asociación de escenario y principio | Cubierto |
| `JS-04` | Experimentar la diferencia | Estructura preservada · `JS-04` | Comparación accesible y explicación del impacto | Cubierto |
| `JS-05` | Consultar y citar la fuente | Estructura preservada · `JS-05` | URL estable, versión y fuente | Cubierto |
| `JS-06` | Pasar de doctrina a práctica | Estructura preservada · `JS-06` | Identificación de una decisión o detención | Cubierto |
| `JS-07` | Comprender SpecKit | Estructura preservada · `JS-07` | Distinción correcta y estado comprendido | Pendiente de aclaración (`CL-06`) |
| `JS-08` | Compartir una idea precisa | Estructura preservada · `JS-08` | Enlace contextual y atribución correcta | Cubierto |
| `JS-09` | Comprender en mi idioma | Estructura preservada · `JS-09` | Paridad, cambio contextual, preferencia reversible | Pendiente de aclaración (`CL-09`) |

### Requisitos funcionales

| ID de fuente | Elemento obligatorio | Destino en esta especificación | Evidencia de aceptación | Estado |
|---|---|---|---|---|
| `FR-001` | Narrativa progresiva | Requisitos · `FR-001` | `AC-01`, `AC-02`, `AC-05` | Cubierto |
| `FR-002` | Navegación no lineal | Requisitos · `FR-002` | `AC-06` | Cubierto |
| `FR-003` | Texto canónico íntegro | Requisitos · `FR-003` | `AC-03` | Cubierto |
| `FR-004` | Explorador de principios | Requisitos · `FR-004` | `AC-03`, `AC-04` | Cubierto |
| `FR-005` | Ejemplos y contraejemplos | Requisitos · `FR-005` | `AC-04` | Cubierto |
| `FR-006` | Pruebas de decisión | Requisitos · `FR-006` | `AC-04` | Cubierto |
| `FR-007` | Aplicación operativa | Requisitos · `FR-007` | `JS-06` | Cubierto |
| `FR-008` | Presentación de SpecKit | Requisitos · `FR-008` | `AC-09` | Cubierto |
| `FR-009` | Estado verificable de SpecKit | Requisitos · `FR-009` | `AC-09` | Cubierto |
| `FR-010` | Acciones según estado de publicación | Requisitos · `FR-010` | `AC-09` | Pendiente de aclaración (`CL-06`) |
| `FR-011` | Compartir y citar | Requisitos · `FR-011` | `AC-11` | Cubierto |
| `FR-012` | Versiones y procedencia | Requisitos · `FR-012` | `AC-11` | Pendiente de aclaración (`CL-02`, `CL-05`) |
| `FR-013` | Preferencia de movimiento | Requisitos · `FR-013` | `AC-06`, `AC-07` | Cubierto |
| `FR-014` | Continuidad de lectura | Requisitos · `FR-014` | `AC-06` | Cubierto |
| `FR-015` | Función esencial sin JavaScript | Requisitos · `FR-015` | `AC-05`, `AC-08` | Cubierto |
| `FR-016` | Descubrimiento | Requisitos · `FR-016` | `AC-11`, `AC-15` | Cubierto |
| `FR-017` | Transparencia de contenido derivado | Requisitos · `FR-017` | `AC-03`, `AC-09` | Cubierto |
| `FR-018` | Privacidad | Requisitos · `FR-018` | `AC-12` | Pendiente de aclaración (`CL-08`) |
| `FR-019` | Experiencia multilingüe | Requisitos · `FR-019` | `AC-13`, `AC-14` | Cubierto |
| `FR-020` | Ajustes de idioma y experiencia | Requisitos · `FR-020` | `AC-14` | Cubierto |
| `FR-021` | Contenido como software | Requisitos · `FR-021` | `AC-15` | Cubierto |

### Criterios de aceptación

| ID de fuente | Elemento obligatorio | Destino en esta especificación | Evidencia de aceptación | Estado |
|---|---|---|---|---|
| `AC-01` | Comprensión del problema | Evidencia · `AC-01` | Prueba moderada con audiencias principales | Cubierto |
| `AC-02` | Comprensión de la tesis | Evidencia · `AC-02` | Prueba moderada | Cubierto |
| `AC-03` | Integridad doctrinal | Evidencia · `AC-03` | Comparación contra núcleo v2.1 | Cubierto |
| `AC-04` | Aplicabilidad | Evidencia · `AC-04` | Revisión de contenido por principio | Cubierto |
| `AC-05` | Profundidad progresiva | Evidencia · `AC-05` | Prueba de navegación sin explicación previa | Cubierto |
| `AC-06` | Control | Evidencia · `AC-06` | Prueba de navegación, compartición y movimiento reducido | Cubierto |
| `AC-07` | Accesibilidad | Evidencia · `AC-07` | Auditoría WCAG 2.2 AA y revisión humana con teclado y lector de pantalla | Cubierto |
| `AC-08` | Rendimiento | Evidencia · `AC-08` | Auditoría contra presupuestos de §24.1 | Cubierto |
| `AC-09` | SpecKit preciso | Evidencia · `AC-09` | Revisión de contenido y prueba de comprensión | Pendiente de aclaración (`CL-06`) |
| `AC-10` | Desarrollo gobernado | Evidencia · `AC-10` | `analyze` y revisión humana de artefactos | Cubierto |
| `AC-11` | Descubrimiento y cita | Evidencia · `AC-11` | Comprobación de URLs, metadatos y vínculos | Cubierto |
| `AC-12` | Privacidad | Evidencia · `AC-12` | Lectura completa sin registro ni datos personales | Pendiente de aclaración (`CL-08`) |
| `AC-13` | Paridad multilingüe | Evidencia · `AC-13` | Revisión lingüística humana en tres idiomas | Pendiente de aclaración (`CL-09`) |
| `AC-14` | Preferencia y continuidad de idioma | Evidencia · `AC-14` | Prueba de cambio de idioma y correspondencia de URLs | Cubierto |
| `AC-15` | Contenido y semántica verificables | Evidencia · `AC-15` | Validación de YAML, enlaces y JSON-LD en build | Cubierto |
| `AC-16` | Integridad TypeScript | Evidencia · `AC-16` | Comprobación estricta de tipos sin errores | Cubierto |

### Principios rectores

| ID de fuente | Elemento obligatorio | Destino en esta especificación | Evidencia de aceptación | Estado |
|---|---|---|---|---|
| `P01` | Progreso como unidad de diseño | Contrato de experiencia; `FR-001`; §17 del PRD por principio | `AC-01`, `AC-04` | Cubierto |
| `P02` | Experiencia como funcionalidad | Contrato de experiencia; `FR-013`, `FR-014` | `AC-02`, `AC-06`, `AC-07` | Cubierto |
| `P03` | Complejidad en el sistema | `FR-007`, `FR-008`; `BR-004` | `AC-09` | Cubierto |
| `P04` | Simple al comenzar, profundo al necesitarlo | `FR-001`, `FR-004` | `AC-05` | Cubierto |
| `P05` | La interfaz no es otra tarea | `FR-002`; `ST-001`–`ST-005` | `AC-05`, `AC-06` | Cubierto |
| `P06` | La atención es un recurso | `FR-013`; §21.2 del PRD | `AC-06` | Cubierto |
| `P07` | La confianza se diseña | `FR-009`, `FR-012`, `FR-017` | `AC-09`, `AC-11` | Cubierto |
| `P08` | Calidad acumulativa | `ST-001`–`ST-005`; §21.4 del PRD | `AC-07` | Cubierto |
| `P09` | Tiempo y continuidad | `FR-014`, `FR-015`; §24.1 del PRD | `AC-08` | Cubierto |
| `P10` | Control y propiedad | `FR-011`, `FR-018`, `FR-020` | `AC-06`, `AC-12` | Cubierto |

### Objetivos, no objetivos y superficies

| ID de fuente | Elemento obligatorio | Destino en esta especificación | Evidencia de aceptación | Estado |
|---|---|---|---|---|
| PRD §12.1–§12.10 | Diez objetivos de producto | Progreso y resultado esperado; cobertura completa | `AC-01`–`AC-16` | Cubierto |
| PRD §13 | Doce no objetivos | Fuente y autoridad · No objetivos; `BR-006` | Ausencia verificada en `analyze` y revisión humana | Cubierto |
| PRD §18.1 | Seis superficies obligatorias | `FR-001`–`FR-010`; contrato de experiencia | `AC-05`, `AC-11` | Cubierto |
| PRD §18.2 | Navegación global | `FR-002`, `FR-012`, `FR-020` | `AC-06`, `AC-14` | Cubierto |
| PRD §19.2 | Entidad Principio | Entidades clave · Principio | `AC-03`, `AC-15` | Cubierto |
| PRD §19.3 | YAML como fuente de contenido | `FR-021`; `BR-007` | `AC-15` | Cubierto |
| PRD §19.4 | Contrato de localización | `FR-019`; `BR-001`–`BR-003` | `AC-13`, `AC-14` | Pendiente de aclaración (`CL-09`) |
| PRD §21.5 | Doce verificaciones de accesibilidad | Evidencia · `AC-07` | Auditoría y revisión humana | Cubierto |
| PRD §24.1 | Presupuestos de Core Web Vitals | Evidencia · `AC-08`; `SC-006` | Medición en percentil 75 | Cubierto |
| PRD §24.2 | Confiabilidad y continuidad | `ST-004`; `EX-001`–`EX-003` | Comprobación de enlaces y despliegue reversible | Pendiente de aclaración (`CL-11`) |
| PRD §24.3 | Seguridad y privacidad | `FR-018`; `BR-008` | `AC-12` | Pendiente de aclaración (`CL-08`, `CL-11`) |
| PRD §24.5 | Mantenibilidad | `BR-007`; `AS-006` | `AC-15`, `AC-16` | Cubierto |
| PRD §24.6 | Arquitectura técnica aprobada | Restricciones técnicas aprobadas | `AC-16` | Cubierto |
| PRD §25.2 | Mapeo semántico mínimo | `FR-016`; entidades clave | `AC-15` | Pendiente de aclaración (`CL-02`) |
| PRD §27 | Gobernanza editorial | `BR-005`, `BR-009` | Revisión humana | Pendiente de aclaración (`CL-09`) |
| PRD §32 | Definición de terminado | Evidencia y criterios de éxito | Revisión humana final | Cubierto |

## Contrato de experiencia

- **Lenguaje y modelo mental**: claro, directo, preciso; humano sin infantilizar; técnico solo cuando mejora la comprensión; sin grandilocuencia sobre IA; sin presentar recomendaciones como hechos; con frases canónicas claramente diferenciadas de la explicación editorial (PRD §21.6). Los conceptos se explican cuando aparecen, sin obligar al lector experto a atravesar explicaciones básicas (PRD §14.3).
- **Inicio simple**: la portada presenta una idea dominante por momento y conduce del problema a la tesis sin exigir conocimientos previos (`FR-001`, PRD §21.1). No se muestra todo a la vez ni se oculta el contenido tras una portada mínima (PRD §17, `P04`).
- **Profundidad progresiva**: significado, aplicación y fuente se revelan a demanda, sin callejones sin salida (PRD §17, `P04`). Los acordeones y capas conservan títulos explícitos y estados accesibles (PRD §21.3).
- **Feedback y estado**: orientación visible sobre dónde estoy, qué significa y qué puedo hacer (PRD §21.1). El idioma activo es perceptible para la persona y para tecnologías de asistencia (PRD §21.7). Progreso honesto solo cuando exista una operación perceptible (PRD §17, `P09`).
- **Control y recuperación**: navegación libre; no se secuestra el scroll; el visitante puede detenerse, saltar, retroceder y abrir una URL profunda (PRD §21.3). Movimiento reducible sin pérdida de información (`FR-013`). Contenido copiable y URLs estables (PRD §17, `P10`). Página 404 útil y orientadora (PRD §24.2). Sin registro, sin audio automático, sin captura innecesaria de datos.
- **Continuidad**: el regreso a una URL profunda restituye la sección correcta; cualquier preservación adicional de progreso es local, transparente y prescindible (`FR-014`). La preferencia de idioma es local, reversible y prescindible (`FR-020`).
- **Accesibilidad y carga**: WCAG 2.2 nivel AA como mínimo, con las doce verificaciones de PRD §21.5. Jerarquía equivalente en móvil, tablet y escritorio; los diagramas se reestructuran en lugar de reducirse hasta volverse ilegibles; el orden de lectura semántico permanece correcto sin CSS; no se exige orientación horizontal ni gestos complejos (PRD §21.4). Toda información revelada por hover está disponible por foco y por toque (PRD §21.3).

**Dirección visual.** La identidad debe sentirse humana, deliberada y contemporánea, sin adoptar una estética genérica de "producto de IA": tipografía de lectura sobresaliente, amplitud y ritmo editorial, uso contenido del color para significado y orientación, e imágenes, diagramas o movimiento solo cuando expliquen una relación (PRD §21.2). El PRD declara expresamente que **no prescribe una marca gráfica antes de comprender su efecto**: la dirección visual definitiva debe explorarse y validarse.

## Requisitos

Los identificadores `FR-001`–`FR-021` son los del PRD §20 y se conservan sin renumerar.

### Requisitos funcionales

- **`FR-001`**: El sistema DEBE presentar el recorrido problema → consecuencias → tesis → principios → aplicación → SpecKit sin exigir conocimientos previos.
- **`FR-002`**: El sistema DEBE permitir que el visitante abandone la secuencia, acceda directamente a cualquier superficie y regrese sin perder orientación.
- **`FR-003`**: El sistema DEBE publicar el núcleo v2.1 completo, con índice, identificadores y enlaces estables.
- **`FR-004`**: El sistema DEBE permitir recorrer y abrir individualmente `P01`–`P10`, conservando orden, identidad y fuente.
- **`FR-005`**: Cada principio DEBE incluir al menos una situación que permita reconocer su aplicación o incumplimiento, sin convertirla en regla nueva.
- **`FR-006`**: Cada principio DEBE exponer preguntas que el visitante pueda utilizar en una revisión de producto.
- **`FR-007`**: El sistema DEBE explicar fundamento de producto, Job Stories como forma de referencia, flujo, artefactos, contrato del agente, detenciones y definición de terminado.
- **`FR-008`**: El sistema DEBE explicar la relación entre núcleo, constitución, anexo, preset y SpecKit nativo.
- **`FR-009`**: La superficie de SpecKit DEBE indicar que la adaptación es independiente, utiliza presets nativos, no modifica el core, fue validada técnicamente en versión 1.0.0, no está publicada todavía, y no constituye una integración oficial ni un respaldo de GitHub.
- **`FR-010`**: Mientras el preset no esté publicado, el sistema NO DEBE mostrar una instalación pública operativa. PUEDE mostrar estado, arquitectura e indicación de disponibilidad futura. Cuando exista publicación autorizada, incorporar enlace e instrucciones REQUERIRÁ actualización de contenido y validación.
- **`FR-011`**: El sistema DEBE ofrecer URLs estables para principios y secciones. La copia o compartición DEBE utilizar contenido preciso y NO DEBE atribuir una explicación editorial al texto canónico.
- **`FR-012`**: El visitante DEBE poder identificar versión del núcleo, fecha de actualización, procedencia del contenido y estado del preset.
- **`FR-013`**: El sistema DEBE respetar `prefers-reduced-motion` y ofrecer una experiencia completa sin movimiento no esencial.
- **`FR-014`**: El regreso a una URL profunda DEBE restituir la sección correcta. Cualquier preservación adicional de progreso DEBE ser local, transparente y prescindible.
- **`FR-015`**: El texto, la navegación primaria, las URLs profundas y el contenido canónico DEBEN seguir disponibles si JavaScript falla o está deshabilitado. Las mejoras interactivas DEBEN incorporarse mediante mejora progresiva.
- **`FR-016`**: El sistema DEBE proporcionar títulos, descripciones, encabezados, enlaces internos, sitemap, URLs canónicas y datos estructurados basados en Schema.org para que personas, buscadores y agentes comprendan jerarquía, idioma y procedencia.
- **`FR-017`**: El sistema DEBE distinguir visual y semánticamente cita canónica, explicación, ejemplo, inferencia o propuesta, y estado técnico confirmado.
- **`FR-018`**: La lectura NO DEBE requerir cuenta, registro ni entrega de datos personales. Cualquier medición DEBE minimizar datos, documentar su propósito y NO DEBE bloquear el contenido por falta de consentimiento.
- **`FR-019`**: Todo el alcance público DEBE estar disponible en `en`, `es` y `pt-BR`, cada versión con URL propia, atributo `lang`, metadatos localizados, enlaces `hreflang` recíprocos y correspondencia con la misma entidad conceptual. Las rutas sin prefijo —incluida `/`— sirven inglés; `/es/` sirve español; `/pt-br/` sirve portugués de Brasil manteniendo `pt-BR` en metadatos. Una URL localizada explícita SIEMPRE prevalece sobre cualquier preferencia almacenada.
- **`FR-020`**: El visitante DEBE poder cambiar el idioma desde cualquier superficie sin perder, cuando exista, la sección equivalente. La elección DEBE conservarse localmente, poder modificarse o restablecerse, y NO DEBE requerir una cuenta. En la primera visita, una ruta sin prefijo DEBE mostrarse en inglés sin redirección automática basada en el idioma del navegador. La superficie de ajustes DEBE agrupar únicamente preferencias reales del producto —inicialmente idioma y comportamiento de movimiento cuando corresponda.
- **`FR-021`**: El contenido DEBE originarse en YAML versionado en GitHub y validarse durante integración y build. Una modificación DEBE permitir conocer qué cambió, quién la aprobó, qué idiomas afecta y qué páginas o datos estructurados genera.

### Reglas, estados y excepciones

- **`BR-001`**: Inglés general (`en`) es el idioma predeterminado y ocupa las rutas sin prefijo. `es` y `pt-BR` son versiones completas de lanzamiento, no resúmenes (PRD §19.4).
- **`BR-002`**: La versión española usa `tú` y `ustedes`. Prohíbe voseo (`vos`, `sos`, `tenés`, `podés`), `vosotros` y sus conjugaciones, y modismos, humor, giros o vocabulario exclusivos de un país (PRD §21.6). La versión 1.0 no crea variantes por país.
- **`BR-003`**: Toda entrada traducible comparte el mismo `id` y declara su código de idioma BCP 47. No se publicará una página como disponible en un idioma si su contenido principal conserva fragmentos no aprobados de otro idioma. Las traducciones no pueden modificar identificadores, relaciones, alcance ni estado del contenido (PRD §19.4, §27.4).
- **`BR-004`**: El texto canónico no se parafrasea dentro de la superficie canónica. La explicación editorial debe referenciar el principio o sección de origen. El ejemplo y el contraejemplo deben identificarse como tales y no como doctrina adicional (PRD §19.1).
- **`BR-005`**: El contenido distingue al menos seis estados editoriales: canónico aprobado, explicación aprobada, ejemplo aprobado, borrador, estado técnico verificado y propuesta futura (PRD §27.1).
- **`BR-006`**: La experiencia pública de la versión 1.0 es determinista. No existe función generativa visible para el visitante. Cualquier capacidad de IA futura requiere Job Story, límites, tratamiento de incertidumbre y evidencia de que reduce carga, antes de autorizarse (PRD §22).
- **`BR-007`**: El build DEBE detenerse ante identificadores duplicados, relaciones rotas, campos obligatorios ausentes o traducciones requeridas incompletas (PRD §19.3). Debe detenerse también ante errores de tipado estricto de TypeScript (PRD §24.6).
- **`BR-008`**: No se recopilan datos que el producto no utilice. No se incorporan claves ni secretos en cliente. Ningún script de terceros puede degradar privacidad, rendimiento o accesibilidad sin decisión aprobada (PRD §24.3).
- **`BR-009`**: El marcado estructurado describe únicamente contenido visible. No se publica marcado que describa contenido inexistente. Se prefiere menor cantidad de propiedades completas y verdaderas sobre marcado extenso o especulativo (PRD §25.2).
- **`ST-001`** *(vacío)*: una superficie sin contenido aprobado en un idioma no se publica como disponible en ese idioma (`BR-003`).
- **`ST-002`** *(carga)*: el contenido inicial no depende de una animación o petición tardía. Los fallos de recursos secundarios no impiden leer (PRD §24.1).
- **`ST-003`** *(éxito)*: al compartir o copiar, el visitante recibe confirmación clara y sin captura innecesaria de datos (PRD §17, `P10`).
- **`ST-004`** *(error)*: la página 404 es útil y orientadora y ofrece rutas de vuelta al recorrido y al texto canónico (PRD §24.2).
- **`ST-005`** *(recuperación e interrupción)*: el regreso a una URL profunda restituye la sección correcta; el cambio de idioma conserva la entidad actual cuando existe equivalencia (`FR-014`, `FR-020`).
- **`EX-001`**: si JavaScript falla o está deshabilitado, el texto, la navegación primaria, las URLs profundas y el contenido canónico permanecen disponibles (`FR-015`).
- **`EX-002`**: si no existe traducción aprobada de una sección equivalente, el cambio de idioma debe informar la ausencia y ofrecer una alternativa comprensible, sin mezclar idiomas en la página publicada (`BR-003`, `FR-020`).
- **`EX-003`**: si cambia la estructura de URLs, deben existir redirecciones y el contenido canónico permanece versionado (PRD §24.2).

### Restricciones técnicas aprobadas

El PRD §24.6 las aprueba. Solo pueden reemplazarse mediante decisión explícita de producto y registro técnico que demuestre incompatibilidad material; preferencia personal o conveniencia del agente no bastan.

- **TypeScript estricto** para lógica, componentes, integraciones, validadores, pruebas y configuración compatible. El build falla ante errores de tipado. Se evita `any`; toda excepción debe ser localizada, explicada y verificable. Los tipos no sustituyen la validación en tiempo de ejecución de entradas provenientes de archivos, navegador o servicios externos.
- **Astro** como framework, con generación estática por defecto y HTML utilizable antes de ejecutar JavaScript. La arquitectura de islas se reserva para interacciones que realmente lo requieran, como ajustes persistentes o comparaciones interactivas. `defaultLocale` es inglés; rutas inglesas sin prefijo, `/es/` y `/pt-br/` con la misma topología. El cambio de idioma es navegación entre URLs equivalentes, no sustitución de texto en cliente.
- **daisyUI sobre Tailwind CSS** como biblioteca base de componentes, subordinada a la identidad visual y a WCAG 2.2 AA. Todo componente parte de HTML semántico, se personaliza mediante tokens propios, cumple foco, teclado, contraste, reflow y estados, evita clases no utilizadas en la salida final, y puede sustituirse localmente cuando contradiga una decisión del manifiesto.
- **YAML versionado en GitHub** como fuente de contenido, con validación mediante esquema formal capaz de detener el build.
- **JSON-LD y Schema.org** generados desde la misma fuente YAML que produce el contenido visible.

### Entidades clave

- **Principio**: `id` estable `P01`–`P10`; nombre canónico; frase canónica; significado; problema o tensión; reglas; pruebas de decisión; ejemplo; señal de incumplimiento; capítulo de presentación; enlace al texto completo; relaciones con Job Stories y requisitos del sitio; versiones aprobadas en `en`, `es` y `pt-BR` (PRD §19.2).
- **Sección canónica**: fragmento del núcleo v2.1 con identificador estable y ancla; conserva versión y procedencia; es la fuente que toda explicación editorial debe referenciar.
- **Explicación editorial**: contenido derivado y revisado; declara el principio o sección de origen y su estado editorial; nunca sustituye al texto canónico.
- **Traducción aprobada**: entrada equivalente en otro idioma; conserva identificador, significado, fuente, versión y estado de revisión; declara su código BCP 47.
- **Estado de implementación del preset**: versión, fecha, validaciones realizadas y limitaciones; alimenta `FR-009` y `FR-012`.
- **Metadatos de publicación**: versión, fecha, autoría, idioma, URL canónica, URLs alternas y relaciones semánticas (PRD §19.1).

## Evidencia y criterios de éxito

Los identificadores `AC-01`–`AC-16` son los del PRD §31 y se conservan sin renumerar. Código correcto, build exitoso o pruebas automatizadas verdes no bastan por sí solos (PRD §32).

- **`AC-01`**: una persona sin contexto previo puede explicar por qué la capacidad de generar software con IA aumenta la necesidad de criterio.
- **`AC-02`**: la persona puede explicar que el progreso humano y la experiencia forman parte del producto.
- **`AC-03`**: los diez principios, sus identificadores y el texto canónico coinciden con el núcleo v2.1.
- **`AC-04`**: cada principio contiene una consecuencia y una prueba de decisión utilizable.
- **`AC-05`**: la narrativa puede comprenderse sin abrir todos los detalles y el contenido completo permanece accesible.
- **`AC-06`**: el visitante puede navegar, saltar, volver, compartir y reducir movimiento sin perder información.
- **`AC-07`**: los recorridos principales cumplen WCAG 2.2 AA y pasan revisión humana con teclado y tecnología de asistencia.
- **`AC-08`**: las métricas reales o de laboratorio representativas cumplen los presupuestos definidos y el contenido esencial aparece sin esperas artificiales.
- **`AC-09`**: la explicación distingue doctrina, anexo, preset y framework; declara independencia, estado y límites.
- **`AC-10`**: los artefactos producidos por SpecKit conservan todas las Job Stories y requisitos del PRD, sin prioridades, MVP o exclusiones inventadas.
- **`AC-11`**: cada principio tiene una dirección estable, metadatos correctos y vínculo con la fuente canónica.
- **`AC-12`**: el sitio puede leerse íntegramente sin registro ni entrega de información personal.
- **`AC-13`**: todo el alcance público existe en los tres idiomas, cada versión conserva significado, navegación, procedencia, accesibilidad y metadatos, sin fragmentos obligatorios pendientes ni mezclas accidentales. La versión española supera una revisión de neutralidad latinoamericana sin voseo, `vosotros` ni localismos nacionales.
- **`AC-14`**: sin preferencia previa, la raíz y las rutas sin prefijo se muestran en inglés. La persona puede cambiar de idioma desde cualquier superficie, mantenerse en la entidad equivalente, conservar o restablecer su elección localmente, y compartir una URL que abre directamente la versión elegida. Una URL localizada explícita no es sustituida por detección del navegador ni por una preferencia diferente.
- **`AC-15`**: el build valida el YAML, las relaciones entre idiomas, los enlaces y el JSON-LD. El marcado Schema.org describe únicamente contenido visible y las comprobaciones aplicables no reportan errores críticos.
- **`AC-16`**: el proyecto supera la comprobación estricta de tipos sin errores. La lógica mantenida por el equipo está escrita en TypeScript y cualquier excepción en JavaScript está técnicamente justificada, acotada y aprobada.

### Criterios de éxito adicionales

- **`SC-001`**: en pruebas moderadas con representantes de las audiencias principales, las personas explican el problema sin mencionar primero una funcionalidad del sitio (PRD §26.1).
- **`SC-002`**: las personas distinguen al menos tres principios cercanos sin confundirlos y relacionan escenarios con principios justificando la relación (PRD §26.1).
- **`SC-003`**: las personas encuentran el manifiesto completo sin ayuda, abren directamente un principio desde un enlace compartido y recorren el contenido por teclado (PRD §26.2).
- **`SC-004`**: las personas cambian de idioma sin perder el concepto o sección actual y conservan o restablecen su preferencia sin crear una cuenta (PRD §26.2).
- **`SC-005`**: las personas no deben cerrar interrupciones, registrarse ni aprender controles no convencionales (PRD §26.2).
- **`SC-006`**: en el percentil 75 de visitas reales, LCP ≤ 2,5 s, INP ≤ 200 ms y CLS ≤ 0,1 (PRD §24.1). Estos indicadores se usan junto con observación del recorrido, no como sustituto de la experiencia.
- **`SC-007`**: no existen enlaces internos rotos antes de liberar y los despliegues son reversibles (PRD §24.2).
- **`SC-008`**: el producto no se optimiza para tiempo de permanencia, páginas vistas o scroll completo si esas métricas compiten con comprensión rápida y control (PRD §26.3).

### Plan de validación exigido

El PRD §26.4 lo establece como condición previa a aceptar la versión 1.0: revisión de contenido contra el núcleo; pruebas moderadas de comprensión; prueba de navegación sin explicación previa; revisión completa por teclado y lector de pantalla; prueba con movimiento reducido; evaluación móvil y escritorio con contenido real; auditoría de rendimiento; comprobación de enlaces, metadatos y datos estructurados; revisión lingüística humana en los tres idiomas; verificación específica de ausencia de voseo, `vosotros` y localismos; prueba de cambio de idioma y correspondencia de URLs; validación del modelo YAML; y revisión humana del recorrido completo.

## Supuestos permitidos

Los supuestos `AS-001`–`AS-005` provienen del PRD §30 y son declarados allí como reversibles por la autoridad de producto. `AS-006` es una decisión técnica reversible tomada durante la preparación del proyecto.

- **`AS-001`**: el sitio será público y no requerirá autenticación — **Reversible porque**: el PRD lo declara supuesto explícito — **Impacto**: menor mientras se conserve `FR-018`.
- **`AS-002`**: las rutas sin prefijo sirven inglés y no redirigen automáticamente según el idioma del navegador — **Reversible porque**: el PRD lo declara supuesto y `FR-020` lo fija como comportamiento — **Impacto**: menor.
- **`AS-003`**: la versión 1.0 se administra mediante YAML versionado en GitHub sin CMS — **Reversible porque**: el PRD §19.3 admite un CMS si aparece una necesidad editorial que YAML no resuelva con menor complejidad, sin cambiar identificadores ni contrato de contenido — **Impacto**: menor.
- **`AS-004`**: no existe función generativa para visitantes en la versión 1.0 — **Reversible porque**: el PRD §22.2 define las condiciones para evaluar capacidades futuras — **Impacto**: menor.
- **`AS-005`**: el texto canónico v2.1 no cambia durante este ciclo de desarrollo — **Reversible porque**: el PRD §27.2 define el procedimiento ante una nueva versión del núcleo — **Impacto**: menor mientras no aparezca la v2.2.
- **`AS-006`**: `bun` es el gestor de paquetes y ejecutor del proyecto — **Reversible porque**: es una decisión técnica que no altera alcance, contenido, experiencia, seguridad, derechos ni posicionamiento, conforme a PRD §2.3; sustituirla requiere solo cambiar el archivo de bloqueo y los scripts — **Impacto**: menor. Debe registrarse en `plan.md` junto con su consecuencia sobre la reproducibilidad de dependencias exigida por PRD §24.5.

## Decisiones materiales pendientes

Las diez primeras corresponden a PRD §29, que las declara decisiones que **requieren autoridad humana** y establece: "Estas decisiones no bloquean la especificación de la arquitectura conceptual, pero bloquean cualquier implementación que las vuelva irreversibles o públicas." La undécima surge de la necesidad de planificar. Ninguna se cierra con un valor predeterminado.

- **`CL-01`** — **[NEEDS CLARIFICATION: nombre público definitivo y dominio del sitio. Autoridad requerida: autoridad de producto. Impacto: determina URL canónica, `hreflang` recíprocos, sitemap, metadatos de `WebSite` y Open Graph; sin ella no puede generarse marcado canónico correcto ni publicarse.]**
- **`CL-02`** — **[NEEDS CLARIFICATION: autoría visible — persona, iniciativa u organización. Autoridad requerida: autoridad de producto. Impacto: determina si el mapeo Schema.org usa `Person` u `Organization` (PRD §25.2), y afecta `FR-012` y la superficie Acerca de.]**
- **`CL-03`** — **[NEEDS CLARIFICATION: existe una identidad visual previa o hay libertad para proponerla. Autoridad requerida: autoridad de producto. Impacto: condiciona la dirección visual de PRD §21.2, los tokens que subordinan daisyUI y el trabajo de exploración previo al diseño.]**
- **`CL-04`** — **[NEEDS CLARIFICATION: nivel de protagonismo personal del autor en la narrativa. Autoridad requerida: autoridad de producto. Impacto: cambia el tono del recorrido y el contenido de la superficie Acerca de.]**
- **`CL-05`** — **[NEEDS CLARIFICATION: licencia del texto del manifiesto y condiciones de reutilización. Autoridad requerida: autoridad de producto. Impacto: `JS-05` y `JS-08` dependen de poder citar y reutilizar; sin licencia declarada no puede publicarse una invitación a citar ni completarse `FR-012`.]**
- **`CL-06`** — **[NEEDS CLARIFICATION: acción pública disponible mientras el preset no esté publicado — solo estado, solicitud de acceso, o ninguna captura. Autoridad requerida: autoridad de producto. Impacto: determina el comportamiento exigido por `FR-010`; "solicitud de acceso" introduciría un formulario y con él requisitos de privacidad y antiabuso de PRD §24.3 que hoy no están autorizados.]**
- **`CL-07`** — **[NEEDS CLARIFICATION: existe un canal de contacto y cuál. Autoridad requerida: autoridad de producto. Impacto: si existe, la superficie Acerca de lo incorpora y podría implicar datos personales, lo que activa `FR-018` y PRD §24.3.]**
- **`CL-08`** — **[NEEDS CLARIFICATION: uso o ausencia de analítica, y herramienta autorizada. Autoridad requerida: autoridad de producto. Impacto: `FR-018` exige minimizar datos, documentar propósito y no bloquear contenido por consentimiento; las señales cuantitativas de PRD §26.3 no pueden medirse sin decidir esto; un script de terceros no autorizado violaría `BR-008`.]**
- **`CL-09`** — **[NEEDS CLARIFICATION: responsables y mecanismo de aprobación lingüística para inglés general, español neutro latinoamericano y portugués de Brasil. Autoridad requerida: autoridad de producto. Impacto: `AC-13` exige revisión lingüística humana aprobada y `BR-003` impide publicar un idioma sin contenido aprobado; sin responsables designados la paridad multilingüe no puede aceptarse.]**
- **`CL-10`** — **[NEEDS CLARIFICATION: publicación futura del preset — repositorio, licencia y soporte. Autoridad requerida: autoridad de producto. Impacto: condiciona `FR-010` y el mapeo `SoftwareSourceCode` de PRD §25.2, que solo procede cuando exista publicación real y URL verificable.]**
- **`CL-11`** — **[NEEDS CLARIFICATION: plataforma de alojamiento y despliegue del sitio. Autoridad requerida: autoridad de producto, por su relación con `CL-01` y `CL-08`. Impacto: PRD §24.2 exige redirecciones y despliegues reversibles y PRD §24.3 exige encabezados de seguridad adecuados; ambos requisitos dependen de la plataforma y no pueden planificarse sin ella. El PRD no la establece.]**

**Consecuencia de estas decisiones.** Ninguna impide especificar ni planificar la arquitectura conceptual. Todas bloquean la publicación y cualquier implementación que las vuelva irreversibles o públicas. `CL-06`, `CL-08` y `CL-09` afectan además el contenido y la aceptación, no solo el despliegue.
