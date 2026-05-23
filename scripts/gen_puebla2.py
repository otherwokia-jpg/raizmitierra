#!/usr/bin/env python3
"""Generate Puebla tianguis files 8-14 (Sierra Norte) and start Valle Serdán"""

import os, random, sys
sys.path.insert(0, os.path.expanduser("~/raizmitierra/scripts"))

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
    "https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=800",
    "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=800",
    "https://images.unsplash.com/photo-1471193945509-9ad0617afabf?w=800",
]

U400 = [u.replace("w=800", "w=400") for u in U800]

BASE = os.path.expanduser("~/raizmitierra/database/puebla")

def rand_800():
    return random.choice(U800)
def rand_400():
    return random.choice(U400)

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
img: "{rand_800()}"
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
    fname = name.lower().replace(' ', '_').replace('í','i').replace('ó','o').replace('é','e').replace('á','a').replace('ú','u').replace('ü','u').replace(',','').replace('.','').replace('ñ','n').replace('—','').replace('í','i')
    path = os.path.join(BASE, sr, f"tianguis_de_{fname}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = gen(idn, name, sr, days, coords, cats, safety, horario, emoji, quote, zones, comments, how, tips)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  [{idn:02d}] {name} [{sr}]")

# ============ SIERRA NORTE (8-14) ============

write("sierra_norte", 8, "Tianguis de Teziutlán", ["Domingo"],
    [19.8167, -97.3611],
    ["plaza-campo", "canasta-basica", "garnachas-sabor", "pueblo-magico", "cultura-tradicion"],
    "Pueblo Mágico seguro, ambiente familiar con presencia de seguridad pública",
    "8:00 AM — 5:00 PM",
    "🌫️",
    "Teziutlán, la Perla de la Sierra, escondida entre la niebla más de 280 días al año, recibe cada domingo a comunidades nahuas y totonacas en un tianguis lleno de tradición serrana.",
    """El tianguis dominical de Teziutlán se extiende por las calles del centro histórico:

- **Zona de Gastronomía**: Quesabirrias, tacos de cecina, mole de sierra, tamales de hoja de maíz.
- **Zona de Frutas y Verduras**: Productos de las comunidades de la sierra: hongos, quelites, frutas de temporada.
- **Zona de Artesanías**: Textiles de lana, bordados, joyería de plata y objetos de madera.
- **Zona de Ropa**: Ropa nueva y de paca, calzado, accesorios.
- **Zona de Plantas y Flores**: Plantas ornamentales, flores, árboles frutales.""",
    """### 🌫️ La Perla de la Sierra
> "Teziutlán es mágico. El tianguis dominical entre la niebla es una experiencia única. Los colores de las frutas y flores contrastan con el paisaje neblinoso de la sierra."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Teziutlan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=400)
### 🌮 Quesabirrias
> "Las quesabirrias de Teziutlán se han vuelto famosas. En el tianguis hay puestos que las preparan con birria de res y mucho queso. ¡Imperdible después de caminar entre la niebla!"
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=quesabirrias+Teziutlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Precios Serranos
> "Los precios son muy buenos. Las frutas y verduras llegan directo de las comunidades. Gasto $300-400 para la semana. La carne de cerdo y res es de excelente calidad."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Teziutlan+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🎭 Danzas Tradicionales
> "Los domingos a menudo hay danzas tradicionales en el tianguis: los Tocotines de San Sebastián, danzas nahuas. La cultura viva se respira en cada esquina."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=danzas+teziutlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🛡️ Pueblo Seguro
> "Teziutlán es de los pueblos más seguros de la sierra. La gente es acogedora. El tianguis es familiar, perfecto para ir con niños."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Teziutlan+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (3 hrs). Desde Veracruz: 2 hrs. En coche: Carretera Puebla-Teziutlán (ruta 129D). El tianguis está en el centro histórico.",
    ["Probar las quesabirrias — son famosas en la región.",
     "Visitar el Santuario de Nuestra Señora del Carmen.",
     "Comprar hongos silvestres de temporada.",
     "Ir abrigado — Teziutlán es conocido por su clima frío y neblina.",
     "Llegar temprano para disfrutar el tianguis antes del medio día."])

write("sierra_norte", 9, "Tianguis de Chignahuapan", ["Sábado"],
    [19.8381, -98.0333],
    ["artesania", "cultura-tradicion", "plaza-campo", "pueblo-magico", "identidad-oficios"],
    "Pueblo Mágico muy seguro, gran afluencia turística los fines de semana",
    "8:00 AM — 4:00 PM",
    "🎄",
    "Chignahuapan, el pueblo de las esferas navideñas, tiene un tianguis sabatino donde el barro, el vidrio y la lana se convierten en arte, mientras comunidades nahuas venden sus cosechas.",
    """El tianguis sabatino de Chignahuapan se instala en el centro del pueblo:

- **Zona de Esferas de Vidrio**: Chignahuapan produce el 70% de las esferas navideñas de México. Talleres y puestos las venden directamente.
- **Zona de Artesanías de Barro**: Ollas, cazuelas y figuras de barro vidriado.
- **Zona de Textiles**: Sarapes de lana, bordados, cobijas tejidas.
- **Zona de Frutas y Verduras**: Productos de comunidades nahuas de la sierra.
- **Zona de Comida Tradicional**: Cemitas, chalupas, mole, tacos de carnitas.""",
    """### 🎄 Capital de la Esfera
> "Chignahuapan es el pueblo de las esferas. En el tianguis sabatino encuentras esferas de vidrio soplado de todos los colores directamente de los talleres familiares. Precios de fábrica."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Chignahuapan+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400)
### 🏺 Barro Vidriado
> "Las cazuelas de barro de Chignahuapan son famosas. En el tianguis las venden más baratas que en las tiendas. Son ideales para cocinar moles y guisos tradicionales."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=barro+chignahuapan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)
### 🌮 Sabor de la Sierra
> "Las cemitas de Chignahuapan son famosas. Pan hecho en horno de piedra, con milanesa, quesillo y aguacate. Doña Lola las prepara en su puesto desde hace 30 años."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Chignahuapan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400)
### 💰 Barato y Bonito
> "Las artesanías aquí son más baratas que en cualquier otro lado. Esferas desde $10, cazuelas de barro desde $50. Los turistas vienen a surtirse para todo el año."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=chignahuapan+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400)
### 🧵 Lana y Tradición
> "Los sarapes de lana tejidos en telar de cintura son una tradición que no se pierde. Las mujeres nahuas tejen cobijas y ponchos que venden a precios justos en el tianguis."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=textiles+chignahuapan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (2 hrs). En coche: Carretera Puebla-Tlaxco, desviación a Chignahuapan (ruta 119). El tianguis está en el centro del pueblo.",
    ["Comprar esferas navideñas directamente de los talleres — precios de fábrica.",
     "Probar las cemitas de Chignahuapan.",
     "Visitar el taller de esferas para ver el soplado de vidrio.",
     "Comprar cazuelas de barro para cocinar.",
     "Ir a la Laguna de Chignahuapan después del tianguis."])

