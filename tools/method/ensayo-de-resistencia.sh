#!/usr/bin/env bash
# Ensayo de resistencia: tres escenarios que intentan romper el método ya
# instalado, para saber dónde cede y qué queda fuera de su control.
#
# No sustituye a `ensayo-de-instalacion.sh`, que comprueba el camino feliz.
# Este hace lo contrario: parte de una instalación correcta y la agrede.
#
# Distingue dos clases de resultado, y la distinción es el punto del ensayo:
#
#   ✓ / ✗  una afirmación que el paquete hace y que aquí se comprueba
#   ·      una conducta observada sobre la que el paquete no afirma nada
#
# Una observación no es un fallo. Es territorio no cubierto, y conocerlo vale
# más que suponer que está cubierto.
#
# No toca este repositorio. Cada escenario vive en su propio directorio
# temporal y se borra al terminar, salvo --conservar.

set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PAQUETE="$RAIZ/dist/software-humano-speckit-starter-v2.2.3"
CONSERVAR=0
[ "${1:-}" = "--conservar" ] && CONSERVAR=1
[ -d "$PAQUETE" ] || { echo "No existe $PAQUETE. Ejecuta tools/build-package.sh primero."; exit 2; }

ok=0; fallo=0; obs=0

comprobar() {  # afirmación del paquete que debe cumplirse
  local desc="$1" real; real="$(eval "$2" 2>/dev/null | tr -d '[:space:]')"
  if [ "$real" = "$3" ]; then printf '  ✓ %s\n' "$desc"; ok=$((ok+1))
  else printf '  ✗ %s\n      esperado «%s», obtenido «%s»\n' "$desc" "$3" "$real"; fallo=$((fallo+1)); fi
}

observar() {  # conducta que se quiere conocer; el veredicto lo pone la persona
  local desc="$1" real; real="$(eval "$2" 2>/dev/null | tr -d '[:space:]')"
  printf '  · %s → %s\n' "$desc" "$real"
  obs=$((obs+1))
  return 0
}

# Prepara un proyecto instalado y correcto. Todo escenario parte de aquí.
montar() {
  local dir; dir="$(mktemp -d)/proyecto"; mkdir -p "$dir"
  cp -R "$PAQUETE/." "$dir/"
  mkdir -p "$dir/.ensayo-bin"
  printf '#!/usr/bin/env bash\nexec "%s" "$@"\n' "$RAIZ/tools/speckit/specify" > "$dir/.ensayo-bin/specify"
  chmod +x "$dir/.ensayo-bin/specify"
  echo "$dir"
}
instalar() {
  git init -q . 2>/dev/null
  git add -A >/dev/null 2>&1
  git -c user.email=e@e -c user.name=e commit -qm base >/dev/null 2>&1
  specify init --here --force --non-interactive --script sh --integration claude --ignore-agent-tools >/dev/null 2>&1
  specify preset add    --dev "tools/speckit/software-humano-spec-kit-preset-2.0.1" >/dev/null 2>&1
  specify extension add --dev "tools/speckit/conformidad-2.2.0"              </dev/null >/dev/null 2>&1
  specify workflow add        "tools/speckit/workflow-software-humano-2.0.0" </dev/null >/dev/null 2>&1
}

###############################################################################
echo "═══ Escenario A · repositorio con trabajo humano previo (brownfield)"
echo "    Pregunta: ¿el método pisa lo que una persona ya escribió?"
echo
A="$(montar)"; cd "$A" || exit 2
export PATH="$A/.ensayo-bin:$A/tools/speckit/shim:$PATH"

git init -q . 2>/dev/null
git add -A >/dev/null 2>&1; git -c user.email=e@e -c user.name=e commit -qm base >/dev/null 2>&1
specify init --here --force --non-interactive --script sh --integration claude --ignore-agent-tools >/dev/null 2>&1

# Trabajo humano anterior al método: una constitución propia, un comando
# sobrescrito a mano y una especificación ya redactada.
printf '# Constitución propia del equipo\n\nEscrita por una persona antes de conocer este método.\n' \
  > .specify/memory/constitution.md
