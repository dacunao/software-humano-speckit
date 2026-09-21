# Instrucciones persistentes para agentes

Este archivo es la **fuente única** de las reglas que gobiernan el trabajo de cualquier agente en este repositorio. Es neutral respecto del agente: sirve para Claude Code, Codex, Cursor, Gemini, Copilot o cualquier otro que lea instrucciones persistentes del proyecto.

Si tu agente carga un archivo distinto —`CLAUDE.md`, por ejemplo—, ese archivo debe **referenciar** este, no duplicarlo. Dos copias de instrucciones rectoras divergen; el anexo lo prohíbe expresamente.

## Mandato

Este repositorio aplica el **Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1** mediante la adaptación Software Humano para SpecKit, y preserva íntegramente el fundamento de producto autorizado.

No conviertas estas instrucciones en una metodología adicional. Usa el flujo nativo de SpecKit y los artefactos que ya define el núcleo.

## Lectura obligatoria antes de actuar

Lee completos y en este orden:

1. `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`
2. El fundamento de producto autorizado de este proyecto — ver **Completar por proyecto**
3. `docs/method/Anexo_Aplicacion_SpecKit_v1.2.md`
4. El `README.md` del preset, en `tools/speckit/`
5. `instructions/00_REQUISITOS_DE_INSTALACION.md`
6. Los artefactos vigentes de `.specify/`, una vez que existan

No basta con buscar palabras o leer resúmenes. Los identificadores permiten navegar y citar; no sustituyen el pasaje completo.

## Autoridad

- El **núcleo** gobierna principios, doctrina, flujo, artefactos, contrato del agente, detenciones, verificación y gobernanza.
- El **fundamento de producto** gobierna visión, alcance completo, requisitos, no objetivos, decisiones aprobadas y aceptación.
- El **anexo** gobierna la correspondencia entre el núcleo y SpecKit.
- El **preset** gobierna la materialización técnica de esa correspondencia.
- **SpecKit** conserva su comportamiento nativo donde el preset no interviene.

El núcleo y el fundamento no compiten: el núcleo gobierna el método y los criterios; el fundamento gobierna el producto.

No alteres silenciosamente una fuente para acomodarla a otra. Si detectas incompatibilidad, cita ambas disposiciones, explica el impacto y detén la decisión afectada.

## Reglas de trabajo

1. Comprende la definición completa antes de proponer componentes o código.
2. Conserva todos los identificadores del fundamento de producto sin renumerarlos ni reagruparlos.
3. No asignes prioridad, MVP, releases, independencia ni incrementalidad salvo autorización expresa del fundamento.
4. Ordena el trabajo por dependencias, bloqueantes, integración y riesgo sin reducir alcance.
5. Distingue hechos, evidencia, supuestos, inferencias, recomendaciones y decisiones humanas.
6. Utiliza la solución más simple que satisfaga lo aprobado; no agregues modos, paneles, configuraciones, abstracciones ni documentos sin fundamento.
7. Trata experiencia, accesibilidad, rendimiento, confianza, continuidad y control como parte de la funcionalidad.
8. No confundas código correcto, build exitoso o pruebas verdes con aceptación del producto.
9. No te atribuyas revisión humana, excepción aprobada ni autoridad para modificar el fundamento.
10. Mantén trazabilidad bidireccional entre fuente, especificación, plan, tareas, código y evidencia.

## Flujo SpecKit obligatorio

1. Comprueba el entorno con `instructions/00_REQUISITOS_DE_INSTALACION.md` y `tools/speckit/preflight.sh`.
2. Instala y verifica el preset siguiendo `instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md`.
3. Materializa la constitución v2.1 completa.
4. Ejecuta `specify` usando el fundamento completo como fuente autorizada.
5. Ejecuta `clarify` en rondas focalizadas hasta resolver las decisiones materiales necesarias.
6. Ejecuta `plan` para todo el alcance; crea auxiliares solo cuando respondan una pregunta necesaria.
7. Ejecuta `tasks` con cobertura completa y evidencia trazable.
8. Ejecuta `analyze` sin modificar los artefactos examinados.
9. Presenta los resultados en lenguaje natural y espera revisión humana.
10. Ejecuta `implement` solo después de autorización explícita.
11. Ejecuta `converge` para cerrar brechas del alcance aprobado; no para agregar producto nuevo.

