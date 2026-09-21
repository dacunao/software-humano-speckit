# Plan de implementación: Sitio público del Manifiesto de Software Humano

**Rama**: `main` (el directorio de la feature se resuelve desde `.specify/feature.json`) | **Fecha**: 2026-09-21 | **Especificación**: [spec.md](./spec.md)

**Entrada**: `specs/001-sitio-manifiesto/spec.md`, derivada de `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md` v1.0

## Resumen

El resultado que debe quedar cubierto es el alcance completo de `spec.md`: las nueve Job Stories, los veintiún requisitos funcionales, los dieciséis criterios de aceptación, los diez principios como contenido publicado, y los requisitos de experiencia, accesibilidad, rendimiento, privacidad, descubrimiento y gobernanza editorial del PRD. **Este plan no selecciona alcance, no asigna prioridad y no introduce fases de producto, MVP ni releases.** Ordena ejecución por dependencias, que es cosa distinta.

**El sitio vive en su propio repositorio**, `dacunao/sitio-software-humano` (`CL-13`), separado del paquete de método. `B00` materializa esa separación y precede a todo lo demás.

La estrategia recomendada es un sitio estático generado desde una **fuente de contenido única y tipada**, con validación relacional que detiene el build, una **capa de tokens** que se interpone entre la dirección visual y daisyUI, islas de cliente solo donde una interacción las exige, y JSON-LD emitido desde la misma fuente que produce el contenido visible. El despliegue ocurre en Cloudflare Pages con encabezados de seguridad y redirecciones versionados en el repositorio.

El orden de ejecución tiene un condicionante que no proviene de la técnica sino de la fuente: **la exploración visual no puede preceder al contenido real**, porque PRD §21.1.8 prohíbe aprobar con contenido simulado y §21.7 exige detectar expansión de texto, cortes y cambios de jerarquía con las tres versiones lingüísticas reales.

## Fuentes y autoridad

- **Fundamento de producto**: `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md`, v1.0, 2026-09-21, estado «Definición de producto para revisión».
- **Especificación operativa**: `specs/001-sitio-manifiesto/spec.md`, con doce decisiones materiales resueltas el 2026-09-21 y registradas en su sección `Clarifications`.
- **Autoridad de alcance**: Damián Acuña. Ni este plan ni ningún agente pueden aprobar cambios de alcance, resultados, exclusiones o estado de publicación (PRD §2.3).
- **Versión de constitución**: núcleo del manifiesto v2.1, materializado en `.specify/memory/constitution.md`.
- **Fuentes subordinadas**: anexo v1.2 para la correspondencia con SpecKit; preset `software-humano` v1.0.1 para su materialización técnica.

## Comprobación de constitución

*PUERTA: debe cumplirse antes de diseñar y revisarse después de resolver la estrategia.*

