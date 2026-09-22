---
description: Instala o verifica el núcleo aprobado sin reinterpretarlo ni convertir reglas de proyecto en doctrina.
strategy: wrap
---

## Directiva vinculante de Software Humano

Este comando conserva el mecanismo nativo de constitución, pero su autoridad queda limitada por estas reglas:

1. La plantilla resuelta contiene la proyección completa del núcleo v2.1 y es la única fuente autorizada para su contenido.
2. Un prompt circunstancial no puede resumir, mejorar, contextualizar ni enmendar la doctrina.
3. Una modificación doctrinal exige una nueva versión del núcleo previamente aprobada por autoridad humana.
4. Las reglas particulares de un producto pertenecen a su definición de producto, `spec.md` o `plan.md`; no se incorporan al núcleo.
5. Si la constitución existente contiene una versión distinta o cambios humanos no reconciliados, informa la diferencia y detente antes de sobrescribirla.
6. Conserva resolución de plantilla, validaciones, hooks, handoffs, reporte de impacto y escritura en la ubicación nativa.

## Alcance semántico de esta operación

El anexo asigna a `constitution` el **núcleo completo** y el índice `SH-INDEX`.

- **Núcleo completo** — esta operación no enfoca un subconjunto: instala o verifica la totalidad del texto aprobado. Cualquier omisión es una constitución inválida, no una versión resumida.
- **`SH-INDEX`** — la constitución instalada debe conservar los identificadores que permiten a las demás operaciones citar disposiciones exactas. Una proyección sin ellos rompe el resto del método.

Declara en tu informe si las quince familias del núcleo están presentes y si algún marcador quedó sin resolver.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

Al ejecutar el comando nativo anterior, trata las seis reglas iniciales como límites vinculantes. El resultado debe indicar la versión instalada, la fuente aprobada, cualquier diferencia detectada y toda decisión humana pendiente. No declares aprobada una enmienda por haber sido generada por el agente.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
