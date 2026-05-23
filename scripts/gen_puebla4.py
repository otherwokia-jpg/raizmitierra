#!/usr/bin/env python3
"""Generate Puebla files 22-38: Valle Serdán (rest) + Mixteca"""

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

# ============ VALLE SERDÁN (22-26) ============

write("valle_serdan", 22, "Tianguis del Trueque de San Pedro Cholula", ["Sábado (Sep 1er fin de semana)"],
    [19.0642, -98.3039],
    ["cultura-tradicion", "trueque", "artesania", "identidad-oficios", "garnachas-sabor"],
    "Evento cultural supervisado, muy seguro, hay presencia de autoridades y organizadores",
    "6:00 AM — 2:00 PM",
    "🔄",
    "El Trueque de Cholula es una tradición milenaria que sobrevive desde la época prehispánica. Una vez al año, el dinero pierde su valor y solo el intercambio directo de productos tiene cabida.",
    """Se realiza en la Plaza de la Concordia de San Pedro Cholula:

- **Zona de Intercambio de Alimentos**: Intercambian maíz, frijol, chile por otros productos.
- **Zona de Artesanías**: Cerámica, textiles, barro se intercambian por alimentos.
- **Zona de Plantas Medicinales**: Hierbas curativas se cambian por otros productos.
- **Zona de Ropa y Textiles**: Prendas tejidas a mano se intercambian.
- **Zona de Animales**: Aves de corral y animales pequeños participan en el trueque.""",
    """### 🔄 El Dinero No Vale
> "El trueque de Cholula es la tradición más hermosa. Por un día, el dinero no sirve. Solo cuentan los productos que traes para intercambiar. Es volver a las raíces prehispánicas del comercio."
- **Tipo:** #Trueque
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=trueque+Cholula+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)
### 🎭 Patrimonio Cultural
> "Esta tradición se mantiene intacta desde hace siglos. Las comunidades de los alrededores traen sus productos para intercambiarlos. Es una ventana al pasado prehispánico de México."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+trueque+Cholula)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🌮 Compartir Sabores
> "Llevo tamales y atole para intercambiar por frutas y verduras. Es una experiencia increíble negociar sin dinero, solo con lo que cada quien ha cultivado o preparado."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=trueque+Cholula+comida)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Economía Alternativa
> "No hay precios, no hay etiquetas. Todo se basa en el valor que cada quien le da a sus productos. Una lección de economía comunitaria y solidaridad."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=trueque+Cholula+tradicion)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1557803178-6ba46a0cda3d?w=400)
### 🛡️ Evento Seguro
> "Es un evento muy organizado, con vigilancia y logística del municipio. La gente participa con respeto y alegría. Ideal para ir con niños."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=trueque+Cholula+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)
### 🚇 Cómo Participar
> "Llega temprano (antes de las 7 AM) con productos para intercambiar. No sirve el dinero. Trae lo que hayas cultivado, preparado o hecho. La experiencia es única."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+participar+trueque+Cholula)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)""",
    "Se realiza en la Plaza de la Concordia de San Pedro Cholula. Desde Puebla: Autobuses Azteca (20 min). Se celebra el primer sábado de septiembre durante la Feria Milenaria de Cholula.",
    ["Llegar con productos para intercambiar: alimentos, artesanías, plantas.",
     "No llevar dinero — el trueque es solo intercambio de productos.",
     "Llegar muy temprano (6 AM) para participar activamente.",
     "Traer frutas, verduras, tamales, pan o artesanías para intercambiar.",
     "Disfrutar la experiencia única de comercio sin dinero."])

