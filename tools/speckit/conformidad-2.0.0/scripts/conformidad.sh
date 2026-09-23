#!/usr/bin/env bash
# Comprobación de conformidad de los artefactos del proyecto.
#
# La ejecuta una persona, una integración continua o un paso `shell` de un
# workflow. **No la ejecuta el agente por su cuenta**, y esa es la diferencia:
# los hooks de SpecKit los invoca el agente y puede omitirlos en silencio.
#
# Qué comprueba: que las secciones que el manifiesto exige existan y tengan
# contenido, y que toda ausencia esté declarada como excepción aprobada en
# .specify/extensions/conformidad/conformidad-config.yml
#
# Qué NO comprueba, y conviene saberlo: si lo escrito en esas secciones es
# bueno. Una tabla llena de frases plausibles pasa esta comprobación. Eso lo
# juzga `analyze` y lo juzga una persona.
#
# Salida: 0 si todo está cubierto o declarado; 1 si hay ausencias sin declarar.

set -uo pipefail

# El script vive en .specify/extensions/<ext>/scripts/, cuatro niveles bajo la
# raíz del proyecto. Contar mal aquí hace que no encuentre ninguna feature y que
# la comprobación pase en verde sin haber mirado nada, que es peor que fallar.
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
[ -d "$RAIZ/.specify" ] || { echo "conformidad: no se encontró .specify desde $RAIZ"; exit 2; }
CONFIG="$RAIZ/.specify/extensions/conformidad/conformidad-config.yml"
[ -f "$CONFIG" ] || CONFIG="$RAIZ/.specify/extensions/conformidad/conformidad-config.local.yml"

# Secciones que los addenda del preset agregan a cada artefacto. Si el preset
# cambia sus addenda, esta lista cambia con él: ambos salen de los mismos
# artefactos del núcleo.
declare -a EXIGIDAS=(
  "spec.md|Mapa del fundamento"
  "spec.md|Mapa de cobertura"
  "spec.md|Contrato de experiencia"
  "plan.md|Modelo de estados"
  "plan.md|Presupuesto de complejidad"
  "plan.md|Plan de aceptación"
  "plan.md|Registro de decisiones"
  "tasks.md|Mapa de cobertura"
  "tasks.md|Plan de aceptación"
)

directorio_de_feature() {
  local f="$RAIZ/.specify/feature.json"
  if [ -f "$f" ]; then
    sed -n 's/.*"feature_directory"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$f" | head -1
  fi
}

esta_exceptuada() {
  [ -f "$CONFIG" ] || return 1
  grep -q "seccion:.*\"\?$1\"\?" "$CONFIG" 2>/dev/null
}

seccion_con_contenido() {
  # Existe el encabezado y hay al menos una línea con texto antes del siguiente.
  awk -v s="$2" '
    $0 ~ "^#+ .*" s { dentro=1; next }
    dentro && /^#+ / { exit }
    dentro && /[^[:space:]]/ && !/^<!--/ && !/^\|[- |:]*\|$/ { hay=1 }
    END { exit !hay }
  ' "$1"
}

FEATURE="$(directorio_de_feature)"
if [ -z "$FEATURE" ] || [ ! -d "$RAIZ/$FEATURE" ]; then
  echo "conformidad: no hay una feature activa en .specify/feature.json"
  echo "  Nada que comprobar todavía. Ejecuta specify primero."
  exit 0
fi

echo "conformidad · $FEATURE"
[ -f "$CONFIG" ] && echo "  excepciones declaradas en $(basename "$CONFIG")" || echo "  sin archivo de excepciones"
echo

faltan=0; exceptuadas=0; cubiertas=0; sin_artefacto=0
for e in "${EXIGIDAS[@]}"; do
  archivo="${e%%|*}"; seccion="${e##*|}"
  ruta="$RAIZ/$FEATURE/$archivo"
  if [ ! -f "$ruta" ]; then
    sin_artefacto=$((sin_artefacto+1)); continue
  fi
  if seccion_con_contenido "$ruta" "$seccion"; then
    cubiertas=$((cubiertas+1))
  elif esta_exceptuada "$seccion"; then
    echo "  excepción aprobada · $archivo › $seccion"
    exceptuadas=$((exceptuadas+1))
  else
    echo "  FALTA · $archivo › $seccion — sin contenido y sin excepción declarada"
    faltan=$((faltan+1))
  fi
done

echo
echo "  $cubiertas con contenido · $exceptuadas con excepción aprobada · $faltan sin declarar"
[ "$sin_artefacto" -gt 0 ] && echo "  ($sin_artefacto comprobaciones omitidas: su artefacto aún no existe)"

if [ "$faltan" -gt 0 ]; then
  echo
  echo "El método no rechaza lo incompleto: rechaza lo que falta sin que nadie lo sepa."
  echo "Declara cada ausencia en $(basename "$CONFIG") con su razón y quién la aprueba, o complétala."
  exit 1
fi
exit 0
