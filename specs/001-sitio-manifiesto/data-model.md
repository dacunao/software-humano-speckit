# Modelo de contenido

**Plan**: [plan.md](./plan.md) · **Especificación**: [spec.md](./spec.md) · **Fecha**: 2026-09-21

`spec.md` enumera las entidades. Este documento define los campos, las relaciones, las reglas que detienen el build y las transiciones de estado que `B02` debe implementar y `tasks.md` verificar. Es el detalle que `BR-007` necesita para ser comprobable en lugar de aspiracional.

**Regla transversal.** Todo identificador es **estable e independiente del idioma** (`BR-003`). El idioma es una dimensión de las entradas traducibles, nunca parte del identificador.

## Entidades

### `Principio`

| Campo | Tipo | Obligatorio | Regla |
|---|---|---|---|
| `id` | `P01`–`P10` | Sí | Único; exactamente diez; orden canónico inmutable |
| `nombre_canonico` | texto traducible | Sí | — |
| `frase_canonica` | texto traducible | Sí | No se parafrasea dentro de la superficie canónica (`BR-004`) |
| `tension` | texto traducible | Sí | Problema humano o de producto que observa |
| `significado` | texto traducible | Sí | Explicación editorial; no reemplaza el texto canónico |
| `consecuencia` | texto traducible | Sí | Qué debe cambiar al diseñar o implementar |
| `ejemplo` | texto traducible | Sí | Marcado como ejemplo, no como doctrina (`BR-004`) |
| `contraejemplo` | texto traducible | Sí | Señal de incumplimiento reconocible |
| `pruebas_de_decision` | lista de texto traducible | Sí, ≥1 | Utilizables en una revisión de producto (`FR-006`) |
| `capitulo` | enum | Sí | `proposito` \| `complejidad-atencion` \| `confianza-continuidad` \| `agencia`. Encuadre de presentación; no crea jerarquía nueva |
| `seccion_canonica_ref` | referencia | Sí | Apunta a una `SeccionCanonica` existente |
| `relaciones.job_stories` | lista de `JS-0n` | Sí, ≥1 | Cada valor debe existir |
| `relaciones.requisitos` | lista de `FR-0nn` | Sí, ≥1 | Cada valor debe existir |
| `estado_editorial` | enum | Sí | Ver `EstadoEditorial` |

Las ocho secciones del contrato de PRD §17 son: declaración (`nombre_canonico` + `frase_canonica`), `tension`, `significado`, `consecuencia`, `ejemplo`, `contraejemplo`, `pruebas_de_decision` y fuente (`seccion_canonica_ref`). **`FR-004` y `AC-04` se verifican contra la presencia de las ocho.**

### `SeccionCanonica`

| Campo | Tipo | Obligatorio | Regla |
|---|---|---|---|
| `id` | texto estable | Sí | Único; corresponde a un identificador del núcleo (`SH-INDEX`, `P01`–`P10`, `V01`–`V12`, `F01`–`F08`, `A01`–`A08`, `STOP01`–`STOP07`, `SH-POCKET`, `SH-AP`, `SH-GOV`) |
| `ancla` | texto | Sí | Debe existir en el documento fuente; el build lo comprueba |
| `fuente` | ruta | Sí | Para `es`: `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`, **leído, no copiado** (`RQ-01`) |
| `fuente_traduccion` | ruta por idioma | Sí para `en` y `pt-BR` | Archivo Markdown de traducción canónica |
| `version_nucleo` | texto | Sí | `2.1` |
| `es_traduccion` | booleano | Sí | Cuando es verdadero, debe declarar referencia al original en español (PRD §19.4) |

### `ExplicacionEditorial`

| Campo | Tipo | Obligatorio | Regla |
|---|---|---|---|
| `id` | texto estable | Sí | Único |
| `origen_ref` | referencia | Sí | Apunta a un `Principio` o a una `SeccionCanonica` existente (`BR-004`) |
| `cuerpo` | texto traducible | Sí | — |
| `estado_editorial` | enum | Sí | Nunca `canonico_aprobado` |
| `registro` | enum | Sí | `editorial` \| `voz_autoral`. `voz_autoral` solo en la nota de origen (`CL-04`) |

### `Superficie`

| Campo | Tipo | Obligatorio | Regla |
|---|---|---|---|
| `id` | enum | Sí | `inicio` \| `manifiesto` \| `principios` \| `aplicacion` \| `speckit` \| `acerca-de`. Las seis de PRD §18.1; ni una más ni una menos |
| `slug` | texto traducible | Sí | Localizado por idioma; alimenta el mapa de equivalencia (`RQ-02`) |
| `titulo`, `descripcion` | texto traducible | Sí | Específicos por superficie e idioma (PRD §25.2) |
| `tipo_schema` | enum | Sí | Ver el contrato de rutas y semántica |

### `Acto`

| Campo | Tipo | Obligatorio | Regla |
|---|---|---|---|
| `id` | `A1`–`A7` | Sí | Exactamente siete (PRD §16); orden fijo |
| `titulo`, `cuerpo` | texto traducible | Sí | — |
| `principios_ref` | lista de `P01`–`P10` | Solo `A4` | `A4` debe referenciar los diez, agrupados por `capitulo` |

