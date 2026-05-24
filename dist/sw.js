/* RaízMiTierra — Service Worker v3.0-FRESH */
const CACHE = 'raizmitierra-v3';
const ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/assets/mercado.jpg',
  '/assets/tianguis.jpg',
  '/assets/piramide.jpg',
  '/assets/malinalco.jpg',
  '/assets/malinalco-pueblo.jpg',
  '/assets/pueblo.jpg',
  '/assets/cascada.jpg',
  '/assets/cacahuamilpa.jpg',
  '/assets/vallebravo.jpg',
  '/assets/otomi.jpg',
  '/assets/montana.jpg',
  '/assets/santuario.jpg',
  '/assets/chalma.jpg'
];

self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(ASSETS)).catch(() => {})
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
});

self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  // data.json = siempre fresco (network first)
  if (url.pathname.endsWith('data.json')) {
    e.respondWith(
      fetch(e.request).catch(() => caches.match(e.request))
    );
    return;
  }
  // assets estáticos = cache first
  if (url.pathname.startsWith('/assets/')) {
    e.respondWith(
      caches.match(e.request).then(cached => cached || fetch(e.request))
    );
    return;
  }
  // lo demás = network first (para HTML, CDN leaflet, etc.)
  e.respondWith(
    fetch(e.request).catch(() => caches.match(e.request))
  );
});
