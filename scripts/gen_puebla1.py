#!/usr/bin/env python3
"""Generate all 50 Puebla tianguis files."""

import os, random

BASE = os.path.expanduser("~/raizmitierra/database/puebla")

U800 = [
    "https://images.unsplash.com/photo-1586271476959-e3492e0f7e6f?w=800",
    "https://images.unsplash.com/photo-1555955591-95b56ea0f7a4?w=800",
    "https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=800",
    "https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=800",
    "https://images.unsplash.com/photo-1506905365341-3c04a535b966?w=800",
    "https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=800",
    "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800",
    "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800",
    "https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=800",
    "https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=800",
    "https://images.unsplash.com/photo-1560750588-73207b1ef5b8?w=800",
    "https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=800",
    "https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=800",
    "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=800",
    "https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=800",
    "https://images.unsplash.com/photo-1596040033229-98200ba6c08c?w=800",
    "https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=800",
    "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800",
    "https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=800",
    "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800",
    "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=800",
    "https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=800",
]

U400 = [
    "https://images.unsplash.com/photo-1586271476959-e3492e0f7e6f?w=400",
    "https://images.unsplash.com/photo-1555955591-95b56ea0f7a4?w=400",
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
    "https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400",
]

def rand_800():
    return random.choice(U800)

def rand_400():
    return random.choice(U400)

def gen(idn, name, region, sub, days, coords, cats, safety, horario, emoji, quote, zones, comments, how, tips):
    cs = ", ".join(f'"{c}"' for c in cats)
    ds = ", ".join(f'"{d}"' for d in days)
    t = "\n".join(f"- {tip}" for tip in tips)
    img = rand_800()
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
img: "{img}"
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
    sub = sr
    path = os.path.join(BASE, sr, f"tianguis_de_{name.lower().replace(' ','_').replace('—','').replace('í','i').replace('ó','o').replace('é','e').replace('á','a').replace('ú','u').replace('ü','u').replace(',','').replace('.','').replace('ñ','n')}.md")
    content = gen(idn, name, sr, sub, days, coords, cats, safety, horario, emoji, quote, zones, comments, how, tips)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  [{idn:02d}] {name}")

# ============ SIERRA NORTE (13) ============

