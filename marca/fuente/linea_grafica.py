from base import Doc, logo, lockup, icon, arcs, partial, ACCENT, LOGO_PATHS

d = Doc('Línea gráfica', 'LG')
A = 'assets/'


def divider(num, title, sub):
    d.page(f'''{arcs(1250, 450, (230, 390, 560, 740), .32, thick=820)}
<div class="d-body" style="justify-content:flex-end;padding-bottom:40px">
  <span class="d-num" style="font-size:22px">{num}</span>
  <h1 class="d-h1" style="font-size:150px;margin-top:18px">{title}</h1>
  <p class="d-lead" style="margin-top:28px">{sub}</p>
</div>''', title)


# 01 — Portada -----------------------------------------------------------
d.page(f'''{arcs(1180, 470, (250, 420, 600), .34, thick=760)}
<div class="d-body" style="justify-content:space-between">
  <div>{lockup(54)}</div>
  <div>
    <span class="d-k" style="font-size:18px">Manual de identidad · Parte 1</span>
    <h1 class="d-h1" style="font-size:170px;margin-top:20px">Línea<br>gráfica</h1>
    <p class="d-lead" style="margin-top:30px">El sistema visual de We Brand U: cómo se ve la marca en cada canal.</p>
  </div>
  <div class="d-cover-meta"><span>Versión<b>1.0</b></span><span>Año<b>2026</b></span><span>Alcance<b>Equipo, pods y proveedores</b></span></div>
</div>''', bare=True)

# 02 — Índice --------------------------------------------------------------
toc = [('01', 'Logo', '04'), ('02', 'Color', '11'), ('03', 'Tipografía', '16'), ('04', 'Composición', '20'),
       ('05', 'Iconografía e ilustración', '25'), ('06', 'Componentes y movimiento', '29'),
       ('07', 'Aplicaciones', '33'), ('08', 'Checklist', '41')]
d.page(f'''<div class="d-body">
  <span class="d-k">Contenido</span>
  <h2 class="d-h2" style="margin:14px 0 44px">Índice</h2>
  <div class="d-toc">{''.join(f'<div><span>{a}</span><span>{b}</span><span>{c}</span></div>' for a, b, c in toc)}</div>
</div>''', 'Índice')

# 03 — Principios ----------------------------------------------------------
pr = [('Negro pleno', 'El fondo es negro puro. La marca vive en la oscuridad y el verde se enciende sobre ella.'),
      ('Losas', 'El contenido se apoya en losas charcoal de radio alto, apenas levantadas del negro. Nunca en tarjetas sueltas.'),
      ('Un solo acento', 'Un único verde, #00CA71. Todo lo demás es negro, charcoal, blanco y grises.'),
      ('Escala extrema', 'Titulares grandes y pesados; cuerpo chico. El salto entre ambos es deliberado.'),
      ('Arcos orbitales', 'Arcos finos verdes cruzan las losas como órbitas. Es el motivo que une todas las piezas.'),
      ('Movimiento con sentido', 'Lo que se mueve sale del dibujo: nodos que se encienden, curvas que se trazan. Nunca un efecto aplicado encima.')]
d.page(f'''<div class="d-body">
  <span class="d-k">Introducción</span>
  <h2 class="d-h2" style="margin:14px 0 18px">Un sistema, no piezas sueltas</h2>
  <p class="d-lead" style="margin-bottom:40px">Seis principios explican cualquier decisión visual de la marca. Si una pieza no responde a alguno, no es We Brand U.</p>
  <div class="d-grid d-g3">{''.join(f'<div class="d-card"><span class="d-num">0{i}</span><h3 class="d-h4" style="margin:12px 0 10px">{t}</h3><p class="d-small">{x}</p></div>' for i, (t, x) in enumerate(pr, 1))}</div>
</div>''', 'Principios')

# ============================ 01 LOGO ======================================
divider('01', 'Logo', 'El símbolo U, sus versiones, su espacio y lo que nunca se le hace.')

d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-slab" style="height:640px;display:grid;place-items:center">{arcs(380, 320, (180, 300), .28, glow=True, w=760, h=640)}<div style="position:relative">{logo(300)}</div></div>
  <div class="d-col">
    <span class="d-k">Símbolo principal</span>
    <h2 class="d-h2">La U</h2>
    <p class="d-p">El símbolo es una U construida con formas geométricas simples: un brazo izquierdo completo, una curva de ancho constante y un brazo derecho partido.</p>
    <p class="d-p">El brazo derecho se abre en un bloque superior, dos cuñas que apuntan hacia adentro y una punta pequeña. Esa ruptura es el rasgo que lo hace reconocible: una forma que se está construyendo.</p>
    <p class="d-p">Se usa siempre como dibujo vectorial. Nunca se redibuja, se recorta ni se reconstruye a mano.</p>
  </div>
</div></div>''', 'Logo')

grid = ''.join(f'<line x1="{x}" y1="-40" x2="{x}" y2="770" stroke="{ACCENT}" stroke-opacity=".35" stroke-width="2" stroke-dasharray="8 8"/>' for x in (0, 175, 430, 610))
grid += ''.join(f'<line x1="-40" y1="{y}" x2="650" y2="{y}" stroke="{ACCENT}" stroke-opacity=".35" stroke-width="2" stroke-dasharray="8 8"/>' for y in (0, 120, 425, 730))
grid += f'<circle cx="305" cy="425" r="305" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/><circle cx="302.5" cy="432" r="127.5" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/>'
d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-slab" style="height:640px;display:grid;place-items:center">
    <svg viewBox="-80 -80 770 890" width="440" height="510"><g fill="{ACCENT}" fill-opacity=".9">{LOGO_PATHS}</g>{grid}</svg>
  </div>
  <div class="d-col">
    <span class="d-k">Construcción</span>
    <h2 class="d-h2">Proporciones fijas</h2>
    <p class="d-p">El símbolo se dibuja sobre una caja de 610 × 730 unidades.</p>
    <table class="d-table">
      <tr><th>Elemento</th><th>Medida</th></tr>
      <tr><td>Ancho del brazo izquierdo (x)</td><td>175 u · 29 % del ancho</td></tr>
      <tr><td>Radio exterior de la curva</td><td>305 u (la mitad del ancho)</td></tr>
      <tr><td>Radio interior de la curva</td><td>127,5 u</td></tr>
      <tr><td>Alto del bloque superior derecho</td><td>120 u en el borde exterior</td></tr>
      <tr><td>Cuñas</td><td>Dos de 95 u de largo y una punta de 40 u</td></tr>
    </table>
    <p class="d-small">La medida x —el ancho del brazo izquierdo— es la unidad que define el espacio de seguridad.</p>
  </div>
</div></div>''', 'Logo')

