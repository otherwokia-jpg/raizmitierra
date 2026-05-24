#!/usr/bin/env python3
"""
RaízMiTierra — CMS Backend
Puerto 9500 · SSO desde Landing (8888)
Sirve el sitio público + /admin/ protegido para gestión de contenidos.
"""
import os, sys, json, re, shutil, secrets, hashlib
from pathlib import Path
from datetime import datetime, timedelta
from io import BytesIO

from dotenv import load_dotenv
import jwt
from flask import (
    Flask, send_from_directory, request, redirect, session,
    url_for, flash, render_template, jsonify, abort
)
from werkzeug.utils import secure_filename
from PIL import Image

load_dotenv()

# ── Paths ──
BASE_DIR = Path(__file__).parent.resolve()
PUBLIC_DIR = BASE_DIR / "public"
CORE_DIR = BASE_DIR / "core"
DB_DIR = BASE_DIR / "database"
DIST_DIR = BASE_DIR / "dist"
REVIEWS_DIR = DB_DIR / "reviews"
UPLOAD_DIR = PUBLIC_DIR / "assets" / "img" / "lugares"
CAT_FILE = CORE_DIR / "categories.json"
REG_FILE = CORE_DIR / "regions.json"
SSO_SECRET_FILE = Path(os.getenv('SSO_SECRET_FILE', str(Path.home() / '.sso_secret.key')))
USERS_FILE = Path(os.getenv('USERS_FILE', str(Path.home() / 'landing-portal' / 'users.json')))
PORTAL_KEY = "raizmitierra"
TOKEN_TTL = 300

# ── WSGI Middleware: strips /raiz prefix when accessed via Cloudflare ──
class PrefixMiddleware:
    """Strips the /raiz prefix from paths when accessed via cloudflare tunnel."""
    def __init__(self, app, prefix='/raiz'):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '')
        if path.startswith(self.prefix):
            environ['PATH_INFO'] = path[len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix

        def rewrite_location(status, headers, exc_info=None):
            new_headers = []
            for name, value in headers:
                if name.lower() == 'location' and value.startswith('/') and not value.startswith(self.prefix):
                    # Prepend the prefix to redirects so they go through the tunnel
                    value = self.prefix + value
                new_headers.append((name, value))
            return start_response(status, new_headers, exc_info)

        return self.app(environ, rewrite_location)

# ── Flask App ──
app = Flask(__name__,
    static_folder=str(PUBLIC_DIR),
    static_url_path='')
app.secret_key = os.environ.get('RAIZ_SECRET') or secrets.token_hex(32)
app.config['SESSION_COOKIE_NAME'] = 'session_raiz'
app.wsgi_app = PrefixMiddleware(app.wsgi_app)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

VALID_DAYS = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

# ── Helpers ──
def get_sso_secret():
    sso_file = os.environ.get('SSO_SECRET_FILE', str(Path.home() / '.sso_secret.key'))
    try:
        with open(sso_file) as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"⚠️ SSO_SECRET_FILE not found: {sso_file}")
        return None

def load_data():
    """Load compiled data.json from public/"""
    try:
        with open(PUBLIC_DIR / "data.json", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"lugares": [], "categories": [], "regions": {}, "meta": {"count": 0}}

def save_data(data):
    """Save compiled data.json (public + dist)"""
    with open(PUBLIC_DIR / "data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(DIST_DIR / "data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",",":"))
    js = "window.RAIZ_DATA=" + json.dumps(data, ensure_ascii=False, separators=(",",":")) + ";"
    with open(DIST_DIR / "data.js", "w", encoding="utf-8") as f:
        f.write(js)