## Condiciones de detención

Detente cuando:

- una ambigüedad pueda cambiar alcance, reglas, derechos, seguridad, contenido o experiencia;
- una fuente autorizada contradiga otra;
- falte autoridad para una decisión irreversible o sensible;
- un requisito, principio, idioma o criterio de aceptación pierda cobertura;
- el plan o una tarea agregue una capacidad sin fundamento;
- exista riesgo de sobrescribir cambios humanos en `.specify/`, documentos rectores o código;
- la constitución no pueda verificarse completa;
- una acción requiera modificar el core de SpecKit o el preset para continuar;
- el resultado solo tenga evidencia técnica y se intente declarar aceptación humana.

Una detención útil indica: el hecho, la evidencia, el impacto, la decisión requerida y la acción que no ejecutaste.

## Archivos protegidos por autoridad

No modifiques sin instrucción humana explícita:

- `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`
- `docs/method/Anexo_Aplicacion_SpecKit_v1.2.md`
- El fundamento de producto autorizado
- El directorio del preset en `tools/speckit/`
- `SHA256SUMS`

Si una implementación revela una mejora posible, regístrala como propuesta separada. No la incorpores retroactivamente a las fuentes.

## Notas de entorno que ahorran tiempo

Estas no son doctrina. Son fricciones reales observadas en instalaciones anteriores.

- **Scripts de SpecKit y PyYAML.** `.specify/scripts/bash/common.sh` usa el primer `python3` del `PATH`. Si no tiene PyYAML, toda resolución de plantillas falla. Antepón el shim del repositorio: `PATH="$PWD/tools/speckit/shim:$PATH"`. No modifiques `.specify/scripts/`: son copias generadas y una actualización las reescribiría.
- **Versión de SpecKit.** Si la instalación global está fuera del rango del preset, usa `tools/speckit/specify`, que fija una instancia aislada sin tocar otros proyectos.
- **Constancia de procedencia.** No modifiques `.specify/memory/.constitution-template.json`. Su desajuste tras materializar la constitución es deliberado: hace que el CLI trate la constitución como documento humano y no la sobrescriba.
- **Estado de la integración.** Tras instalar el preset, `integration status` reporta `warning` con 8 archivos modificados. Es el resultado esperado: son los ocho comandos que el preset compone. Verifica que sean exactamente esos ocho y que no incluyan `checklist` ni `taskstoissues`.

## Comunicación con la persona

- Explica resultados, decisiones, riesgos y evidencia en lenguaje natural.
- Cuando muestres código o comandos, acompáñalos con la consecuencia que producen.
- No ocultes pendientes bajo un estado exitoso.
- Distingue avance técnico, cobertura del alcance y aceptación humana.
- Antes de solicitar autorización para implementar, resume fuente, cobertura, decisiones, riesgos y evidencia esperada.

---

# Completar por proyecto

**Todo lo anterior es invariante y se aplica a cualquier proyecto que use este método. Lo que sigue es específico de este repositorio y debe completarse antes de ejecutar `specify`.**

> **Por eso este archivo queda fuera de `SHA256SUMS`.** Está diseñado para que cada proyecto lo edite, de modo que no es un archivo invariante del método. `SHA256SUMS` verifica el manifiesto, el anexo, el preset, las instrucciones y las herramientas: todo lo que **no** debe cambiar. Si la verificación de integridad falla, hay un problema real; completar esta sección nunca la rompe.

Si un campo está sin completar, el agente debe detenerse y solicitarlo. No lo infiera.

## Producto

- **Nombre del proyecto**: Sitio del Manifiesto de Software Humano
- **Qué construye este repositorio**: el sitio web público, narrativo y documental del Manifiesto de Software Humano, en inglés general, español neutro latinoamericano y portugués de Brasil. Es además el primer proyecto real desarrollado con esta adaptación, y este repositorio mantiene el propio paquete de método.

## Fundamento de producto autorizado

- **Ruta**: `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md`
- **Versión**: 1.0, fecha 2026-09-21, estado «Definición de producto para revisión»
- **Autoridad de producto**: Damián Acuña

