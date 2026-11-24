/* =====================================================================
   IMÁGENES — ÚNICO LUGAR PARA CAMBIARLAS
   ---------------------------------------------------------------------
   Cada slot del HTML (data-slot="…") toma su imagen de acá.
   · Mientras `src` esté vacío se muestra un placeholder claro con el
     nombre del slot y las dimensiones requeridas.
   · Para poner la imagen final: completá `src` (ruta relativa a
     index.html, p. ej. 'img/hero-bg.jpg') y, si querés, `alt`.
   · `w` y `h` son las dimensiones de exportación pedidas. La caja del
     slot usa esa misma proporción, así que la imagen final ocupa
     EXACTAMENTE el mismo espacio que el placeholder (salvo hero-bg,
     que cubre toda la losa del hero con object-fit: cover).
   ===================================================================== */
window.WBU_IMAGES = {

  // 1 · Hero — fondo de la losa (captura: dashboard desenfocado)
  'hero-bg':      { src: '', w: 2480, h: 1400, alt: '' },

  // 4 · See Our Work in Action — publicaciones (cuadradas, formato post)
  'trabajo-1':    { src: '', w: 1080, h: 1080, alt: '' }, // "Why Branding" (arriba izq.)
  'trabajo-2':    { src: '', w: 1080, h: 1080, alt: '' }, // "Top 3 Emerging Trends" (arriba der.)
  'trabajo-3':    { src: '', w: 1080, h: 1080, alt: '' }, // "Día de la Independencia" (izq.)
  'trabajo-4':    { src: '', w: 1080, h: 1080, alt: '' }, // post naranja (der.)
  'trabajo-5':    { src: '', w: 1080, h: 1080, alt: '' }, // "Feliz San Valentín" (abajo izq.)

  // 5 · What our partners say — fotos (marco redondeado)
  'testimonio-1': { src: '', w: 480, h: 480, alt: 'Alejandro Torres' },
  'testimonio-2': { src: '', w: 480, h: 480, alt: 'Sofía Ramírez' },
  'testimonio-3': { src: '', w: 480, h: 480, alt: 'Mariana López' },
};
