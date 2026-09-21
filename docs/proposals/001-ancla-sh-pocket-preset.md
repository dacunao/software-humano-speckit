# Propuesta 001 — Ancla `sh-pocket` huérfana en la plantilla de constitución del preset

**Fecha de registro:** 2026-09-21
**Estado:** propuesta abierta, sin autorización para aplicar
**Archivo afectado:** `tools/speckit/software-humano-spec-kit-preset-1.0.0/templates/constitution-template.md`
**Autoridad requerida:** autoridad del preset

## Hecho observado

En la plantilla de constitución del preset, el ancla `<a id="sh-pocket"></a>` está separada de la sección que debería identificar.

| Elemento | Línea en la plantilla del preset |
|---|---:|
| `## GUÍA DE BOLSILLO · SH-POCKET` | 889 |
| `<a id="sh-pocket"></a>` | 1034 |

El ancla quedó al final del documento, inmediatamente antes del pie de versión, a 145 líneas de su sección. Las demás anclas del núcleo (`sh-fund`, `sh-stop`, `sh-score`, `sh-ap`, `sh-gov`, `sh-done`) preceden correctamente a su sección.

El defecto se propaga a `.specify/memory/constitution.md`, que es una copia byte a byte de la plantilla: sección en línea 941, ancla en 1086.

## Impacto

Un enlace a `#sh-pocket` lleva al final del documento en lugar de a la Guía de bolsillo. Es un defecto de navegación.

No tiene efecto doctrinal: el texto de `SH-POCKET` está íntegro y en su lugar, y ninguna obligación del núcleo cambia. No bloquea especificación, planificación ni implementación.

## Por qué no se corrigió

`AGENTS.md` declara protegido el directorio `tools/speckit/software-humano-spec-kit-preset-1.0.0/` y exige instrucción humana explícita para modificarlo. También establece: "Si una implementación revela una mejora posible, regístrala como propuesta separada. No la incorpores retroactivamente a las fuentes."

Además, modificar la plantilla rompería la verificación de `SHA256SUMS`, que hoy valida 25 de 25 archivos y es la evidencia de integridad del paquete.

## Corrección propuesta

Mover `<a id="sh-pocket"></a>` de la línea 1034 a la línea inmediatamente anterior a `## GUÍA DE BOLSILLO · SH-POCKET`, replicando la convención de las demás anclas.

Al ser un cambio en el preset, requiere además:

1. decisión de la autoridad del preset;
2. incremento de versión del preset y entrada en su `CHANGELOG.md`;
3. regeneración de `SHA256SUMS`;
4. rematerialización de `.specify/memory/constitution.md` mediante `speckit.constitution`.

## Alternativa más simple

No corregir. El defecto no afecta doctrina ni alcance, y el costo de mover una versión del preset supera hoy el beneficio de un ancla de navegación. Esta alternativa es razonable si no hay otra razón para versionar el preset; si aparece una, conviene incluir esta corrección en ese mismo cambio.
