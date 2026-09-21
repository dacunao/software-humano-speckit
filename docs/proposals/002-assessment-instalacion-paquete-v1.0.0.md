# Assessment 002 — Instalación del paquete Software Humano v1.0.0

**Fecha:** 2026-09-21
**Estado:** análisis para decisión de la autoridad del paquete
**Objeto evaluado:** `software-humano-manifesto-site-starter-v1.0.0` y el preset `software-humano` v1.0.0
**Base de evidencia:** una instalación completa y verificada, ejecutada en macOS 15.6 con SpecKit 1.0.8 e integración Claude Code
**Alcance:** qué debe cambiar para que la próxima instalación sea fluida y sin observaciones. No propone cambios al núcleo v2.1 ni al PRD.

## Resumen

La instalación **funcionó y quedó verificada**, pero no fue fluida. Requirió siete intervenciones de juicio que un operador menos experto no habría resuelto, y cuatro de ellas eran evitables con cambios en la documentación, no en el código.

El preset en sí es sólido: su composición, su protección del checklist nativo y su proyección de la constitución se comportaron exactamente como prometen. Los problemas están casi todos en la **capa de instalación y sus requisitos previos**, no en la doctrina ni en la adaptación.

| Categoría | Cantidad | Gravedad |
|---|---:|---|
| Bloqueos reales que detuvieron el trabajo | 4 | Alta |
| Señales que pueden leerse como falsa detención | 2 | Alta |
| Defectos menores del paquete | 3 | Baja |
| Mecanismos que funcionaron sin fricción | 8 | — confirmar |

---

## Parte 1 — Lo que funcionó y no debe tocarse

Estos mecanismos se comportaron correctamente y sostuvieron la verificación. Cambiarlos introduciría riesgo sin beneficio.

**1.1 · Integridad por `SHA256SUMS`.** Verificó 25/25 archivos y **sobrevivió a mover el paquete completo** de una subcarpeta a la raíz del repositorio, porque usa rutas relativas. Fue la evidencia que permitió demostrar, en cada paso, que ningún archivo rector había sido tocado. Es el mejor componente del paquete.

**1.2 · Checksum del ZIP.** `d698aebd…1db1b3` coincidió exactamente con `EXPECTED_SHA256`. La instrucción acierta al ponerlo antes de instalar.

**1.3 · Composición `wrap`.** Los ocho comandos mostraron la cadena `1. [base] core (bundled)` → `2. [wrap] software-humano v1.0.0`. El core nativo permanece íntegro y la capa doctrinal se agrega encima. Funcionó sin excepción.

**1.4 · Protección del checklist nativo.** `checklist-template` y `speckit.checklist` resolvieron desde `core` con cero contribución del preset. La decisión de no intervenirlo es correcta y verificable en un comando.

**1.5 · `constitution-template` completa.** 82.576 bytes, versión 2.1, las quince familias de identificadores, cero marcadores sin resolver. La proyección se instaló byte a byte sin pérdida doctrinal.

**1.6 · `spec-template` cumplió su promesa central.** Permitió representar un PRD de 74 KB con 9 Job Stories, 21 requisitos y 16 criterios **sin convertirlo en historias de usuario y sin inventar prioridades**. Las secciones "Fuente y autoridad", "Estructura de producto preservada" y "Cobertura del alcance" son las que hacen posible esa fidelidad. Son el núcleo del valor del preset.

**1.7 · La anulación del límite de marcadores fue decisiva.** La directiva del wrap —"Deja sin efecto cualquier límite numérico del comando nativo que obligue a ocultar marcadores materiales o a reemplazarlos por conjeturas"— evitó que el límite nativo de tres `NEEDS CLARIFICATION` ocultara ocho decisiones abiertas del PRD. Sin esa cláusula, la especificación habría cerrado por conjetura decisiones sobre licencia, autoría y analítica. **Es la cláusula más valiosa del preset.**

**1.8 · Las condiciones de detención de `AGENTS.md` son accionables.** Se activaron correctamente cuatro veces y en cada caso indicaban qué evidencia presentar y qué decisión pedir.

---

## Parte 2 — Bloqueos reales

### `H-01` · PyYAML no está declarado como requisito y rompe la resolución de plantillas

**Gravedad: alta. Es el problema más importante del paquete.**

**Hecho.** `.specify/scripts/bash/common.sh` usa el primer `python3` del `PATH`. En macOS con Homebrew, ese intérprete no trae PyYAML. La resolución de cualquier plantilla compuesta falla:

```
Error: PyYAML is required to resolve preset template composition
ERROR: Could not resolve required spec-template from the template override stack
```

