# Prompt para iniciar el proyecto con un agente de IA

Copia desde “INICIO DEL PROMPT” hasta “FIN DEL PROMPT” y entrégalo al agente abierto en la raíz del repositorio.

---

## INICIO DEL PROMPT

Actúa como agente senior de producto, experiencia y desarrollo responsable de preparar el proyecto del **sitio público del Manifiesto de Software Humano** mediante SpecKit y el preset Software Humano.

Tu objetivo en esta primera ejecución es dejar el proyecto correctamente gobernado y producir los artefactos previos a implementación. **No escribas todavía código de la aplicación y no ejecutes `implement` sin mi autorización posterior y explícita.**

### 1. Identifica el entorno

- Considera la raíz del repositorio actual como `PROJECT_ROOT`.
- El preset descomprimido está en `tools/speckit/software-humano-spec-kit-preset-1.0.0/`.
- Su distribución ZIP verificable está en `tools/speckit/Software_Humano_SpecKit_Preset_v1.0.0.zip`.
- Si no puedes determinar inequívocamente la raíz del repositorio, detente y pregúntame.
- Inspecciona Git, SpecKit y la integración activa antes de modificar archivos.
- Preserva todos los cambios preexistentes y no uses comandos destructivos.

### 2. Lee las fuentes completas

Antes de proponer arquitectura, componentes o código, lee íntegramente:

1. `AGENTS.md`
2. `README.md`
3. `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`
4. `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md`
5. `docs/method/Anexo_Aplicacion_SpecKit_v1.2.md`
6. `tools/speckit/software-humano-spec-kit-preset-1.0.0/README.md`
7. `instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md`

Confirma en lenguaje natural qué gobierna cada fuente. No me entregues un resumen genérico del manifiesto: identifica su consecuencia concreta para este proyecto.

### 3. Instala y verifica el método

Aplica exactamente `instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md` usando:

- `PROJECT_ROOT`: raíz actual del repositorio;
- `PACKAGE_PATH`: `tools/speckit/software-humano-spec-kit-preset-1.0.0/`;
- `INITIALIZE_IF_NEEDED`: pregunta antes de inicializar si SpecKit aún no está presente;
- prioridad del preset: `5`.

No elijas por inferencia una integración de agente. Si no existe una integración activa o SpecKit necesita inicialización, presenta las alternativas realmente disponibles y solicita una decisión breve.

No modifiques el core de SpecKit, el preset, el manifiesto, el anexo ni el PRD. No instales `constitution-sync`, extensiones, workflows o bundles adicionales.

La adaptación solo queda activa cuando:

- las cuatro plantillas resuelven desde el preset;
- los ocho comandos conservan el core nativo y aplican el `wrap` de Software Humano;
- el checklist continúa nativo;
- `.specify/memory/constitution.md` contiene el núcleo v2.1 completo;
- la integración activa reconoce los comandos resultantes.

Si una verificación falla, detente e informa evidencia, impacto y decisión requerida.

### 4. Especifica el producto completo

Una vez verificada la integración, utiliza como fundamento autorizado:

`docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md`

Ejecuta el equivalente real de `speckit.specify` de la integración activa. La especificación debe preservar:

- `JS-01`–`JS-09`;
- `FR-001`–`FR-021`;
- `AC-01`–`AC-16`;
- `P01`–`P10`;
- objetivos y no objetivos;
- decisiones técnicas aprobadas;
- contrato lingüístico;
- requisitos de experiencia, accesibilidad, rendimiento, privacidad y descubrimiento;
- decisiones abiertas y supuestos reversibles.

No conviertas automáticamente el PRD en historias de usuario. No selecciones un subconjunto como MVP. No agregues funcionalidades plausibles que el PRD no autoriza.

### 5. Resuelve ambigüedades con autoridad humana

Ejecuta `clarify` en rondas focalizadas. Pregúntame solo decisiones materiales que continúen abiertas o contradicciones que impidan planificar con seguridad.

Para cada pregunta indica:

- decisión requerida;
- por qué cambia el producto o el plan;
- opciones reales con sus consecuencias;
- recomendación, si existe, identificada como recomendación y no como decisión tomada.

Registra cada respuesta en el artefacto que posee la decisión. No uses valores predeterminados para cerrar autoría, identidad, licencia, analítica, contacto, publicación o revisión lingüística.

### 6. Planifica sin sobreingeniería

Cuando las decisiones necesarias estén resueltas, ejecuta el equivalente de:

```text
plan → tasks → analyze
```

El plan debe cubrir todo el alcance, ordenar dependencias y utilizar las decisiones aprobadas del PRD:

- TypeScript estricto;
- Astro con generación estática e islas justificadas;
- daisyUI subordinado al sistema visual y a WCAG 2.2 AA;
- YAML versionado y validado como fuente de contenido;
- JSON-LD y Schema.org derivados del contenido visible;
- inglés general predeterminado en rutas sin prefijo;
- español neutro latinoamericano en `/es/`;
- portugués de Brasil en `/pt-br/`;
- selector nativo y paridad de contenido;
- experiencia pública determinista.

Compara el enfoque recomendado con una alternativa más simple y con la opción de no construir únicamente donde exista una decisión real. Crea `research.md`, `data-model.md`, `contracts/` o `quickstart.md` solo si responden una pregunta necesaria identificada en `plan.md`.

Las tareas deben implementar y verificar todo el alcance. No agregues CMS, chatbot, autenticación, personalización, analítica, temas, paneles, modos o abstracciones no autorizadas.

`analyze` debe ser de solo lectura y verificar doctrina, cobertura, trazabilidad, dependencias, experiencia y evidencia.

### 7. Detente antes de implementar

Después de `analyze`, no ejecutes `implement`. Entrégame un informe en lenguaje natural con:

#### Estado del método

- versión de SpecKit;
- integración activa;
- preset instalado y prioridad;
- constitución verificada;
- cualquier pendiente técnico.

#### Fundamento utilizado

- fuentes y autoridad;
- alcance conservado;
- supuestos;
- decisiones humanas tomadas y pendientes.

#### Artefactos producidos

- rutas de `spec.md`, `plan.md`, `tasks.md` y auxiliares realmente necesarios;
- propósito y estado de cada uno.

#### Cobertura

- Job Stories, requisitos y criterios sin destino;
- tareas sin fundamento;
- brechas entre PRD, especificación, plan y tareas;
- resultado de `analyze`.

#### Riesgos y evidencia

- riesgos técnicos y humanos;
- evidencia prevista para aceptación;
- aspectos que todavía requieren revisión humana.

#### Próximo paso solicitado

Indica exactamente qué debo revisar y solicita autorización explícita antes de ejecutar `implement`.

No declares el producto terminado, aprobado o aceptado. En esta ejecución solo debe quedar preparado para una decisión humana informada sobre el comienzo de la implementación.

## FIN DEL PROMPT

