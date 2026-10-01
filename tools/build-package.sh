#!/usr/bin/env bash
# Ensambla el paquete distribuible Software Humano para SpecKit.
#
# Toma las fuentes canónicas del repositorio y produce en dist/:
#   - el directorio del paquete listo para descomprimir en la raíz de un repo;
#   - su ZIP verificable;
#   - SHA256SUMS regenerado.
#
# No modifica ninguna fuente. Es idempotente: borra y rehace dist/.
set -euo pipefail

RAIZ="$(CDPATH="" cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION_PAQUETE="2.3.3"
# Las cinco capas del método comparten el número de salida 2.0.0. No están
# acopladas: cuando una necesite un parche se mueve sola, y esa divergencia
# significará que esa capa cambió. Lo que no significaba nada era que salieran
# desalineadas de origen.
VERSION_PRESET="2.0.3"
VERSION_EXTENSION="2.2.3"
VERSION_WORKFLOW="2.0.0"
VERSION_BUNDLE="2.1.1"
NOMBRE="software-humano-speckit-starter-v${VERSION_PAQUETE}"

DIST="$RAIZ/dist"
STAGE="$DIST/$NOMBRE"
PRESET_DIR="software-humano-spec-kit-preset-${VERSION_PRESET}"
EXTENSION_DIR="conformidad-${VERSION_EXTENSION}"
WORKFLOW_DIR="workflow-software-humano-${VERSION_WORKFLOW}"
BUNDLE_DIR="bundle-software-humano-${VERSION_BUNDLE}"

echo "==> Comprobando conformidad antes de ensamblar"
# Un paquete que no puede demostrar su correspondencia con el manifiesto no se
# distribuye. Las comprobaciones se ejecutan antes de copiar nada, para que un
# fallo no deje un dist/ a medio armar.
python3 "$RAIZ/tools/method/extraer-identificadores.py" --comprobar
python3 "$RAIZ/tools/method/comprobar-vocabulario.py"
python3 "$RAIZ/tools/method/comprobar-conformidad.py"
echo

echo "==> Limpiando dist/"
rm -rf "$DIST"
mkdir -p "$STAGE"

echo "==> Copiando fuentes propias del paquete"
cp -R "$RAIZ/package/." "$STAGE/"

echo "==> Copiando doctrina canónica (sin duplicarla en el repositorio)"
mkdir -p "$STAGE/docs/method"
cp "$RAIZ/docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md" "$STAGE/docs/method/"
cp "$RAIZ/docs/method/Anexo_Aplicacion_SpecKit_v2.0.md"              "$STAGE/docs/method/"
cp "$RAIZ/docs/method/Anexo_Aplicacion_SpecKit_v1.2.md"              "$STAGE/docs/method/"
cp "$RAIZ/docs/method/GUIA_DE_IMPLEMENTACION_SPECKIT.md"             "$STAGE/docs/method/"
cp "$RAIZ/docs/method/inventario-de-objetos.md"                      "$STAGE/docs/method/"
cp "$RAIZ/docs/method/compuertas-del-metodo.md"                      "$STAGE/docs/method/"
cp "$RAIZ/docs/method/mapa-de-cobertura.md"                          "$STAGE/docs/method/"
cp "$RAIZ/docs/method/vocabulario-de-maquinaria.md"                  "$STAGE/docs/method/"

echo "==> Copiando las cuatro capas del método v2.0.0"
for d in "$PRESET_DIR" "$EXTENSION_DIR" "$WORKFLOW_DIR" "$BUNDLE_DIR"; do
  cp -R "$RAIZ/tools/speckit/$d" "$STAGE/tools/speckit/"
done

echo "==> Eliminando basura del sistema de archivos"
find "$STAGE" -name '.DS_Store' -delete
find "$STAGE" -name '__MACOSX' -type d -exec rm -rf {} + 2>/dev/null || true

echo "==> Empaquetando cada capa por separado"
# Cada una se instala por su cuenta mientras no haya catálogo publicado: el zip
# de un bundle lleva solo su manifiesto, no los componentes.
# Cada componente lleva su licencia adentro, como archivo del repositorio y no
# como salida de este script: un archivo que se descarga y se instala por su
# cuenta no puede depender de que alguien tenga a mano el resto del paquete.
# MIT exige que su aviso acompañe a todas las copias, y el catálogo de comunidad
# de SpecKit lo pide como requisito de envío.
#
# El preset lleva además `LICENSE-CONTENT` y su propio `LICENSING.md`, y no es
# simetría: su `templates/constitution-template.md` es texto del núcleo bajo
# CC BY 4.0, no código bajo MIT. Distribuirlo con una sola licencia lo
# licenciaría mal. Es `DP-03`.
for d in "$PRESET_DIR" "$EXTENSION_DIR" "$WORKFLOW_DIR" "$BUNDLE_DIR"; do
  if [ ! -f "$RAIZ/tools/speckit/$d/LICENSE" ]; then
    echo "    FALLO: $d no lleva su LICENSE. Un componente se distribuye solo."
    exit 1
  fi
done
if [ ! -f "$RAIZ/tools/speckit/$PRESET_DIR/LICENSE-CONTENT" ]; then
  echo "    FALLO: el preset no lleva LICENSE-CONTENT, y proyecta el núcleo bajo CC BY."
  exit 1
fi

