from base import Doc, logo, lockup, icon, arcs, partial, ACCENT

d = Doc('Guía de marca', 'GM')


def divider(num, title, sub):
    d.page(f'''{arcs(1250, 450, (230, 390, 560, 740), .32, thick=820)}
<div class="d-body" style="justify-content:flex-end;padding-bottom:40px">
  <span class="d-num" style="font-size:22px">{num}</span>
  <h1 class="d-h1" style="font-size:150px;margin-top:18px">{title}</h1>
  <p class="d-lead" style="margin-top:28px">{sub}</p>
</div>''', title)


def ill(name):
    return f'<div class="ill-stage is-active" style="max-width:none">{partial("ill-" + name)}</div>'


# 01 Portada
d.page(f'''{arcs(1180, 470, (250, 420, 600), .34, thick=760)}
<div class="d-body" style="justify-content:space-between">
  <div>{lockup(54)}</div>
  <div>
    <span class="d-k" style="font-size:18px">Manual de identidad · Parte 2</span>
    <h1 class="d-h1" style="font-size:170px;margin-top:20px">Guía de<br>marca</h1>
    <p class="d-lead" style="margin-top:30px">Quiénes somos, qué vendemos, a quién, y cómo lo decimos.</p>
  </div>
  <div class="d-cover-meta"><span>Versión<b>1.0</b></span><span>Año<b>2026</b></span><span>Alcance<b>Equipo, pods y proveedores</b></span></div>
</div>''', bare=True)

toc = [('01', 'Esencia', '03'), ('02', 'Oferta', '09'), ('03', 'Cómo trabajamos', '17'), ('04', 'Audiencia', '23'),
       ('05', 'Voz y tono', '26'), ('06', 'Escritura', '31'), ('07', 'Mensajes', '35'), ('08', 'Checklist', '39')]
d.page(f'''<div class="d-body">
  <span class="d-k">Contenido</span>
  <h2 class="d-h2" style="margin:14px 0 44px">Índice</h2>
  <div class="d-toc">{''.join(f'<div><span>{a}</span><span>{b}</span><span>{c}</span></div>' for a, b, c in toc)}</div>
  <p class="d-small" style="margin-top:40px;max-width:980px">Esta guía acompaña a la Línea gráfica. La línea gráfica define cómo se ve la marca; esta guía define qué es, qué promete y cómo habla. Todo el texto público de la marca se escribe en inglés; esta guía está en español porque es para el equipo.</p>
</div>''', 'Índice')

# ============================ 01 ESENCIA ===================================
divider('01', 'Esencia', 'Qué es We Brand U y qué problema existe para resolver.')

d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-col">
    <span class="d-k">Quiénes somos</span>
    <h2 class="d-h2">No trabajamos por piezas sueltas</h2>
    <p class="d-p">We Brand U es una agencia creativa de marketing. Levanta la presencia digital completa de una empresa en tres meses.</p>
    <p class="d-p">Después le deja a esa empresa el sistema funcionando y su propio equipo capacitado para sostenerlo.</p>
    <p class="d-p">Forma parte de una familia de marcas “We”, todas fundadas por la misma persona.</p>
  </div>
  <div class="d-slab" style="height:600px;display:grid;place-items:center">{arcs(380, 300, (150, 250, 360), .35, w=760, h=600)}<div style="position:relative;text-align:center">{logo(170)}<p class="d-quote" style="margin-top:34px">Your Idea.<br>Our Goal.</p></div></div>
</div></div>''', 'Esencia')

d.page(f'''<div class="d-body">
  <span class="d-k">El problema</span>
  <h2 class="d-h2" style="margin:14px 0 18px">Atrapados entre dos opciones malas</h2>
  <p class="d-lead" style="margin-bottom:34px">Las empresas medianas que quieren crecer en digital suelen terminar en uno de estos dos lugares.</p>
  <div class="d-grid d-g2" style="gap:26px">
    <div class="d-slab" style="padding:42px">
      <span class="d-num">Opción 1</span><h3 class="d-h3" style="margin:12px 0 16px">Una agencia, para siempre</h3>
      <ul class="d-list"><li>Les produce contenido indefinidamente.</li><li>Nunca aprenden a hacerlo.</li><li>El costo no baja nunca.</li><li>El día que cortan el contrato, vuelven a cero.</li></ul>
    </div>
    <div class="d-slab" style="padding:42px">
      <span class="d-num">Opción 2</span><h3 class="d-h3" style="margin:12px 0 16px">Una persona sin experiencia</h3>
      <ul class="d-list"><li>Contratan a alguien interno.</li><li>Tarda un año en descubrir qué funciona.</li><li>Mientras tanto, publican cualquier cosa.</li></ul>
    </div>
  </div>
