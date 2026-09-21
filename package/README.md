# Software Humano para SpecKit — paquete de método

**Versión del paquete:** 1.1.0
**Fecha:** 2026-09-21
**Núcleo del manifiesto:** 2.1
**Anexo de aplicación SpecKit:** 1.2
**Preset Software Humano:** 1.0.1
**Autoridad:** Damián Acuña

## Qué es

Un paquete autocontenido que instala el **Manifiesto de Software Humano** como doctrina operativa dentro del ciclo SDD nativo de SpecKit, en cualquier proyecto.

Reúne en una sola estructura:

- el núcleo completo del manifiesto v2.1;
- el anexo que lo aplica a SpecKit v1.2;
- el preset instalable Software Humano v1.0.1;
- los requisitos de entorno, con comprobación ejecutable;
- las instrucciones de instalación y verificación;
- un prompt de arranque para entregar al agente;
- instrucciones persistentes en `AGENTS.md` y `CLAUDE.md`;
- utilidades que resuelven fricciones reales de instalación.

**No incluye un fundamento de producto.** Ese lo aporta cada proyecto. El paquete es el método; el PRD, las Job Stories o la definición que uses son tuyos.

El paquete prepara el proyecto. No contiene la aplicación ni autoriza al agente a programar antes de especificar, aclarar, planificar y revisar.

## Empieza aquí

1. Descomprime este paquete **en la raíz del repositorio** que usarás. No en una subcarpeta: si `SHA256SUMS` y `AGENTS.md` no quedan junto a `.git`, mueve el contenido.
2. Verifica la integridad:

   ```bash
   shasum -a 256 -c SHA256SUMS
   ```

3. Comprueba el entorno **antes de instalar nada**:

   ```bash
   tools/speckit/preflight.sh
   ```

4. Coloca tu fundamento de producto en `docs/product/` y completa la sección **Completar por proyecto** al final de `AGENTS.md`. La [plantilla de fundamento](docs/product/PLANTILLA_FUNDAMENTO_DE_PRODUCTO.md) explica qué debe contener.
5. Abre el repositorio con el agente elegido y entrégale el contenido de [`START_WITH_AI_AGENT.md`](START_WITH_AI_AGENT.md).
6. Permite que inspeccione el entorno antes de modificarlo.
7. Responde las decisiones humanas que aparezcan durante `clarify`.
8. Revisa en lenguaje natural `spec.md`, `plan.md`, `tasks.md` y el informe de `analyze`.
9. Autoriza `implement` únicamente cuando esos artefactos sean coherentes, completos y sin decisiones materiales abiertas.

Los agentes que reconocen `AGENTS.md` cargarán las reglas automáticamente. Claude Code carga `CLAUDE.md`, que referencia `AGENTS.md` sin duplicarlo.

## Cuenta con dos sesiones, no una

Las skills o comandos que registra `specify init` suelen cargarse al iniciar la sesión del agente. Por eso la instalación normalmente requiere:

- **Sesión 1**: comprobar entorno, inicializar SpecKit, instalar y verificar el preset.
- **Sesión 2**: materializar y verificar la constitución.

Es lo esperado. Está documentado en el requisito 5 de `instructions/00_REQUISITOS_DE_INSTALACION.md`.

## Orden de lectura y autoridad

Ningún documento debe absorber el papel de otro.

| Orden | Fuente | Qué gobierna |
|---:|---|---|
| 1 | [`docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`](docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md) | Cómo se concibe, decide, implementa y verifica software humano. |
| 2 | Tu fundamento de producto, en `docs/product/` | Qué debe construirse, con qué alcance y qué evidencia permite aceptarlo. |
| 3 | [`docs/method/Anexo_Aplicacion_SpecKit_v1.2.md`](docs/method/Anexo_Aplicacion_SpecKit_v1.2.md) | Cómo se corresponde el núcleo con los mecanismos nativos de SpecKit. |
| 4 | [`tools/speckit/software-humano-spec-kit-preset-1.0.1/`](tools/speckit/software-humano-spec-kit-preset-1.0.1/) | Cómo se materializa técnicamente la adaptación. |
| 5 | SpecKit nativo | El ciclo SDD y todo comportamiento que el preset no modifique. |

El núcleo y el fundamento no compiten: el núcleo gobierna el método; el fundamento gobierna el producto. Ante una contradicción real o aparente, el agente debe identificarla y detener la decisión afectada, no inventar una conciliación.

## Contenido

```text
├── README.md
├── AGENTS.md                         Reglas persistentes. Neutral de agente y de proyecto.
├── CLAUDE.md                         Referencia a AGENTS.md + lo específico de Claude Code.
├── START_WITH_AI_AGENT.md            Prompt de arranque.
├── SHA256SUMS
├── docs/
│   ├── method/
│   │   ├── Manifiesto_Software_Humano_IA_Nucleo_v2.1.md
│   │   └── Anexo_Aplicacion_SpecKit_v1.2.md
│   └── product/
│       └── PLANTILLA_FUNDAMENTO_DE_PRODUCTO.md
├── instructions/
│   ├── 00_REQUISITOS_DE_INSTALACION.md     Requisitos de entorno y checklist.
│   └── 01_INSTALAR_Y_VERIFICAR_SPECKIT.md  Procedimiento y verificación.
└── tools/
    └── speckit/
        ├── preflight.sh                    Comprueba el entorno. No modifica nada.
        ├── specify                         Envoltorio con versión de SpecKit fijada.
        ├── shim/python3                    Intérprete con PyYAML para los scripts.
        ├── Software_Humano_SpecKit_Preset_v1.0.1.zip
        └── software-humano-spec-kit-preset-1.0.1/
```

