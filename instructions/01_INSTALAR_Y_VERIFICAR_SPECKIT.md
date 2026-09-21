# Prompt de implementación de Software Humano en SpecKit

## Propósito

Utiliza este prompt para instalar, activar y verificar el preset **Software Humano v1.0.0** en un proyecto que utilizará SpecKit. El objetivo termina cuando SpecKit opera con el núcleo del manifiesto v2.1 y la adaptación ha superado todas las verificaciones descritas aquí.

Este trabajo configura el método. No autoriza a desarrollar el producto, modificar su PRD ni iniciar una implementación de software salvo que exista una instrucción posterior y explícita.

---

## Prompt

Actúa como agente senior responsable de integrar una adaptación metodológica en un proyecto SpecKit existente. Debes instalar y verificar el paquete **Software Humano para SpecKit v1.0.0** utilizando exclusivamente los mecanismos nativos de SpecKit.

Tu responsabilidad no es reinterpretar el manifiesto ni mejorar el paquete. Tu responsabilidad es dejar el proyecto técnicamente preparado para que los agentes de programación apliquen el **Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1** durante el ciclo SDD nativo de SpecKit.

### Entradas

Antes de actuar, identifica estas entradas:

- **PROJECT_ROOT**: `[ruta absoluta del proyecto que utilizará SpecKit]`
- **PACKAGE_PATH**: `[ruta absoluta de Software_Humano_SpecKit_Preset_v1.0.0.zip o del directorio ya descomprimido]`
- **INITIALIZE_IF_NEEDED**: `[false por defecto; true solo si el usuario autoriza inicializar SpecKit]`
- **EXPECTED_SHA256**: `d698aebd39b65157875bbc8ab0aab6480b30420745cdd13a7b67bd565c1db1b3`

Si falta `PROJECT_ROOT` o `PACKAGE_PATH`, solicítalo y detente. No adivines rutas.

### Fuentes de autoridad

Respeta esta precedencia:

1. El núcleo v2.1 contenido en `templates/constitution-template.md` gobierna la doctrina.
2. El fundamento de producto autorizado gobierna qué debe construirse.
3. El anexo v1.2 contenido en `docs/Anexo_Aplicacion_SpecKit_v1.2.md` gobierna la correspondencia con SpecKit.
4. El preset v1.0.0 gobierna la materialización técnica de esa correspondencia.
5. SpecKit conserva su comportamiento nativo en todo lo que el preset no modifica.

Ante una contradicción real o aparente, no inventes una conciliación: identifica las disposiciones involucradas, informa el conflicto y detén la decisión afectada.

### Resultado requerido

La integración solo se considera completa cuando puedas demostrar que:

- SpecKit pertenece al rango `>=1.0.0,<2.0.0`;
- existe una integración de agente activa;
- el preset `software-humano` v1.0.0 está instalado, habilitado y con prioridad 5;
- cuatro plantillas resuelven desde el preset;
- ocho comandos conservan el core nativo y agregan la capa Software Humano mediante composición `wrap`;
- `checklist` continúa resolviendo desde SpecKit y no ha sido sustituido por el preset;
- `.specify/memory/constitution.md` contiene la proyección completa del núcleo v2.1;
- los comandos adaptados están registrados en la integración activa;
- no se modificó código central de SpecKit ni código de la aplicación;
- cualquier pendiente o excepción se encuentra explícitamente informado.

## Procedimiento

### 1. Inspección previa sin modificaciones

Sitúate en `PROJECT_ROOT` y comprueba:

```bash
pwd
git status --short
specify version
specify integration status --json
specify preset list --json
```

Después:

1. Confirma que la ruta corresponde al proyecto solicitado.
2. Registra los cambios preexistentes sin modificarlos.
3. Si existen cambios preexistentes en `.specify/` o en los archivos de comandos de la integración activa, detente y solicita una decisión humana antes de instalar.
4. Confirma la existencia de `.specify/`.
5. Si SpecKit no está inicializado:
   - si `INITIALIZE_IF_NEEDED` es `false`, informa el bloqueo y detente;
   - si es `true`, inicialízalo mediante `specify init` usando la integración indicada por el usuario; no elijas una integración por inferencia.
6. Si la versión instalada está fuera de `>=1.0.0,<2.0.0`, no fuerces la instalación.
7. Si existe otro preset llamado `software-humano`:
   - si es v1.0.0, no lo reinstales todavía: continúa con la verificación y reconcilia solamente si una comprobación falla;
   - si tiene otra versión, informa la diferencia y detente antes de reemplazarlo.

No uses `--force`, no borres configuraciones existentes y no limpies cambios ajenos.

