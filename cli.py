#!/usr/bin/env python3
"""RAIZMITIERRA CLI - compile, validate, serve."""
import os, sys, json, re, time
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

BASE_DIR = Path(__file__).parent
CORE_DIR = BASE_DIR / "core"
DB_DIR = BASE_DIR / "database"
DIST_DIR = BASE_DIR / "dist"
PUBLIC_DIR = BASE_DIR / "public"
CAT_FILE = CORE_DIR / "categories.json"
REG_FILE = CORE_DIR / "regions.json"
VALID_DAYS = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
DIAS_MAP = {"Lunes":"Lunes","Martes":"Martes","Miercoles":"Miercoles","Miercoles":"Miercoles",
            "Jueves":"Jueves","Viernes":"Viernes","Sabado":"Sabado","Domingo":"Domingo"}

# ── resumenes culturales ──
RESUMENES = {
    "#Sabor": [
        "Capturan los sabores tradicionales del lugar. Llegar con hambre!",
        "Recorrido visual por los platillos tipicos. Ideal para decidir que probar.",
        "Comida callejera en su maximo esplendor. No veas con el estomago vacio.",
    ],
    "#Precio": [
        "Los locales surten su despensa aqui. Comparativas que ahorran dinero.",
        "Los mejores precios del tianguis. La tradicion de regatear sigue viva.",
        "Testimonios de compradores. Economia familiar y tianguis van de la mano.",
    ],
    "#Artesania": [
        "Artesanos que mantienen vivas las tradiciones. Cada pieza cuenta una historia.",
        "Tecnicas heredadas de abuelos que siguen vigentes. El orgullo de lo hecho a mano.",
        "Transforman materiales en obras de arte. Conoce su trabajo directamente.",
    ],
    "#Cultura": [
        "Tradiciones que dan identidad a la comunidad. Musica, costumbres y rituales.",
        "Expresiones culturales del lugar. Aqui el tianguis es mas que comercio: es encuentro.",
        "Herencia cultural viva: danzas, rezos y celebraciones del tianguis.",
    ],
    "#Tradicion": [
        "Tradiciones arraigadas del lugar. Costumbres que pasan de padres a hijos.",
        "Celebraciones tradicionales que rodean el tianguis. Cultura viva.",
    ],
    "#Acceso": [
        "Como llegar y los mejores horarios. Tips de los que ya conocen el lugar.",
        "Guia practica: transporte, estacionamiento y la mejor hora para tu visita.",
    ],
    "#Seguridad": [
        "La comunidad comparte su experiencia sobre la seguridad en la zona.",
        "Testimonios de quienes asisten regularmente. Ambiente familiar.",
    ],
    "#Trueque": [
        "Trueque: tradicion prehispanica que sigue viva. Intercambian sin usar dinero.",
        "Intercambio directo entre campesinos y compradores. Practica que resiste.",
    ],
    "#Chacharas": [
        "Objetos unicos que cuentan historias. Cada puesto es una capsula del tiempo.",
        "Coleccionistas y curiosos comparten sus hallazgos. Tesoros escondidos.",
    ],
}

def _resumen(tipo, nombre, region):
    opts = RESUMENES.get(tipo, ["La comunidad comparte su experiencia en este tianguis."])
    idx = abs(hash(nombre + tipo)) % len(opts)
    return opts[idx]

