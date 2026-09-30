#!/usr/bin/env bash
# Ensayo de instalación: ejecuta la instrucción 01 sobre un proyecto desechable
# y comprueba, una por una, cada afirmación que ese documento hace.
#
# Existe porque hasta ahora el método se validaba a trozos y a mano. Un ensayo
# que se puede repetir convierte esa validación en algo que corre antes de
# exponer el paquete, y no después de que alguien lo instale.
#
# **No toca este repositorio.** Crea un proyecto temporal, instala ahí, y lo
# borra al terminar salvo que se pase --conservar.
#
# Lo que este ensayo NO prueba: que un agente aplique la doctrina. Eso no lo
# comprueba ningún script — lo comprueba el piloto, con personas.

set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PAQUETE="$RAIZ/dist/software-humano-speckit-starter-v2.2.0"
CONSERVAR=0
[ "${1:-}" = "--conservar" ] && CONSERVAR=1

ok=0; fallo=0
comprobar() {  # comprobar "qué afirma la instrucción" "comando" "esperado"
  local desc="$1" real; real="$(eval "$2" 2>/dev/null | tr -d '[:space:]')"
  if [ "$real" = "$3" ]; then
    printf '  ✓ %s\n' "$desc"; ok=$((ok+1))
  else
    printf '  ✗ %s\n      esperado «%s», obtenido «%s»\n' "$desc" "$3" "$real"; fallo=$((fallo+1))
  fi
}

[ -d "$PAQUETE" ] || { echo "No existe $PAQUETE. Ejecuta tools/build-package.sh primero."; exit 2; }

PROYECTO="$(mktemp -d)/ensayo"
mkdir -p "$PROYECTO"
cp -R "$PAQUETE/." "$PROYECTO/"
cd "$PROYECTO" || exit 2
# `specify` se expone por PATH y no por ruta: la del repositorio contiene un
# espacio, y una ruta con espacio dentro de un `eval` se parte en dos palabras.
# Ese bug hizo que el primer ensayo reportara como no instalado lo que sí lo
# estaba — una comprobación que falla por su arnés es peor que no tenerla.
mkdir -p "$PROYECTO/.ensayo-bin"
printf '#!/usr/bin/env bash\nexec "%s" "$@"\n' "$RAIZ/tools/speckit/specify" > "$PROYECTO/.ensayo-bin/specify"
chmod +x "$PROYECTO/.ensayo-bin/specify"
export PATH="$PROYECTO/.ensayo-bin:$PROYECTO/tools/speckit/shim:$PATH"
SPECIFY=specify

echo "Ensayo de instalación · $PROYECTO"
echo

echo "── Paso 2 · integridad del paquete"
comprobar "SHA256SUMS verifica sin una sola discrepancia" \
  "shasum -a 256 -c SHA256SUMS 2>&1 | grep -c 'FAILED'" "0"

echo "── Requisito previo · repositorio e inicialización"
git init -q . 2>/dev/null
git add -A >/dev/null 2>&1 && git -c user.email=e@e -c user.name=e commit -qm base >/dev/null 2>&1
"$SPECIFY" init --here --force --non-interactive --script sh --integration claude --ignore-agent-tools >/dev/null 2>&1
comprobar "SpecKit queda inicializado" "[ -d .specify ] && echo si" "si"

echo "── Paso 3 · instalación de las tres capas"
"$SPECIFY" preset add    --dev "tools/speckit/software-humano-spec-kit-preset-2.0.1" >/dev/null 2>&1
"$SPECIFY" extension add --dev "tools/speckit/conformidad-2.2.0"                      </dev/null >/dev/null 2>&1
"$SPECIFY" workflow add        "tools/speckit/workflow-software-humano-2.0.0"         </dev/null >/dev/null 2>&1
comprobar "el preset queda instalado"      "$SPECIFY preset list 2>/dev/null | grep -c software-humano" "1"
comprobar "la extensión queda instalada"   "[ -d .specify/extensions/conformidad ] && echo si" "si"
comprobar "el workflow queda instalado"    "$SPECIFY workflow list 2>/dev/null | grep -c 'compuertas del manifiesto'" "1"
comprobar "la configuración de excepciones se crea" \
  "[ -f .specify/extensions/conformidad/conformidad-config.yml ] && echo si" "si"

echo "── Paso 5.2 · las plantillas conservan lo nativo y agregan lo del manifiesto"
comprobar "spec-template conserva Success Criteria y Edge Cases" \
  ".specify/scripts/bash/resolve-template.sh spec-template | grep -c 'Success Criteria\|Edge Cases'" "2"