### 2. Verificación del paquete

Si `PACKAGE_PATH` apunta al ZIP:

1. Calcula su SHA-256.
2. Compáralo con `EXPECTED_SHA256`.
3. Si no coincide, detente: no instales un paquete cuya integridad no está demostrada.
4. Descomprímelo en un directorio temporal específico para esta tarea.
5. Localiza dentro de él el directorio que contiene `preset.yml`.

Si `PACKAGE_PATH` apunta a un directorio, confirma que contiene como mínimo:

```text
preset.yml
README.md
LICENSE
CHANGELOG.md
templates/constitution-template.md
templates/spec-template.md
templates/plan-template.md
templates/tasks-template.md
commands/speckit.constitution.md
commands/speckit.specify.md
commands/speckit.clarify.md
commands/speckit.plan.md
commands/speckit.tasks.md
commands/speckit.analyze.md
commands/speckit.implement.md
commands/speckit.converge.md
docs/Anexo_Aplicacion_SpecKit_v1.2.md
```

Lee `preset.yml` y verifica antes de instalar:

- `schema_version: "1.0"`;
- `preset.id: "software-humano"`;
- `preset.version: "1.0.0"`;
- compatibilidad `>=1.0.0,<2.0.0`;
- cuatro entradas de tipo `template`;
- ocho entradas de tipo `command` con estrategia `wrap`;
- ausencia de scripts, extensiones, workflows o bundles propios.

No edites el paquete para hacer que pase una validación. Una discrepancia es un bloqueo que debe informarse.

### 3. Instalación nativa del preset

Desde `PROJECT_ROOT`, instala el directorio que contiene `preset.yml`:

```bash
specify preset add --dev "[PRESET_DIR]" --priority 5
```

No instales una extensión, un workflow, un bundle ni `constitution-sync`. No copies archivos manualmente sobre el código central o las plantillas base de SpecKit.

### 4. Verificación de registro y resolución

Ejecuta:

```bash
specify preset list --json
specify preset info software-humano
specify integration status --json
```

Comprueba las plantillas:

```bash
specify preset resolve constitution-template
specify preset resolve spec-template
specify preset resolve plan-template
specify preset resolve tasks-template
```

Las cuatro deben indicar `software-humano` como capa de mayor precedencia.

Comprueba los comandos:

```bash
specify preset resolve speckit.constitution
specify preset resolve speckit.specify
specify preset resolve speckit.clarify
specify preset resolve speckit.plan
specify preset resolve speckit.tasks
specify preset resolve speckit.analyze
specify preset resolve speckit.implement
specify preset resolve speckit.converge
```

Cada comando debe mostrar una cadena de composición formada, como mínimo, por:

1. el comando base de SpecKit;
2. la capa `software-humano` con estrategia `wrap`.

Comprueba también, usando `specify artifact info --json` cuando resulte útil, que la integración activa recibió el contenido efectivo de esos comandos.

Verifica que el preset no interviene el checklist:

```bash
specify preset resolve checklist-template
specify preset resolve speckit.checklist
```

Ninguno debe mostrar `software-humano` como contribuyente. El checklist nativo de requisitos y el comando de checklists personalizados deben permanecer intactos.

### 5. Materialización controlada de la constitución

La instalación del preset no basta para considerar activo el manifiesto en un proyecto existente. Debes materializar la constitución mediante el comando registrado por la integración activa.

Invoca el equivalente real de `speckit.constitution` para esa integración —por ejemplo, `$speckit-constitution` en una integración basada en skills o `/speckit.constitution` donde corresponda— con esta instrucción exacta:

> Instala o restaura en `.specify/memory/constitution.md` la proyección aprobada del Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1 incluida en `constitution-template`. No resumas, reformules, contextualices ni enmiendes su doctrina. Conserva el mecanismo nativo de resolución, validación y reporte de impacto. Si la constitución existente contiene cambios humanos o una versión doctrinal distinta, no la sobrescribas: presenta la diferencia y solicita resolución.

Si tu entorno no permite invocar el comando registrado:

- no copies la plantilla manualmente como sustituto silencioso;
- informa que el preset quedó instalado pero el manifiesto todavía no está activo;
- entrega al usuario el comando exacto que debe ejecutar;
- detente antes de iniciar `specify`, `plan` o cualquier desarrollo.

### 6. Verificación de la constitución materializada

Lee `.specify/memory/constitution.md` y demuestra que contiene:

- versión doctrinal 2.1;
- un único título principal;
- la sección `Core Principles`;
- los diez principios `P01`–`P10`;
- `SH-FUND`;
- las directivas `D01`–`D06`;
- el flujo `F01`–`F08`;
- los artefactos `A01`–`A08`;
- `SH-STOP` y `STOP01`–`STOP07`;
- el contrato `CR01`–`CR08`;
- las salidas `O01`–`O09`;
- la verificación `V01`–`V12`;
- `SH-SCORE`, `SH-AP`, `SH-GOV`, `SH-DONE` y `SH-POCKET`;
- una sección final `Governance` con versión y fechas ISO;
- ningún placeholder nativo sin resolver.

El reporte temporal de impacto que produzca el comando de constitución puede permanecer durante la revisión, pero no constituye doctrina.

No declares válida una constitución resumida, parcialmente copiada o reconstruida desde el anexo.

### 7. Comprobación de límites

Antes de cerrar, confirma que la integración no hizo ninguna de estas cosas:

- modificar el código central de SpecKit;
- sustituir el ciclo SDD nativo;
- instalar componentes distintos del preset;
- crear etapas, controles o artefactos metodológicos nuevos;
- imponer historias de usuario, prioridad, MVP, independencia o incrementalidad;
- alterar el PRD o cualquier fundamento de producto;
- modificar archivos de la aplicación;
- atribuir al agente aprobación humana.

Revisa nuevamente `git status --short` y separa los cambios producidos por la integración de los cambios que ya existían.

### 8. No ejecutar todavía el desarrollo del producto

No generes un ejemplo artificial ni ejecutes `speckit.specify` sobre un PRD real como parte de esta instalación. Una vez aprobada la integración, el siguiente paso debe ser una instrucción humana separada que identifique el fundamento de producto autorizado.

Cuando llegue esa instrucción, la primera prueba de aplicación deberá ejecutar:

```text
specify → clarify, si corresponde → plan → tasks → analyze
```

Solo después de revisar esos resultados se autoriza `implement` y posteriormente `converge`.

## Condiciones de detención

Detente y solicita decisión humana si ocurre cualquiera de estas situaciones:

1. falta una ruta o no puede identificarse el proyecto correcto;
2. SpecKit no está inicializado y no existe autorización para inicializarlo;
3. la versión de SpecKit es incompatible;
4. el checksum del ZIP no coincide;
5. `preset.yml` o un archivo declarado falta o fue modificado;
6. existe otra versión del preset instalada;
7. hay cambios preexistentes que se superponen con `.specify/` o la integración activa;
8. no existe una integración activa identificable;
9. una plantilla no resuelve desde el preset;
10. un comando no conserva el core en su cadena de composición;
11. `software-humano` aparece como contribuyente del checklist;
12. la constitución existente fue modificada por una persona o contiene otra versión;
13. no puedes materializar o verificar la constitución completa;
14. completar el trabajo exigiría modificar el core, el manifiesto, el anexo o el paquete.

Una detención correcta debe indicar: hecho observado, evidencia, impacto, decisión requerida y la acción que no se ejecutó.

## Formato obligatorio del informe final

Entrega un informe breve y verificable con estas secciones:

### Estado

`LISTO`, `LISTO CON PENDIENTES` o `BLOQUEADO`.

### Entorno

- raíz del proyecto;
- versión de SpecKit;
- integración activa;
- versión y prioridad del preset.

### Verificaciones

| Comprobación | Evidencia | Resultado |
|---|---|---|
| Integridad del paquete | SHA-256 observado | Pasa / Falla |
| Cuatro plantillas | Origen resuelto | Pasa / Falla |
| Ocho comandos | Cadena core + wrap | Pasa / Falla |
| Checklist nativo | Ausencia del preset | Pasa / Falla |
| Constitución v2.1 | Identificadores y metadatos | Pasa / Falla |
| Registro del agente | Integración activa | Pasa / Falla |
| Límites | Archivos realmente modificados | Pasa / Falla |

### Cambios realizados

Enumera únicamente archivos o directorios que realmente hayan cambiado.

### Pendientes y decisiones humanas

Indica cualquier excepción, incertidumbre o acción manual requerida. No ocultes pendientes bajo un estado exitoso.

### Próximo paso autorizado

Si todo pasa, informa:

> La adaptación Software Humano v1.0.0 está instalada y el núcleo v2.1 está activo. El proyecto está preparado para recibir una definición de producto autorizada mediante `speckit.specify`. No se ha iniciado todavía el desarrollo del producto.

## Definición de terminado

No declares completada la integración por el solo hecho de que `specify preset add` haya terminado sin errores. Está terminada únicamente cuando instalación, resolución, composición, registro, materialización, contenido de la constitución y límites hayan sido comprobados con evidencia.
