# Registro de cambios

## 1.1.0 — 2026-09-22

**Conformidad con el anexo v1.2.** Las versiones anteriores no incorporaban las *referencias por operación* que el anexo exige en su línea 516 y verifica en sus criterios 14 y 15. De unas cien asignaciones que el mapa reparte entre los ocho comandos, el preset citaba **tres**.

El efecto medido en el primer piloto real: el preset protegía bien el alcance y la autoridad, y no aplicaba los principios de experiencia ni los controles de verificación. Nueve de los diez principios no aparecían en ningún comando; `V01`–`V12`, `SH-SCORE`, `SH-AP` y `SH-POCKET` estaban ausentes por completo.

**Ningún cambio doctrinal.** El núcleo v2.1 y el anexo v1.2 son idénticos. `templates/constitution-template.md` es byte a byte la de 1.0.2, de modo que **un proyecto instalado no necesita rematerializar su constitución**.

### Qué cambia

- **Los ocho comandos** ganan un apartado «Alcance semántico de esta operación» que nombra las disposiciones que el anexo les asigna y traduce cada una a la obligación que impone **en ese momento**. Se referencia el identificador y se describe el comportamiento exigido, sin copiar una versión abreviada que pueda divergir del núcleo.
- **Los ocho comandos** exigen ahora una **declaración de activación doctrinal**: qué disposiciones se aplicaron y con qué consecuencia concreta. Una disposición nombrada sin consecuencia no cuenta como aplicada.
- **`analyze`** comprueba que esa declaración exista y sea concreta. Su ausencia es un hallazgo. Recorre además `V01`–`V12` una por una y activa `SH-SCORE`, `SH-AP` y `SH-GOV`.
- **`implement`** debe consultar la **Comprobación de constitución** de `plan.md` antes de resolver una alternativa. Una decisión que esa tabla ya adjudica no se reabre ni se traslada a la persona como pendiente.
- **`clarify`** incorpora la regla simétrica que faltaba: antes de **abrir** una pregunta, comprobar si las fuentes rectoras ya la deciden. El preset protegía contra cerrar una decisión sin autoridad y no contra abrir una que ya estaba cerrada.
- **`SH-SCORE` como entrada** en `plan` e `implement`, además de su lugar en verificación. El mapa del anexo es *«un mínimo, no una lista excluyente»*, de modo que excederlo donde el riesgo lo justifica no lo contradice.
- **`plan-template.md`** convierte la Comprobación de constitución en una tabla que exige consecuencias verificables, e incorpora la puntuación de entrada.
- **`tasks-template.md`** pide declarar el **estado esperado de las verificaciones por intervalo**: qué comprobación queda en rojo, entre qué bloques y por qué.

### Lo que esto no logra

Poner la doctrina delante sube la probabilidad de que se consulte; no la garantiza. Lo que cambia es la naturaleza del fallo: antes el instrumento no estaba puesto; ahora un fallo será haber ignorado algo disponible y declarable, y `analyze` puede detectarlo.

## 1.0.2 — 2026-09-21

Licencia. **Ningún cambio doctrinal ni funcional**: `templates/constitution-template.md` es byte a byte idéntica a la de 1.0.1, y las plantillas y comandos no cambian.

- sustituye la licencia propietaria por **MIT**, y `preset.yml` declara `license: "MIT"`. La versión 1.0.1 y anteriores declaraban «All rights reserved… no permission is granted to copy, modify, distribute, sublicense, publish, or use this package», lo que hacía **inejecutable** la decisión de publicar el preset en el catálogo de comunidad de SpecKit, que exige un archivo de licencia open source;
- declara la frontera de licencias **por naturaleza y no por carpeta**: `templates/constitution-template.md` contiene el texto del núcleo v2.1 y se publica bajo **CC BY 4.0**, mientras MIT cubre el resto del preset;
- conserva el aviso de que SpecKit y el software de terceros mantienen sus propias licencias.

Un proyecto que tenga instalada la versión 1.0.1 **no necesita rematerializar su constitución** al adoptar esta versión: la proyección doctrinal no cambió.

## 1.0.1 — 2026-09-21

Corrección de navegación. **Ningún cambio doctrinal**: el texto del núcleo v2.1, ignorando las líneas de ancla, es byte a byte idéntico al de la versión 1.0.0.

- corrige dos anclas desplazadas en `templates/constitution-template.md`. Al reordenar el documento para que `Governance` quede como sección final —según exige la jerarquía nativa de SpecKit—, las anclas no acompañaron a sus secciones: `sh-gov` precedía la Guía de bolsillo, la sección `Governance` quedaba sin ancla y `sh-pocket` quedaba huérfana al final del archivo;
- tras la corrección, las siete anclas (`sh-index`, `sh-fund`, `sh-stop`, `sh-score`, `sh-ap`, `sh-pocket`, `sh-gov`, `sh-done`) preceden cada una a su propia sección;
- sin cambios en `preset.yml` salvo la versión, ni en las plantillas de especificación, plan y tareas, ni en los ocho comandos compuestos.

## 1.0.0 — 2026-09-21

Primera versión instalable.

- incorpora la proyección completa del núcleo v2.1;
- reemplaza las plantillas de constitución, especificación, plan y tareas;
- compone los comandos nativos de constitución, especificación, clarificación, planificación, tareas, análisis, implementación y convergencia;
- conserva sin reemplazo el checklist nativo y los componentes no afectados;
- convierte prioridad, MVP, independencia e incrementalidad en condiciones de aplicación, no en reglas universales;
- declara compatibilidad con SpecKit 1.x;
- incorpora instrucciones de instalación, verificación y desinstalación.