mkdir -p .specify/templates/overrides
printf -- '---\ndescription: version del equipo\n---\n\n# Plan propio del equipo\n' \
  > .specify/templates/overrides/speckit.plan.md
mkdir -p specs/001-previa
printf '# Especificación previa\n\nRequisitos escritos por el equipo. No hay secciones del manifiesto.\n' \
  > specs/001-previa/spec.md
echo '{"feature_directory":"specs/001-previa"}' > .specify/feature.json
HUMANA="$(shasum -a 256 .specify/memory/constitution.md | cut -d' ' -f1)"
PREVIA="$(shasum -a 256 specs/001-previa/spec.md | cut -d' ' -f1)"

specify preset add    --dev "tools/speckit/software-humano-spec-kit-preset-2.0.1" >/dev/null 2>&1
specify extension add --dev "tools/speckit/conformidad-2.2.0"              </dev/null >/dev/null 2>&1
specify workflow add        "tools/speckit/workflow-software-humano-2.0.0" </dev/null >/dev/null 2>&1

comprobar "la constitución escrita por la persona no se toca" \
  "[ \"\$(shasum -a 256 .specify/memory/constitution.md | cut -d' ' -f1)\" = \"$HUMANA\" ] && echo si" "si"
comprobar "la especificación previa no se toca" \
  "[ \"\$(shasum -a 256 specs/001-previa/spec.md | cut -d' ' -f1)\" = \"$PREVIA\" ] && echo si" "si"
comprobar "instalar sobre trabajo previo no aborta" \
  "specify preset list 2>/dev/null | grep -c software-humano" "1"
comprobar "un spec previo sin las secciones del manifiesto detiene la conformidad" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "1"
observar "lo que el agente leerá para plan, ¿lleva el addendum del manifiesto?" \
  "grep -c 'Lo que el manifiesto exige' .claude/skills/speckit-plan/SKILL.md 2>/dev/null | sed 's/^0$/NO/;s/^[1-9].*/SI/'" "NO"
observar "¿cuántos de los ocho comandos alcanza a componer el preset?" \
  "ls .specify/presets/software-humano/.composed/ 2>/dev/null | wc -l" "7"
comprobar "la conformidad detecta el comando sobrescrito y detiene" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "1"
comprobar "y nombra cuál quedó fuera del método" \
  ".specify/extensions/conformidad/scripts/conformidad.sh 2>/dev/null | grep -c 'speckit.plan.*queda fuera del método'" "1"
observar "¿lo reporta la integración como algo distinto de lo normal?" \
  "specify integration status --json 2>/dev/null | python3 -c \"import json,sys;print(len(json.load(sys.stdin)['manifests']['claude']['modified_files']))\"" "7"

###############################################################################
echo
echo "═══ Escenario B · entorno degradado y convivencia con otro preset"
echo "    Pregunta: cuando algo falta, ¿falla ruidoso o se degrada en silencio?"
echo
B="$(montar)"; cd "$B" || exit 2
export PATH="$B/.ensayo-bin:$B/tools/speckit/shim:$PATH"
instalar

# B.1 · sin el shim de PyYAML
LIMPIO="$B/.ensayo-bin:$(echo "$PATH" | tr ':' '\n' | grep -v "tools/speckit/shim" | paste -sd: -)"
observar "sin PyYAML, ¿resolver la plantilla falla o devuelve algo?" \
  "PATH='$LIMPIO' .specify/scripts/bash/resolve-template.sh spec-template >/dev/null 2>&1; [ \$? -ne 0 ] && echo FALLA || echo DEVUELVE" "DEVUELVE"
observar "sin PyYAML, ¿lo que devuelve lleva el addendum del manifiesto?" \
  "PATH='$LIMPIO' .specify/scripts/bash/resolve-template.sh spec-template 2>/dev/null | grep -c 'Lo que el manifiesto exige' | sed 's/^0$/NO/;s/^[1-9].*/SI/'" "NO"
