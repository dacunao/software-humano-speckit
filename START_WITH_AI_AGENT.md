# Prompt para iniciar el proyecto con un agente de IA

Antes de entregar este prompt, completa la sección **Completar por proyecto** al final de `AGENTS.md`. Si está vacía, el agente se detendrá en el primer paso para pedírtela, que es el comportamiento correcto.

Copia desde "INICIO DEL PROMPT" hasta "FIN DEL PROMPT" y entrégalo al agente abierto en la raíz del repositorio.

---

## INICIO DEL PROMPT

Actúa como agente senior de producto, experiencia y desarrollo, responsable de preparar este proyecto mediante SpecKit y el preset Software Humano.

Tu objetivo en esta primera ejecución es dejar el proyecto correctamente gobernado y producir los artefactos previos a la implementación. **No escribas todavía código de la aplicación y no ejecutes `implement` sin mi autorización posterior y explícita.**

### 1. Comprueba el entorno antes de tocar nada

Ejecuta:

```bash
tools/speckit/preflight.sh
```

Aplica `instructions/00_REQUISITOS_DE_INSTALACION.md` y repórtame el resultado de su checklist de siete puntos con evidencia real, no con supuestos.

Si hay un bloqueo, detente e infórmame el hecho, la evidencia, el impacto, la decisión que necesito tomar y la acción que no ejecutaste. No lo rodees por iniciativa propia.

Considera la raíz del repositorio actual como `PROJECT_ROOT`. Si no puedes determinarla inequívocamente, detente y pregúntame. Preserva todos los cambios preexistentes y no uses comandos destructivos.

### 2. Lee las fuentes completas

Antes de proponer arquitectura, componentes o código, lee íntegramente:

1. `AGENTS.md`, incluida su sección **Completar por proyecto**
2. `README.md`
3. `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`
4. El fundamento de producto autorizado que `AGENTS.md` identifica
5. `docs/method/Anexo_Aplicacion_SpecKit_v1.2.md`
6. El `README.md` del preset, en `tools/speckit/`
7. `instructions/00_REQUISITOS_DE_INSTALACION.md`
8. `instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md`

Confírmame en lenguaje natural qué gobierna cada fuente. No me entregues un resumen genérico del manifiesto: identifica su **consecuencia concreta para este proyecto**.

Si la sección **Completar por proyecto** de `AGENTS.md` tiene campos sin completar, detente y pídemelos. No los infieras.

### 3. Instala y verifica el método

Aplica exactamente `instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md` usando:

- `PROJECT_ROOT`: raíz actual del repositorio;
- `PACKAGE_PATH`: el directorio del preset en `tools/speckit/`;
- `INITIALIZE_IF_NEEDED`: pregúntame antes de inicializar si SpecKit aún no está presente;
- `SPECIFY_CMD`: `specify` si la instalación global está en rango, o `tools/speckit/specify` si hay que aislar;
- prioridad del preset: `5`.

No elijas por inferencia una integración de agente. Si no existe una integración activa o SpecKit necesita inicialización, preséntame las alternativas realmente disponibles y pídeme una decisión breve.

No modifiques el core de SpecKit, el preset, el manifiesto, el anexo ni el fundamento de producto. No instales `constitution-sync`, extensiones, workflows ni bundles adicionales.

La adaptación solo queda activa cuando:

- las cuatro plantillas resuelven desde el preset;
- los ocho comandos conservan el core nativo y aplican el `wrap` de Software Humano;
- los ocho archivos que la integración reporta como modificados son exactamente esos ocho comandos, sin `checklist` ni `taskstoissues`;
- el checklist continúa nativo;
- `.specify/memory/constitution.md` contiene el núcleo v2.1 completo y coincide con la proyección del preset;
- la integración activa reconoce los comandos resultantes.

Recuerda que materializar la constitución probablemente requiera una **sesión nueva**: avísame antes de llegar a ese punto.

Si una verificación falla, detente e informa evidencia, impacto y decisión requerida.

### 4. Especifica el producto completo

Una vez verificada la integración, usa como fundamento autorizado el documento que `AGENTS.md` identifica.

Ejecuta el equivalente real de `speckit.specify` de la integración activa. La especificación debe preservar:

- todos los identificadores del fundamento, sin renumerar ni reagrupar;
- objetivos y no objetivos;
- decisiones técnicas ya aprobadas;
- contrato lingüístico, si el producto es multilingüe;
- requisitos de experiencia, accesibilidad, rendimiento, privacidad y descubrimiento;
- decisiones abiertas y supuestos reversibles.

No conviertas automáticamente el fundamento en historias de usuario. No selecciones un subconjunto como MVP. No asignes prioridades, fases ni releases salvo que el fundamento los establezca. No agregues funcionalidades plausibles que el fundamento no autorice.

Conserva visibles todas las ambigüedades materiales. El límite nativo de tres marcadores organiza una ronda de preguntas; no reduce la obligación de resolverlas.

### 5. Resuelve ambigüedades con autoridad humana

Ejecuta `clarify` en rondas focalizadas. Pregúntame solo decisiones materiales que continúen abiertas, o contradicciones que impidan planificar con seguridad.

Para cada pregunta indica:

- la decisión requerida;
- por qué cambia el producto o el plan;
- las opciones reales con sus consecuencias;
- tu recomendación, si la tienes, identificada como recomendación y no como decisión tomada.

Registra cada respuesta en el artefacto que posee la decisión. No uses valores predeterminados para cerrar autoría, identidad, licencia, analítica, contacto, publicación, alojamiento ni revisión lingüística.

### 6. Planifica sin sobreingeniería

Cuando las decisiones necesarias estén resueltas, ejecuta el equivalente de:

```text
plan → tasks → analyze
```

El plan debe cubrir todo el alcance, ordenar dependencias y utilizar las decisiones ya aprobadas en el fundamento. Compara el enfoque recomendado con una alternativa más simple, y con la opción de no construir, únicamente donde exista una decisión real.

Crea `research.md`, `data-model.md`, `contracts/` o `quickstart.md` solo si responden una pregunta necesaria identificada en `plan.md`.

Las tareas deben implementar y verificar todo el alcance. No agregues CMS, chatbot, autenticación, personalización, analítica, temas, paneles, modos ni abstracciones no autorizadas.

`analyze` debe ser de solo lectura y verificar doctrina, cobertura, trazabilidad, dependencias, experiencia y evidencia.

### 7. Detente antes de implementar

Después de `analyze`, no ejecutes `implement`. Entrégame un informe en lenguaje natural con:

**Estado del método** — versión de SpecKit y si es global o aislada; integración activa; preset instalado y prioridad; constitución verificada; cualquier pendiente técnico.

**Fundamento utilizado** — fuentes y autoridad; alcance conservado; supuestos; decisiones humanas tomadas y pendientes.

**Artefactos producidos** — rutas de `spec.md`, `plan.md`, `tasks.md` y auxiliares realmente necesarios; propósito y estado de cada uno.

**Cobertura** — elementos del fundamento sin destino; tareas sin fundamento; brechas entre fundamento, especificación, plan y tareas; resultado de `analyze`.

**Riesgos y evidencia** — riesgos técnicos y humanos; evidencia prevista para aceptación; aspectos que todavía requieren revisión humana.

**Próximo paso solicitado** — qué debo revisar exactamente, y solicitud de autorización explícita antes de ejecutar `implement`.

No declares el producto terminado, aprobado ni aceptado. En esta ejecución solo debe quedar preparado para una decisión humana informada sobre el comienzo de la implementación.

## FIN DEL PROMPT
