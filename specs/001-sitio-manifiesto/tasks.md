---
description: "Tareas trazables para implementar el alcance completo"
---

# Tareas: Sitio público del Manifiesto de Software Humano

**Entrada obligatoria**: [spec.md](./spec.md), [plan.md](./plan.md)
**Entradas condicionales**: [research.md](./research.md), [data-model.md](./data-model.md), [contracts/rutas-y-semantica.md](./contracts/rutas-y-semantica.md), [quickstart.md](./quickstart.md) — los cuatro declarados necesarios en `plan.md`

## Formato

`- [ ] T001 [P?] [REF] Acción concreta en ruta/archivo — Evidencia esperada`

- **[P]**: puede ejecutarse en paralelo porque no comparte archivos ni depende de trabajo incompleto.
- **[REF]**: identificador trazable de fuente, requisito, regla o bloque técnico.
- **Una fase organiza la ejecución; no selecciona ni reduce alcance.**

**Sobre la organización.** Las tareas se agrupan por los doce bloques `B01`–`B12` de `plan.md`, que es la estructura real del trabajo. **No se asigna prioridad, MVP, independencia ni entrega incremental**, porque el PRD no los autoriza: su §15 declara que el orden de las Job Stories «no expresa prioridad ni autoriza a omitir historias», y `AC-10` exige verificar esa ausencia. Por la misma razón no se usan etiquetas de historia de usuario: el fundamento usa Job Stories, no historias de usuario, y `SH-AP` advierte contra imponerlas.

## Inventario de cobertura

Ningún elemento obligatorio queda sin destino. **Toda obligación tiene tareas de implementación y tareas de verificación.**

Las tablas citan las tareas **principales** de cada referencia. La trazabilidad de *toda* tarea, incluidas las de preparación e integración, está en su etiqueta `[REF]`: las 149 declaran un identificador de fuente, requisito, regla, decisión aprobada o sección del PRD. No hay tareas sin fundamento.

### Job Stories

| Referencia | Implementan | Verifican | Dependencias | Estado |
|---|---|---|---|---|
| `JS-01` | T104 | T138, T149 | T103 | Cubierto |
| `JS-02` | T104, T106 | T138, T149 | T043 | Cubierto |
| `JS-03` | T047, T048, T107, T108 | T139, T149 | T046 | Cubierto |
| `JS-04` | T051, T105 | T141, T140 | T095 | Cubierto |
| `JS-05` | T043, T045, T106, T067 | T137, T144 | T044 | Cubierto |
| `JS-06` | T109 | T139, T149 | T055 | Cubierto |
| `JS-07` | T053, T110 | T149 | T073 | Cubierto |
| `JS-08` | T062, T120 | T144, T147 | T059 | Cubierto |
| `JS-09` | T059–T063, T076–T083, T099 | T145, T147 | T028 | Cubierto |

### Requisitos funcionales

| Referencia | Implementan | Verifican | Dependencias | Estado |
|---|---|---|---|---|
| `FR-001` | T050, T104 | T139 | T103 | Cubierto |
| `FR-002` | T098, T060 | T139 | T059 | Cubierto |
| `FR-003` | T043, T045, T106 | T137 | T044 | Cubierto |
| `FR-004` | T046, T047, T048, T107, T108 | T027, T149 | T015 | Cubierto |
| `FR-005` | T047, T048, T051, T105 | T149 | T046 | Cubierto |
| `FR-006` | T047, T048 | T027 | T015 | Cubierto |
| `FR-007` | T109 | T139 | T055 | Cubierto |
| `FR-008` | T110 | T149 | T053 | Cubierto |
| `FR-009` | T053, T110 | T073 | T020 | Cubierto |
| `FR-010` | T053, T073, T110 | T039, T144 | T020 | Cubierto |
| `FR-011` | T062, T095, T120 | T144 | T059 | Cubierto |
| `FR-012` | T009, T054, T111 | T144 | T021 | Cubierto |
| `FR-013` | T091, T092, T118 | T141 | T090 | Cubierto |
| `FR-014` | T067, T113 | T147 | T059 | Cubierto |
| `FR-015` | T105, T115, T119, T121 | T115, T122 | T103 | Cubierto |
| `FR-016` | T065, T066, T068–T071, T123 | T072, T144 | T059 | Cubierto |
| `FR-017` | T095, T096 | T149 | T022 | Cubierto |
| `FR-018` | T126, T127, T129 | T128, T144 | T127 | Cubierto |
| `FR-019` | T059–T063, T076–T080 | T064, T147 | T028 | Cubierto |
| `FR-020` | T118, T119 | T147 | T059 | Cubierto |
| `FR-021` | T002, T011, T015–T033 | T041, T148 | T003 | Cubierto |

### Criterios de aceptación

| Referencia | Implementan | Verifican | Dependencias | Estado |
|---|---|---|---|---|
| `AC-01` | T104 | **T138 (humana)** | T115 | Cubierto |
| `AC-02` | T104, T106 | **T138 (humana)** | T115 | Cubierto |
| `AC-03` | T043, T044 | T137 | T044 | Cubierto |
| `AC-04` | T047, T048 | T027, T137 | T046 | Cubierto |
| `AC-05` | T104, T097 | **T139 (humana)** | T115 | Cubierto |
| `AC-06` | T098, T113, T118, T120 | T141, T147 | T118 | Cubierto |
| `AC-07` | T092, T101, T116, T117 | T101, T102, **T140 (humana)** | T090 | Cubierto |
| `AC-08` | T004, T115 | T133, T143 | T132 | Cubierto |
| `AC-09` | T053, T110 | T073, **T149 (humana)** | T020 | Cubierto |
| `AC-10` | Este archivo y `plan.md` | `analyze` + **T153** | — | Cubierto |
| `AC-11` | T062, T067, T068–T071 | T144 | T059 | Cubierto |
| `AC-12` | T126, T127 | T128, T129 | T127 | Cubierto |
| `AC-13` | T076–T080 | **T145 (humana)**, T146 | T081, T082 | **Bloqueado por dependencia externa** |
| `AC-14` | T059–T063, T118 | T147 | T059 | Cubierto |
| `AC-15` | T025–T033, T064, T072, T074 | T148, T144 | T032 | Cubierto |
| `AC-16` | T005, T010 | T012 | T003 | Cubierto |