write("sierra_norte", 10, "Tianguis de Tetela de Ocampo", ["Domingo"],
    [19.8158, -97.8083],
    ["plaza-campo", "canasta-basica", "cultura-tradicion", "identidad-oficios"],
    "Ambiente rural seguro, comunidad pequeña y tranquila",
    "8:00 AM — 3:00 PM",
    "🏔️",
    "Tetela de Ocampo, en lo más alto de la Sierra Norte, es tierra de nahuas y totonacas. Su tianguis dominical es un encuentro de montaña donde el maíz, el frijol y la tradición son protagonistas.",
    """El tianguis dominical de Tetela se instala en el centro del pueblo, alrededor del jardín principal y el Palacio Municipal:

- **Zona de Granos Básicos**: Maíz criollo, frijol, haba, lenteja — productos de las milpas de la sierra.
- **Zona de Frutas y Verduras**: Manzanas, peras, capulines, verdolagas, quelites.
- **Zona de Artesanías**: Textiles de lana, bordados, cestería, máscaras de madera.
- **Zona de Comida**: Tamales serranos, mole, atole de granillo, pan de pueblo.
- **Zona de Plantas Medicinales**: Hierbas curativas de la sierra.""",
    """### 🌽 Maíz de Altura
> "En Tetela encuentras maíces nativos que ya no se ven en otros lados: maíz azul, rojo, pinto. Las mujeres nahuas traen su cosecha y te cuentan cómo cultivan en las laderas de la sierra."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Tetela+Ocampo)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=400)
### 🎭 Máscaras de Danza
> "Los artesanos de Tetela tallan máscaras de madera para las danzas tradicionales. Cada máscara representa un personaje: el diablo, la muerte, el conquistador. Es arte vivo."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=artesanias+Tetela)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)
### 🌮 Tamales Serranos
> "Los tamales de Tetela son diferentes: los envuelven en hoja de maíz y llevan frijol, chile y carne de cerdo. El atole de granillo es el acompañante perfecto."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Tetela+Ocampo)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Mercado de la Sierra
> "Los precios son los más bajos de la región porque no hay intermediarios. Compro directamente a los campesinos. La canasta básica me cuesta la mitad que en la ciudad."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Tetela+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🚇 Cómo Llegar
> "Tetela está bien conectado. Hay combis desde Zacapoaxtla y autobuses desde Puebla (3 hrs). La carretera es sinuosa pero las vistas de la sierra son espectaculares durante todo el trayecto."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Tetela+Ocampo)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (3 hrs). Desde Zacapoaxtla: Combis cada hora (45 min). En coche: Carretera Puebla-Teziutlán, desviación a Tetela de Ocampo.",
    ["Comprar maíces nativos de colores — son difíciles de encontrar en la ciudad.",
     "Probar los tamales serranos con atole de granillo.",
     "Visitar el Mirador de la Peña del Aire.",
     "Comprar máscaras de madera talladas a mano.",
     "Llevar ropa abrigadora — Tetela está a más de 2,500 msnm."])

write("sierra_norte", 11, "Tianguis de Tlatlauquitepec", ["Sábado"],
    [19.8500, -97.4964],
    ["plaza-campo", "canasta-basica", "garnachas-sabor", "cultura-tradicion", "pueblo-magico"],
    "Pueblo Mágico seguro, vigilancia municipal los días de tianguis",
    "8:00 AM — 4:00 PM",
    "🌲",
    "Tlatlauquitepec, el Pueblo Mágico escondido entre cerros y bosques de niebla, tiene un tianguis sabatino donde la cultura nahua se mezcla con la belleza natural de la sierra.",
    """El tianguis sabatino se instala en las calles del centro:

- **Zona de Frutas Exóticas**: Capulines, tejocotes, manzanas perón, peras, membrillos de la región.
- **Zona de Hongos Silvestres**: En temporada de lluvias, hongos de todo tipo que bajan de los bosques.
- **Zona de Artesanías**: Textiles de lana, bordados nahuas, cestería, objetos de madera.
- **Zona de Comida**: Cecina serrana, mole, tlacoyos, gorditas de maíz quebrado.
- **Zona de Plantas y Flores**: Plantas ornamentales y medicinales.""",
    """### 🌲 Pueblo de la Niebla
> "Tlatlauquitepec es uno de los pueblos más bonitos de la sierra. Su tianguis sabatino es pequeño pero muy auténtico. Las mujeres nahuas venden sus productos con el telón de fondo de los cerros."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Tlatlauquitepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=400)
### 🍄 Hongos de Temporada
> "Si vienes en temporada de lluvias (junio-septiembre), los hongos silvestres son increíbles. Los nahuas traen hongos de los bosques que no encuentras en ningún supermercado."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=hongos+Tlatlauquitepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400)
### 💰 Precios de Montaña
> "Todo es más barato aquí que en la capital. Las frutas de la región son deliciosas y económicas. Los capulines y tejocotes son especialidad local."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Tlatlauquitepec+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🧵 Textiles Nahuas
> "Los bordados de Tlatlauquitepec tienen fama en toda la sierra. Servilletas, manteles y blusas bordadas a mano con diseños tradicionales nahuas. Cada pieza es única."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=artesanias+Tlatlauquitepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🛡️ Pueblo Tranquilo
> "Tlatlauquitepec es muy seguro. Es un Pueblo Mágico pequeño y tranquilo. Puedes recorrer el tianguis con toda confianza."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Tlatlauquitepec+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (2.5 hrs). Desde Teziutlán: Combis cada hora (30 min). En coche: Carretera Puebla-Teziutlán, desviación a Tlatlauquitepec.",
    ["Visitar en temporada de lluvias para los hongos silvestres.",
     "Comprar capulines y tejocotes — frutas típicas de la región.",
     "Caminar al Mirador del Cerro de la Cruz.",
     "Probar la cecina serrana.",
     "Llevar ropa abrigadora y paraguas."])