| Disposición | Consecuencia para el plan | Evidencia o decisión | Estado |
|---|---|---|---|
| `F02` Establecer cobertura | El plan debe inventariar historias, reglas, estados, recorridos y criterios sin vacíos. | Tres tablas de cobertura: 9 `JS`, 21 `FR`, 16 `AC`, más los bloques no funcionales. Ningún elemento sin destino técnico. | Cumple |
| `F03` Planificar la implementación | Resolver dependencias y orden **sin modificar el alcance**. | Doce bloques `B01`–`B12` ordenados por dependencia; se declara expresamente que el orden no es alcance. | Cumple |
| `F05` Contrato de experiencia | Describir qué debe comprender, decidir y sentir la persona en los momentos críticos. | `spec.md` ya lo contiene; el plan lo traduce a `B06`–`B09` y no lo duplica. | Cumple |
| `F07` Explorar y prototipar | Comparar alternativas y probar comprensión antes de optimizar código. | `B06` explora dos direcciones visuales sobre contenido real, con aprobación humana previa a fijar tokens (`CL-03`). | Cumple |
| `A02` Mapa de cobertura | Elementos obligatorios, relaciones, dependencias, implementación, pruebas, estado. | Sección «Cobertura y trazabilidad». | Cumple |
| `A07` Plan de aceptación | Qué evidencia autoriza declarar completo el desarrollo. | `quickstart.md` materializa las trece verificaciones de PRD §26.4. | Cumple |
| `V01` Cobertura | Todo elemento obligatorio tiene implementación y evidencia, o excepción aprobada. | Tablas de cobertura; no se registra ninguna excepción. | Cumple |
| `V09` Estados | Carga, vacío, error, éxito, interrupción y retorno mantienen contexto. | `ST-001`–`ST-005` y `EX-001`–`EX-003` tienen destino en `B08` y `B09`. | Cumple |
| `V10` Accesibilidad | Teclado, foco, etiquetas, contraste y tecnologías de asistencia. | El contraste se verifica en `B06`, antes de existir componentes; `B07` construye sobre HTML semántico; `B12` audita y suma revisión humana. | Cumple |
| `V11` Rendimiento | Presupuesto de respuesta o progreso honesto. | Generación estática, islas justificadas una por una en `B09`, presupuestos verificados en `B12`. | Cumple |
| `V12` IA | Salidas variables declaran incertidumbre. | No aplica a la experiencia pública: `BR-006` la declara determinista y `AS-004` lo registra como supuesto reversible. | Cumple · no aplica |
| `P03` La complejidad pertenece al sistema | La interfaz no debe abrir con rutas, archivos, YAML o comandos. | La superficie de Aplicación y la de SpecKit traducen el modelo antes de mostrar mecanismo (`B08`). | Cumple |
| `P04` Simple al comenzar, profundo al necesitarlo | Ni portada mínima que oculta ni página que muestra todo. | Profundidad progresiva sin callejones sin salida; el texto canónico íntegro siempre alcanzable (`B08`). | Cumple |
| `P07` La confianza se diseña | Distinguir cita, explicación, ejemplo, inferencia y estado confirmado. | Estados editoriales de `BR-005` modelados en `B02` y expresados visual y semánticamente en `B07`. | Cumple |
| `P09` Tiempo y continuidad | Contenido esencial sin JavaScript; retorno al punto de lectura. | `FR-015` gobierna `B08`; las islas de `B09` son mejora progresiva con alternativa sin JavaScript. | Cumple |
| `P10` Control y propiedad | Navegación libre, movimiento reducible, contenido copiable, URLs estables, sin captura innecesaria. | `B04` fija URLs estables; `B09` la preferencia reversible; `CL-07` y `CL-08` eliminan toda captura por parte del sitio. | Cumple |
| `SH-AP` «El plan selecciona alcance» | Implementar algunas historias y postergar el resto sin decisión de producto. | Los doce bloques cubren el alcance completo; ninguno pospone una `JS`, `FR` o `AC`. | Cumple |
| `SH-AP` «La descomposición parece exclusión» | Una fase técnica presentada como si redefiniera lo que el PRD exige. | Declarado explícitamente en «Dependencias, bloqueantes y orden de ejecución». | Cumple |
| `SH-AP` «El happy path define el producto» | Errores, vacíos e interrupciones para después. | `ST-001`–`ST-005` y `EX-001`–`EX-003` se modelan en `B02` y `B08`, no al final. | Cumple |
| `STOP02` | El plan no da cuenta de todo el alcance obligatorio. | No se produce: cobertura completa verificada. | No se activa |
| `STOP03` | Omitir, modificar o postergar una parte sin decisión autorizada. | No se produce: no hay omisiones ni postergaciones de alcance. | No se activa |
| `STOP04` | Una ambigüedad material resuelta por el agente sin autorización. | **Se activa una vez**: ver `R01`. El plan la registra y no la resuelve. | **Detención registrada** |
| `STOP07` | Solo se puede demostrar que el código funciona, no que el usuario progresa. | `B12` incluye pruebas moderadas de comprensión y revisión humana del recorrido, no solo auditorías técnicas. | No se activa |

**Resultado de la puerta antes de diseñar: se puede diseñar.** Una detención quedó registrada como `R01`.

### Re-evaluación después del diseño

| Qué cambió al diseñar | Efecto sobre la puerta |
|---|---|
| `R01` fue elevada a la autoridad de producto y **resuelta por ella** el 2026-09-21 | `STOP04` deja de estar activo. La decisión quedó tomada por quien tiene autoridad, con su fundamento y su consecuencia registrados en `research.md` · `RQ-01`. El agente no la resolvió |
| `RQ-03` redujo las islas de tres a dos y resolvió la comparación del Acto 2 como interacción nativa, sin JavaScript | Refuerza `P06`, `V11` y `FR-015`. Evita el antipatrón «el agente agrega por si acaso»: la isla descartada estaba supuesta en el plan y no resistió el criterio de PRD §24.1 |
| `RQ-04` optó por inserción manual del beacon en lugar de inyección de la plataforma | Hace **auditable** la decisión que `BR-008` exige aprobar. El único script de terceros queda visible en un repositorio que `CL-12` publica bajo MIT para ser estudiado |
| `RQ-01` eliminó la duplicación del texto canónico | `AC-03` pasa de comparación entre copias a comprobación de integridad. Reduce un riesgo de divergencia doctrinal que ninguna prueba automática habría detectado a tiempo |
| Se generaron cuatro documentos auxiliares | Cada uno responde una pregunta necesaria declarada en «Documentos auxiliares». Ninguno se produjo por rutina |
| La cobertura no cambió | Ninguna `JS`, `FR` o `AC` fue pospuesta, agrupada ni reinterpretada. `STOP02` y `STOP03` siguen sin activarse |

**Resultado de la puerta después de diseñar: se puede derivar tareas.** Ninguna detención permanece activa sobre la planificación. Permanecen dos detenciones **sobre la ejecución**, por diseño y no por omisión: la aprobación humana de la dirección visual (`R05`) y la aprobación lingüística externa (`CL-09`). Ambas bloquean tareas concretas, no la derivación de tareas.

## Contexto técnico

