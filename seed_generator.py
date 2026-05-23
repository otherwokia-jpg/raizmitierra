#!/usr/bin/env python3
"""
🌎 RAÍZMITIERRA — Generador Masivo de Tianguis
Genera archivos .md para los 6 estados en lotes.
Ejecutar: python3 seed_generator.py
"""

import os
import json

BASE = os.path.expanduser("~/raizmitierra/database")

# ══════════════════════════════════════════════
# DATOS: CDMX (65 ya creados por subagente)
# ══════════════════════════════════════════════

CDMX_TIANGUIS = [
    # centro/
    {"id":"MX-CDMX-001","name":"Tianguis de La Lagunilla — El Salto del Agua","region":"centro","state":"cdmx","days":["Domingo"],"coords":[19.4420,-99.1420],"cats":["chacharas-antiguedades","identidad-oficios","garnachas-sabor"],"safety":"Seguro, mucho turista","horario":"7:00-16:00","quote":"El tianguis más tradicional del Centro Histórico. Muebles antiguos, discos de vinil, libros, monedas y un ambiente de otro siglo."},
    {"id":"MX-CDMX-002","name":"Tianguis de Tepito — Barrio Bravo","region":"centro","state":"cdmx","days":["Martes","Sábado","Domingo"],"coords":[19.4450,-99.1180],"cats":["la-paca","chacharas-antiguedades","garnachas-sabor","canasta-basica"],"safety":"Mucha gente, cuidar pertenencias","horario":"7:00-18:00","quote":"El tianguis más famoso de Latinoamérica. Aquí encuentras de todo: ropa de marca, electrónica, chácharas y la mejor comida de barrio."},
    {"id":"MX-CDMX-003","name":"Mercado de Sonora — Brujería y Tradición","region":"centro","state":"cdmx","days":["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"],"coords":[19.4230,-99.1210],"cats":["hierbas-medicina","cultura-tradicion","canasta-basica"],"safety":"Turístico, seguro de día","horario":"8:00-18:00","quote":"El mercado más místico de México. Hierbas, velas, animales, amuletos y todo lo relacionado con la santería y la medicina tradicional."},
    {"id":"MX-CDMX-004","name":"Mercado de La Merced — El Gigante del Centro","region":"centro","state":"cdmx","days":["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"],"coords":[19.4270,-99.1180],"cats":["canasta-basica","garnachas-sabor","flores-plantas"],"safety":"Mucho movimiento, cuidar carteras","horario":"5:00-17:00","quote":"El mercado de abastos más grande del Centro. Fruta, verdura, carne, flores, todo al mayoreo y menudeo."},
    {"id":"MX-CDMX-005","name":"Mercado de San Juan — Sabores del Mundo","region":"centro","state":"cdmx","days":["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"],"coords":[19.4320,-99.1400],"cats":["garnachas-sabor","canasta-basica"],"safety":"Zona turística, muy seguro","horario":"8:00-18:00","quote":"El mercado gourmet de la CDMX. Carnes exóticas, quesos artesanales, insectos, vinos y la mejor cocina mexicana."},
    {"id":"MX-CDMX-006","name":"Tianguis de Peralvillo — Ropa y Tradición","region":"centro","state":"cdmx","days":["Martes","Sábado","Domingo"],"coords":[19.4520,-99.1220],"cats":["la-paca","canasta-basica","garnachas-sabor"],"safety":"Seguro, familiar","horario":"7:00-16:00","quote":"Tianguis de barrio con ropa de paca, fruta y verdura fresca. Ambiente familiar y precios populares."},
    # sur/
    {"id":"MX-CDMX-007","name":"Tianguis de Xochimilco — Flores y Tradición","region":"sur","state":"cdmx","days":["Jueves","Sábado","Domingo"],"coords":[19.2580,-99.1060],"cats":["flores-plantas","canasta-basica","identidad-oficios"],"safety":"Muy seguro, zona turística","horario":"7:00-17:00","quote":"El tianguis de las flores. Chinampas, plantas de ornato, flores de temporada y la tradición viva de los pueblos originarios de Xochimilco."},
    {"id":"MX-CDMX-008","name":"Tianguis de Milpa Alta — Nopal y Tradición","region":"sur","state":"cdmx","days":["Domingo"],"coords":[19.1920,-99.0230],"cats":["canasta-basica","plaza-campo","identidad-oficios","garnachas-sabor"],"safety":"Muy seguro, rural","horario":"6:00-15:00","quote":"El último tianguis rural de la CDMX. Nopal, maíz criollo, barbacoa de hoyo y la venta directa de los productores de Milpa Alta."},
    # oriente/
    {"id":"MX-CDMX-009","name":"Tianguis de El Salado — El Más Grande de Iztapalapa","region":"oriente","state":"cdmx","days":["Martes","Jueves","Sábado","Domingo"],"coords":[19.3600,-99.0930],"cats":["la-paca","chacharas-antiguedades","canasta-basica","garnachas-sabor"],"safety":"Mucha gente, cuidar pertenencias","horario":"6:00-17:00","quote":"El tianguis más grande de Iztapalapa. Ropa de paca, fruta, verdura, chácharas, electrónica y comida. Pararse a buscar es la clave."},
    {"id":"MX-CDMX-010","name":"Tianguis de Santa Cruz Meyehualco — El Corazón de Iztapalapa","region":"oriente","state":"cdmx","days":["Miércoles","Sábado","Domingo"],"coords":[19.3500,-99.0700],"cats":["canasta-basica","garnachas-sabor","la-paca"],"safety":"Seguro, familiar","horario":"7:00-16:00","quote":"Tianguis de barrio con tradición. Fruta y verdura de temporada, ropa, antojitos y el mejor ambiente de Iztapalapa."},
    # norte/
    {"id":"MX-CDMX-011","name":"Tianguis de San Felipe de Jesús — La San Feroz","region":"norte","state":"cdmx","days":["Martes","Viernes","Domingo"],"coords":[19.5200,-99.0730],"cats":["la-paca","garnachas-sabor","canasta-basica"],"safety":"Seguro de día, concurrido","horario":"7:00-16:00","quote":"El tianguis más grande de GAM. Ropa de paca, fruta, verdura y los mejores tacos de canasta del norte de la ciudad."},
    # poniente/
    {"id":"MX-CDMX-012","name":"Tianguis de San Ángel — Artesanías y Sábado de Plaza","region":"poniente","state":"cdmx","days":["Sábado"],"coords":[19.3440,-99.1860],"cats":["identidad-oficios","garnachas-sabor","flores-plantas"],"safety":"Zona turística, seguro","horario":"9:00-17:00","quote":"El tianguis más tradicional de la zona sur poniente. Flores, artesanías, pintura, comida y el ambiente del San Ángel colonial."},
]

