# 🌎 RaízMiTierra

> *Caminar, conocer, comer y defender las costumbres de nuestra tierra.*

**RaízMiTierra** es una plataforma comunitaria, anónima y **antigentrificación** para descubrir tianguis, trueque, barbacoa de hoyo, balnearios populares, artesanías y Pueblos Mágicos del Estado de México.

**100% privada.** Tu ubicación nunca sale de tu teléfono.

---

## 📋 Estado del Proyecto

| Componente | Estado |
|---|---|
| `index.html` — App PWA completa | ✅ Funcionando |
| `cli.py` — Compilador/validador | ✅ Funcionando |
| `categories.json` — 12 categorías oficiales | ✅ Completado |
| `regions.json` — 5 regiones del Edomex | ✅ Completado |
| `pueblos_magicos.json` — 12 Pueblos Mágicos | ✅ Completado |
| 1er tianguis: Santiago Tianguistengo (.md) | ✅ Completado |
| `data.json` — Compilado | ✅ 10.8 KB |
| `sw.js` — Service Worker (offline) | ✅ Listo |
| `manifest.json` — PWA instalable | ✅ Listo |
| **Servidor local :9500** | ✅ **¡En vivo!** |

---

## 🚀 Inicio Rápido

```bash
# 1. Servir en local
cd ~/raizmitierra
python3 cli.py build        # Compilar .md → dist/data.json
cp dist/data.json public/   # Copiar a la carpeta pública
python3 cli.py serve 9500   # http://localhost:9500

# 2. En otra terminal, validar estructura
python3 cli.py validate

# 3. Modo desarrollo (recompila automático)
python3 cli.py watch
```

---

## 📁 Estructura del Proyecto

```
📁 ~/raizmitierra/
│
├── cli.py                  ← ⚡ Compilador, validador, servidor
│
├── core/                   ← ⭐ Datos maestros
│   ├── categories.json     → 12 categorías con emojis, colores, keywords
│   ├── regions.json        → 5 regiones del Edomex
│   └── pueblos_magicos.json→ 12 Pueblos Mágicos oficiales
│
├── database/               ← ⭐ Fuente de verdad (.md editables)
│   ├── valle_toluca/
│   │   ├── tianguistengo.md  ← Ejemplo completo con 10 bitácoras
│   │   └── ...
│   ├── norte_bosques/
│   ├── valle_mexico/
│   ├── pueblos_magicos/
│   └── sitios_interes/
│
├── dist/                   ← Compilado por cli.py
│   └── data.json           → Se copia a public/ para servir
│
├── public/                 ← ← ← SE SIRVE AL MUNDO
│   ├── index.html          → App PWA completa
│   ├── data.json           → Catálogo compilado de tianguis
│   ├── manifest.json       → PWA instalable
│   ├── sw.js               → Service Worker (offline)
│   └── assets/
│       ├── icons/
│       └── maps/
│
├── tests/
└── README.md
```

---

## 🔐 Seguridad y Privacidad

### Arquitectura de Privacidad Absoluta

```
📱 TELÉFONO DEL USUARIO
┌─────────────────────────────────────────────┐
│                                             │
│  1. Descarga data.json (única petición HTTP) │
│                                             │
│  2. GPS: watchPosition() — interno          │
│     └── Habla directo con satélites         │
│     └── NUNCA sale del navegador            │
│                                             │
│  3. Búsquedas: en RAM del teléfono          │
│     └── Sin consultas a servidor            │
│     └── Sin AJAX, sin WebSocket             │
│                                             │
│  4. Mapa: Leaflet.js + OpenStreetMap        │
│     └── Tiles públicos, sin tracking         │
│                                             │
│  🔒 NADIE SABE: ubicación, ruta, búsquedas  │
└─────────────────────────────────────────────┘
```

### Medidas de Seguridad Implementadas

| Medida | Implementación |
|---|---|
| **Sin backend** | 100% archivos estáticos. No hay servidor de aplicaciones. |
| **Sin base de datos de usuarios** | No hay registro, login, cookies de sesión ni perfiles. |
| **GPS solo en cliente** | `navigator.geolocation.watchPosition` — cero datos al servidor. |
| **Sin analytics** | No Google Analytics, no Facebook Pixel, no cookies de terceros. |
| **CSP Headers** | Content-Security-Policy en el HTML restringe scripts a CDNs confiables. |
| **Subresource Integrity** | Leaflet cargado con `integrity` hash para evitar manipulación de CDN. |
| **HTTPS** | Cloudflare provee SSL/TLS automático. |
| **Service Worker scope** | Limitado a `/` — no intercepta recursos externos. |
| **Sin formularios** | No hay POST, no hay inyección, no hay XSS desde servidor. |
| **Sin almacenamiento de ubicación** | No se usa `localStorage` ni `IndexedDB` para datos de GPS. |

### Riesgos Mitigados