### Reglas, estados y excepciones

| Referencia | Implementan | Verifican |
|---|---|---|
| `BR-001`–`BR-003` | T028, T031, T060, T080 | T064, T145 |
| `BR-004` | T043, T095 | T137 |
| `BR-005` + voz autoral (`CL-04`) | T022, T056, T057, T096 | T149 |
| `BR-006` | Ausencia por diseño | `analyze`, T153 |
| `BR-007` | T025–T033, T041 | T034–T040, T148 |
| `BR-008` | T126, T127 | T128 |
| `BR-009` | T072 | T144 |
| `ST-001`–`ST-005` | T028, T113 | T151 |
| `EX-001`–`EX-003` | T115, T114, T135 | T115, T147, T134 |
| `SC-001`–`SC-008` | — | T138, T139, T143, T144, T152 |

---

## Bloque 1 · `B01` Preparación necesaria

**Propósito**: dejar el repositorio en condiciones de validar y construir de forma reproducible.
**Dependencias**: ninguna.

- [ ] T001 [B01·plan.md] Crear la estructura de directorios de `plan.md` en `src/{content,schema,lib,tokens,components,layouts,pages,islands}`, `public/` y `tests/` — árbol coincide con «Estructura del proyecto».
- [ ] T002 [B01·FR-021] Configurar el repositorio remoto `https://github.com/dacunao/sitio-software-humano` y publicar la rama principal — `FR-021` exige contenido versionado **en GitHub**; sin remoto ese requisito no se cumple, y es el repositorio cuyas Issues son el canal de contacto de `CL-07`.
- [ ] T003 [B01·AS-006] Crear `package.json` con los scripts del contrato de `quickstart.md` y **fijar la versión de bun** en `.bun-version` y en el campo `packageManager` — `bun --version` coincide con la versión fijada.
- [ ] T004 [P] [B01·PRD §24.6] Instalar Astro y configurar `astro.config.mjs` con salida estática, `site: "https://softwarehumano.com"`, `defaultLocale: "en"`, locales `en`, `es`, `pt-BR`, y prefijo solo para los no predeterminados — `bun run build` produce HTML sin JavaScript de aplicación.
- [ ] T005 [P] [B01·AC-16] Configurar `tsconfig.json` con comprobación estricta, prohibición efectiva de `any` y `noUncheckedIndexedAccess` — `bun run typecheck` falla ante un `any` introducido a propósito.
- [ ] T006 [P] [B01·PRD §24.6] Instalar Tailwind CSS y daisyUI sin tema propio todavía, dejando la configuración preparada para consumir los tokens de T090 — la instalación no fija colores ni tipografías.
- [ ] T007 [P] [B01·CL-12] Crear `LICENSE` con el texto de MIT para el código fuente del sitio — archivo presente en la raíz.
- [ ] T008 [P] [B01·CL-05] Crear `LICENSE-CONTENT` declarando CC BY 4.0 para el texto canónico y el contenido editorial, con su URL — archivo presente y referenciado desde `README`.
- [ ] T009 [B01·JS-07] Crear `README.md` con el propósito del repositorio, cómo construirlo, y la declaración de licencias —código MIT, texto y contenido CC BY 4.0— en la raíz — `JS-07` invita a comprender el piloto y `CL-12` lo publica para ser estudiado: un repositorio público sin README deja esa invitación sin respuesta.
- [ ] T010 [B01·VB-11] Implementar el script `typecheck` — ejecutable y con salida no cero ante error de tipado.
- [ ] T011 [B01·FR-021] Configurar integración continua que ejecute `bun install --frozen-lockfile`, `typecheck`, las validaciones de contenido y `build` — una violación de cualquier regla **detiene** la integración.
- [ ] T012 [B01·AC-16] Registrar la evidencia de `AC-16`: comprobación estricta sin errores sobre el árbol completo — salida del comando archivada.
- [ ] T013 [P] [B01·AS-006] Añadir a `.gitignore` los archivos de bloqueo de npm, yarn y pnpm y versionar el de bun — el repositorio contiene un único archivo de bloqueo.
- [ ] T014 [B01·PRD §24.5] Verificar reproducibilidad: instalación congelada desde cero en un entorno limpio produce el mismo árbol — dos instalaciones sucesivas coinciden.

## Bloque 2 · `B02` Fundamentos compartidos: modelo de contenido y validación

**Resultado cubierto**: `FR-021`, `AC-15`, `BR-003`, `BR-005`, `BR-007`.
**Dependencias**: T001–T011.
**Criterio de integración**: el build se detiene ante cada regla de `data-model.md`, demostrado con casos negativos.

### Esquema y tipos