d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-slab" style="height:640px;display:grid;place-items:center">
    <div style="position:relative;padding:64px;border:2px dashed rgba(0,202,113,.45)">
      {logo(250)}
      <span class="d-small d-acc" style="position:absolute;top:18px;left:50%;transform:translateX(-50%)">x</span>
      <span class="d-small d-acc" style="position:absolute;bottom:18px;left:50%;transform:translateX(-50%)">x</span>
      <span class="d-small d-acc" style="position:absolute;left:24px;top:50%">x</span>
      <span class="d-small d-acc" style="position:absolute;right:24px;top:50%">x</span>
    </div>
  </div>
  <div class="d-col">
    <span class="d-k">Espacio y tamaño</span>
    <h2 class="d-h2">Aire alrededor</h2>
    <p class="d-p">Ningún texto, borde o imagen entra en el espacio de seguridad: una medida x —el ancho del brazo izquierdo— libre en los cuatro lados.</p>
    <table class="d-table">
      <tr><th>Soporte</th><th>Tamaño mínimo del símbolo</th></tr>
      <tr><td>Pantalla</td><td>24 px de alto</td></tr>
      <tr><td>Favicon / ícono de app</td><td>16 px, sin el nombre</td></tr>
      <tr><td>Impresión</td><td>8 mm de alto</td></tr>
      <tr><td>Bloque con nombre</td><td>Símbolo de 20 px de alto o más</td></tr>
    </table>
  </div>
</div></div>''', 'Logo')

vers = [('#0B0B0B', ACCENT, 'Principal', 'Verde sobre negro o charcoal. Es la versión por defecto.'),
        ('#0B0B0B', '#FFFFFF', 'Blanco', 'Cuando el verde ya está ocupado por un CTA en la misma pantalla.'),
        (ACCENT, '#0B0B0B', 'Sobre verde', 'Charcoal sobre verde. Solo en superficies verdes, como Out of the Box.'),
        ('#FFFFFF', '#0B0B0B', 'Una tinta', 'Charcoal sobre blanco. Solo para impresión a un color o sellos.')]
d.page(f'''<div class="d-body">
  <span class="d-k">Versiones</span>
  <h2 class="d-h2" style="margin:14px 0 36px">Cuatro versiones, nada más</h2>
  <div class="d-grid d-g4">{''.join(f'<div class="d-col"><div style="background:{bg};border-radius:22px;height:330px;display:grid;place-items:center;border:1px solid rgba(255,255,255,.08)">{logo(150, fg)}</div><h3 class="d-h4">{t}</h3><p class="d-small">{x}</p></div>' for bg, fg, t, x in vers)}</div>
</div>''', 'Logo')

d.page(f'''<div class="d-body">
  <span class="d-k">Bloque de marca</span>
  <h2 class="d-h2" style="margin:14px 0 36px">Símbolo + nombre</h2>
  <div class="d-grid d-g2" style="align-items:stretch">
    <div class="d-slab" style="height:330px;display:grid;place-items:center">{lockup(110)}</div>
    <div class="d-slab" style="height:330px;display:grid;place-items:center;background:{ACCENT}">{lockup(110, '#0B0B0B', '#0B0B0B')}</div>
  </div>
  <div class="d-grid d-g3" style="margin-top:30px">
    <div class="d-card"><h3 class="d-h4">Nombre</h3><p class="d-small" style="margin-top:8px">“We Brand U” en Inter SemiBold, a la altura de la cuarta parte superior del símbolo.</p></div>
    <div class="d-card"><h3 class="d-h4">Separación</h3><p class="d-small" style="margin-top:8px">Un tercio del alto del símbolo entre la U y el nombre. Siempre en una línea.</p></div>
    <div class="d-card"><h3 class="d-h4">Cuándo usarlo</h3><p class="d-small" style="margin-top:8px">Footer, papelería, firmas y portadas. Dentro del sitio, el símbolo solo basta.</p></div>
  </div>
</div>''', 'Logo')

wrong = [
    (f'<div style="transform:rotate(-18deg)">{logo(120)}</div>', 'No rotar'),
    (f'<div style="transform:scaleX(1.45)">{logo(110)}</div>', 'No deformar'),
    (f'<svg viewBox="0 0 610 730" width="120" height="144" fill="none" stroke="{ACCENT}" stroke-width="14">{LOGO_PATHS}</svg>', 'No usar en contorno'),
    (logo(120, '#6B6B6B'), 'No cambiar el color'),
    (f'<div style="filter:drop-shadow(14px 16px 0 #006337)">{logo(120)}</div>', 'No agregar sombras'),
    (f'<div style="background:#E9E9E9;padding:40px;border-radius:14px">{logo(90)}</div>', 'No usar sobre fondos claros sin control'),
    (f'<div style="display:flex;gap:10px;align-items:center">{logo(70)}<span style="font-size:28px;font-style:italic;font-weight:900">WEBRANDU</span></div>', 'No cambiar el nombre'),
    (f'<div style="display:grid;place-items:center;position:relative">{logo(120)}<span style="position:absolute;font-size:22px">Sale!</span></div>', 'No poner nada encima'),
]
d.page(f'''<div class="d-body">
  <span class="d-k">Usos incorrectos</span>
  <h2 class="d-h2" style="margin:14px 0 32px">Lo que nunca se hace</h2>
  <div class="d-grid d-g4">{''.join(f'<div class="d-col" style="gap:12px"><div class="d-slab d-x" style="height:250px;display:grid;place-items:center">{w}</div><span class="d-dont">✕ {t}</span></div>' for w, t in wrong)}</div>