# ── parse .md ──
def parse_md(filepath):
    content = filepath.read_text("utf-8")
    
    def g(pat, grp=1, flags=0):
        m = re.search(pat, content, flags)
        return m.group(grp) if m else None
    
    id_val = g(r'id:\s*"([^"]+)"')
    if not id_val:
        return None, f"Falta id: {filepath.name}"
    
    name = g(r'name:\s*"([^"]+)"') or "Sin nombre"
    region = g(r'region:\s*"([^"]+)"') or "desconocida"
    state = g(r'state:\s*"([^"]+)"') or "edomex"
    
    dm = g(r'days:\s*\[(.+)\]')
    days = [d.strip().strip('"') for d in dm.split(",")] if dm else []
    
    cm = g(r'coords:\s*\[([^\]]+)\]')
    try:
        coords = [float(x.strip()) for x in cm.split(",")] if cm else []
    except:
        coords = []
    
    cats_m = g(r'categories:\s*\[(.+)\]')
    categories = [c.strip().strip('"') for c in cats_m.split(",")] if cats_m else []
    
    safety = g(r'safety:\s*"([^"]*)"') or ""
    horario = g(r'horario:\s*"([^"]*)"') or "6:00 AM"
    pm = g(r'pueblo_magico:\s*"?([^"\n,]+)"?')
    pueblo_magico = pm.strip() if pm and pm.strip() != "null" else None
    img = g(r'img:\s*"?([^"\n]+)"?') or ""
    
    summary = g(r'> (.+?)\n') or ""
    
    # best_route
    best_route = {}
    rt = g(r'## 🚗 Cómo Llegar\n(.+?)(?=\n##|\Z)', 1, re.DOTALL)
    if rt:
        pm = re.search(r'🅿️.*?\n(.+?)(?:\n|$)', rt)
        tm = re.search(r'Recomendación.*?\n(.+?)(?:\n|$)', rt)
        if pm: best_route["parking"] = pm.group(1).strip()
        if tm: best_route["tip"] = tm.group(1).strip()
    
    # ── commentarios ──
    comentarios = []
    cs = re.search(r'## 💬 Bitácora Comunitaria\n(.+?)(?=\n## 🚗|\Z)', content, re.DOTALL)
    if cs:
        blocks = cs.group(1).split("###")
        for block in blocks[1:]:
            tipo = re.search(r'\*\*Tipo:\*\*\s*(.+?)(?:\n|$)', block)
            texto = re.search(r'> \*?"?([^"]+)"?\*?', block)
            link = re.search(r'Evidencia.*?\]\(([^)]+)\)', block)
            recon = re.search(r'\*\*Recomendación:\*\*\s*(.+?)(?:\n|$)', block)
            if texto:
                raw = texto.group(1).strip().lstrip('*"').rstrip('*" ').strip()
                t = tipo.group(1).strip() if tipo else "#Comunitario"
                comentarios.append({
                    "tipo": t,
                    "texto": raw,
                    "link": link.group(1) if link else "",
                    "resumen": _resumen(t, name, region),
                    "recomendacion": recon.group(1).strip() if recon else "",
                })
    
    return {
        "id": id_val, "name": name, "region": region, "state": state,
        "days": days, "coords": coords, "categories": categories,
        "safety": safety, "horario": horario, "pueblo_magico": pueblo_magico,
        "img": img, "summary": summary, "best_route": best_route,
        "comentarios": comentarios[:10],
    }, None

# ── build ──
def cmd_build():
    print("RAIZMITIERRA - Build\n")
    with open(CAT_FILE) as f: cats_data = json.load(f)
    with open(REG_FILE) as f: regs_data = json.load(f)
    valid_cats = {c["id"] for c in cats_data["categories"]}
    valid_regions = set()
    for sd in regs_data.values():
        for sub in sd.get("subregions", {}): valid_regions.add(sub)
    
    tianguis_list, errors, warnings = [], [], []
    for md_file in sorted(DB_DIR.rglob("*.md")):
        rel = md_file.relative_to(DB_DIR)
        print(f"  {rel}", end="")
        data, err = parse_md(md_file)
        if err: print(f"  {err}"); errors.append(err); continue
        if not data["coords"] or len(data["coords"]) != 2:
            e = f"Sin coords: {rel}"; print(f"  {e}"); errors.append(e); continue
        if not data["days"]:
            e = f"Sin dias: {rel}"; print(f"  {e}"); errors.append(e); continue
        cc = len(data["comentarios"])
        print(f"  OK {data['name']} ({cc} comentarios)")
        tianguis_list.append(data)
    
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    output = {
        "meta": {"name": "RaizMiTierra", "version": "1.0.0",
                 "generated": datetime.now().isoformat(), "count": len(tianguis_list),
                 "count_by_region": {}},
        "tianguis": tianguis_list,
        "categories": cats_data["categories"],
        "regions": regs_data
    }
    for t in tianguis_list:
        r = t["region"]
        output["meta"]["count_by_region"][r] = output["meta"]["count_by_region"].get(r, 0) + 1
    for fp in [DIST_DIR / "data.json", PUBLIC_DIR / "data.json"]:
        with open(fp, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
    fs = (DIST_DIR / "data.json").stat().st_size
    tc = sum(len(t["comentarios"]) for t in tianguis_list)
    print(f"\nOK: {len(tianguis_list)} tianguis, {tc} comentarios, {fs:,} bytes")

# ── serve ──
def cmd_serve():
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 9500
    os.chdir(PUBLIC_DIR)
    HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler).serve_forever()

if __name__ == "__main__":
    if len(sys.argv) < 2: print(__doc__); sys.exit(1)
    {"build": cmd_build, "serve": cmd_serve}.get(sys.argv[1], lambda: print("?"))()