- **Lenguaje y versión**: TypeScript con comprobación estricta. El build falla ante errores de tipado (PRD §24.6, `AC-16`). Se evita `any`; toda excepción debe ser localizada, explicada y verificable. Los tipos no sustituyen la validación en tiempo de ejecución de lo que provenga de archivos o del navegador.
- **Dependencias principales**: Astro con generación estática; Tailwind CSS con daisyUI subordinado a tokens propios; un validador de esquema en tiempo de build. Versiones exactas se fijan en `B01` y quedan ancladas en el archivo de bloqueo.
- **Gestor de paquetes y ejecutor**: **bun** (`AS-006`), verificado disponible en 1.3.14. Consecuencia sobre PRD §24.5, que exige «dependencias y versiones fijadas de manera reproducible», detallada más abajo.
- **Persistencia**: ninguna del lado del servidor. El sitio es estático. La única persistencia es local en el navegador para la preferencia de idioma y de movimiento, declarada por `FR-020` como local, reversible y prescindible.
- **Plataforma objetivo**: navegadores modernos con soporte vigente (PRD §24.4), sin dependencia de dispositivo apuntador, tamaño de pantalla ni modalidad de entrada. Alojamiento en Cloudflare Pages (`CL-11`), origen `https://softwarehumano.com` (`CL-01`).
- **Estrategia de pruebas y evidencia**: validación del contenido y sus relaciones en build, que detiene ante error (`BR-007`); comprobación estricta de tipos; pruebas automatizadas en recorridos críticos; y verificación humana para todo lo que el PRD §26.4 declara humano. Código correcto y build verde no constituyen aceptación (`V01`, `STOP07`, PRD §32).
- **Rendimiento y escala**: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 en el percentil 75 (`SC-006`). Presupuestos explícitos para tipografías y recursos visuales. El contenido inicial no depende de animación ni de petición tardía.
- **Seguridad, privacidad y permisos**: sin cuentas, sin registro, sin formularios, sin captura de datos personales por parte del sitio (`FR-018`, `AC-12`, `CL-06`, `CL-07`). Encabezados de seguridad declarados en el repositorio. Un único script de terceros autorizado, Cloudflare Web Analytics (`CL-08`), sin cookies ni `localStorage` ni *fingerprinting*.
- **Restricciones**: las de PRD §24.6, preservadas sin reabrir; el contrato lingüístico de `BR-001`–`BR-003`; el carácter determinista de la experiencia pública (`BR-006`); y las doce decisiones de `Clarifications`.

### Decisión de gestor de paquetes y su consecuencia sobre la reproducibilidad

`AS-006` adopta **bun** como gestor y ejecutor. PRD §2.3 lo admite como decisión técnica reversible porque no altera alcance, contenido, experiencia, seguridad, derechos ni posicionamiento. PRD §24.5 exige, en cambio, que dependencias y versiones queden «fijadas de manera reproducible». La consecuencia concreta, que este plan registra:

1. **El archivo de bloqueo de bun se versiona** y la instalación en integración continua usa modo congelado. Sin eso, «reproducible» sería una afirmación sin mecanismo.
2. **La versión de bun se fija también**, no solo la de las dependencias. Un archivo de bloqueo interpretado por dos versiones distintas del gestor no garantiza el mismo árbol. Fijar bun forma parte de satisfacer §24.5, no es un extra.
3. **No se generan archivos de bloqueo de npm, yarn ni pnpm**, por instrucción del proyecto. La consecuencia real es que **quien no tenga bun no puede reproducir la instalación exacta**. Esto tiene costo en un repositorio público bajo MIT (`CL-12`) que `JS-07` invita expresamente a estudiar: reduce el conjunto de personas que pueden reconstruir el piloto. Se registra como costo aceptado, no como detalle.
4. Sustituir bun más adelante requiere cambiar el archivo de bloqueo y los scripts; no toca arquitectura ni alcance. La decisión permanece reversible, como `AS-006` declara.

## Estrategia técnica

### Enfoque recomendado

**Una fuente de contenido tipada que genera todo lo demás.** El contenido vive en YAML versionado, con identificadores estables independientes del idioma. Un esquema formal lo valida y un conjunto de validadores relacionales comprueba lo que un esquema por sí solo no ve: identificadores duplicados, relaciones rotas, campos obligatorios ausentes y traducciones requeridas incompletas (`BR-007`, PRD §19.3). De esa misma fuente se derivan el HTML, la navegación, los metadatos, las relaciones `hreflang` y el JSON-LD, de modo que PRD §25.3 —«generar JSON-LD desde la misma fuente YAML que produce el contenido visible»— se cumple por construcción y no por disciplina.

**Una capa de tokens entre la dirección visual y daisyUI.** Es la pieza que impide el riesgo que PRD §28 registra: que la biblioteca de componentes imponga una apariencia genérica. Los tokens se fijan después de que la autoridad de producto apruebe una de las dos direcciones exploradas (`CL-03`), y todo componente se construye sobre HTML semántico y se personaliza con esos tokens, pudiendo sustituirse localmente cuando el componente base contradiga una decisión del manifiesto.

**Islas justificadas una por una.** Generación estática por defecto y HTML utilizable antes de ejecutar JavaScript. Cada isla debe declarar qué interacción la exige y qué ocurre sin JavaScript. El examen de `research.md` · `RQ-03` dejó **dos**: la persistencia de preferencias de idioma y movimiento, y la copia o compartición con atribución diferenciada. Descartó explícitamente el conmutador de idioma —que PRD §24.6 obliga a resolver como navegación entre URLs— y la comparación del Acto 2, que **sigue siendo una interacción**, como PRD §16 declara para el Acto 2, pero resuelta con elementos nativos y sin JavaScript. Ambas islas son mejora progresiva sobre contenido que ya funciona (`FR-015`, `EX-001`).