</div>''', 'Logo')

# ============================ 02 COLOR =====================================
divider('02', 'Color', 'Negro, charcoal, blanco y un solo verde. Nada más.')

sw = [('#000000', 'Black', '--black', '0 0 0', 'Fondo de página', '#fff'),
      ('#0B0B0B', 'Slab', '--slab', '11 11 11', 'Losas, menú, botones', '#fff'),
      ('#0E0E0E', 'Piece', '--piece', '14 14 14', 'Piezas dentro de la losa', '#fff'),
      ('#00CA71', 'Accent', '--accent', '0 202 113', 'Único acento', '#0B0B0B'),
      ('#006337', 'Accent Dark', '--accent-dark', '0 99 55', 'Trazos y arcos oscuros', '#fff'),
      ('#FFFFFF', 'White', '--text', '255 255 255', 'Titulares y texto', '#0B0B0B'),
      ('#C9C9C9', 'Body', '--body', '201 201 201', 'Texto de cuerpo', '#0B0B0B'),
      ('#6B6B6B', 'Dim', '--dim', '107 107 107', 'Labels y datos secundarios', '#fff')]
d.page(f'''<div class="d-body">
  <span class="d-k">Paleta</span>
  <h2 class="d-h2" style="margin:14px 0 32px">Ocho colores con nombre</h2>
  <div class="d-grid d-g4">{''.join(f'<div class="d-sw" style="background:{h};color:{t}"><b>{n}</b><span>{h}<br>RGB {r}<br>{tok}<br>{u}</span></div>' for h, n, tok, r, u, t in sw)}</div>
