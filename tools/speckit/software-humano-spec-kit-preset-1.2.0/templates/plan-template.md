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

<!--
Esta tabla es la traducción de la doctrina a restricciones concretas de ESTE proyecto.
`implement` debe consultarla antes de resolver una alternativa de diseño: una decisión
que esta tabla ya adjudica no se reabre ni se traslada a la persona como pendiente.

Incluye como mínimo las disposiciones que el anexo asigna a `plan`: P03, P04, P06-P10,
D03, D04, F03, F06, F07, A05-A08, CR03-CR06. Agrega cualquier otra que el riesgo del
proyecto justifique.

Una fila sin consecuencia concreta no cuenta como cumplida: "se respetará P07" no es
una consecuencia, "todo estado destructivo confirma y ofrece deshacer" sí lo es.
-->

| Disposición | Consecuencia concreta para este proyecto | Evidencia o decisión | Estado |
|---|---|---|---|
| [ID del núcleo] | [qué queda prohibido o exigido, en términos verificables] | [cómo se satisface] | Cumple / Bloqueado |

### Puntuación de entrada · `SH-SCORE`

*Antes de comprometer la estrategia. Una dimensión crítica en 0 significa que no está lista para proponerse.*

| Dimensión | 0 / 1 / 2 | Evidencia que sostiene el puntaje |
|---|---|---|
| Progreso del usuario | | |
| Carga cognitiva | | |
| [resto de las dimensiones aplicables] | | |

Un **1** que se repite por la misma razón —«argumentado y no observado»— indica que la propuesta descansa en razonamiento y no en evidencia.

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
