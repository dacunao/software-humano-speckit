---
description: "Tareas trazables para implementar el alcance completo"
---

# Tareas: [FEATURE NAME]

**Entrada obligatoria**: `spec.md`, `plan.md`  
**Entradas condicionales**: documentos auxiliares que `plan.md` haya declarado necesarios

## Formato

`- [ ] T001 [P?] [REF] Acción concreta en ruta/archivo — Evidencia esperada`

- **[P]**: puede ejecutarse en paralelo porque no comparte archivos ni depende de trabajo incompleto.
- **[REF]**: identificador trazable de fuente, requisito, regla o bloque técnico.
- Cada tarea incluye una acción, un destino concreto, sus dependencias y la evidencia para cerrarla.
- Una fase organiza la ejecución; no selecciona ni reduce alcance.

## Inventario de cobertura

<!-- Ningún elemento obligatorio puede quedar sin destino o excluirse por prioridad implícita. -->

| Referencia | Tareas que la implementan | Tareas que la verifican | Dependencias | Estado |
|---|---|---|---|---|
| [SOURCE-ID / FR-ID] | [TIDs] | [TIDs] | [TIDs] | Cubierto / Bloqueado |

## Bloque 1: Preparación necesaria

**Propósito**: [preparación mínima que habilita trabajo posterior]

- [ ] T001 [REF] [acción concreta en ruta/archivo] — [evidencia]

## Bloque 2: Fundamentos compartidos

**Propósito**: [reglas, datos o infraestructura compartida realmente necesaria]

- [ ] T002 [REF] [acción concreta en ruta/archivo] — [evidencia]

## Bloque N: [Capacidad, componente o unidad coherente]

**Resultado cubierto**: [referencias de producto satisfechas por este bloque]  
**Dependencias**: [TIDs o ninguna]  
**Criterio de integración**: [cómo se integra con el resultado completo]

### Evidencia antes o junto con la implementación

<!--
Incluye pruebas técnicas o evidencia equivalente cuando los criterios de
aceptación o el riesgo las requieran. No las omitas solo porque el prompt no usó
la palabra "prueba".
-->

- [ ] T0XX [P] [REF] [crear o preparar evidencia en ruta/archivo] — [resultado esperado]

### Implementación

- [ ] T0XX [REF] [implementar comportamiento en ruta/archivo] — [evidencia]
- [ ] T0XX [REF] [cubrir estados y recuperación en ruta/archivo] — [evidencia]

### Integración

- [ ] T0XX [REF] [integrar con dependencias en ruta/archivo] — [evidencia extremo a extremo]

## Verificación del resultado completo

- [ ] T0XX [REF] Reconciliar cada fila del inventario de cobertura con la implementación — matriz sin vacíos ni tareas huérfanas.
- [ ] T0XX [REF] Verificar el recorrido completo, incluidos estados vacíos, carga, error, extremos y recuperación — evidencia registrada.
- [ ] T0XX [REF] Evaluar comprensión, esfuerzo, confianza, control, accesibilidad y rendimiento aplicables — hallazgos y evidencia.
- [ ] T0XX [REF] Registrar pendientes, supuestos, excepciones aprobadas y decisiones humanas requeridas — estado explícito.

## Dependencias y orden de ejecución

<!--
Declara además el ESTADO ESPERADO DE LAS VERIFICACIONES durante el intervalo.
Si el orden deja una comprobación imposible de satisfacer hasta un bloque posterior,
dilo aquí: qué comprobación queda en rojo, entre qué bloques y por qué razón conocida.
Una compuerta roja sin declarar deja de señalar, y un fallo nuevo llega a una rama que
ya estaba rota sin distinguirse del ruido.
-->


| Tarea o bloque | Depende de | Puede ejecutarse en paralelo con | Bloquea |
|---|---|---|---|
| [ID] | [IDs / ninguna] | [IDs / ninguna] | [IDs] |

## Reglas de generación

- Deriva tareas para **todo** el alcance autorizado.
- Agrupa por historia, Job Story, capacidad, componente o bloque técnico según la estructura real de la fuente y del plan.
- Usa prioridad, MVP, independencia o entrega incremental únicamente cuando producto lo haya definido o autorizado.
- Conserva dependencias legítimas; no fuerces independencia artificial.
- No agregues funcionalidades, configuraciones, abstracciones ni controles no fundamentados.
- No presentes una ejecución parcial como reducción o completitud del alcance.
- Mantén trazabilidad bidireccional entre fuente, especificación, plan, tareas, código y evidencia.