Solo esa autoridad puede aprobar cambios de alcance, resultados, exclusiones o estado de publicación. El agente puede proponer alternativas y señalar contradicciones; no puede aprobarlas.

La especificación derivada vive en `specs/001-sitio-manifiesto/spec.md`. No sustituye al PRD ni adquiere autoridad por haber sido generada.

## Identificadores que deben preservarse

Sin renumerar ni reagrupar:

- `JS-01`–`JS-09` — Job Stories, con su circunstancia, motivación y resultado
- `FR-001`–`FR-021` — requisitos funcionales
- `AC-01`–`AC-16` — criterios de aceptación del producto
- `P01`–`P10` — principios del núcleo, que aquí son además **contenido publicado** del sitio
- `CL-01`–`CL-11` — decisiones materiales abiertas registradas en `spec.md`

El orden de las Job Stories permite construir una narrativa. **No expresa prioridad ni autoriza a omitir ninguna.**

## Decisiones técnicas aprobadas

Aprobadas por el PRD §24.6. El agente debe preservarlas, no reabrirlas. Solo pueden reemplazarse mediante decisión humana y evidencia de incompatibilidad material; preferencia personal o conveniencia del agente no bastan.

- **TypeScript estricto** para lógica, componentes, integraciones, validadores, pruebas y configuración compatible. El build falla ante errores de tipado. Se evita `any`.
- **Astro** con generación estática por defecto. Islas solo para interacciones que realmente lo requieran.
- **daisyUI sobre Tailwind CSS** como base de componentes, subordinada a la identidad visual y a WCAG 2.2 AA.
- **YAML versionado en GitHub** como fuente de contenido, con esquema formal capaz de detener el build.
- **JSON-LD y Schema.org** derivados de la misma fuente que el contenido visible.
- **WCAG 2.2 AA** como mínimo, y los presupuestos de Core Web Vitals del PRD §24.1.
- **Experiencia pública determinista** en la versión 1.0: sin función generativa para el visitante.

## Contrato lingüístico

- Inglés general (`en`) es el idioma predeterminado y ocupa las rutas **sin prefijo**, incluida `/`.
- Español neutro latinoamericano (`es`) en `/es/`.
- Portugués de Brasil (`pt-BR`) en `/pt-br/`, conservando `pt-BR` en metadatos.
- Las tres versiones cubren el alcance público completo. No son resúmenes.
- El manifiesto original en español conserva la autoridad doctrinal.
- La versión española usa `tú` y `ustedes`. Prohíbe voseo, `vosotros` y localismos nacionales.
- El cambio de idioma navega a una URL equivalente; no sustituye texto solo en cliente.
- Una URL localizada explícita prevalece sobre detección del navegador y sobre la preferencia guardada.
- No se publica traducción automática ni un widget externo sin revisión humana.

## Herramientas del proyecto

- **Gestor de paquetes y ejecutor**: `bun`. Usa `bun install`, `bun run`, `bunx` y `bun test`. No introduzcas `npm`, `yarn` ni `pnpm`, y no generes sus archivos de bloqueo. Decisión humana reversible de Damián Acuña, 21 de septiembre de 2026, conforme al PRD §2.3. Debe registrarse en `plan.md` junto con su consecuencia sobre la reproducibilidad exigida por el PRD §24.5.
- **SpecKit**: usa `tools/speckit/specify`, que fija v1.0.8 aislada. La instalación global permanece en 0.15.0 al servicio de otros proyectos y **no debe actualizarse** desde aquí.

## Archivos protegidos adicionales

Más allá de los protegidos por el método:

- `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md`
- `package/` y `tools/build-package.sh` — fuentes del paquete de método distribuible. Modificarlas implica versionar el paquete y regenerar su `SHA256SUMS`.

## Decisiones abiertas conocidas

Las once registradas como `CL-01`–`CL-11` en `specs/001-sitio-manifiesto/spec.md`. Diez provienen del PRD §29; `CL-11` es la plataforma de alojamiento, que el PRD no fija.

**Ninguna puede cerrarse con un valor predeterminado.** No bloquean especificar ni planificar la arquitectura conceptual; bloquean la publicación y cualquier implementación que las vuelva irreversibles o públicas. `CL-06`, `CL-08` y `CL-09` afectan además contenido y aceptación.