</div>''', 'Color')

d.page(f'''<div class="d-body">
  <span class="d-k">Proporción</span>
  <h2 class="d-h2" style="margin:14px 0 18px">El verde se gana su lugar</h2>
  <p class="d-lead" style="margin-bottom:36px">En cualquier pantalla o pieza, el verde ocupa poco. Por eso, cuando aparece, se ve.</p>
  <div style="display:flex;height:120px;border-radius:22px;overflow:hidden;border:1px solid rgba(255,255,255,.08)">
    <div style="flex:62;background:#000;display:flex;align-items:flex-end;padding:16px" class="d-small">Black 62 %</div>
    <div style="flex:24;background:#0B0B0B;display:flex;align-items:flex-end;padding:16px" class="d-small">Slab 24 %</div>
    <div style="flex:9;background:#fff;color:#0B0B0B;display:flex;align-items:flex-end;padding:16px" class="d-small">White 9 %</div>
    <div style="flex:5;background:{ACCENT};color:#0B0B0B;display:flex;align-items:flex-end;padding:16px" class="d-small">5 %</div>
  </div>
  <div class="d-grid d-g3" style="margin-top:36px">
    <div class="d-card"><h3 class="d-h4">Un verde sólido por pantalla</h3><p class="d-small" style="margin-top:8px">Las superficies verdes sólidas se reservan para la acción principal. El resto del verde son trazos, brillos e íconos.</p></div>
    <div class="d-card"><h3 class="d-h4">Ningún otro color</h3><p class="d-small" style="margin-top:8px">Sin violetas, azules, rojos ni degradés de colores ajenos. Ni siquiera en un detalle.</p></div>
    <div class="d-card"><h3 class="d-h4">Texto sobre verde</h3><p class="d-small" style="margin-top:8px">Sobre verde, el texto va en Slab (#0B0B0B). Nunca blanco sobre verde.</p></div>
  </div>
</div>''', 'Color')

alph = [('.16', 'Hairline', 'Borde de tarjetas y separadores'), ('.20', 'Chip', 'Borde de chips'),
        ('.30', 'Field', 'Borde de campos de formulario'), ('.32', 'Mid', 'Tarjetas laterales'),
        ('.50', 'Strong', 'Borde de la pieza activa'), ('.22', 'Glow', 'Resplandor de CTA y menú'),
        ('.14', 'Glow soft', 'Fondo del ítem seleccionado'), ('.28', 'Track', 'Pista de sliders (sobre Accent Dark)')]
d.page(f'''<div class="d-body">
  <span class="d-k">Transparencias</span>
  <h2 class="d-h2" style="margin:14px 0 18px">El verde a baja opacidad</h2>
  <p class="d-lead" style="margin-bottom:32px">Los bordes son verdes, no grises. Cada opacidad tiene un uso y un nombre.</p>
  <div class="d-grid d-g4">{''.join(f'<div class="d-slab" style="padding:24px;height:180px;display:flex;flex-direction:column;justify-content:space-between"><div style="height:56px;border-radius:14px;border:2px solid rgba(0,202,113,{a});background:rgba(0,202,113,{float(a)/3:.3f})"></div><div><b style="font-size:18px">{n} · {a}</b><p class="d-micro" style="margin-top:6px">{u}</p></div></div>' for a, n, u in alph)}</div>
</div>''', 'Color')

grays = [('#E9E9E9', 'Placeholder', 'Espacio reservado para imágenes'), ('#BDBDBD', 'Chip text', 'Texto de opciones'),
         ('#8A8A8A', 'Hover', 'Label apagado al pasar el mouse'), ('#5E5E5E', 'Field placeholder', 'Texto de ayuda de campos'),
         ('#5A5A5A', 'Ghost', 'Labels inactivos'), ('#4A4A4A', 'Icon hover', 'Íconos al pasar el mouse'),
         ('#2E2E2E', 'Icon', 'Íconos inactivos del menú'), ('#151515', 'Card', 'Tarjetas de trabajos')]
d.page(f'''<div class="d-body">
  <span class="d-k">Grises funcionales</span>
  <h2 class="d-h2" style="margin:14px 0 18px">Grises con un trabajo</h2>
  <p class="d-lead" style="margin-bottom:32px">No son colores de marca: son estados. Se usan solo para lo que dice su nombre.</p>
  <div class="d-grid d-g4">{''.join(f'<div class="d-col" style="gap:10px"><div style="height:120px;border-radius:18px;background:{h};border:1px solid rgba(255,255,255,.08)"></div><b style="font-size:17px">{n}</b><span class="d-micro">{h} · {u}</span></div>' for h, n, u in grays)}</div>
</div>''', 'Color')

# ============================ 03 TIPOGRAFÍA ================================
divider('03', 'Tipografía', 'Una familia, dos estilos. El contraste lo hace el tamaño.')

d.page(f'''<div class="d-body"><div class="d-split d-split--even">
  <div class="d-col">
    <span class="d-k">Familia única</span>
    <h2 style="font-size:210px;line-height:1;margin:0">Inter</h2>
    <p class="d-p">Inter es la única familia de la marca, en pantalla y en impresión. Se usan solo dos estilos; ningún otro peso se carga ni se aplica.</p>
  </div>
  <div class="d-col" style="gap:26px">
    <div class="d-slab" style="padding:34px">
      <span class="d-k">Inter SemiBold · 600</span>
      <p style="font-size:44px;line-height:1.15;margin:14px 0 10px">Three months. Then it’s yours.</p>
      <p class="d-small">Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Ññ Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz<br>0123456789 .,:;’“”—&amp;%+#</p>
      <p class="d-micro" style="margin-top:12px">Por defecto para todo: titulares, cuerpo, labels y botones.</p>
    </div>
    <div class="d-slab" style="padding:34px">
      <span class="d-k">Inter Black Italic · 900</span>
      <p class="d-it" style="font-size:44px;line-height:1.15;margin:14px 0 10px">“Independent, not dependent.”</p>
      <p class="d-small d-it">Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt</p>
      <p class="d-micro" style="margin-top:12px">Solo para citas de partners y su firma. En ningún otro lugar.</p>
    </div>
  </div>
</div></div>''', 'Tipografía')

scale = [('Display', 154, 46, 1.2, 'Titular del Hero'), ('Display 2', 107, 40, 1.22, 'Titulares de página y cierre'),
         ('Title', 51, 20, 1.25, 'Títulos de sección'), ('Lead', 31, 15, 1.25, 'Nombres de servicio'),
         ('UI large', 21, 11, 1.25, 'Opciones destacadas'), ('UI', 20, 12, 1, 'Botones, campos, cuerpo de artículo'),
         ('Body large', 17.5, 13, 1.5, 'Párrafos y bajadas'), ('Body', 16, 11.5, 1.45, 'Descripciones'),
         ('Small', 13, 11.5, 1.3, 'Citas, labels'), ('Micro', 12, 10, 1.3, 'Datos secundarios')]
rows = ''.join(
    f'<div style="display:grid;grid-template-columns:150px 1fr 230px 240px;align-items:baseline;gap:20px;padding:9px 0;border-top:1px solid rgba(0,202,113,.16)">'
    f'<span class="d-small d-acc">{n}</span><span style="font-size:{min(s * .5, 64):.0f}px;line-height:1.1;white-space:nowrap;overflow:hidden">We build it</span>'
    f'<span class="d-small d-spec">{s} px · móvil {m} px · lh {lh}</span><span class="d-micro">{u}</span></div>'
    for n, s, m, lh, u in scale)
d.page(f'''<div class="d-body">
  <span class="d-k">Escala</span>
  <h2 class="d-h2" style="margin:14px 0 22px">Diez escalones</h2>
  <div>{rows}</div>
  <p class="d-micro" style="margin-top:14px">Medidas de referencia sobre un frame de 1920 px. En pantalla escalan con el ancho de la losa; en móvil pasan a los valores fijos indicados. Muestras al 50 %.</p>
</div>''', 'Tipografía')

d.page(f'''<div class="d-body">
  <span class="d-k">Reglas</span>
  <h2 class="d-h2" style="margin:14px 0 24px">Cómo se compone el texto</h2>
  <div class="d-grid d-g2" style="gap:26px">
    <div class="d-slab" style="padding:30px;text-align:center">
      <p style="font-size:34px;line-height:1.25;margin:0">We solve your business challenges with<br>strategy, creativity, and technology</p>
      <p class="d-small" style="margin-top:20px">Titulares de sección: centrados, en dos líneas.</p>
    </div>
    <div class="d-slab" style="padding:30px">
      <p style="font-size:70px;line-height:1.05;margin:0">Pricing</p>
      <p style="font-size:15px;color:#C9C9C9;margin-top:16px">Three options. No fine print.</p>
      <p class="d-small d-acc" style="margin-top:22px">El salto de escala entre titular y cuerpo es grande y deliberado.</p>
    </div>
  </div>
  <ul class="d-list" style="margin-top:22px">
    <li><b>Un solo peso de trabajo.</b> SemiBold para todo. Si algo pide un peso intermedio, se resuelve con tamaño y color.</li>
    <li><b>Itálica solo en testimonios.</b> Black Italic no se usa para enfatizar ni para decorar.</li>
    <li><b>Sin mayúsculas sostenidas.</b> Salvo las cotas técnicas de las ilustraciones, el texto va en tipo oración.</li>
    <li><b>Interlineado.</b> 1,2 en display, 1,25 en títulos, 1,5 en párrafos.</li>
  </ul>
</div>''', 'Tipografía')

# ============================ 04 COMPOSICIÓN ===============================
divider('04', 'Composición', 'Frames de pantalla completa, losas y aire.')

d.page(f'''<div class="d-body"><div class="d-split">
  <div style="position:relative;height:540px;background:#000;border:1px solid rgba(255,255,255,.12);border-radius:10px">
    <div style="position:absolute;left:1.9%;top:24%;width:4.8%;height:52%;background:#0B0B0B;border-radius:10px;border:1px solid rgba(0,202,113,.35)"></div>
    <div style="position:absolute;left:9.7%;right:3.4%;top:6.8%;bottom:6.8%;background:#0B0B0B;border-radius:18px;border:1px dashed rgba(0,202,113,.45);display:grid;place-items:center" class="d-small">Losa</div>
    <span class="d-micro" style="position:absolute;left:2%;top:10px">Menú</span>
    <span class="d-micro d-acc" style="position:absolute;left:10%;top:-22px">186 px</span>
    <span class="d-micro d-acc" style="position:absolute;right:0;top:-22px">65 px</span>
    <span class="d-micro d-acc" style="position:absolute;right:-56px;top:2%">73 px</span>
  </div>
  <div class="d-col">
    <span class="d-k">Frame</span>
    <h2 class="d-h2">Una pantalla, una idea</h2>
    <p class="d-p">La unidad de composición es el frame de 1920 × 1080. Cada sección ocupa una pantalla y se navega de a una.</p>
    <p class="d-p">El contenido vive en una sola losa por frame, con márgenes fijos: 186 px a la izquierda (donde vive el menú), 65 px a la derecha y 73 px arriba y abajo.</p>
    <p class="d-p">La losa tiene radio alto (32 px a 1920) y fondo Slab. Adentro, todo se mide en proporción a su ancho para que la composición escale igual en cualquier pantalla.</p>
  </div>
</div></div>''', 'Composición')

sp = [('sp-1', '10'), ('sp-2', '15'), ('sp-3', '20'), ('sp-4', '30'), ('sp-5', '50'), ('sp-6', '115')]
rad = [('pill', '999', 'Botones'), ('slab', '32', 'Losas'), ('card', '27', 'Tarjetas'), ('sm', '17', 'Imágenes'), ('field', '15', 'Campos y chips')]
d.page(f'''<div class="d-body">
  <span class="d-k">Espaciado y radios</span>
  <h2 class="d-h2" style="margin:14px 0 34px">Medidas que se repiten</h2>
  <div class="d-grid d-g2" style="gap:56px">
    <div>
      <h3 class="d-h4" style="margin-bottom:18px">Espaciado (a 1920)</h3>
      {''.join(f'<div style="display:flex;align-items:center;gap:20px;padding:10px 0;border-top:1px solid rgba(0,202,113,.16)"><span class="d-small d-acc" style="width:60px">{n}</span><span style="height:22px;width:{int(v) * 3}px;background:rgba(0,202,113,.5);border-radius:4px"></span><span class="d-small">{v} px</span></div>' for n, v in sp)}
    </div>
    <div>
      <h3 class="d-h4" style="margin-bottom:18px">Radios</h3>
      <div class="d-grid d-g5" style="gap:14px">{''.join(f'<div class="d-col" style="gap:8px"><div style="height:110px;border:2px solid rgba(0,202,113,.5);border-radius:{min(int(r), 55)}px"></div><b style="font-size:15px">{n}</b><span class="d-micro">{r} px · {u}</span></div>' for n, r, u in rad)}</div>
      <p class="d-small" style="margin-top:26px">Las esquinas son siempre redondeadas. No hay esquinas a 90° en piezas de marca.</p>
    </div>
  </div>
</div>''', 'Composición')

d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-slab" style="height:640px">{arcs(380, 320, (120, 210, 300, 420), .45, thick=520, w=760, h=640)}</div>
  <div class="d-col">
    <span class="d-k">Motivo</span>
    <h2 class="d-h2">Arcos orbitales</h2>
    <p class="d-p">Círculos concéntricos y finos que cruzan la losa como órbitas. Nunca se ven completos: son arcos cortados por la losa o por la propia línea.</p>
    <ul class="d-list">
      <li><b>Trazo:</b> 1,5 px, verde Accent al 30–50 %.</li>
      <li><b>Centro:</b> fuera del texto, para que el titular quede limpio.</li>
      <li><b>Anillo grueso:</b> un arco ancho con degradé de Accent a transparente asoma en las esquinas.</li>
      <li><b>Movimiento:</b> rotación continua, muy lenta (de 140 a 320 s por vuelta), en sentidos alternados.</li>
    </ul>
  </div>
</div></div>''', 'Composición')