</div>''', 'Esencia')

steps = [('Construimos', 'el sistema: identidad, mensaje, contenido y canales.'),
         ('Lo operamos', 'para demostrar que funciona, midiendo y ajustando.'),
         ('Lo entregamos', 'documentado, con el equipo del cliente entrenado.')]
d.page(f'''<div class="d-body">
  <span class="d-k">Nuestra respuesta</span>
  <h2 class="d-h2" style="margin:14px 0 34px">Romper el dilema</h2>
  <div class="d-grid d-g3">{''.join(f'<div class="d-card" style="padding:36px"><span class="d-num">0{i}</span><h3 class="d-h3" style="margin:14px 0 10px">{t}</h3><p class="d-p">{x}</p></div>' for i, (t, x) in enumerate(steps, 1))}</div>
  <div class="d-slab" style="margin-top:30px;padding:40px 48px;display:flex;align-items:center;justify-content:space-between;gap:40px">
    <p class="d-quote" style="font-size:52px">Independent, not dependent.</p>
    <p class="d-p" style="max-width:520px">El partner queda independiente, no dependiente. Ese es el argumento central de la marca: todo el texto tiene que volver ahí.</p>
  </div>
</div>''', 'Esencia')

d.page(f'''{arcs(1250, 450, (200, 360, 520), .3)}
<div class="d-body">
  <span class="d-k">Argumento central</span>
  <p style="font-size:120px;line-height:1.05;margin:24px 0 36px">Three months.<br>Then it’s yours.</p>
  <p class="d-lead">La promesa en una línea. Resume el plazo definido y la transferencia, que son los dos diferenciales más importantes. Cuando una pieza no sabe qué decir, dice esto.</p>
</div>''', 'Esencia')

d.page(f'''<div class="d-body"><div class="d-split d-split--even">
  <div class="d-col">
    <span class="d-k">La familia “We”</span>
    <h2 class="d-h2">Una marca de una familia</h2>
    <p class="d-p">We Brand U es parte de una familia de marcas “We”, todas fundadas por la misma persona.</p>
    <p class="d-p">El nombre se lee como una frase: we brand you. El símbolo de la marca es la U.</p>
  </div>
  <div class="d-col" style="gap:20px">
    <div class="d-card"><h3 class="d-h4">Cómo se escribe</h3><p class="d-small" style="margin-top:8px">Siempre “We Brand U”: tres palabras, mayúscula inicial en cada una, la U sola. Nunca “WeBrandU”, “WBU”, “We Brand You” ni “WE BRAND U”.</p></div>
    <div class="d-card"><h3 class="d-h4">Cómo se nombra en el texto</h3><p class="d-small" style="margin-top:8px">En el copy hablamos en primera persona del plural: “we”. El nombre completo se usa para presentarnos, no para hablar de nosotros en tercera persona (“We Brand U does…”).</p></div>
    <div class="d-card"><h3 class="d-h4">Los clientes son partners</h3><p class="d-small" style="margin-top:8px">A quienes trabajan con nosotros les decimos “partners”, nunca “clients”. Es una decisión, no un descuido.</p></div>
  </div>
