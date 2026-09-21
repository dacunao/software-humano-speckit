---
description: "Tareas trazables para implementar el alcance completo"
---

# Tareas: Sitio público del Manifiesto de Software Humano

**Entrada obligatoria**: [spec.md](./spec.md), [plan.md](./plan.md)
**Entradas condicionales**: [research.md](./research.md), [data-model.md](./data-model.md), [contracts/rutas-y-semantica.md](./contracts/rutas-y-semantica.md), [quickstart.md](./quickstart.md) — los cuatro declarados necesarios en `plan.md`

## Formato

`- [X] T009 [P?] [REF] Acción concreta en ruta/archivo — Evidencia esperada`

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
| `JS-01` | T112 | T146, T157 | T111 | Cubierto |
| `JS-02` | T112, T114 | T146, T157 | T051 | Cubierto |
| `JS-03` | T055, T056, T115, T116 | T147, T157 | T054 | Cubierto |
| `JS-04` | T059, T113 | T149, T148 | T103 | Cubierto |
| `JS-05` | T051, T053, T114, T075 | T145, T152 | T052 | Cubierto |
| `JS-06` | T117 | T147, T157 | T063 | Cubierto |
| `JS-07` | T061, T118 | T157 | T081 | Cubierto |
| `JS-08` | T070, T128 | T152, T155 | T067 | Cubierto |
| `JS-09` | T067–T071, T084–T091, T107 | T153, T155 | T036 | Cubierto |

### Requisitos funcionales

| Referencia | Implementan | Verifican | Dependencias | Estado |
|---|---|---|---|---|
| `FR-001` | T058, T112 | T147 | T111 | Cubierto |
| `FR-002` | T106, T068 | T147 | T067 | Cubierto |
| `FR-003` | T051, T053, T114 | T145 | T052 | Cubierto |
| `FR-004` | T054, T055, T056, T115, T116 | T035, T157 | T023 | Cubierto |
| `FR-005` | T055, T056, T059, T113 | T157 | T054 | Cubierto |
| `FR-006` | T055, T056 | T035 | T023 | Cubierto |
| `FR-007` | T117 | T147 | T063 | Cubierto |
| `FR-008` | T118 | T157 | T061 | Cubierto |
| `FR-009` | T061, T118 | T081 | T028 | Cubierto |
| `FR-010` | T061, T081, T118 | T047, T152 | T028 | Cubierto |
| `FR-011` | T070, T103, T128 | T152 | T067 | Cubierto |
| `FR-012` | T017, T062, T119 | T152 | T029 | Cubierto |
| `FR-013` | T099, T100, T126 | T149 | T098 | Cubierto |
| `FR-014` | T075, T121 | T155 | T067 | Cubierto |
| `FR-015` | T113, T123, T127, T129 | T123, T130 | T111 | Cubierto |
| `FR-016` | T073, T074, T076–T079, T131 | T080, T152 | T067 | Cubierto |
| `FR-017` | T103, T104 | T157 | T030 | Cubierto |
| `FR-018` | T134, T135, T137 | T136, T152 | T135 | Cubierto |
| `FR-019` | T067–T071, T084–T088 | T072, T155 | T036 | Cubierto |
| `FR-020` | T126, T127 | T155 | T067 | Cubierto |
| `FR-021` | T010, T019, T023–T041 | T049, T156 | T011 | Cubierto |

### Criterios de aceptación

| Referencia | Implementan | Verifican | Dependencias | Estado |
|---|---|---|---|---|
| `AC-01` | T112 | **T146 (humana)** | T123 | Cubierto |
| `AC-02` | T112, T114 | **T146 (humana)** | T123 | Cubierto |
| `AC-03` | T051, T052 | T145 | T052 | Cubierto |
| `AC-04` | T055, T056 | T035, T145 | T054 | Cubierto |
| `AC-05` | T112, T105 | **T147 (humana)** | T123 | Cubierto |
| `AC-06` | T106, T121, T126, T128 | T149, T155 | T126 | Cubierto |
| `AC-07` | T100, T109, T124, T125 | T109, T110, **T148 (humana)** | T098 | Cubierto |
| `AC-08` | T012, T123 | T141, T151 | T140 | Cubierto |
| `AC-09` | T061, T118 | T081, **T157 (humana)** | T028 | Cubierto |
| `AC-10` | Este archivo y `plan.md` | `analyze` + **T161** | — | Cubierto |
| `AC-11` | T070, T075, T076–T079 | T152 | T067 | Cubierto |
| `AC-12` | T134, T135 | T136, T137 | T135 | Cubierto |
| `AC-13` | T084–T088 | **T153 (humana)**, T154 | T089, T090 | **Bloqueado por dependencia externa** |
| `AC-14` | T067–T071, T126 | T155 | T067 | Cubierto |
| `AC-15` | T033–T041, T072, T080, T082 | T156, T152 | T040 | Cubierto |
| `AC-16` | T013, T018 | T020 | T011 | Cubierto |

### Reglas, estados y excepciones

| Referencia | Implementan | Verifican |
|---|---|---|
| `BR-001`–`BR-003` | T036, T039, T068, T088 | T072, T153 |
| `BR-004` | T051, T103 | T145 |
| `BR-005` + voz autoral (`CL-04`) | T030, T064, T065, T104 | T157 |
| `BR-006` | Ausencia por diseño | `analyze`, T161 |
| `BR-007` | T033–T041, T049 | T042–T048, T156 |
| `BR-008` | T134, T135 | T136 |
| `BR-009` | T080 | T152 |
| `ST-001`–`ST-005` | T036, T121 | T159 |
| `EX-001`–`EX-003` | T123, T122, T143 | T123, T155, T142 |
| `SC-001`–`SC-008` | — | T146, T147, T151, T152, T160 |

---

## Bloque 0 · `B00` Separación de repositorios

**Resultado cubierto**: `FR-021`, `CL-07`, `CL-12`, `CL-13`.
**Dependencias**: ninguna.
**Criterio de integración**: **ningún artefacto rector queda duplicado** en los dos repositorios. `AGENTS.md` es explícito: dos copias de instrucciones rectoras divergen.

> Este bloque existe porque la sesión S1 descubrió, al escribir archivos en la raíz, que este repositorio es el del **paquete de método** y no el del sitio. `FR-021`, `CL-07` y `CL-12` suponían un repositorio del sitio que no existía como entidad separada. `CL-13` lo resuelve.

