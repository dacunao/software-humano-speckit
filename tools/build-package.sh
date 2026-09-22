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
VERSION_PAQUETE="1.6.0"
VERSION_PRESET="1.2.0"
NOMBRE="software-humano-speckit-starter-v${VERSION_PAQUETE}"

DIST="$RAIZ/dist"
STAGE="$DIST/$NOMBRE"
PRESET_DIR="software-humano-spec-kit-preset-${VERSION_PRESET}"

echo "==> Limpiando dist/"
rm -rf "$DIST"
mkdir -p "$STAGE"

echo "==> Copiando fuentes propias del paquete"
cp -R "$RAIZ/package/." "$STAGE/"

echo "==> Copiando doctrina canónica (sin duplicarla en el repositorio)"
mkdir -p "$STAGE/docs/method"
cp "$RAIZ/docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md" "$STAGE/docs/method/"
cp "$RAIZ/docs/method/Anexo_Aplicacion_SpecKit_v1.2.md"              "$STAGE/docs/method/"

echo "==> Copiando el preset v${VERSION_PRESET}"
cp -R "$RAIZ/tools/speckit/$PRESET_DIR" "$STAGE/tools/speckit/"

echo "==> Eliminando basura del sistema de archivos"
find "$STAGE" -name '.DS_Store' -delete
find "$STAGE" -name '__MACOSX' -type d -exec rm -rf {} + 2>/dev/null || true

echo "==> Empaquetando el preset"
( cd "$STAGE/tools/speckit" \
  && zip -q -r -X "Software_Humano_SpecKit_Preset_v${VERSION_PRESET}.zip" "$PRESET_DIR" )

echo "==> Asegurando permisos de ejecución"
chmod +x "$STAGE/tools/speckit/preflight.sh" \
         "$STAGE/tools/speckit/specify" \
         "$STAGE/tools/speckit/shim/python3"

echo "==> Generando SHA256SUMS"
( cd "$STAGE" \
  && find . -type f ! -name 'SHA256SUMS' ! -name 'AGENTS.md' -print0 \
     | LC_ALL=C sort -z \
     | xargs -0 shasum -a 256 \
     | sed 's|  \./|  |' > SHA256SUMS )

echo "==> Verificando integridad recién generada"
( cd "$STAGE" && shasum -a 256 -c SHA256SUMS >/dev/null )

echo "==> Empaquetando la distribución"
( cd "$DIST" && zip -q -r -X "${NOMBRE}.zip" "$NOMBRE" )

total="$(grep -c . "$STAGE/SHA256SUMS")"
echo
echo "Paquete listo:"
echo "  directorio : dist/$NOMBRE"
echo "  ZIP        : dist/${NOMBRE}.zip"
echo "  archivos   : $total (verificados $total/$total)"
echo "  sha256 ZIP : $(shasum -a 256 "$DIST/${NOMBRE}.zip" | cut -d' ' -f1)"
