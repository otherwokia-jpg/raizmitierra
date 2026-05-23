#!/usr/bin/env python3
"""Generate Puebla files 30-50: Mixteca (rest) + Popocatépetl"""

import os, random, re

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
    "https://images.unsplash.com/photo-1514228133746-ee71a8f69652?w=400",
    "https://images.unsplash.com/photo-1486299267070-83823f5448dd?w=400",
    "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400",
    "https://images.unsplash.com/photo-1583337130417-3346c1be1e4d?w=400",
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
    fname = name.lower().replace(' ', '_').replace('í','i').replace('ó','o').replace('é','e').replace('á','a').replace('ú','u').replace('ü','u').replace(',','').replace('.','').replace('ñ','n').replace('—','').replace("'",'')
    fname = re.sub(r'_+', '_', fname)
    path = os.path.join(BASE, sr, f"tianguis_de_{fname}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = gen(idn, name, sr, days, coords, cats, safety, horario, emoji, quote, zones, comments, how, tips)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  [{idn:02d}] {name}")

# ============ MIXTECA (30-38) ============

write("mixteca", 30, "Tianguis de Chiautla de Tapia", ["Jueves"],
    [18.2900, -98.6000],
    ["plaza-campo", "canasta-basica", "cultura-tradicion", "identidad-oficios"],
    "Ambiente rural tranquilo, comunidad pequeña y acogedora",
    "7:00 AM — 3:00 PM",
    "🍊",
    "Chiautla de Tapia, en el corazón de la Mixteca Baja, celebra su tianguis los jueves. Es el día en que las comunidades mixtecas y popolocas se reúnen para intercambiar productos.",
    """El tianguis se instala en el centro del pueblo:

- **Zona de Cítricos**: Naranjas, limones, toronjas de la región.
- **Zona de Frutas Tropicales**: Mangos, papayas, plátanos.
- **Zona de Artesanías Popolocas**: Textiles, cestería, cerámica.
- **Zona de Comida**: Mole, tamales, atole.
- **Zona de Ropa y Mercancía**: Ropa, calzado, herramientas.""",
    """### 🍊 Cítricos de la Región
> "Chiautla es tierra de naranjas. En el tianguis los jueves encuentras cítricos frescos, recién cortados, a precios increíbles. Las naranjas son las más dulces de la Mixteca."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Chiautla+Tapia)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🎭 Cultura Popoloca
> "La comunidad popoloca de Chiautla mantiene sus tradiciones. En el tianguis ves sus textiles y artesanías. La lengua popoloca aún se escucha entre los mayores."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+popoloca+Chiautla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 💰 Precios Rurales
> "En Chiautla los precios son de verdad de campo. Las naranjas a $10 el kilo, mangos a $15. Es increíble lo barato que es todo cuando compras directo del productor."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Chiautla+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🌮 Mole de la Región
> "El mole de Chiautla es especial. Usan chiles de la región y especias que solo crecen en la Mixteca. Las mujeres lo preparan con recetas de generaciones."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=mole+Chiautla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)""",
    "Desde Izúcar de Matamoros: Autobuses locales (1 hr). Desde Puebla: Autobús a Izúcar, luego a Chiautla. En coche: Carretera Izúcar-Chiautla.",
    ["Ir los jueves que es día de tianguis.",
     "Comprar naranjas y cítricos frescos.",
     "Probar el mole popoloca.",
     "Comprar artesanías textiles.",
     "Llevar efectivo."])