- [ ] T015 [B02·FR-004] Definir el esquema de `Principio` en `src/schema/principio.ts` con los campos de `data-model.md`: `id` en `P01`–`P10` **único y exactamente diez**, las ocho secciones obligatorias, `capitulo` en `proposito | complejidad-atencion | confianza-continuidad | agencia`, `pruebas_de_decision` con **al menos un elemento**, y `relaciones.job_stories` y `relaciones.requisitos` con **al menos un elemento cada una** — el esquema rechaza una entrada a la que falte cualquiera de las ocho secciones.
- [ ] T016 [P] [B02·FR-003] Definir `SeccionCanonica` en `src/schema/seccion-canonica.ts` con `id` estable único, `ancla` obligatoria, `fuente`, `fuente_traduccion` por idioma, `version_nucleo` igual a `2.1` y `es_traduccion` booleano que **obliga** a declarar referencia al original cuando es verdadero — rechaza una traducción sin referencia al original.
- [ ] T017 [P] [B02·BR-004] Definir `ExplicacionEditorial` en `src/schema/explicacion.ts` con `origen_ref` obligatorio, `estado_editorial` que **nunca** puede ser `canonico_aprobado`, y `registro` en `editorial | voz_autoral` — rechaza una explicación marcada como canónica.
- [ ] T018 [P] [B02·PRD §18.1] Definir `Superficie` en `src/schema/superficie.ts` con `id` restringido a las **seis** de PRD §18.1, `slug`, `titulo` y `descripcion` traducibles y `tipo_schema` — rechaza una séptima superficie.
- [ ] T019 [P] [B02·PRD §16] Definir `Acto` en `src/schema/acto.ts` con `id` en `A1`–`A7`, **exactamente siete**, orden fijo, y `principios_ref` obligatorio solo en `A4` con los diez agrupados por capítulo — rechaza seis u ocho actos.
- [ ] T020 [P] [B02·FR-009] Definir `EstadoPreset` en `src/schema/preset.ts` con `version`, `validado_tecnicamente`, `limitaciones` con **al menos un elemento**, `estado` en `no-publicado | publicado`, `licencia`, y `repositorio`, `download_url`, `sha256` y `catalogo_comunidad` nulables — acepta nulos con `no-publicado`.
- [ ] T021 [P] [B02·FR-012] Definir `MetadatosPublicacion` en `src/schema/metadatos.ts` con `origen`, `nombre_sitio` **no traducible**, `autor` como `Person`, `licencia_contenido`, `licencia_codigo`, `contacto`, `version_nucleo` y `fecha_actualizacion` — rechaza `nombre_sitio` declarado traducible.
- [ ] T022 [B02·BR-005] Definir `EstadoEditorial` con los seis estados y el atributo ortogonal `registro` para la voz autoral en `src/schema/estados.ts` — los seis existen y la voz autoral no es un séptimo estado.
- [ ] T023 [B02·BR-003] Definir `EstadoTraduccion` con la secuencia `ausente → borrador → en_revision → aprobada` y el campo de responsable de aprobación en `src/schema/estados.ts` — solo `aprobada` habilita publicación.
- [ ] T024 [B02·PRD §24.6] Derivar los tipos de TypeScript desde los esquemas como fuente única en `src/schema/index.ts`, sin declararlos por duplicado — un cambio de esquema rompe el tipado de los consumidores.

### Validadores que detienen el build

- [ ] T025 [B02·VB-01] Implementar la detección de identificadores duplicados dentro de un tipo en `src/lib/validators/ids.ts` — detiene ante duplicado.
- [ ] T026 [B02·VB-02] Implementar la comprobación de referencias íntegras para `seccion_canonica_ref`, `origen_ref`, `principios_ref` y `relaciones.*` en `src/lib/validators/referencias.ts` — detiene ante referencia rota.
- [ ] T027 [B02·VB-03] Implementar la comprobación de campos obligatorios, incluidas las ocho secciones de un `Principio`, en `src/lib/validators/obligatorios.ts` — detiene ante sección faltante.
- [ ] T028 [B02·VB-04] Implementar la comprobación de paridad de traducciones: un `id` publicable en un idioma declarado disponible debe tener entrada con `EstadoTraduccion: aprobada` en `src/lib/validators/paridad.ts` — detiene ante traducción no aprobada.
- [ ] T029 [B02·VB-05] Implementar la comprobación de que cada `ancla` declarada existe en el documento fuente, en `src/lib/validators/anclas.ts` — detiene ante ancla inexistente.
- [ ] T030 [B02·VB-08] Implementar la verificación de marcadores de voseo (`vos`, `sos`, `tenés`, `podés`, imperativos como `mirá` o `decí`) y de `vosotros` (`os`, `vuestro`, terminaciones `-áis`, `-éis`) sobre contenido `es` en `src/lib/validators/neutralidad.ts` — detiene ante coincidencia.
- [ ] T031 [B02·VB-09] Implementar la detección de mezcla de idiomas en una entrada publicada, admitiendo nombre propio y cita identificada, en `src/lib/validators/mezcla.ts` — detiene ante mezcla no justificada.
- [ ] T032 [B02·AC-15] Implementar el script `validate:content` que ejecuta T025–T029 en `src/lib/validate-content.ts` — salida no cero ante cualquier violación.
- [ ] T033 [B02·AC-13] Implementar el script `validate:lang` que ejecuta T030 y T031 — salida no cero ante cualquier violación.

### Evidencia: casos negativos

> Una regla sin caso negativo que demuestre la detención **no se considera implementada** (`data-model.md`).

- [ ] T034 [P] [B02·VB-01] Crear caso negativo de identificador duplicado en `tests/negativos/vb-01.test.ts` — el build falla.
- [ ] T035 [P] [B02·VB-02] Crear caso negativo de referencia rota en `tests/negativos/vb-02.test.ts` — el build falla.
- [ ] T036 [P] [B02·VB-03] Crear caso negativo de sección obligatoria ausente en `tests/negativos/vb-03.test.ts` — el build falla.
- [ ] T037 [P] [B02·VB-04] Crear caso negativo de traducción requerida incompleta en `tests/negativos/vb-04.test.ts` — el build falla.
- [ ] T038 [P] [B02·VB-05] Crear caso negativo de ancla inexistente en `tests/negativos/vb-05.test.ts` — el build falla.
- [ ] T039 [P] [B02·VB-08] Crear caso negativo con voseo y con `vosotros` en `tests/negativos/vb-08.test.ts` — el build falla.
- [ ] T040 [P] [B02·VB-09] Crear caso negativo de mezcla de idiomas en `tests/negativos/vb-09.test.ts` — el build falla.
- [ ] T041 [B02·BR-007] Verificar que **cada** regla detiene el build y no solo advierte — la suite de casos negativos pasa completa.
- [ ] T042 [B02·FR-021] Comprobar que una modificación de contenido permite saber qué cambió, qué idiomas afecta y qué páginas y datos estructurados genera — informe de build que lo declara.

## Bloque 3 · `B03` Contenido real en español