</div></div>''', 'Esencia')

# ============================ 02 OFERTA ====================================
divider('02', 'Oferta', 'El programa de tres meses, lo que viene después y los tres servicios.')

months = [('Mes 1', 'Montaje', 'Setup', ['Auditoría de lo que el partner tiene hoy.', 'Definición de identidad visual, mensaje y líneas de contenido.', 'Armado de los canales.', 'Empieza la producción.']),
          ('Mes 2', 'Operación', 'Operation', ['Nuestro equipo produce y publica a volumen completo.', 'Se mide qué funciona y se ajusta.', 'El partner observa y participa.']),
          ('Mes 3', 'Transferencia', 'Handover', ['Se documenta todo el sistema: plantillas, calendario, procesos, criterios.', 'Se capacita al equipo local del partner para que lo opere.', 'Al final del mes, el partner puede seguir solo.'])]
d.page(f'''<div class="d-body">
  <span class="d-k">El programa</span>
  <h2 class="d-h2" style="margin:14px 0 30px">Tres meses, tres etapas</h2>
  <svg viewBox="0 0 1000 120" preserveAspectRatio="none" style="width:100%;height:90px;display:block"><path d="M0 100Q500 -60 1000 100" fill="none" stroke="{ACCENT}" stroke-width="2" vector-effect="non-scaling-stroke"/></svg>
  <div class="d-grid d-g3" style="margin-top:6px">{''.join(f'<div class="d-card"><span class="d-num">{m} · {en}</span><h3 class="d-h3" style="margin:10px 0 12px">{es}</h3><ul class="d-list">{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for m, es, en, xs in months)}</div>
</div>''', 'Oferta')

d.page(f'''<div class="d-body">
  <span class="d-k">Después del tercer mes</span>
  <h2 class="d-h2" style="margin:14px 0 18px">Dos continuidades</h2>
  <p class="d-lead" style="margin-bottom:34px">El equipo del partner opera el sistema. Si quiere respaldo, hay dos opciones, combinables.</p>
  <div class="d-grid d-g2" style="gap:26px">
    <div class="d-slab" style="padding:44px">{icon('s-after', 40, ACCENT)}<h3 class="d-h3" style="margin:22px 0 12px">Soporte anual</h3><p class="d-p">Contrato de soporte por un año: acompañamiento, revisión y ajustes mientras el equipo del partner opera el sistema.</p><p class="d-small d-acc" style="margin-top:18px">En el sitio: Annual Support</p></div>
    <div class="d-slab" style="padding:44px">{icon('s-idea', 40, ACCENT)}<h3 class="d-h3" style="margin:22px 0 12px">Plan Pro</h3><p class="d-p">Opcional. Seguimos produciendo contenido de alta calidad todos los meses para que el partner solo lo publique.</p><p class="d-small d-acc" style="margin-top:18px">En el sitio: Pro Plan</p></div>
  </div>
</div>''', 'Oferta')

d.page(f'''<div class="d-body">
  <span class="d-k">Precios</span>
  <h2 class="d-h2" style="margin:14px 0 18px">Claros y sin letra chica</h2>
  <p class="d-lead" style="margin-bottom:30px">Las opciones se presentan en paralelo, con su estructura de pago a la vista.</p>
  <div class="d-grid d-g3">
    <div class="d-card d-card--strong"><h3 class="d-h4">Programa de 3 meses</h3><p class="d-h3" style="margin:14px 0">[PRECIO-PROGRAMA]</p><p class="d-small">Pago en tres partes durante el programa.</p></div>
    <div class="d-card"><h3 class="d-h4">Soporte anual</h3><p class="d-h3" style="margin:14px 0">[PRECIO-SOPORTE]</p><p class="d-small">Mensual, durante el año siguiente al programa.</p></div>
    <div class="d-card"><h3 class="d-h4">Plan Pro</h3><p class="d-h3" style="margin:14px 0">[PRECIO-PRO]</p><p class="d-small">Mensual. Opcional.</p></div>
  </div>
  <ul class="d-list" style="margin-top:30px">
    <li><b>Ninguna cifra se publica sin confirmar.</b> Mientras no esté aprobada, se usa el marcador.</li>
    <li><b>Siempre las tres opciones juntas.</b> El partner tiene que poder comparar sin pedir nada.</li>
    <li><b>Lo que incluye cada precio, en la misma tarjeta.</b> Nada escondido en otra página.</li>
  </ul>
</div>''', 'Oferta')

services = [
    ('brand', 'Branding &amp; Marketing', 'Identidad visual y estrategia digital. Qué dice la marca, cómo se ve y cómo aparece en cada canal.',
     'Empresas que se ven improvisadas y no transmiten el nivel al que realmente trabajan.',
     ['Identidad visual', 'Piezas gráficas', 'Estrategia de contenido', 'Redes sociales', 'Medios pagos'],
     'Your company works at a high level. Your brand doesn’t show it.'),
    ('tech', 'Tech &amp; Automation', 'Optimización del negocio con tecnología y automatización. Incluye el uso de IA en producción: generación asistida, pipelines automatizados y scripts propios.',
     'Equipos que pierden horas en tareas que una herramienta bien armada hace sola.',
     ['Webs y landings', 'Tiendas online', 'Flujos automatizados', 'IA en producción'],
     'Your team spends hours on tasks a well-built tool does on its own.'),
    ('growth', 'Business Growth &amp; Optimization', 'Crecimiento medido. Análisis de procesos, definición de KPIs y estrategias para escalar. No es “más posteos”: es entender qué mueve el número y repetirlo.',
     'Empresas que publican mucho y no saben si algo de eso les trae clientes.',
     ['Análisis de procesos', 'KPIs', 'Estrategia de crecimiento'],
     'You post a lot. You can’t tell if any of it brings in business.'),
]
for key, name, what, prob, inc, line in services:
    d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-slab" style="padding:46px 30px;display:grid;place-items:center;height:620px">{ill(key)}</div>
  <div class="d-col">
    <span class="d-k">Servicio</span>
    <h2 class="d-h2">{name}</h2>
    <p class="d-p">{what}</p>
    <div class="d-card"><span class="d-k">El problema que resuelve</span><p class="d-p" style="color:#fff;margin-top:8px">{prob}</p></div>
    <div style="display:flex;flex-wrap:wrap;gap:10px">{''.join(f'<span class="d-tag">{x}</span>' for x in inc)}</div>
    <p class="d-small">Línea en el sitio: <span class="d-acc">“{line}”</span></p>
  </div>
</div></div>''', 'Oferta')

d.page(f'''<div class="d-body" style="background:transparent">
  <div class="d-slab" style="background:{ACCENT};color:#0B0B0B;padding:64px 70px;height:640px;display:flex;flex-direction:column;justify-content:space-between">
    <div><span style="font-size:15px">División premium</span><p style="font-size:120px;line-height:1.05;margin:14px 0 0">Out of the Box</p></div>
    <div class="d-grid d-g3" style="gap:30px">
      <p style="font-size:18px;line-height:1.55;margin:0">Para empresas dispuestas a pagar más por campañas que se arriesgan. No es el servicio estándar con otro nombre.</p>
      <p style="font-size:18px;line-height:1.55;margin:0">Es la división donde se proponen ideas que la mayoría de las agencias no se anima a presentar: activaciones físicas, mecánicas de participación poco convencionales.</p>
      <p style="font-size:18px;line-height:1.55;margin:0">Ideas que generan conversación en vez de impresiones. Ejemplo: la gente grita a un micrófono y, si supera cierto nivel de decibeles, gana un premio.</p>
    </div>
  </div>
</div>''', 'Oferta')

# ============================ 03 CÓMO TRABAJAMOS ===========================
divider('03', 'Cómo trabajamos', 'Pods locales, talento sin título y producción asistida por IA.')

d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-slab" style="height:600px;display:grid;place-items:center">{arcs(380, 300, (150, 250), .3, w=760, h=600)}<div style="position:relative">{icon('s-pods', 260, ACCENT)}</div></div>
  <div class="d-col">
    <span class="d-k">El modelo de pods</span>
    <h2 class="d-h2">No somos una oficina</h2>
    <p class="d-p">Operamos con equipos remotos pequeños —pods— formados con talento contratado localmente en cada mercado, empezando por Europa.</p>
    <ul class="d-list"><li><b>Local.</b> Cada pod conoce su mercado, su idioma y su cultura.</li><li><b>Conectado.</b> Cada pod trabaja conectado a la central.</li><li><b>Pequeño.</b> Equipos chicos, cerca del partner.</li></ul>
  </div>
</div></div>''', 'Cómo trabajamos')

d.page(f'''{arcs(1250, 450, (200, 360), .28)}
<div class="d-body">
  <span class="d-k">Filosofía de contratación</span>
  <p style="font-size:110px;line-height:1.05;margin:24px 0 34px">Talent over titles.</p>
  <div class="d-grid d-g2" style="gap:40px;max-width:1240px">
    <p class="d-p">Buscamos gente con talento real que no tiene título formal y que en sus trabajos actuales no tiene libertad creativa. Gente subutilizada.</p>
    <p class="d-p" style="color:#fff">Esa es la ventaja, no una concesión. La decisión es deliberada y se comunica con orgullo, nunca como una disculpa.</p>
  </div>
</div>''', 'Cómo trabajamos')

d.page(f'''<div class="d-body"><div class="d-split">
  <div class="d-col">
    <span class="d-k">Producción asistida por IA</span>
    <h2 class="d-h2">Volumen sin perder calidad</h2>
    <p class="d-p">Usamos IA en producción de verdad, no como discurso: pipelines automatizados, generación de video con herramientas actuales y scripts propios.</p>
    <p class="d-p">Eso es lo que permite producir a volumen completo en el segundo mes del programa sin bajar la calidad.</p>
    <div class="d-card"><span class="d-k">Cómo se comunica</span><p class="d-small" style="margin-top:8px">Siempre con lo concreto: qué se automatiza y qué se gana. Nunca como promesa abstracta ni como palabra de moda.</p></div>
  </div>
  <div class="d-slab" style="padding:40px 26px;height:600px;display:grid;place-items:center">{ill('tech')}</div>
</div></div>''', 'Cómo trabajamos')

difs = [('Transferencia real', 'El partner termina independiente, con su equipo capacitado y el sistema documentado. Casi nadie lo ofrece porque va contra el negocio de la agencia.'),
        ('Plazo definido', 'Tres meses. No un contrato indefinido.'),
        ('Producción asistida por IA', 'Pipelines automatizados, generación de video y scripts propios. Volumen sin perder calidad.'),
        ('Pods locales', 'Gente del mercado, no una agencia hablándole desde afuera.'),
        ('Out of the Box', 'La opción para los que quieren arriesgar.')]
d.page(f'''<div class="d-body">
  <span class="d-k">Diferenciales</span>
  <h2 class="d-h2" style="margin:14px 0 14px">Qué nos hace distintos</h2>
  <p class="d-lead" style="margin-bottom:26px">En orden de importancia. Cuando hay que elegir qué decir, se empieza por arriba.</p>
  <div class="d-col" style="gap:0">{''.join(f'<div style="display:grid;grid-template-columns:90px 330px 1fr;gap:20px;align-items:baseline;padding:20px 0;border-top:1px solid rgba(0,202,113,.16)"><span style="font-size:44px;line-height:1" class="d-acc">{i}</span><span class="d-h3">{t}</span><span class="d-p">{x}</span></div>' for i, (t, x) in enumerate(difs, 1))}</div>
</div>''', 'Cómo trabajamos')

d.page(f'''<div class="d-body">
  <span class="d-k">Prueba disponible</span>
  <h2 class="d-h2" style="margin:14px 0 30px">La trayectoria del fundador</h2>
  <div class="d-grid d-g3">
    <div class="d-card" style="padding:38px"><p style="font-size:92px;line-height:1;margin:0" class="d-acc">1.3M+</p><p class="d-p" style="margin-top:14px">Visualizaciones orgánicas acumuladas.</p></div>
    <div class="d-card" style="padding:38px"><p style="font-size:92px;line-height:1;margin:0" class="d-acc">607K</p><p class="d-p" style="margin-top:14px">En una sola colocación.</p></div>
    <div class="d-card" style="padding:38px"><p style="font-size:92px;line-height:1;margin:0" class="d-acc">6</p><p class="d-p" style="margin-top:14px">Años entre campañas, organizaciones deportivas y marcas de consumo.</p></div>
  </div>
  <div class="d-slab" style="margin-top:28px;padding:30px 38px;display:flex;gap:26px;align-items:center">{icon('s-problem', 40, ACCENT)}
    <p class="d-p" style="color:#fff">Acuerdo de confidencialidad vigente: estos números se pueden usar, pero nunca se nombra al empleador anterior, ni a sus clientes, ni a sus campañas. Se escriben siempre como logro propio, sin identificar la cuenta.</p></div>
</div>''', 'Cómo trabajamos')

# ============================ 04 AUDIENCIA =================================
divider('04', 'Audiencia', 'A quién le vendemos y, con la misma claridad, a quién no.')

d.page(f'''<div class="d-body"><div class="d-split d-split--even">
  <div class="d-slab" style="padding:46px">
    {icon('s-audience', 44, ACCENT)}
    <h2 class="d-h2" style="margin:20px 0 18px">A quién le vendemos</h2>
    <ul class="d-list">
      <li>Empresas medianas que <b>ya facturan</b>.</li>
      <li>Cuya presencia digital <b>no refleja el nivel</b> de su operación.</li>
      <li>Dueños o responsables de marketing que <b>saben que tienen un problema</b>.</li>
      <li>Que <b>no quieren depender</b> de una agencia para siempre.</li>
    </ul>
  </div>
  <div class="d-slab" style="padding:46px">
    {icon('s-problem', 44, '#8A8A8A')}
    <h2 class="d-h2" style="margin:20px 0 18px">A quién no</h2>
    <ul class="d-list">
      <li>Empresas que buscan <b>el proveedor más barato</b>.</li>
      <li>Empresas que quieren <b>delegar y no involucrarse</b>.</li>
    </ul>
    <p class="d-p" style="margin-top:22px">El programa requiere que el equipo del partner participe, porque el objetivo es que después lo sostengan ellos.</p>
  </div>
</div></div>''', 'Audiencia')

d.page(f'''{arcs(1250, 450, (200, 360), .28)}
<div class="d-body">
  <span class="d-k">Por qué lo decimos</span>
  <p style="font-size:96px;line-height:1.06;margin:24px 0 34px">Decir para quién no es<br>genera confianza.</p>
  <p class="d-lead">Decir que servimos para todos no convence a nadie. Por eso cada página de servicio tiene un bloque “It’s not a fit if”, y por eso las conversaciones comerciales empiezan aclarando qué esperamos del equipo del partner.</p>
</div>''', 'Audiencia')

# ============================ 05 VOZ Y TONO ================================
divider('05', 'Voz y tono', 'Cómo suena We Brand U, en cualquier canal.')

traits = [('Directa', 'Frases cortas. Sujeto, verbo, objeto.'), ('Concreta', 'Plazos, entregables y números antes que conceptos.'),
          ('Segura', 'Afirma sin prometer de más.'), ('Del lado del partner', 'Habla de su independencia, no de nosotros.')]
d.page(f'''<div class="d-body">
  <span class="d-k">Personalidad</span>
  <h2 class="d-h2" style="margin:14px 0 30px">Cuatro rasgos</h2>
  <div class="d-grid d-g4">{''.join(f'<div class="d-card" style="padding:34px;min-height:300px;display:flex;flex-direction:column;justify-content:space-between"><span class="d-num">0{i}</span><div><h3 class="d-h3">{t}</h3><p class="d-p" style="margin-top:12px">{x}</p></div></div>' for i, (t, x) in enumerate(traits, 1))}</div>
</div>''', 'Voz y tono')

pairs = [('Directo', 'We build it, run it, and hand it over.', 'We offer comprehensive solutions designed to help businesses navigate digital transformation.'),
         ('Concreto', 'Three months and your team runs it on its own.', 'Integrated digital transformation solutions.'),
         ('Seguro', 'Your team runs it afterwards.', 'We guarantee you will dominate your market.'),
         ('En primera persona', 'We document the whole system.', 'We Brand U documents the whole system.')]
d.page(f'''<div class="d-body">
  <span class="d-k">Principios con ejemplos</span>
  <h2 class="d-h2" style="margin:14px 0 26px">Así sí, así no</h2>
  <table class="d-table"><tr><th style="width:220px">Principio</th><th><span class="d-do">✓ Así</span></th><th><span class="d-dont">✕ Así no</span></th></tr>
  {''.join(f'<tr><td>{p}</td><td style="color:#fff">{a}</td><td class="d-dim">{b}</td></tr>' for p, a, b in pairs)}</table>
  <p class="d-small" style="margin-top:20px">Prueba rápida: si una frase podría estar en el sitio de cualquier otra agencia sin cambiar una palabra, está mal escrita. Se reescribe con algo que solo We Brand U pueda decir.</p>
</div>''', 'Voz y tono')

d.page(f'''<div class="d-body">
  <span class="d-k">Tono por contexto</span>
  <h2 class="d-h2" style="margin:14px 0 30px">La voz es una; el tono se ajusta</h2>
  <div class="d-grid d-g3">
    <div class="d-slab" style="padding:36px"><span class="d-k">Sitio y propuestas</span><h3 class="d-h3" style="margin:12px 0">Claro y sereno</h3><p class="d-p">Explica el programa paso a paso. Frases cortas, datos concretos, sin adjetivos de relleno.</p><p class="d-small d-acc" style="margin-top:16px">“We produce and publish at full volume. We measure what works and adjust.”</p></div>
    <div class="d-slab" style="padding:36px;background:{ACCENT};color:#0B0B0B"><span style="font-size:15px">Out of the Box</span><h3 class="d-h3" style="margin:12px 0">Más audaz</h3><p style="font-size:17px;line-height:1.6;margin:0">Más directo, más corto, más confiado. Nunca grosero ni gritón.</p><p style="font-size:14px;margin-top:16px">“Conversation, not impressions.” “Take the risk.”</p></div>
    <div class="d-slab" style="padding:36px"><span class="d-k">Conversación con partners</span><h3 class="d-h3" style="margin:12px 0">Cercano y honesto</h3><p class="d-p">Dice qué esperamos de su equipo y para quién no es el programa. Prefiere perder una venta a prometer de más.</p></div>
  </div>
</div>''', 'Voz y tono')

d.page(f'''<div class="d-body"><div class="d-split d-split--even">
  <div class="d-col">
    <span class="d-k">Vocabulario</span>
    <h2 class="d-h2">Palabras nuestras</h2>
    <table class="d-table"><tr><th>Decimos</th><th>En lugar de</th></tr>
      <tr><td>partners</td><td>clients</td></tr>
      <tr><td>we</td><td>We Brand U does…</td></tr>
      <tr><td>hand it over / your team runs it</td><td>ongoing management</td></tr>
      <tr><td>three months</td><td>flexible engagement</td></tr>
      <tr><td>pods</td><td>our offices</td></tr>
      <tr><td>measured growth</td><td>more posts</td></tr>
    </table>
  </div>
  <div class="d-col">
    <span class="d-k">Prohibidas</span>
    <h2 class="d-h2">Nunca se usan</h2>
    <div style="display:flex;flex-wrap:wrap;gap:10px">{''.join(f'<span class="d-tag" style="text-decoration:line-through;text-decoration-color:#fff">{w}</span>' for w in ['soluciones integrales', 'sinergia', 'llevamos tu marca al siguiente nivel', 'en el mundo digital de hoy', 'pasión por lo que hacemos', 'no somos una agencia más', 'cutting-edge', 'unlock', 'empower', 'elevate', 'seamless', 'game-changing', 'revolutionary', 'we’re passionate about'])}</div>
    <p class="d-small" style="margin-top:10px">Tampoco sus variantes ni traducciones.</p>
  </div>
</div></div>''', 'Voz y tono')

# ============================ 06 ESCRITURA =================================
divider('06', 'Escritura', 'Largos, puntuación e idioma.')

lens = [('Titulares', 'Máximo 6 palabras', 'Three months. Then it’s yours.'), ('Subtítulos', 'Una frase', 'Your team runs it. If you want backup, there are two options.'),
        ('Párrafos', 'Máximo 3 líneas', 'We audit what you have. We define your identity, message and content lines.'),
        ('Descripción de servicio', '2 o 3 frases', 'Identity, content strategy, social and paid media. For companies whose brand looks improvised.')]
d.page(f'''<div class="d-body">
  <span class="d-k">Largo del texto</span>
  <h2 class="d-h2" style="margin:14px 0 14px">Si hace falta más espacio, la idea no está clara</h2>
  <p class="d-lead" style="margin-bottom:26px">No falta texto: sobra. Estos son los límites.</p>
  <table class="d-table"><tr><th style="width:280px">Pieza</th><th style="width:240px">Límite</th><th>Ejemplo</th></tr>
  {''.join(f'<tr><td>{a}</td><td class="d-acc">{b}</td><td style="color:#fff">{c}</td></tr>' for a, b, c in lens)}</table>
</div>''', 'Escritura')

d.page(f'''<div class="d-body">
  <span class="d-k">Puntuación e idioma</span>
  <h2 class="d-h2" style="margin:14px 0 30px">Reglas fijas</h2>
  <div class="d-grid d-g2" style="gap:24px">
    <div class="d-card"><h3 class="d-h4">Inglés, siempre</h3><p class="d-small" style="margin-top:8px">Todo el producto final —sitio, redes, propuestas— va en inglés. Entre nosotros hablamos en español, pero no se traduce el sitio.</p></div>
    <div class="d-card"><h3 class="d-h4">Sin signos de exclamación</h3><p class="d-small" style="margin-top:8px">La seguridad se transmite con frases firmes, no con signos.</p></div>
    <div class="d-card"><h3 class="d-h4">Sin preguntas retóricas</h3><p class="d-small" style="margin-top:8px">La única excepción es el título que ya existe: “Why work with Us?”. Las preguntas frecuentes son preguntas reales.</p></div>
    <div class="d-card"><h3 class="d-h4">Tipo oración</h3><p class="d-small" style="margin-top:8px">Mayúscula solo al inicio y en nombres propios. Los nombres de servicio y de producto van con mayúscula inicial: The 3-Month Program, Annual Support, Pro Plan.</p></div>
    <div class="d-card"><h3 class="d-h4">Números en cifras</h3><p class="d-small" style="margin-top:8px">1.3M+, 607K, 6 years. Los plazos del programa, en letras en los titulares: “Three months.”</p></div>
    <div class="d-card"><h3 class="d-h4">Comillas y apóstrofes tipográficos</h3><p class="d-small" style="margin-top:8px">It’s, we’ll, “partners”. Nunca comillas rectas.</p></div>
  </div>
</div>''', 'Escritura')

rew = [('Our integrated solutions empower your brand to reach the next level.', 'Three months. Then your team runs it.'),
       ('We’re passionate about creating seamless digital experiences!', 'We build it, run it, and hand it over.'),
       ('Ready to unlock your growth potential?', 'Find what moves the number. Then repeat it.'),
       ('We Brand U delivers cutting-edge AI content.', 'AI-assisted production: volume without losing quality.')]
d.page(f'''<div class="d-body">
  <span class="d-k">Reescrituras</span>
  <h2 class="d-h2" style="margin:14px 0 26px">De genérico a nuestro</h2>
  <div class="d-col" style="gap:0">{''.join(f'<div style="display:grid;grid-template-columns:1fr 60px 1fr;gap:24px;align-items:center;padding:22px 0;border-top:1px solid rgba(0,202,113,.16)"><span class="d-p d-dim" style="text-decoration:line-through">{a}</span>{icon("s-next", 30, ACCENT)}<span style="font-size:24px;line-height:1.3">{b}</span></div>' for a, b in rew)}</div>
</div>''', 'Escritura')

# ============================ 07 MENSAJES ==================================
divider('07', 'Mensajes', 'Frases aprobadas y cómo presentarnos en distintos largos.')

msgs = [('Your Idea. Our Goal.', 'Bienvenida del sitio'), ('Three months. Then it’s yours.', 'Promesa principal'),
        ('Independent, not dependent.', 'Argumento central'), ('Build it. Prove it. Hand it over.', 'El método'),
        ('Proof, not promises.', 'Trabajo y resultados'), ('Talent over titles.', 'Filosofía de los pods'),
        ('Not an office. Pods.', 'El modelo'), ('Take the risk.', 'Out of the Box')]
d.page(f'''<div class="d-body">
  <span class="d-k">Frases aprobadas</span>
  <h2 class="d-h2" style="margin:14px 0 30px">Mensajes clave</h2>
  <div class="d-grid d-g2" style="column-gap:56px;row-gap:0">{''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:22px 0;border-top:1px solid rgba(0,202,113,.16)"><span style="font-size:30px">{a}</span><span class="d-micro">{b}</span></div>' for a, b in msgs)}</div>
</div>''', 'Mensajes')

d.page(f'''<div class="d-body">
  <span class="d-k">Presentarnos</span>
  <h2 class="d-h2" style="margin:14px 0 30px">En tres largos</h2>
  <div class="d-col" style="gap:20px">
    <div class="d-card"><span class="d-k">Una línea</span><p style="font-size:30px;line-height:1.3;margin:10px 0 0">We build your digital presence in three months, then hand it to your trained team.</p></div>
    <div class="d-card"><span class="d-k">Treinta segundos</span><p class="d-p" style="color:#fff;font-size:20px;margin-top:10px">Most companies either pay an agency forever or hire someone who takes a year to figure it out. We do neither. In three months we build your system, run it to prove it works, and train your team to run it. Then you’re independent.</p></div>
    <div class="d-card"><span class="d-k">Para propuestas</span><p class="d-p" style="margin-top:10px">We Brand U is a creative marketing agency that doesn’t work piece by piece. We set up your full digital presence in three months: month one to set it up, month two to run it at full volume, month three to document it and train your local team. After that, you can add a year of support or our Pro Plan. Our pods are hired locally in each market, starting in Europe.</p></div>
  </div>
</div>''', 'Mensajes')

d.page(f'''<div class="d-body">
  <span class="d-k">Lo que no se inventa</span>
  <h2 class="d-h2" style="margin:14px 0 18px">Solo lo que es verdad</h2>
  <p class="d-lead" style="margin-bottom:28px">La confianza se pierde una vez. Estas reglas no tienen excepciones.</p>
  <div class="d-grid d-g2" style="gap:22px">
    <div class="d-card"><h3 class="d-h4">Sin datos ni cifras inventadas</h3><p class="d-small" style="margin-top:8px">Solo los números documentados: 1.3M+, 607K y seis años.</p></div>
    <div class="d-card"><h3 class="d-h4">Sin clientes inventados</h3><p class="d-small" style="margin-top:8px">Los casos se publican cuando existen, con permiso del partner.</p></div>
    <div class="d-card"><h3 class="d-h4">Sin testimonios de relleno</h3><p class="d-small" style="margin-top:8px">Solo citas reales, con nombre y cargo, aprobadas por quien las dijo.</p></div>
    <div class="d-card"><h3 class="d-h4">Sin promesas que no figuran acá</h3><p class="d-small" style="margin-top:8px">Nada de garantías de resultados, plazos distintos ni servicios fuera de los descritos.</p></div>
  </div>
</div>''', 'Mensajes')

# ============================ 08 CHECKLIST =================================
checks = ['Vuelve al argumento central: el partner termina independiente.',
          'Está en inglés, en primera persona del plural (“we”).',
          'Dice “partners”, nunca “clients”.',
          'Ningún titular pasa de 6 palabras; ningún párrafo de 3 líneas.',
          'No tiene signos de exclamación ni preguntas retóricas.',
          'No usa ninguna palabra prohibida.',
          'No podría estar en el sitio de otra agencia sin cambios.',
          'Todo dato, cifra y nombre es verdadero y está permitido.',
          'No identifica al empleador anterior ni a sus clientes.',
          'Si habla del programa, dice el plazo: tres meses.']
d.page(f'''<div class="d-body">
  <span class="d-k">08 · Checklist</span>
  <h2 class="d-h2" style="margin:14px 0 26px">Antes de publicar un texto</h2>
  <div class="d-grid d-g2" style="column-gap:56px;row-gap:0">{''.join(f'<div style="display:flex;gap:18px;padding:17px 0;border-top:1px solid rgba(0,202,113,.16)"><span class="d-num">{i:02d}</span><span class="d-p" style="color:#fff">{c}</span></div>' for i, c in enumerate(checks, 1))}</div>
</div>''', 'Checklist')

d.page(f'''{arcs(800, 450, (200, 340, 500, 680), .3, thick=760)}
<div class="d-body" style="align-items:center;text-align:center;gap:34px">
  {logo(160)}
  <p class="d-h2">Three months. Then it’s yours.</p>
  <p class="d-micro">We Brand U · Guía de marca · Versión 1.0 · 2026</p>
</div>''', bare=True)

DOC = d
