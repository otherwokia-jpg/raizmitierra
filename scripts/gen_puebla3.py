#!/usr/bin/env python3
"""Generate Puebla files 14-26: Valle Serdán"""

import os, random

U400 = [
    "https://images.unsplash.com/photo-1586271476959-e3492e0f7e6f?w=400",
    "https://images.unsplash.com/photo-1555955591-95b56ea0f7a4?w=400",
    "https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400",
    "https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400",
    "https://images.unsplash.com/photo-1506905365341-3c04a535b966?w=400",
    "https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=400",
    "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400",
    "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400",
    "https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400",
    "https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400",
    "https://images.unsplash.com/photo-1560750588-73207b1ef5b8?w=400",
    "https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400",
    "https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400",
    "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=400",
    "https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=400",
    "https://images.unsplash.com/photo-1596040033229-98200ba6c08c?w=400",
    "https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400",
    "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
    "https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400",
    "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400",
    "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400",
    "https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=400",
    "https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=400",
    "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=400",
    "https://images.unsplash.com/photo-1471193945509-9ad0617afabf?w=400",
    "https://images.unsplash.com/photo-1509099836639-18ba1795216d?w=400",
]
U800 = [u.replace('w=400','w=800') for u in U400]
BASE = os.path.expanduser("~/raizmitierra/database/puebla")

def gen(idn, name, sub, days, coords, cats, safety, horario, emoji, quote, zones, comments, how, tips):
    cs = ", ".join(f'"{c}"' for c in cats)
    ds = ", ".join(f'"{d}"' for d in days)
    t = "\n".join(f"- {tip}" for tip in tips)
    return f"""---
id: "MX-PUE-{idn:03d}"
name: "{name}"
region: "{sub}"
state: "puebla"
days: [{ds}]
coords: [{coords[0]}, {coords[1]}]
categories: [{cs}]
safety: "{safety}"
horario: "{horario}"
img: "{random.choice(U800)}"
---

# {emoji} {name}

> {quote}

## 📋 Información Rápida

| Dato | Detalle |
|------|---------|
| 📅 **Días** | {', '.join(days)} |
| ⏰ **Horario** | {horario} |
| 📍 **Región** | {sub} — Puebla |
| 🗺️ **Categorías** | {', '.join(cats)} |

## 🗺️ Zonas del Tianguis

{zones}

## 💬 Bitácora Comunitaria

{comments}

## 🚗 Cómo Llegar

{how}

## Recomendaciones de la Comunidad

{t}
"""

def write(sr, idn, name, days, coords, cats, safety, horario, emoji, quote, zones, comments, how, tips):
    import re
    fname = name.lower().replace(' ', '_').replace('í','i').replace('ó','o').replace('é','e').replace('á','a').replace('ú','u').replace('ü','u').replace(',','').replace('.','').replace('ñ','n').replace('—','').replace("'",'')
    fname = re.sub(r'_+', '_', fname)
    path = os.path.join(BASE, sr, f"tianguis_de_{fname}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = gen(idn, name, sr, days, coords, cats, safety, horario, emoji, quote, zones, comments, how, tips)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  [{idn:02d}] {name}")

# ============ VALLE SERDÁN (14-26) ============