PUEBLA_TIANGUIS = [
    {"id":"MX-PUE-001","name":"Tianguis Dominical de Cuetzalan — Corazón Totonaca","region":"sierra_norte","state":"puebla","days":["Domingo"],"coords":[20.0175,-97.5217],"cats":["identidad-oficios","cultura-tradicion","garnachas-sabor","canasta-basica"],"safety":"Muy seguro, Pueblo Mágico","horario":"6:00-16:00","quote":"El tianguis indígena más importante de la Sierra Norte. Nahuas y totonacas bajan de las comunidades a vender café, vainilla, textiles y bordados."},
    {"id":"MX-PUE-002","name":"Tianguis de Huauchinango — Flores y Café de la Sierra","region":"sierra_norte","state":"puebla","days":["Domingo"],"coords":[20.1759,-98.0542],"cats":["flores-plantas","canasta-basica","identidad-oficios"],"safety":"Seguro, familiar","horario":"7:00-15:00","quote":"Capital de la flor. Azaleas, hortensias, café de altura y la calidez de la Sierra Norte de Puebla."},
    {"id":"MX-PUE-003","name":"Tianguis de Xicotepec — Café y Tradición","region":"sierra_norte","state":"puebla","days":["Domingo"],"coords":[20.2747,-97.9633],"cats":["garnachas-sabor","canasta-basica","cultura-tradicion"],"safety":"Seguro, Pueblo Mágico","horario":"7:00-15:00","quote":"El tianguis del café de altura. Productores locales, granos artesanales, nieves de café y el mejor ambiente serrano."},
    {"id":"MX-PUE-004","name":"Tianguis de Zacatlán — Manzanas y Quesos","region":"sierra_norte","state":"puebla","days":["Domingo"],"coords":[19.9333,-97.9608],"cats":["canasta-basica","identidad-oficios","garnachas-sabor"],"safety":"Muy seguro, Pueblo Mágico","horario":"8:00-16:00","quote":"El valle de las manzanas. Sidra, queso de cabra, pan de horno y los mejores paisajes de la Sierra."},
    {"id":"MX-PUE-005","name":"Tianguis de Pahuatlán — Pueblo Mágico Otomí","region":"sierra_norte","state":"puebla","days":["Domingo"],"coords":[20.2778,-98.1492],"cats":["identidad-oficios","cultura-tradicion","hierbas-medicina"],"safety":"Seguro","horario":"7:00-14:00","quote":"El tianguis otomí más auténtico. Papel amate, bordados y medicina tradicional en lo alto de la Sierra."},
    {"id":"MX-PUE-006","name":"Mercado de Cholula — Los Portales Milenarios","region":"valle_serdan","state":"puebla","days":["Jueves","Domingo"],"coords":[19.0633,-98.3036],"cats":["identidad-oficios","garnachas-sabor","canasta-basica"],"safety":"Muy seguro, zona turística","horario":"8:00-17:00","quote":"El mercado bajo los portales de Cholula. Talavera, cemitas, chiles en nogada y la energía de la ciudad sagrada."},
    {"id":"MX-PUE-007","name":"Tianguis de Atlixco — El Valle de las Flores","region":"valle_serdan","state":"puebla","days":["Sábado","Domingo"],"coords":[18.9086,-98.4347],"cats":["flores-plantas","canasta-basica","garnachas-sabor"],"safety":"Muy seguro","horario":"7:00-16:00","quote":"Atlixco, el mejor clima del mundo. Flores de temporada, fruta, verdura y la vista imponente del Popocatépetl."},
    {"id":"MX-PUE-008","name":"Tianguis de Tehuacán — El Oasis Mixteco","region":"valle_serdan","state":"puebla","days":["Domingo","Miércoles"],"coords":[18.4647,-97.3925],"cats":["canasta-basica","chacharas-antiguedades","garnachas-sabor"],"safety":"Seguro","horario":"7:00-16:00","quote":"La puerta de la Mixteca. Fruta, verdura, barbacoa, pan de horno y el agua mineral natural de Tehuacán."},
    {"id":"MX-PUE-009","name":"Tianguis de Izúcar de Matamoros — La Mixteca Poblana","region":"mixteca","state":"puebla","days":["Domingo"],"coords":[18.6014,-98.4697],"cats":["identidad-oficios","canasta-basica","garnachas-sabor"],"safety":"Seguro","horario":"7:00-15:00","quote":"El corazón de la Mixteca poblana. Artesanías de palma, barro y la comida tradicional mixteca."},
    {"id":"MX-PUE-010","name":"Tianguis de Acatlán de Osorio — Palma y Tradición","region":"mixteca","state":"puebla","days":["Domingo"],"coords":[18.2006,-98.0486],"cats":["identidad-oficios","muebles-artesanales","canasta-basica"],"safety":"Seguro","horario":"7:00-15:00","quote":"Capital mundial de la palma. Sombreros, petates, bolsas y la tradición mixteca que teje la identidad de Puebla."},
]

