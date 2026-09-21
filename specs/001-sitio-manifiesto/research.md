# Investigación técnica

**Plan**: [plan.md](./plan.md) · **Especificación**: [spec.md](./spec.md) · **Fecha**: 2026-09-21

Este documento existe porque cuatro incertidumbres técnicas cambian el plan y ninguna se resuelve en `spec.md`. **No resuelve decisiones de producto.** `RQ-01` tocaba la letra de un requisito y la viabilidad de un flujo del que depende un criterio de aceptación: se elevó a la autoridad de producto y se registra aquí su decisión, no una inferencia del agente.

---

## `RQ-01` · Dónde vive el texto canónico del manifiesto

**Pregunta.** `FR-021` exige que el contenido «origine en YAML versionado». El núcleo v2.1 son ~82 KB de prosa continua en tres idiomas. ¿Dónde se almacena?

**Decisión** — tomada por la autoridad de producto el 2026-09-21, no por el agente.

El texto canónico en español **no se copia**. El build lo lee de su fuente protegida, `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`. El YAML conserva identificadores, anclas, metadatos, estados editoriales y la referencia a esa fuente. Las traducciones canónicas a inglés general y portugués de Brasil son artefactos nuevos, en Markdown, referenciados desde YAML.

**Fundamento.**

1. **Elimina una duplicación de texto rector.** `AGENTS.md` establece que dos copias de instrucciones rectoras divergen. Copiar el núcleo a YAML crearía esa segunda copia.
2. **Convierte `AC-03` en una comprobación y no en una comparación.** `AC-03` exige que los principios, sus identificadores y el texto canónico «coincidan con el núcleo v2.1». Con una sola fuente, coinciden por construcción y la evidencia es la verificación de integridad contra `SHA256SUMS` que ya existe. Con dos copias, `AC-03` sería una comparación textual que puede divergir entre versiones.
3. **Hace viable la revisión externa.** `CL-09` encarga la revisión de inglés y portugués a un servicio profesional, y `AC-13` la convierte en criterio de aceptación. Un corrector profesional puede trabajar sobre Markdown; sobre prosa indentada dentro de YAML, la fricción es real y recae sobre un proveedor externo.

**Relación con la letra de `FR-021`.** La decisión se aparta de «el contenido debe originarse en YAML» y sirve a su propósito declarado: saber qué cambió, quién lo aprobó, qué idiomas afecta y qué páginas y datos estructurados genera. Todo eso se conserva: el YAML sigue siendo el índice, el esquema valida la referencia y la correspondencia de anclas, y el build se detiene si la fuente referenciada no existe o su estructura de anclas no corresponde. **La autoridad de producto aprobó ese apartamiento de forma explícita**; el agente no lo asumió.

**Consecuencia registrada.** El build del sitio pasa a depender de un archivo gobernado por el paquete de método. Una nueva versión del núcleo se vuelve un evento visible y controlado, que es lo que PRD §27.2 pide, y acopla dos cosas hasta ahora sueltas. `AS-005` supone que el texto canónico no cambia durante este ciclo.

**Alternativas consideradas.**

- *Prosa en escalares de bloque YAML.* Cumple la letra sin discusión. Descartada por duplicación del texto rector, exposición de `AC-03` a divergencia y fricción sobre el revisor externo. Se descarta la razón que inicialmente se le atribuyó —diffs ilegibles—: un escalar de bloque se difiere línea por línea igual que cualquier texto, y sostener lo contrario habría sido un argumento falso.
- *Toda la prosa en Markdown referenciado, incluido el español copiado.* Resuelve la fricción del revisor pero mantiene la duplicación y el riesgo sobre `AC-03`.

---

## `RQ-02` · Cómo se representa la equivalencia entre URLs localizadas

**Pregunta.** `AC-14` exige que al cambiar de idioma la persona «se mantenga en la entidad equivalente». `FR-019` exige `hreflang` recíprocos y «correspondencia con la misma entidad conceptual». PRD §25.2 exige «URLs localizadas». ¿Cómo se representa esa correspondencia?

**Decisión.** Segmentos de ruta localizados por idioma, con un **mapa de equivalencia generado en build a partir del `id` estable** que `BR-003` obliga a compartir entre idiomas. Ese mapa es la única fuente de tres cosas: los enlaces del conmutador de idioma, las relaciones `hreflang` recíprocas y las URLs canónicas.

**Fundamento.** El `id` independiente del idioma ya existe por `BR-003`; el mapa solo lo materializa. Que conmutación, reciprocidad y canónicas salgan del mismo dato significa que **no pueden divergir entre sí**, que es precisamente el fallo que `AC-15` verifica y que PRD §25.3 pide comprobar. Si una entidad carece de traducción aprobada, no tiene entrada en el mapa para ese idioma, y esa ausencia —no una conjetura del conmutador— es lo que activa `EX-002`.

**Alternativas consideradas.**

- *Rutas idénticas salvo el prefijo de idioma.* Trivial de conmutar, pero contradice «URLs localizadas» de PRD §25.2 y desaprovecha el descubrimiento por idioma que PRD §26.3 quiere medir.
- *Híbrido con secciones localizadas e identificador crudo como slug.* Una vez que existe el mapa, no aporta nada y publica identificadores internos en la URL, lo que `P03` desaconseja.

