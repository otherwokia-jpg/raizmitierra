#!/usr/bin/env python3
"""Fix: year-collapse, bitacora-collapsed, modal-scroll-top"""
import datetime
files = ['public/index.html', 'dist/index.html']

for fp in files:
    with open(fp, 'r') as f:
        html = f.read()
    
    changes = 0
    
    # 1. FIX MODAL SCROLL: Remove the scrollIntoView to userReviews
    old_scroll = '    // Scroll automático a reseñas de la comunidad\n    setTimeout(() => {\n        const el = document.getElementById(\'userReviews-\' + t.id);\n        if (el) el.scrollIntoView({ behavior: \'smooth\', block: \'start\' });\n    }, 500);'
    if old_scroll in html:
        html = html.replace(old_scroll, '    // Modal opens at top — scroll handled by CSS', 1)
        changes += 1
        print(f'  [{fp}] Fixed: removed scroll-to-bottom')
    else:
        print(f'  ⚠️ [{fp}] scrollIntoView not found')
    
    # 2. CHANGE BITACORA: collapsed by default (remove "open" class from collapse-body)
    old_bitacora = '<div class="collapse-body open" id="collapse-bitacora">'
    new_bitacora = '<div class="collapse-body" id="collapse-bitacora">'
    if old_bitacora in html:
        html = html.replace(old_bitacora, new_bitacora, 1)
        changes += 1
        print(f'  [{fp}] Bitácora default collapsed')
    
    # Also remove "open" from the bitacora icon
    old_bitacora_icon = '<span class="collapse-icon open">▼</span>'
    new_bitacora_icon = '<span class="collapse-icon">▼</span>'
    # Only replace for bitacora (first occurrence after bitacora header)
    bitacora_header = html.find('modalSection-bitacora')
    bitacora_icon_pos = html.find(old_bitacora_icon, bitacora_header)
    if bitacora_icon_pos > 0:
        # Replace ONLY this occurrence
        html = html[:bitacora_icon_pos] + new_bitacora_icon + html[bitacora_icon_pos + len(old_bitacora_icon):]
        changes += 1
        print(f'  [{fp}] Bitácora icon collapsed')
    
    # 3. MAKE YEAR GROUPS INDIVIDUALLY COLLAPSIBLE
    # Replace the year-group rendering code in the IIFE
    old_year_render = '''                        return years.map(year => `
                        <div class="fest-year-group">
                            <div class="fest-year-label">📆 ${year}</div>
                            ${groups[year].map(f => `
                            <div class="fest-item">
                                <div class="fest-nombre">${f.nombre}</div>
                                <div class="fest-fecha">📅 ${f.fecha_inicio || ''}${f.fecha_fin && f.fecha_fin !== f.fecha_inicio ? ' — '+f.fecha_fin : ''}</div>
                                ${f.tipo ? `<span class=\"fest-badge ${f.tipo}\">${FEST_EMOJI[f.tipo]||'🎉'} ${f.tipo.replace(/-/g,' ')}</span>` : ''}
                                ${f.descripcion ? `<div class="fest-desc">${f.descripcion}</div>` : ''}
                                ${f.link ? `<a class="fest-link" href="${f.link}" target="_blank" rel="noopener">🔗 Más información</a>` : ''}
                            </div>`).join('')}
                        </div>`).join('');'''
    
    new_year_render = '''                        return years.map(year => `
                        <div class="fest-year-group">
                            <div class="fest-year-toggle" onclick="toggleYearGroup(this)">
                                <span class="fest-year-label">📆 ${year}</span>
                                <span class="collapse-icon ${year === '2026' ? 'open' : ''}">▼</span>
                            </div>
                            <div class="fest-year-body ${year === '2026' ? 'open' : ''}">
                                ${groups[year].map(f => `
                                <div class="fest-item">
                                    <div class="fest-nombre">${f.nombre}</div>
                                    <div class="fest-fecha">📅 ${f.fecha_inicio || ''}${f.fecha_fin && f.fecha_fin !== f.fecha_inicio ? ' — '+f.fecha_fin : ''}</div>
                                    ${f.tipo ? `<span class=\"fest-badge ${f.tipo}\">${FEST_EMOJI[f.tipo]||'🎉'} ${f.tipo.replace(/-/g,' ')}</span>` : ''}
                                    ${f.descripcion ? `<div class="fest-desc">${f.descripcion}</div>` : ''}
                                    ${f.link ? `<a class="fest-link" href="${f.link}" target="_blank" rel="noopener">🔗 Más información</a>` : ''}
                                </div>`).join('')}
                            </div>
                        </div>`).join('');'''
    
    if old_year_render in html:
        html = html.replace(old_year_render, new_year_render, 1)
        changes += 1
        print(f'  [{fp}] Year groups now individually collapsible')
    else:
        print(f'  ⚠️ [{fp}] Year render code not found')
    
    # 4. Add CSS for year-toggle and year-body
    year_css = '\n    /* Year toggle collapsible */\n    .fest-year-toggle{display:flex;align-items:center;justify-content:space-between;cursor:pointer;padding:6px 8px;margin-bottom:4px;background:var(--papel);border-radius:6px;user-select:none;-webkit-tap-highlight-color:transparent}\n    .fest-year-toggle:active{background:var(--borde)}\n    .fest-year-body{max-height:0;overflow:hidden;transition:max-height .3s ease}\n    .fest-year-body.open{max-height:20000px}\n    .fest-year-toggle .collapse-icon{font-size:.65rem;transition:transform .25s ease}\n    .fest-year-toggle .collapse-icon.open{transform:rotate(180deg)}'
    
    # Insert before .collapsible sections CSS comment
    css_marker = '    /* Collapsible sections in modal */'
    if css_marker in html:
        html = html.replace(css_marker, year_css + '\n' + css_marker, 1)
        changes += 1
        print(f'  [{fp}] Added year-toggle CSS')
    else:
        print(f'  ⚠️ [{fp}] CSS marker not found')
    
    # 5. Add toggleYearGroup function
    toggle_fn = '\nfunction toggleYearGroup(el) {\n    const body = el.nextElementSibling;\n    const icon = el.querySelector(\'.collapse-icon\');\n    if(body) {\n        body.classList.toggle(\'open\');\n        if(icon) icon.classList.toggle(\'open\');\n    }\n}\n'
    
    fn_marker = 'function toggleCollapse'
    if fn_marker in html:
        idx = html.find(fn_marker)
        html = html[:idx] + toggle_fn + html[idx:]
        changes += 1
        print(f'  [{fp}] Added toggleYearGroup function')
    else:
        print(f'  ⚠️ [{fp}] toggleCollapse not found')
    
    # 6. Also add modal top-reset: after setting body.innerHTML
    # Find the line after body.innerHTML = `...` ends (line 1058-1059)
    old_review_form = '        </div>\n    `;\n    document.getElementById(\'modalOverlay\').classList.add(\'show\');\n    document.getElementById(\'detailModal\').classList.add(\'show\');'
    new_review_form = '        </div>\n    `;\n    document.getElementById(\'detailModal\').scrollTop = 0;\n    document.getElementById(\'modalOverlay\').classList.add(\'show\');\n    document.getElementById(\'detailModal\').classList.add(\'show\');'
    if old_review_form in html:
        html = html.replace(old_review_form, new_review_form, 1)
        changes += 1
        print(f'  [{fp}] Added scrollTop=0 on modal open')
    else:
        print(f'  ⚠️ [{fp}] Modal open code not found')
    
    if changes > 0:
        with open(fp, 'w') as f:
            f.write(html)
        print(f'  ✅ {fp}: {changes} cambios')
    else:
        print(f'  ❌ {fp}: sin cambios')

print('\n✅ Todos los arreglos aplicados')