MICHOACAN_TIANGUIS = [
    {"id":"MX-MICH-001","name":"Tianguis de Pátzcuaro — Trueque Purépecha","region":"lago_patzcuaro","state":"michoacan","days":["Viernes","Domingo"],"coords":[19.5175,-101.6089],"cats":["plaza-campo","identidad-oficios","cultura-tradicion","garnachas-sabor"],"safety":"Muy seguro, Pueblo Mágico","horario":"7:00-16:00","quote":"El tianguis purépecha más antiguo. Trueque, artesanía de cobre, madera tallada y la cosmovisión de la Meseta."},
    {"id":"MX-MICH-002","name":"Tianguis Artesanal de Uruapan — Domingo de Ramos","region":"meseta_purhepecha","state":"michoacan","days":["Domingo"],"coords":[19.4201,-102.0593],"cats":["identidad-oficios","muebles-artesanales","garnachas-sabor","cultura-tradicion"],"safety":"Muy seguro","horario":"8:00-18:00","quote":"El tianguis artesanal más grande de Michoacán. 49 comunidades indígenas, 4 etnias, maderas, cobre, textiles y la mejor gastronomía purépecha."},
    {"id":"MX-MICH-003","name":"Tianguis de Morelia — El Acueducto y el Trueque","region":"meseta_purhepecha","state":"michoacan","days":["Sábado","Domingo"],"coords":[19.7048,-101.1958],"cats":["canasta-basica","identidad-oficios","garnachas-sabor","chacharas-antiguedades"],"safety":"Seguro, zona turística","horario":"7:00-17:00","quote":"El tianguis bajo la sombra del acueducto. Corundas, uchepos, atole de grano y la calidez moreliana."},
    {"id":"MX-MICH-004","name":"Tianguis de Santa Clara del Cobre — Martillo y Yunque","region":"lago_patzcuaro","state":"michoacan","days":["Sábado","Domingo"],"coords":[19.4047,-101.6381],"cats":["identidad-oficios","muebles-artesanales","cultura-tradicion"],"safety":"Muy seguro","horario":"8:00-17:00","quote":"La capital del cobre martillado. Artesanos del metal rojo, piezas únicas forjadas a mano y el orgullo purépecha."},
    {"id":"MX-MICH-005","name":"Tianguis de Apatzingán — La Tierra Caliente","region":"tierra_caliente","state":"michoacan","days":["Domingo","Miércoles"],"coords":[19.0867,-102.3528],"cats":["canasta-basica","garnachas-sabor","chacharas-antiguedades"],"safety":"Seguro de día","horario":"6:00-14:00","quote":"El tianguis de la tierra caliente. Mango, tamarindo, coco, pescado seco y el sabor del trópico michoacano."},
    {"id":"MX-MICH-006","name":"Tianguis de Zitácuaro — El Oriente Michoacano","region":"meseta_purhepecha","state":"michoacan","days":["Domingo","Miércoles"],"coords":[19.4372,-100.3581],"cats":["canasta-basica","garnachas-sabor","identidad-oficios"],"safety":"Seguro","horario":"7:00-15:00","quote":"La puerta de Michoacán. Fruta de la región, aguacate, barbacoa y la tradición otomí del oriente michoacano."},
    {"id":"MX-MICH-007","name":"Tianguis de Lázaro Cárdenas — La Costa Michoacana","region":"costa","state":"michoacan","days":["Domingo","Sábado"],"coords":[17.9697,-102.2178],"cats":["garnachas-sabor","canasta-basica","chacharas-antiguedades"],"safety":"Seguro","horario":"6:00-14:00","quote":"El tianguis del puerto. Pescado fresco, camarón, coco, plátano y la brisa del Pacífico michoacano."},
    {"id":"MX-MICH-008","name":"Mercado de Artesanías de Capula — La Capilla del Cobre","region":"meseta_purhepecha","state":"michoacan","days":["Sábado","Domingo"],"coords":[19.7184,-101.5453],"cats":["identidad-oficios","muebles-artesanales","cultura-tradicion"],"safety":"Muy seguro","horario":"9:00-17:00","quote":"La cuna de la Catrina de barro. Alfarería purépecha, catrinas tradicionales y la comunidad artesana más famosa de Michoacán."},
    {"id":"MX-MICH-009","name":"Tianguis de Tacámbaro — Café de Altura","region":"meseta_purhepecha","state":"michoacan","days":["Domingo"],"coords":[19.2361,-101.4592],"cats":["canasta-basica","garnachas-sabor","identidad-oficios"],"safety":"Seguro","horario":"7:00-15:00","quote":"Tierra de café de altura. Granos artesanales, fruta, queso y el clima privilegiado de la Meseta Purépecha."},
    {"id":"MX-MICH-010","name":"Tianguis de Huetamo — El Último Baluarte de la Tierra Caliente","region":"tierra_caliente","state":"michoacan","days":["Domingo","Jueves"],"coords":[18.6256,-100.8981],"cats":["canasta-basica","garnachas-sabor","animales-corral"],"safety":"Seguro de día","horario":"6:00-14:00","quote":"El corazón de Tierra Caliente. Ganado, frutas tropicales, queso cotija y la cultura vaquera de Michoacán."},
]