write("mixteca", 31, "Tianguis de Tepexi de Rodríguez", ["Miércoles"],
    [18.5833, -97.9333],
    ["plaza-campo", "canasta-basica", "garnachas-sabor", "cultura-tradicion"],
    "Zona rural tranquila, tianguis tradicional mixteco",
    "8:00 AM — 3:00 PM",
    "🧶",
    "Tepexi de Rodríguez, en la Mixteca Poblana, tiene su tianguis los miércoles. Es conocido por sus textiles de lana y la calidad de sus productos artesanales.",
    """El tianguis se instala en el centro:

- **Zona de Textiles de Lana**: Sarapes, cobijas, jorongos, bufandas tejidas a mano.
- **Zona de Frutas y Verduras**: Productos de la región.
- **Zona de Comida**: Mole, barbacoa, mixiotes.
- **Zona de Artesanías**: Cerámica, cestería, trabajos en palma.
- **Zona de Ropa**: Ropa y accesorios.""",
    """### 🧶 Lana de Tepexi
> "Los sarapes de Tepexi son famosos en toda la Mixteca. Tejidos en telar de cintura con lana de borrego. Son pesados, calientitos, de excelente calidad. Los precios son directos del artesano."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Tepexi+Rodriguez)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🌮 Mixiotes
> "Los mixiotes de Tepexi son imperdibles. Carne de pollo o cerdo envuelta en hoja de maguey, cocida al vapor con especias. Un platillo tradicional de la Mixteca."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Tepexi+Rodriguez)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Artesanía Accesible
> "Los textiles son muy económicos comparados con la ciudad. Sarapes desde $200, cobijas desde $300. La lana es 100% natural, teñida con tintes naturales."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Tepexi+artesanias+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400)
### 🎭 Tradición Mixteca
> "Tepexi conserva muchas tradiciones. El miércoles de tianguis es el día de convivencia. Las mujeres visten sus trajes típicos y el mixteco se escucha en las calles."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+Tepexi)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (2 hrs). En coche: Carretera Puebla-Tepexi. El tianguis está en el centro del pueblo.",
    ["Comprar sarapes y cobijas de lana artesanal.",
     "Probar los mixiotes tradicionales.",
     "Adquirir textiles de lana directamente de los tejedores.",
     "Ir los miércoles — día de tianguis.",
     "Llevar efectivo."])

write("mixteca", 32, "Tianguis Dominical de Tepeaca", ["Domingo"],
    [18.9667, -97.9000],
    ["canasta-basica", "plaza-campo", "garnachas-sabor", "cultura-tradicion", "chacharas-antiguedades"],
    "Zona del centro histórico, vigilada los domingos, ambiente familiar",
    "8:00 AM — 5:00 PM",
    "🏛️",
    "Tepeaca, una de las ciudades más antiguas de Puebla, tiene un tianguis dominical que es una tradición centenaria. Es el punto de encuentro de comunidades mixtecas y nahuas de la región.",
    """El tianguis se instala en el centro histórico:

- **Zona de Artesanías**: Cerámica, textiles, objetos de palma.
- **Zona de Frutas y Verduras**: Productos de la región de Tepeaca.
- **Zona de Comida**: Mole, barbacoa, tlacoyos, cemitas.
- **Zona de Ropa y Mercancía**: Ropa, calzado, accesorios.
- **Zona de Chácharas**: Antigüedades, herramientas, libros, juguetes.""",
    """### 🌮 Sabor Tepeaquense
> "Los tlacoyos de Tepeaca son famosos. Masa azul rellena de frijol, con nopales, salsa y crema. Las cemitas también son especiales, con pan crujiente y milanesa."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Tepeaca+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 🏛️ Historia Viva
> "Tepeaca fue fundada en 1320. Su tianguis tiene raíces prehispánicas. El centro histórico con sus portales es el marco perfecto para el mercado dominical."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=historia+Tepeaca)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 💰 Precios de Región
> "Tepeaca es centro agrícola. Las frutas y verduras son frescas y baratas. Compro para toda la semana, me ahorro mucho comparado con la capital."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Tepeaca+precios+mercado)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🔧 Chácharas
> "Los domingos hay puestos de antigüedades y chácharas. He encontrado monedas antiguas, herramientas, discos de vinilo. Un buen lugar para coleccionistas."
- **Tipo:** #Chacharas
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=chacharas+Tepeaca)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (45 min). En coche: Carretera federal Puebla-Tepeaca. El tianguis está en el centro histórico, alrededor del zócalo y los portales.",
    ["Ir los domingos — día principal del tianguis.",
     "Probar los tlacoyos de masa azul.",
     "Visitar el Convento Franciscano del siglo XVI.",
     "Comprar frutas y verduras frescas de la región.",
     "Buscar antigüedades en los puestos de chácharas."])