**Evidencia.** `/opt/homebrew/bin/python3` (3.14.7) → `ModuleNotFoundError: No module named 'yaml'`. `/usr/bin/python3` (3.9.6) → `PyYAML 6.0.3`.

**Impacto.** Bloquea `specify`, `plan` y `tasks`, es decir todo el ciclo posterior a la instalación. El mensaje de error no dice qué hacer. La solución obvia está cerrada: `pip install --user pyyaml` sobre el Python de Homebrew lo rechaza PEP 668, y forzarlo con `--break-system-packages` produce la advertencia "can result in a broken Homebrew installation".

**Por qué importa para la reutilización.** Afecta a cualquier proyecto que instale este preset en un macOS con Homebrew, que es una configuración muy común. No es específico de este repositorio.

**Ajuste propuesto.**

1. Agregar a "Requisitos previos" del `README.md`: *un `python3` en el `PATH` con PyYAML disponible*.
2. Agregar al paso 1 de la instrucción una comprobación previa, antes de instalar:

   ```bash
   python3 -c 'import yaml; print("PyYAML", yaml.__version__)'
   ```

   Si falla, detenerse e informar, con las tres salidas reales: usar un intérprete que sí lo tenga, instalarlo en un entorno no gestionado, o anteponer un shim al `PATH`.
3. Incluir en el paquete un shim de referencia reutilizable, equivalente a `tools/speckit/shim/python3` de este repositorio, con su explicación.

### `H-02` · El rango de versión de SpecKit se detecta pero no se resuelve

**Gravedad: alta.**

**Hecho.** El preset exige `>=1.0.0,<2.0.0`. La instalación global del usuario era **0.15.0**, fuera de rango. La instrucción tiene la condición de detención número 3 para este caso, pero no ofrece ninguna ruta de salida.

**Evidencia.** `specify --version` → `0.15.0`. `specify self check` → `Update available: 0.15.0 → v1.0.8`.

**Agravante.** El usuario tenía **tres proyectos SpecKit activos**, los tres con `"speckit_version": "0.15.0"` en su `.specify/`. Actualizar el CLI global habría puesto una versión mayor delante de proyectos en curso, sin evidencia de compatibilidad.

**Impacto.** El operador queda detenido ante una decisión no trivial que la instrucción no anticipa: actualizar globalmente y arriesgar otros proyectos, o no instalar.

**Ajuste propuesto.** Agregar a la instrucción una sección "Cuando la versión instalada está fuera de rango" con las dos salidas reales y su consecuencia:

- **Instancia aislada por proyecto**, que no toca la instalación global:

  ```bash
  uvx --from git+https://github.com/github/spec-kit.git@v1.0.8 specify <subcomando>
  ```

  Recomendada cuando existen otros proyectos con una versión distinta. SpecKit ya fija la versión por proyecto en `.specify/init-options.json`, de modo que el aislamiento es coherente con su propio diseño.
- **Actualización global**, cuando no hay otros proyectos o se decide migrarlos juntos.

Conviene además envolver el comando en un script versionado dentro del repositorio, como `tools/speckit/specify`, para que la versión quede fijada y auditable.

### `H-03` · `init --here` exige `--force`, que la instrucción prohíbe

**Gravedad: alta. Es una contradicción interna del documento.**

**Hecho.** El paso 1 de la instrucción dice literalmente: *"No uses `--force`, no borres configuraciones existentes y no limpies cambios ajenos."* Pero como el paquete se descomprime en la raíz del repositorio, el directorio nunca está vacío, y en una sesión no interactiva el `init` falla:

```
Warning: Current directory is not empty (12 items)
Error: Current directory is not empty and no confirmation input is available.
Re-run with --force to merge into it.
```

**Impacto.** Un agente que obedezca la prohibición literal no puede completar la instalación. Uno que use `--force` viola la instrucción escrita. Ambos caminos son incorrectos tal como está redactada.

**Análisis.** `--force` significa dos cosas distintas según el comando. En `init --here` solo omite la confirmación de un *merge*. En `preset add` sí implica sobrescritura. La prohibición es correcta para el segundo caso y equivocada para el primero.

**Ajuste propuesto.** Reescribir la prohibición distinguiendo ambos usos:

> No uses `--force` en `specify preset add`: implica sobrescribir una instalación existente.
> En `specify init --here`, `--force` únicamente omite la confirmación interactiva de un merge y es necesario en sesiones no interactivas. Antes de usarlo, establece un commit base que permita detectar y revertir cualquier sobrescritura, y verifica después con `git status --short` y `shasum -a 256 -c SHA256SUMS`.