d.page(f'''<div class="d-body">
  <span class="d-k">Luz</span>
  <h2 class="d-h2" style="margin:14px 0 34px">Brillos, no degradés de color</h2>
  <div class="d-grid d-g3">
    <div class="d-col"><div class="d-slab" style="height:300px;display:grid;place-items:center"><div style="width:280px;height:280px;border-radius:50%;background:radial-gradient(closest-side,rgba(0,202,113,.35),transparent)"></div></div><h3 class="d-h4">Resplandor radial</h3><p class="d-small">Detrás de títulos centrales y botones. Accent al 22–35 % hacia transparente.</p></div>
    <div class="d-col"><div class="d-slab" style="height:300px;display:grid;place-items:center"><div style="width:120px;height:280px;background:linear-gradient(to right,transparent,rgba(0,202,113,.2),transparent);-webkit-mask-image:linear-gradient(transparent,#000 25%,#000 75%,transparent)"></div></div><h3 class="d-h4">Columna</h3><p class="d-small">Una franja vertical de luz detrás de una rueda o lista. Se desvanece arriba y abajo.</p></div>
    <div class="d-col"><div class="d-slab" style="height:300px">{arcs(500, 380, (300,), .0, thick=320, glow=False, w=500, h=300)}</div><h3 class="d-h4">Anillo de esquina</h3><p class="d-small">El arco grueso que entra por una esquina, de Accent a Accent Dark y a transparente.</p></div>
  </div>
</div>''', 'Composición')

# ============================ 05 ÍCONOS E ILUSTRACIÓN =======================
divider('05', 'Iconografía e ilustración', 'Glifos rellenos y dibujos que se mueven.')

icons = [('p-home', 'Home'), ('p-servicios', 'Services'), ('p-programa', 'Program'), ('p-out-of-the-box', 'Out of the Box'),
         ('p-trabajo', 'Work'), ('p-nosotros', 'About'), ('p-blog', 'Blog'), ('p-contacto', 'Contact'),
         ('s-why', 'Why'), ('s-problem', 'Problem'), ('s-included', 'Included'), ('s-audience', 'Audience'),
         ('s-after', 'After'), ('s-pricing', 'Pricing'), ('s-faq', 'FAQ'), ('s-track', 'Track record'),
         ('s-idea', 'Idea'), ('s-pods', 'Pods'), ('s-pieces', 'Pieces'), ('s-next', 'Next'), ('s-list', 'List'), ('s-article', 'Article')]
d.page(f'''<div class="d-body">
  <span class="d-k">Íconos</span>
  <h2 class="d-h2" style="margin:14px 0 14px">Una familia de glifos</h2>
  <p class="d-lead" style="margin-bottom:28px">Rellenos, en una caja de 24 × 24, con esquinas suaves. Grises cuando están inactivos, verdes con brillo cuando están activos.</p>
  <div style="display:grid;grid-template-columns:repeat(11,1fr);gap:14px">{''.join(f'<div class="d-slab" style="height:118px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px">{icon(s, 34, ACCENT if i == 2 else "#8A8A8A")}<span class="d-micro" style="color:#C9C9C9">{n}</span></div>' for i, (s, n) in enumerate(icons))}</div>
</div>''', 'Íconos')