# Sin `grep -q`: cierra la tubería, el script de arriba muere con SIGPIPE y
# `pipefail` hace que el `&&` nunca dispare. La comprobación decía que faltaba
# algo que estaba.
comprobar "plan-template conserva Constitution Check" \
  "[ \"\$(.specify/scripts/bash/resolve-template.sh plan-template | grep -c 'Constitution Check')\" -ge 1 ] && echo si" "si"
comprobar "plan-template conserva sus tokens de invocación resueltos" \
  ".specify/scripts/bash/resolve-template.sh plan-template | grep -c '__SPECKIT_COMMAND'" "0"
for t in spec plan tasks; do
  comprobar "$t-template lleva los artefactos del manifiesto" \
    ".specify/scripts/bash/resolve-template.sh $t-template | grep -c 'Lo que el manifiesto exige en este artefacto'" "1"
done

echo "── Paso 5.3 · los comandos conservan su frontmatter nativo"
for c in specify plan tasks clarify constitution; do
  comprobar "speckit.$c conserva sus handoffs" \
    "head -20 .specify/presets/software-humano/.composed/speckit.$c.md | grep -c '^handoffs:'" "1"
done
comprobar "speckit.plan conserva su descripción nativa" \
  "head -4 .specify/presets/software-humano/.composed/speckit.plan.md | grep -c 'implementation planning workflow'" "1"
comprobar "speckit.plan conserva sus scripts" \
  "head -20 .specify/presets/software-humano/.composed/speckit.plan.md | grep -c '^scripts:'" "1"

echo "── Lo que hace invocable al método desde conversación"
# El piloto midió que los comandos se disparan porque su descripción nativa
# nombra artefactos y momentos. Una capa que declara frontmatter la reemplaza y
# el agente deja de reconocer cuándo aplican. Las aserciones sobre `handoffs`
# NO lo detectan: analyze, converge e implement no traen handoffs en el core.
# El frontmatter es `---` en la PRIMERA línea. `grep -l '^---'` busca en todo el
# archivo y estos comandos usan `---` como separador horizontal: daba 8 de 8 y
# habría detenido el ensamblado por un defecto que no existía.
comprobar "ningún comando del preset declara frontmatter propio" \
  "for f in .specify/presets/software-humano/commands/*.md; do head -1 \"\$f\"; done | grep -c '^---'" "0"
comprobar "los ocho comandos empiezan en el marcador del core" \
  "grep -c '^{CORE_TEMPLATE}' .specify/presets/software-humano/commands/*.md | grep -c ':1$'" "8"
comprobar "speckit.analyze conserva la descripción nativa que nombra los artefactos" \
  "head -4 .specify/presets/software-humano/.composed/speckit.analyze.md | grep -c 'cross-artifact consistency'" "1"
comprobar "speckit.converge conserva la suya" \
  "head -5 .specify/presets/software-humano/.composed/speckit.converge.md | grep -c 'Assess the current codebase'" "1"

echo "── Paso 5.4 · el checklist sigue nativo"
comprobar "el preset no toca speckit.checklist" \
  "[ -f .specify/presets/software-humano/commands/speckit.checklist.md ] && echo si || echo no" "no"

echo "── Paso 5.5 · alcance de la integración"
comprobar "la integración reporta exactamente ocho comandos modificados" \
  "$SPECIFY integration status --json 2>/dev/null | python3 -c \"import json,sys; d=json.load(sys.stdin); print(len(d['manifests']['claude']['modified_files']))\"" "8"
comprobar "no incluye checklist ni taskstoissues" \
  "$SPECIFY integration status --json 2>/dev/null | grep -c 'checklist\|taskstoissues'" "0"

echo "── Pasos 7 y 8 · conformidad y excepciones aprobadas"
mkdir -p specs/001-ensayo
echo '{"feature_directory":"specs/001-ensayo"}' > .specify/feature.json
# El fixture trae con contenido todo lo que la conformidad exige de spec.md,
# **menos una sección**, para que el fallo sea el que se quiere provocar y no
# uno accidental. En el primer ensayo faltaban dos y la causa quedó confundida.
cat > specs/001-ensayo/spec.md <<'FIXTURE'
# Especificación

## Mapa del fundamento

Fuente: docs/product/base.md, autoridad de prueba.

## Contrato de experiencia

Ruta principal: una sola pantalla de ensayo.