- [ ] T001 [B00·CL-13] Crear el repositorio público `dacunao/sitio-software-humano` en GitHub, sin README ni licencia generados automáticamente — **acción que publica: requiere autorización humana explícita en el momento de ejecutarla**, no basta la autorización general de `implement`.
- [ ] T002 [B00·CL-13] Instalar el preset `software-humano` en el nuevo repositorio siguiendo `instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md` y materializar la constitución v2.1 — `integration status` reporta los ocho comandos compuestos y la constitución coincide byte a byte con la proyección del preset.
- [ ] T003 [B00·AC-10] Trasladar `specs/001-sitio-manifiesto/` íntegro: `spec.md`, `plan.md`, `tasks.md`, los cuatro auxiliares y el checklist — identificadores y trazabilidad conservados **sin renumerar**.
- [ ] T004 [B00·PRD §2.3] Trasladar el fundamento de producto `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md` — **archivo protegido: requiere instrucción humana explícita**. Sin él el nuevo repositorio carece de fuente autorizada y `STOP01` se activa.
- [ ] T005 [B00·CL-13] Crear en el nuevo repositorio `AGENTS.md` y `CLAUDE.md` con su sección «Completar por proyecto» — declara fundamento, autoridad, identificadores a preservar, decisiones técnicas aprobadas y contrato lingüístico del sitio.
- [ ] T006 [B00·CL-13] Trasladar los artefactos de código de S1: `src/`, `tests/`, `public/`, `design/`, `tools/audit/`, `tools/revision/`, `astro.config.mjs`, `tsconfig.json`, `package.json`, `bun.lock`, `.bun-version` y `.github/workflows/ci.yml` — en el nuevo repositorio pasan `bun install --frozen-lockfile`, `typecheck`, `bun test` y `build`.
- [ ] T007 [B00·AGENTS.md] Retirar del repositorio de método lo que ya viva en el del sitio — **corresponde a la sesión que mantiene el paquete de método**. Esta sesión lo reporta y no lo ejecuta.
- [ ] T008 [B00·AGENTS.md] Verificar que ningún artefacto rector queda duplicado entre ambos repositorios — comprobación explícita y registrada, no implícita.

## Bloque 1 · `B01` Preparación necesaria

**Propósito**: dejar el repositorio en condiciones de validar y construir de forma reproducible.
**Dependencias**: ninguna.

- [X] T009 [B01·plan.md] Crear la estructura de directorios de `plan.md` en `src/{content,schema,lib,tokens,components,layouts,pages,islands}`, `public/` y `tests/` — árbol coincide con «Estructura del proyecto».
- [ ] T010 [B01·FR-021] Configurar el remoto del **repositorio del sitio** creado en `B00` y publicar su rama principal — `FR-021` exige contenido versionado **en GitHub**; es además el repositorio cuyas Issues son el canal de contacto de `CL-07`. No se ejecuta sobre el repositorio del paquete de método.
- [X] T011 [B01·AS-006] Crear `package.json` con los scripts del contrato de `quickstart.md` y **fijar la versión de bun** en `.bun-version` y en el campo `packageManager` — `bun --version` coincide con la versión fijada.
- [X] T012 [P] [B01·PRD §24.6] Instalar Astro y configurar `astro.config.mjs` con salida estática, `site: "https://softwarehumano.com"`, `defaultLocale: "en"`, locales `en`, `es`, `pt-BR`, y prefijo solo para los no predeterminados — `bun run build` produce HTML sin JavaScript de aplicación.
- [X] T013 [P] [B01·AC-16] Configurar `tsconfig.json` con comprobación estricta, prohibición efectiva de `any` y `noUncheckedIndexedAccess` — `bun run typecheck` falla ante un `any` introducido a propósito.
- [X] T014 [P] [B01·PRD §24.6] Instalar Tailwind CSS y daisyUI sin tema propio todavía, dejando la configuración preparada para consumir los tokens de T098 — la instalación no fija colores ni tipografías.
- [ ] T015 [P] [B01·CL-12] Crear `LICENSE` con el texto de MIT **en la raíz del repositorio del sitio** — archivo presente. No se coloca en el repositorio del paquete de método, cuya licencia es decisión de la sesión que lo mantiene.
- [ ] T016 [P] [B01·CL-05] Crear `LICENSE-CONTENT` declarando CC BY 4.0 para el texto canónico y el contenido editorial, con su URL, **en la raíz del repositorio del sitio** — archivo presente y referenciado desde su `README.md`.
- [ ] T017 [B01·JS-07] Crear `README.md` **en la raíz del repositorio del sitio** con su propósito, cómo construirlo y la declaración de licencias (código MIT, texto y contenido CC BY 4.0) — `JS-07` invita a comprender el piloto y `CL-12` lo publica para ser estudiado: un repositorio público sin README deja esa invitación sin respuesta. El `README.md` del paquete de método es otro archivo, está protegido y no se toca.
- [X] T018 [B01·VB-11] Implementar el script `typecheck` — ejecutable y con salida no cero ante error de tipado.
- [X] T019 [B01·FR-021] Configurar integración continua que ejecute `bun install --frozen-lockfile`, `typecheck`, las validaciones de contenido y `build` — una violación de cualquier regla **detiene** la integración.
- [X] T020 [B01·AC-16] Registrar la evidencia de `AC-16`: comprobación estricta sin errores sobre el árbol completo — salida del comando archivada.
- [X] T021 [P] [B01·AS-006] Añadir a `.gitignore` los archivos de bloqueo de npm, yarn y pnpm y versionar el de bun — el repositorio contiene un único archivo de bloqueo.
- [X] T022 [B01·PRD §24.5] Verificar reproducibilidad: instalación congelada desde cero en un entorno limpio produce el mismo árbol — dos instalaciones sucesivas coinciden.

## Bloque 2 · `B02` Fundamentos compartidos: modelo de contenido y validación

**Resultado cubierto**: `FR-021`, `AC-15`, `BR-003`, `BR-005`, `BR-007`.
**Dependencias**: T009–T019.
**Criterio de integración**: el build se detiene ante cada regla de `data-model.md`, demostrado con casos negativos.

### Esquema y tipos