**Configuración de despliegue como artefacto del repositorio.** Encabezados de seguridad y redirecciones se declaran en archivos versionados que el build publica, de modo que una reversión de despliegue restituye contenido y configuración juntos (`CL-11`, PRD §24.2, §24.3).

### Alternativa más simple considerada

**Colecciones de contenido de Astro con cuerpos en Markdown y validación de frontmatter, sin capa de datos propia.** Es genuinamente más simple: es el mecanismo nativo del framework, requiere menos código propio y da tipado del frontmatter sin construir nada.

**Se adopta parcialmente y se descarta como solución única**, por una razón concreta y no estética: PRD §19.3 exige detener el build ante «identificadores duplicados, relaciones rotas, campos obligatorios ausentes o traducciones requeridas incompletas». Las tres últimas son comprobaciones **entre documentos y entre idiomas** —que el mismo `id` exista en `en`, `es` y `pt-BR`, que la relación entre un principio y su sección canónica apunte a algo que existe, que un `hreflang` tenga recíproco—, y eso es una validación de grafo que la validación por documento no alcanza. La parte que sí se adopta es el manejo de prosa extensa en Markdown, y es precisamente lo que abre la decisión registrada como `R01`.

### Opción de no construir

No se evalúa para el producto en su conjunto: PRD §34 establece que la aprobación del fundamento autoriza especificar y planificar, y la decisión de construir ya fue tomada por la autoridad de producto. Presentarla como alternativa abierta sería simular una deliberación cerrada.

Sí se aplicó, y se aplica, a decisiones concretas donde existe una elección real:

- **No construir captura de datos para el preset** — `CL-06` la descartó. Fue la opción de no construir y fue la elegida.
- **No construir formulario de contacto** — `CL-07` la descartó por la misma razón.
- **No construir analítica de sesiones ni observabilidad** — `CL-08` la descartó; se demostró además que `AC-08` y `SC-006` son satisfacibles sin instrumentar el sitio.
- **No construir exploración visual** — evaluada y **excluida por la fuente, no por criterio técnico**: equivaldría a adoptar el tema por defecto de daisyUI, que PRD §13 declara no objetivo.
- **No construir un CMS** — `AS-003` lo registra; PRD §19.3 solo lo justificaría ante una necesidad editorial que YAML no resuelva con menor complejidad, y no ha aparecido.

## Cobertura y trazabilidad

Todo elemento obligatorio tiene destino técnico. **Ningún elemento queda pospuesto y no se registra ninguna excepción aprobada**, porque no se solicitó ninguna (`V01`).

### Job Stories

| ID | Componente o decisión técnica | Dependencias | Evidencia prevista | Estado |
|---|---|---|---|---|
| `JS-01` | `B08` superficie Inicio, Actos 1–2 | `B04`, `B07` | Prueba moderada de comprensión; lectura sin JavaScript | Planificado |
| `JS-02` | `B08` Acto 3 con texto canónico breve | `B03` | Prueba moderada; apertura directa por enlace compartido | Planificado |
| `JS-03` | `B03` entidad Principio + `B08` superficie Principios | `B02` | Asociación escenario–principio; ocho secciones presentes | Planificado |
| `JS-04` | `B08` comparación del Acto 2 como **interacción sin JavaScript**, con alternativa textual equivalente (`research.md` · `RQ-03`) | `B07` | Prueba con movimiento reducido y recorrido por teclado | Planificado |
| `JS-05` | `B03` núcleo íntegro + `B04` anclas estables | `B02` | URL estable, versión y procedencia verificadas | Planificado |
| `JS-06` | `B08` superficie Aplicación | `B03`, `B07` | La persona identifica una razón de detención concreta | Planificado |
| `JS-07` | `B08` superficie SpecKit + `B02` estado del preset | `B02` | Distinción de las cuatro capas; estado «no publicado» comprendido | Planificado |
| `JS-08` | `B04` URLs estables + `B08` atribución diferenciada | `B02` | Enlace compartido abre la entidad correcta con contexto | Planificado |
| `JS-09` | `B04` topología por idioma + `B05` traducciones + `B09` preferencia | `B02` | Paridad, cambio contextual y preferencia reversible | Planificado |

### Requisitos funcionales

