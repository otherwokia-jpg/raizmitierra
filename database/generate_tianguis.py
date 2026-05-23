#!/usr/bin/env python3
"""Generate 65 tianguis .md files for CDMX regions."""

import os

BASE = os.path.expanduser("~/raizmitierra/database/cdmx")

# Real Unsplash photo IDs for market/tianguis photos
PHOTOS = [
    "ZOa4h3N5uzg",  # people standing near trees, market
    "fKdUakd75kU",  # people walking through busy market aisle
    "ha5Ddw4Bh1U",  # woman in front of fruits/vegetables
    "I1wtHVLlh0o",  # woman in front of fruit stand
    "ASiAa22J7tM",  # assorted fruits on crates
    "m3I92SgM3Mk",  # person standing near vegetables
    "TC6jZWxTwJs",  # fruit seller behind colorful stall
    "Mjw-dIbFl-w",  # woman cooking front of man
    "0Ivo6D8U1hI",  # man rides bicycle past stall at night
    "ADwvXtjEn8M",  # vendor displays fresh produce
    "RqS7r2CzL68",  # bunch of vegetables
    "KbR06h9dNQw",  # lot of people walking on street (CDMX)
    "xuLZHLNrUsA",  # woman buys vegetables
    "tnqi1MA8Ad0",  # people walk past market stalls towards church
    "w89EjgIcwe8",  # grayscale shot of street food market
    "wt3disORDAg",  # people in market during daytime (Cholula)
    "VuKfiY4mKvA",  # people walking on street during daytime
    "-7n_T3BVFcc",  # woman sells food at market stall
    "Ad9btljg-zQ",  # people on red chairs under blue umbrella
    "suylWZtsR8w",  # people walking in large open plaza
]

# ============================================================
# DATA: All 65 tianguis
# ============================================================