El directorio y el ZIP del preset son la misma versión. El directorio facilita inspección e instalación local; el ZIP conserva la distribución verificable.

## Requisitos previos

Comprobados todos por `tools/speckit/preflight.sh`:

- un repositorio Git con árbol limpio;
- SpecKit compatible con `>=1.0.0,<2.0.0`;
- **un `python3` en el `PATH` con PyYAML** — sin él, la resolución de plantillas falla;
- una integración de agente elegida por una persona;
- permiso para inicializar SpecKit si no existe `.specify/`;
- capacidad del agente para ejecutar comandos, leer Markdown y presentar resultados en lenguaje natural.

No se requiere un CMS ni ninguna tecnología concreta: el paquete no impone arquitectura. Esas decisiones pertenecen a tu fundamento de producto.

## Flujo autorizado

El paquete conserva el flujo nativo de SpecKit:

1. `constitution` — instala o verifica el núcleo v2.1.
2. `specify` — deriva la especificación desde el fundamento completo.
3. `clarify` — resuelve decisiones materiales sin adivinarlas.
4. `plan` — define la estrategia técnica y las dependencias.
5. `tasks` — deriva trabajo para todo el alcance autorizado.
6. `analyze` — comprueba doctrina, cobertura y trazabilidad.
7. Revisión humana de los artefactos escritos.
8. `implement` — solo después de autorización explícita.
9. `converge` — reconcilia implementación, alcance y evidencia.

Una ejecución parcial es avance, no una reducción del alcance. El agente no puede inventar prioridades, MVP, releases, exclusiones ni aceptación.

## Qué significa estar listo para desarrollar

- SpecKit está inicializado con la integración elegida;
- el preset resuelve sus cuatro plantillas y sus ocho comandos con la cadena core + wrap;
- el checklist nativo sigue sin intervenir;
- la constitución v2.1 completa está materializada y verificada;
- el fundamento de producto fue utilizado como fuente autorizada;
- las decisiones materiales necesarias para planificar están resueltas;
- `spec.md`, `plan.md`, `tasks.md` y `analyze` conservan todo el alcance;
- una persona revisó los artefactos y autorizó comenzar `implement`.

Instalar el preset o generar código no basta para declarar que el proyecto está preparado.

## Cambios de la versión 1.1.0

Esta versión **no modifica doctrina**. El núcleo v2.1 y el anexo v1.2 son idénticos a los de la versión 1.0.0. Los cambios corrigen la capa de instalación, a partir de una aplicación real completa que se detuvo cuatro veces por requisitos no declarados.

| Área | Cambio |
|---|---|
| Requisitos | Nuevo `00_REQUISITOS_DE_INSTALACION.md` con seis requisitos, remediación y checklist. |
| Comprobación | Nuevo `tools/speckit/preflight.sh`: verifica el entorno sin modificar nada. |
| PyYAML | Declarado como requisito; se incluye `tools/speckit/shim/python3`. Era el bloqueo más grave. |
| Versión de SpecKit | Nueva ruta de remediación con instancia aislada; se incluye `tools/speckit/specify`. |
| `--force` | Se distingue su uso en `init --here` (necesario) del de `preset add` (prohibido). La versión anterior los confundía y hacía la instalación imposible de completar al pie de la letra. |
| Sesiones | Se documenta que los comandos registrados suelen requerir una sesión nueva. |
| Estado de la integración | El `warning` con 8 archivos modificados se reencuadra como verificación positiva de alcance. |
| Checklist de `specify` | Se explica por qué dos de sus ítems no pueden aprobarse en situaciones legítimas. |
| Constitución | Se fija cuándo se retira el reporte de impacto y se añade el `diff` como verificación más fuerte. Se advierte no tocar `.constitution-template.json`. |
| `AGENTS.md` | Reescrito neutral de agente y de proyecto, con sección **Completar por proyecto**. |
| `CLAUDE.md` | Nuevo. Referencia `AGENTS.md` y añade solo lo específico de Claude Code. |
| Preset 1.0.1 | Corrige dos anclas desplazadas en la plantilla de constitución. Sin cambio doctrinal. |

## Integridad y licencias

`SHA256SUMS` permite verificar los archivos del paquete. Usa rutas relativas, de modo que sigue verificando si mueves el paquete completo.

El preset conserva su licencia propietaria en su propio directorio. Este paquete no concede una licencia adicional sobre el manifiesto, SpecKit ni software de terceros.

## Una nota sobre fechas

El núcleo v2.1 declara **ratificación el 2026-09-20**; el paquete se fecha el **2026-09-21**. La diferencia es deliberada: la doctrina se ratifica antes de empaquetarse. No es una inconsistencia que deba corregirse.