write("sierra_norte", 1, "Tianguis Dominical de Cuetzalan", ["Domingo"],
    [20.0173, -97.5206],
    ["cultura-tradicion", "garnachas-sabor", "artesania", "plaza-campo", "identidad-oficios"],
    "Ambiente seguro y turístico, presencia de autoridades municipales los domingos",
    "7:00 AM — 4:00 PM",
    "🌽",
    "En Cuetzalan el tianguis no es solo mercado, es el corazón de la cultura nahua donde las mujeres con quexquémitl bordado venden sus productos como hace siglos.",
    """El tianguis dominical se despliega por las calles empedradas del centro, alrededor del zócalo y la Parroquia de San Francisco de Asís. Zonas principales:

- **Zona de Artesanías**: Textiles bordados a mano, quexquémitles, huipiles, bolsas de ixtle, joyería de filigrana y cerámica.
- **Zona de Flores y Plantas**: Orquídeas silvestres, flores de compasúchil, plantas medicinales y café de altura.
- **Zona de Alimentos**: Garnachas, molotes, tamales de hoja de maíz, atole de granillo y café de olla.
- **Zona de Frutas y Verduras**: Productos directos de las comunidades nahuas de las montañas.
- **Zona de Ropa y Textiles**: Ropa típica, manteles bordados, servilletas y accesorios.

Las mujeres nahuas vestidas con sus trajes tradicionales son el alma del tianguis, muchas caminan horas desde comunidades alejadas.""",
    """### 🌮 Los Molotes de Doña Martina
> "Los molotes de Cuetzalan son únicos. Doña Martina los prepara desde hace 40 años con papa, carne y salsa verde. Su receta es secreto familiar, no los encuentras igual en ningún lado."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Cuetzalan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Canasta Semanal
> "Hago la despensa aquí y ahorro mucho. Frutas, verduras y café directo del productor. La canasta semanal me sale en $250-300. El café de altura a $80 el kilo."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Cuetzalan+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🎭 Nahua Vivo
> "Las mujeres venden con sus quexquémitles de colores, hablando náhuatl entre ellas. Es un orgullo ver que la lengua y la vestimenta tradicional siguen vivas cada domingo en el zócalo."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+nahua+Cuetzalan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🧵 Bordados que Cuentan Historias
> "Cada huipil es una obra de arte. Los bordados representan la cosmovisión nahua: montañas, animales, flores. Los precios van de $200 a $2000 según la complejidad."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=artesanias+Cuetzalan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🚇 Cómo Llegar
> "Desde Puebla son 3 horas en autobús. El centro se cierra a autos los domingos. Las calles empedradas son pintorescas pero pueden ser difíciles para sillas de ruedas."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+a+Cuetzalan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)
### 🌿 Hierbas de las Abuelas
> "Las abuelas nahuas venden hierbas medicinales: ruda para el susto, árnica para golpes, manzanilla para nervios. Saben cuál sirve para cada mal y te explican con paciencia."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=hierbas+medicinales+Cuetzalan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=400)
### 🛡️ Andar Tranquilo
> "Pueblo Mágico bastante seguro. Hay policía turística los domingos. La gente es amable y hospitalaria. Como en todo lugar concurrido, cuidar tus pertenencias."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Cuetzalan+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)
### 🔄 Trueque que Perdura
> "Todavía se práctica el trueque en comunidades alejadas. Intercambian café por ropa, huevos por hierbas. Una tradición prehispánica que resiste en la sierra."
- **Tipo:** #Trueque
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=trueque+Cuetzalan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)
### ☕ Café de las Nubes
> "El café de Cuetzalan es de los mejores de México. Lo venden tostado y molido, directo de las parcelas nahuas. El aroma inunda todo el tianguis los domingos."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cafe+Cuetzalan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=400)""",
    "Desde Puebla: Autobuses en la CAPU hacia Cuetzalan (3 horas). Combis desde Zacapoaxtla. En auto: Carretera Puebla-Tuxpan hasta Xicotepec, desviación a Cuetzalan. El centro se cierra a vehículos los domingos.",
    ["Llegar antes de las 8 AM para ver la llegada de las mujeres nahuas con sus productos.",
     "Probar los molotes de Cuetzalan con salsa verde — la especialidad local.",
     "Comprar café de altura directamente de los productores nahuas.",
     "Visitar las grutas de Cuetzalan después del tianguis.",
     "Llevar efectivo — la mayoría no acepta tarjeta."])

write("sierra_norte", 2, "Tianguis de Xicotepec de Juárez", ["Jueves", "Domingo"],
    [20.2750, -97.9600],
    ["plaza-campo", "canasta-basica", "garnachas-sabor", "cultura-tradicion"],
    "Zona segura con ambiente familiar y comerciantes organizados",
    "8:00 AM — 5:00 PM",
    "☕",
    "Xicotepec, Pueblo Mágico entre montañas, donde el tianguis de jueves y domingo es el punto de encuentro de nahuas y totonacas que bajan de las comunidades a vender sus cosechas.",
    """El tianguis se instala en las principales calles del centro, alrededor del Palacio Municipal:

- **Zona de Café y Granos**: Café orgánico de altura en todas sus presentaciones, la especialidad de Xicotepec.
- **Zona de Frutas Tropicales**: Naranjas, mandarinas, plátanos, mameyes, zapotes y aguacates.
- **Zona de Antojitos**: Tacos de cecina, tlacoyos, gorditas de maíz quebrado, tamales de frijol.
- **Zona de Artesanías Totonacas**: Bordados, textiles, máscaras de madera para danzas tradicionales.
- **Zona de Ropa y Mercancía General**: Ropa, calzado, herramientas y productos del hogar.

Los jueves el tianguis es más grande y concurrido; los domingos tiene un ambiente más familiar.""",
    """### ☕ Café de Altura
> "Xicotepec huele a café. Don Toño vende su café de finca a $90 el kilo, tostado artesanalmente. El aroma del café recién molido es la bienvenida al tianguis."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Xicotepec+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=400)
### 💰 Ahorro Seguro
> "Hago la despensa aquí y ahorro hasta 40% comparado con el supermercado. Frutas y verduras fresquísimas, recién cortadas de las huertas de la sierra."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Xicotepec+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🌮 Gorditas de la Abuela
> "Las gorditas de maíz quebrado con chicharrón y salsa verde de Doña Chole son imperdibles. Masa hecha a mano, nixtamalizada al estilo tradicional. Desde las 6 AM ya está trabajando."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Xicotepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400)
### 🎭 Manos Totonacas
> "Los totonaca bajan con sus textiles y bordados. Cada pieza es única con diseños que representan su cosmovisión. Precios justos y trato directo con el artesano."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=totonacas+Xicotepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400)
### 🚇 Acceso
> "Autobuses desde la CAPU cada hora. El tianguis está en el centro, caminando desde la terminal. En coche, estacionamiento en el centro $30."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Xicotepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)
### 🍲 Cocina Tradicional
> "Los puestos de mole y pipián son espectaculares. Recetas que pasan de generación en generación. El mole poblano de Doña Juanita es famoso en toda la región."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=mole+Xicotepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)""",
    "Desde Puebla: Autobuses desde CAPU cada 30 min (2.5 hrs). En coche: Carretera federal 130 Puebla-Tuxpan, 120 km. El tianguis está en calles del centro, todo caminable.",
    ["Ir los jueves — es el día más grande con mayor variedad.",
     "Comprar café de altura tostado artesanalmente.",
     "Probar las gorditas de maíz quebrado con cecina.",
     "Visitar el Santuario del Señor del Santo Entierro.",
     "Llevar bolsas reutilizables para las compras."])