write("valle_serdan", 23, "Tianguis de Las Vías, Cholula", ["Domingo"],
    [19.0620, -98.3080],
    ["garnachas-sabor", "la-paca", "chacharas-antiguedades", "canasta-basica"],
    "Zona concurrida los domingos, ambiente familiar con seguridad municipal",
    "8:00 AM — 4:00 PM",
    "🚂",
    "El Tianguis de Las Vías de Cholula se instala junto a las antiguas vías del tren en San Pedro Cholula. Es el domingo de compras para las familias cholultecas.",
    """Se instala a lo largo de la calle Lázaro Cárdenas, junto a las vías del tren:

- **Zona de Ropa y Accesorios**: Ropa nueva, ropa de paca, calzado, bolsas, bisutería.
- **Zona de Comida**: Garnachas, tlacoyos, tacos, cemitas, aguas frescas.
- **Zona de Chácharas**: Juguetes, herramientas, artículos del hogar.
- **Zona de Frutas y Verduras**: Productos frescos de la región.
- **Zona de Plantas**: Flores y plantas ornamentales.""",
    """### 🌮 Garnachas Cholutecas
> "El tianguis de Las Vías tiene la mejor comida de Cholula los domingos. Los tlacoyos de masa azul con nopales y salsa verde son mi perdición. Llego solo por ellos."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+las+vias+Cholula)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 👕 Ropa para Todos
> "Aquí encuentras ropa para toda la familia a buen precio. Los domingos es el paseo familiar. Los niños juegan mientras los papás compran."
- **Tipo:** #LaPaca
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=ropa+las+vias+Cholula)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)
### 💰 Precios Cholultecas
> "Los precios son para el presupuesto familiar. Verduras, frutas y abarrotes a buen precio. Las garnachas son económicas y deliciosas."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Las+vias+Cholula+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🚇 Acceso Fácil
> "Está en San Pedro Cholula, a 10 minutos de la Pirámide. Se llega fácil desde Puebla en autobús. El domingo es el día ideal para visitar Cholula."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+las+vias+Cholula)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)""",
    "Desde Puebla: Autobuses Azteca o Estrella Roja (20 min). En coche: Vía Atlixcáyotl hasta San Pedro Cholula. El tianguis está sobre Calle Lázaro Cárdenas.",
    ["Llegar temprano para evitar el calor y las multitudes.",
     "Probar los tlacoyos de masa azul con salsa verde.",
     "Visitar la Pirámide de Cholula después del tianguis.",
     "Comprar flores frescas — Cholula tiene excelentes flores.",
     "Llevar efectivo."])

