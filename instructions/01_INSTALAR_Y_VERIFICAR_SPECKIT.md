# Instalar y verificar la adaptación Software Humano en SpecKit

## Propósito

Instalar, activar y verificar el preset **Software Humano** en un proyecto que utilizará SpecKit. El objetivo termina cuando SpecKit opera con el núcleo del manifiesto v2.1 y la adaptación ha superado todas las verificaciones descritas aquí.

Este trabajo configura el método. No autoriza a desarrollar el producto, modificar su fundamento ni iniciar una implementación salvo que exista una instrucción posterior y explícita.

> **Antes de empezar, aplica [`00_REQUISITOS_DE_INSTALACION.md`](00_REQUISITOS_DE_INSTALACION.md).** Ese documento existe porque la primera aplicación real de esta instrucción se detuvo cuatro veces por requisitos de entorno no declarados. Ejecuta `tools/speckit/preflight.sh` y resuelve todo bloqueo antes de continuar.

---

## Prompt

Actúa como agente senior responsable de integrar una adaptación metodológica en un proyecto SpecKit. Debes instalar y verificar el paquete **Software Humano para SpecKit** utilizando exclusivamente los mecanismos nativos de SpecKit.

Tu responsabilidad no es reinterpretar el manifiesto ni mejorar el paquete. Es dejar el proyecto técnicamente preparado para que los agentes apliquen el **Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1** durante el ciclo SDD nativo.

### Entradas

- **PROJECT_ROOT**: `[ruta absoluta del proyecto que utilizará SpecKit]`
- **PACKAGE_PATH**: `[ruta absoluta del ZIP del preset o del directorio ya descomprimido]`
- **INITIALIZE_IF_NEEDED**: `[false por defecto; true solo si la persona autoriza inicializar SpecKit]`
- **SPECIFY_CMD**: `[cómo invocar SpecKit: 'specify' si la instalación global está en rango, o 'tools/speckit/specify' para la instancia aislada]`
- **EXPECTED_SHA256**: el declarado en `SHA256SUMS` para el ZIP del preset

Si falta `PROJECT_ROOT` o `PACKAGE_PATH`, solicítalo y detente. No adivines rutas.

### Fuentes de autoridad

1. El núcleo v2.1 contenido en `templates/constitution-template.md` gobierna la doctrina.
2. El fundamento de producto autorizado gobierna qué debe construirse.
3. El anexo v1.2 contenido en `docs/Anexo_Aplicacion_SpecKit_v1.2.md` gobierna la correspondencia con SpecKit.
4. El preset gobierna la materialización técnica de esa correspondencia.
5. SpecKit conserva su comportamiento nativo en todo lo que el preset no modifica.

Ante una contradicción real o aparente, no inventes una conciliación: identifica las disposiciones involucradas, informa el conflicto y detén la decisión afectada.

### Resultado requerido

La integración solo está completa cuando puedas demostrar que:

- SpecKit pertenece al rango `>=1.0.0,<2.0.0`;
- existe una integración de agente activa, elegida por una persona;
- el preset `software-humano` está instalado, habilitado y con prioridad 5;
- cuatro plantillas resuelven desde el preset;
- ocho comandos conservan el core nativo y agregan la capa Software Humano mediante composición `wrap`;
- `checklist` sigue resolviendo desde SpecKit y no fue sustituido;
- `.specify/memory/constitution.md` contiene la proyección completa del núcleo v2.1;
- los comandos adaptados están registrados en la integración activa;
- no se modificó código central de SpecKit ni código de la aplicación;
- cualquier pendiente o excepción está explícitamente informado.

## Procedimiento

### 1. Inspección previa sin modificaciones

Sitúate en `PROJECT_ROOT` y comprueba:

```bash
pwd
git status --short
tools/speckit/preflight.sh
$SPECIFY_CMD version
$SPECIFY_CMD integration status --json
$SPECIFY_CMD preset list --json
```

Después:

1. Confirma que la ruta corresponde al proyecto solicitado.
2. Registra los cambios preexistentes sin modificarlos.
3. Si existen cambios preexistentes en `.specify/` o en los archivos de comandos de la integración activa, detente y solicita una decisión humana antes de instalar.
4. Confirma la existencia de `.specify/`.
5. Si SpecKit no está inicializado:
   - si `INITIALIZE_IF_NEEDED` es `false`, informa el bloqueo y detente;
   - si es `true`, inicialízalo con la integración **indicada por la persona**; no elijas una por inferencia.
