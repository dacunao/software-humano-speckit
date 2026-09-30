#!/usr/bin/env bash
# Comprobación de conformidad de los artefactos del proyecto.
#
# La ejecuta una persona, una integración continua o un paso `shell` de un
# workflow. **No la ejecuta el agente por su cuenta**, y esa es la diferencia:
# los hooks de SpecKit los invoca el agente y puede omitirlos en silencio.
#
# Comprueba dos cosas, en este orden:
#
#   1. Que el método siga instalado entero. Un preset puede quedar sin efecto
#      sin que nada lo diga —un override local del proyecto, otro preset con
#      más precedencia, un archivo del addendum vaciado por una deriva o un
#      merge—. En los tres casos el artefacto sale limpio porque nunca se le
#      pidió nada. Comprobar los artefactos sin comprobar esto primero es
#      mirar por un vidrio que alguien quitó.
#
#   2. Que lo decidido haya llegado. Una decisión tomada hablando se registra
#      en AGENTS.md o en el fundamento, y puede no llegar nunca a spec.md ni a
#      plan.md. El artefacto queda completo y correcto, así que ninguna otra
#      comprobación lo ve. Esta compara cuándo cambió cada uno por última vez.
#
#   3. Que las secciones que el manifiesto exige existan y tengan contenido,
#      y que toda ausencia esté declarada como excepción aprobada.
#
# Qué NO comprueba, y conviene saberlo: si lo escrito en esas secciones es
# bueno. Una tabla llena de frases plausibles pasa esta comprobación. Eso lo
# juzga `analyze` y lo juzga una persona.
#
# Salida: 0 si todo está cubierto o declarado; 1 si hay ausencias sin declarar
# o el método no está íntegro; 2 si no encuentra el proyecto.

set -uo pipefail

# El script vive en .specify/extensions/<ext>/scripts/, cuatro niveles bajo la
# raíz del proyecto. Contar mal aquí hace que no encuentre ninguna feature y que
# la comprobación pase en verde sin haber mirado nada, que es peor que fallar.
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
[ -d "$RAIZ/.specify" ] || { echo "conformidad: no se encontró .specify desde $RAIZ"; exit 2; }
CONFIG="$RAIZ/.specify/extensions/conformidad/conformidad-config.yml"
[ -f "$CONFIG" ] || CONFIG="$RAIZ/.specify/extensions/conformidad/conformidad-config.local.yml"

# Esta extensión conoce el preset por su identificador. El acoplamiento es real
# y deliberado: comprueban la misma doctrina y se distribuyen juntos.
PRESET="$RAIZ/.specify/presets/software-humano"
MARCA="Lo que el manifiesto exige"

declare -a COMANDOS=(
  speckit.constitution speckit.specify speckit.clarify speckit.plan
  speckit.tasks speckit.analyze speckit.implement speckit.converge
)
declare -a ADDENDA=(spec-addendum.md plan-addendum.md tasks-addendum.md)

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

# ── 1 · El método sigue instalado ────────────────────────────────────────────

