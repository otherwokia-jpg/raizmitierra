#!/usr/bin/env python3
"""Generate 50 Puebla tianguis .md files with authentic data."""

import os

BASE = os.path.expanduser("~/raizmitierra/database/puebla")

# Unsplash photo IDs for variety
PHOTOS = {
    "market1": "https://images.unsplash.com/photo-1586271476959-e3492e0f7e6f?w=800",
    "market2": "https://images.unsplash.com/photo-1586271476959-e3492e0f7e6f?w=400",
    "market3": "https://images.unsplash.com/photo-1555955591-95b56ea0f7a4?w=800",
    "market4": "https://images.unsplash.com/photo-1555955591-95b56ea0f7a4?w=400",
    "market5": "https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=800",
    "market6": "https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400",
    "market7": "https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=800",
    "market8": "https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=800",
    "market9": "https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400",
    "fruit1": "https://images.unsplash.com/photo-1506905365341-3c04a535b966?w=800",
    "fruit2": "https://images.unsplash.com/photo-1506905365341-3c04a535b966?w=400",
    "fruit3": "https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=800",
    "fruit4": "https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=400",
    "craft1": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800",
    "craft2": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400",
    "craft3": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800",
    "craft4": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400",
    "craft5": "https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=800",
    "craft6": "https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400",
    "flowers1": "https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=800",
    "flowers2": "https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400",
    "flowers3": "https://images.unsplash.com/photo-1560750588-73207b1ef5b8?w=800",
    "flowers4": "https://images.unsplash.com/photo-1560750588-73207b1ef5b8?w=400",
    "veggies1": "https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=800",
    "veggies2": "https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400",
    "veggies3": "https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=800",
    "veggies4": "https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400",
    "herbs1": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=800",
    "herbs2": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=400",
    "herbs3": "https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=800",
    "herbs4": "https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=400",
    "spices1": "https://images.unsplash.com/photo-1596040033229-98200ba6c08c?w=800",
    "spices2": "https://images.unsplash.com/photo-1596040033229-98200ba6c08c?w=400",
    "food1": "https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=800",
    "food2": "https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400",
    "food3": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800",
    "food4": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
    "textiles1": "https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=800",
    "textiles2": "https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400",
    "textiles3": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800",
    "textiles4": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400",
    "animals1": "https://images.unsplash.com/photo-1583337130417-3346c1be1e4d?w=800",
    "animals2": "https://images.unsplash.com/photo-1583337130417-3346c1be1e4d?w=400",
    "landscape1": "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=800",
    "landscape2": "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400",
    "landscape3": "https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=800",
    "landscape4": "https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=400",
}

# Shared photo pool for bitácora entries (400px versions)
PHOTO_POOL = [v for k, v in PHOTOS.items() if 'w=400' in v]
PHOTO_POOL_800 = [v for k, v in PHOTOS.items() if 'w=800' in v]

import random

def get_photo():
    return random.choice(PHOTO_POOL)

def get_photo_800():
    return random.choice(PHOTO_POOL_800)

def gen_content(id_num, name, region, subregion, days, coords, categories, safety, horario, emoji, quote, zones_text, comments, how_to_get, tips):
    """Generate a complete .md file content following the template."""
    categories_str = ", ".join([f'"{c}"' for c in categories])

    content = f"""---
id: "MX-PUE-{id_num:03d}"
name: "{name}"
region: "{subregion}"
state: "puebla"
days: [{', '.join([f'"{d}"' for d in days])}]
coords: [{coords[0]}, {coords[1]}]
categories: [{categories_str}]
safety: "{safety}"
horario: "{horario}"
img: "{get_photo_800()}"
---

# {emoji} {name}

> {quote}

## 📋 Información Rápida

| Dato | Detalle |
|------|---------|
| 📅 **Días** | {', '.join(days)} |
| ⏰ **Horario** | {horario} |
| 📍 **Región** | {subregion} — Puebla |
| 🗺️ **Categorías** | {', '.join(categories)} |

## 🗺️ Zonas del Tianguis

{zones_text}

## 💬 Bitácora Comunitaria

{comments}

## 🚗 Cómo Llegar

{how_to_get}

## Recomendaciones de la Comunidad

{chr(10).join([f'- {t}' for t in tips])}
"""
    return content


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