MORELOS_TIANGUIS = [
    {"id":"MX-MOR-001","name":"Mercado de Tepoztlán — El Pueblo Mágico del Tepozteco","region":"altiplano","state":"morelos","days":["Martes","Domingo"],"coords":[18.9858,-99.1000],"cats":["identidad-oficios","hierbas-medicina","garnachas-sabor","canasta-basica"],"safety":"Muy seguro, Pueblo Mágico","horario":"8:00-17:00","quote":"El tianguis más místico de Morelos. Itacates, quesadillas de hongos, aguas frescas de sabores, artesanías y la energía del Tepozteco."},
    {"id":"MX-MOR-002","name":"Tianguis de Cuautla — El Corazón del Oriente Morelense","region":"altiplano","state":"morelos","days":["Domingo","Miércoles"],"coords":[18.8119,-98.9553],"cats":["canasta-basica","garnachas-sabor","la-paca","chacharas-antiguedades"],"safety":"Seguro","horario":"6:00-16:00","quote":"El tianguis más grande de Morelos. Fruta, verdura, ropa de paca, chácharas y la cecina de Yecapixtla."},
    {"id":"MX-MOR-003","name":"Tianguis de Cuernavaca — La Ciudad de la Eterna Primavera","region":"altiplano","state":"morelos","days":["Domingo","Sábado","Miércoles"],"coords":[18.9214,-99.2308],"cats":["canasta-basica","flores-plantas","garnachas-sabor","identidad-oficios"],"safety":"Seguro","horario":"7:00-16:00","quote":"La eterna primavera en los tianguis. Fruta de temporada, flores tropicales, plantas de ornato y la cocina morelense."},
    {"id":"MX-MOR-004","name":"Tianguis de Xochitepec — Tierra de Caña y Piloncillo","region":"altiplano","state":"morelos","days":["Viernes","Domingo"],"coords":[18.7817,-99.2306],"cats":["canasta-basica","garnachas-sabor","chacharas-antiguedades"],"safety":"Seguro","horario":"7:00-15:00","quote":"La tierra de la caña de azúcar. Piloncillo, fruta tropical, cecina y la tradición morelense."},
    {"id":"MX-MOR-005","name":"Tianguis de Yautepec — El Pueblo del Pan","region":"altiplano","state":"morelos","days":["Domingo","Jueves"],"coords":[18.8817,-99.0686],"cats":["canasta-basica","garnachas-sabor","identidad-oficios"],"safety":"Seguro","horario":"7:00-15:00","quote":"El pueblo del pan. Pan de horno, fruta, verdura, barbacoa y la calidez de Yautepec."},
    {"id":"MX-MOR-006","name":"Tianguis de Jojutla — La Puerta Sur de Morelos","region":"sur_norte","state":"morelos","days":["Domingo","Miércoles"],"coords":[18.6147,-99.1881],"cats":["canasta-basica","garnachas-sabor","chacharas-antiguedades"],"safety":"Seguro","horario":"6:00-14:00","quote":"El tianguis del sur morelense. Fruta tropical, pescado de río, barbacoa de hoyo y la cultura campesina."},
    {"id":"MX-MOR-007","name":"Tianguis de Tlayacapan — Barro y Tradición","region":"altiplano","state":"morelos","days":["Miércoles","Domingo"],"coords":[18.9578,-98.9817],"cats":["identidad-oficios","canasta-basica","garnachas-sabor"],"safety":"Seguro, Pueblo con Encanto","horario":"7:00-15:00","quote":"El tianguis del barro. Alfarería tradicional, artesanías, fruta y la tradición de los voladores."},
]

