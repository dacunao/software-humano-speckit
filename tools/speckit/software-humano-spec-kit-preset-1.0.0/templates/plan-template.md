# Plan de implementación: [FEATURE]

**Rama**: `[###-feature-name]` | **Fecha**: [DATE] | **Especificación**: [link]

**Entrada**: `/specs/[###-feature-name]/spec.md`

## Resumen

[Resultado de producto que debe quedar cubierto y estrategia técnica recomendada.]

## Fuentes y autoridad

- **Fundamento de producto**: [referencia preservada desde spec.md]
- **Especificación operativa**: [ruta]
- **Autoridad de alcance**: [persona o función]
- **Versión de constitución**: [versión cargada]

## Comprobación de constitución

*PUERTA: debe cumplirse antes de diseñar y revisarse después de resolver la estrategia.*

| Disposición | Consecuencia para el plan | Evidencia o decisión | Estado |
|---|---|---|---|
| [ID del núcleo] | [regla aplicable] | [cómo se satisface] | Cumple / Bloqueado |

## Contexto técnico

<!-- Mantén solo los campos aplicables. Una decisión material desconocida no se infiere. -->

- **Lenguaje y versión**: [valor o NEEDS CLARIFICATION]
- **Dependencias principales**: [valor o N/A]
- **Persistencia**: [valor o N/A]
- **Plataforma objetivo**: [valor]
- **Estrategia de pruebas y evidencia**: [valor]
- **Rendimiento y escala**: [criterios aplicables]
- **Seguridad, privacidad y permisos**: [criterios aplicables]
- **Restricciones**: [valor]

## Estrategia técnica

### Enfoque recomendado

[Cómo se implementará el alcance completo y por qué este enfoque es proporcional.]

### Alternativa más simple considerada

[Alternativa y razón concreta para adoptarla o descartarla.]

### Opción de no construir

[Qué ocurriría y por qué no satisface —o sí satisface— el fundamento.]

## Cobertura y trazabilidad

| ID de fuente / requisito | Componente o decisión técnica | Dependencias | Evidencia prevista | Estado |
|---|---|---|---|---|
| [SOURCE-ID / FR-ID] | [destino] | [IDs] | [prueba o revisión] | Planificado / Bloqueado |

## Dependencias, bloqueantes y orden de ejecución

<!-- El orden técnico no modifica alcance ni presupone releases incrementales. -->

| Bloque | Entrega técnica | Depende de | Desbloquea | Criterio para avanzar |
|---|---|---|---|---|
| B01 | [trabajo coherente] | [ninguno / IDs] | [IDs] | [evidencia] |

## Integración y recorrido completo

- **Puntos de integración**: [componentes, datos o servicios]
- **Recorrido de extremo a extremo**: [cómo se produce el resultado completo]
- **Estados y recuperación**: [vacío, carga, error, extremos y retorno]
- **Riesgos de integración**: [riesgo y mitigación]

## Estructura del proyecto

```text
[árbol real y mínimo de archivos o módulos]
```

**Decisión de estructura**: [por qué esta estructura resuelve el problema sin capas innecesarias]

## Documentos auxiliares

<!--
No generes documentos por rutina. Materializa cada archivo únicamente cuando
responda una pregunta necesaria que no quede bien resuelta en spec.md o plan.md.
-->

| Documento nativo | ¿Se requiere? | Pregunta que responde | Justificación |
|---|---|---|---|
| `research.md` | Sí / No | [incertidumbre técnica] | [razón] |
| `data-model.md` | Sí / No | [modelo de dominio] | [razón] |
| `contracts/` | Sí / No | [interfaz o contrato] | [razón] |
| `quickstart.md` | Sí / No | [validación integrada] | [razón] |

## Riesgos y decisiones pendientes

| ID | Riesgo o decisión | Impacto | Autoridad | Tratamiento / condición de detención |
|---|---|---|---|---|
| R01 | [descripción] | [impacto] | [responsable] | [acción] |

## Complejidad excepcional

> Completa esta sección solo cuando el plan introduce una complejidad que requiere justificación.

| Complejidad | Necesidad concreta | Alternativa más simple rechazada porque |
|---|---|---|
| [elemento] | [problema real] | [evidencia] |