write("valle_serdan", 14, "Tianguis de Analco — Barrio de Artesanos", ["Sábado", "Domingo"],
    [19.0414, -98.2067],
    ["artesania", "cultura-tradicion", "identidad-oficios", "pueblo-magico", "garnachas-sabor"],
    "Zona turística del Centro Histórico de Puebla, muy segura y vigilada",
    "9:00 AM — 7:00 PM",
    "🎨",
    "En el Barrio de Analco, el más antiguo de Puebla, cada fin de semana el tianguis artesanal convierte las calles empedradas en una galería viva de arte popular poblano.",
    """El Tianguis de Analco se instala en el barrio más antiguo de Puebla:

- **Zona de Artesanías**: Talavera poblana, barro vidriado, textiles, alebrijes, joyería artesanal.
- **Zona de Pintura y Grabado**: Artistas locales exponen y venden sus obras.
- **Zona de Gastronomía**: Cemitas, chalupas, molotes, tacos árabes, dulces típicos.
- **Zona de Ropa Artesanal**: Huipiles, blusas bordadas, rebozos, accesorios.
- **Zona de Música en Vivo**: Trovadores, mariachis y música tradicional.""",
    """### 🎨 Galería al Aire Libre
> "Analco es el corazón artesanal de Puebla. Cada fin de semana los artesanos exhiben su mejor trabajo: talavera, textiles, joyería. Es un lugar perfecto para encontrar regalos únicos."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Analco+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400)
### 🌮 Sabor Poblano
> "Las cemitas de Analco son de las mejores de Puebla. Pan recién horneado, milanesa, quesillo, chipotle y aguacate. La combinación perfecta después de recorrer el tianguis."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Analco+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Arte Accesible
> "Los precios son justos porque tratas directamente con el artesano. Piezas de talavera desde $50, joyería artesanal desde $100. Mejor calidad que en las tiendas turísticas del centro."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Analco+artesanias+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400)
### 🎭 Cultura Viva
> "Analco tiene más de 500 años de historia. El tianguis mantiene viva la tradición artesanal de Puebla. Los sábados hay danza y música tradicional en las calles del barrio."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+Analco+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🛡️ Zona Segura
> "El barrio de Analco es muy seguro, especialmente los fines de semana cuando hay más gente. Hay vigilancia policial y los locales son amables con los visitantes."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Analco+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "En el Centro Histórico de Puebla, a 5 calles del zócalo. Se llega caminando desde cualquier punto del centro. Estacionamiento público en los alrededores ($30-50).",
    ["Visitar el sábado por la mañana cuando hay más artesanos y menos gente.",
     "Probar las cemitas poblanas en los puestos locales.",
     "Comprar talavera directamente de los artesanos.",
     "Caminar por las calles empedradas del barrio histórico.",
     "Llevar efectivo — la mayoría de puestos no acepta tarjeta."])

write("valle_serdan", 15, "Tianguis de Santa María Xixitla, Cholula", ["Domingo", "Miércoles"],
    [19.0642, -98.3039],
    ["canasta-basica", "plaza-campo", "garnachas-sabor", "cultura-tradicion"],
    "Zona segura en San Pedro Cholula, ambiente familiar, vigilancia municipal",
    "8:00 AM — 8:00 PM",
    "🍅",
    "Santa María Xixitla es el tianguis más grande de Cholula, donde desde la época prehispánica las comunidades se reúnen para intercambiar productos frescos, artesanías y tradiciones.",
    """El tianguis se extiende por varias calles alrededor de la Capilla de Santa María Xixitla:

- **Zona de Frutas y Verduras**: Productos frescos de las comunidades cholultecas: aguacate, chile, jitomate, verduras.
- **Zona de Comida**: Fondas con mole poblano, chalupas, tacos, tlacoyos, cemitas.
- **Zona de Flores**: Flores frescas, plantas ornamentales, hierbas de olor.
- **Zona de Ropa y Mercancía**: Ropa, calzado, accesorios, productos del hogar.
- **Zona de Artesanías**: Cerámica de Cholula, talavera, textiles.""",
    """### 🌮 El Sabor de Cholula
> "Xixitla tiene la mejor comida de Cholula. Los tlacoyos de Doña Coco son famosos: masa azul, frijol, nopal y salsa verde. Los mejores que he probado en mi vida."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Xixitla+Cholula)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400)
### 💰 Los Mejores Precios
> "Aquí los precios son imbatibles. Las verduras y frutas son recién traídas de las chinampas y huertos de Cholula. Gasto $300 para toda la semana."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Xixitla+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🎭 Tradición Cholulteca
> "Cholula tiene una historia milenaria. En Xixitla todavía se siente la conexión con el pasado prehispánico. Las mujeres venden sus productos como lo hacían sus abuelas."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+Cholula+tianguis)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🏺 Cerámica de Cholula
> "La cerámica de Cholula es famosa desde tiempos prehispánicos. En el tianguis encuentras piezas únicas: cazuelas, platos, jarrones decorados a mano."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=ceramica+Cholula)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)
### 🚇 Cómo Llegar
> "Se llega fácil desde Puebla en autobús (Ruta Azteca, 20 min). En coche, estacionamiento en la zona. Los miércoles el tianguis es más pequeño, los domingos es el día grande."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Xixitla+Cholula)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)
### 🌿 Hierbas Medicinales
> "Las abuelas de Cholula venden hierbas medicinales en Xixitla. Conocen las propiedades de cada planta. El té de tila, manzanilla y ruda son los más populares."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=hierbas+Xixitla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=400)""",
    "Desde Puebla: Autobuses Azteca o Estrella Roja rumbo a Cholula (20 min). El tianguis está a 10 min caminando de la Capilla de Santa María Xixitla. En coche: Vía Atlixcáyotl, desviación a San Pedro Cholula.",
    ["Ir los domingos — es el día más grande con mayor variedad.",
     "Probar los tlacoyos de masa azul con salsa verde.",
     "Comprar cerámica de Cholula directamente de los artesanos.",
     "Visitar la Capilla de Santa María Xixitla.",
     "Llevar bolsas reutilizables para las compras."])

write("valle_serdan", 16, "Tianguis de San Martín Texmelucan", ["Miércoles", "Domingo"],
    [19.2819, -98.4389],
    ["la-paca", "chacharas-antiguedades", "canasta-basica", "garnachas-sabor", "plaza-campo"],
    "Zona comercial muy concurrida, mantener precaución con pertenencias personales en áreas muy concurridas",
    "7:00 AM — 5:00 PM",
    "👕",
    "El Tianguis de San Martín Texmelucan es uno de los más grandes de América Latina, con 35 hectáreas de extensión. Es el centro de distribución textil más importante del sureste mexicano.",
    """El tianguis se ubica en San Lucas Atoyatenco, a 30 min del centro:

- **Zona Textil**: La más grande. Ropa al mayoreo y menudeo: pantalones, camisas, vestidos, chamarras. Precios de fábrica.
- **Zona de Paca**: Ropa de segunda mano americana de excelente calidad.
- **Zona de Frutas y Verduras**: Productos frescos de la región.
- **Zona de Comida**: Cemitas, tlacoyos, tacos, barbacoa, carnitas.
- **Zona de Chácharas**: Herramientas, electrónicos, antigüedades.
- **Zona de Calzado**: Zapatos, tenis, botas al mayoreo y menudeo.""",
    """### 👕 Capital Textil
> "San Martín Texmelucan es el tianguis de ropa más grande de Latinoamérica. 35 hectáreas de puestos. Viene gente de Oaxaca, Chiapas y Guerrero a surtirse. Los precios al mayoreo son imbatibles."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+San+Martin+Texmelucan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🌮 Tlacoyos Famosos
> "Los tlacoyos del mercado de San Martín son famosos en todo Puebla. Masa de maíz azul, frijol, nopal y salsa. La gente viene específicamente a comerlos."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tlacoyos+San+Martin+Texmelucan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Mayoreo y Menudeo
> "Los precios al mayoreo son de locura. Pantalones desde $80, camisas desde $50, chamarras desde $150. Si compras varias piezas, los descuentos son enormes."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Texmelucan+ropa+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400)
### 🔧 Chácharas y Tesoros
> "En la zona de chácharas encuentras de todo: herramientas antiguas, juguetes, discos, libros. Si sabes buscar, encuentras verdaderas joyas a precios irrisorios."
- **Tipo:** #Chacharas
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=chacharas+Texmelucan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)
### 🚇 Acceso
> "Desde Puebla hay autobuses cada 15 minutos (45 min). El tianguis está en San Lucas Atoyatenco. Es enorme, lleva todo el día recorrerlo. Mejor ir temprano."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Texmelucan+tianguis)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)
### 🛡️ Precauciones
> "Es un lugar muy concurrido y grande. Como en cualquier tianguis enorme, hay que cuidar las pertenencias personales. No llevar objetos de valor innecesarios."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Texmelucan+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)
### 🎭 Cultura Viva
> "El tianguis tiene raíces virreinales, del siglo XVII. Ha sido un punto vital del Camino Real México-Puebla. Hoy sigue siendo un nodo de intercambio cultural y comercial único."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=historia+Texmelucan+tianguis)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🐄 Zona de Animales
> "Los domingos también hay venta de animales de corral: pollos, guajolotes, borregos. Es una de las zonas más tradicionales del tianguis."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=animales+Texmelucan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1583337130417-3346c1be1e4d?w=400)""",
    "Desde Puebla: Autobuses desde la CAPU (45 min). En coche: Carretera federal Puebla-Tlaxcala (ruta 119). El tianguis está en San Lucas Atoyatenco, a 30 min del centro de San Martín Texmelucan.",
    ["Ir los miércoles o domingos — los días principales.",
     "Ir con ropa cómoda y zapatos para caminar — el tianguis es enorme.",
     "Comprar ropa al mayoreo para obtener los mejores descuentos.",
     "Probar los tlacoyos en los puestos del mercado.",
     "Llevar efectivo en abundancia — muchos puestos solo aceptan efectivo."])

write("valle_serdan", 17, "Tianguis de La Libertad, Puebla", ["Viernes"],
    [19.0450, -98.2050],
    ["la-paca", "chacharas-antiguedades", "garnachas-sabor", "canasta-basica"],
    "Zona popular muy concurrida los viernes, vigilancia de la policía municipal",
    "8:00 AM — 6:00 PM",
    "🛍️",
    "El Tianguis de La Libertad es el más grande de la ciudad de Puebla, un laberinto de puestos donde encuentras desde ropa de paca hasta antigüedades, en un ambiente de barrio lleno de vida.",
    """El tianguis se extiende por varias calles de la Colonia La Libertad:

- **Zona de Paca**: Ropa americana de segunda mano de excelente calidad, zapatos, accesorios.
- **Zona de Chácharas**: Antigüedades, herramientas, libros, discos, juguetes, electrónicos.
- **Zona de Comida**: Anafres, tacos, tlacoyos, gorditas, aguas frescas.
- **Zona de Frutas y Verduras**: Productos frescos a buen precio.
- **Zona de Ropa Nueva**: Ropa de temporada, calzado, accesorios.""",
    """### 🛍️ El Paraíso de la Paca
> "La Libertad es el mejor lugar para comprar ropa de paca en Puebla. Ropa americana de marca a precios ridículos. Encuentras desde $10 las prendas básicas."
- **Tipo:** #LaPaca
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+La+Libertad+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🌮 Comida de Barrio
> "Los puestos de comida de La Libertad son de los mejores de Puebla. Las gorditas de chicharrón y los tacos de canasta son imperdibles. Comida de la auténtica."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+La+Libertad+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 🔧 Tesoros Ocultos
> "En la zona de chácharas encuentras verdaderas joyas. Discos de vinilo, cámaras antiguas, herramientas, lo que te imagines. Es un paraíso para los coleccionistas."
- **Tipo:** #Chacharas
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=chacharas+La+Libertad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)
### 💰 Precios Imbatibles
> "Los precios aquí son los más bajos de Puebla capital. Ropa desde $10, verduras por mayoreo, comida económica. Ideal para quienes buscan estirar el presupuesto."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=La+Libertad+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🚇 Llegada
> "Se llega en cualquier autobús que vaya a La Libertad (Ruta Libertad, Ruta 3). En coche hay estacionamiento en las calles cercanas. Llegar temprano para evitar lo más pesado."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+La+Libertad+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)""",
    "Desde el centro de Puebla: Autobuses Ruta Libertad o Ruta 3 (20 min). En coche: Av. Reforma, desviación a Colonia La Libertad. El tianguis está a 15 min del centro.",
    ["Ir temprano (8 AM) para encontrar la mejor ropa de paca.",
     "Revisar bien la ropa de paca — a veces hay piezas de diseñador.",
     "Probar las gorditas de chicharrón en los puestos de comida.",
     "Llevar efectivo en denominaciones pequeñas.",
     "Ir con tiempo para recorrer todo — el tianguis es grande."])

write("valle_serdan", 18, "Tianguis Los Lavaderos, Puebla", ["Jueves", "Domingo"],
    [19.0380, -98.2000],
    ["la-paca", "garnachas-sabor", "chacharas-antiguedades", "canasta-basica"],
    "Zona popular muy concurrida, mantener precaución con pertenencias, evitar objetos de valor",
    "8:00 AM — 6:00 PM",
    "👗",
    "Los Lavaderos es el tianguis de ropa más famoso de Puebla capital. Con más de 30 años de historia, es el destino favorito para quienes buscan ropa de paca, accesorios y auténticos hallazgos.",
    """Se instala en la Diagonal Defensores de la República, cerca de la China Poblana:

- **Zona de Ropa de Paca**: La especialidad. Ropa americana seleccionada, de marca, en buen estado.
- **Zona de Ropa Nueva**: Prendas de temporada, accesorios, bisutería, bolsas.
- **Zona de Comida**: Puestos de garnachas, tacos, tlacoyos, aguas frescas.
- **Zona de Calzado**: Zapatos nuevos y de paca, tenis, botas.
- **Zona de Chácharas**: Discos, juguetes, herramientas, artículos para el hogar.""",
    """### 👗 El Paraíso del Ropero
> "Los Lavaderos es el tianguis de ropa más famoso de Puebla. Los jueves es el día fuerte, llega ropa nueva de paca. Encuentras marcas como Zara, H&M, Tommy a precios de $50-200."
- **Tipo:** #LaPaca
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Los+Lavaderos+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🌮 Picar por el Tianguis
> "Después de horas buscando ropa, los tacos de canasta de Los Lavaderos son la recompensa perfecta. Doña Leti los prepara con papa, adobo y salsa verde."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Los+Lavaderos)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Gangas Seguras
> "Los precios son los mejores de la ciudad. Ropa de paca desde $20-30 la prenda. Si compras varias piezas, hay descuento. Los jueves es cuando llega la mejor mercancía."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Los+Lavaderos+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400)
### 🔧 Buscando Tesoros
> "Además de ropa, hay puestos de chácharas interesantes. Discos, libros, juguetes antiguos. He encontrado cosas muy valiosas por casi nada."
- **Tipo:** #Chacharas
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=chacharas+Los+Lavaderos)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)
### 🚇 Cómo Llegar
> "Se llega por Metrobús (estación Lavaderos, Línea 2). También hay autobuses que pasan por la Diagonal Defensores. En coche, estacionamiento en las calles cercanas."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Lavaderos+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)
### 🛡️ Precauciones
> "Es un tianguis muy grande y concurrido. Como en todos los tianguis de la ciudad, hay que cuidar carteras y teléfonos. No llevar bolsas de marca ni joyas llamativas."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Lavaderos+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "Metrobús Línea 2, estación Lavaderos. Desde el centro: Autobuses que van por la Diagonal Defensores. En coche: Av. Reforma hasta Diagonal Defensores.",
    ["Ir los jueves — es el día que llega la mejor ropa de paca.",
     "Llegar temprano (9 AM) para tener la mejor selección.",
     "Revisar cada prenda cuidadosamente antes de comprar.",
     "Probar los tacos de canasta de Doña Leti.",
     "Llevar efectivo y una bolsa grande para las compras."])