| Riesgo | Mitigación |
|---|---|
| Fuga de ubicación | 🟢 **Imposible** — el GPS opera 100% en el navegador |
| Hackeo de base de datos | 🟢 **No hay BD** — solo archivos JSON estáticos |
| Venta de datos a inmobiliarias | 🟢 **No hay datos que vender** |
| Tracking entre sesiones | 🟢 **Sin cookies, sin fingerprints** |
| Inyección XSS | 🟢 No hay inputs que se envíen al servidor |
| DDoS | 🟢 Cloudflare lo absorbe |

---

## ☁️ Despliegue a Cloudflare (Futuro)

### Opción A: Cloudflare Pages (Recomendada — Gratis)

```bash
# 1. Conectar repo Git
cd ~/raizmitierra
git init
git add .
git commit -m "🌎 RaízMiTierra: lanzamiento inicial"

# 2. Subir a GitHub/GitLab
gh repo create raizmitierra --public --push

# 3. En Cloudflare Dashboard:
#    → Pages → Crear proyecto
#    → Conectar repositorio
#    → Build: (ninguno — es estático)
#    → Output: /public
#    → Dominio: raizmitierra.mx

# 4. ¡Listo!
#    https://raizmitierra.pages.dev  (subdominio temporal)
#    https://raizmitierra.mx         (dominio personalizado)
```

### Opción B: Cloudflare Tunnel (Si prefieres tu servidor)

```bash
# 1. En ~/.cloudflared/config.yml agregar:
#    - hostname: raizmitierra.mx
#      service: http://localhost:9500

# 2. DNS: apuntar raizmitierra.mx → tunnel
# 3. En el servidor: python3 cli.py serve 9500

# 4. Cache de Cloudflare:
#    - Regla de Page Rule: raizmitierra.mx/*
#    - Cache Level: Standard
#    - Edge Cache TTL: 1 día
```

### Configuración Recomendada de Cloudflare

| Ajuste | Valor |
|---|---|
| SSL/TLS | Full (strict) |
| Always Use HTTPS | ✅ ON |
| Brotli Compression | ✅ ON |
| Auto Minify | HTML, JS, CSS |
| Cache Level | Standard |
| Edge Cache TTL | 1 día |
| Security Level | Medium |
| Bot Fight Mode | ✅ ON |

---

## 🏷️ Las 12 Categorías Oficiales

| Tag | Emoji | Concepto |
|---|---|---|
| `plaza-campo` | 🐴 | Trueque y plaza de ganado |
| `garnachas-sabor` | 🌮 | Barbacoa, tacos, antojitos |
| `canasta-basica` | 🥬 | Verduras, frutas, carnes |
| `la-paca` | 👕 | Ropa americana de segunda mano |
| `chacharas-antiguedades` | 🔧 | Herramientas usadas, fierro viejo |
| `identidad-oficios` | 🏺 | Artesanías, barro, textiles |
| `muebles-artesanales` | 🪑 | Muebles de tule, equipal, madera |
| `animales-corral` | 🐑 | Ganado, aves, caballos |
| `cultura-tradicion` | 🎭 | Festivales, danzas, tradiciones |
| `pueblo-magico` | 🏆 | Pueblos Mágicos del Edomex |
| `hierbas-medicina` | 🌿 | Medicina tradicional, temazcal |
| `flores-plantas` | 🌸 | Viveros, plantas, jardinería |

---

## 🗺️ Los 12 Pueblos Mágicos del Edomex

Aculco · El Oro · Ixtapan de la Sal · Jilotepec · Malinalco · Metepec · Otumba · San Juan Teotihuacán · Tepotzotlán · Tonatico · Valle de Bravo · Villa del Carbón

---

## 📝 Cómo Agregar un Nuevo Tianguis

1. Crear `database/<region>/<nombre>.md`
2. Copiar la plantilla de `tianguistengo.md`
3. Llenar: id, name, region, days, coords, categories
4. Agregar bitácoras comunitarias (mínimo 5)
5. Agregar cómo llegar + POIs
6. Ejecutar: `python3 cli.py validate`
7. Ejecutar: `python3 cli.py build && cp dist/data.json public/`

---

## 📦 Peso y Rendimiento

| Recurso | Tamaño |
|---|---|
| `index.html` | ~33 KB |
| `data.json` (100 tianguis estimado) | ~500 KB |
| Leaflet CSS+JS | ~150 KB (cacheable) |
| **Primera carga** | ~700 KB |
| **Cargas siguientes** | **0 KB** (Service Worker cachea todo) |
| **Tiempo de carga 3G** | < 2 segundos |

---

## 🛠️ Comandos del CLI

```bash
python3 cli.py build       # Compilar .md → dist/data.json
python3 cli.py validate    # Validar integridad
python3 cli.py watch       # Recompilar automático
python3 cli.py serve       # Servidor :9500
python3 cli.py stats       # Estadísticas
```

---

## 📄 Licencia

Proyecto comunitario abierto. Hecho para la gente de a pie del Estado de México.

> *"Es tecnología nuestra para caminar, conocer, comer y defender las costumbres de nuestra tierra."*