- [X] T023 [B02·FR-004] Definir el esquema de `Principio` en `src/schema/principio.ts` con los campos de `data-model.md`: `id` en `P01`–`P10` **único y exactamente diez**, las ocho secciones obligatorias, `capitulo` en `proposito | complejidad-atencion | confianza-continuidad | agencia`, `pruebas_de_decision` con **al menos un elemento**, y `relaciones.job_stories` y `relaciones.requisitos` con **al menos un elemento cada una** — el esquema rechaza una entrada a la que falte cualquiera de las ocho secciones.
- [X] T024 [P] [B02·FR-003] Definir `SeccionCanonica` en `src/schema/seccion-canonica.ts` con `id` estable único, `ancla` obligatoria, `fuente`, `fuente_traduccion` por idioma, `version_nucleo` igual a `2.1` y `es_traduccion` booleano que **obliga** a declarar referencia al original cuando es verdadero — rechaza una traducción sin referencia al original.
- [X] T025 [P] [B02·BR-004] Definir `ExplicacionEditorial` en `src/schema/explicacion.ts` con `origen_ref` obligatorio, `estado_editorial` que **nunca** puede ser `canonico_aprobado`, y `registro` en `editorial | voz_autoral` — rechaza una explicación marcada como canónica.
- [X] T026 [P] [B02·PRD §18.1] Definir `Superficie` en `src/schema/superficie.ts` con `id` restringido a las **seis** de PRD §18.1, `slug`, `titulo` y `descripcion` traducibles y `tipo_schema` — rechaza una séptima superficie.
- [X] T027 [P] [B02·PRD §16] Definir `Acto` en `src/schema/acto.ts` con `id` en `A1`–`A7`, **exactamente siete**, orden fijo, y `principios_ref` obligatorio solo en `A4` con los diez agrupados por capítulo — rechaza seis u ocho actos.
- [X] T028 [P] [B02·FR-009] Definir `EstadoPreset` en `src/schema/preset.ts` con `version`, `validado_tecnicamente`, `limitaciones` con **al menos un elemento**, `estado` en `no-publicado | publicado`, `licencia`, y `repositorio`, `download_url`, `sha256` y `catalogo_comunidad` nulables — acepta nulos con `no-publicado`.
- [X] T029 [P] [B02·FR-012] Definir `MetadatosPublicacion` en `src/schema/metadatos.ts` con `origen`, `nombre_sitio` **no traducible**, `autor` como `Person`, `licencia_contenido`, `licencia_codigo`, `contacto`, `version_nucleo` y `fecha_actualizacion` — rechaza `nombre_sitio` declarado traducible.
- [X] T030 [B02·BR-005] Definir `EstadoEditorial` con los seis estados y el atributo ortogonal `registro` para la voz autoral en `src/schema/estados.ts` — los seis existen y la voz autoral no es un séptimo estado.
- [X] T031 [B02·BR-003] Definir `EstadoTraduccion` con la secuencia `ausente → borrador → en_revision → aprobada` y el campo de responsable de aprobación en `src/schema/estados.ts` — solo `aprobada` habilita publicación.
- [X] T032 [B02·PRD §24.6] Derivar los tipos de TypeScript desde los esquemas como fuente única en `src/schema/index.ts`, sin declararlos por duplicado — un cambio de esquema rompe el tipado de los consumidores.

### Validadores que detienen el build

- [X] T033 [B02·VB-01] Implementar la detección de identificadores duplicados dentro de un tipo en `src/lib/validators/ids.ts` — detiene ante duplicado.
- [X] T034 [B02·VB-02] Implementar la comprobación de referencias íntegras para `seccion_canonica_ref`, `origen_ref`, `principios_ref` y `relaciones.*` en `src/lib/validators/referencias.ts` — detiene ante referencia rota.
- [X] T035 [B02·VB-03] Implementar la comprobación de campos obligatorios, incluidas las ocho secciones de un `Principio`, en `src/lib/validators/obligatorios.ts` — detiene ante sección faltante.
- [X] T036 [B02·VB-04] Implementar la comprobación de paridad de traducciones: un `id` publicable en un idioma declarado disponible debe tener entrada con `EstadoTraduccion: aprobada` en `src/lib/validators/paridad.ts` — detiene ante traducción no aprobada.
- [X] T037 [B02·VB-05] Implementar la comprobación de que cada `ancla` declarada existe en el documento fuente, en `src/lib/validators/anclas.ts` — detiene ante ancla inexistente.
- [X] T038 [B02·VB-08] Implementar la verificación de marcadores de voseo (`vos`, `sos`, `tenés`, `podés`, imperativos como `mirá` o `decí`) y de `vosotros` (`os`, `vuestro`, terminaciones `-áis`, `-éis`) sobre contenido `es` en `src/lib/validators/neutralidad.ts` — detiene ante coincidencia.
- [X] T039 [B02·VB-09] Implementar la detección de mezcla de idiomas en una entrada publicada, admitiendo nombre propio y cita identificada, en `src/lib/validators/mezcla.ts` — detiene ante mezcla no justificada.
- [X] T040 [B02·AC-15] Implementar el script `validate:content` que ejecuta T033–T037 en `src/lib/validate-content.ts` — salida no cero ante cualquier violación.
- [X] T041 [B02·AC-13] Implementar el script `validate:lang` que ejecuta T038 y T039 — salida no cero ante cualquier violación.

### Evidencia: casos negativos

> Una regla sin caso negativo que demuestre la detención **no se considera implementada** (`data-model.md`).

- [X] T042 [P] [B02·VB-01] Crear caso negativo de identificador duplicado en `tests/negativos/vb-01.test.ts` — el build falla.
- [X] T043 [P] [B02·VB-02] Crear caso negativo de referencia rota en `tests/negativos/vb-02.test.ts` — el build falla.
- [X] T044 [P] [B02·VB-03] Crear caso negativo de sección obligatoria ausente en `tests/negativos/vb-03.test.ts` — el build falla.
- [X] T045 [P] [B02·VB-04] Crear caso negativo de traducción requerida incompleta en `tests/negativos/vb-04.test.ts` — el build falla.
- [X] T046 [P] [B02·VB-05] Crear caso negativo de ancla inexistente en `tests/negativos/vb-05.test.ts` — el build falla.
- [X] T047 [P] [B02·VB-08] Crear caso negativo con voseo y con `vosotros` en `tests/negativos/vb-08.test.ts` — el build falla.
- [X] T048 [P] [B02·VB-09] Crear caso negativo de mezcla de idiomas en `tests/negativos/vb-09.test.ts` — el build falla.
- [X] T049 [B02·BR-007] Verificar que **cada** regla detiene el build y no solo advierte — la suite de casos negativos pasa completa.
- [ ] T050 [B02·FR-021] Implementar el informe de impacto en `src/lib/impacto.ts`: qué cambió, qué identificadores afecta, en qué idiomas y con qué registro de aprobación — informe de build que lo declara. **La otra mitad de `FR-021` —qué páginas y qué datos estructurados genera— se cierra en `T082`**, porque depende de la topología de rutas y del emisor de JSON-LD.

