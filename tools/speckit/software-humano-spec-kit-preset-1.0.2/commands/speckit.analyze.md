---
description: Analiza doctrina, cobertura y trazabilidad sin modificar los artefactos examinados.
strategy: wrap
---

## Directiva vinculante de Software Humano

Además de los controles nativos, el análisis debe comprobar:

- correspondencia entre la fuente autorizada y todos los elementos de `spec.md`;
- preservación de Job Stories existentes y ausencia de Job Stories impuestas;
- requisitos sin tareas y tareas sin fundamento;
- prioridades, MVP, exclusiones, releases o independencia no autorizados;
- dependencias e integración representadas sin pérdida de alcance;
- experiencia, estados, recuperación, accesibilidad, rendimiento y control aplicables;
- evidencia necesaria para cada criterio de aceptación;
- cumplimiento de las razones de detención `STOP01`–`STOP07`.

Una contradicción con la constitución es crítica. La corrección debe volver al artefacto que posee la decisión; `analyze` no modifica archivos ni reinterpreta el núcleo para acomodar los valores predeterminados de SpecKit.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

El reporte final debe separar hechos, inferencias y decisiones humanas; identificar la fuente de cada hallazgo; y distinguir una brecha de producto, una brecha técnica y una falta de evidencia. No uses un puntaje o checklist como aceptación automática.