| ID | Componente o decisión técnica | Dependencias | Evidencia prevista | Estado |
|---|---|---|---|---|
| `FR-001` | `B08` recorrido de siete actos | `B04`, `B07` | `AC-01`, `AC-02`, `AC-05` | Planificado |
| `FR-002` | `B08` navegación global; `B04` URLs profundas | `B04` | `AC-06`, prueba de navegación sin explicación previa | Planificado |
| `FR-003` | `B03` carga del núcleo v2.1 íntegro; `B08` superficie Manifiesto | `B02` | `AC-03` por comparación contra el núcleo | Planificado |
| `FR-004` | `B03` entidades `P01`–`P10`; `B08` explorador | `B02` | `AC-03`, `AC-04` | Planificado |
| `FR-005` | `B02` campos de ejemplo y contraejemplo; `B08` comparación del Acto 2 como interacción sin JavaScript | `B02` | `AC-04`; revisión editorial de que no crean doctrina nueva | Planificado |
| `FR-006` | `B02` campo de pruebas de decisión | `B02` | `AC-04` | Planificado |
| `FR-007` | `B08` superficie Aplicación | `B03`, `B07` | `JS-06`; traducción de conceptos antes del mecanismo (`P03`) | Planificado |
| `FR-008` | `B08` superficie SpecKit, relación entre las cuatro capas | `B03` | `AC-09` | Planificado |
| `FR-009` | `B02` entidad Estado del preset; `B08` render de estado | `B02` | `AC-09`; verificable contra la documentación de SpecKit | Planificado |
| `FR-010` | `B02` campo `estado` y render condicional; `BR-007` detiene si es incoherente | `B02`, `B08` | `AC-09`; ausencia de enlaces sin destino verificada en `B12` | Planificado |
| `FR-011` | `B04` URLs estables; `B08` copia con atribución diferenciada | `B02` | `AC-11` | Planificado |
| `FR-012` | `B03` metadatos de versión y procedencia; `B08` superficie Acerca de | `B02` | `AC-11`; licencias `CL-05` y `CL-12` declaradas | Planificado |
| `FR-013` | `B06` política de movimiento; `B07` componentes; `B09` islas | `B06` | `AC-06`, `AC-07` | Planificado |
| `FR-014` | `B04` anclas y restitución de sección; `B09` continuidad local | `B04` | `AC-06` | Planificado |
| `FR-015` | `B08` HTML estático utilizable; `B09` mejora progresiva | `B07` | `AC-05`, `AC-08`; prueba con JavaScript deshabilitado | Planificado |
| `FR-016` | `B04` títulos, encabezados, sitemap, canónicas; `B10` datos estructurados | `B02` | `AC-11`, `AC-15` | Planificado |
| `FR-017` | `B02` estados editoriales de `BR-005`; `B07` expresión visual y semántica | `B02` | `AC-03`, `AC-09` | Planificado |
| `FR-018` | Ninguna captura por diseño (`CL-06`, `CL-07`); `B10` beacon sin cookies; `B11` encabezados | `B10` | `AC-12`: lectura íntegra sin registro ni datos personales | Planificado |
| `FR-019` | `B04` topología `/`, `/es/`, `/pt-br/`; `B05` traducciones aprobadas | `B02` | `AC-13`, `AC-14`; reciprocidad `hreflang` verificada en build | Planificado |
| `FR-020` | `B09` isla de preferencias; `B08` superficie de ajustes acotada | `B08` | `AC-14`; URL explícita prevalece sobre preferencia | Planificado |
| `FR-021` | `B02` esquema y validadores; `B01` integración continua | `B01` | `AC-15`; el build se detiene ante contenido inválido | Planificado |

### Criterios de aceptación

| ID | Dónde se produce | Dependencias | Evidencia prevista | Estado |
|---|---|---|---|---|
| `AC-01` | `B08` | `B12` | Prueba moderada con audiencias principales | Planificado |
| `AC-02` | `B08` | `B12` | Prueba moderada | Planificado |
| `AC-03` | `B03` | `B12` | Comparación de contenido contra el núcleo v2.1 | Planificado |
| `AC-04` | `B03` | `B12` | Revisión de contenido por principio | Planificado |
| `AC-05` | `B08` | `B12` | Prueba de navegación sin explicación previa | Planificado |
| `AC-06` | `B08`, `B09` | `B12` | Navegación, compartición y movimiento reducido | Planificado |
| `AC-07` | `B06`, `B07` | `B12` | Auditoría WCAG 2.2 AA **más** revisión humana con teclado y lector de pantalla | Planificado |
| `AC-08` | `B01`, `B08` | `B12` | Auditoría contra los presupuestos de PRD §24.1 | Planificado |
| `AC-09` | `B08` | `B12` | Revisión de contenido y prueba de comprensión | Planificado |
| `AC-10` | Este plan y `tasks.md` | `analyze` | `analyze` y revisión humana: sin prioridades, MVP ni exclusiones inventadas | Planificado |
| `AC-11` | `B04` | `B12` | Comprobación de URLs, metadatos y vínculos | Planificado |
| `AC-12` | `B10`, `B11` | `B12` | Lectura completa sin registro; inventario de peticiones de red | Planificado |
| `AC-13` | `B05` | `B12` | **Revisión lingüística humana aprobada** en los tres idiomas (`CL-09`) | Planificado |
| `AC-14` | `B04`, `B09` | `B12` | Prueba de cambio de idioma y correspondencia de URLs | Planificado |
| `AC-15` | `B02`, `B04`, `B10` | `B12` | Validación de YAML, relaciones, enlaces y JSON-LD en build | Planificado |
| `AC-16` | `B01` | `B12` | Comprobación estricta de tipos sin errores | Planificado |

### Principios, reglas, estados y excepciones

| Elemento | Destino técnico |
|---|---|
| `P01`–`P10` como **contenido publicado** | `B03` entidades; `B08` superficie Principios |
| `P01`–`P10` como **criterio de construcción** | Comprobación de constitución de este plan; revisión humana en `B12` |
| `BR-001`–`BR-003` contrato lingüístico | `B02` esquema; `B04` topología; `B05` revisión; verificación automatizada de voseo y `vosotros` en `B02` |
| `BR-004` texto canónico no parafraseado | `B03` carga literal; `B12` comparación contra el núcleo |
| `BR-005` seis estados editoriales, más el registro de voz autoral (`CL-04`) | `B02` modelo; `B07` expresión visual y semántica |
| `BR-006` experiencia determinista | Ausencia de función generativa; verificado en `analyze` y en `B12` |
| `BR-007` build que se detiene | `B02` validadores; `B01` integración continua |
| `BR-008` sin datos innecesarios ni scripts no autorizados | `B10`; inventario de peticiones en `B12` |
| `BR-009` marcado solo de contenido visible | `B04`, `B10`; verificado en `B12` |
| `ST-001`–`ST-005` estados | `B02` (vacío, `ST-001`), `B08` (carga, error, éxito, recuperación) |
| `EX-001`–`EX-003` excepciones | `B09` (`EX-001`), `B05` y `B08` (`EX-002`), `B11` (`EX-003`) |
| `SC-001`–`SC-008` criterios de éxito | `B12` |

