# Software Humano para SpecKit

Preset instalable que aplica el **Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1** al ciclo SDD nativo de SpecKit.

## Qué hace

- instala una proyección completa del núcleo como `constitution-template`;
- acepta PRD, Job Stories u otras definiciones de producto sin deformar su estructura;
- conserva el alcance completo y su autoridad;
- ordena el trabajo por dependencias, bloqueantes e integración;
- mantiene prioridad, MVP, independencia e incrementalidad como opciones condicionales;
- exige evidencia proporcional a los criterios de aceptación y al riesgo;
- conserva los comandos, scripts, hooks, handoffs y checklists nativos de SpecKit.

## Qué no hace

- no sustituye SpecKit ni crea otro ciclo SDD;
- no agrega etapas, ceremonias o artefactos metodológicos;
- no modifica el código central de SpecKit;
- no decide alcance, prioridad, releases o aceptación por cuenta del agente;
- no convierte todas las entradas en historias de usuario.

## Compatibilidad verificada

- Núcleo del manifiesto: **2.1**.
- Anexo de aplicación SpecKit: **1.2**.
- Preset Software Humano: **1.2.0**.
- SpecKit: `>=1.0.0,<2.0.0`.
- Referencia de validación: SpecKit `1.0.8` (etiqueta oficial) y `1.0.9.dev0`, revisión `d4229c071c7ea3885b43e8a7739847300f618f13`. Las versiones 1.0.1, 1.0.2, 1.1.0 y 1.2.0 fueron instaladas y verificadas de extremo a extremo sobre SpecKit `1.0.8` el 21 de septiembre de 2026.

## Instalación local

El proyecto debe haber sido inicializado previamente con SpecKit y tener una integración de agente activa.

```bash
specify preset add --dev /ruta/absoluta/software-humano-spec-kit-preset-1.2.0 --priority 5
```

Comprueba la instalación y la resolución efectiva:

```bash
specify preset info software-humano
specify preset resolve constitution-template
specify preset resolve spec-template
specify preset resolve plan-template
specify preset resolve tasks-template
specify preset resolve speckit.specify
```

Después de instalarlo en un proyecto existente, ejecuta el comando de constitución de la integración activa —por ejemplo, `/speckit.constitution`— para materializar el núcleo aprobado en `.specify/memory/constitution.md`. La instrucción debe limitarse a instalar o restaurar el núcleo v2.1 incluido en el preset; no debe pedir una reinterpretación del manifiesto.

## Uso

El flujo continúa siendo el flujo nativo de SpecKit:

1. `constitution` instala o verifica el núcleo aprobado.
2. `specify` deriva una especificación trazable desde el fundamento de producto.
3. `clarify` resuelve ambigüedades materiales en rondas focalizadas.
4. `plan` define la estrategia técnica y las dependencias.
5. `tasks` deriva trabajo para todo el alcance autorizado.
6. `analyze` comprueba consistencia, cobertura y doctrina.
7. `implement` ejecuta las tareas dentro de la autoridad otorgada.
8. `converge` identifica y cierra brechas del alcance aprobado.

El comando `checklist` y el checklist nativo de requisitos se conservan sin reemplazo. Un checklist evalúa la calidad de requisitos; no demuestra que la implementación esté terminada.

## Tratamiento de la constitución

`templates/constitution-template.md` contiene el núcleo v2.1 completo, reorganizado únicamente para cumplir la jerarquía nativa de SpecKit. No es un resumen. El comando compuesto de constitución impide que un prompt circunstancial modifique la doctrina o incorpore reglas particulares de un proyecto.

La instalación del preset no debe combinarse con `constitution-sync` salvo que el equipo haya decidido conscientemente adoptar su modelo de propagación materializada. Este paquete utiliza el modelo nativo recomendado de resolución en tiempo de ejecución y mantiene la constitución como fuente única de verdad.

## Decisiones de composición

- `constitution-template`, `spec-template`, `plan-template` y `tasks-template` se reemplazan porque su estructura nativa contiene supuestos incompatibles o porque debe alojar el núcleo completo.
- Los comandos se componen con estrategia `wrap`: el comando nativo permanece íntegro y una directiva vinculante precisa las excepciones doctrinales.
- `checklist` y los demás componentes no declarados se resuelven directamente desde SpecKit.

## Desinstalación

```bash
specify preset remove software-humano
```

La desinstalación retira el preset y recompone los comandos nativos. La constitución materializada es un documento del proyecto y debe conservarse o cambiarse mediante una decisión explícita; no se borra automáticamente.

## Publicación futura

La licencia de distribución está aprobada: **MIT**, con `templates/constitution-template.md` bajo **CC BY 4.0** por contener el texto del núcleo. El repositorio de publicación previsto es `https://github.com/dacunao/spec-kit-preset-software-humano`.

Falta únicamente el *release*: mientras no exista, no hay URL de descarga versionada ni su `sha256`. Hasta entonces el preset se instala localmente desde su directorio o su ZIP, y **no debe presentarse como publicado ni como integración oficial de SpecKit**.

## Documentos rectores

- `templates/constitution-template.md`: proyección operativa completa del núcleo v2.1.
- `docs/Anexo_Aplicacion_SpecKit_v1.2.md`: diseño y límites de la adaptación.

Ante una contradicción, prevalece el núcleo. El agente debe informar la incompatibilidad y detener la decisión afectada.