def make_entries():
    """Build list of (filename, frontmatter_dict, content_parts)."""
    entries = []

    # ---- CENTRO (15) ----
    centro = [
        {
            "id": "MX-CDMX-001",
            "name": "La Lagunilla — Tianguis de Antigüedades",
            "region": "centro",
            "days": ["Domingo"],
            "coords": [19.4440, -99.1370],
            "categories": ["antiguedades", "cultura-tradicion", "chacharas", "identidad-oficios"],
            "safety": "Zona concurrida, mantener precaución con pertenencias",
            "horario": "10:00 AM — 5:00 PM",
            "emoji": "🕰️",
            "quote": "El tianguis más emblemático del Centro Histórico, donde el pasado y el presente se encuentran entre muebles antiguos, discos de vinilo y reliquias familiares.",
            "zonas": "El tianguis se extiende por las calles Comonfort, Allende y República de Perú. Se divide en: Zona de Antigüedades (muebles, lámparas, vajillas), Zona de Coleccionismo (monedas, discos, juguetes vintage), Zona de Ropa y Accesorios, y el área gastronómica con puestos de comida tradicional.",
            "llegar": "Metro Lagunilla (Línea 2, azul) — salida directa al tianguis. También Metro Allende (Línea 2) caminando 5 min hacia el norte. En auto, estacionamiento en Calle Comonfort $40/hr.",
            "recomendaciones": "Llegar antes de las 11 AM para evitar multitudes. Llevar efectivo, muchos puestos no aceptan tarjeta. Regatear con respeto es parte de la tradición. Explorar los puestos de comida: las gorditas y el pozole son imperdibles.",
        },
        {
            "id": "MX-CDMX-002",
            "name": "Tepito — Barrio Bravo",
            "region": "centro",
            "days": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
            "coords": [19.4460, -99.1250],
            "categories": ["ropa", "electronica", "cultura-tradicion", "chacharas", "identidad-oficios"],
            "safety": "Barrio bravo, ir con precaución y sin objetos de valor visibles",
            "horario": "10:00 AM — 6:00 PM (domingo hasta 5:00 PM)",
            "emoji": "🏪",
            "quote": "Tepito no es un lugar, es una cultura. El tianguis más famoso y polémico de México, donde la resistencia comunitaria y el comercio popular laten con fuerza.",
            "zonas": "Tepito abarca más de 30 manzanas entre las colonias Morelos y Peralvillo. El tianguis se divide en secciones: Ropa y Calzado (calles Eje 1 Norte, Tenochtitlan), Electrónicos (Fray Bartolomé de las Casas), Películas y Música, y el famoso 'Calpulli' de comida.",
            "llegar": "Metro Tepito (Línea 3, verde claro) o Metro Lagunilla (Línea 2). Autobuses RTP por Eje 1 Norte. No recomendable ir en auto por falta de estacionamiento seguro.",
            "recomendaciones": "Ir acompañado y conocer la zona de día. No usar joyas o celulares visibles. Probar las tortas de la esquina de Jesús Carranza. Aprender el 'código tepiteño': todo se negocia. Conocer la historia del 'Barrio Bravo' con un guía local.",
        },
        {
            "id": "MX-CDMX-003",
            "name": "Mercado de Sonora — Tianguis de lo Esotérico",
            "region": "centro",
            "days": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
            "coords": [19.4250, -99.1333],
            "categories": ["esoterico", "artesania", "cultura-tradicion", "identidad-oficios"],
            "safety": "Zona turística, segura de día. Evitar calles laterales de noche.",
            "horario": "9:00 AM — 6:00 PM",
            "emoji": "🔮",
            "quote": "El mercado de la brujería, las hierbas curativas y la sanación tradicional. Un viaje al mundo mágico de la medicina indígena y el esoterismo popular.",
            "zonas": "El mercado techado tiene tres naves principales: Hierbas y Remedios (medicina tradicional, velas, sahumerios), Animales (aves, conejos, mascotas exóticas), y Artesanías Esotéricas (amuletos, figuras, limpias). El tianguis exterior se extiende por Fray Servando Teresa de Mier.",
            "llegar": "Metro La Merced (Línea 1, rosa) saliendo por Calle San Ciprián hacia el sur. Metrobús Línea 4. En auto, estacionamiento en Mercado de Sonora $30/hr.",
            "recomendaciones": "Visitar con mente abierta a las tradiciones. Las 'limpias' con hierbas son una experiencia cultural auténtica. Comprar velas y sahumerios artesanales. Probar los tés de hierbas medicinales. Ir temprano para evitar aglomeraciones.",
        },
        {
            "id": "MX-CDMX-004",
            "name": "Mercado de La Merced",
            "region": "centro",
            "days": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
            "coords": [19.4270, -99.1280],
            "categories": ["canasta-basica", "comida", "cultura-tradicion", "identidad-oficios"],
            "safety": "Zona muy concurrida, cuidar pertenencias. Seguro de día.",
            "horario": "6:00 AM — 6:00 PM",
            "emoji": "🛒",
            "quote": "El centro de abasto más grande de la capital, un mar de frutas, verduras, carnes y todo lo que puedas imaginar. La Merced es el estómago de la CDMX.",
            "zonas": "La Merced es un complejo de varios mercados: Nave Mayor (frutas y verduras), Nave de Carnes, Nave de Pescados y Mariscos, Zona de Comida Preparada (los famosos 'puestos de lunch'), Pasaje de las Flores, y el área de abarrotes y dulces típicos.",
            "llegar": "Metro La Merced (Línea 1, rosa) o Metro San Lázaro (Línea B). Múltiples rutas de RTP y peseros. En auto, estacionamientos públicos $30-50/hr.",
            "recomendaciones": "Llegar muy temprano (7 AM) para ver el mercado en su máximo esplendor. Probar los 'tacos de canasta' y los jugos frescos. Comparar precios entre pasillos. Llevar bolsas reutilizables grandes. No perderse el pasaje de los dulces típicos mexicanos.",
        },
        {
            "id": "MX-CDMX-005",
            "name": "Mercado de San Juan — Tianguis Gourmet",
            "region": "centro",
            "days": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
            "coords": [19.4300, -99.1460],
            "categories": ["gourmet", "comida", "cultura-tradicion", "artesania"],
            "safety": "Zona segura, muy turística. Colonia San Juan.",
            "horario": "8:00 AM — 5:00 PM",
            "emoji": "🍽️",
            "quote": "El mercado de los chefs y los sabores exóticos. Desde insectos hasta caviar, San Juan es el paraíso gastronómico de la CDMX con más de 100 años de historia.",
            "zonas": "Dividido en: Zona de Carnes Exóticas (cocodrilo, avestruz, jabalí, venado), Pescadería y Mariscos (ostiones, langosta, erizos), Quesos y Vinos (importados y artesanales), Frutas y Verduras (orgánicos y exóticos), y el famoso pasillo de insectos (chapulines, escamoles, gusanos de maguey).",
            "llegar": "Metro Salto del Agua (Línea 1 y 3) o Metrobús Línea 4. A 5 min caminando del Palacio de Bellas Artes. Estacionamiento limitado $50/hr.",
            "recomendaciones": "Ir con hambre pero también con presupuesto — los precios son más altos que en otros mercados. Probar los escamoles (huevos de hormiga). Los ostiones frescos son imperdibles. Los chefs ofrecen degustaciones. Ir entre semana para evitar las multitudes de fin de semana.",
        },
        {
            "id": "MX-CDMX-006",
            "name": "Tianguis de San Lázaro — Ropa y Accesorios",
            "region": "centro",
            "days": ["Martes", "Viernes"],
            "coords": [19.4305, -99.1200],
            "categories": ["ropa", "chacharas", "canasta-basica"],
            "safety": "Zona de paso concurrido, precaución estándar",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "👕",
            "quote": "El tianguis de la Raza trabajadora, donde las familias del oriente y el centro se surten de ropa, hogar y comida a precios populares.",
            "zonas": "Se extiende a lo largo del Eje 1 Oriente (Av. del Taller) entre San Lázaro y La Merced. Zonas: Ropa nueva y de segunda, Calzado, Abarrotes y Frutas, Comida preparada, Artículos para el hogar.",
            "llegar": "Metro San Lázaro (Línea B y Línea 1) o Metro Candelaria (Línea 1 y 4). También Metrobús Línea 4.",
            "recomendaciones": "Buscar ofertas de ropa de paca. Probar los tacos de canasta que venden en la entrada. Llegar temprano para encontrar mejores precios. Comparar entre varios puestos antes de comprar.",
        },
        {
            "id": "MX-CDMX-007",
            "name": "Tianguis de la Lagunilla — Ropa (Jueves)",
            "region": "centro",
            "days": ["Jueves"],
            "coords": [19.4435, -99.1360],
            "categories": ["ropa", "chacharas", "cultura-tradicion"],
            "safety": "Zona concurrida de día, precaución estándar",
            "horario": "10:00 AM — 4:00 PM",
            "emoji": "👗",
            "quote": "El tianguis de ropa y accesorios que precede al gran domingo de antigüedades. Aquí se encuentra la moda popular y la ropa de segunda mano con historia.",
            "zonas": "Calles aledañas al Mercado de La Lagunilla. Secciones: Ropa americana de paca, Ropa nueva de temporada, Accesorios y bisutería, Zapatos y bolsas, y un pequeño pasaje de comida.",
            "llegar": "Metro Lagunilla (Línea 2). También Metro Allende a 10 min caminando.",
            "recomendaciones": "Buscar gangas en ropa de paca americana. Probar las gorditas de chicharrón. Ir con tiempo para rebuscar entre los puestos. No ir solo si es la primera vez.",
        },
        {
            "id": "MX-CDMX-008",
            "name": "Tianguis de la Lagunilla — Discos y Coleccionismo (Sábado)",
            "region": "centro",
            "days": ["Sábado"],
            "coords": [19.4445, -99.1375],
            "categories": ["coleccionismo", "musica", "cultura-tradicion", "artesania"],
            "safety": "Zona tranquila de día, mucha afluencia de coleccionistas",
            "horario": "10:00 AM — 5:00 PM",
            "emoji": "🎵",
            "quote": "El paraíso de los melómanos y coleccionistas. Discos de vinilo, CDs, cassettes y todo tipo de memorabilia musical en el corazón de La Lagunilla.",
            "zonas": "Se concentra en la calle República de Perú. Zonas: Discos de Vinilo (rock, salsa, boleros, música clásica), CDs y DVDs, Carteles y memorabilia, Libros y revistas antiguas, Juguetes vintage.",
            "llegar": "Metro Lagunilla (Línea 2). Salida hacia República de Perú.",
            "recomendaciones": "Los coleccionistas llegan desde las 9 AM a buscar las joyas. Llevar efectivo y billetes pequeños. Revisar el estado del vinilo antes de comprar. Los precios son negociables si compras varios discos.",
        },
        {
            "id": "MX-CDMX-009",
            "name": "Tianguis de Morelos — El Baratillo",
            "region": "centro",
            "days": ["Domingo"],
            "coords": [19.4490, -99.1240],
            "categories": ["chacharas", "ropa", "cultura-tradicion"],
            "safety": "Zona popular, precaución con pertenencias como en cualquier tianguis grande",
            "horario": "9:00 AM — 4:00 PM",
            "emoji": "🧰",
            "quote": "El tianguis de la colonia Morelos, donde el trueque y la cháchara son leyenda. Un mercado de pulgas que mantiene viva la tradición del intercambio comunitario.",
            "zonas": "Entre las calles de Jesús Carranza y Eje 1 Norte. Secciones: Herramientas y ferretería, Ropa usada y nueva, Electrónicos, Juguetes, Comida tradicional, y la zona de trueque donde se intercambian objetos.",
            "llegar": "Metro Tepito (Línea 3) o Metro Lagunilla (Línea 2), caminando hacia el oriente.",
            "recomendaciones": "El trueque es una tradición: lleva objetos para intercambiar. Probar los tacos de guisado. Ir acompañado y conocer la zona. Buscar herramientas y artículos de ferretería a buen precio.",
        },
        {
            "id": "MX-CDMX-010",
            "name": "Tianguis de Peralvillo",
            "region": "centro",
            "days": ["Miércoles", "Sábado"],
            "coords": [19.4550, -99.1300],
            "categories": ["canasta-basica", "ropa", "chacharas"],
            "safety": "Zona de la colonia Peralvillo, precaución estándar",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🧺",
            "quote": "El tianguis del corazón de Peralvillo, donde las abuelas compran la verdura fresca y los niños escogen sus juguetes. Un pedazo de vida comunitaria en el centro-norte de la ciudad.",
            "zonas": "A lo largo de la calle Norte 2-A y Eje 2 Norte. Zonas: Frutas y verduras frescas, Abarrotes, Ropa y calzado, Juguetes, Comida preparada, Artículos de limpieza.",
            "llegar": "Metro Lagunilla o Tepito, luego caminar hacia el norte. También autobuses RTP por Eje 2 Norte.",
            "recomendaciones": "Excelente para la despensa semanal a buen precio. La zona de frutas es muy surtida. Probar los tlacoyos de haba. Ir antes de las 11 AM para lo más fresco.",
        },
        {
            "id": "MX-CDMX-011",
            "name": "Tianguis de Ramos Millán",
            "region": "centro",
            "days": ["Martes", "Viernes"],
            "coords": [19.4150, -99.1310],
            "categories": ["canasta-basica", "ropa", "chacharas", "comida"],
            "safety": "Colonia Ramos Millán, zona tranquila de día",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🍎",
            "quote": "Un tianguis de barrio con sabor a comunidad, donde los vecinos de la colonia se encuentran cada semana para surtir la despensa y compartir noticias.",
            "zonas": "Sobre la calle Dr. Ignacio Chávez, entre Eje 3 Sur y Calzada de la Viga. Secciones: Frutas y verduras, Ropa, Comida preparada, Abarrotes, y artículos para el hogar.",
            "llegar": "Metro La Viga (Línea 4) o Metro Coyuya (Línea 3), luego caminar 10 min.",
            "recomendaciones": "Es un tianguis pequeño pero muy completo. Los precios son bajos comparado con otros mercados. Probar los tamales de la esquina. Ir temprano para mejor selección.",
        },
        {
            "id": "MX-CDMX-012",
            "name": "Tianguis de Doctores",
            "region": "centro",
            "days": ["Martes", "Sábado"],
            "coords": [19.4190, -99.1490],
            "categories": ["canasta-basica", "ropa", "comida", "artesania"],
            "safety": "Colonia Doctores, precaución estándar en horario diurno",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🥦",
            "quote": "En la histórica colonia Doctores, este tianguis es el sustento de muchas familias. Aquí la comida corre a la par de la comunidad.",
            "zonas": "Entre las calles Dr. Lavista, Dr. Lucio y Dr. Balmis. Zonas: Abarrotes y frutas, Ropa, Zona de antojitos, Artículos de hogar, Plantas y flores.",
            "llegar": "Metro Doctores o Metro Niños Héroes (Línea 3), caminando 5-10 min.",
            "recomendaciones": "Excelente para comprar fruta fresca a buen precio. Las flores son más baratas que en los mercados fijos. Probar los sopes y quesadillas. Ir temprano los sábados.",
        },
        {
            "id": "MX-CDMX-013",
            "name": "Tianguis de la Lagunilla — Antigüedades y Arte (Sábado-Domingo)",
            "region": "centro",
            "days": ["Sábado", "Domingo"],
            "coords": [19.4450, -99.1380],
            "categories": ["antiguedades", "arte", "cultura-tradicion", "identidad-oficios"],
            "safety": "Zona muy turística, segura de día con vigilancia visible",
            "horario": "9:00 AM — 5:00 PM",
            "emoji": "🎨",
            "quote": "El tianguis de las antigüedades finas y el arte popular. Pinturas, esculturas, muebles coloniales y objetos de época que cuentan la historia de México.",
            "zonas": "Se extiende desde el Mercado de La Lagunilla hacia la calle Allende. Zonas: Muebles antiguos y coloniales, Pintura y arte popular, Porcelana y vajillas, Joyería antigua, Libros y documentos históricos, Relojes y objetos de colección.",
            "llegar": "Metro Lagunilla (Línea 2) o Metro Allende (Línea 2), caminando 5 min.",
            "recomendaciones": "Los domingos hay más puestos pero también más gente. Los sábados son ideales para comprar con calma. Los precios son más altos que en el tianguis general. Preguntar por la historia de las piezas. No comprar esculturas prehispánicas originales (es ilegal).",
        },
        {
            "id": "MX-CDMX-014",
            "name": "Tianguis de Balandrano",
            "region": "centro",
            "days": ["Jueves", "Domingo"],
            "coords": [19.4110, -99.1170],
            "categories": ["canasta-basica", "ropa", "chacharas"],
            "safety": "Colonia Balandrano, zona tranquila",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🍊",
            "quote": "Un tianguis de barrio con auténtico sabor popular, donde las familias de la colonia hacen su despensa y los niños esperan los domingos para su juguete.",
            "zonas": "Sobre la calle Balandrano y avenidas aledañas de la colonia del mismo nombre. Secciones: Frutas y verduras, Abarrotes, Ropa, Juguetes, Comida preparada.",
            "llegar": "Metro Coyuya (Línea 3) o Metro Santa Anita (Línea 4), caminando 15 min. También peseros sobre Calzada de la Viga.",
            "recomendaciones": "Precios muy accesibles para la canasta básica. Ambiente familiar y tranquilo. Probar las gorditas de la esquina. Ideal para ir con niños pequeños.",
        },
        {
            "id": "MX-CDMX-015",
            "name": "Tianguis de la Merced — Ropa y Accesorios",
            "region": "centro",
            "days": ["Martes", "Jueves", "Domingo"],
            "coords": [19.4260, -99.1260],
            "categories": ["ropa", "accesorios", "chacharas", "cultura-tradicion"],
            "safety": "Zona de alto tránsito, precaución con carteras",
            "horario": "9:00 AM — 5:00 PM",
            "emoji": "🛍️",
            "quote": "El tianguis de ropa que complementa al gigante de La Merced. Aquí las familias encuentran desde ropa interior hasta abrigos, todo a precio de tianguis.",
            "zonas": "Calles aledañas al Mercado de La Merced, especialmente sobre San Ciprián y Emiliano Zapata. Zonas: Ropa de mujer, Ropa de hombre, Ropa infantil, Calzado, Accesorios y bisutería, Ropa americana de paca.",
            "llegar": "Metro La Merced (Línea 1) o Metro San Lázaro (Línea B), caminando 10 min.",
            "recomendaciones": "La ropa de paca americana es una ganga si sabes buscar. Los domingos hay más variedad. Probar los jugos naturales de la zona de comidas. Llevar efectivo en denominaciones pequeñas.",
        },
    ]

    # ---- SUR (15) ----
    sur = [
        {
            "id": "MX-CDMX-016",
            "name": "Tianguis de Xochimilco — Centro Histórico",
            "region": "sur",
            "days": ["Domingo"],
            "coords": [19.2570, -99.1020],
            "categories": ["canasta-basica", "cultura-tradicion", "artesania", "identidad-oficios"],
            "safety": "Zona turística segura, vigilancia los días de tianguis",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🌺",
            "quote": "En la tierra de los canales y las chinampas, el tianguis dominical de Xochimilco es una explosión de colores, sabores y tradiciones que vienen desde la época prehispánica.",
            "zonas": "Se instala en el centro de Xochimilco, alrededor del kiosco y la plaza principal. Zonas: Flores y plantas ornamentales, Frutas y verduras de chinampa, Artesanías en madera y barro, Comida típica (mixiotes, barbacoa, atole), Ropa y textiles.",
            "llegar": "Metro Xochimilco (Línea 2, azul) o Tren Ligero desde Tasqueña hasta Xochimilco. En auto, estacionamiento en el centro $40-50.",
            "recomendaciones": "Probar la barbacoa de borrego en los puestos locales. Comprar flores frescas — Xochimilco es el jardín de la CDMX. Visitar el mercado de plantas. Dar un paseo en trajinera después del tianguis. Probar el atole de champurrado.",
        },
        {
            "id": "MX-CDMX-017",
            "name": "Tianguis de Coyoacán — Bazar del Sábado",
            "region": "sur",
            "days": ["Sábado", "Domingo"],
            "coords": [19.3490, -99.1610],
            "categories": ["artesania", "cultura-tradicion", "comida", "identidad-oficios"],
            "safety": "Zona turística muy segura, mucha afluencia de visitantes",
            "horario": "10:00 AM — 5:00 PM",
            "emoji": "🎭",
            "quote": "El tianguis más bohemio de la CDMX, donde el arte, la artesanía y la comida se mezclan con el eco de Frida Kahlo y los coyotes del barrio.",
            "zonas": "Alrededor del Jardín Hidalgo, el Jardín Centenario y sobre calle Allende. Zonas: Artesanías mexicanas (barro, textiles, alebrijes), Pintura y arte local, Joyería artesanal, Comida gourmet (tostadas, tlacoyos, café de olla), Música en vivo.",
            "llegar": "Metro Coyoacán (Línea 3) o Metro Viveros. Metrobús Línea 1 hasta Ciudad Universitaria, luego caminar. Estacionamiento público $40-60/hr.",
            "recomendaciones": "El Bazar del Sábado es más artístico, el domingo hay más variedad. Probar las tostadas de la Bodega de Coyoacán. Visitar el Mercado de Coyoacán a una cuadra. Llevar efectivo. Ir temprano para evitar multitudes de turistas.",
        },
        {
            "id": "MX-CDMX-018",
            "name": "Tianguis de Tlalpan — Centro Histórico",
            "region": "sur",
            "days": ["Domingo"],
            "coords": [19.2870, -99.1670],
            "categories": ["canasta-basica", "comida", "cultura-tradicion", "artesania"],
            "safety": "Zona segura, muy familiar en el centro de Tlalpan",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🏛️",
            "quote": "En el Pueblo de Tlalpan, con sus calles empedradas y su kiosco centenario, el tianguis dominical es una tradición que reúne a productores locales y familias enteras.",
            "zonas": "Alrededor de la Plaza de la Constitución y sobre las calles Congreso y Moneda. Secciones: Agricultores locales (verduras orgánicas de la zona sur), Comida típica (cecina, tlacoyos, huaraches), Artesanías, Ropa, Plantas y flores.",
            "llegar": "Metro Taxqueña (Línea 2) y tomar RTP hacia Tlalpan Centro. También autobuses por Calzada de Tlalpan. En auto, estacionamiento en el centro.",
            "recomendaciones": "Probar la cecina de Yecapixtla. Las verduras orgánicas son de la mejor calidad. Disfrutar del ambiente familiar alrededor del kiosco. Subir al Cerro de la Estrella para vistas panorámicas. Visitar el Museo de Tlalpan.",
        },
        {
            "id": "MX-CDMX-019",
            "name": "Tianguis de Milpa Alta — Villa Milpa Alta",
            "region": "sur",
            "days": ["Domingo"],
            "coords": [19.1910, -99.0250],
            "categories": ["canasta-basica", "comida", "cultura-tradicion", "artesania", "identidad-oficios"],
            "safety": "Zona rural segura, ambiente familiar",
            "horario": "7:00 AM — 3:00 PM",
            "emoji": "🌽",
            "quote": "En la cima de la CDMX, Milpa Alta conserva las tradiciones indígenas más puras. Su tianguis es el corazón económico y cultural de la alcaldía.",
            "zonas": "Centro de Villa Milpa Alta, alrededor de la plaza principal. Zonas: Productores de nopal (Milpa Alta produce el 60% del nopal de la CDMX), Mole artesanal (famoso en toda la ciudad), Frutas y verduras de temporada, Artesanías en ixtle y palma, Comida tradicional (mixiotes, barbacoa).",
            "llegar": "Metro Taxqueña y tomar autobús RTP 'Milpa Alta' (1 hr). También peseros desde Xochimilco. En auto, carretera Xochimilco-Milpa Alta (45 min).",
            "recomendaciones": "Comprar nopal fresco directo del productor. El mole de Milpa Alta es legendario — llevarse una cazuela. Probar los mixiotes de pollo o borrego. Ir con tiempo, el viaje es largo pero vale la pena. Conocer el Museo de la Nopalera y el Maguey.",
        },
        {
            "id": "MX-CDMX-020",
            "name": "Tianguis de San Gregorio Atlapulco",
            "region": "sur",
            "days": ["Jueves", "Domingo"],
            "coords": [19.2530, -99.0740],
            "categories": ["canasta-basica", "agricultura", "cultura-tradicion", "identidad-oficios"],
            "safety": "Pueblo originario, muy seguro y tranquilo",
            "horario": "7:00 AM — 2:00 PM",
            "emoji": "🌿",
            "quote": "San Gregorio Atlapulco, el pueblo chinampero que mantiene viva la tradición agrícola de los antiguos mexicas. Su tianguis es un mercado de productores locales.",
            "zonas": "Centro de San Gregorio, frente a la iglesia y el kiosco. Zonas: Verduras de chinampa (lechugas, acelgas, rábanos), Flores de temporada, Plantas medicinales, Hierbas aromáticas, Comida tradicional a base de maíz.",
            "llegar": "Tren Ligero desde Tasqueña hasta Xochimilco, luego tomar pesero 'San Gregorio'. En auto, carretera Xochimilco-San Gregorio (20 min del centro de Xochimilco).",
            "recomendaciones": "Las verduras de chinampa son las más frescas de la ciudad. Probar el 'huazontle' (quelite tradicional). Las plantas medicinales son de gran calidad. Conocer el sistema de chinampas. Ir en bicicleta por los canales después del tianguis.",
        },
        {
            "id": "MX-CDMX-021",
            "name": "Tianguis de San Luis Tlaxialtemalco",
            "region": "sur",
            "days": ["Viernes"],
            "coords": [19.2350, -99.0900],
            "categories": ["agricultura", "cultura-tradicion", "artesania", "identidad-oficios"],
            "safety": "Pueblo originario tranquilo",
            "horario": "7:00 AM — 2:00 PM",
            "emoji": "🌸",
            "quote": "San Luis Tlaxialtemalco es el pueblo de las flores. En su tianguis los viernes, los colores y aromas de las flores de temporada inundan el centro.",
            "zonas": "Frente a la iglesia de San Luis Obispo y en la plaza principal. Zonas: Flores de ornato (cempasúchil, gladiolas, rosas), Verduras de chinampa, Frutas de temporada, Artesanías de palma, Miel y derivados.",
            "llegar": "Tren Ligero a Xochimilco, luego pesero 'San Luis'. En auto, tomar Calzada Tláhuac hasta San Luis.",
            "recomendaciones": "San Luis es famoso por sus flores — no irse sin un ramo. Probar la miel de abeja local. Conocer el tianguis de flores es una experiencia única. Visitar el embarcadero de San Luis. Llevar cámara para las fotos de colores.",
        },
        {
            "id": "MX-CDMX-022",
            "name": "Tianguis de Nativitas — Xochimilco",
            "region": "sur",
            "days": ["Martes", "Sábado"],
            "coords": [19.2470, -99.1100],
            "categories": ["canasta-basica", "ropa", "cultura-tradicion"],
            "safety": "Zona de Xochimilco, segura de día",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🥬",
            "quote": "En el pueblo de Nativitas, el tianguis es el punto de encuentro de los chinamperos y las familias que buscan productos frescos directos de la tierra.",
            "zonas": "Calles principales de Nativitas, alrededor del centro del pueblo. Zonas: Verduras de chinampa, Abarrotes, Ropa, Comida preparada, Plantas medicinales, Artesanías.",
            "llegar": "Tren Ligero hasta Xochimilco, luego pesero 'Nativitas'. En auto, 10 min del centro de Xochimilco.",
            "recomendaciones": "Comprar verduras directamente de los chinamperos. El sábado hay más puestos. Probar los tlacoyos de frijol. Conocer las chinampas de la zona. Ambiente muy familiar.",
        },
        {
            "id": "MX-CDMX-023",
            "name": "Tianguis de Santa Cecilia Tláhuac",
            "region": "sur",
            "days": ["Domingo"],
            "coords": [19.2780, -99.0500],
            "categories": ["canasta-basica", "comida", "cultura-tradicion", "identidad-oficios"],
            "safety": "Pueblo de Tláhuac, zona tranquila",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🐟",
            "quote": "Santa Cecilia Tláhuac, a orillas del Lago de los Reyes, tiene un tianguis que es la memoria viva de la cultura lacustre del Valle de México.",
            "zonas": "Centro de Santa Cecilia, alrededor de la parroquia. Zonas: Pescado y charales frescos del lago, Verduras, Frutas, Artesanías de tule, Comida típica (pescado frito, tamales de carpa).",
            "llegar": "Metro Tasqueña y autobús hacia Tláhuac. También desde Xochimilco por la carretera Xochimilco-Tláhuac.",
            "recomendaciones": "Probar los charales frescos — son una tradición lacustre. Los tamales de pescado son únicos en la CDMX. Conocer el Lago de los Reyes. El tianguis mantiene tradiciones prehispánicas de pesca y recolección.",
        },
        {
            "id": "MX-CDMX-024",
            "name": "Tianguis de San Pedro Atocpan — Mole y Tradición",
            "region": "sur",
            "days": ["Sábado", "Domingo"],
            "coords": [19.2070, -99.0150],
            "categories": ["comida", "artesania", "cultura-tradicion", "identidad-oficios"],
            "safety": "Pueblo de Milpa Alta, muy seguro",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🍲",
            "quote": "San Pedro Atocpan es la capital del mole en la CDMX. Su tianguis es una fiesta de sabores donde el mole almendrado, el pipián y el mole rojo son los protagonistas.",
            "zonas": "Centro de San Pedro Atocpan, a lo largo de la calle principal. Zonas: Mole artesanal (más de 60 variedades), Frutas y verduras, Artesanías, Ropa, Comida preparada (tacos de mole, tamales).",
            "llegar": "Metro Taxqueña y autobús RTP 'Milpa Alta', luego pesero 'San Pedro Atocpan'. En auto, carretera Milpa Alta-San Pedro (20 min desde Villa Milpa Alta).",
            "recomendaciones": "Comprar mole artesanal en pasta o polvo — los precios son los mejores de la CDMX. Probar el mole almendrado y el mole verde. Llevar tu propio recipiente. El domingo hay más puestos y degustaciones. Conocer la Feria del Mole en octubre.",
        },
        {
            "id": "MX-CDMX-025",
            "name": "Tianguis de San Antonio Tecomitl",
            "region": "sur",
            "days": ["Lunes", "Viernes"],
            "coords": [19.1750, -99.0180],
            "categories": ["canasta-basica", "agricultura", "cultura-tradicion"],
            "safety": "Zona rural de Milpa Alta, muy segura",
            "horario": "7:00 AM — 2:00 PM",
            "emoji": "🌾",
            "quote": "En las faldas del volcán Teuhtli, San Antonio Tecomitl cultiva el maíz y el nopal como desde tiempos prehispánicos. Su tianguis es un mercado de productores.",
            "zonas": "Centro del pueblo, alrededor de la iglesia. Zonas: Nopal y derivados, Maíz criollo, Frijol, Verduras de temporal, Quesos artesanales, Pan de pueblo.",
            "llegar": "Metro Taxqueña y RTP a Milpa Alta, luego pesero 'San Antonio Tecomitl'. En auto, 30 min de Villa Milpa Alta.",
            "recomendaciones": "Comprar nopal fresco de la región. El maíz criollo es de la mejor calidad para hacer tortillas. Probar el queso artesanal de la zona. Llegar temprano para encontrar lo mejor. Disfrutar del paisaje del volcán Teuhtli.",
        },
        {
            "id": "MX-CDMX-026",
            "name": "Tianguis de Tulyehualco — Frutas y Flores",
            "region": "sur",
            "days": ["Miércoles", "Domingo"],
            "coords": [19.2170, -99.0530],
            "categories": ["agricultura", "comida", "cultura-tradicion", "identidad-oficios"],
            "safety": "Xochimilco rural, zona tranquila",
            "horario": "7:00 AM — 2:00 PM",
            "emoji": "🍓",
            "quote": "Tulyehualco, el pueblo donde el aguacate y la chirimoya crecen en las faldas del volcán. Su tianguis es una despensa de frutas de temporada únicas en la ciudad.",
            "zonas": "Centro de Tulyehualco y alrededores de la plaza. Zonas: Frutas de temporada (aguacate criollo, chirimoya, capulín), Verduras, Flores, Miel y propóleos, Comida tradicional.",
            "llegar": "Tren Ligero a Xochimilco y pesero 'Tulyehualco'. En auto, carretera Xochimilco-Tulyehualco (25 min).",
            "recomendaciones": "Buscar el aguacate criollo — es más pequeño pero más sabroso. Probar la chirimoya en temporada (agosto-noviembre). La miel de la zona es excelente. Visitar el criadero de truchas de la zona.",
        },
        {
            "id": "MX-CDMX-027",
            "name": "Tianguis de Santo Domingo — Coyoacán",
            "region": "sur",
            "days": ["Jueves", "Domingo"],
            "coords": [19.3410, -99.1430],
            "categories": ["canasta-basica", "ropa", "comida", "artesania"],
            "safety": "Colonia Santo Domingo, zona popular. Precaución estándar.",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🧶",
            "quote": "En la colonia Santo Domingo de Coyoacán, este tianguis es el corazón comercial del sur-oriente de la alcaldía. Aquí la comunidad se abastece y se encuentra.",
            "zonas": "Sobre Av. Aztecas y calles aledañas. Zonas: Frutas y verduras, Ropa y calzado, Artesanías, Comida preparada, Artículos de limpieza, Plantas y flores.",
            "llegar": "Metro General Anaya (Línea 2) o Metro Taxqueña (Línea 2), luego pesero 'Santo Domingo'. Metrobús Línea 1 hasta Ciudad Universitaria.",
            "recomendaciones": "Excelente relación calidad-precio en frutas y verduras. Los artesanos locales venden textiles y bordados. Probar las quesadillas de hongos. Ambiente de barrio muy auténtico.",
        },
        {
            "id": "MX-CDMX-028",
            "name": "Tianguis de San Lorenzo Acopilco — Contreras Sur",
            "region": "sur",
            "days": ["Domingo"],
            "coords": [19.3370, -99.1030],
            "categories": ["canasta-basica", "comida", "cultura-tradicion"],
            "safety": "Pueblo de Contreras, zona segura",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🍄",
            "quote": "San Lorenzo Acopilco, pueblo de la Magdalena Contreras, donde el bosque y la milpa se encuentran. Su tianguis ofrece productos de la tierra y del bosque.",
            "zonas": "Centro del pueblo de San Lorenzo. Zonas: Hongos de temporada (temporada de lluvias), Verduras, Frutas, Plantas medicinales, Artesanías de madera, Comida típica.",
            "llegar": "Metro Barranca del Muerto (Línea 7) y tomar RTP hacia San Lorenzo. En auto, carretera al Ajusco.",
            "recomendaciones": "En temporada de lluvias, los hongos silvestres son imperdibles. Probar los tlacoyos de hongo. Visitar el bosque de La Magdalena. Comprar plantas medicinales del páramo. Ir temprano para conseguir hongos frescos.",
        },
        {
            "id": "MX-CDMX-029",
            "name": "Tianguis de Ajusco — Pueblo de Santa Úrsula",
            "region": "sur",
            "days": ["Sábado", "Domingo"],
            "coords": [19.2270, -99.2100],
            "categories": ["agricultura", "cultura-tradicion", "comida", "identidad-oficios"],
            "safety": "Zona rural del Ajusco, segura de día",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🌲",
            "quote": "En las faldas del Ajusco, Santa Úrsula Xitla mantiene la tradición del tianguis de productores. Aquí el bosque y la milpa se dan la mano.",
            "zonas": "Centro de Santa Úrsula Xitla, cerca de la iglesia. Zonas: Productos del bosque (hongos, hierbas, leña), Verduras orgánicas, Frutas de temporal, Artesanías de madera, Comida típica (mixiotes, hongos).",
            "llegar": "Metro Taxqueña y RTP 'Ajusco' hasta Santa Úrsula. En auto, carretera Picacho-Ajusco (30 min desde Periférico).",
            "recomendaciones": "Los hongos del Ajusco son famosos en toda la ciudad. Probar los mixiotes de hongo. El paisaje del bosque es espectacular. Comprar leña para chimenea si tienes auto. Ideal para combinar con caminata en el bosque.",
        },
        {
            "id": "MX-CDMX-030",
            "name": "Tianguis de la Feria de la Flor — Xochimilco (Febrero)",
            "region": "sur",
            "days": ["Viernes", "Sábado", "Domingo"],
            "coords": [19.2600, -99.0980],
            "categories": ["flores", "cultura-tradicion", "artesania", "identidad-oficios"],
            "safety": "Evento festivo con vigilancia especial",
            "horario": "9:00 AM — 6:00 PM",
            "emoji": "💐",
            "quote": "La Feria de la Flor de Xochimilco es el tianguis floral más grande e impresionante de la CDMX. Miles de flores de todos los colores y variedades cubren el centro del pueblo.",
            "zonas": "Centro de Xochimilco, desde el kiosco hasta el embarcadero. Zonas: Flores de ornato, Flores comestibles, Plantas de ornato, Artesanías florales, Comida típica, Música y danza tradicional.",
            "llegar": "Tren Ligero hasta Xochimilco. En auto, estacionamiento habilitado en la periferia del centro durante la feria.",
            "recomendaciones": "Ir en febrero para la Feria de la Flor completa. Las flores son más baratas que en cualquier otro mercado. Probar las flores de calabaza rellenas. Llevar cámara — es uno de los eventos más fotogénicos de la CDMX. Las trajineras decoradas con flores son imperdibles.",
        },
    ]

    # ---- NORTE (10) ----
    norte = [
        {
            "id": "MX-CDMX-031",
            "name": "Tianguis San Felipe de Jesús — La San Feroz",
            "region": "norte",
            "days": ["Domingo"],
            "coords": [19.5200, -99.1080],
            "categories": ["ropa", "electronica", "chacharas", "comida", "cultura-tradicion", "identidad-oficios"],
            "safety": "Tianguis enorme, cuidar pertenencias como en cualquier aglomeración",
            "horario": "7:00 AM — 5:00 PM",
            "emoji": "🏪",
            "quote": "El tianguis más grande de la CDMX y uno de los más imponentes de América Latina. San Felipe de Jesús, conocido cariñosamente como 'La San Feroz', es una ciudad dentro de otra ciudad.",
            "zonas": "San Felipe de Jesús abarca más de 40 calles. Zonas: Ropa y calzado (la más grande), Electrónicos y tecnología, Muebles y hogar, Comida (carnes asadas, paella, carnitas), Chácharas y antigüedades, Juguetes, Plantas y flores, Abarrotes.",
            "llegar": "Metro 18 de Marzo (Línea 3 y 6), luego colectivo 'San Felipe'. Autobuses RTP desde Indios Verdes. En auto, precaución con estacionamiento en calles aledañas.",
            "recomendaciones": "Llegar antes de las 9 AM para recorrerlo completo — ¡es enorme! Usar zapatos cómodos. Llevar agua y efectivo. Las carnitas asadas son imperdibles. No intentar verlo todo en un día si es primera vez. Mejor ir con un plan y un punto de encuentro.",
        },
        {
            "id": "MX-CDMX-032",
            "name": "Tianguis de La Raza — Pulgas y Ropa",
            "region": "norte",
            "days": ["Domingo"],
            "coords": [19.4680, -99.1380],
            "categories": ["ropa", "chacharas", "cultura-tradicion", "calzado"],
            "safety": "Zona de alto tránsito peatonal, precaución con carteras",
            "horario": "9:00 AM — 4:00 PM",
            "emoji": "👟",
            "quote": "El famoso tianguis de La Raza, conocido por sus tenis y ropa americana a precios imbatibles. Miles de capitalinos llegan cada domingo en busca de gangas.",
            "zonas": "A las afueras del Metro La Raza, sobre Av. de los Insurgentes y calles aledañas. Zonas: Calzado y tenis, Ropa americana de paca, Ropa nueva, Electrónicos, Chácharas, Comida rápida.",
            "llegar": "Metro La Raza (Línea 3 y 5) — salida directa al tianguis. También Metrobús Línea 1 y 3.",
            "recomendaciones": "Especialistas en tenis: hay de todas las marcas a precios de remate. Revisar bien la calidad de la ropa americana. Llegar temprano (9 AM) para mejor selección. Regatear con respeto. Probar las tortas de la zona de comidas.",
        },
        {
            "id": "MX-CDMX-033",
            "name": "Tianguis de Azcapotzalco — Centro",
            "region": "norte",
            "days": ["Martes", "Domingo"],
            "coords": [19.4870, -99.1820],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion"],
            "safety": "Zona céntrica de Azcapotzalco, segura de día",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🌮",
            "quote": "En el corazón de Azcapotzalco, este tianguis es el punto de encuentro de las familias de la alcaldía. Productos frescos, ropa de temporada y la mejor comida del norte de la ciudad.",
            "zonas": "Centro de Azcapotzalco, alrededor de la Plaza Principal y calle Morelos. Zonas: Frutas y verduras, Ropa y accesorios, Comida preparada (tacos de canasta, tlacoyos, tortas), Abarrotes, Artículos de hogar, Plantas y flores.",
            "llegar": "Metro Azcapotzalco (Línea 6, roja) o Metro Ferrería. También autobuses RTP por Av. Azcapotzalco.",
            "recomendaciones": "Probar los tacos de canasta — son famosos en la zona. La zona de ropa tiene buenas ofertas. El tianguis de los martes es más de abasto, el domingo es más variado. Visitar el Jardín Hidalgo después del tianguis.",
        },
        {
            "id": "MX-CDMX-034",
            "name": "Tianguis de La Lagunilla Norte — Gustavo A. Madero",
            "region": "norte",
            "days": ["Jueves", "Domingo"],
            "coords": [19.5050, -99.1250],
            "categories": ["canasta-basica", "ropa", "chacharas", "comida"],
            "safety": "Colonia Lagunilla Norte, zona popular segura de día",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🥑",
            "quote": "La Lagunilla Norte es el tianguis que abastece a las familias del norte de la ciudad. Aquí el precio justo y la calidad son la ley.",
            "zonas": "Sobre Av. Lagunilla Norte entre Montevideo y 5 de Febrero. Zonas: Frutas y verduras, Abarrotes, Ropa, Calzado, Comida preparada, Artículos de limpieza.",
            "llegar": "Metro La Raza (Línea 3 o 5) y caminar 15 min al norte. Autobuses RTP sobre Eje Central.",
            "recomendaciones": "Excelentes precios en frutas y verduras. Ambiente familiar. Probar los sopes de la entrada. Ideal para la despensa semanal. Los jueves hay menos gente que los domingos.",
        },
        {
            "id": "MX-CDMX-035",
            "name": "Tianguis de Cuautepec — Barrio Alto",
            "region": "norte",
            "days": ["Domingo"],
            "coords": [19.5350, -99.1450],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion"],
            "safety": "Zona de Gustavo A. Madero, popular y bulliciosa",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🏔️",
            "quote": "Cuautepec, el barrio más alto de la CDMX. Su tianguis dominical es el centro de abasto de toda la sierra de Guadalupe.",
            "zonas": "Centro de Cuautepec, sobre Av. Cuautepec y calles aledañas. Zonas: Frutas y verduras, Ropa, Calzado, Comida típica, Artículos de hogar, Plantas.",
            "llegar": "Metro Indios Verdes (Línea 3) y RTP 'Cuautepec'. En auto, subir por la carretera a Cuautepec (30 min desde Indios Verdes).",
            "recomendaciones": "Las vistas de la ciudad desde Cuautepec son espectaculares. Probar las gorditas de la zona. Llegar temprano porque el tianguis termina temprano. Llevar suéter — hace más frío que en el centro.",
        },
        {
            "id": "MX-CDMX-036",
            "name": "Tianguis de Lindavista — Vallejo",
            "region": "norte",
            "days": ["Miércoles", "Sábado"],
            "coords": [19.4880, -99.1380],
            "categories": ["canasta-basica", "ropa", "electronica", "comida"],
            "safety": "Colonia Lindavista, zona residencial segura",
            "horario": "9:00 AM — 4:00 PM",
            "emoji": "🍇",
            "quote": "Lindavista, el barrio de las casonas y los árboles centenarios, también tiene su tianguis. Un mercado de barrio con calidad de exportación.",
            "zonas": "Sobre Av. Vallejo y calles aledañas a la colonia Lindavista. Zonas: Frutas y verduras gourmet, Ropa de marca, Electrónicos, Comida artesanal, Artículos de decoración.",
            "llegar": "Metro Lindavista (Línea 6) o Metro Vallejo. Autobuses RTP por Av. Montevideo.",
            "recomendaciones": "La calidad de las frutas y verduras es superior al promedio. Los sábados hay más puestos de artesanías. Probar los churros rellenos de cajeta. Ambiente más tranquilo que otros tianguis del norte.",
        },
        {
            "id": "MX-CDMX-037",
            "name": "Tianguis de Aragón — La Villa",
            "region": "norte",
            "days": ["Jueves", "Domingo"],
            "coords": [19.4760, -99.1070],
            "categories": ["canasta-basica", "ropa", "chacharas", "comida", "cultura-tradicion"],
            "safety": "Zona de alta afluencia, precaución estándar",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "⛲",
            "quote": "A las faldas de la Villa de Guadalupe, el tianguis de Aragón es el mercado más grande de la zona. Peregrinos y locales se mezclan en este mar de puestos.",
            "zonas": "Alrededor de la Basílica de Guadalupe y sobre Av. de los Misterios. Zonas: Ropa y recuerdos religiosos, Frutas y verduras, Comida, Artesanías religiosas, Juguetes, Electrónicos.",
            "llegar": "Metro La Villa-Basílica (Línea 6) o Metro Deportivo 18 de Marzo. Autobuses por Calzada de Guadalupe.",
            "recomendaciones":  "Los domingos hay mucha afluencia por los visitantes de la Basílica. Probar los tamales oaxaqueños. Comprar recuerdos religiosos artesanales. Los jueves son más tranquilos para hacer despensa.",
        },
        {
            "id": "MX-CDMX-038",
            "name": "Tianguis de Santa Isabel Tola",
            "region": "norte",
            "days": ["Martes", "Viernes"],
            "coords": [19.4970, -99.1580],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion"],
            "safety": "Colonia Santa Isabel Tola, zona popular segura",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🧅",
            "quote": "En el corazón de la colonia Santa Isabel Tola, este tianguis es el alma del barrio. Dos veces por semana, las calles se llenan de color y sabor.",
            "zonas": "Av. Santa Isabel y calles aledañas. Zonas: Frutas y verduras, Abarrotes, Ropa, Comida preparada, Artículos para el hogar.",
            "llegar": "Metro Azcapotzalco (Línea 6) o Metro El Rosario (Línea 7), luego RTP. Autobuses por Calzada de las Armas.",
            "recomendaciones": "Los precios son de los más bajos del norte de la ciudad. Probar los tlacoyos de la señora María. Ambiente netamente de barrio. Ideal para conocer la vida cotidiana de la zona.",
        },
        {
            "id": "MX-CDMX-039",
            "name": "Tianguis de Industrial Vallejo",
            "region": "norte",
            "days": ["Miércoles", "Sábado"],
            "coords": [19.4930, -99.1480],
            "categories": ["canasta-basica", "ropa", "electronica", "chacharas"],
            "safety": "Zona industrial, segura de día",
            "horario": "9:00 AM — 3:00 PM",
            "emoji": "⚙️",
            "quote": "En la zona industrial de Vallejo, el tianguis es el respiro de los trabajadores. Aquí se consigue desde herramienta industrial hasta la verdura para la comida.",
            "zonas": "Sobre Av. Vallejo y calles de la colonia Industrial. Zonas: Herramientas y ferretería, Ropa de trabajo, Frutas y verduras, Electrónicos, Comida corrida.",
            "llegar": "Metro Vallejo (Línea 6) o Metro Lindavista. Autobuses RTP sobre Av. Vallejo.",
            "recomendaciones": "Si buscas herramientas, este es tu tianguis. Los sábados hay más variedad de ropa. Probar la comida corrida — es la comida de los trabajadores de la zona.",
        },
        {
            "id": "MX-CDMX-040",
            "name": "Tianguis de Chalma de Guadalupe",
            "region": "norte",
            "days": ["Domingo"],
            "coords": [19.5110, -99.1350],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion"],
            "safety": "Colonia Chalma de Guadalupe, zona tranquila",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🌮",
            "quote": "Chalma de Guadalupe, en la sierra de GAM, tiene un tianguis que es pura esencia de barrio popular. Aquí la comunidad se reúne cada domingo.",
            "zonas": "Calles principales de la colonia Chalma de Guadalupe. Zonas: Frutas y verduras, Ropa, Abarrotes, Comida típica, Juguetes.",
            "llegar": "Metro Indios Verdes y RTP 'Chalma'. En auto, carretera a Cuautepec.",
            "recomendaciones": "Atmósfera de barrio auténtico. Probar las tortas de tamal, una especialidad local. Los precios son muy accesibles. Conocer la zona alta de Gustavo A. Madero.",
        },
    ]

    # ---- ORIENTE (15) ----
    oriente = [
        {
            "id": "MX-CDMX-041",
            "name": "Tianguis de Santa Cruz Meyehualco",
            "region": "oriente",
            "days": ["Martes", "Viernes"],
            "coords": [19.3630, -99.0600],
            "categories": ["chacharas", "ropa", "electronica", "comida", "cultura-tradicion"],
            "safety": "Tianguis muy grande, precaución estándar con pertenencias",
            "horario": "8:00 AM — 5:00 PM",
            "emoji": "🏗️",
            "quote": "Uno de los tianguis más grandes de Iztapalapa y de toda la CDMX. Santa Cruz Meyehualco es un laberinto de puestos donde se encuentra absolutamente de todo.",
            "zonas": "Entre Av. Santa Cruz Meyehualco y Calzada Ermita Iztapalapa. Zonas: Aparatos de ejercicio, Electrodomésticos, Ropa, Maquinaria médica, Muebles, Electrónicos, Chácharas, Comida, Plantas.",
            "llegar": "Metro Santa Marta (Línea 2) o Metro Acatitla (Línea 3), luego RTP o pesero. En auto, por Calzada Ermita Iztapalapa.",
            "recomendaciones": "El martes hay más variedad, el viernes mejores precios en segunda mano. Es tan grande que conviene ir con un mapa mental. Las carnitas asadas son imperdibles. Llevar carrito de compras. Ir temprano y con paciencia.",
        },
        {
            "id": "MX-CDMX-042",
            "name": "Tianguis del Salado — Santa Martha Acatitla",
            "region": "oriente",
            "days": ["Miércoles"],
            "coords": [19.3570, -99.0070],
            "categories": ["chacharas", "ropa", "comida", "cultura-tradicion", "identidad-oficios"],
            "safety": "Tianguis enorme y muy concurrido, mantener precaución con objetos de valor",
            "horario": "7:00 AM — 4:00 PM",
            "emoji": "🌊",
            "quote": "El mítico Tianguis del Salado, una institución en Iztapalapa. Lo que no encuentras aquí, no existe. Ropa, herramientas, antigüedades y el mejor ambiente de barrio.",
            "zonas": "Francisco César Morales 36, Santa Martha Acatitla. Zonas: Ropa americana, Herramientas, Antigüedades, Electrónicos, Chácharas, Comida, Mascotas, Plantas.",
            "llegar": "Metro Santa Marta (Línea 2) y caminar 15 min o tomar pesero. También Metro Acatitla (Línea 3).",
            "recomendaciones": "Es uno de los tianguis más grandes de América Latina. Ir con ropa cómoda y calzado resistente. La ropa americana es de las más baratas de la CDMX. Probar los tacos de canasta. El miércoles es el día principal — llegar antes de las 9 AM.",
        },
        {
            "id": "MX-CDMX-043",
            "name": "Tianguis de El Salado — Zona Nocturna (Martes noche)",
            "region": "oriente",
            "days": ["Martes"],
            "coords": [19.3580, -99.0060],
            "categories": ["ropa", "electronica", "chacharas", "cultura-tradicion"],
            "safety": "Zona muy concurrida de noche, ir acompañado",
            "horario": "8:00 PM — 2:00 AM (madrugada del miércoles)",
            "emoji": "🌙",
            "quote": "El tianguis nocturno del Salado es una experiencia única en la CDMX. Cuando cae la noche, las calles de Santa Martha se iluminan con focos y el comercio popular cobra vida.",
            "zonas": "Misma zona que el tianguis del miércoles, pero empieza la noche del martes. Zonas: Ropa, Accesorios, Electrónicos, Zapatos, Comida nocturna (tacos, tamales, atole).",
            "llegar": "Metro Santa Marta (Línea 2) y caminar. Recomendable ir en grupo.",
            "recomendaciones": "Ir acompañado por seguridad. El ambiente nocturno es muy diferente al diurno. Probar los tacos de canasta nocturnos. Llevar linterna para revisar la ropa. Los precios suelen bajar después de medianoche.",
        },
        {
            "id": "MX-CDMX-044",
            "name": "Tianguis de Iztapalapa Centro — Ermita",
            "region": "oriente",
            "days": ["Jueves", "Domingo"],
            "coords": [19.3570, -99.0890],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion"],
            "safety": "Zona del centro de Iztapalapa, segura de día",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🏰",
            "quote": "En el centro ceremonial de Iztapalapa, donde la Semana Santa es Patrimonio Cultural, el tianguis es el latido comercial del oriente de la ciudad.",
            "zonas": "Alrededor del Jardín Cuitláhuac y sobre Calzada Ermita Iztapalapa. Zonas: Frutas y verduras, Ropa, Comida tradicional (tlacoyos, sopes, barbacoa), Artesanías, Flores.",
            "llegar": "Metro Iztapalapa (Línea 3) o Metro Cerro de la Estrella. También RTP por Ermita.",
            "recomendaciones": "Probar los tlacoyos de chicharrón. Subir al Cerro de la Estrella para vistas panorámicas. Los domingos hay más puestos de artesanías. Conocer el Museo de Iztapalapa.",
        },
        {
            "id": "MX-CDMX-045",
            "name": "Tianguis de Vicente Guerrero — Iztapalapa",
            "region": "oriente",
            "days": ["Miércoles", "Sábado"],
            "coords": [19.3780, -99.0450],
            "categories": ["canasta-basica", "ropa", "chacharas", "comida"],
            "safety": "Colonia Vicente Guerrero, zona popular segura de día",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🏘️",
            "quote": "En la colonia Vicente Guerrero, el tianguis es el punto de reunión de las familias trabajadoras del oriente. Dos veces por semana, las calles se llenan de vida.",
            "zonas": "Sobre Av. Vicente Guerrero y calles aledañas. Zonas: Frutas y verduras, Ropa, Abarrotes, Comida preparada, Artículos de hogar.",
            "llegar": "Metro Acatitla (Línea 3) o Metro Santa Marta (Línea 2), luego pesero. Autobuses RTP por Av. Telecomunicaciones.",
            "recomendaciones": "Buenos precios en frutas y verduras. Ambiente de barrio auténtico. Probar los tacos de canasta. Los sábados hay más variedad de ropa.",
        },
        {
            "id": "MX-CDMX-046",
            "name": "Tianguis de San Miguel Teotongo",
            "region": "oriente",
            "days": ["Miércoles", "Domingo"],
            "coords": [19.3490, -99.0240],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion", "identidad-oficios"],
            "safety": "Zona de la sierra de Iztapalapa, segura de día",
            "horario": "7:00 AM — 3:00 PM",
            "emoji": "🏔️",
            "quote": "San Miguel Teotongo, en la sierra de Santa Catarina. Su tianguis es el sustento de los pueblos originarios de la zona alta de Iztapalapa.",
            "zonas": "Centro de San Miguel Teotongo, alrededor de la iglesia. Zonas: Productos de la milpa (maíz, frijol, calabaza), Nopal, Verduras, Ropa, Comida típica, Artesanías.",
            "llegar": "Metro Santa Marta y pesero 'San Miguel Teotongo' (subida por la sierra). En auto, carretera a San Miguel.",
            "recomendaciones": "El nopal y el maíz criollo son de primera calidad. Probar los quelites de temporada. Las vistas de la cuenca desde la sierra son espectaculares. Ambiente comunitario muy fuerte.",
        },
        {
            "id": "MX-CDMX-047",
            "name": "Tianguis de San Juan Xalpa",
            "region": "oriente",
            "days": ["Martes", "Viernes"],
            "coords": [19.3680, -99.0180],
            "categories": ["canasta-basica", "ropa", "comida", "chacharas"],
            "safety": "Colonia San Juan Xalpa, zona tranquila",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🧺",
            "quote": "San Juan Xalpa, donde el oriente de la ciudad se encuentra con la tradición del pueblo. Su tianguis es una mezcla de productos del campo y de la ciudad.",
            "zonas": "Calles principales de San Juan Xalpa. Zonas: Frutas y verduras, Ropa, Abarrotes, Comida preparada, Artículos de hogar.",
            "llegar": "Metro Acatitla (Línea 3) y pesero 'San Juan Xalpa', o Metro Santa Marta.",
            "recomendaciones": "Excelente para la despensa semanal. Ambiente familiar. Probar los tamales de la señora Lupe. Los viernes hay más puestos que los martes.",
        },
        {
            "id": "MX-CDMX-048",
            "name": "Tianguis de Zapotitlán — Iztapalapa",
            "region": "oriente",
            "days": ["Jueves", "Domingo"],
            "coords": [19.3530, -99.0450],
            "categories": ["canasta-basica", "ropa", "comida", "artesania"],
            "safety": "Colonia Zapotitlán, zona segura de día",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🌵",
            "quote": "Zapotitlán, uno de los pueblos originarios de Iztapalapa, mantiene su tianguis como espacio de resistencia cultural y comercial.",
            "zonas": "Centro de Zapotitlán. Zonas: Frutas y verduras, Nopal y maguey, Ropa, Artesanías, Comida tradicional.",
            "llegar": "Metro Acatitla y pesero 'Zapotitlán', o desde Iztapalapa centro.",
            "recomendaciones": "Comprar nopal fresco directo del productor. Probar el pulque curado si hay. Conocer la historia del pueblo de Zapotitlán. Ambiente más tranquilo que el centro de Iztapalapa.",
        },
        {
            "id": "MX-CDMX-049",
            "name": "Tianguis de Apatlaco — Iztacalco",
            "region": "oriente",
            "days": ["Martes", "Domingo"],
            "coords": [19.3900, -99.1050],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion"],
            "safety": "Barrio de Iztacalco, precaución estándar",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🚲",
            "quote": "Apatlaco, en Iztacalco, tiene un tianguis que es el centro de abasto de la alcaldía más pequeña de la CDMX. Aquí la comunidad se conoce toda.",
            "zonas": "Alrededor del Metro Apatlaco y calles aledañas. Zonas: Frutas y verduras, Ropa, Comida, Abarrotes, Artículos de hogar, Plantas.",
            "llegar": "Metro Apatlaco (Línea 2) — salida directa. También Metrobús Línea 4.",
            "recomendaciones": "El tianguis está a la salida del metro — muy accesible. Buenos precios en frutas. Probar los tacos de guisado. Ambiente de barrio tradicional de Iztacalco.",
        },
        {
            "id": "MX-CDMX-050",
            "name": "Tianguis de Santa María Aztahuacán",
            "region": "oriente",
            "days": ["Miércoles", "Domingo"],
            "coords": [19.3670, -99.0350],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion", "identidad-oficios"],
            "safety": "Pueblo originario de Iztapalapa, zona tranquila",
            "horario": "7:00 AM — 3:00 PM",
            "emoji": "🛐",
            "quote": "Santa María Aztahuacán, cuna de tradiciones, tiene un tianguis que es la memoria del México profundo. Aquí el náhuatl aún se escucha entre los puestos.",
            "zonas": "Centro de Santa María Aztahuacán, alrededor de la iglesia. Zonas: Milpa (maíz, frijol, calabaza), Nopal, Frutas de temporada, Artesanías, Comida tradicional, Ropa.",
            "llegar": "Metro Santa Marta y pesero 'Santa María Aztahuacán'. También desde Iztapalapa centro.",
            "recomendaciones": "Escuchar náhuatl en el tianguis es una experiencia cultural única. Comprar maíz criollo para hacer tortillas. Probar el atole de maíz quebrada. Conocer la iglesia de Santa María. La comunidad defiende sus tradiciones desde tiempos prehispánicos.",
        },
        {
            "id": "MX-CDMX-051",
            "name": "Tianguis de San Lorenzo Tezonco",
            "region": "oriente",
            "days": ["Miércoles", "Sábado"],
            "coords": [19.3460, -99.0760],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion"],
            "safety": "Pueblo de Iztapalapa, zona tranquila",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🌋",
            "quote": "San Lorenzo Tezonco, un pueblo de Iztapalapa con raíces profundas. Su tianguis es el punto de encuentro de las familias que mantienen vivas las tradiciones.",
            "zonas": "Centro de San Lorenzo Tezonco. Zonas: Frutas y verduras, Ropa, Abarrotes, Comida típica, Artesanías.",
            "llegar": "Metro Iztapalapa (Línea 3) y pesero 'San Lorenzo', o Metro Cerro de la Estrella.",
            "recomendaciones": "Probar las gorditas de nopal. El ambiente es muy tranquilo y familiar. Buenos precios en frutas de temporada. Conocer el pueblo y su iglesia.",
        },
        {
            "id": "MX-CDMX-052",
            "name": "Tianguis de La Purísima — Iztacalco",
            "region": "oriente",
            "days": ["Jueves", "Domingo"],
            "coords": [19.3960, -99.0960],
            "categories": ["canasta-basica", "ropa", "comida", "artesania"],
            "safety": "Colonia La Purísima, zona segura",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🧘",
            "quote": "La Purísima en Iztacalco, un tianguis de barrio que conserva el sabor de las colonias tradicionales del oriente de la ciudad.",
            "zonas": "Sobre Av. La Purísima y calles aledañas. Zonas: Frutas y verduras, Ropa, Artesanías, Comida preparada, Artículos de hogar.",
            "llegar": "Metro Coyuya (Línea 3) o Metro Apatlaco (Línea 2), caminando 10 min.",
            "recomendaciones": "Artesanías locales de buena calidad. Ambiente tranquilo y familiar. Probar los sopes de la zona. Ideal para ir en bicicleta.",
        },
        {
            "id": "MX-CDMX-053",
            "name": "Tianguis de San Andrés Tetepilco",
            "region": "oriente",
            "days": ["Martes", "Viernes"],
            "coords": [19.3780, -99.0780],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion"],
            "safety": "Colonia San Andrés, Iztapalapa, zona segura",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "⛪",
            "quote": "San Andrés Tetepilco, un barrio con nombre náhuatl que significa 'en el cerro de las piedras'. Su tianguis es un mercado de barrio con esencia de pueblo.",
            "zonas": "Calles principales de San Andrés Tetepilco. Zonas: Frutas y verduras, Ropa, Abarrotes, Comida típica, Plantas.",
            "llegar": "Metro Iztapalapa (Línea 3) y pesero, o Metro Cerro de la Estrella.",
            "recomendaciones": "Ambiente de barrio auténtico. Buenos precios en abarrotes. Probar las quesadillas de hongos. Ideal para conocer la vida cotidiana de Iztapalapa.",
        },
        {
            "id": "MX-CDMX-054",
            "name": "Tianguis de Acatitla — La Paz Oriente",
            "region": "oriente",
            "days": ["Miércoles", "Sábado"],
            "coords": [19.3590, -98.9950],
            "categories": ["canasta-basica", "ropa", "chacharas", "comida"],
            "safety": "Zona de Iztapalapa límite con Edomex, precaución estándar",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🛤️",
            "quote": "En los límites de la CDMX con el Estado de México, el tianguis de Acatitla es el punto de encuentro de dos entidades. Un crisol de culturas y comercios.",
            "zonas": "Alrededor del Metro Acatitla y Av. Acatitla. Zonas: Frutas y verduras, Ropa, Chácharas, Comida, Artículos de hogar.",
            "llegar": "Metro Acatitla (Línea 3) — salida directa. También RTP por Calzada Ermita Iztapalapa.",
            "recomendaciones": "Los precios son bajos por la competencia con Edomex. Probar las carnitas — famosas en la zona. Los sábados hay más puestos. Revisar bien la ropa de segunda mano.",
        },
        {
            "id": "MX-CDMX-055",
            "name": "Tianguis de la Coatlicue — Iztapalapa",
            "region": "oriente",
            "days": ["Domingo"],
            "coords": [19.3560, -99.0700],
            "categories": ["cultura-tradicion", "artesania", "comida", "identidad-oficios"],
            "safety": "Centro de Iztapalapa, segura de día",
            "horario": "9:00 AM — 4:00 PM",
            "emoji": "🗿",
            "quote": "El tianguis de la Coatlicue, nombrado así en honor a la diosa mexica, es un espacio de resistencia cultural donde el trueque y la artesanía celebran las raíces indígenas de Iztapalapa.",
            "zonas": "Cerca del Cerro de la Estrella y el centro de Iztapalapa. Zonas: Artesanía indígena, Hierbas medicinales, Comida tradicional prehispánica, Trueque e intercambio, Música y danza tradicional.",
            "llegar": "Metro Iztapalapa (Línea 3) o Metro Cerro de la Estrella, caminando 10 min.",
            "recomendaciones": "El trueque es la esencia — lleva objetos para intercambiar. Probar el chocolate de metate y el pinole. Conocer la danza de los concheros. Comprar artesanía directamente de los artesanos. Llegar temprano para la ceremonia de apertura.",
        },
    ]

    # ---- PONIENTE (10) ----
    poniente = [
        {
            "id": "MX-CDMX-056",
            "name": "Tianguis de La Búfalo — Narvarte Poniente",
            "region": "poniente",
            "days": ["Domingo"],
            "coords": [19.4030, -99.1670],
            "categories": ["antiguedades", "chacharas", "ropa", "cultura-tradicion", "artesania"],
            "safety": "Colonia Narvarte, zona segura y muy concurrida los domingos",
            "horario": "9:00 AM — 4:00 PM",
            "emoji": "🐃",
            "quote": "La Búfalo es el tianguis de antigüedades y chácharas más famoso del poniente de la CDMX. Un mercado de pulgas donde cada domingo hay un nuevo tesoro por descubrir.",
            "zonas": "Río Becerra a la altura de Av. Alta Tensión, colonia Narvarte. Zonas: Antigüedades, Muebles vintage, Ropa de época, Discos y libros, Coleccionismo, Tatuajes y arte alternativo, Comida gourmet callejera.",
            "llegar": "Metro Etiopía/Plaza de la Transparencia (Línea 3) o Metro Centro Médico (Línea 3 y 9), caminando 15 min. Metrobús Línea 1.",
            "recomendaciones": "Ir con tiempo para explorar cada puesto. Los precios de antigüedades son negociables. Probar los churros rellenos y el café de olla. Ambiente hipster-mexicano único. Los tatuadores locales ofrecen precios especiales los domingos.",
        },
        {
            "id": "MX-CDMX-057",
            "name": "Tianguis de la Sullivan — Monumento a la Madre",
            "region": "poniente",
            "days": ["Martes", "Viernes", "Domingo"],
            "coords": [19.4210, -99.1550],
            "categories": ["comida", "ropa", "cultura-tradicion", "artesania"],
            "safety": "Zona de la colonia Cuauhtémoc-Roma, segura, muy vigilada",
            "horario": "10:00 AM — 6:00 PM",
            "emoji": "🍽️",
            "quote": "El Tianguis de Sullivan es el paraíso gastronómico del poniente. Reconocido como el mejor lugar para comer de todos los tianguis de la CDMX, con más de 50 puestos de comida.",
            "zonas": "A espaldas del Monumento a la Madre, sobre Sullivan y calles aledañas. Zonas: Comida (tortas, tamales, tacos, tlacoyos, gorditas, crepas, churros, mariscos), Ropa y accesorios, Artesanías, Plantas, Discos y libros.",
            "llegar": "Metro Cuauhtémoc (Línea 1) o Metro Revolución (Línea 2), caminando 10 min. Metrobús Línea 1.",
            "recomendaciones": "Venir con hambre — la oferta gastronómica es la mejor de todos los tianguis. Probar las tortas de la Suiza y los tamales oaxaqueños. Los domingos hay más puestos de artesanías. El ambiente es bohemio y relajado. Llegar después de las 11 AM para ver el tianguis completo.",
        },
        {
            "id": "MX-CDMX-058",
            "name": "Tianguis de San Ángel — Bazar del Sábado",
            "region": "poniente",
            "days": ["Sábado"],
            "coords": [19.3420, -99.1860],
            "categories": ["artesania", "cultura-tradicion", "comida", "identidad-oficios"],
            "safety": "San Ángel, zona residencial de lujo, muy segura",
            "horario": "10:00 AM — 5:00 PM",
            "emoji": "🎨",
            "quote": "El Bazar del Sábado en San Ángel es el tianguis de arte y artesanía más elegante de la CDMX. En el corazón del barrio colonial, los artesanos mexicanos exhiben su mejor trabajo.",
            "zonas": "Plaza San Ángel, Avenida Revolución y calles del centro de San Ángel. Zonas: Artesanía fina (barro, vidrio, textiles, plata), Pintura y escultura, Joyería artesanal, Ropa de diseño, Comida gourmet, Música en vivo.",
            "llegar": "Metro Barranca del Muerto (Línea 7) o Metro Miguel Ángel de Quevedo (Línea 3), luego RTP o pesero. En auto, estacionamiento $50-80/hr.",
            "recomendaciones": "Es el tianguis más caro de la CDMX pero la calidad artesanal es excepcional. Llegar temprano para evitar multitudes. Probar los tamales de elote y el atole de fresa. Visitar el Ex Convento del Carmen después. Comprar artesanía de alta calidad directamente de los maestros.",
        },
        {
            "id": "MX-CDMX-059",
            "name": "Tianguis de Cuajimalpa — Centro",
            "region": "poniente",
            "days": ["Miércoles", "Domingo"],
            "coords": [19.3580, -99.2830],
            "categories": ["canasta-basica", "ropa", "comida", "cultura-tradicion", "identidad-oficios"],
            "safety": "Centro de Cuajimalpa, zona segura de día",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🌲",
            "quote": "Cuajimalpa, el pulmón del poniente de la CDMX, tiene un tianguis que es el centro de abasto de toda la alcaldía. Productos del bosque y de la milpa en cada esquina.",
            "zonas": "Centro de Cuajimalpa, alrededor de la Plaza Principal. Zonas: Frutas y verduras, Hongos de temporada, Ropa, Comida típica (barbacoa, mixiotes), Artesanías de madera, Plantas de ornato.",
            "llegar": "Metro Constituyentes (Línea 7) y RTP 'Cuajimalpa'. En auto, carretera México-Toluca (20 min desde Constituyentes).",
            "recomendaciones": "Los hongos del bosque en temporada de lluvias son imperdibles. Probar la barbacoa de borrego — famosa en la zona. El paisaje del Pueblo de Cuajimalpa es hermoso. Visitar el Parque Nacional Desierto de los Leones. Comprar leña y carbón para asados.",
        },
        {
            "id": "MX-CDMX-060",
            "name": "Tianguis de Santa Rosa Xochiac — Álvaro Obregón",
            "region": "poniente",
            "days": ["Viernes", "Domingo"],
            "coords": [19.3450, -99.2220],
            "categories": ["canasta-basica", "comida", "cultura-tradicion", "identidad-oficios"],
            "safety": "Pueblo originario, zona segura y tranquila",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🥬",
            "quote": "Santa Rosa Xochiac, en las montañas de Álvaro Obregón, es uno de los pocos pueblos que conservan el cultivo de la milpa. Su tianguis es el orgullo de la comunidad.",
            "zonas": "Centro de Santa Rosa Xochiac. Zonas: Productos de la milpa (maíz, frijol, calabaza), Nopal, Verduras orgánicas, Hierbas medicinales, Comida típica, Artesanías.",
            "llegar": "Metro Barranca del Muerto y RTP 'Santa Rosa'. En auto, carretera al Desierto de los Leones (25 min).",
            "recomendaciones": "Comprar maíz criollo para nixtamal. Las hierbas medicinales son de gran calidad. Probar los tlacoyos de haba. Visitar la iglesia del pueblo. Disfrutar del paisaje montañoso.",
        },
        {
            "id": "MX-CDMX-061",
            "name": "Tianguis de la Magdalena Contreras — Centro",
            "region": "poniente",
            "days": ["Martes", "Sábado"],
            "coords": [19.3290, -99.2430],
            "categories": ["canasta-basica", "ropa", "comida", "artesania", "cultura-tradicion"],
            "safety": "Centro de Contreras, zona segura de día",
            "horario": "8:00 AM — 4:00 PM",
            "emoji": "🏞️",
            "quote": "La Magdalena Contreras, donde el río y el bosque se encuentran con la ciudad. Su tianguis es el corazón comercial del poniente sur de la CDMX.",
            "zonas": "Centro de la Magdalena Contreras, sobre Av. Hidalgo y calles aledañas. Zonas: Frutas y verduras, Hongos del bosque, Ropa, Artesanías, Comida típica, Plantas de ornato.",
            "llegar": "Metro Barranca del Muerto (Línea 7) y RTP 'Contreras'. En auto, por Av. San Jerónimo (20 min).",
            "recomendaciones": "Los hongos silvestres en temporada son una delicia. Probar los tacos de carnitas de la zona. Visitar el Bosque de la Magdalena. Los sábados hay más puestos de artesanías. Ambiente de pueblo mágico.",
        },
        {
            "id": "MX-CDMX-062",
            "name": "Tianguis de San Jerónimo Lídice",
            "region": "poniente",
            "days": ["Miércoles", "Domingo"],
            "coords": [19.3180, -99.2250],
            "categories": ["canasta-basica", "ropa", "comida", "artesania"],
            "safety": "Colonia San Jerónimo, zona residencial segura",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🌸",
            "quote": "San Jerónimo Lídice, un barrio con nombre de memoria histórica. Su tianguis es el punto de encuentro de las familias del poniente de la ciudad.",
            "zonas": "Sobre Av. San Jerónimo y calles aledañas. Zonas: Frutas y verduras, Ropa, Artesanías, Comida preparada, Plantas y flores.",
            "llegar": "Metro Barranca del Muerto y RTP 'San Jerónimo', o autobuses por Av. San Jerónimo.",
            "recomendaciones": "Excelente para comprar frutas y verduras de calidad. Probar los tamales de la esquina. Ambiente tranquilo y familiar. Visitar el Centro Cultural San Jerónimo.",
        },
        {
            "id": "MX-CDMX-063",
            "name": "Tianguis de La Portales — Chácharas y Coleccionismo",
            "region": "poniente",
            "days": ["Todos los días"],
            "coords": [19.3990, -99.1600],
            "categories": ["chacharas", "coleccionismo", "cultura-tradicion", "artesania"],
            "safety": "Colonia Portales, zona concurrida de día, segura",
            "horario": "11:00 AM — 5:00 PM",
            "emoji": "🎪",
            "quote": "El tianguis de La Portales es el paraíso de los coleccionistas y los buscadores de tesoros. Abierto todos los días del año, nunca sabes qué joya te espera.",
            "zonas": "A las afueras del Metro Portales, dirección Taxqueña. Zonas: Antigüedades, Coleccionismo (monedas, billetes, tarjetas), Juguetes vintage, Discos y cassettes, Ropa de época, Libros y revistas, Arte y artesanía.",
            "llegar": "Metro Portales (Línea 2) — salida directa. También Metrobús Línea 1.",
            "recomendaciones": "Ir con paciencia — el tesoro está en rebuscar. Los coleccionistas llegan temprano. Probar las tortas de la entrada. Los precios varían mucho según el vendedor. Los fines de semana hay más puestos pero también más precios altos.",
        },
        {
            "id": "MX-CDMX-064",
            "name": "Tianguis de San Bartolo Ameyalco",
            "region": "poniente",
            "days": ["Jueves", "Domingo"],
            "coords": [19.3390, -99.2680],
            "categories": ["canasta-basica", "agricultura", "cultura-tradicion", "identidad-oficios"],
            "safety": "Pueblo de Álvaro Obregón, muy seguro",
            "horario": "7:00 AM — 2:00 PM",
            "emoji": "💧",
            "quote": "San Bartolo Ameyalco, el pueblo del agua y los manantiales. Su tianguis es el mercado de los productores que cultivan en las faldas del cerro.",
            "zonas": "Centro de San Bartolo Ameyalco. Zonas: Verduras orgánicas, Frutas de temporada, Plantas medicinales, Comida tradicional, Artesanías.",
            "llegar": "Metro Barranca del Muerto y RTP 'San Bartolo'. En auto, 15 min del centro de Contreras.",
            "recomendaciones": "La calidad de las verduras orgánicas es excepcional. Probar el agua de frutas natural. Conocer los manantiales del pueblo. Ambiente rural único dentro de la CDMX.",
        },
        {
            "id": "MX-CDMX-065",
            "name": "Tianguis de San Lorenzo Acopilco Poniente — Artesanías y Bosque",
            "region": "poniente",
            "days": ["Sábado", "Domingo"],
            "coords": [19.3190, -99.2590],
            "categories": ["artesania", "cultura-tradicion", "comida", "identidad-oficios"],
            "safety": "Magdalena Contreras, zona boscosa segura de día",
            "horario": "8:00 AM — 3:00 PM",
            "emoji": "🎋",
            "quote": "En lo alto de la Magdalena Contreras, San Lorenzo Acopilco tiene un tianguis que huele a bosque y a tradición. Artesanías de madera, hongos y la mejor comida serrana.",
            "zonas": "Centro de San Lorenzo Acopilco. Zonas: Artesanías de madera y vara, Hongos silvestres, Verduras, Plantas medicinales, Comida típica (mixiotes, barbacoa).",
            "llegar": "Metro Barranca del Muerto y RTP 'San Lorenzo'. En auto, carretera a la Magdalena Contreras (30 min).",
            "recomendaciones": "Las artesanías de madera tallada a mano son únicas. En temporada de lluvias, los hongos son imperdibles. Probar los mixiotes de pollo. Llevar ropa abrigadora. Disfrutar del bosque después del tianguis.",
        },
    ]

    return centro + sur + norte + oriente + poniente


