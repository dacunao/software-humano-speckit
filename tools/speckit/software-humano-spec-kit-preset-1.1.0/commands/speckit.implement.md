---
description: Implementa dentro del alcance y la autoridad, manteniendo visibles cobertura, estados y evidencia.
strategy: wrap
---

## Directiva vinculante de Software Humano

Conserva la ejecución nativa y aplica estas reglas:

- Mantén visible el inventario completo aunque trabajes por segmentos o en paralelo.
- No agregues funcionalidades, modos, configuraciones o abstracciones sin fundamento aprobado.
- Respeta dependencias, reglas deterministas, permisos, estados y recuperación descritos.
- Produce la evidencia requerida por cada tarea y criterio; una prueba verde no sustituye el resultado humano.
- El checklist de requisitos y los checklists personalizados controlan calidad de requisitos, no completitud de implementación.
- Una ejecución parcial se informa como avance parcial y nunca como reducción del alcance o aceptación final.
- Detente ante contradicción material, pérdida de cobertura, autoridad insuficiente o una acción sensible sin autorización y recuperación.
- El agente no puede otorgarse revisión humana, excepción aprobada ni aceptación de producto.

## Alcance semántico de esta operación

**Esta es la operación donde se toman las decisiones reales de producto.** El anexo le asigna las disposiciones siguientes. **Declara en tu informe cuáles aplicaste y con qué consecuencia concreta.**

**Antes de decidir: consulta lo que ya se decidió**

- Lee la **Comprobación de constitución** de `plan.md` antes de resolver cualquier alternativa de diseño o implementación. Esa tabla ya tradujo las disposiciones del núcleo a restricciones concretas de este proyecto. **Una decisión que esa tabla ya adjudica no se vuelve a abrir, ni se traslada a la persona como si estuviera pendiente.**
- Si vas a presentar opciones a la autoridad humana, comprueba primero que las fuentes rectoras no las resuelvan. Abrir una decisión que la doctrina ya cerró gasta la atención que **`P06`** protege.

**Complejidad, confianza y control**

- **`P03`** — absorbe la complejidad en el sistema. Ninguna estructura interna, nombre de entidad ni excepción del dominio llega a la persona sin traducción.
- **`P07`** — estado visible, consecuencia anticipada, resultado confirmado y recuperación proporcional al riesgo.
- **`P08`** — estados vacíos, de carga, error, éxito, interrupción y retorno son parte del trabajo, no un cierre posterior.
- **`P09`** — respuesta, progreso honesto y preservación del trabajo.
- **`P10`** — confirmación proporcional al impacto, reversibilidad, y ninguna captura de datos que el producto no use.
- **`A05`** — respeta los estados y transiciones definidos; si aparece uno nuevo, decláralo en lugar de resolverlo en silencio.

**Uso de IA y evidencia**

- **`D04`** — reglas críticas, permisos, cálculos y validaciones como lógica verificable; no delegues certeza a un comportamiento variable.
- **`D05`** — código correcto y pruebas verdes no equivalen a producto terminado.
- **`D06`**, **`CR06`** — declara incertidumbre, mantén revisión y reversibilidad, y no ejecutes acciones de alto impacto sin autorización proporcional.
- **`F08`**, **`A02`**, **`A07`**, **`CR07`** — mantén visible el inventario completo, produce la evidencia que cada criterio exige, y no agregues nada sin fundamento aprobado.

**Controles de entrada** *(el mapa del anexo es un mínimo y no una lista excluyente)*

- **`SH-SCORE` como entrada** — antes de proponer una solución, puntúala. Una dimensión crítica en **0** significa que no está lista para presentarse. Sirve además para lo que a un agente le cuesta solo: **separar «lo razoné» de «lo observé»**. Un argumento sólido no es evidencia.
- **`SH-AP`** — vigila «el agente agrega por si acaso», «el happy path define el producto» y «la estética maquilla la fricción».

**Entrega**

- **`O06`**–**`O09`** — archivos y componentes tocados, estados cubiertos, pruebas y su resultado, y riesgos, pendientes y decisiones que requieren juicio humano.

**No edites el contenido para que pase una validación.** La regla que prohíbe modificar el paquete para satisfacer una comprobación se aplica igual a lo que el proyecto produce: redactar esquivando lo que un validador marca mal produce una suite verde y un resultado peor. Si una validación está equivocada, corrígela y declara la corrección.

---

{CORE_TEMPLATE}

## Confirmación de aplicación Software Humano

El reporte final debe indicar qué se implementó, qué evidencia se obtuvo, qué cobertura permanece, qué supuestos y excepciones existen, qué riesgos continúan y qué requiere juicio humano. Solo usa la palabra "terminado" cuando todas las tareas aplicables estén reconciliadas con la definición completa y la definición de terminado del núcleo.

**Declaración de activación doctrinal, obligatoria.** Indica qué disposiciones del alcance semántico de esta operación aplicaste y **qué consecuencia concreta tuvo cada una** en el resultado. Una disposición nombrada sin consecuencia no cuenta como aplicada. Si alguna no fue aplicable, decláralo y explica por qué.

Esta declaración no es un trámite: es lo que permite a `analyze` comprobar que la doctrina gobernó las decisiones y no solo estuvo disponible.
