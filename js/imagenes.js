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

  // 1 · Hero — OPCIONAL. Sin src se ve el dashboard desenfocado dibujado en
  //     SVG (index.html, .hero-dash). Con src, la imagen lo tapa.
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

  // ---------------------------------------------------------------
  // PÁGINAS INTERNAS
  // ---------------------------------------------------------------

  // /trabajo — un juego de slots por caso: '<slug>-portada' y '<slug>-pieza-N'.
  // Al copiar el caso plantilla, duplicá estas líneas con el slug nuevo.
  'caso-ejemplo-portada': { src: '', w: 1600, h: 900,  alt: '' }, // grilla y hero del caso
  'caso-ejemplo-pieza-1': { src: '', w: 1080, h: 1080, alt: '' },
  'caso-ejemplo-pieza-2': { src: '', w: 1080, h: 1080, alt: '' },
  'caso-ejemplo-pieza-3': { src: '', w: 1080, h: 1080, alt: '' },
  'caso-ejemplo-pieza-4': { src: '', w: 1080, h: 1080, alt: '' },

  // /nosotros — fotos del equipo (cuadradas)
  'equipo-1':     { src: '', w: 480, h: 480, alt: '' },
  'equipo-2':     { src: '', w: 480, h: 480, alt: '' },
  'equipo-3':     { src: '', w: 480, h: 480, alt: '' },
  'equipo-4':     { src: '', w: 480, h: 480, alt: '' },
  'equipo-5':     { src: '', w: 480, h: 480, alt: '' },
  'equipo-6':     { src: '', w: 480, h: 480, alt: '' },

  // /blog — un slot por artículo: '<slug>-portada' (listado y artículo).
  // Al copiar el artículo plantilla, duplicá esta línea con el slug nuevo.
  'post-ejemplo-portada': { src: '', w: 1600, h: 900, alt: '' },

  // Open Graph — la imagen que aparece al compartir cualquier página.
  // Sin src, build.mjs usa img/placeholders/og-default.png (placeholder).
  // Ruta relativa a la raíz del sitio, p. ej. 'img/og.jpg'.
  'og-default':   { src: '', w: 1200, h: 630, alt: 'We Brand U' },
};
