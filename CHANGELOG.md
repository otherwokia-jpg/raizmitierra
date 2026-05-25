# Changelog — RaízMiTierra

## v2.2.0 — 2026-05-24

### 🎉 Festivales y Eventos
- Nuevo filtro "🎉 Eventos" junto a "🌎 Todos", "🌮 Tianguis", "📍 Lugares"
- **445 festividades** para **212 lugares** en 7 estados
- Selector de fecha 📅 con chips rápidos: Hoy · Este finde · Próx. 7d · Próx. 30d
- Filtros por tipo: 🎭 Patronal · 🏆 Feria Pueblo · 🌮 Gastronómica · 🎶 Cultural · 🎄 Tradición
- Default a "Próx. 30d" al seleccionar Eventos (más útil que Hoy)
- "Hoy" no interfiere con Eventos (se desactiva automáticamente)
- Sección de festividades en modal de detalle de cada lugar

### 🗣️ Reseñas Comunitarias
- Sistema completo de reseñas por lugar
- Nombre del reseñista obligatorio
- Aprobación por admin (pendiente → aprobada/rechazada)
- Admin panel en `/admin/reviews`
- Enlace "🌐 Ver lugar" desde admin
- Botón "✍️ Dejar reseña" con formulario toggle

### 🐳 Infraestructura
- Dockerizado con healthchecks y Gunicorn
- Cloudflare Tunnel → `datacenter.hubmultiteck.io/raiz/`
- Cloudflare Pages → `raizmitierra.pages.dev`
- SSO integrado con Landing Portal (puerto 8888)
- Proxy mode para debugging

### 🐛 Fixes
- CORS habilitado para pages.dev
- Photos: prioriza foto admin, fallback a categoría
- 85 URLs rotas de Unsplash eliminadas
- Rutas absolutas de assets para pages.dev + Docker
- RAIZ_DATA inline regenerado con festivales incluidos
- Redirección SSO en proxy mode corregida