def ill(name, cls=''):
    return f'<div class="ill-stage is-active {cls}" style="max-width:none">{partial("ill-" + name)}</div>'


d.page(f'''<div class="d-body">
  <span class="d-k">Ilustraciones de servicio</span>
  <h2 class="d-h2" style="margin:14px 0 30px">Un dibujo por servicio</h2>
  <div class="d-grid d-g3">
    <div class="d-col"><div class="d-slab" style="padding:30px 20px">{ill('brand')}</div><h3 class="d-h4">Branding &amp; Marketing</h3><p class="d-small">La marca en el centro y sus canales orbitando alrededor, girando lento.</p></div>
    <div class="d-col"><div class="d-slab" style="padding:30px 20px">{ill('tech')}</div><h3 class="d-h4">Tech &amp; Automation</h3><p class="d-small">Un diagrama de nodos que se traza y se enciende en secuencia.</p></div>
    <div class="d-col"><div class="d-slab" style="padding:30px 20px">{ill('growth')}</div><h3 class="d-h4">Business Growth</h3><p class="d-small">Una curva que se dibuja de izquierda a derecha sobre columnas tenues.</p></div>
  </div>
</div>''', 'Ilustración')

d.page(f'''<div class="d-body">
  <span class="d-k">Ilustraciones de argumento</span>
  <h2 class="d-h2" style="margin:14px 0 30px">Cada razón, un dibujo</h2>
  <div class="d-grid d-g3">
    <div class="d-col"><div class="d-slab" style="padding:30px 20px">{ill('road')}</div><h3 class="d-h4">Fast Execution</h3><p class="d-small">Una ruta en perspectiva: las líneas corren hacia quien mira y la flecha acelera.</p></div>
    <div class="d-col"><div class="d-slab" style="padding:30px 20px">{ill('inspect')}</div><h3 class="d-h4">Customized Solutions</h3><p class="d-small">Un inspector de botón: las cotas y los valores aparecen uno por uno.</p></div>
    <div class="d-col"><div class="d-slab" style="padding:30px 20px">{ill('sliders')}</div><h3 class="d-h4">Free Initial Evaluation</h3><p class="d-small">Sliders que corren hasta su posición al aparecer.</p></div>
  </div>
  <p class="d-small" style="margin-top:24px">Reglas: dibujadas en vector, con la paleta de la marca, trazos de 1,2 a 3 px y nodos con brillo. Nunca fotos ni íconos de librería en su lugar.</p>
</div>''', 'Ilustración')

# ============================ 06 COMPONENTES Y MOVIMIENTO ==================
divider('06', 'Componentes y movimiento', 'Las piezas de la interfaz y cómo se mueven.')

d.page(f'''<div class="d-body">
  <span class="d-k">Componentes</span>
  <h2 class="d-h2" style="margin:14px 0 30px">Piezas base</h2>
  <div class="d-grid d-g3" style="gap:26px">
    <div class="d-slab" style="padding:34px;display:flex;flex-direction:column;gap:18px;align-items:flex-start">
      <span class="d-k">Botón píldora</span>
      <span class="d-pill">Get Your Free Evaluation</span>
      <span class="d-pill" style="border-color:{ACCENT}">Hover: borde verde</span>
      <p class="d-small">Borde fino, fondo oscuro. Nunca se levanta ni proyecta sombra.</p>
    </div>
    <div class="d-slab" style="padding:34px;display:flex;flex-direction:column;gap:18px">
      <span class="d-k">Tarjeta</span>
      <div class="d-card"><h3 class="d-h4">A trained team</h3><p class="d-small" style="margin-top:6px">Your local team, able to run it without us.</p></div>
      <div class="d-card d-card--strong"><h3 class="d-h4">Activa</h3><p class="d-small" style="margin-top:6px">Borde al 50 % para la pieza destacada.</p></div>
    </div>
    <div class="d-slab" style="padding:34px;display:flex;flex-direction:column;gap:16px">
      <span class="d-k">Formulario</span>
      <div style="height:54px;border-radius:15px;border:1px solid rgba(0,202,113,.3);display:flex;align-items:center;padding:0 20px;color:#5E5E5E;font-size:17px">Email</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
        <div style="height:60px;border-radius:15px;border:1px solid rgba(0,202,113,.2);display:grid;place-items:center;color:#BDBDBD;font-size:15px">Tech &amp; Automation</div>
        <div style="height:60px;border-radius:15px;border:1px solid {ACCENT};display:grid;place-items:center;font-size:15px">Branding</div>
      </div>
      <div style="height:8px;border-radius:99px;background:rgba(0,99,55,.28);overflow:hidden"><div style="width:50%;height:100%;background:{ACCENT}"></div></div>
      <p class="d-small">Campos con borde verde, opciones como chips y progreso en verde.</p>
    </div>
  </div>
</div>''', 'Componentes')

d.page(f'''<div class="d-body"><div class="d-split">
  <img class="d-shot" src="{A}web-nav-open.png" style="max-height:650px;object-fit:contain;background:#000">
  <div class="d-col">
    <span class="d-k">Navegación</span>
    <h2 class="d-h2">Dos niveles a la izquierda</h2>
    <p class="d-p">El menú principal lista las páginas del sitio, siempre en el mismo orden. Se compacta cuando la página tiene secciones y se despliega al pasar el mouse: los nombres salen de atrás de la barra.</p>
    <p class="d-p">A su lado, el menú de secciones muestra dónde estás dentro de la página, con el brillo verde que sigue a la vista activa.</p>
    <p class="d-p">En el teléfono, el menú pasa a una barra inferior con nombre bajo cada ícono y un botón Menu con todas las páginas y secciones.</p>
  </div>
</div></div>''', 'Componentes')

mov = [('Arcos orbitales', 'Rotación continua', '140–320 s', 'lineal'),
       ('Cambio de vista', 'Desplazamiento de pantalla', '1 s', '(.76, 0, .24, 1)'),
       ('Tarjetas que se expanden', 'Ancho y contenido', '0,8 s', '(.65, 0, .35, 1)'),
       ('Diagrama de nodos', 'Trazo + encendido en secuencia', '1,1 s + 0,13 s por nodo', '(.65, 0, .35, 1)'),
       ('Curva de crecimiento', 'Se dibuja de izquierda a derecha', '1,8 s', '(.45, .05, .35, 1)'),
       ('Sliders', 'Corren hasta su posición', '1,2 s', '(.2, .8, .2, 1)'),
       ('Menú', 'Se despliega y muestra nombres', '0,6 s', '(.65, 0, .35, 1)'),
       ('Hover', 'Cambio de borde o color', '0,3 s', '(.65, 0, .35, 1)')]
