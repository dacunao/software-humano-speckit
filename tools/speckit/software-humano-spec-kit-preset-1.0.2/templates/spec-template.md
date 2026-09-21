# Especificación: [FEATURE NAME]

**Rama**: `[###-feature-name]`  
**Creada**: [DATE]  
**Estado**: Borrador  
**Entrada**: "$ARGUMENTS"

## Fuente y autoridad

<!--
Identifica la definición de producto que gobierna esta especificación. Puede ser
un PRD, una o varias Job Stories, épicas, capacidades, requisitos, reglas u otra
forma autorizada. No reformules la fuente para ajustarla a esta plantilla.
-->

- **Fuente autorizada**: [documento, ubicación o descripción recibida]
- **Autoridad para modificar alcance**: [persona o función]
- **Alcance declarado**: [qué debe quedar cubierto]
- **No objetivos explícitos**: [qué queda fuera, solo si la fuente lo establece]
- **Evidencia disponible**: [investigación, datos, observación o N/A]

## Progreso y resultado esperado

<!-- Describe el cambio que la persona o el proceso necesita conseguir. -->

- **Situación de partida**: [circunstancia observable]
- **Motivación o tensión**: [por qué necesita avanzar]
- **Resultado buscado**: [condición verificable]
- **Personas afectadas**: [solo los roles que cambien reglas, derechos o experiencia]

## Estructura de producto preservada

<!--
Representa los elementos obligatorios con la estructura y los identificadores de
la fuente. No impongas historias de usuario, prioridad, MVP o independencia. Si
la fuente contiene Job Stories, conserva circunstancia, motivación y resultado.
Repite la subsección siguiente por cada unidad coherente que exista en la fuente.
-->

### [SOURCE-ID] [Nombre del elemento]

- **Tipo en la fuente**: [Job Story, épica, capacidad, requisito, regla, recorrido u otro]
- **Definición**: [significado fiel a la fuente]
- **Dependencias**: [otros elementos necesarios o ninguna]
- **Reglas y límites**: [condiciones aplicables]
- **Resultado verificable**: [cómo se reconoce que quedó satisfecho]

#### Escenarios de aceptación

1. **Dado** [estado inicial], **cuando** [acción o evento], **entonces** [resultado].
2. **Dado** [estado alternativo], **cuando** [acción o evento], **entonces** [resultado].

## Cobertura del alcance

<!-- Todo elemento obligatorio de la fuente debe aparecer una vez como mínimo. -->

| ID de fuente | Elemento obligatorio | Destino en esta especificación | Evidencia de aceptación | Estado |
|---|---|---|---|---|
| [SOURCE-ID] | [resumen] | [sección / requisito / escenario] | [evidencia esperada] | Cubierto / Pendiente de aclaración |

## Contrato de experiencia

<!-- Define la experiencia como parte de la funcionalidad, no como decoración. -->

- **Lenguaje y modelo mental**: [términos que la persona reconoce]
- **Inicio simple**: [qué necesita ver o hacer primero]
- **Profundidad progresiva**: [qué se revela en contexto]
- **Feedback y estado**: [qué ocurrió, qué ocurre y qué sigue]
- **Control y recuperación**: [confirmación, reversibilidad y salida]
- **Continuidad**: [cómo se preserva el trabajo]
- **Accesibilidad y carga**: [condiciones relevantes]

## Requisitos

### Requisitos funcionales

- **FR-001**: El sistema DEBE [comportamiento verificable y trazable a SOURCE-ID].
- **FR-002**: El sistema DEBE [comportamiento verificable y trazable a SOURCE-ID].

### Reglas, estados y excepciones

- **BR-001**: [regla determinista, autorización o límite].
- **ST-001**: [estado vacío, carga, éxito, error, recuperación o extremo aplicable].
- **EX-001**: [excepción y comportamiento esperado].

### Entidades clave *(solo cuando existan datos de dominio)*

- **[Entidad]**: [significado, relaciones y restricciones sin diseño técnico].

## Evidencia y criterios de éxito

<!--
La evidencia debe ser proporcional al riesgo. Incluye calidad humana y técnica.
No limites las pruebas a lo pedido explícitamente si son necesarias para demostrar
un criterio de aceptación.
-->

- **SC-001**: [resultado humano o de producto medible].
- **SC-002**: [calidad de experiencia: comprensión, esfuerzo, confianza o control].
- **SC-003**: [comportamiento técnico, seguridad, rendimiento o continuidad aplicable].

## Supuestos permitidos

<!-- Solo decisiones menores, reversibles, explícitas y dentro de la autoridad. -->

- **AS-001**: [supuesto] — **Reversible porque**: [razón] — **Impacto**: [menor].

## Decisiones materiales pendientes

<!--
No completes mediante convenciones genéricas una decisión que pueda cambiar
alcance, reglas, derechos, seguridad o experiencia. Conserva cada marcador hasta
que la autoridad correspondiente lo resuelva.
-->

- **[NEEDS CLARIFICATION: pregunta concreta, autoridad requerida e impacto]**