### `H-04` · Los comandos de la integración no existen en la sesión que los instala

**Gravedad: alta para agentes; media para uso manual.**

**Hecho.** `specify init --integration claude` registra los comandos como skills en `.claude/skills/`. Claude Code carga su catálogo de skills **al iniciar la sesión**. En la sesión que ejecuta el `init`, invocar el comando falla:

```
Skill(speckit-constitution) → Unknown skill: speckit-constitution
```

**Impacto.** El paso 5 de la instrucción —materializar la constitución— no puede ejecutarse en la misma sesión que instaló el preset. La instrucción contempla el caso genérico ("Si tu entorno no permite invocar el comando registrado") pero no anticipa esta causa concreta, que es la más probable y ocurre siempre en una instalación desde cero.

**Consecuencia observada.** La instalación requirió **dos sesiones**: una para instalar y verificar, otra para materializar la constitución. Eso es correcto, pero nadie lo advirtió de antemano.

**Ajuste propuesto.** Agregar una nota al inicio del paso 5:

> Si ejecutaste `specify init` en esta misma sesión, los comandos de la integración probablemente todavía no estén cargados: muchos agentes leen su catálogo al iniciar. Inicia una sesión nueva en el mismo directorio antes de continuar. Verifica que el comando esté disponible **antes** de intentar materializar la constitución; no copies la plantilla manualmente como sustituto.

---

## Parte 3 — Señales que pueden leerse como falsa detención

### `H-05` · Tras instalar el preset, `integration status` reporta `warning` con 8 archivos modificados

**Gravedad: alta, por riesgo de interpretación errónea.**

**Hecho.** Después de `preset add`, el estado de la integración es:

```json
{ "status": "warning", "modified_managed_files": 8 }
```

Los ocho archivos son exactamente los comandos que el preset envuelve. `speckit-checklist` y `speckit-taskstoissues`, los dos que el preset no toca, **no** aparecen.

**Análisis.** La causa es esperada: `init` escribió el contenido core y registró sus hashes en `claude.manifest.json`; `preset add` recompuso esos ocho archivos con el wrap sin actualizar el manifiesto. El `warning` es, en realidad, **evidencia positiva de que el preset se aplicó correctamente y de que respetó exactamente su alcance declarado**.

**Riesgo.** La condición de detención número 7 de la instrucción dice: *"hay cambios preexistentes que se superponen con `.specify/` o la integración activa"*. Un operador que ejecute `integration status` después de instalar puede leer ese `warning` como esa condición y detenerse sin motivo.

**Ajuste propuesto.** Convertir esto en una verificación positiva del paso 4, en lugar de dejarlo como una señal ambigua:

> Tras instalar el preset, `specify integration status --json` reportará `status: "warning"` con `modified_managed_files` igual al número de comandos compuestos (8). **Esto es el resultado esperado**, no una anomalía: el preset recompuso esos comandos después de que `init` registrara la versión core.
> Comprueba que la lista de `modified_files` contenga exactamente los ocho comandos adaptados y **no** incluya `checklist` ni `taskstoissues`. Si aparece alguno de esos dos, el preset excedió su alcance: detente.

Esta comprobación es mejor que la que la instrucción prescribe hoy, porque verifica alcance y no solo presencia.

### `H-06` · El checklist nativo contiene ítems que el propio wrap vuelve imposibles de aprobar

**Gravedad: media. Es un conflicto de diseño, no un error.**

**Hecho.** El preset conserva deliberadamente el checklist nativo de requisitos y su directiva dice: *"Conserva el checklist nativo de calidad de requisitos. No crees otro checklist propio del manifiesto."* Pero ese checklist incluye dos ítems que la doctrina impide satisfacer:

| Ítem del checklist nativo | Conflicto |
|---|---|
| `No [NEEDS CLARIFICATION] markers remain` | El wrap **obliga** a conservarlos hasta que la autoridad los resuelva. Con un PRD que declara diez decisiones abiertas, el ítem no puede aprobarse al especificar. |
| `No implementation details (languages, frameworks, APIs)` | El PRD §24.6 aprueba TypeScript, Astro y daisyUI como **decisiones de producto** que `AGENTS.md` obliga a preservar, y `AC-16` nombra TypeScript en un criterio de aceptación. |

**Consecuencia observada.** El checklist quedó con dos ítems sin aprobar y hubo que documentar por qué el resultado correcto es precisamente ese. Un operador sin ese contexto concluiría que la especificación está defectuosa.

**Análisis.** No conviene modificar el checklist nativo: conservarlo intacto es una decisión correcta del anexo. El problema es de documentación.