**Resultado cubierto**: `FR-003`–`FR-007`, `FR-012`, `AC-03`, `AC-04`, `JS-01`–`JS-03`, `JS-05`–`JS-07`.
**Dependencias**: T015–T033.
**Criterio de integración**: el contenido real existe y valida; habilita `B04`, `B05` y `B06`.

- [ ] T043 [B03·RQ-01] Implementar el lector de la fuente protegida en `src/lib/nucleo.ts`, que **lee sin copiar** `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md` y extrae su estructura de encabezados y anclas — no se crea ninguna copia del texto en `src/content/`.
- [ ] T044 [B03·AC-03] Implementar la verificación de integridad de esa fuente contra `SHA256SUMS` en `src/lib/nucleo.ts` — el build falla si el archivo fue alterado.
- [ ] T045 [B03·FR-003] Crear las entradas de `SeccionCanonica` en `src/content/canonico/` con `id`, `ancla` y `version_nucleo`, referenciando la fuente — todas las anclas validan contra T029.
- [ ] T046 [B03·FR-004] Crear la estructura de las diez entradas de `Principio` en `src/content/principios/` con sus identificadores, capítulo y relaciones — `validate:content` pasa con las diez.
- [ ] T047 [B03·AC-04·FR-006] Redactar las ocho secciones de `P01`–`P05` en `src/content/principios/` — cada uno con consecuencia y al menos una prueba de decisión utilizable.
- [ ] T048 [B03·AC-04·FR-006] Redactar las ocho secciones de `P06`–`P10` en `src/content/principios/` — mismo criterio.
- [ ] T049 [B03·PRD §16] Asignar los cuatro capítulos de presentación sin alterar el orden canónico, en `src/content/principios/` — `P01`–`P02`, `P03`–`P06`, `P07`–`P09`, `P10`.
- [ ] T050 [B03·FR-001] Crear los siete actos en `src/content/actos/` con el recorrido problema → consecuencias → tesis → principios → aplicación → SpecKit — `validate:content` pasa con siete.
- [ ] T051 [B03·FR-005] Redactar la comparación del Acto 2 —una respuesta centrada en el sistema y una centrada en la persona— con alternativa textual equivalente, en `src/content/actos/a2.yaml` — la comparación se comprende sin interacción.
- [ ] T052 [B03·PRD §18.1] Crear las seis entradas de `Superficie` con slug, título y descripción en español, en `src/content/superficies/` — seis exactas.
- [ ] T053 [B03·FR-009] Crear la entrada de `EstadoPreset` con `estado: no-publicado`, `version: 1.0.1`, `licencia: MIT`, `repositorio: https://github.com/dacunao/spec-kit-preset-software-humano`, `download_url: null`, `sha256: null` y las limitaciones declaradas, en `src/content/preset.yaml` — valida con nulos.
- [ ] T054 [B03·FR-012] Crear `MetadatosPublicacion` con origen, nombre único, autoría `Person`, ambas licencias, contacto y versión del núcleo, en `src/content/metadatos.yaml` — valida contra T021.
- [ ] T055 [B03·FR-007] Redactar las explicaciones editoriales de la superficie de Aplicación —fundamento, Job Stories, flujo, artefactos, contrato del agente, detenciones y definición de terminado— en `src/content/explicaciones/`, cada una con `origen_ref` — todas referencian su origen.
- [ ] T056 [B03·CL-04] Redactar la nota de origen en primera persona con `registro: voz_autoral` en `src/content/explicaciones/origen.yaml` — es la **única** entrada con ese registro.
- [ ] T057 [B03·BR-005] Asignar estado editorial a cada entrada de contenido — ninguna queda sin estado.
- [ ] T058 [B03·AC-03] Comparar el contenido publicado contra el núcleo v2.1 y registrar la evidencia — identificadores, orden y texto coinciden.

## Bloque 4 · `B04` Topología de rutas y semántica

**Resultado cubierto**: `FR-011`, `FR-014`, `FR-016`, `FR-019`, `AC-11`, `AC-14`, `AC-15`, `JS-05`, `JS-08`.
**Dependencias**: T045–T054.
**Criterio de integración**: conmutación de idioma, `hreflang` y canónicas salen del mismo dato y no pueden divergir.

- [ ] T059 [B04·RQ-02] Implementar el mapa de equivalencia en `src/lib/rutas/mapa.ts`, generado en build desde el `id` estable compartido entre idiomas — un `id` sin traducción aprobada **no tiene entrada** para ese idioma.
- [ ] T060 [B04·FR-019] Implementar el enrutamiento por idioma en `src/pages/`: inglés sin prefijo incluida la raíz, `/es/` y `/pt-br/` con la misma topología — las tres raíces responden.
- [ ] T061 [B04·PRD §25.2] Implementar los slugs localizados por superficie y principio desde el contenido, en `src/lib/rutas/slugs.ts` — las URLs son comprensibles en cada idioma.
- [ ] T062 [B04·FR-011] Emitir `<link rel="canonical">` absoluto por página e idioma en `src/layouts/` — cada página declara su propia canónica.
- [ ] T063 [B04·FR-019] Emitir `hreflang` recíprocos por idioma con traducción aprobada, más `x-default` apuntando a la ruta sin prefijo, en `src/layouts/` — reciprocidad completa.
- [ ] T064 [B04·VB-06] Implementar el validador de reciprocidad `hreflang` y correspondencia con el mapa en `src/lib/validators/rutas.ts` — detiene ante falta de recíproco.
- [ ] T065 [B04·FR-016] Generar el sitemap con las tres versiones y sus relaciones en `src/pages/sitemap.xml.ts` — incluye los tres idiomas.
- [ ] T066 [P] [B04·FR-016] Configurar `robots` de forma explícita en `public/robots.txt` — declara sitemap y no bloquea las versiones localizadas.
- [ ] T067 [B04·FR-014] Implementar anclas estables y restitución de sección al regresar a una URL profunda en `src/lib/rutas/anclas.ts` — la URL profunda abre la sección correcta.
- [ ] T068 [B04·AC-11] Emitir JSON-LD `WebSite` con `name`, `url`, `inLanguage` y `author`, y `Person` para la autoría, desde `src/lib/jsonld/sitio.ts` — el tipo de autoría es `Person`, no `Organization`.
- [ ] T069 [B04·PRD §25.3] Emitir JSON-LD `CreativeWork` del manifiesto con `version`, `inLanguage`, `author`, `datePublished`, `license` apuntando a CC BY 4.0, y `translationOfWork`/`workTranslation` entre versiones, desde `src/lib/jsonld/manifiesto.ts` — las relaciones entre obras son reales.
- [ ] T070 [B04·AC-11] Emitir `DefinedTermSet` y `DefinedTerm` por principio conservando `P01`–`P10` como identificador, desde `src/lib/jsonld/principios.ts` — los diez son entidades enlazables.
- [ ] T071 [B04·PRD §25.2] Emitir `BreadcrumbList` **solo** en páginas cuya navegación visible muestre esa jerarquía, desde `src/lib/jsonld/breadcrumb.ts` — ausente donde no corresponde.
- [ ] T072 [B04·VB-10] Implementar el validador que comprueba que cada entidad, relación, fecha, versión y URL del JSON-LD existe en la página visible, en `src/lib/validators/semantica.ts` — detiene ante marcado especulativo.
- [ ] T073 [B04·VB-07] Implementar la regla de emisión condicional: `SoftwareSourceCode` **solo** con `estado: publicado`, y detención si `publicado` carece de `repositorio`, `download_url` o `sha256`, en `src/lib/validators/preset.ts` — con `no-publicado` no se emite marcado del preset.
- [ ] T074 [B04·VB-12] Implementar los scripts `validate:routes`, `validate:semantics` y `check:links` — salida no cero ante enlace interno roto o incoherencia.