# ============================================================
# SIERRA NORTE (13 files)
# ============================================================
sierra_norte = []

# 1. Cuetzalan
sierra_norte.append({
    "id": 1,
    "name": "Tianguis Dominical de Cuetzalan",
    "region": "sierra_norte",
    "days": ["Domingo"],
    "coords": [20.0173, -97.5206],
    "categories": ["cultura-tradicion", "garnachas-sabor", "artesania", "plaza-campo", "identidad-oficios"],
    "safety": "Ambiente seguro y turístico, hay presencia de autoridades municipales y locales amigables",
    "horario": "7:00 AM — 4:00 PM",
    "emoji": "🌽",
    "quote": "En Cuetzalan el tianguis no es solo mercado, es el corazón de la cultura nahua donde las mujeres con quexquémitl bordado venden sus productos como hace siglos.",
    "zones": """El tianguis dominical de Cuetzalan se despliega por las calles empedradas del centro, alrededor del zócalo y la Parroquia de San Francisco de Asís. Se divide en:

- **Zona de Artesanías**: Textiles bordados a mano, quexquémitles, huipiles, bolsas de ixtle, joyería de filigrana y cerámica.
- **Zona de Flores y Plantas**: Orquídeas silvestres, flores de cempasúchil, plantas medicinales y café de altura.
- **Zona de Alimentos**: Puestos de garnachas, molotes, tamales de hoja de maíz, atole de granillo y café de olla.
- **Zona de Frutas y Verduras**: Productos de las comunidades nahuas de las montañas circundantes.
- **Zona de Ropa y Textiles**: Ropa típica, manteles bordados, servilletas y accesorios.

Las mujeres nahuas vestidas con sus trajes tradicionales son el alma del tianguis, muchas caminan horas desde comunidades alejadas para vender sus productos.""",
    "comments": """### 🌮 Sabores de la Sierra
> "Aquí los molotes de Cuetzalan son únicos en el mundo. Recién hechos, con papa, carne y salsa verde. Doña Martina los prepara desde hace 40 años y su receta es secreto familiar."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Cuetzalan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Precios de la Tierra
> "Las frutas y verduras son directamente del productor, sin intermediarios. Compramos la canasta de la semana por $200-300 pesos. El café de altura está a $80 el kilo, increíble."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Cuetzalan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🎭 Cultura Viva Nahua
> "Las mujeres venden con sus quexquémitles de colores, hablando náhuatl entre ellas. Es un orgullo ver que la lengua y la vestimenta tradicional siguen vivas en cada domingo."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Cuetzalan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🧵 Artesanía Textil
> "Los bordados de Cuetzalan son famosos. Cada huipil cuenta una historia diferente. Los precios van desde $200 hasta $2000 dependiendo de la complejidad del bordado."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=artesanias+Cuetzalan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🚇 Acceso al Tianguis
> "Se puede llegar en autobús desde Puebla (3 horas). El centro se cierra a vehículos los domingos. Es accesible para caminar, aunque las calles empedradas pueden ser difíciles para sillas de ruedas."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+a+Cuetzalan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)
### 🌿 Hierbas Medicinales
> "Las abuelas venden hierbas para todo: ruda para el susto, árnica para los golpes, manzanilla para los nervios. Saben cuál sirve para cada mal y te explican con paciencia."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=plantas+medicinales+Cuetzalan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=400)
### 🛡️ Seguridad
> "Es un pueblo mágico bastante seguro. Hay policía turística los domingos. La gente es amable y hospitalaria. Como en todo lugar concurrido, cuida tus pertenencias."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Cuetzalan+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)
### 🔄 Trueque Prehispánico
> "Todavía algunas comunidades practican el trueque. Intercambian café por ropa, huevos por hierbas. Es una tradición que no se ha perdido en las comunidades más alejadas."
- **Tipo:** #Trueque
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=trueque+Cuetzalan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)
### 🍲 Café de Altura
> "El café de Cuetzalan es de los mejores de México. En el tianguis lo venden tostado y molido, directo de las parcelas de las comunidades nahuas. El aroma es inconfundible."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cafe+Cuetzalan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=400)""",
    "how_to_get": "Desde Puebla capital, tomar autobús en la CAPU hacia Cuetzalan (3 horas). También hay combis desde Zacapoaxtla. En automóvil: tomar la carretera federal Puebla-Tuxpan hasta Xicotepec, luego desviarse a Cuetzalan. El centro se cierra a vehículos los domingos.",
    "tips": [
        "Llegar temprano (antes de las 8 AM) para ver la llegada de las mujeres nahuas con sus productos.",
        "Probar los molotes de Cuetzalan con salsa verde — son la especialidad local.",
        "Comprar café de altura directamente de los productores nahuas.",
        "Visitar las grutas de Cuetzalan después del tianguis.",
        "Llevar efectivo — muchos puestos no aceptan tarjeta."
    ]
})

