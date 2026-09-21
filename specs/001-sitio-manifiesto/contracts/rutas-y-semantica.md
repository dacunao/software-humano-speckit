# Contrato de rutas y semántica

**Plan**: [../plan.md](../plan.md) · **Modelo**: [../data-model.md](../data-model.md) · **Fecha**: 2026-09-21

Este es el contrato que verifican `AC-11`, `AC-13`, `AC-14` y `AC-15`. Define la topología de URLs, la correspondencia entre idiomas y el mapeo semántico. Todo lo que aquí se declara **se genera desde la misma fuente que produce el contenido visible** (PRD §25.3); nada se escribe a mano en una plantilla.

## Topología de URLs

| Idioma | Código BCP 47 | Prefijo | Raíz |
|---|---|---|---|
| Inglés general | `en` | **ninguno** | `https://softwarehumano.com/` |
| Español neutro latinoamericano | `es` | `/es/` | `https://softwarehumano.com/es/` |
| Portugués de Brasil | `pt-BR` | `/pt-br/` | `https://softwarehumano.com/pt-br/` |

El prefijo de ruta es `pt-br` en minúsculas; el código declarado en `lang`, en `hreflang` y en `inLanguage` es **`pt-BR`** (`FR-019`).

Las seis superficies obligatorias tienen la **misma topología** en los tres idiomas y **slug localizado** en cada uno. Los valores de slug son contenido traducible y viven en YAML; este contrato fija la forma, no las palabras.

```
/                      /es/                      /pt-br/                    → inicio
/<slug>/               /es/<slug>/               /pt-br/<slug>/             → manifiesto, principios,
                                                                              aplicacion, speckit, acerca-de
/<slug-principios>/<slug-principio>/   …                                    → principio individual (P01–P10)
/<slug-manifiesto>/#<ancla>            …                                    → sección canónica
```

**Reglas invariantes.**

1. Una URL localizada explícita **siempre** prevalece sobre cualquier preferencia almacenada y sobre la detección del navegador (`FR-019`, `FR-020`, `AC-14`).
2. En la primera visita, una ruta sin prefijo se sirve en inglés **sin redirección automática** por idioma del navegador (`FR-020`, `AC-14`).
3. Toda URL profunda restituye la sección correcta al regresar (`FR-014`, `ST-005`).
4. Si cambia la estructura de URLs deben existir redirecciones, declaradas en `public/_redirects` (`EX-003`, PRD §24.2).

## Mapa de equivalencia

Generado en build desde el `id` estable que comparten las entradas traducibles (`BR-003`). Es la **fuente única** de tres salidas, de modo que no pueden divergir entre sí:

1. los enlaces del conmutador de idioma —que son `<a>` generados, no sustitución de texto en cliente (PRD §24.6);
2. las relaciones `hreflang` recíprocas;
3. la URL canónica de cada página.

```
id estable ──┬── (en) URL sin prefijo
             ├── (es) URL bajo /es/
             └── (pt-BR) URL bajo /pt-br/
```

**Ausencia de traducción aprobada.** Si un `id` no tiene entrada `aprobada` en un idioma, **no existe** en el mapa para ese idioma. El conmutador no adivina: informa la ausencia y ofrece una alternativa comprensible, sin mezclar idiomas en la página publicada (`EX-002`, `BR-003`). `VB-04` detiene el build si una superficie se declara disponible en un idioma sin contenido aprobado.

## Encabezados de enlace y metadatos por página

| Elemento | Regla |
|---|---|
| `lang` | Código BCP 47 del idioma de la página; perceptible también para tecnologías de asistencia (PRD §21.7) |
| `<link rel="canonical">` | URL absoluta de **esta** página en **este** idioma |
| `<link rel="alternate" hreflang>` | Una por idioma con traducción aprobada, **recíproca**; `VB-06` detiene el build ante falta de reciprocidad |
| `hreflang="x-default"` | Apunta a la URL sin prefijo, coherente con que el inglés sea la versión predeterminada y con la ausencia de redirección automática. Decisión técnica reversible conforme a PRD §2.3 |
| `<title>`, `<meta name="description">` | Específicos por superficie **y** por idioma (PRD §25.2) |
| Open Graph y tarjetas sociales | Textos fieles al contenido visible; `og:locale` con el código del idioma y `og:locale:alternate` con los demás |
| Sitemap | Incluye las tres versiones con sus relaciones; `robots` configurado de forma explícita |

## Mapeo semántico

Se emite el **tipo más específico que sea correcto**, no el que prometa mejor apariencia en resultados, y se prefieren menos propiedades completas y verdaderas sobre marcado extenso o especulativo (PRD §25.2). `VB-10` detiene el build ante marcado que describa algo ausente de la página visible (`BR-009`).

| Superficie o entidad | Tipo | Condición y propiedades mínimas |
|---|---|---|
| Sitio completo | `WebSite` | `name` «Software Humano» —valor único, no traducible—, `url` `https://softwarehumano.com`, `inLanguage`, `author` |
| Autoría | `Person` | Damián Acuña (`CL-02`). **No `Organization`**: no existe entidad que declarar (`BR-009`) |
| Superficie | `WebPage` | Subtipo más específico solo si describe realmente la página visible |
| Manifiesto canónico | `CreativeWork` | `version` `2.1`, `inLanguage`, `author`, `datePublished`, `license` → `https://creativecommons.org/licenses/by/4.0/` (`CL-05`) |
| Relación entre versiones canónicas | `translationOfWork` / `workTranslation` | Expresan relaciones **reales** entre la obra original en español y sus traducciones (PRD §25.3, §19.4) |
| Colección de principios | `DefinedTermSet` | Los diez deben ser entidades visibles y enlazables |
| Principio individual | `DefinedTerm` | Conserva `P01`–`P10` como identificador, `name`, `description` y pertenencia al conjunto |
| Jerarquía de navegación | `BreadcrumbList` | **Solo** en páginas cuya navegación visible muestre esa jerarquía |
| Preset | `SoftwareSourceCode` | **Solo** cuando `EstadoPreset.estado` sea `publicado` y existan URL verificable y contenido visible equivalente. Con `no-publicado` **no se emite** (`FR-010`, `VB-07`) |

## Encabezados HTTP

Declarados en `public/_headers`, versionados y restituidos junto al contenido al revertir un despliegue (`CL-11`).

| Encabezado | Valor y razón |
|---|---|
| `Content-Security-Policy` | Según `research.md` · `RQ-04`. Incluye `form-action 'none'`, que aquí expresa una decisión de producto: `CL-06` y `CL-07` establecieron que el sitio no tiene formularios |
| `Strict-Transport-Security` | Transporte seguro obligatorio |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | Restrictivo; ninguna medición autorizada lo necesita más amplio |
| `Permissions-Policy` | Deniega lo que el sitio no usa |

**Origen único permitido.** `softwarehumano.com` y el beacon autorizado de `CL-08`. Cualquier otro origen observado en el inventario de red de `B12` es un fallo de `BR-008`, no una observación.