## Bloque 5 · `B05` Traducciones y aprobación lingüística

**Resultado cubierto**: `FR-019`, `AC-13`, `BR-003`, `JS-09`.
**Dependencias**: T043–T058.
**Criterio de integración**: el criterio de terminado **no es que el texto exista**, sino que exista registro de revisión aprobada (`CL-09`).

- [ ] T075 [B05·CL-09] Preparar el paquete de revisión en formato Markdown para el proveedor externo, generado desde el contenido, en `tools/revision/` — el proveedor no necesita editar YAML.
- [ ] T076 [B05·FR-003] Producir la traducción canónica al inglés general en `src/content/canonico/en/` como Markdown referenciado, declarando su condición de traducción y la referencia al original en español — valida contra T016.
- [ ] T077 [B05·FR-003] Producir la traducción canónica al portugués de Brasil en `src/content/canonico/pt-br/` con `pt-BR` en metadatos — valida contra T016.
- [ ] T078 [B05·FR-019] Traducir al inglés general el contenido editorial: principios, actos, superficies, explicaciones — `validate:content` pasa con paridad.
- [ ] T079 [B05·FR-019] Traducir al portugués de Brasil el mismo alcance — `validate:content` pasa con paridad.
- [ ] T080 [B05·BR-003] Implementar el registro de aprobación por idioma con responsable identificado en `src/content/aprobaciones/` — `EstadoTraduccion` refleja el estado real.
- [ ] T081 [B05·CL-09] **Dependencia externa**: encargar y obtener la revisión profesional nativa del inglés general — registro de revisión **aprobada**; sin él, `BR-003` impide publicar ese idioma.
- [ ] T082 [B05·CL-09] **Dependencia externa**: encargar y obtener la revisión profesional nativa del portugués de Brasil — registro de revisión **aprobada**.
- [ ] T083 [B05·AC-13] **Revisión humana de la autoridad de producto**: neutralidad latinoamericana del español, sin voseo, `vosotros` ni localismos nacionales — registro de aprobación. `R03` deja constancia de que esta revisión no tiene segunda mirada.

## Bloque 6 · `B06` Exploración visual y tokens

**Resultado cubierto**: `CL-03`, PRD §21.2, `AC-07` parcial.
**Dependencias**: T043–T058 y borradores de T076–T079.
**Criterio de integración**: **contiene una detención humana**. Sin aprobación no se fijan tokens y `B07`–`B12` permanecen bloqueados.

- [ ] T084 [B06·PRD §21.1.8] Preparar la muestra de contenido **real** en los tres idiomas —tesis del Acto 3, un principio completo con sus ocho secciones y un fragmento canónico— en `design/muestra/` — **prohibido contenido simulado**.
- [ ] T085 [B06·CL-03] Producir la dirección visual A sobre esa muestra en `design/direccion-a/` — tipografía, color, ritmo, diagramas y movimiento propuestos.
- [ ] T086 [B06·CL-03] Producir la dirección visual B sobre la misma muestra en `design/direccion-b/` — alternativa genuinamente distinta, no una variación de A.
- [ ] T087 [B06·AC-07] Verificar el contraste de texto y de componentes de **ambas** direcciones contra WCAG 2.2 AA en `design/contraste.md` — el contraste se resuelve antes de elegir, porque §21.1.6 lo trata como condición de función.
- [ ] T088 [B06·PRD §21.7] Probar la expansión de texto entre los tres idiomas sobre ambas direcciones en `design/expansion.md` — cortes y cambios de jerarquía detectados antes de fijar tokens.
- [ ] T089 [B06·R05] **DETENCIÓN. Presentar ambas direcciones a la autoridad de producto y obtener su elección** — decisión registrada con fecha. Ningún agente puede aprobarla ni atribuirse esta revisión.
- [ ] T090 [B06·PRD §24.6] Fijar los tokens de la dirección elegida en `src/tokens/` — escala tipográfica, roles de color, ritmo de espaciado y puntos de quiebre.
- [ ] T091 [B06·FR-013] Definir la política de movimiento en `src/tokens/movimiento.ts`, con movimiento solo cuando explique una relación y respeto de `prefers-reduced-motion` — sin movimiento no esencial.

## Bloque 7 · `B07` Sistema de componentes sobre daisyUI

**Resultado cubierto**: `FR-013`, `FR-017`, `AC-07`, `P08`.
**Dependencias**: T090, T091.
**Criterio de integración**: daisyUI queda subordinado a los tokens; ningún componente define identidad.