## Bloque 3 · `B03` Contenido real en español

**Resultado cubierto**: `FR-003`–`FR-007`, `FR-012`, `AC-03`, `AC-04`, `JS-01`–`JS-03`, `JS-05`–`JS-07`.
**Dependencias**: T023–T041.
**Criterio de integración**: el contenido real existe y valida; habilita `B04`, `B05` y `B06`.

- [ ] T051 [B03·RQ-01] Implementar el lector de la fuente protegida en `src/lib/nucleo.ts`, que **lee sin copiar** `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md` y extrae su estructura de encabezados y anclas — no se crea ninguna copia del texto en `src/content/`.
- [ ] T052 [B03·AC-03] Implementar la verificación de integridad de esa fuente contra `SHA256SUMS` en `src/lib/nucleo.ts` — el build falla si el archivo fue alterado.
- [ ] T053 [B03·FR-003] Crear las entradas de `SeccionCanonica` en `src/content/canonico/` con `id`, `ancla` y `version_nucleo`, referenciando la fuente — todas las anclas validan contra T037.
- [ ] T054 [B03·FR-004] Crear la estructura de las diez entradas de `Principio` en `src/content/principios/` con sus identificadores, capítulo y relaciones — `validate:content` pasa con las diez.
- [ ] T055 [B03·AC-04·FR-006] Redactar las ocho secciones de `P01`–`P05` en `src/content/principios/` — cada uno con consecuencia y al menos una prueba de decisión utilizable.
- [ ] T056 [B03·AC-04·FR-006] Redactar las ocho secciones de `P06`–`P10` en `src/content/principios/` — mismo criterio.
- [ ] T057 [B03·PRD §16] Asignar los cuatro capítulos de presentación sin alterar el orden canónico, en `src/content/principios/` — `P01`–`P02`, `P03`–`P06`, `P07`–`P09`, `P10`.
- [ ] T058 [B03·FR-001] Crear los siete actos en `src/content/actos/` con el recorrido problema → consecuencias → tesis → principios → aplicación → SpecKit — `validate:content` pasa con siete.
- [ ] T059 [B03·FR-005] Redactar la comparación del Acto 2 —una respuesta centrada en el sistema y una centrada en la persona— con alternativa textual equivalente, en `src/content/actos/a2.yaml` — la comparación se comprende sin interacción.
- [ ] T060 [B03·PRD §18.1] Crear las seis entradas de `Superficie` con slug, título y descripción en español, en `src/content/superficies/` — seis exactas.
- [ ] T061 [B03·FR-009] Crear la entrada de `EstadoPreset` con `estado: no-publicado`, `version: 1.0.1`, `licencia: MIT`, `repositorio: https://github.com/dacunao/spec-kit-preset-software-humano`, `download_url: null`, `sha256: null` y las limitaciones declaradas, en `src/content/preset.yaml` — valida con nulos.
- [ ] T062 [B03·FR-012] Crear `MetadatosPublicacion` con origen, nombre único, autoría `Person`, ambas licencias, contacto y versión del núcleo, en `src/content/metadatos.yaml` — valida contra T029.
- [ ] T063 [B03·FR-007] Redactar las explicaciones editoriales de la superficie de Aplicación —fundamento, Job Stories, flujo, artefactos, contrato del agente, detenciones y definición de terminado— en `src/content/explicaciones/`, cada una con `origen_ref` — todas referencian su origen.
- [ ] T064 [B03·CL-04] Redactar la nota de origen en primera persona con `registro: voz_autoral` en `src/content/explicaciones/origen.yaml` — es la **única** entrada con ese registro.
- [ ] T065 [B03·BR-005] Asignar estado editorial a cada entrada de contenido — ninguna queda sin estado.
- [ ] T066 [B03·AC-03] Comparar el contenido publicado contra el núcleo v2.1 y registrar la evidencia — identificadores, orden y texto coinciden.

## Bloque 4 · `B04` Topología de rutas y semántica

**Resultado cubierto**: `FR-011`, `FR-014`, `FR-016`, `FR-019`, `AC-11`, `AC-14`, `AC-15`, `JS-05`, `JS-08`.
**Dependencias**: T053–T062.
**Criterio de integración**: conmutación de idioma, `hreflang` y canónicas salen del mismo dato y no pueden divergir.