def load_categories():
    try:
        with open(CAT_FILE, encoding="utf-8") as f:
            return json.load(f).get("categories", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_categories(cats):
    CORE_DIR.mkdir(parents=True, exist_ok=True)
    with open(CAT_FILE, "w", encoding="utf-8") as f:
        json.dump({"categories": cats}, f, ensure_ascii=False, indent=2)

def load_regions():
    try:
        with open(REG_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_regions(regs):
    CORE_DIR.mkdir(parents=True, exist_ok=True)
    with open(REG_FILE, "w", encoding="utf-8") as f:
        json.dump(regs, f, ensure_ascii=False, indent=2)

def load_reviews():
    """Load all pending reviews"""
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    reviews = []
    for f in sorted(REVIEWS_DIR.glob("*.json")):
        try:
            with open(f, encoding="utf-8") as fh:
                reviews.append(json.load(fh))
        except:
            pass
    return reviews

def save_review(review_data):
    """Save a single review"""
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    rid = review_data.get("id", secrets.token_hex(8))
    review_data["id"] = rid
    with open(REVIEWS_DIR / f"{rid}.json", "w", encoding="utf-8") as f:
        json.dump(review_data, f, ensure_ascii=False, indent=2)
    return rid

def get_place_md(place_id):
    """Find the .md file for a given place ID"""
    for md_file in DB_DIR.rglob("*.md"):
        content = md_file.read_text("utf-8")
        m = re.search(r'id:\s*"([^"]+)"', content)
        if m and m.group(1) == place_id:
            return md_file, content
    return None, None

def parse_md_content(content, filepath=None):
    """Parse a .md file content into a dict"""
    def g(pat, grp=1, flags=0):
        m = re.search(pat, content, flags)
        return m.group(grp) if m else None

    id_val = g(r'id:\s*"([^"]+)"')
    if not id_val:
        return None
    name = g(r'name:\s*"([^"]+)"') or "Sin nombre"
    region = g(r'region:\s*"([^"]+)"') or "desconocida"
    state = g(r'state:\s*"([^"]+)"') or "edomex"
    entry_type = g(r'type:\s*"([^"]+)"') or "tianguis"
    subtype = g(r'subtype:\s*"([^"]*)"') or ""
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
    horario = g(r'horario:\s*"([^"]*)"') or ""
    img = g(r'img:\s*"([^"]*)"') or ""
    hours = g(r'hours:\s*"([^"]*)"') or ""
    entrance_fee = g(r'entrance_fee:\s*"([^"]*)"') or ""
    activities = g(r'activities:\s*"([^"]*)"') or ""
    summary = g(r'> (.+?)\n') or ""
    pueblo_magico = g(r'pueblo_magico:\s*"([^"]*)"')
    pueblo_magico = pueblo_magico if pueblo_magico and pueblo_magico.strip() != "null" else None
    phone = g(r'phone:\s*"([^"]*)"') or ""
    address = g(r'address:\s*"([^"]*)"') or ""
    website = g(r'website:\s*"([^"]*)"') or ""

    return {
        "id": id_val, "name": name, "type": entry_type, "subtype": subtype,
        "region": region, "state": state, "days": days, "coords": coords,
        "categories": categories, "safety": safety, "horario": horario,
        "img": img, "summary": summary, "hours": hours,
        "entrance_fee": entrance_fee, "activities": activities,
        "pueblo_magico": pueblo_magico, "phone": phone,
        "address": address, "website": website
    }

def md_from_data(data):
    """Generate .md content from place data dict"""
    cats = ", ".join(f'"{c}"' for c in data.get("categories", []))
    days = ", ".join(f'"{d}"' for d in data.get("days", []))
    coords = f"[{data['coords'][0]}, {data['coords'][1]}]" if len(data.get("coords", [])) == 2 else "[]"

    lines = [
        "---",
        f'id: "{data["id"]}"',
        f'name: "{data["name"]}"',
        f'region: "{data.get("region", "desconocida")}"',
        f'state: "{data.get("state", "edomex")}"',
        f'type: "{data.get("type", "tianguis")}"',
    ]
    if data.get("subtype"):
        lines.append(f'subtype: "{data["subtype"]}"')
    if days:
        lines.append(f"days: [{days}]")
    if coords:
        lines.append(f"coords: {coords}")
    if data.get("categories"):
        lines.append(f"categories: [{cats}]")
    lines.append(f'safety: "{data.get("safety", "")}"')
    lines.append(f'horario: "{data.get("horario", "")}"')
    if data.get("img"):
        lines.append(f'img: "{data["img"]}"')
    if data.get("pueblo_magico"):
        lines.append(f'pueblo_magico: "{data["pueblo_magico"]}"')
    if data.get("phone"):
        lines.append(f'phone: "{data["phone"]}"')
    if data.get("address"):
        lines.append(f'address: "{data["address"]}"')
    if data.get("website"):
        lines.append(f'website: "{data["website"]}"')
    if data.get("hours"):
        lines.append(f'hours: "{data["hours"]}"')
    if data.get("entrance_fee"):
        lines.append(f'entrance_fee: "{data["entrance_fee"]}"')
    if data.get("activities"):
        lines.append(f'activities: "{data["activities"]}"')
    lines.append("---")
    lines.append("")
    lines.append(f"# {data.get('type_emoji', '📍')} {data['name']}")
    lines.append("")
    lines.append(f"> {data.get('summary', '')}")
    lines.append("")
    lines.append("## 📋 Información Rápida")
    lines.append("")
    if days:
        lines.append(f"| 📅 **Días** | {', '.join(data['days'])} |")
    if data.get("horario"):
        lines.append(f"| ⏰ **Horario** | {data['horario']} |")
    if data.get("hours"):
        lines.append(f"| 🕐 **Horario ext.** | {data['hours']} |")
    lines.append(f"| 📍 **Región** | {data.get('region', '')} — {data.get('state', '')} |")
    if data.get("address"):
        lines.append(f"| 🏠 **Dirección** | {data['address']} |")
    if data.get("phone"):
        lines.append(f"| 📞 **Teléfono** | {data['phone']} |")
    if data.get("website"):
        lines.append(f"| 🌐 **Web** | {data['website']} |")
    if data.get("entrance_fee"):
        lines.append(f"| 💰 **Costo** | {data['entrance_fee']} |")
    if data.get("activities"):
        lines.append(f"| 🎯 **Actividades** | {data['activities']} |")
    lines.append("")
    lines.append("## 📝 Descripción")
    lines.append("")
    lines.append(data.get("description", ""))
    lines.append("")

    return "\n".join(lines)

def run_build():
    """Run the build process — compiles .md → data.json"""
    import subprocess
    result = subprocess.run(
        [sys.executable, "cli.py", "build"],
        capture_output=True, text=True, cwd=str(BASE_DIR)
    )
    return result.stdout + result.stderr, result.returncode

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_photo(file, place_id):
    """Save and optimize photo, return URL path"""
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    ext = "webp"
    filename = f"{place_id}.{ext}"
    filepath = UPLOAD_DIR / filename

    img = Image.open(file)
    # Resize to max 800px
    if img.width > 800:
        ratio = 800 / img.width
        img = img.resize((800, int(img.height * ratio)), Image.LANCZOS)
    # Convert to RGB if needed
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(filepath, "WEBP", quality=82)

    return f"/assets/img/lugares/{filename}"

# ── SSO Auth Middleware ──
@app.before_request
def check_sso():
    path = request.path

    # ── SSO Token: procesar SIEMPRE antes de cualquier ruta ──
    sso_token = request.args.get("sso_token")
    if sso_token:
        try:
            payload = jwt.decode(sso_token, get_sso_secret(), algorithms=["HS256"])
            username = payload.get("username", "")
            allowed = payload.get("allowed_portals", [])
            if PORTAL_KEY in allowed or "raizmitierra" in allowed:
                session["authenticated"] = True
                session["username"] = username
                session["full_name"] = payload.get("full_name", username)
                session["email"] = payload.get("email", f"{username}@hubmultiteck.io")
                session["role"] = payload.get("role", "viewer")
                session["allowed_portals"] = allowed
                # Redirect limpio (sin sso_token en URL) a la dashboard admin
                # Si hay un parámetro 'next', úsalo; por defecto va a /admin/
                next_target = request.args.get("next", "/admin/")
                # Limpiar sso_token y next de la query string
                clean = {k: v for k, v in request.args.items() if k not in ("sso_token", "next")}
                qs = "&".join(f"{k}={v}" for k, v in clean.items())
                target = next_target + ("?" + qs if qs else "")
                return redirect(target)
        except Exception:
            pass

    # Rutas públicas: sitio frontend, assets, API pública
    public_prefixes = ("/static/", "/assets/", "/manifest.json", "/sw.js",
                      "/favicon.ico", "/data.json", "/preview-icon.html",
                      "/api/review", "/api/routes")
    if path in ("/", "/health", "/login", "/sso_login") or \
       any(path.startswith(p) for p in public_prefixes):
        return None

    # Rutas admin: require SSO (sesión ya establecida)
    if path.startswith("/admin"):
        if session.get("authenticated") and session.get("role") in ("superadmin", "admin"):
            return None
        return redirect(f"https://datacenter.hubmultiteck.io/login?next=https://datacenter.hubmultiteck.io/raiz/admin/")

    return None

# ── Static Routes ──
@app.route("/")
def index():
    return send_from_directory(str(PUBLIC_DIR), "index.html")

@app.route("/health")
def health():
    return jsonify({"status": "ok", "port": 9500, "portal": PORTAL_KEY})

@app.route("/api/admin-status")
def api_admin_status():
    """Return whether current session is admin (para el botón oculto)."""
    is_admin = session.get("authenticated") and session.get("role") in ("superadmin", "admin")
    return jsonify({
        "is_admin": is_admin,
        "username": session.get("username", ""),
        "full_name": session.get("full_name", "")
    })

@app.route("/sso_login")
def sso_login():
    sso_token = request.args.get("sso_token")
    if not sso_token:
        return redirect("https://datacenter.hubmultiteck.io/login?next=https://datacenter.hubmultiteck.io/raiz/")
    return redirect(f"/admin/?sso_token={sso_token}")

@app.route("/login")
def login_page():
    return redirect(f"https://datacenter.hubmultiteck.io/login?next=https://datacenter.hubmultiteck.io/raiz/admin/")

# ── Admin Dashboard ──
@app.route("/admin/")
def admin_dashboard():
    data = load_data()
    meta = data.get("meta", {})
    reviews = load_reviews()
    pending_reviews = len([r for r in reviews if r.get("status") == "pending"])
    return render_template("admin_dashboard.html",
        count=meta.get("count", 0),
        categories=len(data.get("categories", [])),
        regions=len(data.get("regions", {})),
        total_reviews=len(reviews),
        pending_reviews=pending_reviews,
        user=session.get("full_name", "Admin"),
        role=session.get("role", "admin")
    )

# ── Lugares CRUD ──
@app.route("/admin/lugares")
def admin_lugares():
    data = load_data()
    lugares = sorted(data.get("lugares", []), key=lambda x: x.get("name", ""))
    return render_template("admin_lugares.html", lugares=lugares,
        user=session.get("full_name", "Admin"))

@app.route("/admin/lugares/nuevo", methods=["GET", "POST"])
def admin_lugar_nuevo():
    if request.method == "GET":
        cats = load_categories()
        regs = load_regions()
        return render_template("admin_lugar_form.html",
            lugar=None, categories=cats, regions=regs,
            valid_days=VALID_DAYS, types=["tianguis","mercado","plaza",
                "pueblo_magico","balneario","cascada","zona_arqueologica",
                "mirador","centro_otomi","artesanias","trueque"],
            user=session.get("full_name", "Admin"))

    # POST — Create
    data = request.form
    place_id = data.get("id") or f"MX-{data.get('state','edomex').upper()[:4]}-{secrets.token_hex(3).upper()}"

    place = {
        "id": place_id,
        "name": data.get("name", "").strip(),
        "type": data.get("type", "tianguis"),
        "subtype": data.get("subtype", ""),
        "region": data.get("region", ""),
        "state": data.get("state", ""),
        "days": [d.strip() for d in data.get("days", "").split(",") if d.strip()],
        "coords": [float(data.get("lat", 0)), float(data.get("lng", 0))],
        "categories": [c.strip() for c in data.get("categories", "").split(",") if c.strip()],
        "safety": data.get("safety", ""),
        "horario": data.get("horario", ""),
        "hours": data.get("hours", ""),
        "entrance_fee": data.get("entrance_fee", ""),
        "activities": data.get("activities", ""),
        "summary": data.get("summary", ""),
        "description": data.get("description", ""),
        "phone": data.get("phone", ""),
        "address": data.get("address", ""),
        "website": data.get("website", ""),
        "pueblo_magico": data.get("pueblo_magico") or None,
        "img": ""
    }

    # Handle photo upload
    if "photo" in request.files and request.files["photo"].filename:
        file = request.files["photo"]
        if allowed_file(file.filename):
            img_url = save_photo(file, place_id)
            place["img"] = img_url

    # Determine save path by state/region
    state_dir = DB_DIR / place["state"]
    region_dir = state_dir / place["region"]
    region_dir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r'[^a-z0-9]+', '_', place["name"].lower()).strip("_")
    md_path = region_dir / f"{slug}.md"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_from_data(place))

    flash(f"✅ Lugar «{place['name']}» creado correctamente. Recompila para verlo.", "success")
    return redirect("/admin/")