comprobar_instalacion() {
  local roto=0
  if [ ! -d "$PRESET/.composed" ]; then
    echo "  FALTA · el preset Software Humano no está instalado o no compuso nada"
    return 1
  fi
  for c in "${COMANDOS[@]}"; do
    if [ ! -f "$PRESET/.composed/$c.md" ]; then
      echo "  FALTA · $c no está compuesto — otra capa lo está reemplazando"
      roto=$((roto+1))
    elif ! grep -q "$MARCA" "$PRESET/.composed/$c.md" 2>/dev/null; then
      echo "  FALTA · $c está compuesto pero perdió lo que el manifiesto exige"
      roto=$((roto+1))
    fi
  done
  for a in "${ADDENDA[@]}"; do
    if [ ! -s "$PRESET/templates/$a" ]; then
      echo "  FALTA · $a está vacío o no existe — la plantilla ya no lleva el manifiesto"
      roto=$((roto+1))
    fi
  done
  # Nuestra composición puede estar intacta y aun así no llegar al agente: otro
  # preset con más precedencia registra el comando en su lugar y el nuestro
  # queda escrito pero sin efecto. El registro de SpecKit dice quién registró
  # qué y con qué prioridad; es la única fuente que lo sabe.
  local registro="$RAIZ/.specify/presets/.registry"
  if [ -f "$registro" ]; then
    local usurpados
    usurpados="$(python3 -c '
import json, sys
NUESTRO = "software-humano"
OCHO = {"speckit.constitution","speckit.specify","speckit.clarify","speckit.plan",
        "speckit.tasks","speckit.analyze","speckit.implement","speckit.converge"}
try:
    presets = json.load(open(sys.argv[1]))["presets"]
except Exception:
    sys.exit(0)
mio = presets.get(NUESTRO, {}).get("priority")
if mio is None:
    sys.exit(0)
for pid, datos in presets.items():
    if pid == NUESTRO or not datos.get("enabled", True):
        continue
    # Menor numero = mas precedencia. En empate SpecKit desempata por id.
    if datos.get("priority", 10**6) > mio:
        continue
    suyos = {c for lista in (datos.get("registered_commands") or {}).values() for c in lista}
    for c in sorted(suyos & OCHO):
        print(c + " lo registra el preset " + pid)
' "$registro" 2>/dev/null)"
    if [ -n "$usurpados" ]; then
      while IFS= read -r linea; do
        [ -z "$linea" ] && continue
        echo "  FALTA · $linea, con más precedencia que el método"
        roto=$((roto+1))
      done <<< "$usurpados"
    fi
  else
    echo "  aviso · no se encontró el registro de presets: no se pudo comprobar la precedencia"
  fi

  # Un override del proyecto gana sobre cualquier preset: es el mecanismo que
  # SpecKit documenta para personalizar, y usarlo saca ese comando del método
  # sin que nada más lo señale. No es un error del proyecto; es una decisión
  # que debe ser visible.
  if [ -d "$RAIZ/.specify/templates/overrides" ]; then
    for c in "${COMANDOS[@]}"; do
      [ -f "$RAIZ/.specify/templates/overrides/$c.md" ] || continue
      echo "  FALTA · $c está sobrescrito en .specify/templates/overrides/ y queda fuera del método"
      roto=$((roto+1))
    done
  fi
  return "$roto"
}

# ── Lo decidido llegó a los artefactos ──────────────────────────────────────
#
# Qué detecta: que una fuente rectora cambiara DESPUÉS que spec.md o plan.md.
# Cuando eso pasa, algo se decidió y no llegó; es certeza, no sospecha.
#
# Qué NO detecta, y conviene saberlo: lo contrario no prueba nada. Que spec.md
# sea más reciente no significa que haya absorbido la decisión — pudo tocarse
# por cualquier otra razón. Esta comprobación cubre una dirección sola.
#
# Usa la fecha del último commit, no la del sistema de archivos: un `clone` o un
# `checkout` reescriben las mtime y la comparación diría cualquier cosa.

fecha_de() {  # último cambio registrado, en segundos
  [ -f "$RAIZ/$1" ] || return 1
  git -C "$RAIZ" log -1 --format=%ct -- "$1" 2>/dev/null
}

comprobar_frescura() {
  local feature="$1" roto=0
  if ! git -C "$RAIZ" rev-parse --git-dir >/dev/null 2>&1; then
    echo "  aviso · sin repositorio git: no se pudo comprobar si lo decidido llegó"
    return 0
  fi
  # La ruta del fundamento la declara AGENTS.md en «Completar por proyecto».
  local fundamento
  fundamento="$(sed -n 's/^- \*\*Ruta\*\*:[[:space:]]*`\([^`]*\)`.*/\1/p' "$RAIZ/AGENTS.md" 2>/dev/null | head -1)"

  declare -a RECTORAS=("AGENTS.md")
  if [ -n "$fundamento" ] && [ -f "$RAIZ/$fundamento" ]; then
    RECTORAS+=("$fundamento")
  else
    echo "  aviso · no se pudo leer la ruta del fundamento en AGENTS.md; se comprueba solo AGENTS.md"
  fi

  for derivado in "$feature/spec.md" "$feature/plan.md"; do
    local td; td="$(fecha_de "$derivado")" || continue
    [ -n "$td" ] || continue
    for rectora in "${RECTORAS[@]}"; do
      local tr; tr="$(fecha_de "$rectora")"
      [ -n "$tr" ] || continue
      if [ "$tr" -gt "$td" ]; then
        echo "  FALTA · $(basename "$derivado") es anterior a $rectora — algo se decidió y no llegó"
        echo "           $rectora cambió el $(date -r "$tr" '+%Y-%m-%d %H:%M' 2>/dev/null)"
        echo "           $(basename "$derivado") no se toca desde el $(date -r "$td" '+%Y-%m-%d %H:%M' 2>/dev/null)"
        roto=$((roto+1))
      fi
    done
  done
  return "$roto"
}

echo "conformidad · integridad del método"
if comprobar_instalacion; then
  echo "  el preset compone los ocho comandos y las tres plantillas llevan el manifiesto"
  INSTALACION_ROTA=0