- [ ] T092 [B07·AC-07] Implementar la capa base en `src/components/base/` sobre HTML semántico, con foco visible, lógico y no oculto, y tamaño adecuado de objetivos — la capa funciona sin estilos.
- [ ] T093 [B07·PRD §21.2] Implementar la escala tipográfica desde tokens en `src/components/base/tipografia.css` — la lectura es la prioridad declarada.
- [ ] T094 [B07·PRD §24.6] Configurar daisyUI para consumir exclusivamente los tokens y eliminar clases no utilizadas de la salida, en `tailwind.config.ts` — ningún color o tipografía proviene del tema por defecto.
- [ ] T095 [B07·FR-017] Implementar el componente que distingue **visual y semánticamente** cita canónica, explicación, ejemplo, inferencia o propuesta y estado técnico confirmado, en `src/components/procedencia/` — la distinción sobrevive a copiar y pegar.
- [ ] T096 [B07·BR-005] Implementar los indicadores de estado editorial y del registro de voz autoral en `src/components/procedencia/estado.astro` — los seis estados y la voz autoral son reconocibles.
- [ ] T097 [B07·PRD §21.3] Implementar las capas progresivas con `details`/`summary` nativos, con títulos explícitos y estados accesibles, en `src/components/capas/` — funcionan sin JavaScript.
- [ ] T098 [B07·FR-002] Implementar la navegación global con las ocho posibilidades de PRD §18.2 en `src/components/navegacion/` — acción principal variable por contexto, sin llamados compitiendo con el mismo peso.
- [ ] T099 [B07·PRD §24.6] Implementar el conmutador de idioma como **enlaces generados en build** desde el mapa de T059, nombrando English, Español y Português (Brasil) sin depender de banderas, en `src/components/navegacion/idioma.astro` — no hay sustitución de texto en cliente.
- [ ] T100 [B07·FR-004] Implementar la vista de principio con sus ocho secciones y el vínculo al pasaje canónico, en `src/components/principio/` — las ocho son visibles o alcanzables.
- [ ] T101 [B07·PRD §21.5] Verificar las doce comprobaciones de accesibilidad que apliquen a cada componente y registrar el resultado en `tests/a11y/componentes.test.ts` — sin errores críticos.
- [ ] T102 [B07·AC-07] Implementar el script `audit:a11y` que ejecuta el barrido automatizado WCAG 2.2 AA sobre componentes y superficies, en `tools/audit/a11y.ts` — salida no cero ante error crítico. **No sustituye** la revisión humana de `AC-07`.

## Bloque 8 · `B08` Superficies y recorrido

**Resultado cubierto**: `JS-01`–`JS-08`, `FR-001`–`FR-010`, `FR-015`, `ST-001`–`ST-005`, `EX-002`.
**Dependencias**: T059–T074, T076–T083, T092–T101.
**Criterio de integración**: el recorrido completo es utilizable **sin JavaScript**.

- [ ] T103 [B08·FR-019] Implementar el layout base en `src/layouts/Base.astro` con `lang` correcto por idioma, metadatos localizados, canónica, `hreflang` y JSON-LD — el idioma activo es perceptible también para tecnologías de asistencia.
- [ ] T104 [B08·FR-001] Implementar la superficie Inicio con los siete actos en `src/pages/index.astro` y sus equivalentes localizados — una idea dominante por momento; **no se secuestra el scroll**.
- [ ] T105 [B08·JS-04] Implementar la comparación del Acto 2 como **interacción sin JavaScript** —revelación o alternancia mediante `details`/`summary` nativos—, con alternativa textual equivalente, en `src/components/comparacion/` — PRD §16 declara el Acto 2 como **interacción** y `P02` pide «comparar dos respuestas que llegan al mismo contenido con cargas distintas»: una comparación meramente estática no lo satisface. La información completa permanece disponible con movimiento reducido y por teclado.
- [ ] T106 [B08·FR-003] Implementar la superficie Manifiesto con índice, identificadores, anclas estables y el texto canónico íntegro leído de la fuente, en `src/pages/[...manifiesto].astro` — el texto se alcanza desde cualquier superficie.
- [ ] T107 [B08·FR-004] Implementar el explorador de principios en `src/pages/[...principios]/index.astro` conservando orden, identidad y fuente — los diez recorribles.
- [ ] T108 [B08·JS-03] Implementar la página de principio individual en `src/pages/[...principios]/[principio].astro` — abre directamente sin recorrer la narrativa.
- [ ] T109 [B08·FR-007] Implementar la superficie Aplicación en `src/pages/[...aplicacion].astro` traduciendo los conceptos antes del mecanismo — **no abre con rutas, archivos, YAML ni comandos** (`P03`).
- [ ] T110 [B08·FR-008] Implementar la superficie SpecKit en `src/pages/[...speckit].astro` con las cuatro capas, el estado real y **render condicional** por `EstadoPreset.estado` — con `no-publicado` muestra estado, arquitectura y disponibilidad futura, y **ningún enlace, botón o puntero sin destino**.
- [ ] T111 [B08·FR-012] Implementar la superficie Acerca de en `src/pages/[...acerca-de].astro` con procedencia, autoría `Person`, ambas licencias, gobernanza, la nota de origen en voz autoral y los dos canales de `CL-07` —`mailto:manifiestosoftwarehumano@gmail.com` e Issues de `https://github.com/dacunao/sitio-software-humano`— en los tres idiomas — el `mailto:` es texto plano **sin ofuscación por JavaScript**, que rompería `FR-015` y la accesibilidad.
- [ ] T112 [B08·ST-004] Implementar la página 404 útil y orientadora en `src/pages/404.astro`, con rutas de vuelta al recorrido y al texto canónico — orientadora en los tres idiomas.
- [ ] T113 [B08·ST-001..ST-005] Implementar los estados de vacío, carga, éxito, error y recuperación en las superficies — el contenido inicial no depende de animación ni de petición tardía.
- [ ] T114 [B08·EX-002] Implementar el comportamiento ante traducción ausente: informar la ausencia y ofrecer alternativa comprensible **sin mezclar idiomas** — la página publicada no mezcla idiomas.
- [ ] T115 [B08·FR-015] Verificar el recorrido completo con JavaScript deshabilitado en `tests/sin-js.test.ts` — texto, navegación primaria, URLs profundas y contenido canónico disponibles.
- [ ] T116 [B08·PRD §21.4] Verificar jerarquía equivalente en móvil, tablet y escritorio, con **diagramas reestructurados y no reducidos** hasta la ilegibilidad — sin exigir orientación horizontal ni gestos complejos.
- [ ] T117 [B08·PRD §21.4] Verificar que el orden de lectura semántico permanece correcto **sin CSS** — la página sin estilos se lee en orden.