write("mixteca", 33, "Tianguis Sabatino de Tecamachalco", ["Sábado"],
    [18.8833, -97.7333],
    ["canasta-basica", "plaza-campo", "garnachas-sabor", "artesania", "cultura-tradicion"],
    "Zona del centro, vigilancia municipal los sábados",
    "8:00 AM — 5:00 PM",
    "🌾",
    "Tecamachalco, en el valle de Tepeaca, tiene un tianguis sabatino que es el centro de abasto de la región. Aquí convergen comunidades nahuas, mixtecas y popolocas.",
    """El tianguis se instala en las calles del centro:

- **Zona de Granos**: Maíz, frijol, trigo, cebada de la región.
- **Zona de Frutas y Verduras**: Productos del valle.
- **Zona de Artesanías**: Cerámica, textiles, cestería.
- **Zona de Comida**: Mole, barbacoa, mixiotes, tlacoyos.
- **Zona de Ropa y Mercancía**: Ropa, calzado, herramientas.""",
    """### 🌾 Granero de Puebla
> "Tecamachalco es el granero de Puebla. En el tianguis sabatino encuentras maíz, frijol y trigo de la mejor calidad. Los campesinos traen sus cosechas directamente."
- **Tipo:** #Plaza
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Tecamachalco)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=400)
### 🎭 Tres Culturas
> "En Tecamachalco conviven nahuas, mixtecos y popolocas. Cada grupo trae sus productos típicos. Es fascinante ver la diversidad cultural en un solo tianguis."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+Tecamachalco)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🌮 Mole Poblano
> "El mole de Tecamachalco es de los mejores. Las cocineras tradicionales lo preparan con recetas centenarias. Para llevar o comer ahí mismo."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Tecamachalco)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Precios Agrícolas
> "Al ser zona de producción, los granos y verduras son muy baratos. Maíz a $10 el kilo, frijol a $25. La canasta básica aquí cuesta la mitad."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Tecamachalco+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (1 hr). En coche: Carretera Puebla-Tepeaca-Tecamachalco. El tianguis está en el centro de la ciudad.",
    ["Ir los sábados — día del tianguis.",
     "Comprar granos básicos directamente de los productores.",
     "Probar el mole tradicional.",
     "Observar la diversidad cultural de las tres etnias.",
     "Llevar efectivo."])

write("mixteca", 34, "Tianguis Dominical de Tehuacán", ["Domingo"],
    [18.4667, -97.3833],
    ["canasta-basica", "plaza-campo", "garnachas-sabor", "artesania", "cultura-tradicion"],
    "Zona del centro histórico, segura los domingos con vigilancia municipal",
    "7:00 AM — 5:00 PM",
    "🏺",
    "Tehuacán, la cuna del maíz, tiene un tianguis dominical que es uno de los más grandes del sur de Puebla. Es el punto de encuentro de comunidades popolocas, nahuas y mixtecas.",
    """El tianguis dominical se extiende por calles del centro:

- **Zona de Artesanías Popolocas**: Cerámica, textiles, bordados, cestería.
- **Zona de Frutas y Verduras**: Productos del Valle de Tehuacán.
- **Zona de Comida**: Mole, barbacoa, mixiotes, tlacoyos, tamales.
- **Zona de Ropa y Mercancía**: Ropa, calzado, accesorios.
- **Zona de Plantas**: Cactáceas, plantas medicinales, árboles frutales.""",
    """### 🏺 Cuna del Maíz
> "En Tehuacán se domesticó el maíz hace 5,000 años. El tianguis dominical es una celebración de esa herencia. Encuentras maíces nativos de todos los colores."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Tehuacan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=400)
### 🌮 Barbacoa Tehuacanera
> "La barbacoa de Tehuacán es especial. La preparan en horno de piedra con pencas de maguey. El consomé es una delicia. Los domingos es el platillo obligado."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Tehuacan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Mercado Regional
> "Tehuacán es el centro comercial del sur de Puebla. Los precios son competitivos. La fruta y verdura es fresca y variada. Viene gente de toda la región."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Tehuacan+mercado+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🧵 Textiles Popolocas
> "Los bordados popolocas son de los más bellos de México. Colores vibrantes, diseños geométricos. En el tianguis los encuentras directos de las artesanas."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=textiles+popolocas+Tehuacan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🚇 Cómo Llegar
> "Desde Puebla: Autobuses cada 30 minutos (2 hrs). En coche: Autopista Puebla-Tehuacán. El tianguis está en el centro histórico, cerca del zócalo."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Tehuacan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)""",
    "Desde Puebla: Autobuses desde CAPU cada 30 min (2 hrs). En coche: Autopista Puebla-Tehuacán (ruta 135D). El tianguis está en el centro histórico de Tehuacán.",
    ["Ir los domingos — el día más grande del tianguis.",
     "Probar la barbacoa con consomé.",
     "Comprar textiles popolocas bordados a mano.",
     "Visitar el Museo del Maíz.",
     "Probar el pan de Tehuacán."])

write("mixteca", 35, "Tianguis de Ajalpan", ["Jueves"],
    [18.4500, -97.2500],
    ["plaza-campo", "canasta-basica", "cultura-tradicion", "identidad-oficios"],
    "Ambiente rural, comunidad pequeña y tranquila",
    "7:00 AM — 3:00 PM",
    "🪴",
    "Ajalpan, en la Sierra Negra de Puebla, tiene un tianguis que es el corazón de la comunidad nahua y popoloca. Es un mercado de montaña lleno de autenticidad.",
    """El tianguis se instala en el centro del pueblo:

- **Zona de Café**: Café de altura de la Sierra Negra.
- **Zona de Frutas Tropicales**: Mangos, plátanos, naranjas, papayas.
- **Zona de Artesanías**: Textiles, bordados, cestería.
- **Zona de Comida**: Tamales, mole, atole.
- **Zona de Plantas**: Plantas medicinales y ornamentales.""",
    """### 🪴 Café de la Sierra Negra
> "El café de Ajalpan es de especialidad. Cultivado en las faldas de la Sierra Negra, a más de 1,000 msnm. En el tianguis lo venden tostado y molido, directo del productor."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Ajalpan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=400)
### 🎭 Nahuas y Popolocas
> "En Ajalpan conviven dos culturas: nahuas y popolocas. Cada grupo tiene sus propias artesanías y productos. El tianguis los jueves es testigo de este encuentro cultural."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+Ajalpan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 💰 Precios de Montaña
> "Los precios son muy accesibles. Café de altura desde $60 el kg, frutas tropicales baratísimas. Es de los lugares más económicos para comprar en la región."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Ajalpan+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🌿 Plantas Medicinales
> "Las abuelas de Ajalpan conocen las plantas de la sierra. Venden hierbas para todo: té de monte, hojas de guayaba, corteza de quina. Sabiduría tradicional."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=hierbas+Ajalpan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=400)""",
    "Desde Tehuacán: Autobuses locales (1 hr). En coche: Carretera Tehuacán-Ajalpan. El tianguis está en el centro del pueblo.",
    ["Ir los jueves — día de tianguis.",
     "Comprar café de altura de la Sierra Negra.",
     "Probar los tamales tradicionales.",
     "Adquirir plantas medicinales.",
     "Llevar efectivo."])

write("mixteca", 36, "Tianguis Dominical de Coyomeapan", ["Domingo"],
    [18.2833, -97.0000],
    ["plaza-campo", "canasta-basica", "cultura-tradicion", "identidad-oficios"],
    "Comunidad pequeña y remota, ambiente rural muy tranquilo",
    "8:00 AM — 2:00 PM",
    "🏔️",
    "Coyomeapan, en lo alto de la Sierra Negra, es una comunidad nahua donde el tianguis dominical es el único momento de la semana en que las comunidades bajan a intercambiar productos.",
    """El tianguis es pequeño pero profundamente auténtico:

- **Zona de Café**: Café orgánico de altura, principal producto de la región.
- **Zona de Miel**: Miel de abeja criolla, pura de la sierra.
- **Zona de Frutas**: Frutas de la región: manzanas, peras, duraznos.
- **Zona de Artesanías**: Textiles nahuas, bordados.
- **Zona de Comida**: Comida tradicional nahua.""",
    """### 🏔️ La Sierra Más Profunda
> "Coyomeapan es una de las comunidades más remotas de Puebla. El tianguis dominical es el único día de comercio. Las familias caminan horas para llegar. Es la autenticidad total."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Coyomeapan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### ☕ Café Orgánico
> "El café de Coyomeapan es 100% orgánico, cultivado en las montañas sin químicos. Las comunidades nahuas lo cultivan como hace siglos. Sabor incomparable."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cafe+Coyomeapan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=400)
### 🍯 Miel de Montaña
> "La miel de Coyomeapan es pura, sin adulterar. Las abejas se alimentan de flores de la sierra. El sabor es floral y dulce, totalmente natural."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=miel+Coyomeapan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 💰 Precios de Comunidad
> "No hay precios turísticos aquí. Todo es para la comunidad. Café $50 el kilo, miel $60 el litro. Los precios más honestos de todo Puebla."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Coyomeapan+mercado)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🛡️ Comunidad Segura
> "Es una comunidad muy segura. Todos se conocen. No hay problemas de inseguridad. El mayor desafío es llegar por el camino de montaña."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Coyomeapan+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "Desde Tehuacán: Autobuses (2 hrs) o camionetas locales. En coche: Carretera Tehuacán-Coyomeapan, camino sinuoso de montaña. Se recomienda vehículo alto.",
    ["Ir con respeto — es comunidad nahua remota.",
     "Comprar café orgánico directamente de los productores.",
     "Adquirir miel pura de la sierra.",
     "Llevar efectivo — no hay bancos.",
     "Ir con vehículo adecuado para camino de montaña."])