- [ ] T067 [B04·RQ-02] Implementar el mapa de equivalencia en `src/lib/rutas/mapa.ts`, generado en build desde el `id` estable compartido entre idiomas — un `id` sin traducción aprobada **no tiene entrada** para ese idioma.
- [ ] T068 [B04·FR-019] Implementar el enrutamiento por idioma en `src/pages/`: inglés sin prefijo incluida la raíz, `/es/` y `/pt-br/` con la misma topología — las tres raíces responden.
- [ ] T069 [B04·PRD §25.2] Implementar los slugs localizados por superficie y principio desde el contenido, en `src/lib/rutas/slugs.ts` — las URLs son comprensibles en cada idioma.
- [ ] T070 [B04·FR-011] Emitir `<link rel="canonical">` absoluto por página e idioma en `src/layouts/` — cada página declara su propia canónica.
- [ ] T071 [B04·FR-019] Emitir `hreflang` recíprocos por idioma con traducción aprobada, más `x-default` apuntando a la ruta sin prefijo, en `src/layouts/` — reciprocidad completa.
- [ ] T072 [B04·VB-06] Implementar el validador de reciprocidad `hreflang` y correspondencia con el mapa en `src/lib/validators/rutas.ts` — detiene ante falta de recíproco.
- [ ] T073 [B04·FR-016] Generar el sitemap con las tres versiones y sus relaciones en `src/pages/sitemap.xml.ts` — incluye los tres idiomas.
- [ ] T074 [P] [B04·FR-016] Configurar `robots` de forma explícita en `public/robots.txt` — declara sitemap y no bloquea las versiones localizadas.
- [ ] T075 [B04·FR-014] Implementar anclas estables y restitución de sección al regresar a una URL profunda en `src/lib/rutas/anclas.ts` — la URL profunda abre la sección correcta.
- [ ] T076 [B04·AC-11] Emitir JSON-LD `WebSite` con `name`, `url`, `inLanguage` y `author`, y `Person` para la autoría, desde `src/lib/jsonld/sitio.ts` — el tipo de autoría es `Person`, no `Organization`.
- [ ] T077 [B04·PRD §25.3] Emitir JSON-LD `CreativeWork` del manifiesto con `version`, `inLanguage`, `author`, `datePublished`, `license` apuntando a CC BY 4.0, y `translationOfWork`/`workTranslation` entre versiones, desde `src/lib/jsonld/manifiesto.ts` — las relaciones entre obras son reales.
- [ ] T078 [B04·AC-11] Emitir `DefinedTermSet` y `DefinedTerm` por principio conservando `P01`–`P10` como identificador, desde `src/lib/jsonld/principios.ts` — los diez son entidades enlazables.
- [ ] T079 [B04·PRD §25.2] Emitir `BreadcrumbList` **solo** en páginas cuya navegación visible muestre esa jerarquía, desde `src/lib/jsonld/breadcrumb.ts` — ausente donde no corresponde.
- [ ] T080 [B04·VB-10] Implementar el validador que comprueba que cada entidad, relación, fecha, versión y URL del JSON-LD existe en la página visible, en `src/lib/validators/semantica.ts` — detiene ante marcado especulativo.
- [ ] T081 [B04·VB-07] Implementar la regla de emisión condicional: `SoftwareSourceCode` **solo** con `estado: publicado`, y detención si `publicado` carece de `repositorio`, `download_url` o `sha256`, en `src/lib/validators/preset.ts` — con `no-publicado` no se emite marcado del preset.
- [ ] T082 [B04·VB-12·FR-021] Implementar los scripts `validate:routes`, `validate:semantics` y `check:links`, **extender el `build` de `package.json` para incluirlos**, y completar el informe de impacto de `T050` con las páginas y los datos estructurados que genera cada cambio — salida no cero ante enlace interno roto o incoherencia. `FR-021` queda cerrado entre `T050` y esta tarea.

## Bloque 5 · `B05` Traducciones y aprobación lingüística

**Resultado cubierto**: `FR-019`, `AC-13`, `BR-003`, `JS-09`.
**Dependencias**: T051–T066.
**Criterio de integración**: el criterio de terminado **no es que el texto exista**, sino que exista registro de revisión aprobada (`CL-09`).

- [ ] T083 [B05·CL-09] Preparar el paquete de revisión en formato Markdown para el proveedor externo, generado desde el contenido, en `tools/revision/` — el proveedor no necesita editar YAML.
- [ ] T084 [B05·FR-003] Producir la traducción canónica al inglés general en `src/content/canonico/en/` como Markdown referenciado, declarando su condición de traducción y la referencia al original en español — valida contra T024.
- [ ] T085 [B05·FR-003] Producir la traducción canónica al portugués de Brasil en `src/content/canonico/pt-br/` con `pt-BR` en metadatos — valida contra T024.
- [ ] T086 [B05·FR-019] Traducir al inglés general el contenido editorial: principios, actos, superficies, explicaciones — `validate:content` pasa con paridad.
- [ ] T087 [B05·FR-019] Traducir al portugués de Brasil el mismo alcance — `validate:content` pasa con paridad.
- [ ] T088 [B05·BR-003] Implementar el registro de aprobación por idioma con responsable identificado en `src/content/aprobaciones/` — `EstadoTraduccion` refleja el estado real.
- [ ] T089 [B05·CL-09] **Dependencia externa**: encargar y obtener la revisión profesional nativa del inglés general — registro de revisión **aprobada**; sin él, `BR-003` impide publicar ese idioma.
- [ ] T090 [B05·CL-09] **Dependencia externa**: encargar y obtener la revisión profesional nativa del portugués de Brasil — registro de revisión **aprobada**.
- [ ] T091 [B05·AC-13] **Revisión humana de la autoridad de producto**: neutralidad latinoamericana del español, sin voseo, `vosotros` ni localismos nacionales — registro de aprobación. `R03` deja constancia de que esta revisión no tiene segunda mirada.

## Bloque 6 · `B06` Exploración visual y tokens

**Resultado cubierto**: `CL-03`, PRD §21.2, `AC-07` parcial.
**Dependencias**: T051–T066 y borradores de T084–T087.
**Criterio de integración**: **contiene una detención humana**. Sin aprobación no se fijan tokens y `B07`–`B12` permanecen bloqueados.

- [ ] T092 [B06·PRD §21.1.8] Preparar la muestra de contenido **real** en los tres idiomas —tesis del Acto 3, un principio completo con sus ocho secciones y un fragmento canónico— en `design/muestra/` — **prohibido contenido simulado**.
- [ ] T093 [B06·CL-03] Producir la dirección visual A sobre esa muestra en `design/direccion-a/` — tipografía, color, ritmo, diagramas y movimiento propuestos.
- [ ] T094 [B06·CL-03] Producir la dirección visual B sobre la misma muestra en `design/direccion-b/` — alternativa genuinamente distinta, no una variación de A.
- [ ] T095 [B06·AC-07] Verificar el contraste de texto y de componentes de **ambas** direcciones contra WCAG 2.2 AA en `design/contraste.md` — el contraste se resuelve antes de elegir, porque §21.1.6 lo trata como condición de función.
- [ ] T096 [B06·PRD §21.7] Probar la expansión de texto entre los tres idiomas sobre ambas direcciones en `design/expansion.md` — cortes y cambios de jerarquía detectados antes de fijar tokens.
- [ ] T097 [B06·R05] **DETENCIÓN. Presentar ambas direcciones a la autoridad de producto y obtener su elección** — decisión registrada con fecha. Ningún agente puede aprobarla ni atribuirse esta revisión.
- [ ] T098 [B06·PRD §24.6] Fijar los tokens de la dirección elegida en `src/tokens/` — escala tipográfica, roles de color, ritmo de espaciado y puntos de quiebre.
- [ ] T099 [B06·FR-013] Definir la política de movimiento en `src/tokens/movimiento.ts`, con movimiento solo cuando explique una relación y respeto de `prefers-reduced-motion` — sin movimiento no esencial.