## Bloque 9 · `B09` Islas justificadas

**Resultado cubierto**: `FR-013`, `FR-020`, `ST-003`, `AC-06`, `AC-14`.
**Dependencias**: T103–T117.
**Criterio de integración**: suprimir cualquier isla **no elimina información ni acceso** (`research.md` · `RQ-03`).

- [ ] T118 [B09·FR-020] Implementar la isla de preferencias de idioma y movimiento en `src/islands/Preferencias.tsx` — la elección se conserva **localmente**, es reversible, se puede restablecer y **no requiere cuenta**.
- [ ] T119 [B09·EX-001] Verificar el comportamiento sin JavaScript de T118: rutas sin prefijo en inglés y `prefers-reduced-motion` respetado por CSS — solo se pierde el recuerdo, que `FR-020` declara prescindible.
- [ ] T120 [B09·ST-003] Implementar la isla de copiar y compartir con atribución diferenciada en `src/islands/Compartir.tsx` — confirmación clara y **sin captura de datos**; la copia distingue cita canónica de explicación editorial.
- [ ] T121 [B09·EX-001] Verificar el comportamiento sin JavaScript de T120: texto seleccionable y URL estable y visible — el resultado de `JS-08` se alcanza igual.
- [ ] T122 [B09·FR-015] Verificar que la supresión de ambas islas no elimina información ni acceso en `tests/islas.test.ts` — el recorrido conserva su resultado.

## Bloque 10 · `B10` Descubrimiento y medición

**Resultado cubierto**: `FR-016`, `FR-018`, `AC-12`, `CL-08`, `BR-008`.
**Dependencias**: T059–T074, T103–T117.
**Criterio de integración**: ningún origen de red fuera de `softwarehumano.com` y del beacon autorizado.

- [ ] T123 [B10·FR-016] Implementar Open Graph y tarjetas sociales con textos **fieles al contenido visible**, `og:locale` y `og:locale:alternate`, en `src/layouts/Base.astro` — sin promesas ausentes de la página.
- [ ] T124 [P] [B10·CL-08] Configurar la verificación de Google Search Console por DNS o archivo — **sin script en el sitio**; provee impresiones, clics y consultas por idioma.
- [ ] T125 [P] [B10·SC-006] Establecer la línea base de CrUX y PageSpeed Insights para el origen — **sin script**; se documenta si el origen todavía no dispone de datos de campo (`R02`).
- [ ] T126 [B10·CL-08] Insertar **manualmente** el beacon de Cloudflare Web Analytics en `src/layouts/Base.astro` — el único script de terceros queda **visible y versionado** en el repositorio (`research.md` · `RQ-04`).
- [ ] T127 [B10·PRD §24.3] Declarar la política de seguridad de contenido en `public/_headers` con `script-src` admitiendo `https://static.cloudflareinsights.com`, `connect-src` admitiendo `https://cloudflareinsights.com`, y **`form-action 'none'`** — este último expresa la decisión de `CL-06` y `CL-07` de no tener formularios.
- [ ] T128 [B10·BR-008] Implementar el script `audit:network` que inventaría las peticiones del recorrido completo en `tools/audit/network.ts` — cualquier origen distinto de los dos autorizados es **fallo**, no observación.
- [ ] T129 [B10·AC-12] Verificar que el sitio se lee íntegramente **sin registro ni entrega de información personal** y que ningún contenido se bloquea por falta de consentimiento — evidencia registrada.

## Bloque 11 · `B11` Despliegue

**Resultado cubierto**: PRD §24.2, §24.3, `EX-003`, `CL-11`.
**Dependencias**: T001–T014, T123–T129.
**Criterio de integración**: una reversión restituye contenido **y** configuración.

- [ ] T130 [B11·PRD §24.3] Completar `public/_headers` con `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy` restrictivo y `Permissions-Policy` denegando lo no usado — encabezados versionados en el repositorio.
- [ ] T131 [B11·EX-003] Crear `public/_redirects` con las redirecciones necesarias y su regla de mantenimiento — versionado junto al contenido.
- [ ] T132 [B11·CL-11] Configurar el proyecto en Cloudflare Pages y el dominio `softwarehumano.com` con las tres raíces de idioma — el sitio responde en el origen canónico.
- [ ] T133 [B11·AC-08] Implementar el script `audit:perf` que mide los presupuestos de PRD §24.1 sobre el sitio desplegado, en `tools/audit/perf.ts` — reporta LCP, INP y CLS y declara si la fuente es campo o laboratorio representativo.
- [ ] T134 [B11·PRD §24.2] Probar una reversión de despliegue y comprobar que restituye contenido **y** encabezados y redirecciones juntos — evidencia registrada.
- [ ] T135 [B11·EX-003] Verificar que un cambio de estructura de URLs conserva redirecciones y contenido canónico versionado — sin enlaces rotos tras el cambio.
- [ ] T136 [B11·SC-007] Ejecutar `check:links` sobre el despliegue y confirmar ausencia de enlaces internos rotos antes de liberar — cero rotos.

## Bloque 12 · `B12` Evidencia y aceptación

**Resultado cubierto**: `AC-01`–`AC-16`, `SC-001`–`SC-008`, PRD §26.4, §32.
**Dependencias**: todos los bloques anteriores.
**Criterio de integración**: **ninguna auditoría automática sustituye la revisión humana** (`STOP07`, PRD §32).