write("sierra_norte", 3, "Tianguis Sabatino de Huauchinango", ["Sábado"],
    [20.1767, -98.0500],
    ["plaza-campo", "canasta-basica", "cultura-tradicion", "identidad-oficios"],
    "Zona concurrida con seguridad municipal, ambiente familiar",
    "7:00 AM — 5:00 PM",
    "🌺",
    "Huauchinango, Pueblo Mágico de la Sierra Norte, recibe cada sábado a cientos de familias nahuas y totonacas que convierten las calles en un mercado de colores, aromas y tradición viva.",
    """El tianguis sabatino se extiende por varias calles del centro, desde el Mercado 5 de Mayo hasta calles aledañas al jardín principal:

- **Mercado 5 de Mayo**: Zona techada con puestos fijos de carnes, lácteos, abarrotes y comida preparada.
- **Zona de Ropa y Textiles**: Calles con ropa nueva y de paca, calzado, accesorios.
- **Zona de Frutas y Verduras**: Productos de comunidades nahuas: hongos silvestres, quelites, verdolagas.
- **Zona de Artesanías**: Textiles de lana, bordados, joyería, cestería y objetos de palma.
- **Zona de Comida**: Fondas con mole de caderas, pipián, tamales de acelga, atole de aguamiel.""",
    """### 🌮 Mole de Caderas
> "El mole de caderas solo se da en temporada (octubre-noviembre) y es una maravilla. Los tamales de acelga con salsa verde son mi desayuno obligado cada sábado."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Huauchinango+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400)
### 💰 Despensa Sabatina
> "Aquí el sábado es día de despensa. Gasto unos $400 y llevo bastante más que en el supermercado. Todo fresco y directo del productor."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Huauchinango+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🎭 Lengua Viva
> "Las mujeres nahuas llegan desde Xaltepec y Papatlazolco. Muchas aún hablan náhuatl como primera lengua. El tianguis es su espacio de comercio y encuentro social."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+nahua+Huauchinango)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🧵 Bordados Florales
> "Los bordados de la región son espectaculares: servilletas, manteles y blusas bordadas a mano con diseños florales. Las artesanas explican el significado de cada símbolo."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=artesanias+Huauchinango)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400)
### 🌿 Hierbas Curativas
> "En la zona de hierbas hay de todo: té de tila, hoja de aguacate para riñones, gordolobo para la tos. Las abuelas saben cuál planta sirve para cada mal."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=hierbas+Huauchinango)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=400)""",
    "Desde Puebla: Autobuses desde CAPU a Huauchinango (2 hrs). En coche: Carretera México-Tuxpan (130), desviación a Huauchinango. Tianguis en el centro histórico alrededor del Mercado 5 de Mayo.",
    ["Llegar antes de las 8 AM para los mejores productos frescos.",
     "Probar el mole de caderas si es temporada (octubre-noviembre).",
     "Visitar el Museo de Atuendos Indígenas en el centro.",
     "Comprar hongos silvestres de temporada.",
     "Llevar efectivo en denominaciones pequeñas."])