6. Si la versión está fuera de `>=1.0.0,<2.0.0`, no fuerces la instalación. Aplica el requisito 2 de la instrucción 00 y presenta las dos salidas reales: instancia aislada o actualización global.
7. Si existe otro preset `software-humano`:
   - si es la misma versión, no lo reinstales: continúa verificando y reconcilia solo si una comprobación falla;
   - si tiene otra versión, informa la diferencia y detente antes de reemplazarlo.

**Sobre `--force`.** Significa cosas distintas según el comando, y confundirlas fue un defecto de la versión anterior de este documento:

- En **`$SPECIFY_CMD preset add`** implica sobrescribir una instalación existente. **No lo uses nunca.**
- En **`$SPECIFY_CMD init --here`** únicamente omite la confirmación interactiva de un *merge*. Como el paquete ya ocupa la raíz del repositorio, el directorio nunca está vacío y en una sesión no interactiva el comando falla sin él:

  ```
  Error: Current directory is not empty and no confirmation input is available.
  Re-run with --force to merge into it.
  ```

  Úsalo solo con un commit base establecido, y verifica inmediatamente después que no sobrescribió nada:

  ```bash
  git status --short
  shasum -a 256 -c SHA256SUMS
  ```

No borres configuraciones existentes y no limpies cambios ajenos.

### 2. Verificación del paquete

Si `PACKAGE_PATH` apunta al ZIP:

1. Calcula su SHA-256 y compáralo con `EXPECTED_SHA256`.
2. Si no coincide, detente: no instales un paquete cuya integridad no está demostrada.
3. Descomprímelo en un directorio temporal específico para esta tarea.
4. Localiza dentro de él el directorio que contiene `preset.yml`.

Si apunta a un directorio, confirma que contiene como mínimo:

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
- `preset.version` coincidente con el paquete;
- compatibilidad `>=1.0.0,<2.0.0`;
- cuatro entradas de tipo `template`;
- ocho entradas de tipo `command` con estrategia `wrap`;
- ausencia de scripts, extensiones, workflows o bundles propios.

> **No es un defecto** que las doce entradas aparezcan bajo la clave `provides.templates:`. El CLI clasifica por el campo `type` de cada entrada, y `preset list --json` reporta correctamente `{"commands": 8, "templates": 4, "scripts": 0}`. No lo "corrijas".

No edites el paquete para hacer que pase una validación. Una discrepancia es un bloqueo que debe informarse.

### 3. Instalación nativa del preset

Limpia primero la basura del sistema de archivos, porque `--dev` copia el directorio completo:

```bash
find "[PRESET_DIR]" -name '.DS_Store' -delete
```

Instala:

```bash
$SPECIFY_CMD preset add --dev "[PRESET_DIR]" --priority 5
```

`--dev` significa "instalar desde un directorio local". Produce una **copia real** en `.specify/presets/software-humano/`, no un enlace: el preset instalado queda autocontenido y no depende del directorio de origen.

No instales una extensión, un workflow, un bundle ni `constitution-sync`. No copies archivos manualmente sobre el código central o las plantillas base de SpecKit.

### 4. Verificación de registro y resolución

```bash
$SPECIFY_CMD preset list --json
$SPECIFY_CMD preset info software-humano
$SPECIFY_CMD integration status --json
```

#### 4.1 · Plantillas

```bash
$SPECIFY_CMD preset resolve constitution-template
$SPECIFY_CMD preset resolve spec-template
$SPECIFY_CMD preset resolve plan-template
$SPECIFY_CMD preset resolve tasks-template
```

Las cuatro deben indicar `software-humano` como capa de mayor precedencia.

#### 4.2 · Comandos

```bash
for c in constitution specify clarify plan tasks analyze implement converge; do
    $SPECIFY_CMD preset resolve "speckit.$c"
done
```

Cada uno debe mostrar una cadena de composición con, como mínimo:

1. `[base] core (bundled)` — el comando nativo de SpecKit;
2. `[wrap] software-humano` — la capa doctrinal.

#### 4.3 · El checklist debe seguir nativo

```bash
$SPECIFY_CMD preset resolve checklist-template
$SPECIFY_CMD preset resolve speckit.checklist
```

Ninguno debe mostrar `software-humano` como contribuyente.

#### 4.4 · Estado de la integración: qué esperar realmente

Tras instalar el preset, `integration status` reportará:

```json
{ "status": "warning", "modified_managed_files": 8 }
```