write("valle_serdan", 24, "Tianguis CAPU, Puebla", ["Jueves"],
    [19.0580, -98.2150],
    ["canasta-basica", "garnachas-sabor", "plaza-campo", "chacharas-antiguedades"],
    "Zona de la central de autobuses, concurrida, precauciones normales en transporte público",
    "9:00 AM — 7:00 PM",
    "🚌",
    "El Tianguis de la CAPU se instala cerca de la Central de Autobuses de Puebla. Es el punto de encuentro de viajeros y locales que buscan productos variados a buen precio.",
    """Se instala en las calles cercanas a la CAPU:

- **Zona de Frutas y Verduras**: Productos frescos para el viajero y locales.
- **Zona de Comida**: Anafres, tacos, tortas, cemitas, aguas frescas.
- **Zona de Ropa**: Ropa, accesorios, mochilas, artículos de viaje.
- **Zona de Chácharas**: Electrónicos, juguetes, artículos variados.
- **Zona de Artesanías**: Recuerdos típicos de Puebla.""",
    """### 🌮 Comida de Terminal
> "Los tacos de la CAPU son famosos entre los viajeros. Rápidos, ricos y económicos. Las tortas de la abuela son mi parada obligada antes de tomar el autobús."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+CAPU+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Últimas Compras
> "Ideal para comprar frutas y verduras antes de subir al autobús. Precios de terminal, no los más baratos, pero hay buena variedad. Cómodo para viajeros."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=CAPU+mercado+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 🛡️ Seguridad
> "La zona de la CAPU es concurrida, hay vigilancia. Como en toda terminal de autobuses, hay que cuidar las pertenencias personales y el equipaje."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=CAPU+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "En la zona de la CAPU (Central de Autobuses de Puebla), Blvd. Municipio Libre. Se llega en cualquier autobús que vaya a la CAPU. El tianguis está en las calles alrededor de la terminal.",
    ["Ir los jueves — el día del tianguis CAPU.",
     "Probar las tortas y tacos de los puestos de comida.",
     "Comprar frutas para el viaje si vas a salir de la CAPU.",
     "Cuidar las pertenencias en la zona de la terminal.",
     "Visitar temprano para mejor variedad."])

write("valle_serdan", 25, "Tianguis TAMEME — Orgánico y Artesanal, Puebla", ["Martes", "Sábado"],
    [19.0100, -98.2350],
    ["plaza-campo", "canasta-basica", "hierbas-medicina", "cultura-tradicion", "identidad-oficios"],
    "Zona residencial segura, ambiente tranquilo y familiar",
    "9:00 AM — 4:00 PM",
    "🌱",
    "TAMEME es el tianguis orgánico y artesanal más importante de Puebla. Un espacio de consumo responsable donde productores locales ofrecen alimentos libres de químicos y artesanías.",
    """Se instala en un espacio privado al sur de la ciudad:

- **Zona de Orgánicos**: Frutas, verduras y hortalizas cultivadas sin pesticidas.
- **Zona de Productos Artesanales**: Quesos, pan, miel, mermeladas, café orgánico.
- **Zona de Comida Saludable**: Comida vegana, vegetariana, sin gluten, fermentados.
- **Zona de Artesanías**: Textiles, cerámica, joyería artesanal.
- **Zona de Hierbas Medicinales**: Tés, infusiones, suplementos naturales.""",
    """### 🌱 Consumo Consciente
> "TAMEME es el mejor lugar para comprar orgánico en Puebla. Los productores están ahí, te cuentan cómo cultivan, sin químicos. El sabor de las verduras es incomparable."
- **Tipo:** #Plaza
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=TAMEME+Puebla+tianguis)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🌿 Sabores Auténticos
> "El pan artesanal de TAMEME es espectacular. Masas madre, fermentaciones largas, ingredientes orgánicos. El queso de cabra artesanal es otro imperdible."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=TAMEME+comida)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Precios Justos
> "Sí, es un poco más caro que el tianguis normal, pero la calidad es superior. Trato directo con productores, sabes de dónde viene tu comida. Vale cada peso."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=TAMEME+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🛡️ Ambiente Seguro
> "Es un espacio privado, tranquilo, familiar. Perfecto para ir con niños. Ambiente relajado, sin aglomeraciones. Música en vivo algunos días."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=TAMEME+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)""",
    "En el sur de Puebla. Se llega en coche o Uber. El estacionamiento es gratuito. También hay rutas de autobús que pasan cerca.",
    ["Ir los sábados por la mañana — hay más productores y variedad.",
     "Llevar bolsas reutilizables y recipientes para compras a granel.",
     "Probar el pan artesanal de masa madre.",
     "Hablar con los productores — te explican sus procesos.",
     "Llevar efectivo — algunos puestos aceptan tarjeta."])

write("valle_serdan", 26, "Tianguis de Puebla 7 Sur", ["Miércoles"],
    [19.0400, -98.1950],
    ["canasta-basica", "garnachas-sabor", "chacharas-antiguedades", "plaza-campo"],
    "Zona de la colonia Loma Bella, ambiente de barrio concurrido",
    "8:00 AM — 4:00 PM",
    "🏪",
    "El Tianguis de la 7 Sur es uno de los más concurridos de la zona sur de Puebla, donde los miércoles las calles se llenan de puestos con productos frescos, ropa y comida.",
    """Se instala sobre la Calle 7 Sur:

- **Zona de Frutas y Verduras**: Productos frescos para la despensa semanal.
- **Zona de Comida**: Tacos, tlacoyos, gorditas, tortas, aguas frescas.
- **Zona de Ropa**: Ropa nueva y de paca, accesorios.
- **Zona de Chácharas**: Herramientas, juguetes, artículos del hogar.
- **Zona de Plantas**: Plantas ornamentales y flores.""",
    """### 🌮 Garnachas del Sur
> "Los miércoles de tianguis en la 7 Sur son sagrados. Las gorditas de chicharrón son mi antojo. La salsa verde de Doña Mary es la mejor de toda la colonia."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+7+sur+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Precios de Barrio
> "Los precios son accesibles, para el gasto diario. Gasto $200-300 para la semana. La verdura es fresca y variada."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=7+sur+Puebla+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1566385101042-1a0cd0c8d1e5?w=400)
### 👕 Ropa para la Familia
> "Encuentras ropa para niños a muy buen precio. Juguetes, mochilas, útiles escolares. Ideal para familias."
- **Tipo:** #LaPaca
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=ropa+7+sur+Puebla)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)""",
    "En la Calle 7 Sur, colonia Loma Bella. Autobuses Ruta Loma Bella o Ruta Sur. En coche: Av. 16 de Septiembre.",
    ["Ir los miércoles — día del tianguis.",
     "Probar las gorditas de chicharrón.",
     "Hacer la despensa de la semana.",
     "Llevar efectivo.",
     "Ir temprano para mejor selección."])

# ============ MIXTECA (27-38) ============

write("mixteca", 27, "Tianguis Dominical de Acatlán de Osorio", ["Domingo"],
    [18.2019, -98.0486],
    ["cultura-tradicion", "artesania", "plaza-campo", "canasta-basica", "identidad-oficios"],
    "Zona del mercado municipal y centro, ambiente de tianguis tradicional mixteco",
    "7:00 AM — 4:00 PM",
    "🏺",
    "Acatlán de Osorio es la capital de la Mixteca Poblana y su tianguis dominical es el corazón comercial de la región, donde se encuentran las comunidades mixtecas y popolocas.",
    """El tianguis se instala en el centro de Acatlán:

- **Zona de Artesanías Mixtecas**: Barro vidriado, textiles de lana, bordados mixtecos.
- **Zona de Frutas y Verduras**: Productos de la Mixteca: jitomate, chile, cacahuate, ajonjolí.
- **Zona de Comida**: Mole mixteco, barbacoa, barbacoa de hoyo, tamales.
- **Zona de Ropa y Textiles**: Ropa, sarapes, cobijas de lana, huaraches.
- **Zona de Plantas Medicinales**: Hierbas de la tradición mixteca.""",
    """### 🏺 Barro de Acatlán
> "La cerámica de Acatlán es famosa en todo México. En el tianguis dominical encuentras piezas de barro vidriado directamente de los alfareros. Cazuelas, jarrones, vajillas completas."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Acatlan+Osorio)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)
### 🌮 Mole Mixteco
> "El mole de la Mixteca es diferente al poblano. Más espeso, con más especias. Doña Chole lo prepara con receta familiar de tres generaciones. Imperdible."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Acatlan+Osorio)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 La Mixteca Barata
> "Los precios en Acatlán son de los más bajos de Puebla. La canasta básica cuesta una fracción de lo que cuesta en la capital. Las frutas y verduras son muy económicas."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Acatlan+precios+mercado)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🎭 Cultura Mixteca
> "Las mujeres mixtecas venden con sus trajes típicos. Se escucha el mixteco en el tianguis. Es una experiencia cultural auténtica, alejada del turismo masivo."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+mixteca+Acatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🛡️ Acatlán Seguro
> "Acatlán es una ciudad tranquila. El tianguis dominical es seguro, ambiente familiar. La gente es amable y hospitalaria con los visitantes."
- **Tipo:** #Seguridad
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Acatlan+seguridad)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1544230726-4d48a0e7a89f?w=400)
### 🔄 Trueque Mixteco
> "En las comunidades más alejadas todavía se práctica el trueque. En el tianguis de Acatlán a veces ves intercambios directos entre campesinos."
- **Tipo:** #Trueque
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=trueque+Acatlan)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1578911595545-8d12f0b7b15e?w=400)""",
    "Desde Puebla: Autobuses desde la CAPU (3 hrs). En coche: Carretera federal Puebla-Huajuapan (ruta 190). El tianguis está en el centro de la ciudad.",
    ["Comprar cerámica de barro vidriado directamente de los alfareros.",
     "Probar el mole mixteco.",
     "Visitar el Mercado Municipal de Acatlán.",
     "Comprar cacahuate y ajonjolí de la región.",
     "Llevar efectivo."])

write("mixteca", 28, "Tianguis de Izúcar de Matamoros", ["Lunes", "Viernes"],
    [18.6019, -98.4642],
    ["canasta-basica", "plaza-campo", "garnachas-sabor", "cultura-tradicion", "artesania"],
    "Zona del centro, ambiente de tianguis regional con vigilancia municipal",
    "7:00 AM — 5:00 PM",
    "🌮",
    "Izúcar de Matamoros, puerta de la Mixteca Poblana, tiene sus tianguis los lunes y viernes. Es el centro de abasto más importante de la región sur del estado.",
    """El tianguis se instala en las calles del centro:

- **Zona de Carnitas**: Izúcar es famoso por sus carnitas al estilo poblano. Varios puestos especializados.
- **Zona de Frutas y Verduras**: Productos de la región mixteca.
- **Zona de Artesanías**: Cerámica, textiles, bordados popolocas y mixtecos.
- **Zona de Comida**: Chicharrón, carnitas, mole, tamales.
- **Zona de Ropa y Mercancía**: Ropa, calzado, productos del hogar.""",
    """### 🌮 Carnitas de Izúcar