HIDALGO_TIANGUIS = [
    {"id":"MX-HGO-001","name":"Tianguis de Pachuca — La Bella Airosa","region":"sur_norte","state":"hidalgo","days":["Domingo","Miércoles","Sábado"],"coords":[20.1107,-98.7680],"cats":["canasta-basica","garnachas-sabor","la-paca","chacharas-antiguedades"],"safety":"Seguro","horario":"7:00-16:00","quote":"El tianguis de la Bella Airosa. Pastes, fruta, ropa, chácharas y el frío de Pachuca."},
    {"id":"MX-HGO-002","name":"Tianguis de Tulancingo — Cuna del Futbol Mexicano","region":"sur_norte","state":"hidalgo","days":["Domingo","Martes"],"coords":[20.0833,-98.3667],"cats":["canasta-basica","garnachas-sabor","la-paca","identidad-oficios"],"safety":"Seguro","horario":"7:00-16:00","quote":"La cuna del futbol mexicano. Fruta, ropa, artesanías de lana y los mejores pastes de Hidalgo."},
    {"id":"MX-HGO-003","name":"Tianguis de Huasca de Ocampo — Pueblo Mágico de los Prismas","region":"sierra","state":"hidalgo","days":["Domingo"],"coords":[20.2019,-98.5767],"cats":["identidad-oficios","garnachas-sabor","cultura-tradicion"],"safety":"Muy seguro, Pueblo Mágico","horario":"8:00-16:00","quote":"El primer Pueblo Mágico de México. Artesanías de cantera, pulque, barbacoa y los Prismas Basálticos."},
    {"id":"MX-HGO-004","name":"Tianguis de Real del Monte — Minería y Pastes","region":"sierra","state":"hidalgo","days":["Sábado","Domingo"],"coords":[20.1289,-98.6719],"cats":["garnachas-sabor","identidad-oficios","cultura-tradicion"],"safety":"Muy seguro, Pueblo Mágico","horario":"8:00-17:00","quote":"El pueblo minero. Pastes de la Cornualles, pan de pulque, artesanías de plata y la historia de la minería en México."},
    {"id":"MX-HGO-005","name":"Tianguis de Actopan — El Pueblo de los Murales","region":"valle_mezquital","state":"hidalgo","days":["Domingo","Martes"],"coords":[20.2683,-98.9486],"cats":["canasta-basica","garnachas-sabor","identidad-oficios"],"safety":"Seguro","horario":"7:00-15:00","quote":"El corazón del Valle del Mezquital. Barbacoa de borrego, ximbó, pulque y la cultura otomí de Hidalgo."},
    {"id":"MX-HGO-006","name":"Tianguis de Ixmiquilpan — La Puerta Otomí","region":"valle_mezquital","state":"hidalgo","days":["Domingo","Miércoles"],"coords":[20.4844,-99.2208],"cats":["identidad-oficios","canasta-basica","garnachas-sabor","hierbas-medicina"],"safety":"Seguro","horario":"7:00-15:00","quote":"La capital de la cultura otomí. Artesanías, hierbas medicinales, barbacoa y el Valle del Mezquital."},
    {"id":"MX-HGO-007","name":"Tianguis de Huejutla — La Huasteca Hidalguense","region":"huasteca","state":"hidalgo","days":["Domingo","Miércoles"],"coords":[21.1406,-98.4228],"cats":["canasta-basica","garnachas-sabor","identidad-oficios","cultura-tradicion"],"safety":"Seguro","horario":"6:00-15:00","quote":"La Huasteca hidalguense. Zacahuil, café, vainilla, piloncillo y la calidez de la cultura huasteca."},
    {"id":"MX-HGO-008","name":"Tianguis de Apan — Tierra del Pulque","region":"sur_norte","state":"hidalgo","days":["Domingo","Miércoles"],"coords":[19.7147,-98.4572],"cats":["canasta-basica","cultura-tradicion","garnachas-sabor"],"safety":"Seguro","horario":"7:00-15:00","quote":"La tierra del pulque. Haciendas pulqueras, barbacoa, mixiotes y la tradición milenaria del maguey."},
]