**Esto es el resultado esperado y es evidencia positiva, no una anomalía.** La causa: `init` escribió el contenido core de los comandos y registró sus hashes en el manifiesto de la integración; `preset add` recompuso esos ocho archivos con el `wrap` sin actualizar el manifiesto.

La verificación correcta no es que no haya `warning`, sino **qué archivos aparecen**:

```bash
$SPECIFY_CMD integration status --json \
  | python3 -c "import json,sys; print('\n'.join(json.load(sys.stdin)['manifests']['claude']['modified_files']))"
```

La lista debe contener **exactamente los ocho comandos adaptados**, y **no** debe incluir `checklist` ni `taskstoissues`. Si aparece alguno de esos dos, el preset excedió su alcance declarado: **detente**.

Esta comprobación es más fuerte que verificar solo la presencia de los comandos, porque verifica también el límite.

#### 4.5 · Contenido efectivo recibido por la integración

Comprueba que los archivos de comandos de la integración contienen realmente la capa doctrinal, no solo el core:

```bash
$SPECIFY_CMD artifact info speckit.specify --json
```

### 5. Materialización controlada de la constitución

Instalar el preset **no basta** para considerar activo el manifiesto. Debes materializar la constitución mediante el comando registrado por la integración activa.

> **Antes de intentarlo: si ejecutaste `specify init` en esta misma sesión, el comando probablemente todavía no exista.** Muchos agentes cargan su catálogo de comandos al iniciar la sesión. Es habitual y esperado que la instalación requiera **dos sesiones**: una para instalar y verificar, otra —iniciada de nuevo en el mismo directorio— para la constitución. Comprueba que el comando está disponible antes de continuar, e informa a la persona de este paso intermedio en lugar de presentarlo como una falla.

Invoca el equivalente real de `speckit.constitution` para la integración activa —`/speckit-constitution` o `$speckit-constitution` según el agente— con esta instrucción exacta:

> Instala o restaura en `.specify/memory/constitution.md` la proyección aprobada del Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1 incluida en `constitution-template`. No resumas, reformules, contextualices ni enmiendes su doctrina. Conserva el mecanismo nativo de resolución, validación y reporte de impacto. Si la constitución existente contiene cambios humanos o una versión doctrinal distinta, no la sobrescribas: presenta la diferencia y solicita resolución.

Si tu entorno no permite invocar el comando registrado:

- **no copies la plantilla manualmente como sustituto silencioso**;
- informa que el preset quedó instalado pero el manifiesto todavía no está activo;
- entrega a la persona el comando exacto que debe ejecutar;
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

No declares válida una constitución resumida, parcialmente copiada o reconstruida desde el anexo.

#### 6.1 · El reporte de impacto: cuándo se retira

El comando de constitución antepone un reporte de impacto como comentario HTML. Es material temporal de revisión y **no constituye doctrina**.

**Consérvalo mientras dure la revisión humana. Retíralo antes del primer commit de la constitución.**

Con el reporte retirado dispones de la verificación más fuerte posible, que ninguna comprobación de identificadores iguala:

```bash
diff .specify/memory/constitution.md \
     .specify/presets/software-humano/templates/constitution-template.md
```

Sin diferencias, la constitución es byte a byte la proyección aprobada.

#### 6.2 · No modifiques la constancia de procedencia

Tras materializar la constitución, `.specify/memory/.constitution-template.json` quedará desactualizada: seguirá declarando el origen y el hash del andamiaje anterior.

**No la corrijas.** Pertenece al mecanismo `constitution-sync`, que este paquete no adopta. El CLI compara su campo `sha256` contra el hash del **contenido vivo** de `constitution.md`; mientras no coincidan, trata la constitución como documento redactado por una persona y **no la sobrescribe**. Actualizarla invertiría esa protección.

### 7. Comprobación de límites

Confirma que la integración no hizo ninguna de estas cosas:

- modificar el código central de SpecKit;
- sustituir el ciclo SDD nativo;
- instalar componentes distintos del preset;
- crear etapas, controles o artefactos metodológicos nuevos;
- imponer historias de usuario, prioridad, MVP, independencia o incrementalidad;
- alterar el fundamento de producto;
- modificar archivos de la aplicación;
- atribuir al agente aprobación humana.

```bash
git status --short
shasum -a 256 -c SHA256SUMS
```

Separa los cambios producidos por la integración de los que ya existían.

### 8. No ejecutar todavía el desarrollo del producto