### `EstadoPreset`

| Campo | Tipo | Obligatorio | Regla |
|---|---|---|---|
| `version` | texto | Sí | `1.0.1` |
| `validado_tecnicamente` | booleano | Sí | — |
| `limitaciones` | lista de texto traducible | Sí, ≥1 | `FR-009` |
| `estado` | enum | Sí | `no-publicado` \| `publicado` |
| `licencia` | texto | Sí | `MIT` (`CL-10`) |
| `repositorio` | URL o nulo | Condicional | `https://github.com/dacunao/spec-kit-preset-software-humano` |
| `download_url` | URL o nulo | Condicional | Solo existe con *release* |
| `sha256` | texto o nulo | Condicional | Solo existe con *release* |
| `catalogo_comunidad` | URL o nulo | Condicional | Entrada en el catálogo de SpecKit |

### `MetadatosPublicacion`

| Campo | Regla |
|---|---|
| `origen` | `https://softwarehumano.com` (`CL-01`) |
| `nombre_sitio` | «Software Humano», **valor único, no traducible** (`CL-01`) |
| `autor` | Persona: Damián Acuña → Schema.org `Person` (`CL-02`) |
| `licencia_contenido` | `CC BY 4.0` (`CL-05`) |
| `licencia_codigo` | `MIT` (`CL-12`) |
| `contacto` | `manifiestosoftwarehumano@gmail.com` e Issues de `https://github.com/dacunao/sitio-software-humano` (`CL-07`) |
| `version_nucleo`, `fecha_actualizacion` | `FR-012` |

## Enumeraciones de estado

### `EstadoEditorial` — `BR-005`

`canonico_aprobado` · `explicacion_aprobada` · `ejemplo_aprobado` · `borrador` · `estado_tecnico_verificado` · `propuesta_futura`

`BR-005` exige «al menos seis», de modo que el registro `voz_autoral` de `CL-04` se modela como atributo ortogonal y no como séptimo estado: una nota de origen puede ser borrador o aprobada igual que cualquier otra explicación.

### `EstadoTraduccion`

`ausente` → `borrador` → `en_revision` → `aprobada`

**Solo `aprobada` habilita publicar esa entrada en ese idioma** (`BR-003`, `ST-001`). El registro de aprobación identifica al responsable: la autoridad de producto para el español, el servicio profesional para inglés y portugués (`CL-09`).

### `EstadoPreset.estado`

`no-publicado` → `publicado`. La transición exige `repositorio`, `download_url` y `sha256` presentes, y es la que habilita emitir `SoftwareSourceCode` y mostrar instrucciones de instalación (`FR-010`, PRD §25.2).

## Reglas que detienen el build

`BR-007` y PRD §19.3 exigen detención, no advertencia. `B02` implementa cada regla **con un caso negativo que demuestra la detención**; una regla sin caso negativo no se considera implementada.

| ID | Regla | Origen |
|---|---|---|
| `VB-01` | Identificadores duplicados dentro de un tipo | PRD §19.3 |
| `VB-02` | Referencia rota: `seccion_canonica_ref`, `origen_ref`, `principios_ref`, `relaciones.*` | PRD §19.3 |
| `VB-03` | Campo obligatorio ausente, incluidas las ocho secciones de un `Principio` | PRD §19.3, `FR-004` |
| `VB-04` | Traducción requerida incompleta: un `id` publicable sin entrada `aprobada` en un idioma declarado disponible | PRD §19.3, `BR-003`, `ST-001` |
| `VB-05` | Ancla declarada que no existe en el documento fuente | `FR-003`, `RQ-01` |
| `VB-06` | Falta de reciprocidad `hreflang` o discrepancia con el mapa de equivalencia — implementada en `B04` | `FR-019`, `AC-15` |
| `VB-07` | `estado: publicado` sin `repositorio`, `download_url` o `sha256` | `FR-010`, `CL-06` |
| `VB-08` | Marcador de voseo o de `vosotros` en contenido `es` | PRD §26.4, `BR-002` |
| `VB-09` | Mezcla de idiomas en una entrada publicada, salvo nombre propio o cita identificada | PRD §21.7, `BR-003` |
| `VB-10` | JSON-LD que declara una entidad, relación, fecha, versión o URL ausente de la página visible — implementada en `B04` | `BR-009`, PRD §25.3 |
| `VB-11` | Error de tipado estricto de TypeScript — implementada en `B01` | PRD §24.6, `AC-16` |
| `VB-12` | Enlace interno roto — implementada en `B04` junto con la topología de rutas, no en `B02`, porque requiere las URLs generadas | PRD §24.2, `SC-007` |

**`VB-08` no sustituye la revisión humana.** PRD §26.4 la exige explícitamente y `CL-09` la asigna. Atrapa marcadores mecánicos; no atrapa vocabulario ni giros nacionales, y así queda registrado en `R03`.