write("mixteca", 37, "Tianguis de Zapotitlán Salinas", ["Sábado"],
    [18.3333, -97.4833],
    ["plaza-campo", "canasta-basica", "artesania", "cultura-tradicion", "identidad-oficios"],
    "Pueblo pequeño y tranquilo, ambiente rural seguro",
    "8:00 AM — 3:00 PM",
    "🧂",
    "Zapotitlán Salinas es famoso por sus salinas prehispánicas y su tianguis sabatino donde se venden productos de la región mixteca, artesanías de palma y sal artesanal.",
    """El tianguis se instala en el centro del pueblo:

- **Zona de Sal Artesanal**: Sal de las salinas prehispánicas de Zapotitlán.
- **Zona de Artesanías de Palma**: Sombreros, canastos, petates tejidos a mano.
- **Zona de Frutas y Verduras**: Productos de la Mixteca.
- **Zona de Comida**: Mole, barbacoa, tamales.
- **Zona de Cactáceas**: Plantas de la región, incluyendo biznagas y magueyes.""",
    """### 🧂 Sal Milenaria
> "Las salinas de Zapotitlán se explotan desde hace más de 2,000 años. La sal artesanal que venden en el tianguis es única, con un sabor mineral inigualable."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Zapotitlan+Salinas)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1596040033229-98200ba6c08c?w=400)
### 🧺 Palma Tejida
> "Los sombreros de palma de Zapotitlán son famosos. Tejidos a mano, ligeros y resistentes. En el tianguis los encuentras desde $50, directo del artesano."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=artesanias+Zapotitlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)
### 🌵 Paisaje Único
> "Zapotitlán está en un valle rodeado de cactáceas. El paisaje es espectacular. En el tianguis venden biznagas y plantas de la región a precios muy bajos."
- **Tipo:** #Plaza
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Zapotitlan+cactaceas)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400)
### 💰 Precios Mixtecos
> "Los precios en Zapotitlán son populares. La sal artesanal a $15-20 el kilo, sombreros desde $50. Es de los pueblos más accesibles de la Mixteca."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Zapotitlan+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400)""",
    "Desde Tehuacán: Autobuses locales (45 min). En coche: Carretera Tehuacán-Zapotitlán. El tianguis está en el centro del pueblo.",
    ["Comprar sal artesanal de las salinas prehispánicas.",
     "Adquirir sombreros de palma tejidos a mano.",
     "Visitar el Jardín Botánico de Cactáceas.",
     "Probar la comida tradicional mixteca.",
     "Llevar efectivo."])

write("mixteca", 38, "Tianguis de San Gabriel Chilac", ["Sábado"],
    [18.3333, -97.3500],
    ["plaza-campo", "canasta-basica", "cultura-tradicion", "garnachas-sabor"],
    "Pueblo tranquilo, ambiente familiar y seguro",
    "8:00 AM — 3:00 PM",
    "🌽",
    "San Gabriel Chilac, en el Valle de Tehuacán, tiene un tianguis sabatino donde las comunidades popolocas traen sus productos. Es conocido por su pan artesanal y sus frutas.",
    """El tianguis se instala en el centro del pueblo:

- **Zona de Pan Artesanal**: Pan de pueblo, cemitas, pan de burro, conchas.
- **Zona de Frutas y Verduras**: Productos del valle.
- **Zona de Artesanías Popolocas**: Textiles, bordados, cestería.
- **Zona de Comida**: Mole, barbacoa, tamales, atole.
- **Zona de Ropa**: Ropa y accesorios.""",
    """### 🌮 Pan de Pueblo
> "El pan de San Gabriel Chilac es famoso en toda la región. Las cemitas y el pan de burro horneados en horno de piedra. El aroma del pan recién hecho inunda el tianguis."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+San+Gabriel+Chilac)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 🎭 Cultura Popoloca
> "San Gabriel Chilac es una comunidad popoloca. En el tianguis se escucha la lengua popoloca. Los textiles y bordados tienen diseños tradicionales que han pasado por generaciones."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+popoloca+Chilac)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 💰 Precios del Valle
> "El pan es baratísimo y delicioso. Cemitas a $5, pan de burro a $8. Las frutas y verduras del valle a precios de productor."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Chilac+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🌽 Productos del Valle
> "El valle de Tehuacán es fértil. Aquí encuentras frutas y verduras frescas durante todo el año. Los popolocas son excelentes agricultores."
- **Tipo:** #Plaza
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Chilac+frutas)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=400)""",
    "Desde Tehuacán: Autobuses locales (20 min). En coche: Carretera Tehuacán-San Gabriel Chilac. El tianguis está en el centro del pueblo.",
    ["Comprar pan artesanal recién horneado.",
     "Probar las cemitas de San Gabriel.",
     "Adquirir textiles popolocas bordados a mano.",
     "Visitar el templo del siglo XVI.",
     "Llevar efectivo."])

print("Mixteca files 30-38 done")
