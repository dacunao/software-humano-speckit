# Registro de cambios

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