d.page(f'''<div class="d-body">
  <span class="d-k">Movimiento</span>
  <h2 class="d-h2" style="margin:14px 0 14px">Se mueve lo que tiene sentido</h2>
  <p class="d-lead" style="margin-bottom:24px">Las animaciones salen del dibujo y se disparan una sola vez, al entrar en pantalla. Sin fundidos genéricos ni tarjetas que se levantan.</p>
  <table class="d-table"><tr><th>Elemento</th><th>Qué pasa</th><th>Duración</th><th>Curva</th></tr>
  {''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td class="d-spec">{e}</td></tr>' for a, b, c, e in mov)}</table>
  <p class="d-small" style="margin-top:16px">Si la persona pidió reducir el movimiento en su sistema, todo aparece en su estado final y nada gira.</p>
</div>''', 'Movimiento')

# ============================ 07 APLICACIONES ==============================
divider('07', 'Aplicaciones', 'El sistema aplicado: web, teléfono, redes, presentaciones y papelería.')

d.page(f'''<div class="d-body">
  <span class="d-k">Web · Home</span>
  <h2 class="d-h2" style="margin:14px 0 26px">La vidriera</h2>
  <div class="d-split" style="grid-template-columns:900px 1fr;gap:56px"><div><div class="d-grid d-g2"><img class="d-shot" src="{A}web-home-hero.png"><img class="d-shot" src="{A}web-home-services.png"></div>
  <div class="d-grid d-g2" style="margin-top:22px"><img class="d-shot" src="{A}web-home-why.png"><img class="d-shot" src="{A}web-home-work.png"></div></div>
  <div class="d-col"><p class="d-p">El home es la vidriera: seis pantallas que se recorren de a una, con todas las ilustraciones animadas.</p><p class="d-p">Cada pantalla tiene una sola idea, un titular y una acción.</p></div></div>
</div>''', 'Aplicaciones')

d.page(f'''<div class="d-body">
  <span class="d-k">Web · Páginas internas</span>
  <h2 class="d-h2" style="margin:14px 0 26px">Para leer y decidir</h2>
  <div class="d-split" style="grid-template-columns:900px 1fr;gap:56px"><div><div class="d-grid d-g2"><img class="d-shot" src="{A}web-program-hero.png"><img class="d-shot" src="{A}web-service.png"></div>
  <div class="d-grid d-g2" style="margin-top:22px"><img class="d-shot" src="{A}web-program-timeline.png"><img class="d-shot" src="{A}web-program-pricing.png"></div></div>
  <div class="d-col"><p class="d-p">Las páginas internas son para leer y decidir: menos movimiento, más texto ordenado en tarjetas.</p><p class="d-p">Los arcos siguen presentes y las ilustraciones de servicio se animan al entrar en pantalla.</p></div></div>
</div>''', 'Aplicaciones')

d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-col"><img class="d-shot" src="{A}web-ootb.png"><img class="d-shot" src="{A}web-ootb-cta.png"></div>
  <div class="d-col">
    <span class="d-k">La excepción</span>
    <h2 class="d-h2">Out of the Box</h2>
    <p class="d-p">La división premium se ve más audaz, con los mismos elementos:</p>
    <ul class="d-list">
      <li><b>Escala máxima.</b> Titulares en el escalón Display.</li>
      <li><b>Más aire.</b> Cada bloque ocupa una pantalla completa.</li>
      <li><b>Más verde.</b> El cierre es una losa verde entera.</li>
      <li><b>Más movimiento.</b> Más arcos, el anillo grueso y trazos que corren.</li>
    </ul>
    <p class="d-small">Sin colores ni tipografías nuevas. La diferencia está en la intensidad, no en otro idioma visual.</p>
  </div>
</div></div>''', 'Aplicaciones')

d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-row" style="gap:30px;justify-content:center">
    <img src="{A}mob-program.png" style="height:650px;border-radius:28px;border:1px solid rgba(0,202,113,.2)">
    <img src="{A}mob-menu.png" style="height:650px;border-radius:28px;border:1px solid rgba(0,202,113,.2)">
  </div>
  <div class="d-col">
    <span class="d-k">Teléfono</span>
    <h2 class="d-h2">Misma marca, otro formato</h2>
    <p class="d-p">En el teléfono las losas se apilan y el texto pasa a tamaños fijos. El menú se convierte en una barra inferior con nombre bajo cada ícono.</p>
    <p class="d-p">El botón Menu abre todas las páginas y las secciones de la página actual, con la activa marcada en verde.</p>
  </div>
</div></div>''', 'Aplicaciones')


def post(w, h, title, sub='', k='We Brand U', big=True):
    sc = w / 1080
    return f'''<div style="position:relative;width:{w}px;height:{h}px;background:#000;border-radius:{18 * sc + 8:.0f}px;overflow:hidden;border:1px solid rgba(255,255,255,.1)">
      <div style="position:absolute;inset:{40 * sc:.0f}px;background:#0B0B0B;border-radius:{36 * sc:.0f}px;overflow:hidden">{arcs(w * .78, h * .7, (w * .35, w * .6, w * .9), .4, thick=w * 1.05, w=w, h=h)}
      <div style="position:absolute;left:{80 * sc:.0f}px;right:{80 * sc:.0f}px;top:{80 * sc:.0f}px;bottom:{80 * sc:.0f}px;display:flex;flex-direction:column;justify-content:space-between">
        <div style="display:flex;align-items:center;gap:{14 * sc:.0f}px;font-size:{30 * sc:.0f}px">{logo(40 * sc)}<span>{k}</span></div>
        <div><p style="font-size:{(118 if big else 84) * sc:.0f}px;line-height:1.08;margin:0">{title}</p>
        {f'<p style="font-size:{34 * sc:.0f}px;color:#C9C9C9;margin:{24 * sc:.0f}px 0 0;line-height:1.4">{sub}</p>' if sub else ''}</div>
      </div></div></div>'''