---

## `RQ-03` · Qué interacciones exigen realmente una isla

**Pregunta.** PRD §24.6 reserva las islas para «interacciones que realmente lo requieran» y PRD §24.1 exige que «el JavaScript se justifique por interacción necesaria». ¿Cuáles sobreviven al criterio?

**Decisión.** **Dos islas, no tres.** El examen descartó la candidata que el plan había supuesto.

| Candidata | Veredicto | Razón |
|---|---|---|
| Preferencia de idioma y de movimiento | **Isla** | `FR-020` exige conservar la elección localmente. Eso requiere estado persistente en el navegador. Sin JavaScript: las rutas sin prefijo sirven inglés y `prefers-reduced-motion` se respeta por CSS; solo se pierde el recuerdo, que `FR-020` declara prescindible |
| Copiar y compartir con atribución diferenciada | **Isla** | `ST-003` exige confirmación clara al copiar o compartir, y `FR-011` que la copia distinga cita canónica de explicación editorial. Sin JavaScript: el texto es seleccionable y la URL permanece estable y visible |
| **Conmutador de idioma** | **No** | PRD §24.6 es literal: «El cambio de idioma será una navegación entre URLs equivalentes, no una sustitución de texto en cliente». Son enlaces generados en build desde el mapa de `RQ-02` |
| **Comparación del Acto 2** | **No** | `JS-04` pide comparar dos respuestas y PRD §16 la declara **interacción**, de modo que sigue siéndolo: lo que no necesita es JavaScript. Un `details`/`summary` nativo es interacción, cumple la alternativa textual de PRD §21.3 y funciona con movimiento reducido (`FR-013`) |
| Acordeones y capas progresivas | **No** | `details`/`summary` nativos conservan títulos explícitos y estados accesibles, como pide PRD §21.3 |

**Consecuencia sobre el plan.** `B09` se reduce a dos islas y la comparación del Acto 2 pasa a `B08` **como interacción resuelta con elementos nativos**, no como contenido estático: PRD §16 declara el Acto 2 como interacción y `P02` pide comparar dos respuestas con cargas distintas, de modo que descartar la isla no autoriza a descartar la interacción. Si `B06` demuestra que una transición **explica una relación** —el único uso de movimiento que PRD §21.2 autoriza—, la isla se justifica entonces con esa evidencia. No antes: eso sería el antipatrón «el agente agrega por si acaso».

---

## `RQ-04` · Cómo se expresa la política de seguridad admitiendo el único beacon autorizado

**Pregunta.** PRD §24.3 exige «encabezados de seguridad adecuados». `CL-08` autoriza Cloudflare Web Analytics como único script de terceros, y `BR-008` prohíbe que un tercero degrade privacidad, rendimiento o accesibilidad sin decisión aprobada. ¿Cómo se declara la política sin abrir la superficie?

**Hechos verificados el 2026-09-21** contra la documentación de Cloudflare: el beacon se carga desde `https://static.cloudflareinsights.com/beacon.min.js`. Con inyección automática de la plataforma, los datos viajan al mismo dominio y basta `connect-src 'self'`, y Cloudflare añade un atributo de integridad. Con inserción manual, el script se conecta a `cloudflareinsights.com` y hay que permitirlo en `connect-src`.

**Decisión.** **Inserción manual**, con la política expresada en `public/_headers`, versionada.

**Fundamento.** `BR-008` exige que la incorporación de un script de terceros sea una **decisión aprobada**, y `CL-12` publica el repositorio bajo MIT precisamente para que el piloto pueda estudiarse. Un script inyectado por la plataforma no aparece en el código fuente: sería la única pieza de la experiencia pública invisible en el repositorio. Se acepta a cambio un `connect-src` un punto más amplio.

**Forma de la política.** `default-src 'self'`; `script-src 'self' https://static.cloudflareinsights.com`; `connect-src 'self' https://cloudflareinsights.com`; `style-src 'self'`; `img-src 'self' data:`; `object-src 'none'`; `base-uri 'self'`; `frame-ancestors 'none'`; y **`form-action 'none'`**, que aquí no es una precaución genérica sino la expresión exacta de una decisión de producto: `CL-06` y `CL-07` establecieron que el sitio no tiene formularios. Se acompaña de `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy` restrictivo y `Permissions-Policy` denegando lo que el sitio no usa.

**Verificación.** `B12` levanta un inventario de peticiones de red del recorrido completo. Cualquier origen distinto de `softwarehumano.com` y del beacon autorizado es un fallo de `BR-008`, no una observación.

**Alternativa considerada.** *Inyección automática de la plataforma.* Da una política más estrecha y añade integridad sin trabajo propio. Descartada por invisibilidad en el repositorio, que contradice el propósito de `JS-07` y de `CL-12`. Es una decisión técnica reversible conforme a PRD §2.3.

---

## Fuentes consultadas

- Documentación de Cloudflare Web Analytics: [datos y recolección](https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/), [preguntas frecuentes](https://developers.cloudflare.com/web-analytics/faq/), [políticas de seguridad de contenido](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/)
- Documentación de SpecKit: [presets](https://github.github.io/spec-kit/reference/presets.html), [publicación de presets de comunidad](https://github.com/github/spec-kit/blob/main/presets/PUBLISHING.md)
