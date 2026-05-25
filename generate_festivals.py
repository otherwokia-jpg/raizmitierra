#!/usr/bin/env python3
"""
Generador de festivales 2027-2030 para RaízMiTierra.
Basado en el análisis de 53 festivales únicos en 212 lugares.
"""
import json, re, copy
from datetime import date, timedelta

# ─── Cargar datos actuales ───
with open('public/index.html') as f:
    html = f.read()

start = html.find('window.RAIZ_DATA=')
end = html.find('</script>', start)
raw_js = html[start:end].strip()
raw_js = raw_js[len('window.RAIZ_DATA='):]
data = json.loads(raw_js, strict=False)

lugares = data['lugares']
print(f'Lugares cargados: {len(lugares)}')
print(f'Con festivales: {sum(1 for l in lugares if l.get("festividades"))}')
print(f'Festivales actuales: {sum(len(l.get("festividades",[])) for l in lugares)}')

# ─── Calcular fechas flotantes ───
def last_sunday_of_september(year):
    """Huey Atlixcáyotl: último domingo de septiembre"""
    d = date(year, 9, 30)
    # Go back to Sunday
    days_ahead = d.weekday()  # Monday=0, Sunday=6
    d = d - timedelta(days=(days_ahead - 6) % 7)
    return d

def get_floating_date(event_name, base_mm_dd, year):
    """
    Para eventos con fecha flotante, calcula la fecha correcta del año.
    Si el evento es de fecha fija, devuelve la misma mm-dd.
    """
    event_lower = event_name.lower()
    
    # Huey Atlixcáyotl: último domingo de septiembre
    if 'huey' in event_lower and 'atlixc' in event_lower:
        d = last_sunday_of_september(year)
        return f'{d.month:02d}-{d.day:02d}', f'{d.month:02d}-{d.day:02d}'
    
    # Para todo lo demás, mantener fecha fija
    return base_mm_dd, base_mm_dd

# ─── Generar nombres con año ───
def make_year_name(name, source_year, target_year):
    """Actualiza referencias de año/edición en el nombre del festival."""
    new_name = name
    
    # Step 1: Handle edition numbers that are NOT years (e.g. "Edición 169" → "170")
    def increment_edition(m):
        prefix = m.group(1)
        num = int(m.group(2))
        year_diff = target_year - source_year
        return f'{prefix}{num + year_diff}'
    
    new_name = re.sub(r'([Ee]dici[oó]n\s+)(\d+)', increment_edition, new_name)
    
    # Step 2: Replace all 4-digit years (handles standalone years AND edition-years)
    new_name = re.sub(r'\b(?:19|20)\d{2}\b', str(target_year), new_name)
    
    return new_name

# ─── Generar festivales para todos los años ───
YEARS = [2026, 2027, 2028, 2029, 2030]
total_added = 0
total_places_updated = 0

for lugar in lugares:
    if not lugar.get('festividades'):
        continue
    
    original_fests = lugar['festividades']
    new_fests = []
    
    for year in YEARS:
        for fest in original_fests:
            # Solo usar 2026 como fuente, generar los demás años
            fi = fest['fecha_inicio']
            if fi[:4] != '2026':
                continue
            
            mm_dd_start = fi[5:]
            mm_dd_end = fest.get('fecha_fin', fi)[5:]
            
            # Obtener fecha flotante o fija
            new_mm_start, new_mm_end = get_floating_date(
                fest['nombre'], mm_dd_start, year
            )
            
            new_fest = copy.deepcopy(fest)
            new_fest['fecha_inicio'] = f'{year}-{new_mm_start}'
            new_fest['fecha_fin'] = f'{year}-{new_mm_end}'
            new_fest['nombre'] = make_year_name(fest['nombre'], 2026, year)
            
            new_fests.append(new_fest)
    
    lugar['festividades'] = new_fests
    total_places_updated += 1
    total_added += len(new_fests)

print(f'\nLugares actualizados: {total_places_updated}')
print(f'Festivales totales generados: {total_added}')

# ─── Estadísticas finales ───
print('\n=== ESTADÍSTICAS FINALES ===')
years_coverage = set()
for lugar in lugares:
    if lugar.get('festividades'):
        for f in lugar['festividades']:
            fi = f.get('fecha_inicio','')
            if fi: years_coverage.add(fi[:4])
print(f'Años cubiertos: {sorted(years_coverage)}')

fest_per_place = {}
for lugar in lugares:
    if lugar.get('festividades'):
        n = len(lugar['festividades'])
        fest_per_place[n] = fest_per_place.get(n,0)+1
print(f'Festivales por lugar: {dict(sorted(fest_per_place.items()))}')

# ─── Verificar que las fechas sean válidas ───
from datetime import datetime
invalid_dates = 0
for lugar in lugares:
    if lugar.get('festividades'):
        for f in lugar['festividades']:
            try:
                datetime.strptime(f['fecha_inicio'], '%Y-%m-%d')
                if f.get('fecha_fin'):
                    datetime.strptime(f['fecha_fin'], '%Y-%m-%d')
            except:
                invalid_dates += 1
                print(f'  Fecha inválida: {f["nombre"]} -> {f["fecha_inicio"]}')
print(f'Fechas inválidas: {invalid_dates}')

# ─── Verificar muestra ───
print('\n=== MUESTRA: Tepoztlán ===')
for lugar in lugares:
    if 'Tepoztlán' in lugar.get('name','') and not 'Mercado' in lugar.get('name',''):
        for f in lugar.get('festividades',[]):
            print(f'  {f["fecha_inicio"]} -> {f.get("fecha_fin","")} | {f["nombre"][:55]}')
        break

print('\n=== MUESTRA: Tianguis de Coyoacán ===')
for lugar in lugares:
    if 'Coyoacán' in lugar.get('name','') and 'Bazar' in lugar.get('name',''):
        for f in lugar.get('festividades',[]):
            print(f'  {f["fecha_inicio"]} -> {f.get("fecha_fin","")} | {f["nombre"][:55]}')
        break

# ─── Guardar datos actualizados ───
with open('public/data_2026_2030.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=None)
print('\n✅ Datos guardados en public/data_2026_2030.json')