## Dependencias, bloqueantes y orden de ejecución

> **El orden técnico no modifica alcance ni presupone releases incrementales.** Los doce bloques cubren el alcance completo; ninguno pospone una Job Story, un requisito o un criterio de aceptación. `SH-AP` advierte contra dos confusiones que aquí se declaran evitadas: «el plan selecciona alcance» y «la descomposición parece exclusión». Un bloque es una unidad de trabajo coherente con un criterio para avanzar, no una entrega parcial de producto ni una fase.

| Bloque | Entrega técnica | Depende de | Desbloquea | Criterio para avanzar |
|---|---|---|---|---|
| `B00` | Separación de repositorios: creación del repositorio del sitio, instalación propia del preset, traslado del fundamento, de los artefactos de SpecKit y del código, y verificación de que nada rector queda duplicado | — | todo | Ningún artefacto rector existe en dos repositorios (`CL-13`) |
| `B01` | Fundamento del repositorio: bun con versión fijada e instalación congelada, TypeScript estricto, Astro estático, estructura de directorios, integración continua que ejecuta tipado y validaciones | `B00` | `B02`, `B11` | `AC-16` pasa; el build se ejecuta desde una instalación reproducible |
| `B02` | Modelo de contenido: esquema formal, tipos derivados de fuente única, validadores relacionales de identificadores, relaciones, campos obligatorios y paridad de traducciones; verificación de voseo y `vosotros`; estados editoriales y voz autoral | `B01` | `B03`, `B04` | El build **se detiene** ante cada caso de `BR-007`, demostrado con casos negativos |
| `B03` | Contenido real en español: núcleo v2.1 íntegro con anclas, `P01`–`P10` con sus ocho secciones, metadatos de versión, procedencia y licencias, estado del preset | `B02` | `B04`, `B05`, `B06`, `B08` | `AC-03` comparado contra el núcleo; `AC-04` por principio |
| `B04` | Topología y semántica: rutas por idioma, URLs canónicas, `hreflang` recíprocos, sitemap, robots, anclas estables, JSON-LD desde la misma fuente | `B02`, `B03` | `B08`, `B10` | Reciprocidad y correspondencia verificadas en build; `AC-11` parcial |
| `B05` | Traducciones a inglés general y portugués de Brasil, con **aprobación del servicio profesional de revisión nativa** (`CL-09`) | `B03` | `B06` (borrador), `B08` | Registro de revisión aprobada por idioma; sin él, `BR-003` impide publicar ese idioma |
| `B06` | Exploración visual: **dos direcciones** sobre contenido real en los tres idiomas; escala tipográfica, roles de color con contraste verificado, ritmo, tratamiento de diagramas, política de movimiento; y los **tokens** resultantes | `B03`, borradores de `B05` | `B07` | **Aprobación humana de la autoridad de producto.** Sin ella no se fijan tokens ni se construyen componentes |
| `B07` | Sistema de componentes sobre daisyUI subordinado a los tokens: HTML semántico, foco, teclado, contraste, reflow, estados; sustitución local donde el componente base contradiga una decisión | `B06` | `B08` | Cada componente pasa las verificaciones de PRD §21.5 que le apliquen |
| `B08` | Las seis superficies obligatorias y el recorrido: Inicio con los siete actos —incluida la comparación del Acto 2, **interactiva sin JavaScript**—, Manifiesto, Principios, Aplicación, SpecKit, Acerca de; navegación global; conmutador de idioma como enlaces generados en build; página 404 orientadora; estados `ST-001`–`ST-005` | `B04`, `B05`, `B07` | `B09`, `B10` | Recorrido completo utilizable **sin JavaScript** (`FR-015`, `EX-001`) |
| `B09` | **Dos** islas justificadas, según `research.md` · `RQ-03`: preferencia de idioma y movimiento, y copiar o compartir con atribución diferenciada. Cada una declara la interacción que la exige y su comportamiento sin JavaScript | `B08` | `B12` | La supresión de la isla no elimina información ni acceso |
| `B10` | Descubrimiento y medición: Open Graph y tarjetas sociales, verificación de Search Console, línea base de CrUX, beacon de Cloudflare Web Analytics y la política de contenido que lo admite sin abrir la superficie | `B04`, `B08` | `B11` | Inventario de peticiones de red: ningún tercero fuera del autorizado |
| `B11` | Despliegue: Cloudflare Pages, encabezados de seguridad y redirecciones versionados, dominio `softwarehumano.com`, reversión comprobada | `B01`, `B10` | `B12` | Una reversión restituye contenido **y** configuración; `EX-003` cubierto |
| `B12` | Evidencia y aceptación: las trece verificaciones de PRD §26.4, incluidas las humanas | Todos | — | **Revisión humana.** Ninguna auditoría automática la sustituye (`STOP07`, PRD §32) |