@app.route("/admin/lugares/<place_id>/editar", methods=["GET", "POST"])
def admin_lugar_editar(place_id):
    md_file, content = get_place_md(place_id)
    if not md_file:
        flash("❌ Lugar no encontrado.", "error")
        return redirect("/admin/lugares")

    lugar = parse_md_content(content)
    if not lugar:
        flash("❌ Error al parsear el lugar.", "error")
        return redirect("/admin/lugares")

    if request.method == "GET":
        cats = load_categories()
        regs = load_regions()
        return render_template("admin_lugar_form.html",
            lugar=lugar, categories=cats, regions=regs,
            valid_days=VALID_DAYS, types=["tianguis","mercado","plaza",
                "pueblo_magico","balneario","cascada","zona_arqueologica",
                "mirador","centro_otomi","artesanias","trueque"],
            user=session.get("full_name", "Admin"))

    # POST — Update
    data = request.form
    updated = {
        "id": place_id,
        "name": data.get("name", lugar["name"]).strip(),
        "type": data.get("type", lugar["type"]),
        "subtype": data.get("subtype", lugar.get("subtype", "")),
        "region": data.get("region", lugar["region"]),
        "state": data.get("state", lugar["state"]),
        "days": [d.strip() for d in data.get("days", "").split(",") if d.strip()],
        "coords": [float(data.get("lat", 0)), float(data.get("lng", 0))],
        "categories": [c.strip() for c in data.get("categories", "").split(",") if c.strip()],
        "safety": data.get("safety", lugar.get("safety", "")),
        "horario": data.get("horario", lugar.get("horario", "")),
        "hours": data.get("hours", lugar.get("hours", "")),
        "entrance_fee": data.get("entrance_fee", lugar.get("entrance_fee", "")),
        "activities": data.get("activities", lugar.get("activities", "")),
        "summary": data.get("summary", lugar.get("summary", "")),
        "description": data.get("description", ""),
        "phone": data.get("phone", lugar.get("phone", "")),
        "address": data.get("address", lugar.get("address", "")),
        "website": data.get("website", lugar.get("website", "")),
        "pueblo_magico": data.get("pueblo_magico") or lugar.get("pueblo_magico"),
        "img": lugar.get("img", "")
    }

    # Handle photo upload
    if "photo" in request.files and request.files["photo"].filename:
        file = request.files["photo"]
        if allowed_file(file.filename):
            img_url = save_photo(file, place_id)
            updated["img"] = img_url

    # Delete old file, write new
    old_md = md_file
    state_dir = DB_DIR / updated["state"]
    region_dir = state_dir / updated["region"]
    region_dir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r'[^a-z0-9]+', '_', updated["name"].lower()).strip("_")
    new_md_path = region_dir / f"{slug}.md"

    with open(new_md_path, "w", encoding="utf-8") as f:
        f.write(md_from_data(updated))

    # Remove old file if path changed
    if old_md and old_md != new_md_path:
        try:
            old_md.unlink()
        except:
            pass

    flash(f"✅ Lugar «{updated['name']}» actualizado. Recompila para ver cambios.", "success")
    return redirect("/admin/lugares")