write("sierra_norte", 4, "Tianguis Dominical de Pahuatlán", ["Domingo"],
    [20.2800, -98.1500],
    ["cultura-tradicion", "identidad-oficios", "plaza-campo", "canasta-basica"],
    "Ambiente tranquilo, comunidad pequeña y acogedora con arraigo otomí",
    "8:00 AM — 3:00 PM",
    "🪶",
    "En Pahuatlán el tiempo se detiene. Los otomíes (hñähñú) bajan de San Pablito cada domingo con su papel amate, sus bordados y productos del campo, manteniendo vivas tradiciones milenarias.",
    """El tianguis dominical se instala en el centro del pueblo alrededor del zócalo:

- **Zona de Papel Amate**: San Pablito es famoso por su papel amate artesanal. Mujeres otomíes venden láminas pintadas con escenas de su cosmovisión.
- **Zona de Bordados Otomíes**: Servilletas, manteles, blusas con bordados tradicionales hñähñú.
- **Zona de Productos del Campo**: Frutas, verduras, café, piloncillo, miel y queso artesanal.
- **Zona de Comida Tradicional**: Mole de guajolote, tamales de frijol, atole de aguamiel.
- **Zona de Artesanías Tepehuas**: Cestería, textiles y objetos de palma.""",
    """### 📜 Papel Amate Milenario
> "El papel amate de San Pablito no se produce en ningún otro lugar. Las mujeres otomíes extraen la corteza del jonote y la martillan hasta obtener láminas para pintar. Es herencia prehispánica."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=papel+amate+Pahuatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)
### 🧵 Símbolos Hñähñú
> "Cada bordado tiene significado: el venado es abundancia, el águila es espíritu, los floreros fertilidad. Compro manteles bordados para toda la familia, son únicos."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=bordados+otomi+Pahuatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🌮 Mole de Guajolote
> "El mole de guajolote de las mujeres otomíes no se parece a ningún otro. Tuestan sus chiles en comal de barro. Es un sabor que no encuentras en restaurantes, solo aquí."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Pahuatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Trato Directo
> "Precios de productor a consumidor. Queso artesanal $60, miel de abeja $70 el litro. No hay intermediarios, todo es trato directo con las comunidades otomíes."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Pahuatlan+mercado)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🎭 Otomí Vivo
> "Las señoras mayores aún visten su traje tradicional. Escuchar la lengua hñähñú en el tianguis es escuchar historia viva. Son amables y explican su cultura con orgullo."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+otomi+Pahuatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)""",
    "Desde Huauchinango: Combis cada hora (45 min). Desde Puebla: Autobús a Huauchinango, luego combi. En coche: Carretera México-Tuxpan, desviación a Pahuatlán. Camino sinuoso pero pavimentado.",
    ["Visitar San Pablito para ver la elaboración del papel amate.",
     "Comprar papel amate pintado directamente de las artesanas.",
     "Probar el mole de guajolote en las fondas del tianguis.",
     "Llevar efectivo — no hay cajeros cercanos.",
     "Aprender algunas palabras en hñähñú para conectar con los vendedores."])