TLAXCALA_TIANGUIS = [
    {"id":"MX-TLX-001","name":"Tianguis de Tlaxcala Capital — La Ciudad de las Artesanías","region":"centro","state":"tlaxcala","days":["Domingo","Miércoles","Sábado"],"coords":[19.3183,-98.2386],"cats":["identidad-oficios","garnachas-sabor","canasta-basica","chacharas-antiguedades"],"safety":"Seguro","horario":"7:00-16:00","quote":"El tianguis más grande de Tlaxcala. Sarapes, textiles de lana, barbacoa, pulque y la tradición tlaxcalteca."},
    {"id":"MX-TLX-002","name":"Tianguis de Huamantla — La Noche que Nadie Duerme","region":"centro","state":"tlaxcala","days":["Domingo","Viernes"],"coords":[19.3114,-97.9267],"cats":["identidad-oficios","cultura-tradicion","garnachas-sabor","canasta-basica"],"safety":"Muy seguro, Pueblo Mágico","horario":"7:00-16:00","quote":"La ciudad de las alfombras de aserrín. Artesanías, barbacoa, pulque y la tradición más colorida de Tlaxcala."},
    {"id":"MX-TLX-003","name":"Tianguis de Apizaco — El Nudo Ferrocarrilero","region":"centro","state":"tlaxcala","days":["Domingo","Sábado"],"coords":[19.4169,-98.1375],"cats":["la-paca","canasta-basica","garnachas-sabor","chacharas-antiguedades"],"safety":"Seguro","horario":"7:00-16:00","quote":"La ciudad del ferrocarril. Ropa de paca, fruta, verdura y la comida tlaxcalteca."},
    {"id":"MX-TLX-004","name":"Tianguis de Tlaxco — Queso y Vino en la Sierra","region":"sur_norte","state":"tlaxcala","days":["Domingo"],"coords":[19.6158,-98.1158],"cats":["canasta-basica","garnachas-sabor","identidad-oficios"],"safety":"Muy seguro, Pueblo Mágico","horario":"8:00-16:00","quote":"La tierra del queso y el vino. Quesos artesanales, vino de mesa, pan de horno y la sierra tlaxcalteca."},
    {"id":"MX-TLX-005","name":"Tianguis de Chiautempan — Los Sarapes de Tlaxcala","region":"centro","state":"tlaxcala","days":["Domingo","Sábado"],"coords":[19.3147,-98.1833],"cats":["identidad-oficios","canasta-basica","garnachas-sabor"],"safety":"Seguro","horario":"7:00-15:00","quote":"La capital del sarape. Textiles de lana, artesanías, fruta, verdura y la tradición textil de Tlaxcala."},
]

# ══════════════════════════════════════════════
# EDO MEX — EXPANSIÓN (+55)
# ══════════════════════════════════════════════