@app.route("/admin/lugares/<place_id>/borrar", methods=["POST"])
def admin_lugar_borrar(place_id):
    md_file, content = get_place_md(place_id)
    if md_file:
        md_file.unlink()
        flash(f"🗑️ Lugar eliminado.", "success")
    return redirect("/admin/lugares")

# ── Categorías ──
@app.route("/admin/categorias", methods=["GET", "POST"])
def admin_categorias():
    cats = load_categories()
    if request.method == "POST":
        action = request.form.get("action")
        if action == "nueva":
            new_cat = {
                "id": request.form.get("id", "").strip().lower().replace(" ", "-"),
                "label": request.form.get("label", "").strip(),
                "emoji": request.form.get("emoji", "📍"),
                "description": request.form.get("description", ""),
                "color": request.form.get("color", "#E86A33"),
                "bg": request.form.get("bg", "#FEF3C7"),
                "keywords": [k.strip() for k in request.form.get("keywords", "").split(",") if k.strip()]
            }
            cats.append(new_cat)
            save_categories(cats)
            flash(f"✅ Categoría «{new_cat['label']}» creada.", "success")
        elif action == "editar":
            cat_id = request.form.get("id")
            for c in cats:
                if c["id"] == cat_id:
                    c["label"] = request.form.get("label", c["label"])
                    c["emoji"] = request.form.get("emoji", c.get("emoji", "📍"))
                    c["description"] = request.form.get("description", c.get("description", ""))
                    c["color"] = request.form.get("color", c.get("color", "#E86A33"))
                    c["bg"] = request.form.get("bg", c.get("bg", "#FEF3C7"))
                    c["keywords"] = [k.strip() for k in request.form.get("keywords", "").split(",") if k.strip()]
                    break
            save_categories(cats)
            flash(f"✅ Categoría actualizada.", "success")
        elif action == "borrar":
            cat_id = request.form.get("id")
            cats = [c for c in cats if c["id"] != cat_id]
            save_categories(cats)
            flash(f"🗑️ Categoría eliminada.", "success")
        return redirect("/admin/categorias")

    return render_template("admin_categorias.html", categories=cats,
        user=session.get("full_name", "Admin"))

