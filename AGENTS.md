# Instrucciones persistentes para agentes

## Mandato

Este repositorio desarrolla el sitio público del Manifiesto de Software Humano. Debes aplicar el núcleo v2.1 mediante la adaptación Software Humano para SpecKit y preservar íntegramente el PRD autorizado.

No conviertas estas instrucciones en una metodología adicional. Usa el flujo nativo de SpecKit y los artefactos que ya define el núcleo.

## Lectura obligatoria antes de actuar

Lee completos y en este orden:

1. `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`
2. `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md`
3. `docs/method/Anexo_Aplicacion_SpecKit_v1.2.md`
4. `tools/speckit/software-humano-spec-kit-preset-1.0.0/README.md`
5. Los artefactos vigentes de `.specify/`, una vez que existan.

No basta con buscar palabras o leer resúmenes. Los identificadores permiten navegar y citar; no sustituyen el pasaje completo.

## Autoridad

- El núcleo gobierna principios, doctrina, flujo, artefactos, contrato del agente, detenciones, verificación y gobernanza.
- El PRD gobierna visión, alcance completo, Job Stories, requisitos, no objetivos, decisiones aprobadas y aceptación del sitio.
- El anexo gobierna la correspondencia entre el núcleo y SpecKit.
- El preset gobierna la materialización técnica de esa correspondencia.
- SpecKit conserva su comportamiento nativo donde el preset no interviene.
- Damián Acuña es la autoridad de producto declarada en el PRD.

No alteres silenciosamente una fuente para acomodarla a otra. Si detectas incompatibilidad, cita ambas disposiciones, explica el impacto y detén la decisión afectada.

## Reglas de trabajo

1. Comprende la definición completa antes de proponer componentes o código.
2. Conserva `JS-01`–`JS-09`, `FR-001`–`FR-021`, `AC-01`–`AC-16` y `P01`–`P10`.
3. No asignes prioridad, MVP, releases, independencia ni incrementalidad salvo autorización expresa.
4. Ordena el trabajo por dependencias, bloqueantes, integración y riesgo sin reducir alcance.
5. Distingue hechos, evidencia, supuestos, inferencias, recomendaciones y decisiones humanas.
6. Utiliza la solución más simple que satisfaga lo aprobado; no agregues modos, paneles, configuraciones, abstracciones o documentos sin fundamento.
7. Trata experiencia, accesibilidad, rendimiento, confianza, continuidad y control como parte de la funcionalidad.
8. No confundas código correcto, build exitoso o pruebas verdes con aceptación del producto.
9. No te atribuyas revisión humana, excepción aprobada ni autoridad para modificar el PRD.
10. Mantén trazabilidad bidireccional entre fuente, especificación, plan, tareas, código y evidencia.

## Decisiones técnicas aprobadas

- TypeScript estricto para lógica, componentes, integraciones, validadores, pruebas y configuración compatible.
- Astro como framework de la versión 1.0.
- Generación estática por defecto; islas solo para interacciones justificadas.
- daisyUI sobre Tailwind CSS como base de componentes, sin permitir que determine la identidad visual.
- YAML versionado en GitHub como fuente de contenido, con validación que pueda detener el build.
- JSON-LD y vocabulario Schema.org derivados de la misma fuente que el contenido visible.
- WCAG 2.2 AA como mínimo.
- Presupuestos de Core Web Vitals definidos en el PRD.
- Experiencia pública determinista en la versión 1.0.

Una tecnología aprobada solo puede reemplazarse mediante decisión humana y evidencia de incompatibilidad material. Preferencia personal o conveniencia del agente no bastan.

## Contrato lingüístico

- Inglés general (`en`) es el idioma predeterminado y utiliza rutas sin prefijo.
- Español neutro latinoamericano (`es`) utiliza `/es/`.
- Portugués de Brasil (`pt-BR`) utiliza `/pt-br/`.
- Las tres versiones cubren el alcance público completo.
- El manifiesto original en español conserva la autoridad doctrinal.
- La versión española usa `tú` y `ustedes`; prohíbe voseo, `vosotros` y localismos nacionales.
- El cambio de idioma navega a una URL equivalente y no sustituye texto solo en cliente.
- Una URL localizada explícita prevalece sobre detección del navegador y preferencias guardadas.
- No uses traducción automática o un widget externo como contenido publicado sin revisión humana.

## Flujo SpecKit obligatorio

1. Instala y verifica el preset siguiendo `instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md`.
2. Materializa la constitución v2.1 completa.
3. Ejecuta `specify` usando el PRD completo como fundamento autorizado.
4. Ejecuta `clarify` en rondas focalizadas hasta resolver las decisiones materiales necesarias.
5. Ejecuta `plan` para todo el alcance y crea auxiliares solo cuando respondan una pregunta necesaria.
6. Ejecuta `tasks` con cobertura completa y evidencia trazable.
7. Ejecuta `analyze` sin modificar los artefactos examinados.
8. Presenta los resultados en lenguaje natural y espera revisión humana.
9. Ejecuta `implement` solo después de autorización explícita.
10. Ejecuta `converge` para cerrar brechas del alcance aprobado; no para agregar producto nuevo.

## Condiciones de detención

Detente cuando:

- una ambigüedad pueda cambiar alcance, reglas, derechos, seguridad, contenido o experiencia;
- una fuente autorizada contradiga otra;
- falte autoridad para una decisión irreversible o sensible;
- una Job Story, requisito, principio, idioma o criterio de aceptación pierda cobertura;
- el plan o una tarea agregue una capacidad sin fundamento;
- exista riesgo de sobrescribir cambios humanos en `.specify/`, documentos rectores o código;
- la constitución no pueda verificarse completa;
- una acción requiera modificar el core de SpecKit o el preset para continuar;
- el resultado solo tenga evidencia técnica y se intente declarar aceptación humana.

Una detención útil debe indicar el hecho, la evidencia, el impacto, la decisión requerida y la acción que no ejecutaste.

## Archivos protegidos por autoridad

No modifiques sin instrucción humana explícita:

- `docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md`
- `docs/method/Anexo_Aplicacion_SpecKit_v1.2.md`
- `docs/product/PRD_Sitio_Manifiesto_Software_Humano_v1.0.md`
- `tools/speckit/software-humano-spec-kit-preset-1.0.0/`

Si una implementación revela una mejora posible, regístrala como propuesta separada. No la incorpores retroactivamente a las fuentes.

## Comunicación con la persona

- Explica resultados, decisiones, riesgos y evidencia en lenguaje natural.
- Cuando muestres código o comandos, acompáñalos con la consecuencia que producen.
- No ocultes pendientes bajo un estado exitoso.
- Distingue avance técnico, cobertura del alcance y aceptación humana.
- Antes de solicitar autorización para implementar, resume fuente, cobertura, decisiones, riesgos y evidencia esperada.
