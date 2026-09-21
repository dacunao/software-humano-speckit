# Sitio del Manifiesto de Software Humano — paquete de inicio

**Versión del paquete:** 1.0.0  
**Fecha:** 2026-09-21  
**Producto:** sitio público del Manifiesto de Software Humano  
**Autoridad de producto:** Damián Acuña

## Para qué sirve

Este paquete permite iniciar el proyecto con un agente de IA sin separar la implementación del fundamento que debe gobernarla. Reúne en una sola estructura:

- el núcleo completo del Manifiesto de Software Humano v2.1;
- el anexo que lo aplica a SpecKit v1.2;
- el preset Software Humano para SpecKit v1.0.0;
- el PRD vigente del sitio;
- las instrucciones para instalar y verificar la adaptación;
- un prompt de arranque listo para entregar al agente;
- instrucciones persistentes en `AGENTS.md`.

El paquete prepara el proyecto. No contiene todavía la aplicación ni autoriza al agente a comenzar a programar antes de especificar, aclarar, planificar y revisar.

## Empieza aquí

1. Descomprime este paquete en la raíz del repositorio que utilizarás para el sitio.
2. Abre el repositorio con el agente de IA elegido.
3. Entrégale íntegramente el contenido de [`START_WITH_AI_AGENT.md`](START_WITH_AI_AGENT.md).
4. Permite que inspeccione el entorno antes de modificarlo.
5. Responde las decisiones humanas que aparezcan durante `clarify`.
6. Revisa en lenguaje natural `spec.md`, `plan.md`, `tasks.md` y el informe de `analyze`.
7. Autoriza `implement` únicamente cuando esos artefactos sean coherentes, completos y no tengan decisiones materiales abiertas.

Si el agente reconoce `AGENTS.md`, cargará automáticamente las reglas persistentes. Si no lo reconoce, el prompt de arranque le ordena leerlo de forma explícita.

## Orden de lectura y autoridad

Los documentos cumplen funciones diferentes; ninguno debe absorber el papel de otro.

| Orden | Fuente | Qué gobierna |
|---:|---|---|
| 1 | [`docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`](docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md) | Cómo se concibe, decide, implementa y verifica software humano. |
| 2 | [`docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md`](docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md) | Qué debe construirse para este sitio, con qué alcance y qué evidencia permite aceptarlo. |
| 3 | [`docs/method/Anexo_Aplicacion_SpecKit_v1.2.md`](docs/method/Anexo_Aplicacion_SpecKit_v1.2.md) | Cómo se corresponde el núcleo con los mecanismos nativos de SpecKit. |
| 4 | [`tools/speckit/software-humano-spec-kit-preset-1.0.0/`](tools/speckit/software-humano-spec-kit-preset-1.0.0/) | Cómo se materializa técnicamente la adaptación. |
| 5 | SpecKit nativo | El ciclo SDD y todo comportamiento que el preset no modifique. |

El núcleo y el PRD no compiten: el núcleo gobierna el método y los criterios; el PRD gobierna el producto. Ante una contradicción real o aparente, el agente debe identificarla y detener la decisión afectada, no inventar una conciliación.

## Contenido del paquete

```text
software-humano-manifesto-site-starter-v1.0.0/
├── README.md
├── AGENTS.md
├── START_WITH_AI_AGENT.md
├── SHA256SUMS
├── docs/
│   ├── method/
│   │   ├── Manifiesto_Software_Humano_IA_Nucleo_v2.1.md
│   │   └── Anexo_Aplicacion_SpecKit_v1.2.md
│   └── product/
│       └── PRD_Sitio_Manifiesto_Software_Humano_v1.0.md
├── instructions/
│   └── 01_INSTALAR_Y_VERIFICAR_SPECKIT.md
└── tools/
    └── speckit/
        ├── Software_Humano_SpecKit_Preset_v1.0.0.zip
        └── software-humano-spec-kit-preset-1.0.0/
```