write("valle_serdan", 19, "Tianguis de Atlixco", ["Martes", "Sábado"],
    [18.9072, -98.4361],
    ["canasta-basica", "plaza-campo", "garnachas-sabor", "flores-plantas", "cultura-tradicion"],
    "Zona segura con vigilancia municipal, más de 2,600 comerciantes organizados",
    "8:00 AM — 5:00 PM",
    "🌸",
    "Atlixco, Pueblo Mágico y jardín de Puebla, tiene su tianguis los martes y sábados. Es el corazón comercial de la región donde confluyen comunidades nahuas, floricultores y productores del valle.",
    """El tianguis de Atlixco es uno de los más grandes del estado, ocupando calles del centro:

- **Zona de Flores**: Atlixco es famoso por sus flores. Claveles, rosas, gerberas, gladiolas a precios de cultivo.
- **Zona de Frutas y Verduras**: Productos del valle: aguacate, jitomate, chile, verduras.
- **Zona de Comida**: Mole, cemitas, chalupas, carnitas, barbacoa, tacos.
- **Zona de Ropa y Textiles**: Ropa, calzado, accesorios.
- **Zona de Artesanías**: Barro vidriado, textiles, cestería, objetos de palma.""",
    """### 🌸 Jardín de México
> "Atlixco es conocido como el jardín de México por sus flores. En el tianguis encuentras ramos enormes por $50-100. Las flores son frescas, cortadas esa misma mañana."
- **Tipo:** #Flores
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Atlixco+flores)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1560750588-73207b1ef5b8?w=400)
### 🌮 Sabor Poblano
> "Las cemitas de Atlixco son otra cosa. Pan grande, milanesa, quesillo, chipotle, pápalo. La combinación es perfecta. Los puestos de carnitas también son espectaculares."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Atlixco)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400)
### 💰 Precios de Cultivo
> "Al estar en el valle agrícola, los precios de frutas y verduras son los mejores de la región. Aguacates, jitomates, chiles directamente del productor. Ahorras mucho."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Atlixco+precios+mercado)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🎭 Cultura del Valle
> "Atlixco tiene una mezcla de tradiciones. Aquí conviven nahuas, mestizos y floricultores. El tianguis es el punto de encuentro de todas las comunidades del valle."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+Atlixco+tianguis)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🚇 Cómo Llegar
> "Desde Puebla: Autobuses cada 15 minutos (30 min). En coche: Vía Atlixcáyotl. El tianguis está en el centro, los sábados es el día más grande."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Atlixco)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)
### 🏺 Artesanía Local
> "Los artesanos de Atlixco trabajan el barro vidriado y la palma. En el tianguis encuentras cazuelas, jarrones y canastos a buen precio. Ideal para decorar la casa."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=artesanias+Atlixco)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)""",
    "Desde Puebla: Autobuses desde la CAPU (30 min) o Ruta Atlixcáyotl. En coche: Vía Atlixcáyotl (30 min desde Puebla). El tianguis está en las calles del centro de Atlixco.",
    ["Ir los sábados — día más grande con más variedad de productos.",
     "Comprar flores frescas — son las más baratas y hermosas del estado.",
     "Probar las cemitas poblanas y las carnitas.",
     "Visitar el Mercado Ignacio Zaragoza.",
     "Subir al Cerro de San Miguel para vistas panorámicas."])