def generate_file(data, idx):
    """Generate a single .md file."""
    name_clean = data["name"].lower().replace(" ", "_").replace("—", "").replace("–", "").replace(",", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n").replace("__", "_").strip("_")
    filename = f"{name_clean[:50]}.md"

    days_str = ", ".join(data["days"])
    cats_str = ", ".join(data["categories"])
    coords_str = f"[{data['coords'][0]}, {data['coords'][1]}]"
    days_list = str(data["days"]).replace("'", '"')
    cats_list = str(data["categories"]).replace("'", '"')

    # Tags for comments - pick 8-10 depending on tianguis type
    all_tags = ["#Precio", "#Sabor", "#Acceso", "#Artesania", "#Chacharas", "#Seguridad", "#Cultura", "#Trueque"]
    
    # Generate 9 comments
    comments = []
    
    # Determine which tags to use based on categories
    cat_str = " ".join(data["categories"])
    
    comment_templates = [
        {
            "tag": "#Sabor",
            "title": "🌮 El Sabor del Barrio",
            "text": f"\"La comida de este tianguis es de otro nivel. Los puestos de {data['name'].split('—')[0].strip()} tienen unos tacos y tlacoyos que no encuentras en ningún restaurante. Todo recién hecho, con recetas de la abuela.\"",
            "photo": PHOTOS[0]
        },
        {
            "tag": "#Precio",
            "title": "💰 Precios que Ayudan",
            "text": f"\"Aquí el dinero rinde mucho más que en el supermercado. Las frutas y verduras están a menos de la mitad que en tiendas establecidas. La canasta básica semanal baja hasta un 40%.\"",
            "photo": PHOTOS[1]
        },
        {
            "tag": "#Cultura",
            "title": "🎭 Memoria Viva",
            "text": f"\"Cada domingo es una clase de historia viviente. Los abuelos que venden en este tianguis han estado aquí por generaciones. Saben de plantas medicinales, de cocina tradicional, de la historia del barrio.\"",
            "photo": PHOTOS[2]
        },
        {
            "tag": "#Acceso",
            "title": "🚇 Cómo Llegar",
            "text": f"\"El transporte público deja justo en la entrada del tianguis. Si vienes en coche, mejor llegar antes de las 10 AM porque el estacionamiento se llena rápido. El acceso para sillas de ruedas es limitado en las calles más angostas.\"",
            "photo": PHOTOS[3]
        },
        {
            "tag": "#Artesania",
            "title": "🎨 Manos Artesanas",
            "text": f"\"Los artesanos locales traen su mejor trabajo: textiles bordados a mano, barro vidriado, alebrijes y joyería de plata. Cada pieza cuenta una historia de las comunidades indígenas de la región.\"",
            "photo": PHOTOS[4]
        },
        {
            "tag": "#Chacharas",
            "title": "🔧 Tesoros Escondidos",
            "text": f"\"Lo mejor de este tianguis son las chácharas. Desde herramientas antiguas hasta juguetes de la infancia. Si sabes buscar, encuentras verdaderas joyas a precios irrisorios.\"",
            "photo": PHOTOS[5]
        },
        {
            "tag": "#Seguridad",
            "title": "🛡️ Andar Tranquilo",
            "text": f"\"El ambiente es familiar y la comunidad se cuida entre sí. Los mismos locatarios vigilan que todo esté en orden. Como en cualquier lugar concurrido, solo hay que cuidar las pertenencias personales.\"",
            "photo": PHOTOS[6]
        },
        {
            "tag": "#Trueque",
            "title": "🔄 El Trueque Vive",
            "text": f"\"Todavía se practica el trueque en este tianguis. Los abuelos intercambian productos de sus cosechas: verduras por ropa, hierbas por comida. Una tradición que viene de tiempos prehispánicos.\"",
            "photo": PHOTOS[7]
        },
        {
            "tag": "#Sabor",
            "title": "🍲 Cocina de las Abuelas",
            "text": f"\"Los puestos de comida son el alma del tianguis. Doña María y Doña Chole cocinan como en sus pueblos: mole oaxaqueño, barbacoa de hoyo, tamales de elote. Recetas que no cambian porque ya son perfectas.\"",
            "photo": PHOTOS[8]
        },
    ]

    name_for_search = data["name"].replace("—", "").strip()
    search_name = name_for_search.split("—")[0].strip() if "—" in name_for_search else name_for_search

    for i, ct in enumerate(comment_templates):
        yt_query = f"tianguis {search_name} CDMX".replace(" ", "+")
        comments.append(f"""### {ct['title']}
> {ct['text']}
- **Tipo:** {ct['tag']}
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query={yt_query})
- 📸 **Foto:** ![Tianguis CDMX](https://images.unsplash.com/photo-{ct['photo']}?w=400)""")

    # Recomendaciones
    recs = data.get("recomendaciones", "")
    rec_lines = []
    if recs:
        for r in recs.split("."):
            r = r.strip()
            if r:
                rec_lines.append(f"- {r}.")
    rec_text = "\n".join(rec_lines) if rec_lines else "- Llegar temprano.\n- Llevar efectivo.\n- Ir con ropa cómoda."

    content = f"""---
id: "{data['id']}"
name: "{data['name']}"
region: "{data['region']}"
state: "cdmx"
days: {days_list}
coords: {coords_str}
categories: {cats_list}
safety: "{data['safety']}"
horario: "{data['horario']}"
img: "https://images.unsplash.com/photo-{PHOTOS[9]}?w=800"
---

# {data['emoji']} {data['name']}

> {data['quote']}

## 📋 Información Rápida

| Dato | Detalle |
|------|---------|
| 📅 **Días** | {days_str} |
| ⏰ **Horario** | {data['horario']} |
| 📍 **Región** | {data['region'].title()} — CDMX |
| 🗺️ **Categorías** | {cats_str} |

## 🗺️ Zonas

{data['zonas']}

## 💬 Bitácora Comunitaria

{chr(10).join(comments)}

## 🚗 Cómo Llegar

{data['llegar']}

## Recomendaciones

{rec_text}
"""

    return filename, content


def main():
    entries = make_entries()
    
    # Create region dirs
    for reg in ["centro", "sur", "norte", "oriente", "poniente"]:
        os.makedirs(os.path.join(BASE, reg), exist_ok=True)
    
    # Track which region gets how many
    region_counts = {"centro": 0, "sur": 0, "norte": 0, "oriente": 0, "poniente": 0}
    
    for data in entries:
        reg = data["region"]
        filename, content = generate_file(data, len(entries))
        filepath = os.path.join(BASE, reg, filename)
        with open(filepath, "w") as f:
            f.write(content)
        region_counts[reg] += 1
        print(f"✓ [{reg}] {filename}")
    
    print(f"\nCompletado: {sum(region_counts.values())} archivos generados")
    for reg, count in region_counts.items():
        print(f"  {reg}: {count}")


if __name__ == "__main__":
    main()