## Bloque 7 · `B07` Sistema de componentes sobre daisyUI

**Resultado cubierto**: `FR-013`, `FR-017`, `AC-07`, `P08`.
**Dependencias**: T098, T099.
**Criterio de integración**: daisyUI queda subordinado a los tokens; ningún componente define identidad.

- [ ] T100 [B07·AC-07] Implementar la capa base en `src/components/base/` sobre HTML semántico, con foco visible, lógico y no oculto, y tamaño adecuado de objetivos — la capa funciona sin estilos.
- [ ] T101 [B07·PRD §21.2] Implementar la escala tipográfica desde tokens en `src/components/base/tipografia.css` — la lectura es la prioridad declarada.
- [ ] T102 [B07·PRD §24.6] Configurar daisyUI para consumir exclusivamente los tokens y eliminar clases no utilizadas de la salida, en `tailwind.config.ts` — ningún color o tipografía proviene del tema por defecto.
- [ ] T103 [B07·FR-017] Implementar el componente que distingue **visual y semánticamente** cita canónica, explicación, ejemplo, inferencia o propuesta y estado técnico confirmado, en `src/components/procedencia/` — la distinción sobrevive a copiar y pegar.
- [ ] T104 [B07·BR-005] Implementar los indicadores de estado editorial y del registro de voz autoral en `src/components/procedencia/estado.astro` — los seis estados y la voz autoral son reconocibles.
- [ ] T105 [B07·PRD §21.3] Implementar las capas progresivas con `details`/`summary` nativos, con títulos explícitos y estados accesibles, en `src/components/capas/` — funcionan sin JavaScript.
- [ ] T106 [B07·FR-002] Implementar la navegación global con las ocho posibilidades de PRD §18.2 en `src/components/navegacion/` — acción principal variable por contexto, sin llamados compitiendo con el mismo peso.
- [ ] T107 [B07·PRD §24.6] Implementar el conmutador de idioma como **enlaces generados en build** desde el mapa de T067, nombrando English, Español y Português (Brasil) sin depender de banderas, en `src/components/navegacion/idioma.astro` — no hay sustitución de texto en cliente.
- [ ] T108 [B07·FR-004] Implementar la vista de principio con sus ocho secciones y el vínculo al pasaje canónico, en `src/components/principio/` — las ocho son visibles o alcanzables.
- [ ] T109 [B07·PRD §21.5] Verificar las doce comprobaciones de accesibilidad que apliquen a cada componente y registrar el resultado en `tests/a11y/componentes.test.ts` — sin errores críticos.
- [ ] T110 [B07·AC-07] Implementar el script `audit:a11y` que ejecuta el barrido automatizado WCAG 2.2 AA sobre componentes y superficies, en `tools/audit/a11y.ts` — salida no cero ante error crítico. **No sustituye** la revisión humana de `AC-07`.

## Bloque 8 · `B08` Superficies y recorrido

**Resultado cubierto**: `JS-01`–`JS-08`, `FR-001`–`FR-010`, `FR-015`, `ST-001`–`ST-005`, `EX-002`.
**Dependencias**: T067–T082, T084–T091, T100–T109.
**Criterio de integración**: el recorrido completo es utilizable **sin JavaScript**.

- [ ] T111 [B08·FR-019] Implementar el layout base en `src/layouts/Base.astro` con `lang` correcto por idioma, metadatos localizados, canónica, `hreflang` y JSON-LD — el idioma activo es perceptible también para tecnologías de asistencia.
- [ ] T112 [B08·FR-001] Implementar la superficie Inicio con los siete actos en `src/pages/index.astro` y sus equivalentes localizados — una idea dominante por momento; **no se secuestra el scroll**.
- [ ] T113 [B08·JS-04] Implementar la comparación del Acto 2 como **interacción sin JavaScript** —revelación o alternancia mediante `details`/`summary` nativos—, con alternativa textual equivalente, en `src/components/comparacion/` — PRD §16 declara el Acto 2 como **interacción** y `P02` pide «comparar dos respuestas que llegan al mismo contenido con cargas distintas»: una comparación meramente estática no lo satisface. La información completa permanece disponible con movimiento reducido y por teclado.
- [ ] T114 [B08·FR-003] Implementar la superficie Manifiesto con índice, identificadores, anclas estables y el texto canónico íntegro leído de la fuente, en `src/pages/[...manifiesto].astro` — el texto se alcanza desde cualquier superficie.
- [ ] T115 [B08·FR-004] Implementar el explorador de principios en `src/pages/[...principios]/index.astro` conservando orden, identidad y fuente — los diez recorribles.
- [ ] T116 [B08·JS-03] Implementar la página de principio individual en `src/pages/[...principios]/[principio].astro` — abre directamente sin recorrer la narrativa.
- [ ] T117 [B08·FR-007] Implementar la superficie Aplicación en `src/pages/[...aplicacion].astro` traduciendo los conceptos antes del mecanismo — **no abre con rutas, archivos, YAML ni comandos** (`P03`).
- [ ] T118 [B08·FR-008] Implementar la superficie SpecKit en `src/pages/[...speckit].astro` con las cuatro capas, el estado real y **render condicional** por `EstadoPreset.estado` — con `no-publicado` muestra estado, arquitectura y disponibilidad futura, y **ningún enlace, botón o puntero sin destino**.
- [ ] T119 [B08·FR-012] Implementar la superficie Acerca de en `src/pages/[...acerca-de].astro` con procedencia, autoría `Person`, ambas licencias, gobernanza, la nota de origen en voz autoral y los dos canales de `CL-07` —`mailto:manifiestosoftwarehumano@gmail.com` e Issues de `https://github.com/dacunao/sitio-software-humano`— en los tres idiomas — el `mailto:` es texto plano **sin ofuscación por JavaScript**, que rompería `FR-015` y la accesibilidad.
- [ ] T120 [B08·ST-004] Implementar la página 404 útil y orientadora en `src/pages/404.astro`, con rutas de vuelta al recorrido y al texto canónico — orientadora en los tres idiomas.
- [ ] T121 [B08·ST-001..ST-005] Implementar los estados de vacío, carga, éxito, error y recuperación en las superficies — el contenido inicial no depende de animación ni de petición tardía.
- [ ] T122 [B08·EX-002] Implementar el comportamiento ante traducción ausente: informar la ausencia y ofrecer alternativa comprensible **sin mezclar idiomas** — la página publicada no mezcla idiomas.
- [ ] T123 [B08·FR-015] Verificar el recorrido completo con JavaScript deshabilitado en `tests/sin-js.test.ts` — texto, navegación primaria, URLs profundas y contenido canónico disponibles.
- [ ] T124 [B08·PRD §21.4] Verificar jerarquía equivalente en móvil, tablet y escritorio, con **diagramas reestructurados y no reducidos** hasta la ilegibilidad — sin exigir orientación horizontal ni gestos complejos.
- [ ] T125 [B08·PRD §21.4] Verificar que el orden de lectura semántico permanece correcto **sin CSS** — la página sin estilos se lee en orden.