d.page(f'''<div class="d-body">
  <span class="d-k">Redes sociales</span>
  <h2 class="d-h2" style="margin:14px 0 26px">Posts y stories</h2>
  <div class="d-row" style="gap:34px;align-items:flex-end">
    {post(430, 430, 'Three months.<br>Then it’s yours.', 'Build it. Prove it. Hand it over.')}
    {post(430, 430, 'Independent,<br>not dependent.', '', big=True)}
    {post(255, 453, 'Talent over<br>titles.', 'Pods hired locally, starting in Europe.')}
  </div>
  <p class="d-small" style="margin-top:22px">Plantilla fija: losa sobre negro, símbolo y nombre arriba, una sola frase grande abajo y los arcos entrando por una esquina.</p>
</div>''', 'Aplicaciones')

d.page(f'''<div class="d-body">
  <span class="d-k">Presentaciones y perfiles</span>
  <h2 class="d-h2" style="margin:10px 0 18px">Diapositiva y portada de perfil</h2>
  <div style="position:relative;width:780px;height:439px;background:#000;border-radius:16px;overflow:hidden;border:1px solid rgba(255,255,255,.1)">
    <div style="position:absolute;left:84px;right:30px;top:30px;bottom:30px;background:#0B0B0B;border-radius:20px;overflow:hidden">{arcs(540, 230, (120, 200, 300), .35, thick=360, w=666, h=379)}
      <div style="position:absolute;left:70px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:18px">
        <span class="d-k">Month 2</span><p style="font-size:54px;line-height:1.1;margin:0">Operation</p>
        <p class="d-small" style="max-width:420px">We produce and publish at full volume. We measure what works and adjust.</p></div></div>
    <div style="position:absolute;left:20px;top:110px;width:44px;height:220px;background:#0B0B0B;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:space-evenly">{icon('p-home', 18, '#2E2E2E')}{icon('p-servicios', 18, '#2E2E2E')}{icon('p-programa', 18, ACCENT)}{icon('p-trabajo', 18, '#2E2E2E')}{icon('p-contacto', 18, '#2E2E2E')}</div>
  </div>
  <div style="position:relative;width:780px;height:160px;margin-top:18px;background:#0B0B0B;border-radius:16px;overflow:hidden;border:1px solid rgba(255,255,255,.1)">{arcs(650, 140, (100, 170, 250), .4, thick=300, w=780, h=160)}
    <div style="position:absolute;left:50px;top:0;bottom:0;display:flex;align-items:center;gap:36px">{lockup(46)}<span class="d-lead" style="font-size:18px">Three months. Then it’s yours.</span></div></div>
</div>''', 'Aplicaciones')

card_front = f'''<div style="width:510px;height:330px;background:#0B0B0B;border-radius:18px;position:relative;overflow:hidden;border:1px solid rgba(255,255,255,.1)">{arcs(430, 260, (110, 190, 280), .4, thick=330, w=510, h=330)}
  <div style="position:absolute;left:40px;top:40px">{logo(46)}</div>
  <div style="position:absolute;left:40px;bottom:40px"><p style="font-size:24px;margin:0">[Nombre Apellido]</p><p class="d-small" style="margin-top:6px">[Rol]</p></div></div>'''
card_back = f'''<div style="width:510px;height:330px;background:{ACCENT};border-radius:18px;display:grid;place-items:center;color:#0B0B0B">{lockup(70, '#0B0B0B', '#0B0B0B')}</div>'''
d.page(f'''<div class="d-body">
  <span class="d-k">Papelería</span>
  <h2 class="d-h2" style="margin:14px 0 30px">Tarjeta y firma</h2>
  <div class="d-row" style="gap:30px">{card_front}{card_back}</div>
  <div class="d-slab" style="margin-top:30px;padding:28px 34px;display:flex;align-items:center;gap:34px;max-width:1060px">
    {logo(46)}
    <div style="border-left:1px solid rgba(0,202,113,.3);padding-left:30px"><p style="font-size:19px;margin:0">[Nombre Apellido]</p><p class="d-small" style="margin-top:4px">[Rol] · We Brand U</p><p class="d-micro" style="margin-top:8px">[email] · estebanguimi.github.io/we_brand_u</p></div>
    <span class="d-small d-acc" style="margin-left:auto">Three months. Then it’s yours.</span>
  </div>
  <p class="d-micro" style="margin-top:14px">Tarjeta 85 × 55 mm. Frente charcoal con arcos; dorso verde con el bloque de marca. Firma de email sin imágenes de fondo.</p>
</div>''', 'Aplicaciones')

# ============================ 08 CHECKLIST =================================
checks = ['El fondo es negro y el contenido está sobre una losa charcoal.',
          'Hay un solo verde, #00CA71, y ningún otro color.',
          'Como mucho una superficie verde sólida, y es la acción principal.',
          'Toda la tipografía es Inter SemiBold; Black Italic solo en una cita de partner.',
          'El titular es grande y el cuerpo chico: el salto de escala se nota.',
          'Los bordes son verdes a baja opacidad, no grises.',
          'Los arcos orbitales están presentes y no tapan el texto.',
          'Los íconos son de la familia de glifos de la marca.',
          'El logo tiene su espacio de seguridad y no está deformado ni recoloreado.',
          'Lo que se mueve tiene sentido y respeta la preferencia de movimiento reducido.']
d.page(f'''<div class="d-body">
  <span class="d-k">08 · Checklist</span>
  <h2 class="d-h2" style="margin:14px 0 26px">Antes de publicar una pieza</h2>
  <div class="d-grid d-g2" style="column-gap:56px;row-gap:0">{''.join(f'<div style="display:flex;gap:18px;padding:17px 0;border-top:1px solid rgba(0,202,113,.16)"><span class="d-num">{i:02d}</span><span class="d-p" style="color:#fff">{c}</span></div>' for i, c in enumerate(checks, 1))}</div>
</div>''', 'Checklist')

d.page(f'''{arcs(800, 450, (200, 340, 500, 680), .3, thick=760)}
<div class="d-body" style="align-items:center;text-align:center;gap:34px">
  {logo(160)}
  <p class="d-h2">Your Idea. Our Goal.</p>
  <p class="d-micro">We Brand U · Línea gráfica · Versión 1.0 · 2026</p>
</div>''', bare=True)

DOC = d