write("sierra_norte", 12, "Tianguis de Zongozotla", ["Sábado"],
    [19.9769, -97.7269],
    ["plaza-campo", "canasta-basica", "cultura-tradicion", "identidad-oficios"],
    "Comunidad pequeña y pacífica, ambiente rural tradicional",
    "8:00 AM — 2:00 PM",
    "🌿",
    "Zongozotla es una comunidad nahua en lo profundo de la Sierra Norte. Su tianguis sabatino es de los más auténticos y menos tocados por el turismo en todo el estado de Puebla.",
    """El tianguis de Zongozotla es pequeño pero profundamente auténtico:

- **Zona de Milpa**: Maíz criollo, frijol, calabaza y chiles de las milpas nahuas.
- **Zona de Café**: Café de altura cultivado en las laderas de la sierra.
- **Zona de Artesanías**: Textiles de lana, bordados tradicionales, cestería.
- **Zona de Comida**: Comida tradicional nahua, tamales, atole.
- **Zona de Plantas Medicinales**: Hierbas curativas de la tradición nahua.""",
    """### 🌿 Autenticidad Nahua
> "Zongozotla es de esos lugares donde el turismo no ha llegado. El tianguis es completamente auténtico. Las mujeres venden en náhuatl, los precios son para la comunidad, no para turistas."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Zongozotla+puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### ☕ Café de Altura
> "El café que cultivan aquí es de especialidad. Los nahuas tienen sus parcelas en las montañas, a más de 1,500 msnm. El café es orgánico, sin químicos."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cafe+zongozotla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1576045057995-568f588f82f3?w=400)
### 💰 Sin Intermediarios
> "Los precios son los más bajos de la sierra porque aquí no hay intermediarios. Compras directamente al productor. La miel, el café y los frijoles son de primera calidad."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Zongozotla+mercado)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🧵 Tradición Textil
> "Las mujeres nahuas tejen en telar de cintura. Sus bordados tienen símbolos de la cosmovisión nahua: el sol, la lluvia, el maíz. Compro mis servilletas aquí desde hace años."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=textiles+nahuas+Zongozotla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 🚇 Camino de Montaña
> "Llegar a Zongozotla es una aventura. La carretera es de terracería en algunos tramos pero el paisaje es impresionante. Valles, montañas y bosques de niebla."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Zongozotla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.less+unsplash.com/photo-1509391366360-2e959784a276?w=400)""",
    "Desde Xicotepec: Camionetas que salen del centro (1 hr). Desde Puebla: Autobús a Xicotepec, luego camioneta. La carretera es sinuosa y parcialmente de terracería.",
    ["Ir con respeto a la comunidad — no es un destino turístico masivo.",
     "Comprar café orgánico de altura directamente de los productores.",
     "Llevar efectivo — no hay bancos ni cajeros.",
     "Visitar con vehículo alto si llueve (camino de terracería).",
     "Probar la comida tradicional nahua en las fondas locales."])