**Ajuste propuesto.** Agregar a la directiva de `specify` en el preset una frase que resuelva la lectura:

> El checklist nativo se conserva sin modificar. Dos de sus ítems no pueden aprobarse mientras existan decisiones materiales abiertas o cuando el fundamento de producto apruebe explícitamente una arquitectura técnica. En esos casos, registra el motivo en las notas del checklist y continúa: un checklist sin aprobar por esta razón indica fidelidad a la fuente, no un defecto de la especificación.

---

## Parte 4 — Defectos menores del paquete

### `H-07` · Ancla `sh-pocket` huérfana

Registrado en detalle en [`001-ancla-sh-pocket-preset.md`](001-ancla-sh-pocket-preset.md). En `constitution-template.md`, la sección `GUÍA DE BOLSILLO · SH-POCKET` está en la línea 889 y su ancla `<a id="sh-pocket"></a>` en la 1034. Un enlace a `#sh-pocket` lleva al final del documento. Sin efecto doctrinal.

### `H-08` · Discrepancia de fechas entre el paquete y la constitución

**Hecho.** `README.md` y el `CHANGELOG.md` del preset declaran **2026-09-21**. El pie de la constitución declara **Ratified: 2026-09-20 | Last Amended: 2026-09-20**.

**Impacto.** Ninguno funcional; el paso 6 de la instrucción solo exige "fechas ISO" y ambas lo son. Pero `FR-012` del PRD exige que el visitante pueda identificar la fecha de actualización del núcleo, y el sitio publicará una de las dos.

**Ajuste propuesto.** Confirmar cuál es la fecha de ratificación correcta del núcleo v2.1 y alinearla, o documentar que la ratificación precede deliberadamente al empaquetado.

### `H-09` · La instalación copia lo que haya en el directorio, incluida basura del sistema de archivos

**Hecho.** `preset add --dev` hace una **copia real** del directorio, no un enlace simbólico. Eso es bueno —el preset instalado queda autocontenido y no depende del origen— pero también copió un `.DS_Store` generado por macOS a `.specify/presets/software-humano/`.

**Ajuste propuesto.** Agregar al paso 3 de la instrucción una limpieza previa, y recordar que `--dev` produce una copia:

```bash
find "[PRESET_DIR]" -name '.DS_Store' -delete
```

---

## Parte 5 — Correcciones a supuestos que resultaron falsos

Dos observaciones que parecían defectos y **no lo son**. Conviene registrarlas para que no se "corrijan" por error.

**`H-10` · `preset.yml` declara los ocho comandos bajo la clave `provides.templates:`.** Parece un error de esquema. No lo es: el CLI clasifica por el campo `type` de cada entrada, y `preset list --json` reporta correctamente `{"commands": 8, "templates": 4, "scripts": 0}`. **No cambiar.** Como mucho, un comentario en el archivo que explique que la clave es un artefacto del esquema 1.0.

**`H-11` · `specify preset list --json` falla.** Solo en 0.15.0 (`No such option: --json`). En 1.0.8 funciona y devuelve JSON válido. La instrucción es correcta; el fallo **confirma** la necesidad del rango de versión en lugar de contradecirla. Conviene mencionarlo como síntoma diagnóstico: si `--json` no existe, la versión está fuera de rango.

Nota menor: `specify artifact info --json` requiere un argumento `name` (por ejemplo `specify artifact info speckit.specify --json`). La instrucción lo menciona sin el argumento.

---

## Parte 6 — Un vacío no cubierto por la instrucción

### `H-12` · `.constitution-template.json` no se menciona y su comportamiento es contraintuitivo

**Hecho.** `specify init` crea `.specify/memory/.constitution-template.json` con el sha y el origen de la constitución generada. Tras materializar el núcleo v2.1, esa constancia queda desactualizada: sigue declarando `source: "core"` y el sha del andamiaje anterior.

**Por qué importa.** El primer impulso es corregirla. **Sería un error.** `_constitution_is_generated()` del CLI compara ese sha contra el sha del **contenido vivo** de `constitution.md`. Mientras no coincidan, el CLI trata la constitución como redactada por una persona y **no la sobrescribe**. Actualizar la constancia invertiría la protección.

Además, todo ese mecanismo pertenece a `constitution-sync`, que el README del preset prohíbe expresamente adoptar.

**Ajuste propuesto.** Agregar una nota al paso 6 de la instrucción:

> Tras materializar la constitución, `.specify/memory/.constitution-template.json` quedará desactualizada. **No la modifiques.** Es la constancia del modelo `constitution-sync`, que este paquete no adopta. Su desajuste hace que el CLI trate la constitución como documento redactado por una persona y no la reemplace, que es el comportamiento deseado.

