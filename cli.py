#!/usr/bin/env python3
"""
🌎 RAÍZMITIERRA — CLI de compilación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Herramienta de línea de comandos para compilar, validar y servir
el mapa comunitario de tianguis y Pueblos Mágicos del Edomex.

Uso:
    python cli.py build        → Compila .md → dist/data.json
    python cli.py validate     → Valida integridad de todos los .md
    python cli.py watch        → Recompila automático al editar .md
    python cli.py serve        → Servidor local en :9500
    python cli.py stats        → Estadísticas del contenido
"""

import os
import sys
import json
import re
import hashlib
import time
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

# ── Rutas base ──
BASE_DIR = Path(__file__).parent
CORE_DIR = BASE_DIR / "core"
DB_DIR = BASE_DIR / "database"
DIST_DIR = BASE_DIR / "dist"
PUBLIC_DIR = BASE_DIR / "public"

VALID_DAYS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
CATEGORIES_FILE = CORE_DIR / "categories.json"
REGIONS_FILE = CORE_DIR / "regions.json"

# ═══════════════════════════════════════════════════════════
# ⚡ PARSEAR UN ARCHIVO .md
# ═══════════════════════════════════════════════════════════

def parse_md(filepath):
    content = filepath.read_text(encoding="utf-8")
    id_match = re.search(r'id:\s*"([^"]+)"', content)
    if not id_match:
        return None, f"❌ {filepath.name}: Falta id:"
    id_val = id_match.group(1)

    name_match = re.search(r'name:\s*"([^"]+)"', content)
    region_match = re.search(r'region:\s*"([^"]+)"', content)
    days_match = re.search(r'days:\s*\[(.+)\]', content)
    coords_match = re.search(r'coords:\s*\[([^\]]+)\]', content)
    cats_match = re.search(r'categories:\s*\[(.+)\]', content)
    safety_match = re.search(r'safety:\s*"([^"]*)"', content)
    horario_match = re.search(r'horario:\s*"([^"]*)"', content)
    pm_match = re.search(r'pueblo_magico:\s*"?([^"\n,]+)"?', content)
    img_match = re.search(r'img:\s*"?([^"\n]+)"?', content)

    name = name_match.group(1) if name_match else "Sin nombre"
    region = region_match.group(1) if region_match else "desconocida"
    days = [d.strip().strip('"') for d in days_match.group(1).split(",")] if days_match else []
    try:
        coords = [float(x.strip()) for x in coords_match.group(1).split(",")] if coords_match else []
    except:
        coords = []
    categories = [c.strip().strip('"') for c in cats_match.group(1).split(",")] if cats_match else []
    safety = safety_match.group(1) if safety_match else ""
    horario = horario_match.group(1) if horario_match else "6:00 AM"
    pueblo_magico = pm_match.group(1).strip() if pm_match and pm_match.group(1) != "null" else None
    img = img_match.group(1).strip() if img_match else ""

    # Extraer resumen (primer párrafo después del blockquote)
    summary = ""
    summary_match = re.search(r'> (.+?)\n', content)
    if summary_match:
        summary = summary_match.group(1)

    # Extraer cómo llegar
    best_route = {}
    route_text = re.search(r'## 🚗 Cómo Llegar\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    if route_text:
        rt = route_text.group(1)
        from_cdmx_m = re.search(r'Ruta desde CDMX.*?\n(.+?)(?:\n|$)', rt)
        sin_caseta_m = re.search(r'Ruta sin caseta.*?\n(.+?)(?:\n|$)', rt)
        parking_m = re.search(r'🅿️.*?\n(.+?)(?:\n|$)', rt)
        tip_m = re.search(r'Llegar\s*(.+?)(?:\n|$)', rt)
        if from_cdmx_m: best_route['from_cdmx'] = from_cdmx_m.group(1).strip()
        if sin_caseta_m: best_route['sin_caseta'] = sin_caseta_m.group(1).strip()
        if parking_m: best_route['parking'] = parking_m.group(1).strip()
        if tip_m: best_route['tip'] = tip_m.group(1).strip()

    # Extraer POIs
    pois = []
    poi_section = re.search(r'## 🏪 Sitios de Interés Cercanos\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    if poi_section:
        for line in poi_section.group(1).strip().split('\n'):
            line = line.strip()
            m = re.match(r'[-*]\s*\*?\*?(.+?)\*?\*?\s*[—–-]\s*(.+)$', line)
            if m:
                pois.append({"name": m.group(1).strip(), "description": m.group(2).strip()})

    # Extraer comentarios
    comentarios = []
    comment_section = re.search(r'## 💬 Bitácora Comunitaria\n(.+?)(?=\n## 🚗|\Z)', content, re.DOTALL)
    if comment_section:
        blocks = re.split(r'\n###\s+', comment_section.group(1))
        for block in blocks:
            tipo_m = re.search(r'\*\*Tipo:\*\*\s*(.+?)(?:\n|$)', block)
            fecha_m = re.search(r'\*\*Fecha:\*\*\s*(.+?)(?:\n|$)', block)
            texto_m = re.search(r'> \*?"?(.+?)"?\*?', block)
            link_m = re.search(r'Evidencia.*?\[([^\]]+)\]\(([^)]+)\)', block)
            if texto_m:
                comentarios.append({
                    "tipo": tipo_m.group(1).strip() if tipo_m else "#Comunitario",
                    "fecha": fecha_m.group(1).strip() if fecha_m else "",
                    "texto": texto_m.group(1).strip() if texto_m else "",
                    "link": link_m.group(2) if link_m else ""
                })

    return {
        "id": id_val,
        "name": name,
        "region": region,
        "days": days,
        "coords": coords,
        "categories": categories,
        "safety": safety,
        "horario": horario,
        "pueblo_magico": pueblo_magico,
        "img": img,
        "summary": summary,
        "best_route": best_route,
        "pois": pois,
        "comentarios": comentarios[:10],  # Máximo 10
    }, None

# ═══════════════════════════════════════════════════════════
# 📦 COMANDO: build
# ═══════════════════════════════════════════════════════════

def cmd_build():
    print("🌎 RAÍZMITIERRA — Build\n")

    # Cargar categorías y regiones
    with open(CATEGORIES_FILE) as f:
        cats_data = json.load(f)
    with open(REGIONS_FILE) as f:
        regs_data = json.load(f)

    valid_cats = {c["id"] for c in cats_data["categories"]}
    valid_regions = {r["id"] for r in regs_data["regions"]}

    tianguis_list = []
    errors = []
    warnings = []

    # Recorrer database/
    for md_file in sorted(DB_DIR.rglob("*.md")):
        rel = md_file.relative_to(DB_DIR)
        print(f"  📄 {rel}", end="")

        data, err = parse_md(md_file)
        if err:
            print(f"  {err}")
            errors.append(err)
            continue

        # Validaciones
        if data["region"] not in valid_regions:
            w = f"  ⚠️  {rel}: región '{data['region']}' no existe en regions.json"
            print(w)
            warnings.append(w)

        bad_cats = [c for c in data["categories"] if c not in valid_cats]
        if bad_cats:
            w = f"  ⚠️  {rel}: categorías inválidas: {bad_cats}"
            print(w)
            warnings.append(w)

        bad_days = [d for d in data["days"] if d not in VALID_DAYS]
        if bad_days:
            w = f"  ⚠️  {rel}: días inválidos: {bad_days}"
            print(w)
            warnings.append(w)

        if not data["coords"] or len(data["coords"]) != 2:
            e = f"  ❌ {rel}: coordenadas inválidas"
            print(e)
            errors.append(e)
            continue

        if not data["days"]:
            e = f"  ❌ {rel}: sin días"
            print(e)
            errors.append(e)
            continue

        print(f"  ✅ {data['name']} — {', '.join(data['days'])}")
        tianguis_list.append(data)

    # Generar data.json
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    output = {
        "meta": {
            "name": "RaízMiTierra",
            "version": "1.0.0",
            "generated": datetime.now().isoformat(),
            "count": len(tianguis_list),
            "count_by_region": {}
        },
        "tianguis": tianguis_list,
        "categories": cats_data["categories"],
        "regions": regs_data["regions"]
    }

    # Contar por región
    for t in tianguis_list:
        r = t["region"]
        output["meta"]["count_by_region"][r] = output["meta"]["count_by_region"].get(r, 0) + 1

    data_path = DIST_DIR / "data.json"
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    file_size = data_path.stat().st_size
    print(f"\n📦 data.json → {file_size:,} bytes ({len(tianguis_list)} tianguis)")
    if errors:
        print(f"❌ {len(errors)} errores")
    if warnings:
        print(f"⚠️  {len(warnings)} advertencias")
    print(f"✅ Build completado!")

# ═══════════════════════════════════════════════════════════
# ✅ COMANDO: validate
# ═══════════════════════════════════════════════════════════

def cmd_validate():
    print("🔍 RAÍZMITIERRA — Validación\n")

    with open(CATEGORIES_FILE) as f:
        cats_data = json.load(f)
    with open(REGIONS_FILE) as f:
        regs_data = json.load(f)

    valid_cats = {c["id"] for c in cats_data["categories"]}
    valid_regions = {r["id"] for r in regs_data["regions"]}

    ids = set()
    total = 0
    errors = 0
    warnings = 0

    for md_file in sorted(DB_DIR.rglob("*.md")):
        total += 1
        rel = md_file.relative_to(DB_DIR)
        data, err = parse_md(md_file)
        if err:
            print(f"  ❌ {rel}: {err}")
            errors += 1
            continue

        # ID único
        if data["id"] in ids:
            print(f"  ❌ {rel}: ID duplicado '{data['id']}'")
            errors += 1
        ids.add(data["id"])

        # Región
        if data["region"] not in valid_regions:
            print(f"  ❌ {rel}: región '{data['region']}' no válida")
            errors += 1

        # Categorías
        bad_cats = [c for c in data["categories"] if c not in valid_cats]
        if bad_cats:
            print(f"  ❌ {rel}: categorías inválidas: {bad_cats}")
            errors += 1

        # Días
        bad_days = [d for d in data["days"] if d not in VALID_DAYS]
        if bad_days:
            print(f"  ❌ {rel}: días inválidos: {bad_days}")
            errors += 1

        # Coordenadas en Edomex (aproximado)
        lat, lon = data["coords"] if len(data["coords"]) == 2 else (0, 0)
        if not (17.5 <= lat <= 20.5 and -101.0 <= lon <= -98.0):
            print(f"  ⚠️  {rel}: coordenadas fuera de Edomex ({lat}, {lon})")
            warnings += 1

        print(f"  ✅ {rel} — {data['name']}")

    print(f"\n📊 {total} archivos, {errors} errores, {warnings} advertencias")
    return errors == 0

# ═══════════════════════════════════════════════════════════
# 👁️ COMANDO: watch
# ═══════════════════════════════════════════════════════════

def cmd_watch():
    print("👁️  RAÍZMITIERRA — Watch mode\n")
    print("  Observando cambios en database/...")
    print("  Presiona Ctrl+C para salir\n")

    last_build = 0
    while True:
        latest = max(
            (f.stat().st_mtime for f in DB_DIR.rglob("*.md")),
            default=0
        )
        if latest > last_build:
            last_build = time.time()
            print(f"\n  🔄 Cambio detectado a las {datetime.now().strftime('%H:%M:%S')}")
            cmd_build()
            print("\n  👁️  Esperando cambios...")
        time.sleep(1)

# ═══════════════════════════════════════════════════════════
# 🚀 COMANDO: serve
# ═══════════════════════════════════════════════════════════

def cmd_serve():
    port = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == "serve" else 9500

    os.chdir(PUBLIC_DIR)
    server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    print(f"\n🚀 RAÍZMITIERRA — Servidor local")
    print(f"  → http://localhost:{port}")
    print(f"  → http://0.0.0.0:{port}")
    print(f"  Presiona Ctrl+C para detener\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido.")

# ═══════════════════════════════════════════════════════════
# 📊 COMANDO: stats
# ═══════════════════════════════════════════════════════════

def cmd_stats():
    print("📊 RAÍZMITIERRA — Estadísticas\n")

    md_files = list(DB_DIR.rglob("*.md"))
    json_files = list(DB_DIR.rglob("*.json"))

    print(f"  📄 Archivos .md:     {len(md_files)}")
    print(f"  📋 Archivos .json:   {len(json_files)}")

    if DIST_DIR.exists():
        data_file = DIST_DIR / "data.json"
        if data_file.exists():
            with open(data_file) as f:
                data = json.load(f)
            t = data.get("tianguis", [])
            print(f"\n  🌎 Tianguis compilados: {len(t)}")
            print(f"  🏆 Pueblos Mágicos: {sum(1 for x in t if x.get('pueblo_magico'))}")
            print(f"  💬 Comentarios totales: {sum(len(x.get('comentarios', [])) for x in t)}")
            print(f"\n  📦 data.json: {data_file.stat().st_size:,} bytes")
            print(f"  🕐 Generado: {data['meta']['generated']}")

    print()

# ═══════════════════════════════════════════════════════════
# 🎯 MAIN
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "build":
        cmd_build()
    elif command == "validate":
        if not cmd_validate():
            sys.exit(1)
    elif command == "watch":
        cmd_watch()
    elif command == "serve":
        cmd_serve()
    elif command == "stats":
        cmd_stats()
    else:
        print(f"❌ Comando desconocido: {command}")
        print(__doc__)
        sys.exit(1)