- [ ] T137 [B12·AC-03] Verificación 1: revisión de contenido contra el núcleo, con comparación de integridad y lectura humana — registro de comparación.
- [ ] T138 [B12·AC-01,AC-02] Verificación 2: **pruebas moderadas de comprensión, humanas**, con representantes de las audiencias de PRD §14.1 — las personas explican el problema sin mencionar primero una funcionalidad del sitio.
- [ ] T139 [B12·AC-05] Verificación 3: **prueba de navegación sin explicación previa, humana** — observación registrada.
- [ ] T140 [B12·AC-07] Verificación 4: **revisión completa por teclado y lector de pantalla, humana**, más el barrido automatizado `audit:a11y` — registro por recorrido; la auditoría automática no lo sustituye.
- [ ] T141 [B12·AC-06] Verificación 5: prueba con movimiento reducido — misma información sin movimiento no esencial.
- [ ] T142 [B12·PRD §21.4] Verificación 6: **evaluación móvil y escritorio con contenido real, humana** — prohibido aprobar con contenido simulado.
- [ ] T143 [B12·AC-08] Verificación 7: auditoría de rendimiento contra los presupuestos de PRD §24.1 — LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1; se declara si la fuente es campo o laboratorio representativo.
- [ ] T144 [B12·AC-11,AC-15] Verificación 8: comprobación de enlaces, metadatos y datos estructurados — sin errores críticos y sin marcado de contenido inexistente.
- [ ] T145 [B12·AC-13] Verificación 9: **revisión lingüística humana aprobada** en los tres idiomas — registro de aprobación por idioma; sin él la versión 1.0 no puede aceptarse.
- [ ] T146 [B12·BR-002] Verificación 10: ausencia de voseo, `vosotros` y localismos nacionales, por comando **y** por revisión humana — `R03` deja constancia del límite.
- [ ] T147 [B12·AC-14] Verificación 11: prueba de cambio de idioma y correspondencia de URLs — la persona se mantiene en la entidad equivalente y una URL explícita no es sustituida.
- [ ] T148 [B12·AC-15] Verificación 12: validación del modelo de contenido y sus reglas de integridad con los casos negativos — la suite completa pasa.
- [ ] T149 [B12·PRD §32] Verificación 13: **revisión humana del recorrido completo** — dictamen de la autoridad de producto sobre comprensión, confianza, control y coherencia con los diez principios.

## Verificación del resultado completo

- [ ] T150 [VERIF·V01] Reconciliar cada fila del inventario de cobertura con la implementación — matriz sin vacíos ni tareas huérfanas.
- [ ] T151 [VERIF·V09] Verificar el recorrido completo incluidos estados vacíos, carga, error, extremos y recuperación — evidencia registrada.
- [ ] T152 [VERIF·SH-SCORE] Evaluar comprensión, esfuerzo, confianza, control, accesibilidad y rendimiento — hallazgos y evidencia; ninguna dimensión crítica puntúa 0.
- [ ] T153 [VERIF·AC-10] Registrar pendientes, supuestos, excepciones aprobadas y decisiones humanas requeridas, y **verificar que no se introdujeron prioridades, MVP ni exclusiones inventadas** — estado explícito.

## Dependencias y orden de ejecución

| Bloque | Depende de | Puede ejecutarse en paralelo con | Bloquea |
|---|---|---|---|
| `B01` T001–T014 | ninguna | — | todo |
| `B02` T015–T042 | `B01` | — | `B03`, `B04` |
| `B03` T043–T058 | `B02` | — | `B04`, `B05`, `B06` |
| `B04` T059–T074 | `B02`, `B03` | `B05` | `B08`, `B10` |
| `B05` T075–T083 | `B03` | `B04` | `B06` (borradores), `B08` |
| `B06` T084–T091 | `B03`, borradores de `B05` | — | `B07`–`B12` |
| `B07` T092–T102 | `B06` | — | `B08` |
| `B08` T103–T117 | `B04`, `B05`, `B07` | — | `B09`, `B10` |
| `B09` T118–T122 | `B08` | `B10` | `B12` |
| `B10` T123–T129 | `B04`, `B08` | `B09` | `B11` |
| `B11` T130–T136 | `B01`, `B10` | — | `B12` |
| `B12` T137–T149 | todos | — | aceptación |

### Detenciones que el orden no puede resolver

- **T089** · elección de dirección visual. Requiere la autoridad de producto. Bloquea `B07`–`B12`.
- **T081, T082** · revisión profesional externa. Bloquea `AC-13` y, con él, la aceptación de la 1.0.
- **T083** · revisión humana de neutralidad del español.
- **T138, T139, T140, T142, T149** · verificaciones humanas que ninguna herramienta sustituye.

## Notas sobre esta derivación

**No se asignó prioridad, MVP, independencia ni entrega incremental.** El PRD no los autoriza; su §15 declara que el orden de las Job Stories no expresa prioridad, y `AC-10` exige verificar esa ausencia. En lugar del «alcance de MVP sugerido» del comando nativo, esta sección describe el orden técnico neutro: `B01`–`B03` construyen la base de contenido validado, `B04`–`B05` la topología y la paridad lingüística, `B06`–`B07` la identidad visual y sus componentes, `B08`–`B09` las superficies y sus dos islas, `B10`–`B11` descubrimiento y despliegue, `B12` la evidencia. **Ningún bloque completado reduce ni redefine el alcance comprometido.**

**No se usaron etiquetas de historia de usuario.** El fundamento usa Job Stories; `SH-AP` advierte contra imponer historias de usuario, y la plantilla del preset usa `[REF]` trazable en su lugar.

**Las pruebas no se omitieron por no haber sido pedidas con esa palabra.** `AC-07`, `AC-08`, `AC-15`, `AC-16` y `SC-007` exigen evidencia, y `BR-007` exige detención efectiva: por eso T034–T041 existen como casos negativos, sin los cuales una regla de validación no se considera implementada.