## Bloque 9 · `B09` Islas justificadas

**Resultado cubierto**: `FR-013`, `FR-020`, `ST-003`, `AC-06`, `AC-14`.
**Dependencias**: T111–T125.
**Criterio de integración**: suprimir cualquier isla **no elimina información ni acceso** (`research.md` · `RQ-03`).

- [ ] T126 [B09·FR-020] Implementar la isla de preferencias de idioma y movimiento en `src/islands/Preferencias.tsx` — la elección se conserva **localmente**, es reversible, se puede restablecer y **no requiere cuenta**.
- [ ] T127 [B09·EX-001] Verificar el comportamiento sin JavaScript de T126: rutas sin prefijo en inglés y `prefers-reduced-motion` respetado por CSS — solo se pierde el recuerdo, que `FR-020` declara prescindible.
- [ ] T128 [B09·ST-003] Implementar la isla de copiar y compartir con atribución diferenciada en `src/islands/Compartir.tsx` — confirmación clara y **sin captura de datos**; la copia distingue cita canónica de explicación editorial.
- [ ] T129 [B09·EX-001] Verificar el comportamiento sin JavaScript de T128: texto seleccionable y URL estable y visible — el resultado de `JS-08` se alcanza igual.
- [ ] T130 [B09·FR-015] Verificar que la supresión de ambas islas no elimina información ni acceso en `tests/islas.test.ts` — el recorrido conserva su resultado.

## Bloque 10 · `B10` Descubrimiento y medición

**Resultado cubierto**: `FR-016`, `FR-018`, `AC-12`, `CL-08`, `BR-008`.
**Dependencias**: T067–T082, T111–T125.
**Criterio de integración**: ningún origen de red fuera de `softwarehumano.com` y del beacon autorizado.

- [ ] T131 [B10·FR-016] Implementar Open Graph y tarjetas sociales con textos **fieles al contenido visible**, `og:locale` y `og:locale:alternate`, en `src/layouts/Base.astro` — sin promesas ausentes de la página.
- [ ] T132 [P] [B10·CL-08] Configurar la verificación de Google Search Console por DNS o archivo — **sin script en el sitio**; provee impresiones, clics y consultas por idioma.
- [ ] T133 [P] [B10·SC-006] Establecer la línea base de CrUX y PageSpeed Insights para el origen — **sin script**; se documenta si el origen todavía no dispone de datos de campo (`R02`).
- [ ] T134 [B10·CL-08] Insertar **manualmente** el beacon de Cloudflare Web Analytics en `src/layouts/Base.astro` — el único script de terceros queda **visible y versionado** en el repositorio (`research.md` · `RQ-04`).
- [ ] T135 [B10·PRD §24.3] Declarar la política de seguridad de contenido en `public/_headers` con `script-src` admitiendo `https://static.cloudflareinsights.com`, `connect-src` admitiendo `https://cloudflareinsights.com`, y **`form-action 'none'`** — este último expresa la decisión de `CL-06` y `CL-07` de no tener formularios.
- [ ] T136 [B10·BR-008] Implementar el script `audit:network` que inventaría las peticiones del recorrido completo en `tools/audit/network.ts` — cualquier origen distinto de los dos autorizados es **fallo**, no observación.
- [ ] T137 [B10·AC-12] Verificar que el sitio se lee íntegramente **sin registro ni entrega de información personal** y que ningún contenido se bloquea por falta de consentimiento — evidencia registrada.

## Bloque 11 · `B11` Despliegue

**Resultado cubierto**: PRD §24.2, §24.3, `EX-003`, `CL-11`.
**Dependencias**: T009–T022, T131–T137.
**Criterio de integración**: una reversión restituye contenido **y** configuración.

- [ ] T138 [B11·PRD §24.3] Completar `public/_headers` con `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy` restrictivo y `Permissions-Policy` denegando lo no usado — encabezados versionados en el repositorio.
- [ ] T139 [B11·EX-003] Crear `public/_redirects` con las redirecciones necesarias y su regla de mantenimiento — versionado junto al contenido.
- [ ] T140 [B11·CL-11] Configurar el proyecto en Cloudflare Pages y el dominio `softwarehumano.com` con las tres raíces de idioma — el sitio responde en el origen canónico.
- [ ] T141 [B11·AC-08] Implementar el script `audit:perf` que mide los presupuestos de PRD §24.1 sobre el sitio desplegado, en `tools/audit/perf.ts` — reporta LCP, INP y CLS y declara si la fuente es campo o laboratorio representativo.
- [ ] T142 [B11·PRD §24.2] Probar una reversión de despliegue y comprobar que restituye contenido **y** encabezados y redirecciones juntos — evidencia registrada.
- [ ] T143 [B11·EX-003] Verificar que un cambio de estructura de URLs conserva redirecciones y contenido canónico versionado — sin enlaces rotos tras el cambio.
- [ ] T144 [B11·SC-007] Ejecutar `check:links` sobre el despliegue y confirmar ausencia de enlaces internos rotos antes de liberar — cero rotos.

## Bloque 12 · `B12` Evidencia y aceptación