No generes un ejemplo artificial ni ejecutes `speckit.specify` sobre un fundamento real como parte de esta instalación. El siguiente paso debe ser una instrucción humana separada que identifique el fundamento de producto autorizado.

Cuando llegue, la primera aplicación deberá ejecutar:

```text
specify → clarify, si corresponde → plan → tasks → analyze
```

Solo después de revisar esos resultados se autoriza `implement` y luego `converge`.

### 9. Qué esperar de `specify` y su checklist

Anticípalo para no interpretarlo como defecto.

El comando `specify` genera un checklist nativo de calidad de requisitos, que el preset **conserva sin modificar**. Dos de sus ítems no pueden aprobarse en ciertas situaciones legítimas:

| Ítem del checklist nativo | Cuándo no puede aprobarse |
|---|---|
| `No [NEEDS CLARIFICATION] markers remain` | Cuando el fundamento declara decisiones abiertas. La directiva del preset **obliga** a conservar los marcadores hasta que la autoridad los resuelva, y deja sin efecto el límite nativo de tres. |
| `No implementation details (languages, frameworks, APIs)` | Cuando el fundamento aprueba explícitamente una arquitectura técnica como decisión de producto. |

En esos casos, registra el motivo en las notas del checklist y continúa. **Un checklist sin aprobar por estas razones indica fidelidad a la fuente, no un defecto de la especificación.** Resolverlo conjeturando sería una infracción de `STOP04`.

## Condiciones de detención

Detente y solicita decisión humana si:

1. falta una ruta o no puede identificarse el proyecto correcto;
2. `preflight.sh` reporta un bloqueo;
3. SpecKit no está inicializado y no existe autorización para inicializarlo;
4. la versión de SpecKit es incompatible y no hay decisión sobre aislar o actualizar;
5. no hay un `python3` con PyYAML ni forma de anteponer el shim;
6. el checksum del ZIP no coincide;
7. `preset.yml` o un archivo declarado falta o fue modificado;
8. existe otra versión del preset instalada;
9. hay cambios preexistentes que se superponen con `.specify/` o la integración activa;
10. no existe una integración activa identificable, o no fue elegida por una persona;
11. una plantilla no resuelve desde el preset;
12. un comando no conserva el core en su cadena de composición;
13. `software-humano` aparece como contribuyente del checklist, o entre los archivos modificados de la integración;
14. la constitución existente fue modificada por una persona o contiene otra versión;
15. no puedes materializar o verificar la constitución completa;
16. completar el trabajo exigiría modificar el core, el manifiesto, el anexo o el paquete.

Una detención correcta indica: hecho observado, evidencia, impacto, decisión requerida y la acción que no se ejecutó.

## Formato obligatorio del informe final

### Estado

`LISTO`, `LISTO CON PENDIENTES` o `BLOQUEADO`.

### Entorno

- raíz del proyecto;
- versión de SpecKit y si es global o aislada;
- integración activa;
- versión y prioridad del preset;
- si se usó el shim de PyYAML.

### Verificaciones

| Comprobación | Evidencia | Resultado |
|---|---|---|
| Entorno (`preflight.sh`) | Bloqueos y avisos | Pasa / Falla |
| Integridad del paquete | `SHA256SUMS`, n/n | Pasa / Falla |
| Integridad del preset | SHA-256 observado | Pasa / Falla |
| Cuatro plantillas | Capa de origen resuelta | Pasa / Falla |
| Ocho comandos | Cadena core + wrap | Pasa / Falla |
| Checklist nativo | Ausencia del preset | Pasa / Falla |
| Alcance de la integración | Los 8 modificados son los 8 compuestos | Pasa / Falla |
| Constitución v2.1 | `diff` contra la proyección del preset | Pasa / Falla |
| Límites | Archivos realmente modificados | Pasa / Falla |

### Cambios realizados

Enumera únicamente archivos o directorios que realmente hayan cambiado.

### Pendientes y decisiones humanas

Cualquier excepción, incertidumbre o acción manual requerida. No ocultes pendientes bajo un estado exitoso.

### Próximo paso autorizado

Si todo pasa:

> La adaptación Software Humano está instalada y el núcleo v2.1 está activo. El proyecto está preparado para recibir una definición de producto autorizada mediante `speckit.specify`. No se ha iniciado todavía el desarrollo del producto.

## Definición de terminado

No declares completada la integración porque `preset add` terminó sin errores. Está terminada únicamente cuando instalación, resolución, composición, alcance, registro, materialización, contenido de la constitución y límites hayan sido comprobados con evidencia.