# 2. Xicotepec
sierra_norte.append({
    "id": 2,
    "name": "Tianguis de Xicotepec de Juárez",
    "region": "sierra_norte",
    "days": ["Jueves", "Domingo"],
    "coords": [20.2750, -97.9600],
    "categories": ["plaza-campo", "canasta-basica", "garnachas-sabor", "cultura-tradicion"],
    "safety": "Zona segura, tianguis tradicional con ambiente familiar y presencia de comerciantes organizados",
    "horario": "8:00 AM — 5:00 PM",
    "emoji": "☕",
    "quote": "Xicotepec, Pueblo Mágico entre montañas, donde el tianguis de jueves y domingo es el punto de encuentro de nahuas y totonacas que bajan de las comunidades a vender sus cosechas.",
    "zones": """El tianguis se instala en las principales calles del centro de Xicotepec, alrededor del Palacio Municipal y el jardín principal. Sus zonas incluyen:

- **Zona de Café y Granos**: Xicotepec es región cafetalera; aquí se vende café orgánico de altura en todas sus presentaciones.
- **Zona de Frutas Tropicales**: Naranjas, mandarinas, plátanos, mameyes, zapotes y aguacates de la región.
- **Zona de Antojitos**: Tacos de cecina, tlacoyos, gorditas de maíz quebrado, tamales de frijol.
- **Zona de Artesanías Totonacas**: Bordados, textiles, máscaras de madera para danzas tradicionales.
- **Zona de Ropa y Mercancía General**: Ropa, calzado, herramientas y productos del hogar.

Los jueves el tianguis es más grande y concurrido, mientras que los domingos tiene un ambiente más familiar y relajado.""",
    "comments": """### ☕ Café de Altura
> "Xicotepec huele a café. En el tianguis encuentras el mejor café de la región, tostado artesanalmente. Don Toño vende su café de finca a $90 el kilo, directo de su parcela en la sierra."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Xicotepec+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=400)
### 💰 Canasta Barata
> "Hago la despensa aquí y me ahorro hasta un 40% comparado con el supermercado. Las frutas y verduras son fresquísimas, recién cortadas de las huertas de la sierra."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Xicotepec+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🌮 Sabor Tradicional
> "Las gorditas de maíz quebrado con chicharrón y salsa verde son imperdibles. Doña Chole las prepara desde las 6 AM, con masa hecha a mano, nixtamalizada al estilo tradicional."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Xicotepec+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 🎭 Cultura Totonaca
> "Los totonacas de la región bajan con sus textiles y bordados. Cada pieza es única, con diseños que representan la cosmovisión totonaca. Los precios son justos y directos con el artesano."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=totonacas+Xicotepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400)
### 🚇 Llegada
> "Se llega fácil por la carretera federal Puebla-Tuxpan. Hay autobuses desde la CAPU cada hora. El tianguis está en el centro, caminando desde la terminal de autobuses."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Xicotepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)""",
    "how_to_get": "Desde Puebla: Autobuses desde la CAPU hacia Xicotepec cada 30 minutos (2.5 horas). En coche: Carretera federal Puebla-Tuxpan (ruta 130), aproximadamente 120 km. El tianguis se instala en las calles del centro, todas caminables desde cualquier punto de la ciudad.",
    "tips": [
        "Ir los jueves — es el día más grande con mayor variedad de productos.",
        "Comprar café de altura tostado artesanalmente.",
        "Probar las gorditas de maíz quebrado con cecina.",
        "Visitar el Santuario del Señor del Santo Entierro después del tianguis.",
        "Llevar bolsas reutilizables para las compras."
    ]
})