comprobar "preflight nombra la ausencia de PyYAML y dice cómo corregirla" \
  "PATH='$LIMPIO' bash tools/speckit/preflight.sh 2>&1 | grep -c 'NO tiene PyYAML'" "1"
observar "¿esa ausencia bloquea el preflight o solo avisa?" \
  "PATH='$LIMPIO' bash tools/speckit/preflight.sh >/dev/null 2>&1; [ \$? -ne 0 ] && echo BLOQUEA || echo AVISA" "AVISA"

# B.2 · otro preset instalado encima del nuestro
mkdir -p ajeno/commands
cat > ajeno/preset.yml <<'YML'
schema_version: "1.0"

preset:
  id: "preset-ajeno"
  name: "Preset ajeno"
  version: "1.0.0"
  description: "Preset de otro equipo, instalado despues del nuestro"
  priority: 5

requires:
  speckit_version: ">=1.0.0,<2.0.0"

provides:
  templates:
    - type: "command"
      name: "speckit.plan"
      file: "commands/speckit.plan.md"
      description: "Plan del otro equipo"
      strategy: "replace"
YML
printf -- '---\ndescription: plan del otro equipo\n---\n\n# Plan ajeno\n' > ajeno/commands/speckit.plan.md
specify preset add --dev ajeno >/dev/null 2>&1
comprobar "el preset ajeno queda realmente instalado y con más precedencia" \
  "specify preset list 2>/dev/null | grep -c 'preset-ajeno'" "1"
observar "con otro preset en 'replace' encima, ¿sobrevive el addendum en plan?" \
  "grep -c 'Lo que el manifiesto exige' .claude/skills/speckit-plan/SKILL.md 2>/dev/null | sed 's/^0$/NO/;s/^[1-9].*/SI/'" "NO"
observar "¿sobreviven los handoffs nativos de plan?" \
  "head -20 .specify/presets/software-humano/.composed/speckit.plan.md 2>/dev/null | grep -c '^handoffs:' | sed 's/^0$/NO/;s/^[1-9].*/SI/'" "NO"
comprobar "la conformidad detecta que otro preset le quitó la doctrina a plan" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "1"
specify preset remove preset-ajeno </dev/null >/dev/null 2>&1

# B.3 · reinstalación
specify preset remove software-humano </dev/null >/dev/null 2>&1
specify preset add --dev "tools/speckit/software-humano-spec-kit-preset-2.0.1" >/dev/null 2>&1
comprobar "reinstalar el preset no duplica ni rompe la composición" \
  "grep -c 'Lo que el manifiesto exige' .specify/presets/software-humano/.composed/speckit.plan.md" "1"
comprobar "reinstalar no altera el alcance de la integración" \
  "specify integration status --json 2>/dev/null | python3 -c \"import json,sys;print(len(json.load(sys.stdin)['manifests']['claude']['modified_files']))\"" "8"

###############################################################################
echo
echo "═══ Escenario C · manipulación de la doctrina ya instalada"
echo "    Pregunta: ¿qué protege al proyecto una vez que el paquete se abrió?"
echo
C="$(montar)"; cd "$C" || exit 2
export PATH="$C/.ensayo-bin:$C/tools/speckit/shim:$PATH"
instalar
mkdir -p specs/001-ensayo && echo '{"feature_directory":"specs/001-ensayo"}' > .specify/feature.json

comprobar "SHA256SUMS detecta un archivo del paquete alterado" \
  "printf 'x\n' >> instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md; shasum -a 256 -c SHA256SUMS 2>/dev/null | grep -c 'FAILED'" "1"
git checkout -- instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md 2>/dev/null

# C.1 · borrar el addendum del preset ya instalado
CAPA=".specify/presets/software-humano/templates/spec-addendum.md"
cp "$CAPA" "$CAPA.bak"
: > "$CAPA"
observar "vaciada la capa del preset, ¿la plantilla resuelta pierde el manifiesto?" \
  ".specify/scripts/bash/resolve-template.sh spec-template 2>/dev/null | grep -c 'Lo que el manifiesto exige' | sed 's/^0$/PIERDE/;s/^[1-9].*/CONSERVA/'" "PIERDE"