## Mapa de cobertura

<!-- deliberadamente vacío: es la ausencia que este ensayo provoca -->
FIXTURE
comprobar "una ausencia sin declarar detiene la conformidad" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "1"
cat >> .specify/extensions/conformidad/conformidad-config.yml <<'YML'

excepciones:
  - artefacto: "spec.md"
    seccion: "Mapa de cobertura"
    razon: "Proyecto de ensayo; no hay alcance real que cubrir."
    aprobada_por: "Ensayo automatizado"
YML
comprobar "la misma ausencia, declarada, no detiene nada" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "0"


echo "── Excepciones: las cuatro o ninguna"
cat > .specify/extensions/conformidad/conformidad-config.local.yml <<'YML'
excepciones:
  - artefacto: "spec.md"
    seccion: "Mapa de cobertura"
YML
rm -f .specify/extensions/conformidad/conformidad-config.yml
comprobar "una excepción sin razón ni aprobador no es excepción aprobada" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "1"
comprobar "y dice cuál de los dos campos falta" \
  ".specify/extensions/conformidad/scripts/conformidad.sh 2>/dev/null | grep -c 'sin razon y aprobada_por'" "1"

echo "── Integridad del método instalado"
comprobar "la conformidad confirma que el preset compone los ocho comandos" \
  ".specify/extensions/conformidad/scripts/conformidad.sh 2>/dev/null | grep -c 'compone los ocho comandos'" "1"
mkdir -p .specify/templates/overrides
printf -- '---\ndescription: version del equipo\n---\n' > .specify/templates/overrides/speckit.plan.md
comprobar "un override del proyecto sobre uno de los ocho se reporta y detiene" \
  ".specify/extensions/conformidad/scripts/conformidad.sh 2>/dev/null | grep -c 'queda fuera del método'" "1"
rm -rf .specify/templates/overrides
: > .specify/presets/software-humano/templates/spec-addendum.md
comprobar "un addendum vaciado se reporta" \
  ".specify/extensions/conformidad/scripts/conformidad.sh 2>/dev/null | grep -c 'la plantilla ya no lleva el manifiesto'" "1"

echo "── Lo decidido llegó a los artefactos"
# Se provoca la ventana real del piloto: una fuente rectora cambia después del
# artefacto que deriva de ella. Se usan commits porque la comprobación lee la
# fecha del commit, no la del sistema de archivos.
# La capa del preset se restaura: la comprobación anterior la vació a propósito
# y aquí estorbaría el diagnóstico.
git checkout -- .specify/presets/software-humano/templates/spec-addendum.md 2>/dev/null \
  || printf 'Lo que el manifiesto exige en este artefacto\n' > .specify/presets/software-humano/templates/spec-addendum.md
# Fechas explícitas: `git log --format=%ct` tiene resolución de SEGUNDOS, y dos
# commits del ensayo caen en el mismo. La ventana real del piloto duró horas;
# la del ensayo hay que forzarla o la comprobación parece no disparar.
fechar() { GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1" \
  git -c user.email=e@e -c user.name=e commit -qm "$2" >/dev/null 2>&1; }
git add -A >/dev/null 2>&1
fechar "2026-09-28T23:32:00" "artefactos"
printf '\n<!-- una decisión tomada conversando -->\n' >> AGENTS.md
git add AGENTS.md >/dev/null 2>&1
fechar "2026-09-29T16:28:00" "decisión en AGENTS.md"
comprobar "una decisión que no llegó a spec.md detiene la conformidad" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "1"
comprobar "y nombra cuál artefacto quedó atrás" \
  ".specify/extensions/conformidad/scripts/conformidad.sh 2>/dev/null | grep -c 'spec.md es anterior a AGENTS.md'" "1"
printf '\n<!-- la decisión, ya recogida -->\n' >> specs/001-ensayo/spec.md
git add specs >/dev/null 2>&1
fechar "2026-09-29T21:06:00" "spec recoge la decisión"
comprobar "al reconciliar a mano, vuelve a verde sola" \
  ".specify/extensions/conformidad/scripts/conformidad.sh 2>/dev/null | grep -c 'son posteriores a AGENTS.md'" "1"

echo
echo "  $ok comprobaciones pasaron · $fallo fallaron"
if [ "$CONSERVAR" = "1" ]; then
  echo "  proyecto conservado en $PROYECTO"
else
  rm -rf "$(dirname "$PROYECTO")"
fi
[ "$fallo" -eq 0 ] || exit 1