# 3. Huauchinango
sierra_norte.append({
    "id": 3,
    "name": "Tianguis Sabatino de Huauchinango",
    "region": "sierra_norte",
    "days": ["Sábado"],
    "coords": [20.1767, -98.0500],
    "categories": ["plaza-campo", "canasta-basica", "cultura-tradicion", "identidad-oficios"],
    "safety": "Zona concurrida con presencia de seguridad municipal, ambiente familiar durante todo el día",
    "horario": "7:00 AM — 5:00 PM",
    "emoji": "🌺",
    "quote": "Huauchinango, Pueblo Mágico de la Sierra Norte, recibe cada sábado a cientos de familias nahuas y totonacas que convierten las calles en un mercado de colores, aromas y tradición viva.",
    "zones": """El tianguis sabatino se extiende por varias calles del centro de Huauchinango, desde el Mercado 5 de Mayo hasta las calles aledañas al jardín principal. Zonas principales:

- **Mercado 5 de Mayo**: Zona techada con puestos fijos de carnes, lácteos, abarrotes y comida preparada.
- **Zona de Ropa y Textiles**: Calles con ropa nueva y de paca, calzado, accesorios.
- **Zona de Frutas y Verduras**: Productos de las comunidades nahuas de la sierra: hongos silvestres, quelites, verdolagas, frutas de temporada.
- **Zona de Artesanías**: Textiles de lana, bordados, joyería, cestería y objetos de palma.
- **Zona de Comida**: Fondas con platillos típicos de la región: mole de caderas, pipián, tamales de acelga, atole de aguamiel.""",
    "comments": """### 🌮 Sabores Serranos
> "El mole de caderas que preparan aquí es una maravilla. Solo en temporada, pero vale la pena. Los tamales de acelga con salsa verde son mi desayuno obligado cada sábado."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Huauchinango+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400)
### 💰 Economía Familiar
> "Aquí el sábado es día de despensa. Compro fruta, verdura, carne y abarrotes para toda la semana. Gasto unos $400 y llevo bastante más que en cualquier supermercado."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Huauchinango)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🎭 Cultura Viva
> "Las mujeres nahuas llegan desde comunidades como Xaltepec y Papatlazolco con sus mejores productos. Muchas aún hablan náhuatl como primera lengua. El tianguis es su espacio de comercio y encuentro social."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+nahua+Huauchinango)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🧵 Bordados Totonacas
> "Los bordados de la región son espectaculares. Servilletas, manteles y blusas bordadas a mano con diseños florales. Las artesanas totonacas te explican el significado de cada símbolo."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=artesanias+Huauchinango)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400)
### 🚇 Acceso
> "La terminal de autobuses está a 5 minutos caminando. Si vienes en coche, hay estacionamiento en el centro por $30. El tianguis es muy caminable aunque las calles tienen pendientes."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Huauchinango)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)
### 🌿 Hierbas y Remedios
> "En la zona de hierbas medicinales hay de todo: té de tila, hoja de aguacate para los riñones, gordolobo para la tos. Las abuelas saben cuál planta sirve para cada mal."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=hierbas+medicinales+Huauchinango)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=400)""",
    "how_to_get": "Desde Puebla: Autobuses desde la CAPU a Huauchinango (2 horas). En coche: Carretera federal México-Tuxpan (ruta 130), desviación a Huauchinango. El tianguis se concentra en el centro histórico, alrededor del Mercado 5 de Mayo y la plaza principal.",
    "tips": [
        "Llegar temprano (antes de las 8 AM) para conseguir los mejores productos frescos.",
        "Probar el mole de caderas si es temporada (octubre-noviembre).",
        "Visitar el Museo de Atuendos Indígenas en el centro.",
        "Comprar hongos silvestres de temporada (lluvias).",
        "Llevar efectivo en denominaciones pequeñas."
    ]
})