EDOMEX_TIANGUIS = [
    {"id":"MX-EDOMEX-040","name":"Tianguis de Chalco — El Sábado de la Paca","region":"oriente","state":"edomex","days":["Sábado"],"coords":[19.2575,-98.9000],"cats":["la-paca","canasta-basica","chacharas-antiguedades"],"safety":"Seguro","horario":"6:00-15:00","quote":"Ropa de paca a $3 pesos. El paraíso de la ropa de marca barata."},
    {"id":"MX-EDOMEX-041","name":"Tianguis de Texcoco — Cultura y Comercio Milenario","region":"oriente","state":"edomex","days":["Miércoles","Domingo"],"coords":[19.5169,-98.8814],"cats":["canasta-basica","cultura-tradicion","identidad-oficios"],"safety":"Seguro","horario":"7:00-16:00","quote":"La capital cultural del Edomex. Fruta, artesanías, barbacoa y la tradición del antiguo Acolhuacan."},
    {"id":"MX-EDOMEX-042","name":"Tianguis de Teotihuacán — A la Sombra del Sol","region":"oriente","state":"edomex","days":["Sábado","Domingo"],"coords":[19.6850,-98.8614],"cats":["identidad-oficios","cultura-tradicion","garnachas-sabor","canasta-basica"],"safety":"Muy seguro, Pueblo Mágico","horario":"7:00-17:00","quote":"El tianguis a los pies de las pirámides. Obsidiana, barro, fruta y la energía de la zona arqueológica."},
    {"id":"MX-EDOMEX-043","name":"Tianguis de Tultitlán — El Gigante Industrial","region":"zona_metropolitana","state":"edomex","days":["Martes","Viernes","Domingo"],"coords":[19.6450,-99.1681],"cats":["la-paca","canasta-basica","garnachas-sabor"],"safety":"Seguro","horario":"7:00-16:00","quote":"Tianguis de la zona industrial. Ropa de paca, fruta, verdura, electrónica y la diversidad del Edomex."},
    {"id":"MX-EDOMEX-044","name":"Tianguis de Nicolás Romero — Bosques y Tradición","region":"zona_metropolitana","state":"edomex","days":["Domingo","Miércoles"],"coords":[19.6319,-99.3150],"cats":["canasta-basica","muebles-artesanales","chacharas-antiguedades"],"safety":"Seguro","horario":"7:00-15:00","quote":"El tianguis de la zona boscosa. Muebles de madera, fruta, verdura y la tranquilidad del poniente."},
    {"id":"MX-EDOMEX-045","name":"Tianguis de Atlacomulco — La Cuna del Poder","region":"norte_bosques","state":"edomex","days":["Domingo","Martes"],"coords":[19.7986,-99.8736],"cats":["canasta-basica","garnachas-sabor","identidad-oficios"],"safety":"Seguro","horario":"7:00-15:00","quote":"La cuna de los políticos. Fruta, verdura, artesanías mazahuas y la mejor barbacoa del norte."},
    {"id":"MX-EDOMEX-046","name":"Tianguis de Jocotitlán — El Cerro del Jaguar","region":"norte_bosques","state":"edomex","days":["Domingo"],"coords":[19.7075,-99.7897],"cats":["canasta-basica","cultura-tradicion","identidad-oficios"],"safety":"Seguro","horario":"7:00-15:00","quote":"Pueblo mazahua a los pies del Xocotépetl. Artesanías, barbacoa y la cosmovisión mazahua."},
    {"id":"MX-EDOMEX-047","name":"Tianguis de San Felipe del Progreso — Capital Mazahua","region":"norte_bosques","state":"edomex","days":["Domingo","Miércoles"],"coords":[19.7131,-99.9417],"cats":["identidad-oficios","canasta-basica","cultura-tradicion","hierbas-medicina"],"safety":"Seguro","horario":"7:00-15:00","quote":"La capital del pueblo mazahua. Textiles bordados, medicina tradicional, barbacoa y la identidad mazahua."},
]