# ── Regiones ──
@app.route("/admin/regiones", methods=["GET", "POST"])
def admin_regiones():
    regs = load_regions()
    if request.method == "POST":
        action = request.form.get("action")
        if action == "nueva_region":
            state_id = request.form.get("state_id", "").strip().lower()
            state_name = request.form.get("state_name", "").strip()
            state_emoji = request.form.get("state_emoji", "📍")
            if state_id and state_id not in regs:
                regs[state_id] = {
                    "name": state_name,
                    "emoji": state_emoji,
                    "subregions": {}
                }
                save_regions(regs)
                flash(f"✅ Estado «{state_name}» creado.", "success")
        elif action == "editar_region":
            state_id = request.form.get("state_id")
            if state_id in regs:
                regs[state_id]["name"] = request.form.get("state_name", regs[state_id]["name"])
                regs[state_id]["emoji"] = request.form.get("state_emoji", regs[state_id].get("emoji", "📍"))
                save_regions(regs)
                flash(f"✅ Región actualizada.", "success")
        elif action == "borrar_region":
            state_id = request.form.get("state_id")
            if state_id in regs:
                del regs[state_id]
                save_regions(regs)
                flash(f"🗑️ Región eliminada.", "success")
        elif action == "nueva_subregion":
            state_id = request.form.get("state_id")
            sub_id = request.form.get("sub_id", "").strip().lower().replace(" ", "_")
            sub_name = request.form.get("sub_name", "").strip()
            if state_id in regs and sub_id and sub_id not in regs[state_id]["subregions"]:
                regs[state_id]["subregions"][sub_id] = sub_name
                save_regions(regs)
                flash(f"✅ Subregión «{sub_name}» creada.", "success")
        elif action == "borrar_subregion":
            state_id = request.form.get("state_id")
            sub_id = request.form.get("sub_id")
            if state_id in regs and sub_id in regs[state_id]["subregions"]:
                del regs[state_id]["subregions"][sub_id]
                save_regions(regs)
                flash(f"🗑️ Subregión eliminada.", "success")
        return redirect("/admin/regiones")

    return render_template("admin_regiones.html", regions=regs,
        user=session.get("full_name", "Admin"))