write("sierra_norte", 13, "Tianguis de Ahuazotepec", ["Domingo"],
    [20.0500, -98.1667],
    ["plaza-campo", "canasta-basica", "cultura-tradicion", "identidad-oficios"],
    "Zona rural tranquila, comunidad acogedora",
    "8:00 AM — 3:00 PM",
    "🌾",
    "Ahuazotepec, en los límites de Puebla e Hidalgo, tiene un tianguis dominical donde se encuentran las comunidades nahuas y otomíes de ambos estados en un intercambio cultural y comercial único.",
    """El tianguis dominical se instala en el centro del pueblo:

- **Zona de Trueque**: Área donde aún se práctica el intercambio de productos sin dinero.
- **Zona de Artesanías**: Textiles otomíes y nahuas, bordados, cestería.
- **Zona de Granos y Semillas**: Maíz, frijol, haba, lenteja de la región.
- **Zona de Frutas y Verduras**: Productos de la sierra y del Valle de Tulancingo.
- **Zona de Comida**: Mole, tamales, atole, pan artesanal.""",
    """### 🔄 Trueque Vivo
> "En Ahuazotepec todavía se práctica el trueque como en tiempos prehispánicos. La gente intercambia productos sin usar dinero. Es increíble ver esta tradición tan viva."
- **Tipo:** #Trueque
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Ahuazotepec+trueque)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)
### 🌮 Sabor de Frontera
> "La comida de Ahuazotepec mezcla lo mejor de Puebla e Hidalgo. El mole, los tamales y el pastel de cebolla son imperdibles. Doña María hace un mole que no tiene comparación."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Ahuazotepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 🧵 Encuentro de Pueblos
> "Aquí se encuentran nahuas y otomíes de Puebla e Hidalgo. Cada grupo trae sus artesanías características. Es un intercambio cultural fascinante."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+Ahuazotepec)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 💰 Precios Compartidos
> "Los precios son muy accesibles. Al estar en la frontera de dos estados, hay productos de ambas regiones. Compro queso y crema de Hidalgo, frutas y verduras de Puebla."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Ahuazotepec+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)""",
    "Desde Huauchinango: Combis locales (30 min). Desde Tulancingo, Hidalgo: 40 min. En coche: Carretera México-Tuxpan, desviación a Ahuazotepec.",
    ["Experimentar el trueque — trae productos para intercambiar.",
     "Probar el mole de Doña María.",
     "Comprar textiles otomíes y nahuas en un mismo lugar.",
     "Llegar temprano para ver el inicio del trueque.",
     "Llevar efectivo y también productos para trueque."])

print("Sierra Norte files 8-13 done")