> "Izúcar es la capital de las carnitas en Puebla. En el tianguis los lunes hay puestos especializados. Chicharrón, cueritos, maciza, costilla. Todo recién hecho."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Izucar+Matamoros)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 El Lunes de Plaza
> "Los lunes es el día más grande. Viene gente de toda la región. Los precios son buenos, especialmente en frutas y verduras. Compro para toda la semana."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Izucar+precios+mercado)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🎭 Cultura Popoloca
> "En Izúcar conviven mixtecos y popolocas. Cada grupo trae sus artesanías y productos característicos. El tianguis es un mosaico cultural único en Puebla."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=cultura+popoloca+Izucar)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🏺 Alfarería
> "La cerámica de Izúcar tiene tradición centenaria. En el tianguis encuentras piezas de barro vidriado, cazuelas y ollas a buen precio."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=alfareria+Izucar)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1590915859829-3a2593b4021f?w=400)
### 🚇 Acceso
> "Autobuses desde Puebla cada hora (1.5 hrs). En coche: Carretera Puebla-Izúcar (ruta 190). El tianguis está en el centro de la ciudad."
- **Tipo:** #Acceso
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+Izucar)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (1.5 hrs). En coche: Carretera Puebla-Izúcar. El tianguis se instala en las calles del centro de Izúcar.",
    ["Ir los lunes — el día más grande del tianguis.",
     "Probar las carnitas al estilo poblano.",
     "Comprar cerámica de barro vidriado.",
     "Visitar la Feria de Santo Domingo (agosto).",
     "Llevar efectivo."])

write("mixteca", 29, "Tianguis Dominical de Tehuitzingo", ["Domingo"],
    [18.3331, -98.2831],
    ["plaza-campo", "canasta-basica", "cultura-tradicion", "identidad-oficios"],
    "Zona del centro, ambiente rural tradicional mixteco",
    "7:00 AM — 3:00 PM",
    "🌵",
    "Tehuitzingo, en plena Mixteca Poblana, celebra su tianguis dominical como el evento más importante de la semana. Es el punto de encuentro de las comunidades mixtecas de la región.",
    """El tianguis dominical se instala en el centro del pueblo:

- **Zona de Productos de la Región**: Cacahuate, ajonjolí, jitomate, chile seco.
- **Zona de Artesanías Mixtecas**: Textiles, bordados, cestería, sombreros de palma.
- **Zona de Comida**: Mole, barbacoa de hoyo, tamales mixtecos.
- **Zona de Ropa**: Ropa, calzado, sombreros.
- **Zona de Plantas**: Plantas medicinales y árboles frutales.""",
    """### 🌵 Corazón Mixteco
> "Tehuitzingo es la Mixteca más auténtica. El domingo todo el pueblo se vuelca al tianguis. Los campesinos bajan de las comunidades a vender sus cosechas. Es pura tradición."
- **Tipo:** #Cultura
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+Tehuitzingo)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400)
### 🌮 Barbacoa de Hoyo
> "La barbacoa de hoyo de Tehuitzingo es legendaria. La preparan bajo tierra, envuelta en pencas de maguey. El sabor ahumado es único. Los domingos es el platillo estrella."
- **Tipo:** #Sabor
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=comida+Tehuitzingo)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=400)
### 💰 Precios de Campo
> "Los precios en Tehuitzingo son de los más bajos de la Mixteca. Cacahuate, ajonjolí y jitomate directamente del productor. Una ganga."
- **Tipo:** #Precio
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=Tehuitzingo+precios)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1577392742038-5e2d2f8c6301?w=400)
### 🧵 Textiles Mixtecos
> "Los textiles de Tehuitzingo son famosos. Bordados a mano, colores vivos, diseños tradicionales. Las mujeres mixtecas tejen servilletas, manteles y blusas."
- **Tipo:** #Artesania
- 🔗 **Evidencia:** [YouTube](https://www.youtube.com/results?search_query=textiles+Tehuitzingo)
- 📸 **Foto:** ![Tianguis Puebla](https://images.unsplash.com/photo-1605515296013-18a0c2f2b6aa?w=400)""",
    "Desde Puebla: Autobuses desde CAPU (2.5 hrs) vía Izúcar. En coche: Carretera Puebla-Izúcar, luego desviación a Tehuitzingo.",
    ["Ir los domingos que es el día de plaza.",
     "Probar la barbacoa de hoyo.",
     "Comprar cacahuate y ajonjolí de la región.",
     "Adquirir textiles bordados a mano.",
     "Llevar efectivo."])

print("Files 22-29 done")