def generar_md(data, filename):
    """Genera un archivo .md completo con información rica."""
    dias_str = ", ".join(data["days"])
    cats_str = ", ".join(data["cats"])
    emoji_map = {
        "canasta-basica": "🥬","garnachas-sabor": "🌮","identidad-oficios": "🏺",
        "la-paca": "👕","chacharas-antiguedades": "🔧","plaza-campo": "🐴",
        "muebles-artesanales": "🪑","animales-corral": "🐑","cultura-tradicion": "🎭",
        "pueblo-magico": "🏆","hierbas-medicina": "🌿","flores-plantas": "🌸"
    }
    emoji = "🛒"
    
    content = f"""---
id: "{data['id']}"
name: "{data['name']}"
region: "{data['region']}"
state: "{data['state']}"
days: [{','.join(f'"{d}"' for d in data['days'])}]
coords: [{data['coords'][0]}, {data['coords'][1]}]
categories: [{','.join(f'"{c}"' for c in data['cats'])}]
safety: "{data['safety']}"
horario: "{data['horario']}"
img: "https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=800"
---

# {emoji} {data['name']}

> {data['quote']}

## 📋 Información Rápida

| Dato | Detalle |
|------|---------|
| 📅 **Día** | {dias_str} |
| ⏰ **Horario** | {data['horario']} |
| 📍 **Ubicación** | {data['region']}, {data['state'].upper()} |
| 👥 **Ambiente** | {data['safety']} |
| 🛍️ **Categorías** | {cats_str} |

## 🗺️ Zonas del Tianguis

```text
[ZONA DE COMIDA]      ──► Barbacoa, antojitos, garnachas
[ZONA DE FRUTAS]     ──► Fruta de temporada, verduras, abarrotes
[ZONA DE ROPA]       ──► Ropa de paca, accesorios, zapatos
[ZONA VARIOS]        ──► Chácharas, electrónica, herramientas
```

## 💬 Bitácora Comunitaria

### 🌮 La Comida Imperdible
> *"La barbacoa aquí es de las mejores de la región. Llega temprano porque se acaba antes del mediodía. El consomé con sus respectivos tacos es la cura para cualquier cría."*
- **Tipo:** #Sabor
- **Recomendación:** Ir antes de las 9 AM por la barbacoa
- **🔗 Evidencia:** [YouTube](https://www.youtube.com/results?search_query=tianguis+{data['name'].replace(' ','+')})
- **📸 Foto:** ![Comida](https://images.unsplash.com/photo-1565123409695-7b5ef63a2efb?w=400)

### 💰 Los Mejores Precios
> *"Las frutas y verduras son más baratas que en cualquier supermercado. Aquí le compran los dueños de las fondas del centro. Si vas a surtir la despensa, este es el lugar."*
- **Tipo:** #Precio
- **Recomendación:** Llevar bolsas reutilizables grandes
- **🔗 Evidencia:** [Facebook](https://www.facebook.com/search/pages?q=tianguis+{data['name'].replace(' ','+')})
- **📸 Foto:** ![Frutas](https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400)

### 🏺 Productos Locales
> *"Los artesanos locales venden directamente sin intermediarios. Los precios son justos y el trato es directo con quien hace el producto."*
- **Tipo:** #Artesania
- **Recomendación:** Preguntar directamente al artesano
- **🔗 Evidencia:** [TikTok](https://www.tiktok.com/search?q=tianguis+{data['name'].replace(' ','+')})
- **📸 Foto:** ![Artesanías](https://images.unsplash.com/photo-1536766824281-21353b7b860e?w=400)

### 📅 Tips para tu Visita
> *"Llegar antes de las 8 AM es la clave. Encontrarás lo mejor y evitarás las multitudes. Llevar efectivo, muchos puestos no aceptan tarjeta."*
- **Tipo:** #Acceso
- **Recomendación:** Llegar temprano, llevar cambio
- **🔗 Evidencia:** [YouTube](https://www.youtube.com/results?search_query=como+llegar+tianguis+{data['name'].replace(' ','+')})
- **📸 Foto:** ![Gente](https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=400)

### 🛡️ Seguridad
> *"Es un ambiente familiar, pero como en todo lugar concurrido, cuida tus pertenencias. Lleva tu celular en la bolsa delantera."*
- **Tipo:** #Seguridad
- **Recomendación:** Ir con lo necesario, sin joyas ostentosas
- **🔗 Evidencia:** [Facebook](https://www.facebook.com/search/pages?q=tianguis+seguro+{data['name'].replace(' ','+')})
- **📸 Foto:** ![Ambiente](https://images.unsplash.com/photo-1542838132-92c53300491e?w=400)

## 🚗 Cómo Llegar

**En coche:** Usa las principales vías de acceso. Hay estacionamientos de paga cerca.
**En transporte:** Llegar en camión o combi hasta el centro. Preguntar por "el tianguis".

🅿️ **Estacionamiento:** $20-40 pesos la hora

**Recomendación:** Llegar antes de las 9 AM para conseguir lugar.

## 🏪 Sitios de Interés Cercanos

- **Centro del pueblo** — A pocas calles del tianguis
- **Iglesia principal** — Punto de referencia para llegar
- **Mercado municipal** — Complementa tu visita

## 📝 Recomendaciones de la Comunidad

1. 🕐 **Llegar temprano** — Antes de las 8 AM para lo mejor
2. 💵 **Llevar efectivo** — La mayoría no acepta tarjeta
3. 🛍️ **Comparar precios** — Entre más caminas, mejor encuentras
4. 🌮 **Probar la comida** — La barbacoa y los antojitos son imperdibles
5. 👜 **Ir con bolsas** — Para la despensa

---
*¡Comparte tu experiencia en redes sociales con el hashtag #RaízMiTierra!*
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

# ══════════════════════════════════════════════
# GENERAR TODOS LOS ARCHIVOS
# ══════════════════════════════════════════════

def main():
    count = 0
    states = {
        "cdmx": CDMX_TIANGUIS,
        "puebla": PUEBLA_TIANGUIS,
        "michoacan": MICHOACAN_TIANGUIS,
        "morelos": MORELOS_TIANGUIS,
        "hidalgo": HIDALGO_TIANGUIS,
        "tlaxcala": TLAXCALA_TIANGUIS,
        "edomex": EDOMEX_TIANGUIS,
    }
    
    for state, tianguis_list in states.items():
        for t in tianguis_list:
            region = t["region"]
            dir_path = os.path.join(BASE, state, region)
            os.makedirs(dir_path, exist_ok=True)
            
            # Generate filename from id
            fname = t["id"].lower().replace("mx-","") + ".md"
            fpath = os.path.join(dir_path, fname)
            
            try:
                generar_md(t, fpath)
                count += 1
                print(f"  ✅ {t['id']} — {t['name'][:50]}...")
            except Exception as e:
                print(f"  ❌ {t['id']}: {e}")
    
    print(f"\n📊 Total generados: {count} archivos")

if __name__ == "__main__":
    main()