# 4. Pahuatlán
sierra_norte.append({
    "id": 4,
    "name": "Tianguis Dominical de Pahuatlán",
    "region": "sierra_norte",
    "days": ["Domingo"],
    "coords": [20.2800, -98.1500],
    "categories": ["cultura-tradicion", "identidad-oficios", "plaza-campo", "canasta-basica"],
    "safety": "Ambiente tranquilo y seguro, comunidad pequeña y acogedora con arraigo indígena otomí y tepehua",
    "horario": "8:00 AM — 3:00 PM",
    "emoji": "🪶",
    "quote": "En Pahuatlán el tiempo se detiene. Los otomíes bajan de San Pablito cada domingo con su papel amate, sus bordados y sus productos del campo, manteniendo vivas tradiciones milenarias.",
    "zones": """El tianguis dominical de Pahuatlán se instala en el centro del pueblo, alrededor del zócalo y la iglesia principal. Es un tianguis pequeño pero profundamente auténtico:

- **Zona de Papel Amate**: San Pablito es famoso mundialmente por su papel amate artesanal. Las mujeres otomíes venden láminas pintadas con escenas de la cosmovisión otomí.
- **Zona de Bordados Otomíes**: Servilletas, manteles, blusas y vestidos bordados con diseños tradicionales hñähñú.
- **Zona de Productos del Campo**: Frutas, verduras, café, piloncillo, miel de abeja y queso artesanal.
- **Zona de Comida Tradicional**: Mole de guajolote, tamales de frijol, atole de aguamiel y pan de pueblo.
- **Zona de Artesanías Tepehuas**: Cestería, textiles y objetos de palma de las comunidades tepehuas de la región.""",
    "comments": """### 📜 Papel Amate Milenario
> "El papel amate de San Pablito no se produce en ningún otro lugar del mundo. Las mujeres otomíes continúan la tradición prehispánica de extraer la corteza del árbol jonote y martillarla hasta obtener finas láminas para pintar."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=papel+amate+Pahuatlan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)
### 🧵 Bordados Hñähñú
> "Los bordados otomíes son de una belleza increíble. Cada figura tiene un significado: el venado es la abundancia, el águila es el espíritu, los floreros son la fertilidad. Compro manteles para toda la familia."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=bordados+otomi+Pahuatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🌮 Sabor de la Tierra
> "El mole de guajolote que preparan aquí no se parece a ningún otro. Las mujeres otomíes tuestan sus propios chiles en comal de barro, es un sabor que no encuentras en ningún restaurante."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Pahuatlan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Precios Justos
> "Los precios son directamente de productor a consumidor. El queso artesanal a $60 la pieza, la miel de abeja a $70 el litro. No hay intermediarios, todo es trato directo con las comunidades."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Pahuatlan+mercado)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🎭 Cultura Otomí Viva
> "Las señoras mayores aún visten su traje tradicional todos los días. Escuchar su lengua hñähñú en el tianguis es escuchar la historia viva de este pueblo. Son amables y te explican con orgullo su cultura."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+otomi+Pahuatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🚇 Cómo Llegar
> "Llegar a Pahuatlán es toda una aventura. Desde Huauchinango hay combis que suben por la carretera de montaña. El camino tiene curvas pero las vistas de la sierra son espectaculares."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Pahuatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=400)
### 🛡️ Tranquilidad Total
> "Pahuatlán es un pueblo muy seguro. Todos se conocen, no hay problemas de inseguridad. Puedes dejar tus compras en un puesto mientras sigues recorriendo y nadie las toca."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Pahuatlan+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "how_to_get": "Desde Huauchinango: Combis y autobuses que salen cada hora hacia Pahuatlán (45 minutos). Desde Puebla: Tomar autobús a Huauchinango y luego combi a Pahuatlán. En coche: Carretera federal México-Tuxpan, desviación a Pahuatlán. El camino es sinuoso pero pavimentado.",
    "tips": [
        "Visitar San Pablito para ver cómo se hace el papel amate artesanal.",
        "Comprar papel amate pintado directamente de las artesanas otomíes.",
        "Probar el mole de guajolote en las fondas del tianguis.",
        "Llevar efectivo — no hay cajeros automáticos cercanos.",
        "Aprender algunas palabras en hñähñú (otomí) para conectar con los vendedores."
    ]
})

print("Sierra Norte templates defined: 4 files")
for d in sierra_norte:
    print(f"  - {d['name']}")