**Tres dependencias merecen atención porque no son técnicas.**

`B06` depende de `B03` y de borradores de `B05` por mandato de la fuente, no por comodidad: PRD §21.1.8 prohíbe aprobar con contenido simulado y §21.7 exige detectar expansión de texto y cambios de jerarquía con las tres versiones reales. Aprobar una dirección visual sobre texto de relleno y descubrir después que el portugués rompe la jerarquía obligaría a rehacer los tokens.

`B06` contiene además una **detención humana explícita**. Ningún agente puede aprobar la dirección visual ni atribuirse esa revisión. `B07` y todo lo que sigue permanecen bloqueados hasta que exista aprobación.

`B05` es una **dependencia externa con proveedor**, tiempo y costo. Su criterio de terminado no es que el texto exista, sino que exista un registro de revisión aprobada.

## Integración y recorrido completo

- **Puntos de integración**: el esquema de contenido es la junta entre autoría y build; los tokens son la junta entre dirección visual e implementación; la topología de rutas es la junta entre contenido y descubrimiento; los archivos de encabezados y redirecciones son la junta entre repositorio y plataforma.
- **Recorrido de extremo a extremo**: un cambio en YAML pasa por revisión en GitHub, el build lo valida y se detiene si viola `BR-007`, genera HTML por idioma con sus metadatos y su JSON-LD, y Cloudflare Pages publica ese resultado junto con los encabezados y redirecciones del mismo commit. Una modificación permite saber qué cambió, quién la aprobó, qué idiomas afecta y qué páginas y datos estructurados genera (`FR-021`).
- **Estados y recuperación**: vacío (`ST-001`, un idioma sin contenido aprobado no se publica como disponible); carga (`ST-002`, el contenido inicial no depende de animación ni de petición tardía); éxito (`ST-003`, confirmación al copiar o compartir, sin captura); error (`ST-004`, 404 orientadora con rutas al recorrido y al texto canónico); recuperación (`ST-005`, la URL profunda restituye la sección y el cambio de idioma conserva la entidad). Excepciones: `EX-001` sin JavaScript, `EX-002` traducción ausente, `EX-003` cambio de estructura de URLs.
- **Riesgos de integración**: que el JSON-LD se separe de su fuente y describa contenido inexistente — mitigado generándolo desde la misma fuente y verificándolo en `B12`; que la política de contenido bloquee el beacon autorizado o, peor, que se relaje de más para admitirlo — mitigado declarándola en `B10` junto al beacon y verificándola con un inventario de peticiones; que una traducción se publique sin aprobación — mitigado por `BR-003` y la compuerta de `ST-001` implementada en `B02`, no confiada a la disciplina editorial.

## Estructura del proyecto

```text
# Raíz del **repositorio del sitio** (`CL-13`), separado del paquete de método.
.
├── src/
│   ├── content/            # fuente de contenido versionada, por idioma e id estable
│   ├── schema/             # esquema formal y tipos derivados de fuente única
│   ├── lib/                # validadores relacionales, rutas por idioma, JSON-LD
│   ├── tokens/             # capa de tokens resultante de B06, entre identidad y daisyUI
│   ├── components/         # componentes sobre HTML semántico
│   ├── layouts/
│   ├── pages/              # topología: raíz en inglés, /es/, /pt-br/
│   └── islands/            # solo las islas justificadas en B09
├── public/
│   ├── _headers            # encabezados de seguridad, versionados
│   └── _redirects          # redirecciones, versionadas
├── design/                 # exploración visual de B06: muestra real, dos direcciones, contraste, expansión
├── tools/
│   ├── audit/              # a11y, rendimiento e inventario de red
│   └── revision/           # paquete Markdown para el servicio profesional de revisión
├── tests/                  # recorridos críticos y casos negativos de validación
└── specs/001-sitio-manifiesto/
```

**Decisión de estructura**: separa lo que cambia por razones distintas —contenido, esquema, tokens, presentación— sin crear capas que no resuelvan un problema presente. `src/tokens/` existe porque PRD §24.6 exige que daisyUI quede subordinado a reglas propias y necesita un lugar donde eso sea verificable; `src/islands/` existe para que cada excepción a la generación estática sea visible y auditable en lugar de dispersarse. No hay capa de servicios, de estado global ni de abstracción de datos, porque no hay servidor, sesión ni origen de datos externo que las justifique.

## Documentos auxiliares

| Documento nativo | ¿Se requiere? | Pregunta que responde | Justificación |
|---|---|---|---|
| `research.md` | **Sí** | Cuatro incertidumbres técnicas que cambian el plan: cómo se almacena la prosa canónica extensa frente a la letra de `FR-021`; cómo se representa la equivalencia entre URLs localizadas para que el cambio de idioma caiga en la misma entidad; qué interacciones exigen realmente una isla; y cómo se expresa la política de seguridad admitiendo el único beacon autorizado sin abrir la superficie | Ninguna se resuelve en `spec.md` y las cuatro tienen alternativas con consecuencias distintas. La primera además **toca la letra de un requisito** y se registra como `R01` |
| `data-model.md` | **Sí** | Campos, relaciones, reglas de validación y transiciones del modelo de contenido | `spec.md` enumera las entidades pero no el detalle que `B02` y `tasks.md` necesitan para implementar y verificar `BR-007` |
| `contracts/` | **Sí**, un solo archivo | Contrato de rutas y semántica: topología por idioma, canónicas, reciprocidad `hreflang`, sitemap y mapeo JSON-LD por superficie | Es lo que `AC-11`, `AC-13`, `AC-14` y `AC-15` verifican. Distinto consumidor que `data-model.md`: la capa de render y descubrimiento, no la de contenido |
| `quickstart.md` | **Sí** | Qué evidencia autoriza declarar completo el desarrollo y cómo se produce cada pieza | Materializa `A07` de la constitución y las trece verificaciones de PRD §26.4, separando lo comprobable por comando de lo que exige revisión humana |

