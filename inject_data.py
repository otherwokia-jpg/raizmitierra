#!/usr/bin/env python3
"""
Inyecta los datos generados (2026-2030) en el HTML de RaízMiTierra.
Reemplaza window.RAIZ_DATA en public/index.html y dist/index.html
"""
import json, re, os

YEARS_TO_INJECT = 5  # How many years to include

def inject_data(html_path, json_path, output_path=None):
    if output_path is None:
        output_path = html_path
    
    # Load generated data
    with open(json_path, 'r', encoding='utf-8') as f:
        new_data = json.load(f)
    
    # Load HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Find RAIZ_DATA boundaries
    start_marker = 'window.RAIZ_DATA='
    start_idx = html.find(start_marker)
    end_idx = html.find('</script>', start_idx)
    
    if start_idx == -1 or end_idx == -1:
        print(f'ERROR: Could not find RAIZ_DATA in {html_path}')
        return False
    
    # Serialize new data as compact JSON (no spaces, no indentation)
    new_json = json.dumps(new_data, ensure_ascii=False, separators=(',', ':'))
    
    # Update meta to reflect multi-year
    new_data['meta']['years_covered'] = ['2026','2027','2028','2029','2030']
    new_data['meta']['version'] = 'v5yr-20260524'
    new_data['meta']['total_festivals_5yr'] = sum(len(l.get('festividades',[])) for l in (new_data['lugares'] if isinstance(new_data['lugares'], list) else list(new_data['lugares'].values())))
    
    # Re-serialize with updated meta
    new_json = json.dumps(new_data, ensure_ascii=False, separators=(',', ':'))
    
    # Build replacement
    replacement = f'window.RAIZ_DATA={new_json};'
    
    # Replace
    old_chunk = html[start_idx:end_idx + len('</script>')]
    new_chunk = replacement + '</script>'
    html = html.replace(old_chunk, new_chunk, 1)
    
    # Write
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    old_size = os.path.getsize(html_path)
    new_size = len(html.encode('utf-8'))
    fest_count = new_data['meta']['total_festivals_5yr']
    lugar_count = len(new_data['lugares']) if isinstance(new_data['lugares'], list) else len(new_data['lugares'])
    
    print(f'✅ {html_path}')
    print(f'   Tamaño: {old_size/1024:.0f}KB → {new_size/1024:.0f}KB')
    print(f'   {lugar_count} lugares, {fest_count} festivales (2026-2030)')
    print(f'   {new_data["meta"]["years_covered"]}')
    return True

if __name__ == '__main__':
    base = '/home/home/raizmitierra'
    inject_data(f'{base}/public/index.html', f'{base}/public/data_2026_2030.json')
    inject_data(f'{base}/dist/index.html', f'{base}/public/data_2026_2030.json')
    print('\n✅ HTMLs actualizados con datos 2026-2030')