# ── Reseñas ──
@app.route("/api/review", methods=["POST"])
def api_submit_review():
    """Public endpoint to submit a review"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400

    place_id = data.get("place_id", "").strip()
    if not place_id:
        return jsonify({"error": "place_id requerido"}), 400

    review = {
        "id": secrets.token_hex(8),
        "place_id": place_id,
        "place_name": data.get("place_name", "").strip(),
        "author": data.get("author", "Anónimo").strip() or "Anónimo",
        "tipo": data.get("tipo", "#Comunitario"),
        "texto": data.get("texto", "").strip(),
        "rating": min(5, max(1, int(data.get("rating", 5)))),
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "ip": request.remote_addr or ""
    }

    if not review["texto"]:
        return jsonify({"error": "Texto de reseña requerido"}), 400

    save_review(review)
    return jsonify({"success": True, "message": "Reseña enviada. Pendiente de moderación."})

@app.route("/admin/resenas")
def admin_resenas():
    reviews = load_reviews()
    pending = [r for r in reviews if r.get("status") == "pending"]
    approved = [r for r in reviews if r.get("status") == "approved"]
    rejected = [r for r in reviews if r.get("status") == "rejected"]
    return render_template("admin_resenas.html",
        pending=pending, approved=approved, rejected=rejected,
        user=session.get("full_name", "Admin"))

@app.route("/admin/resenas/<review_id>/aprobar", methods=["POST"])
def admin_resena_aprobar(review_id):
    rpath = REVIEWS_DIR / f"{review_id}.json"
    if rpath.exists():
        with open(rpath, encoding="utf-8") as f:
            rev = json.load(f)
        rev["status"] = "approved"
        rev["moderated_at"] = datetime.now().isoformat()
        rev["moderated_by"] = session.get("username", "admin")
        with open(rpath, "w", encoding="utf-8") as f:
            json.dump(rev, f, ensure_ascii=False, indent=2)
        flash("✅ Reseña aprobada.", "success")
    return redirect("/admin/resenas")

@app.route("/admin/resenas/<review_id>/rechazar", methods=["POST"])
def admin_resena_rechazar(review_id):
    rpath = REVIEWS_DIR / f"{review_id}.json"
    if rpath.exists():
        with open(rpath, encoding="utf-8") as f:
            rev = json.load(f)
        rev["status"] = "rejected"
        rev["moderated_at"] = datetime.now().isoformat()
        rev["moderated_by"] = session.get("username", "admin")
        with open(rpath, "w", encoding="utf-8") as f:
            json.dump(rev, f, ensure_ascii=False, indent=2)
        flash("❌ Reseña rechazada.", "error")
    return redirect("/admin/resenas")

@app.route("/admin/resenas/<review_id>/borrar", methods=["POST"])
def admin_resena_borrar(review_id):
    rpath = REVIEWS_DIR / f"{review_id}.json"
    if rpath.exists():
        rpath.unlink()
        flash("🗑️ Reseña eliminada.", "success")
    return redirect("/admin/resenas")

# ── Build ──
@app.route("/admin/build", methods=["GET", "POST"])
def admin_build():
    result = ""
    success = False
    if request.method == "POST":
        output, code = run_build()
        result = output
        success = (code == 0)
        if success:
            flash(f"✅ Build completado. {result[:200]}", "success")
        else:
            flash(f"❌ Error en build: {result[:500]}", "error")
    return render_template("admin_build.html",
        result=result, success=success,
        user=session.get("full_name", "Admin"))

# ── Routes API (for walkable routes feature) ──
@app.route("/api/routes", methods=["GET"])
def api_routes():
    lat = request.args.get("lat", type=float)
    lng = request.args.get("lng", type=float)
    radius = request.args.get("radius", default=2, type=float)
    day = request.args.get("day", "")

    if not lat or not lng:
        return jsonify({"error": "lat y lng requeridos"}), 400

    data = load_data()
    near = []
    for lugar in data.get("lugares", []):
        c = lugar.get("coords", [])
        if len(c) != 2:
            continue
        # Rough distance calc (1° ≈ 111km)
        dlat = abs(c[0] - lat)
        dlng = abs(c[1] - lng)
        dist_km = ((dlat**2 + dlng**2)**0.5) * 111
        if dist_km <= radius:
            lugar["distance_km"] = round(dist_km, 1)
            if day:
                lugar_days = [d.lower() for d in lugar.get("days", [])]
                if day.lower() not in lugar_days:
                    continue
            near.append(lugar)

    near.sort(key=lambda x: x["distance_km"])
    return jsonify({"places": near[:20], "count": len(near), "radius": radius})

# ── Serve static files from public/ ──
@app.route("/<path:path>")
def serve_static(path):
    file_path = PUBLIC_DIR / path
    if file_path.exists() and file_path.is_file():
        return send_from_directory(str(PUBLIC_DIR), path)
    # Fallback to index.html for SPA-like routing
    return send_from_directory(str(PUBLIC_DIR), "index.html")

# ── Run ──
if __name__ == "__main__":
    port = int(os.getenv('PORT', '9500'))
    debug = os.getenv('DEBUG', 'false').lower() == 'true'
    print(f"🌿 RaízMiTierra CMS — SSO {PORTAL_KEY}")
    print(f"   Admin: http://192.168.0.111:{port}/admin/")
    print(f"   Site:  http://192.168.0.111:{port}/")
    app.run(host='0.0.0.0', port=port, debug=debug)