( cd "$STAGE/tools/speckit" \
  && zip -q -r -X "Software_Humano_Preset_v${VERSION_PRESET}.zip"    "$PRESET_DIR" \
  && zip -q -r -X "Software_Humano_Conformidad_v${VERSION_EXTENSION}.zip" "$EXTENSION_DIR" \
  && zip -q -r -X "Software_Humano_Workflow_v${VERSION_WORKFLOW}.zip"     "$WORKFLOW_DIR" \
  && zip -q -r -X "Software_Humano_Bundle_v${VERSION_BUNDLE}.zip"         "$BUNDLE_DIR" )

echo "==> Asegurando permisos de ejecución"
chmod +x "$STAGE/tools/speckit/preflight.sh" \
         "$STAGE/tools/speckit/specify" \
         "$STAGE/tools/speckit/shim/python3"

echo "==> Comprobando que el bundle fije las versiones reales"
python3 - "$RAIZ" <<'PYBUNDLE'
import pathlib, re, sys
raiz = pathlib.Path(sys.argv[1])
bundle = next(raiz.glob("tools/speckit/bundle-*/bundle.yml"))
texto = bundle.read_text()
fallos = []
for pin, fuente in re.findall(r'version:\s*"([^"]+)"\s*\n\s*source:\s*"\.\./([^"]+)"', texto):
    manifiesto = next((raiz / "tools/speckit" / fuente).glob("*.yml"), None)
    if manifiesto is None:
        fallos.append(f"{fuente}: no se encontró su manifiesto"); continue
    # `schema_version` va sin sangría y la del componente dentro de su bloque,
    # así que la sangría las distingue. Sin eso se lee «1.0» para todo.
    real = re.search(r'^\s+version:\s*"([^"]+)"', manifiesto.read_text(), re.M)
    real = real.group(1) if real else "?"
    if real != pin:
        fallos.append(f"{fuente}: el bundle fija {pin} y el componente declara {real}")
if fallos:
    print("    FALLO: el bundle fija versiones que no coinciden con los componentes.")
    for f in fallos: print("      " + f)
    sys.exit(1)
print("    el bundle fija las versiones que los componentes declaran")
PYBUNDLE

echo "==> Generando SHA256SUMS"
# Quedan fuera los archivos que **pertenecen al proyecto que instala**, no al
# método. Fijarlos obliga a cada proyecto a conservarlos tal cual para que su
# verificación de integridad pase, y eso es apropiarse de su repositorio:
#
#   AGENTS.md   cada proyecto lo completa — ya estaba fuera
#   README.md   el README de un repositorio es suyo
#
# Se excluye por ruta y no por nombre: `tools/speckit/shim/README.md` y el del
# bundle sí son del método y siguen cubiertos.
#
# `LICENSE` sigue cubierto y no debería: un proyecto también tiene la suya. No
# se toca aquí porque el arreglo real es que los archivos del método dejen de
# vivir en la raíz del proyecto, y eso cambia la forma del paquete. Queda en la
# propuesta 011.
( cd "$STAGE" \
  && find . -type f ! -name 'SHA256SUMS' ! -name 'AGENTS.md' ! -path './README.md' -print0 \
     | LC_ALL=C sort -z \
     | xargs -0 shasum -a 256 \
     | sed 's|  \./|  |' > SHA256SUMS )

echo "==> Verificando integridad recién generada"
( cd "$STAGE" && shasum -a 256 -c SHA256SUMS >/dev/null )

echo "==> Ensayo de instalación sobre un proyecto desechable"
# Instalar el paquete recién armado en un proyecto limpio y comprobar cada
# afirmación de la instrucción 01. Un paquete que se arma pero no se instala no
# está probado, y hasta ahora esa distancia se cubría a mano.
bash "$RAIZ/tools/method/ensayo-de-instalacion.sh" | sed 's/^/    /'
echo

echo "==> Sincronizando el manifiesto de integridad del repositorio"
# El de dist/ cubre el paquete armado, zips incluidos. El de la raíz cubre las
# fuentes: los zips son salida de este script y no existen en el repositorio.
# Generarlo aquí evita que quede describiendo una versión anterior, que es lo
# que ocurrió con el 1.6.0.
grep -v '  tools/speckit/Software_Humano_.*\.zip$' "$STAGE/SHA256SUMS" > "$RAIZ/SHA256SUMS"
# La raíz de este repositorio es la instalación del propio método sobre sí mismo:
# `package/` es la fuente y la raíz es la copia instalada. Si una diverge, el
# repositorio dejó de correr el método que distribuye, y conviene saber cuál.
if ! ( cd "$RAIZ" && shasum -a 256 -c SHA256SUMS >/dev/null 2>&1 ); then
  echo "    FALLO: la instalación de la raíz no coincide con el paquete armado."
  echo "    Archivos que divergieron:"
  ( cd "$RAIZ" && shasum -a 256 -c SHA256SUMS 2>/dev/null \
      | grep -v ': OK$' | sed 's/^/      /' )
  echo "    Copia la fuente sobre la raíz, o corrige la fuente si el cambio era ahí."
  exit 1
fi
echo "    integridad del repositorio: $(wc -l < "$RAIZ/SHA256SUMS" | tr -d ' ') archivos"

echo "==> Empaquetando la distribución"
( cd "$DIST" && zip -q -r -X "${NOMBRE}.zip" "$NOMBRE" )

total="$(grep -c . "$STAGE/SHA256SUMS")"
echo
echo "Paquete listo:"
echo "  directorio : dist/$NOMBRE"
echo "  ZIP        : dist/${NOMBRE}.zip"
echo "  archivos   : $total (verificados $total/$total)"
echo "  sha256 ZIP : $(shasum -a 256 "$DIST/${NOMBRE}.zip" | cut -d' ' -f1)"
