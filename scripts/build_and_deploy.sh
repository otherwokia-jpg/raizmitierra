#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────
# build_and_deploy.sh — RaízMiTierra Build & Deploy Pipeline
# Uso: ./scripts/build_and_deploy.sh [--no-deploy]
# ──────────────────────────────────────────────────────────────
set -euo pipefail

BASE_DIR="$HOME/raizmitierra"
LOG_FILE="$BASE_DIR/build_and_deploy.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

log "=== RaízMiTierra Build & Deploy ==="

# ── 1. Ir al directorio del proyecto ──
cd "$BASE_DIR"
log "Working directory: $(pwd)"

# ── 2. Construir el data.json ──
log "Ejecutando: python3 cli.py build"
python3 cli.py build 2>&1 | tee -a "$LOG_FILE"

BUILD_EXIT=${PIPESTATUS[0]}
if [ $BUILD_EXIT -ne 0 ]; then
    log "ERROR: Build falló con código $BUILD_EXIT"
    exit $BUILD_EXIT
fi
log "Build completado exitosamente"

# ── 3. Copiar data.json a public/ ──
log "Copiando dist/data.json → public/data.json"
cp dist/data.json public/data.json

# ── 4. Verificar integridad del JSON ──
log "Verificando integridad del JSON..."
python3 -c "
import json, sys
with open('dist/data.json') as f:
    data = json.load(f)
lugares = data.get('lugares', [])
meta = data.get('meta', {})
print(f'  Lugares: {len(lugares)}')
print(f'  Tipos: {meta.get(\"count_by_type\", {})}')
print(f'  Generado: {meta.get(\"generated\", \"?\")}')
# Check for duplicate IDs
ids = [l['id'] for l in lugares]
dupes = set([id for id in ids if ids.count(id) > 1])
if dupes:
    print(f'  ADVERTENCIA: {len(dupes)} IDs duplicados: {sorted(dupes)[:5]}...')
else:
    print(f'  Sin duplicados de ID')
sys.exit(0)
" 2>&1 | tee -a "$LOG_FILE"

log "=== Build & Deploy completado ==="
echo ""
echo "dist/data.json: $(ls -lh dist/data.json | awk '{print $5}')"
echo "public/data.json: $(ls -lh public/data.json | awk '{print $5}')"
echo ""
