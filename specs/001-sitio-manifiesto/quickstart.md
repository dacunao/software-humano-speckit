# Guía de validación y aceptación

**Plan**: [plan.md](./plan.md) · **Especificación**: [spec.md](./spec.md) · **Fecha**: 2026-09-21

Materializa `A07` de la constitución —«¿qué evidencia autoriza declarar completo el desarrollo?»— y las trece verificaciones que PRD §26.4 declara condición previa a aceptar la versión 1.0.

> **Los comandos de esta guía no existen todavía.** Son el contrato de scripts que `B01` y `B02` deben crear. Se documentan aquí para que las tareas tengan un destino verificable y no una intención.

> **Advertencia que gobierna todo el documento.** Código correcto, build exitoso y pruebas verdes **no bastan** (`V01`, `STOP07`, PRD §32). La mitad derecha de este documento —lo humano— no es un complemento de la izquierda: es la parte que decide la aceptación.

## Requisitos previos

```bash
bun --version          # debe coincidir con la versión fijada por el proyecto
```

La versión de bun se fija junto con las dependencias. Un archivo de bloqueo interpretado por dos versiones distintas del gestor no garantiza el mismo árbol, y PRD §24.5 exige reproducibilidad (ver `plan.md`, «Decisión de gestor de paquetes»).

```bash
bun install --frozen-lockfile
```

El modo congelado es lo que convierte «dependencias fijadas» en una afirmación con mecanismo.

## Verificación automatizada

Cada comando corresponde a reglas concretas del modelo de contenido. **Una regla sin caso negativo que demuestre la detención no se considera implementada** (`data-model.md`, «Reglas que detienen el build»).

| Comando | Qué comprueba | Reglas | Criterio |
|---|---|---|---|
| `bun run typecheck` | Tipado estricto de TypeScript | `VB-11` | Cero errores → `AC-16` |
| `bun run validate:content` | Identificadores, referencias, campos obligatorios, paridad de traducciones, anclas | `VB-01`–`VB-05` | Detención efectiva ante cada caso negativo |
| `bun run validate:lang` | Marcadores de voseo y de `vosotros` en contenido `es`; mezcla de idiomas | `VB-08`, `VB-09` | Cero coincidencias |
| `bun run validate:routes` | Reciprocidad `hreflang`, correspondencia con el mapa, canónicas | `VB-06` | Coherencia total → parte de `AC-14`, `AC-15` |
| `bun run validate:semantics` | JSON-LD describe solo contenido visible; estado del preset coherente | `VB-07`, `VB-10` | Sin marcado especulativo → `AC-15` |
| `bun run build` | Generación estática completa | todas | El build **falla** si cualquier regla se viola (`BR-007`) |
| `bun run check:links` | Enlaces internos | `VB-12` | Cero rotos → `SC-007` |
| `bun test` | Recorridos críticos y casos negativos de validación | `VB-01`–`VB-09` | Verde, con la suite de casos negativos completa |
| `bun run audit:a11y` | Barrido automatizado WCAG 2.2 AA | — | Sin errores críticos. **No sustituye** la revisión humana de `AC-07` |
| `bun run audit:perf` | Presupuestos de PRD §24.1 | — | LCP ≤ 2,5 s · INP ≤ 200 ms · CLS ≤ 0,1 |
| `bun run audit:network` | Inventario de peticiones del recorrido completo | — | Solo `softwarehumano.com` y el beacon autorizado → `AC-12`, `BR-008` |

## Las trece verificaciones de PRD §26.4

| # | Verificación | Cómo | Evidencia | Criterios |
|---|---|---|---|---|
| 1 | Revisión de contenido contra el núcleo | Comparación de integridad contra `SHA256SUMS` más lectura humana | Registro de comparación | `AC-03` |
| 2 | Pruebas moderadas de comprensión | **Humana**, con representantes de las audiencias de PRD §14.1 | Notas de sesión | `AC-01`, `AC-02`, `SC-001`, `SC-002` |
| 3 | Navegación sin explicación previa | **Humana** | Observación registrada | `AC-05`, `SC-003` |
| 4 | Revisión completa por teclado y lector de pantalla | **Humana** | Registro por recorrido | `AC-07` |
| 5 | Prueba con movimiento reducido | Automatizada más **humana** | Captura de ambos modos | `AC-06`, `FR-013` |
| 6 | Evaluación móvil y escritorio con contenido real | **Humana**, prohibido contenido simulado (PRD §21.1.8) | Registro por punto de quiebre | `AC-07`, PRD §21.4 |
| 7 | Auditoría de rendimiento | `bun run audit:perf` más campo | Informe | `AC-08`, `SC-006` |
| 8 | Enlaces, metadatos y datos estructurados | `check:links`, `validate:routes`, `validate:semantics` | Salida de comandos | `AC-11`, `AC-15` |
| 9 | Revisión lingüística humana en los tres idiomas | **Humana**: autoridad de producto para `es`; servicio profesional para `en` y `pt-BR` (`CL-09`) | **Registro de revisión aprobada por idioma** | `AC-13` |
| 10 | Ausencia de voseo, `vosotros` y localismos | `validate:lang` **más** revisión humana | Salida más registro | `AC-13`, `BR-002` |
| 11 | Cambio de idioma y correspondencia de URLs | `validate:routes` más prueba **humana** | Recorrido documentado | `AC-14`, `SC-004` |
| 12 | Validación del modelo YAML y sus reglas de integridad | `validate:content` con casos negativos | Salida | `AC-15` |
| 13 | Revisión humana del recorrido completo | **Humana** | Dictamen de la autoridad de producto | `AC-01`–`AC-16`, PRD §32 |

**Sobre el punto 9.** El criterio de terminado de una traducción no es que el texto exista, sino que exista registro de revisión aprobada. Sin él, `BR-003` y `ST-001` impiden publicar ese idioma y `AC-13` no puede declararse cumplido.

**Sobre el punto 10.** `validate:lang` atrapa marcadores mecánicos. No atrapa vocabulario ni giros nacionales, y el español queda sin segunda mirada humana por decisión registrada en `CL-09`. Ese límite está anotado como `R03` y fue aceptado por la autoridad de producto; no se presenta como cobertura completa.

## Detenciones que esta guía no puede levantar

- **Dirección visual** (`B06`, `R05`). Requiere aprobación de la autoridad de producto. Ningún agente puede aprobarla ni atribuirse esa revisión. Sin ella no se fijan tokens y `B07`–`B12` permanecen bloqueados.
- **Aprobación lingüística** (`CL-09`). Es humana y externa para dos de los tres idiomas.
- **Aceptación del producto** (PRD §32). Requiere que una revisión humana confirme comprensión, confianza, control y coherencia con los diez principios. Esta guía produce evidencia; no produce aceptación.

## Qué autoriza declarar terminada la versión 1.0

Todo lo de PRD §32, que este proyecto no reinterpreta: cobertura con evidencia o excepción aprobada; `JS-01`–`JS-09` cubiertas y trazables; contenido canónico comparado con el núcleo; paridad y revisión aprobada en los tres idiomas; validación del modelo y del JSON-LD; tipado estricto y pruebas sin errores; recorrido probado con personas; estados responsivos, accesibilidad, rendimiento, enlaces y metadatos verificados; presentación de SpecKit correspondiente al estado técnico real; ninguna capacidad no autorizada incorporada; `analyze` y `converge` sin brechas críticas; y revisión humana final.
