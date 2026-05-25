# 🌎 RaízMiTierra

> *Caminar, conocer, comer y defender las costumbres de nuestra tierra.*

**RaízMiTierra** es una plataforma comunitaria, anónima y **antigentrificación** para descubrir tianguis, trueque, barbacoa de hoyo, balnearios populares, artesanías y Pueblos Mágicos del Estado de México.

**100% privada.** Tu ubicación nunca sale de tu teléfono.

---

## 📋 Estado del Proyecto

| Componente | Estado |
|---|---|
| `index.html` — App PWA completa | ✅ Funcionando |
| `raizmitierra_server.py` — Backend Flask | ✅ Funcionando |
| `data.json` — 259 lugares (202 tianguis + 57 lugares) | ✅ 1.1 MB |
| **🎉 Festivales y Eventos** — 212 lugares con eventos | ✅ **¡Nuevo!** |
| **🗣️ Reseñas Comunitarias** — Sistema de reseñas + admin | ✅ **¡Nuevo!** |
| 🔐 SSO Integrado (Landing Portal) | ✅ Funcionando |
| 🐳 Docker + Cloudflare Tunnel | ✅ En producción |
| ☁️ Cloudflare Pages (`raizmitierra.pages.dev`) | ✅ En producción |

## 🎉 Festivales y Eventos

Cada lugar puede tener festividades asociadas. Al seleccionar **🎉 Eventos**:

- **Selector de fecha** 📅 — elige cualquier día para ver qué festividades hay
- **Chips rápidos**: Hoy · Este finde · Próx. 7d · Próx. 30d
- **Filtros por tipo**: 🎭 Patronal · 🏆 Feria Pueblo · 🌮 Gastronómica · 🎶 Cultural · 🎄 Tradición
- **445 festividades** para **212 lugares** en CDMX, Puebla, Michoacán, Morelos, Hidalgo, Tlaxcala y Edomex
- **Default**: Próximos 30 días (no interfiere con filtro "Hoy")

## 🗣️ Reseñas Comunitarias

Los usuarios pueden dejar reseñas en cada lugar:
- Nombre del reseñista obligatorio
- Aprobación por admin antes de publicar
- Admin panel en `/admin/reviews`
- Enlace directo al lugar desde cada reseña pendiente

## 🔐 SSO Integrado

RaízMiTierra se integra al ecosistema SSO del Landing Portal (puerto 8888):
- Usuarios autenticados via SSO pueden acceder al admin
- Proxy mode para debugging
- Portal key: `raizmitierra`

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

## ☁️ Despliegue

### Producción Actual (Docker + Cloudflare Tunnel)

```bash
# Backend/admin en servidor propio
cd ~/raizmitierra
docker-compose up -d --build
# Sirve en http://localhost:9500
# Cloudflare Tunnel → https://datacenter.hubmultiteck.io/raiz/
```

### Frontend Estático (Cloudflare Pages)

```bash
cd ~/raizmitierra
npx wrangler pages deploy --project-name raizmitierra --branch main ./dist/
# → https://raizmitierra.pages.dev
```

### Variables de Entorno (.env)

| Variable | Descripción |
|---|---|
| `RAIZ_SECRET` | Clave secreta para sesiones Flask |
| `SSO_SECRET_FILE` | Ruta al archivo de clave SSO |
| `USERS_FILE` | Ruta al archivo users.json del Landing |
| `PORT` | Puerto (9500) |

---

## 🏷️ Las 17 Categorías Oficiales

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
| `zona-arqueologica` | 🏛️ | Pirámides, zonas arqueológicas |
| `pueblo-tradicional` | 🏘️ | Pueblos con encanto |
| `centro-otomi` | 🏮 | Centros ceremoniales otomíes |
| `balneario-cascada` | 🏊 | Balnearios, aguas termales, cascadas |
| `mirador-naturaleza` | ⛰️ | Miradores, cerros, bosques |

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
| `index.html` (con datos inline) | ~930 KB |
| `data.json` (259 lugares, 445 festivales) | ~1.1 MB |
| Leaflet CSS+JS | ~150 KB (cacheable) |
| **Primera carga** | ~1 MB |
| **Cargas siguientes** | 0 KB (Service Worker cachea)

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