**Resultado cubierto**: `AC-01`–`AC-16`, `SC-001`–`SC-008`, PRD §26.4, §32.
**Dependencias**: todos los bloques anteriores.
**Criterio de integración**: **ninguna auditoría automática sustituye la revisión humana** (`STOP07`, PRD §32).

- [ ] T145 [B12·AC-03] Verificación 1: revisión de contenido contra el núcleo, con comparación de integridad y lectura humana — registro de comparación.
- [ ] T146 [B12·AC-01,AC-02] Verificación 2: **pruebas moderadas de comprensión, humanas**, con representantes de las audiencias de PRD §14.1 — las personas explican el problema sin mencionar primero una funcionalidad del sitio.
- [ ] T147 [B12·AC-05] Verificación 3: **prueba de navegación sin explicación previa, humana** — observación registrada.
- [ ] T148 [B12·AC-07] Verificación 4: **revisión completa por teclado y lector de pantalla, humana**, más el barrido automatizado `audit:a11y` — registro por recorrido; la auditoría automática no lo sustituye.
- [ ] T149 [B12·AC-06] Verificación 5: prueba con movimiento reducido — misma información sin movimiento no esencial.
- [ ] T150 [B12·PRD §21.4] Verificación 6: **evaluación móvil y escritorio con contenido real, humana** — prohibido aprobar con contenido simulado.
- [ ] T151 [B12·AC-08] Verificación 7: auditoría de rendimiento contra los presupuestos de PRD §24.1 — LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1; se declara si la fuente es campo o laboratorio representativo.
- [ ] T152 [B12·AC-11,AC-15] Verificación 8: comprobación de enlaces, metadatos y datos estructurados — sin errores críticos y sin marcado de contenido inexistente.
- [ ] T153 [B12·AC-13] Verificación 9: **revisión lingüística humana aprobada** en los tres idiomas — registro de aprobación por idioma; sin él la versión 1.0 no puede aceptarse.
- [ ] T154 [B12·BR-002] Verificación 10: ausencia de voseo, `vosotros` y localismos nacionales, por comando **y** por revisión humana — `R03` deja constancia del límite.
- [ ] T155 [B12·AC-14] Verificación 11: prueba de cambio de idioma y correspondencia de URLs — la persona se mantiene en la entidad equivalente y una URL explícita no es sustituida.
- [ ] T156 [B12·AC-15] Verificación 12: validación del modelo de contenido y sus reglas de integridad con los casos negativos — la suite completa pasa.
- [ ] T157 [B12·PRD §32] Verificación 13: **revisión humana del recorrido completo** — dictamen de la autoridad de producto sobre comprensión, confianza, control y coherencia con los diez principios.

## Verificación del resultado completo

- [ ] T158 [VERIF·V01] Reconciliar cada fila del inventario de cobertura con la implementación — matriz sin vacíos ni tareas huérfanas.
- [ ] T159 [VERIF·V09] Verificar el recorrido completo incluidos estados vacíos, carga, error, extremos y recuperación — evidencia registrada.
- [ ] T160 [VERIF·SH-SCORE] Evaluar comprensión, esfuerzo, confianza, control, accesibilidad y rendimiento — hallazgos y evidencia; ninguna dimensión crítica puntúa 0.
- [ ] T161 [VERIF·AC-10] Registrar pendientes, supuestos, excepciones aprobadas y decisiones humanas requeridas, y **verificar que no se introdujeron prioridades, MVP ni exclusiones inventadas** — estado explícito.

## Dependencias y orden de ejecución

| Bloque | Depende de | Puede ejecutarse en paralelo con | Bloquea |
|---|---|---|---|
| `B00` T001–T008 | ninguna | — | todo |
| `B01` T009–T022 | `B00` | — | todo lo demás |
| `B02` T023–T050 | `B01` | — | `B03`, `B04` |
| `B03` T051–T066 | `B02` | — | `B04`, `B05`, `B06` |
| `B04` T067–T082 | `B02`, `B03` | `B05` | `B08`, `B10` |
| `B05` T083–T091 | `B03` | `B04` | `B06` (borradores), `B08` |
| `B06` T092–T099 | `B03`, borradores de `B05` | — | `B07`–`B12` |
| `B07` T100–T110 | `B06` | — | `B08` |
| `B08` T111–T125 | `B04`, `B05`, `B07` | — | `B09`, `B10` |
| `B09` T126–T130 | `B08` | `B10` | `B12` |
| `B10` T131–T137 | `B04`, `B08` | `B09` | `B11` |
| `B11` T138–T144 | `B01`, `B10` | — | `B12` |
| `B12` T145–T157 | todos | — | aceptación |

### Detenciones que el orden no puede resolver

- **T097** · elección de dirección visual. Requiere la autoridad de producto. Bloquea `B07`–`B12`.
- **T089, T090** · revisión profesional externa. Bloquea `AC-13` y, con él, la aceptación de la 1.0.
- **T091** · revisión humana de neutralidad del español.
- **T146, T147, T148, T150, T157** · verificaciones humanas que ninguna herramienta sustituye.

## Notas sobre esta derivación

**No se asignó prioridad, MVP, independencia ni entrega incremental.** El PRD no los autoriza; su §15 declara que el orden de las Job Stories no expresa prioridad, y `AC-10` exige verificar esa ausencia. En lugar del «alcance de MVP sugerido» del comando nativo, esta sección describe el orden técnico neutro: `B01`–`B03` construyen la base de contenido validado, `B04`–`B05` la topología y la paridad lingüística, `B06`–`B07` la identidad visual y sus componentes, `B08`–`B09` las superficies y sus dos islas, `B10`–`B11` descubrimiento y despliegue, `B12` la evidencia. **Ningún bloque completado reduce ni redefine el alcance comprometido.**

**No se usaron etiquetas de historia de usuario.** El fundamento usa Job Stories; `SH-AP` advierte contra imponer historias de usuario, y la plantilla del preset usa `[REF]` trazable en su lugar.

**Las pruebas no se omitieron por no haber sido pedidas con esa palabra.** `AC-07`, `AC-08`, `AC-15`, `AC-16` y `SC-007` exigen evidencia, y `BR-007` exige detención efectiva: por eso T042–T049 existen como casos negativos, sin los cuales una regla de validación no se considera implementada.