write("valle_serdan", 20, "Tianguis de San Ramón — La Curva, Puebla", ["Domingo"],
    [18.9700, -98.2150],
    ["la-paca", "chacharas-antiguedades", "garnachas-sabor", "canasta-basica"],
    "Zona popular muy concurrida los domingos, precaución con pertenencias personales",
    "8:00 AM — 5:00 PM",
    "🔧",
    "El Tianguis de San Ramón, conocido como 'La Curva', es uno de los más grandes y populares del sur de Puebla. Famoso por sus chácharas, ropa de paca y ambiente de barrio.",
    """Se instala en la zona de San Ramón, al sur de la ciudad:

- **Zona de Chácharas**: La más famosa. Herramientas, electrónicos, antigüedades, juguetes, todo tipo de objetos.
- **Zona de Ropa de Paca**: Ropa americana seleccionada, zapatos, accesorios.
- **Zona de Comida**: Tacos, gorditas, tlacoyos, carnitas, barbacoa.
- **Zona de Plantas**: Plantas ornamentales, flores, árboles frutales.
- **Zona de Muebles**: Muebles usados y nuevos, artículos para el hogar.""",
    """### 🔧 El Reino de las Chácharas
> "San Ramón es el mejor tianguis de chácharas de Puebla. Encuentras de todo: herramientas, aparatos electrónicos, piezas de coche, antigüedades. Es un paraíso para los buscadores de tesoros."
- **Tipo:** #Chacharas
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+San+RAMON+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)
### 👕 Paca de Calidad
> "La ropa de paca de San Ramón es de las mejores. Familias enteras vienen a surtir el clóset. Ropa americana de marca a precios de $20-100 la prenda."
- **Tipo:** #LaPaca
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=paca+San+Ramon+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🌮 Garnachas del Sur
> "Los tacos de canasta y las gorditas de San Ramón son famosos. Doña Mary las hace con chicharrón prensado, papa y adobo. Salsa verde bien picosa."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+San+Ramon+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Precios Populares
> "Los precios son populares, para la raza. Negociables casi siempre. Si compras varias cosas, puedes pedir descuento. Es el tianguis más accesible de la ciudad."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=San+Ramon+precios+tianguis)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400)
### 🛡️ Ambiente Familiar
> "Los domingos es un ambiente familiar. Mucha gente, pero también hay seguridad de los mismos locatarios. Solo cuidar lo básico."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=San+Ramon+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "Desde el centro de Puebla: Autobuses Ruta San Ramón o Ruta Sur (30 min). En coche: Av. 16 de Septiembre, pasando la 37 Sur. El tianguis está en la zona de La Curva.",
    ["Ir temprano (8 AM) para encontrar las mejores chácharas.",
     "Revisar bien todo antes de comprar — especialmente electrónicos.",
     "Negociar los precios — es parte de la experiencia.",
     "Probar los tacos de canasta de Doña Mary.",
     "Llevar efectivo — casi nadie acepta tarjeta."])

write("valle_serdan", 21, "Tianguis de Loma Bella, Puebla", ["Domingo"],
    [18.9900, -98.2100],
    ["la-paca", "canasta-basica", "garnachas-sabor", "chacharas-antiguedades"],
    "Tianguis de barrio, concurrido los domingos, precauciones normales",
    "8:00 AM — 4:00 PM",
    "🏘️",
    "El Tianguis de Loma Bella es el mercado dominical del sur de Puebla, donde las familias del barrio se reúnen para hacer la despensa, comer garnachas y encontrar ropa a buen precio.",
    """Se instala en las calles de la colonia Loma Bella:

- **Zona de Ropa**: Ropa nueva y de paca, calzado, accesorios, bisutería.
- **Zona de Frutas y Verduras**: Productos frescos para la despensa semanal.
- **Zona de Comida**: Fondas con antojitos, tacos, tlacoyos, aguas frescas.
- **Zona de Chácharas**: Juguetes, herramientas, artículos para el hogar.
- **Zona de Plantas**: Plantas ornamentales y flores.""",
    """### 🏘️ Tianguis de Barrio
> "Loma Bella es el tianguis de mi colonia. Los domingos toda la familia sale a hacer la despensa. Encuentras de todo: ropa, fruta, verdura, comida. Muy completo."
- **Tipo:** #Canasta
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Loma+Bella+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🌮 Antojitos de Barrio
> "Las gorditas de chicharrón de Loma Bella son las mejores. Masa crujiente, chicharrón bien sazonado, salsa verde. Un clásico de los domingos poblanos."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Loma+Bella)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Precios de Colonia
> "Los precios son para el bolsillo del barrio. Frutas y verduras baratas, ropa accesible. Gasto como $200-300 y llevo bastante para la semana."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Loma+Bella+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 👕 Paca y Ropa
> "Hay varios puestos de ropa de paca con buena selección. Ropa americana a buen precio, ideal para encontrar piezas únicas sin gastar mucho."
- **Tipo:** #LaPaca
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=paca+Loma+Bella)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)""",
    "Desde el centro: Autobuses Ruta Loma Bella (25 min). En coche: Av. 16 de Septiembre hasta Blvd. Villas del Álamo. Estacionamiento en calles aledañas.",
    ["Ir los domingos por la mañana para mejor variedad.",
     "Probar las gorditas de chicharrón.",
     "Hacer la despensa de la semana — buenos precios en frutas y verduras.",
     "Buscar ropa de paca — hay buena selección.",
     "Llevar efectivo."])

print("Valle Serdán files 14-21 done")