### `H-13` · El reporte de impacto no tiene dueño ni momento de retiro

**Hecho.** El comando de constitución antepone un reporte de impacto como comentario HTML. El paso 6 dice que "puede permanecer durante la revisión" y el anexo dice que "no pasa a formar parte de la doctrina". Ninguno dice quién lo retira ni cuándo.

**Consecuencia observada.** Quedó en el archivo y hubo que decidir su destino en una sesión posterior. Mientras está presente, `constitution.md` no es byte a byte idéntica a la proyección del preset, lo que complica la verificación.

**Ajuste propuesto.** Fijar la regla en el paso 6:

> Conserva el reporte de impacto mientras dure la revisión humana. Retíralo antes del primer commit de la constitución. Con el reporte retirado, `constitution.md` debe ser byte a byte idéntica a la proyección del preset, y esa igualdad es la verificación más fuerte disponible:
>
> ```bash
> diff .specify/memory/constitution.md .specify/presets/software-humano/templates/constitution-template.md
> ```

---

## Parte 7 — Ajustes propuestos, por prioridad

| # | Ajuste | Dónde | Esfuerzo | Desbloquea |
|---|---|---|---|---|
| 1 | Declarar PyYAML como requisito previo, con comprobación y shim de referencia | `README.md`, instrucción paso 1, nuevo archivo en el paquete | Bajo | `H-01` |
| 2 | Documentar la instalación aislada de SpecKit cuando la versión global está fuera de rango | Instrucción, nueva sección | Bajo | `H-02` |
| 3 | Distinguir `--force` de `init` del `--force` de `preset add` | Instrucción paso 1 | Muy bajo | `H-03` |
| 4 | Advertir que los comandos de la integración requieren una sesión nueva | Instrucción paso 5 | Muy bajo | `H-04` |
| 5 | Reencuadrar `warning` + 8 modificados como verificación positiva de alcance | Instrucción paso 4 | Bajo | `H-05` |
| 6 | Explicar por qué dos ítems del checklist nativo no pueden aprobarse | Directiva de `specify` del preset | Bajo | `H-06` |
| 7 | Fijar cuándo se retira el reporte de impacto y añadir el `diff` como verificación | Instrucción paso 6 | Muy bajo | `H-13` |
| 8 | Advertir que no se toque `.constitution-template.json` | Instrucción paso 6 | Muy bajo | `H-12` |
| 9 | Limpiar `.DS_Store` antes de `preset add` | Instrucción paso 3 | Muy bajo | `H-09` |
| 10 | Corregir el ancla `sh-pocket` | `constitution-template.md` del preset | Bajo | `H-07` |
| 11 | Alinear o explicar la discrepancia de fechas | Paquete | Muy bajo | `H-08` |

Los ajustes 1 a 9 son **solo documentación**: no tocan el preset, no rompen `SHA256SUMS` del contenido normativo y no requieren versionar el preset. Resuelven las cuatro detenciones reales y las dos señales ambiguas.

Los ajustes 10 y 11 sí modifican archivos del preset y exigen incremento de versión, entrada en el `CHANGELOG.md` y regeneración de `SHA256SUMS`. Conviene agruparlos en una única v1.0.1 en lugar de versionar dos veces.

## Alternativa más simple

No cambiar nada y documentar los siete rodeos en una guía de problemas conocidos.

No la recomiendo. Cuatro de los hallazgos **detienen** la instalación, no la incomodan, y tres de ellos se resuelven con un párrafo cada uno. Una guía de problemas conocidos traslada al operador un trabajo que el paquete puede absorber, que es exactamente lo que `P03` del propio manifiesto rechaza.

## Alternativa de no construir

Aplicable solo a los ajustes 10 y 11. El ancla huérfana y la discrepancia de fechas no afectan doctrina ni alcance, y versionar el preset tiene un costo real. Si no aparece otra razón para mover la versión, es defendible dejarlos como están. Los ajustes 1 a 9 no admiten esta alternativa: sin ellos, la próxima instalación vuelve a detenerse cuatro veces.

## Decisión requerida

De la autoridad del paquete:

1. ¿Se aplican los ajustes 1 a 9, que son solo documentación y no versionan el preset?
2. ¿Se agrupan los ajustes 10 y 11 en una v1.0.1 del preset, o se dejan registrados sin aplicar?
3. ¿Cuál es la fecha de ratificación correcta del núcleo v2.1: 2026-09-20 o 2026-09-21?