El directorio y el ZIP del preset representan la misma versión. El directorio facilita inspección e instalación local; el ZIP conserva la distribución verificable cuyo SHA-256 esperado está declarado en la instrucción de instalación.

## Requisitos previos

- Un repositorio Git identificado y bajo control del usuario.
- SpecKit compatible con `>=1.0.0,<2.0.0`.
- Una integración de agente soportada y elegida por el usuario.
- Permiso para inicializar SpecKit si el repositorio aún no contiene `.specify/`.
- Capacidad del agente para ejecutar comandos, leer Markdown y presentar resultados en lenguaje natural.

No se requiere un CMS para comenzar. El PRD establece YAML versionado en GitHub como fuente de contenido para la versión 1.0.

## Flujo autorizado

El paquete conserva el flujo nativo de SpecKit:

1. `constitution`: instala o verifica el núcleo v2.1.
2. `specify`: deriva la especificación desde el PRD completo.
3. `clarify`: resuelve decisiones materiales sin adivinarlas.
4. `plan`: define la estrategia técnica y las dependencias.
5. `tasks`: deriva trabajo para todo el alcance autorizado.
6. `analyze`: comprueba doctrina, cobertura y trazabilidad.
7. Revisión humana de los artefactos escritos.
8. `implement`: solo después de autorización explícita.
9. `converge`: reconcilia implementación, alcance y evidencia.

Una ejecución parcial es avance, no una reducción del alcance. El agente no puede inventar prioridades, MVP, releases, exclusiones o aceptación.

## Decisiones de producto ya aprobadas

El agente debe preservarlas al especificar y planificar:

- TypeScript estricto como lenguaje fuente.
- Astro con generación estática y JavaScript de cliente selectivo.
- daisyUI como biblioteca base subordinada a la identidad y accesibilidad del producto.
- YAML versionado en GitHub como fuente de contenido.
- Schema.org y JSON-LD donde correspondan al contenido visible.
- Inglés general como idioma predeterminado en rutas sin prefijo.
- Español neutro latinoamericano en `/es/`, sin voseo ni `vosotros`.
- Portugués de Brasil en `/pt-br/`, con metadatos `pt-BR`.
- Selector de idioma nativo y rutas localizadas equivalentes.
- Experiencia pública determinista en la versión 1.0.

Las decisiones todavía abiertas están identificadas en la sección 29 del PRD. Deben resolverse por autoridad humana; su presencia no autoriza al agente a elegir valores predeterminados.

## Primer punto de control humano

Antes de programar, el agente debe entregar:

- estado de instalación y activación del preset;
- versión y contenido verificado de la constitución;
- fuente y autoridad utilizadas;
- especificación completa derivada del PRD;
- decisiones resueltas y todavía pendientes;
- plan, tareas y matriz de cobertura;
- resultado de `analyze` separado en hechos, inferencias y decisiones humanas;
- propuesta explícita del siguiente paso.

No autorices implementación si se perdió una Job Story, un requisito, un criterio de aceptación, un idioma, un principio o una decisión material continúa abierta.

## Integridad y licencias

`SHA256SUMS` permite verificar los archivos del paquete. El preset conserva su licencia propietaria en su propio directorio. Este paquete no concede una licencia adicional sobre el manifiesto, el PRD, SpecKit ni software de terceros.

## Qué significa estar listo para desarrollar

El proyecto está listo cuando:

- SpecKit está inicializado con la integración elegida;
- el preset está instalado y resuelve sus cuatro plantillas y ocho comandos;
- la constitución v2.1 completa está materializada;
- el PRD fue utilizado como fuente autorizada;
- las decisiones materiales necesarias para planificar están resueltas;
- `spec.md`, `plan.md`, `tasks.md` y `analyze` conservan todo el alcance;
- una persona revisó los artefactos y autorizó comenzar `implement`.

Instalar el preset o generar código no basta para declarar que el proyecto está preparado.