**No se generan otros documentos.** El contrato de experiencia, el mapa del fundamento y las fichas de Job Story ya existen en `spec.md` y se referencian sin duplicarse, conforme a la regla de la constitución: si la información ya existe, debe referenciarse.

## Riesgos y decisiones pendientes

| ID | Riesgo o decisión | Impacto | Autoridad | Tratamiento / condición de detención |
|---|---|---|---|---|
| `R01` | **Almacenamiento del texto canónico extenso.** `FR-021` dice que el contenido «DEBE originarse en YAML versionado». El núcleo v2.1 son ~82 KB de prosa continua, y son tres idiomas. Cabe en escalares de bloque YAML y los diffs siguen siendo legibles, así que no es un problema de control de versiones. El problema es **quién edita y revisa**: `CL-09` encarga la revisión de inglés y portugués a un servicio profesional externo, y `AC-13` hace de esa revisión un criterio de aceptación. Revisar prosa dentro de YAML indentado es fricción real para ese proveedor. La alternativa es prosa en Markdown referenciada desde YAML, con el esquema validando la referencia y la correspondencia de anclas | Toca la **letra** de `FR-021` y afecta la viabilidad del flujo de revisión del que depende `AC-13` | **Autoridad de producto** | **Resuelta el 2026-09-21 por la autoridad de producto**, tras elevarla como `STOP04`: el español se lee de la fuente protegida sin copiarse y las traducciones viven en Markdown referenciado desde YAML. Fundamento y consecuencia en `research.md` · `RQ-01` |
| `R02` | CrUX solo reporta un origen con tráfico suficiente. Un sitio recién publicado puede no figurar durante meses | `SC-006` pide percentil 75 de visitas reales | Autoridad de producto | Mitigado: Cloudflare Web Analytics reporta Core Web Vitals desde el primer día, y `AC-08` admite «métricas reales **o de laboratorio representativas**». Se documenta cuál se usó |
| `R03` | La revisión de neutralidad latinoamericana queda sin segunda mirada (`CL-09`) | `AC-13` | Autoridad de producto | **Aceptado explícitamente.** La verificación automatizada de `B02` atrapa marcadores mecánicos, no vocabulario ni giros |
| `R04` | `B05` depende de un proveedor externo con tiempo y costo | Bloquea `B08` y, por borradores, condiciona `B06` | Autoridad de producto | El plan lo ordena temprano. Su criterio de terminado es el registro de revisión aprobada |
| `R05` | `B06` contiene una detención humana | Bloquea `B07`–`B12` | Autoridad de producto | Por diseño. Ningún agente aprueba dirección visual ni se atribuye esa revisión |
| `R06` | El preset debe extraerse a su repositorio propio, publicarse y catalogarse | No bloquea el sitio | **Sesión que mantiene el método** | Si no ocurre, el estado permanece `no-publicado` y el sitio se comporta correctamente. Reportado, no ejecutado aquí |
| `R07` | La expansión de texto entre idiomas puede romper una jerarquía tipográfica ya aprobada | Retrabajo de tokens | — | Mitigado por diseño: `B06` explora sobre los tres idiomas, no sobre uno |
| `R08` | Fijar bun sin archivos de bloqueo alternativos reduce quién puede reproducir la instalación | Adopción del piloto por terceros | Autoridad de producto | Costo aceptado y registrado en «Decisión de gestor de paquetes» |

## Complejidad excepcional

| Complejidad | Necesidad concreta | Alternativa más simple rechazada porque |
|---|---|---|
| Validadores relacionales propios además del esquema por documento | PRD §19.3 exige detener el build ante relaciones rotas y traducciones requeridas incompletas, que son comprobaciones **entre** documentos e idiomas | La validación por documento del framework no ve el grafo: no puede saber que un `id` falta en `pt-BR` ni que un `hreflang` carece de recíproco |
| Capa de tokens propia entre identidad y daisyUI | PRD §24.6 exige que daisyUI no defina la identidad visual y que todo componente se personalice con reglas propias | Usar el tema por defecto reproduce el riesgo que PRD §28 registra y contradice un no objetivo de PRD §13 |
| Verificación automatizada de voseo y `vosotros` | PRD §26.4 la exige como verificación específica, y `CL-09` deja el español sin segunda mirada humana | Confiar solo en la revisión humana deja sin red el punto que la propia decisión reconoció como más frágil |

**Ninguna otra complejidad se introduce.** No hay CMS, chatbot, autenticación, personalización, analítica de sesiones, temas, paneles, modos ni abstracciones anticipadas.