write("sierra_norte", 5, "Tianguis de San Pablito, Pahuatlán", ["Jueves"],
    [20.2630, -98.1300],
    ["cultura-tradicion", "identidad-oficios", "artesania", "plaza-campo"],
    "Comunidad pequeña y segura, ambiente rural tradicional",
    "8:00 AM — 2:00 PM",
    "🌿",
    "San Pablito es el corazón del papel amate en México. Aquí las familias otomíes mantienen viva la técnica prehispánica de extraer fibras del jonote para crear el lienzo donde pintan su cosmovisión.",
    """El tianguis de San Pablito es pequeño pero de gran riqueza cultural, instalado en la plaza principal de la comunidad:

- **Zona de Papel Amate**: El epicentro mundial del papel amate. Decenas de familias venden láminas de todos tamaños, pintadas a mano con escenas de la cosmovisión otomí.
- **Zona de Bordados**: Blusas, servilletas y manteles bordados con diseños tradicionales hñähñú.
- **Zona de Productos Locales**: Café orgánico, piloncillo, miel, frutas de la región.
- **Zona de Comida**: Comida típica otomí: tamales, atole, mole.""",
    """### 📜 Cuna del Papel Amate
> "San Pablito es el único lugar del mundo donde se produce papel amate de manera tradicional. Ver a las mujeres martillar la corteza del jonote por horas hasta obtener fibras suaves es impresionante."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=san+pablito+papel+amate)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)
### 🧵 Bordados Sagrados
> "Los diseños otomíes en los textiles no son solo adornos. Cada figura representa elementos de su cosmovisión: el maíz, el sol, la lluvia. Es su forma de escribir su historia."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=bordados+san+pablito)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 💰 Arte Accesible
> "Los precios del papel amate son muy accesibles. Desde $20 las láminas pequeñas hasta $500 las grandes y detalladas. Compro directamente a las artesanas, sin intermediarios."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=san+pablito+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🌮 Sabor Otomí
> "Los tamales de San Pablito son diferentes: los hacen con frijol y hoja de aguacate. El atole de aguamiel es delicioso y solo se consigue acá en la sierra."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+san+pablito)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 🛡️ Comunidad Segura
> "San Pablito es una comunidad pequeña donde todos se conocen. Es muy seguro caminar. La gente es increíblemente hospitalaria con los visitantes que llegan a conocer su cultura."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=san+pablito+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "Desde Pahuatlán: Camionetas locales que suben a San Pablito (20 min). Desde Huauchinango: Combis a Pahuatlán, luego camioneta a San Pablito.",
    ["Ver el proceso de elaboración del papel amate en los talleres familiares.",
     "Comprar papel amate pintado a mano directamente de las artesanas.",
     "Probar los tamales de frijol envueltos en hoja de aguacate.",
     "Contratar una visita guiada comunitaria para conocer la cultura otomí.",
     "Llevar efectivo — no hay bancos ni cajeros."])

write("sierra_norte", 6, "Tianguis de Zacapoaxtla", ["Miércoles"],
    [19.8728, -97.5872],
    ["plaza-campo", "canasta-basica", "animales-corral", "garnachas-sabor", "cultura-tradicion"],
    "Tianguis tradicional supervisado por autoridades locales, ambiente rural",
    "7:00 AM — 4:00 PM",
    "🐄",
    "Zacapoaxtla, la 'Heroica Ciudad de las Flores', recibe cada miércoles a las comunidades nahuas de la sierra en un tianguis que es una explosión de vida, colores y tradición.",
    """El tianguis de Zacapoaxtla es uno de los más importantes de la Sierra Norte, ocupando las calles del centro:

- **Plaza de Animales**: Zona de ganado bovino, porcino, ovino y aves de corral. Es de las más grandes de la región.
- **Zona de Frutas y Verduras**: Productos de las comunidades nahuas: papas, habas, frutas de temporada.
- **Zona de Antojitos**: Empanadas, caldos de pescado, mole en pasta, tlacoyos.
- **Zona de Artesanías**: Textiles, bordados, objetos de palma y madera.
- **Zona de Ropa y Mercancía**: Ropa, calzado, herramientas y productos básicos.""",
    """### 🐄 La Plazuela de Animales
> "La plaza de animales de Zacapoaxtla los miércoles es impresionante. Traen ganado de toda la sierra. Se respira el ambiente rural más auténtico de la región."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=zacapoaxtla+tianguis+animales)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1583337130417-3346c1be1e4d?w=400)
### 🐟 Caldo de Pescado
> "El caldo de pescado de Zacapoaxtla no tiene igual. Lo preparan con pescado fresco de la región, hierbabuena y chile. Un plato típico que no te puedes perder."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+zacapoaxtla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400)
### 💰 Economía Regional
> "Los miércoles todo Zacapoaxtla se mueve en torno al tianguis. Los precios son los mejores de la sierra, la competencia entre los puestos hace que todo sea más barato."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+zacapoaxtla+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🌽 Maíz de la Sierra
> "Aquí encuentras maíces nativos de todos los colores: azul, rojo, amarillo, blanco. Las mujeres nahuas traen su cosecha y te explican los usos de cada variedad."
- **Tipo:** #Plaza
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=maiz+nativo+zacapoaxtla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=400)
### 🚇 Acceso
> "La terminal de autobuses está a 3 calles del tianguis. Hay combis desde Zaragoza y Tlatlauquitepec. El miércoles es el día más movido, mejor llegar temprano."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Zacapoaxtla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)""",
    "Desde Puebla: Autobuses desde CAPU a Zacapoaxtla (2.5 hrs). Desde Teziutlán: Combis cada hora (45 min). En coche: Carretera Puebla-Teziutlán, desviación a Zacapoaxtla.",
    ["Ir los miércoles que es el día de tianguis grande.",
     "Visitar la plaza de animales (Plazuela) — es única.",
     "Probar el caldo de pescado en las fondas del centro.",
     "Comprar maíces nativos de colores.",
     "Llegar temprano para conseguir los mejores productos."])

write("sierra_norte", 7, "Tianguis Dominical de Zacatlán", ["Domingo"],
    [19.9320, -97.9580],
    ["cultura-tradicion", "artesania", "garnachas-sabor", "plaza-campo", "pueblo-magico"],
    "Pueblo Mágico seguro, vigilancia los días de tianguis",
    "8:00 AM — 4:00 PM",
    "🍎",
    "Zacatlán, el Pueblo Mágico de las manzanas y los relojes, recibe cada domingo a comunidades nahuas que bajan de las montañas con sus cosechas y artesanías.",
    """El tianguis dominical se instala en las calles del centro histórico alrededor del zócalo:

- **Zona de Manzanas y Derivados**: Sidra, manzanas frescas, dulces de manzana, ate — Zacatlán es la región manzanera de Puebla.
- **Zona de Artesanías**: Cerámica de barro, textiles de lana, objetos de cantera y madera, relojes artesanales.
- **Zona de Flores y Plantas**: Flores de temporada, plantas ornamentales, árboles frutales.
- **Zona de Comida Tradicional**: Tacos de carnitas, mole poblano, chalupas, cemitas.
- **Zona de Frutas y Verduras**: Productos de las comunidades nahuas de la sierra.""",
    """### 🍎 Tierra de Manzanas
> "La sidra y los dulces de manzana de Zacatlán son famosos en todo México. En el tianguis hay puestos que venden directamente de las productoras locales, más barato que en las tiendas turísticas."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Zacatlan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🎭 Cultura en las Calles
> "Zacatlán tiene una gran tradición artesanal. Los relojes monumentales, la cerámica y los textiles son orgullo local. El tianguis dominical es el mejor día para conocer la cultura viva del pueblo."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+Zacatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 💰 Precios de Pueblo
> "Los domingos hay ofertas en todo. Las frutas y verduras son más baratas que en los mercados de la capital. El queso artesanal y la crema son deliciosos y económicos."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Zacatlan+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🌮 Garnachas Serranas
> "Las chalupas zacatecas no son como las de la capital. Aquí las hacen con masa fresca, salsa verde y pollo deshebrado. Un sabor auténtico de la sierra."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=chalupas+Zacatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 🛡️ Turístico Seguro
> "Pueblo Mágico turístico, bastante seguro. Hay vigilancia los domingos. El tianguis es familiar, ideal para ir con niños. Solo cuidar lo básico en zonas concurridas."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Zacatlan+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (2 hrs). En coche: Carretera federal Puebla-Apizaco, desviación a Zacatlán. El centro cierra a vehículos los domingos.",
    ["Probar la sidra artesanal y los dulces de manzana.",
     "Visitar el Museo del Reloj.",
     "Comprar cerámica de barro directamente de los artesanos.",
     "Ir al Mirador de la Barranca de los Jilgueros.",
     "Llegar temprano para disfrutar el tianguis antes del turismo."])

print("Sierra Norte files 1-7 done")