else
  INSTALACION_ROTA=1
fi
echo

# ── 2 · Los artefactos del proyecto ──────────────────────────────────────────

directorio_de_feature() {
  local f="$RAIZ/.specify/feature.json"
  if [ -f "$f" ]; then
    sed -n 's/.*"feature_directory"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$f" | head -1
  fi
}

# Una excepción vale solo con sus cuatro campos y para el artefacto que nombra.
# `awk` lee cada entrada de la lista como una unidad: al abrir una nueva («- »)
# olvida la anterior, de modo que los campos no se mezclan entre entradas.
_leer_excepcion() {  # <artefacto> <seccion> <modo: valida|diagnostica>
  [ -f "$CONFIG" ] || return 1
  awk -v art="$1" -v sec="$2" -v modo="$3" '
    /^[[:space:]]*#/ || /^[[:space:]]*$/ { next }
    /^[[:space:]]*-[[:space:]]/ { a=""; s=""; r=""; p="" }
    {
      l = $0
      sub(/^[[:space:]]*-[[:space:]]*/, "", l)
      sub(/^[[:space:]]+/, "", l)
      if (l ~ /^[a-z_]+:/) {
        k = substr(l, 1, index(l, ":") - 1)
        v = substr(l, index(l, ":") + 1)
        gsub(/^[[:space:]]+|[[:space:]]+$/, "", v)
        gsub(/^"|"$/, "", v)
        if (k == "artefacto")    a = v
        if (k == "seccion")      s = v
        if (k == "razon")        r = v
        if (k == "aprobada_por") p = v
      }
    }
    a == art && s == sec {
      if (modo == "valida") { if (r != "" && p != "") { hallada = 1; exit } }
      else {
        falta = ""
        if (r == "") falta = "razon"
        if (p == "") falta = (falta == "" ? "aprobada_por" : falta " y aprobada_por")
        if (falta != "") { print falta; hallada = 1; exit }
      }
    }
    END { exit !hallada }
  ' "$CONFIG"
}
esta_exceptuada()      { _leer_excepcion "$1" "$2" valida; }
excepcion_incompleta() { _leer_excepcion "$1" "$2" diagnostica; }

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
  echo "  Nada que comprobar todavía en los artefactos. Ejecuta specify primero."
  exit "$INSTALACION_ROTA"
fi

echo "conformidad · lo decidido llegó a los artefactos"
if comprobar_frescura "$FEATURE"; then
  echo "  spec.md y plan.md son posteriores a AGENTS.md y al fundamento"
  FRESCURA_ROTA=0
else
  FRESCURA_ROTA=1
fi
echo

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
  elif esta_exceptuada "$archivo" "$seccion"; then
    echo "  excepción aprobada · $archivo › $seccion"
    exceptuadas=$((exceptuadas+1))
  else
    incompleta="$(excepcion_incompleta "$archivo" "$seccion" 2>/dev/null)"
    if [ -n "$incompleta" ]; then
      echo "  FALTA · $archivo › $seccion — hay una excepción declarada, pero sin $incompleta"
    else
      echo "  FALTA · $archivo › $seccion — sin contenido y sin excepción declarada"
    fi
    faltan=$((faltan+1))
  fi
done

echo
echo "  $cubiertas con contenido · $exceptuadas con excepción aprobada · $faltan sin declarar"
[ "$sin_artefacto" -gt 0 ] && echo "  ($sin_artefacto comprobaciones omitidas: su artefacto aún no existe)"

if [ "$faltan" -gt 0 ] || [ "$INSTALACION_ROTA" -ne 0 ] || [ "${FRESCURA_ROTA:-0}" -ne 0 ]; then
  echo
  if [ "$faltan" -gt 0 ]; then
    echo "El método no rechaza lo incompleto: rechaza lo que falta sin que nadie lo sepa."
    echo "Declara cada ausencia en $(basename "$CONFIG") con su artefacto, su sección, su"
    echo "razón y quién la aprueba —las cuatro—, o compléta la sección."
  fi
  [ "$INSTALACION_ROTA" -ne 0 ] && \
    echo "El método no está instalado entero: lo de arriba se comprobó sobre un método incompleto."
  [ "${FRESCURA_ROTA:-0}" -ne 0 ] && { \
    echo "Una fuente rectora cambió después que el artefacto que deriva de ella."; \
    echo "No hay comando que propague ese cambio: se lleva a mano. Al hacerlo, la"; \
    echo "comprobación vuelve a verde sola."; }
  exit 1
fi
exit 0