comprobar "la conformidad detecta el addendum vaciado y detiene" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "1"
observar "¿SHA256SUMS cubre lo instalado en .specify?" \
  "grep -c '\.specify/presets' SHA256SUMS | sed 's/^0$/NO/;s/^[1-9].*/SI/'" "NO"
mv "$CAPA.bak" "$CAPA"

# C.2 · una excepción sin razón y sin quién la aprueba
cat > specs/001-ensayo/spec.md <<'FIX'
# Especificación

## Mapa del fundamento
Fuente de prueba.

## Contrato de experiencia
Una pantalla.

## Mapa de cobertura
FIX
comprobar "la ausencia sin declarar detiene" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "1"
printf '\nexcepciones:\n  - seccion: "Mapa de cobertura"\n' \
  >> .specify/extensions/conformidad/conformidad-config.yml
observar "una excepción sin razón y sin aprobador, ¿pasa igual?" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; [ \$? -eq 0 ] && echo PASA || echo DETIENE" "PASA"

# C.3 · una excepción de spec.md ¿tapa la misma sección en tasks.md?
cat > specs/001-ensayo/tasks.md <<'FIX'
# Tareas

## Mapa de cobertura

## Plan de aceptación
Se acepta con revisión humana.
FIX
observar "una excepción nombra una sección; ¿a cuántos artefactos tapa?" \
  ".specify/extensions/conformidad/scripts/conformidad.sh 2>/dev/null | grep -c '^  excepción aprobada'" "2"

# C.4 · editar directamente el archivo que lee el agente
# Aislado a propósito: se deja el proyecto conforme —config limpia y artefactos
# completos— para que un resultado distinto de cero solo pueda venir de la
# edición. Sin aislarlo, el estado que dejó C.2 hacía que la comprobación
# reportara «lo detecta» sin haber detectado nada.
printf 'excepciones: []\n' > .specify/extensions/conformidad/conformidad-config.yml
rm -f specs/001-ensayo/tasks.md
cat > specs/001-ensayo/spec.md <<'FIX'
# Especificación

## Mapa del fundamento
Fuente de prueba.

## Contrato de experiencia
Una pantalla.

## Mapa de cobertura
Todo cubierto.
FIX
comprobar "el proyecto queda conforme antes de la última agresión" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; echo \$?" "0"
printf -- '---\nname: speckit-plan\n---\n\n# sin doctrina\n' > .claude/skills/speckit-plan/SKILL.md
observar "editado a mano lo que lee el agente, ¿lo detecta la conformidad?" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; [ \$? -eq 0 ] && echo NO || echo SI"

# C.5 · un proyecto sin ningún artefacto
rm -f specs/001-ensayo/spec.md specs/001-ensayo/tasks.md
observar "un proyecto sin artefacto alguno, ¿sale en verde?" \
  ".specify/extensions/conformidad/scripts/conformidad.sh >/dev/null 2>&1; [ \$? -eq 0 ] && echo VERDE || echo DETIENE" "VERDE"

###############################################################################
echo
echo "───────────────────────────────────────────────────────────"
echo "  $ok afirmaciones cumplidas · $fallo incumplidas · $obs conductas observadas"
echo
echo "  Lo que ninguna comprobación alcanza todavía:"
echo "    — El archivo que el agente lee de verdad. La conformidad mira la"
echo "      composición, el registro de precedencia y los overrides; si alguien"
echo "      edita .claude/skills/… o su equivalente en otra integración, nadie"
echo "      lo ve. Es la única de las cuatro vías que sigue abierta."
echo "    — SHA256SUMS solo cubre el paquete antes de instalarlo. Lo instalado"
echo "      en .specify/ no tiene integridad propia; lo que lo sostiene es que"
echo "      la conformidad comprueba su contenido, no su hash."
if [ "$CONSERVAR" = "1" ]; then
  echo; echo "  proyectos conservados en $A, $B, $C"
else
  rm -rf "$(dirname "$A")" "$(dirname "$B")" "$(dirname "$C")"
fi
[ "$fallo" -eq 0 ] || exit 1
