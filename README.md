# We Brand U — sitio web

Sitio estático (HTML + CSS + JS vanilla). Un build propio sin dependencias arma todas las páginas desde `src/`. Las capturas de Figma en [`diseno/`](diseno/) quedan como referencia histórica; el sistema del sitio es la fuente de verdad.

Publicado en GitHub Pages: https://estebanguimi.github.io/we_brand_u/

## Editar y publicar

1. Editá lo que necesites en `src/` (páginas, piezas compartidas, datos).
2. Generá el sitio:

   ```bash
   node build.mjs
   ```

3. Subí todo (incluidas las carpetas generadas). GitHub Pages publica solo.

**No edites a mano** los `index.html` generados (raíz, `servicios/`, `programa/`, etc.): se pisan en cada build.

## Verlo local

```bash
node build.mjs
python3 -m http.server 8000
```

Abrir http://localhost:8000.

## Estructura

| Ruta | Qué es |
|---|---|
| `build.mjs` | El build (solo Node, sin instalar nada) |
| `src/site.json` | Nombre, URL pública, **navegación del rail** (orden, íconos, cuáles van en la barra mobile) |
| `src/layout.html` | Esqueleto común: `<head>` con title, description y Open Graph, rail, footer, scripts |
| `src/pages/` | Una página por archivo. 1ª línea: `<!--page {...} -->` con ruta, título, descripción y sección del rail |
| `src/templates/` + `src/data/` | Páginas que salen de una plantilla + datos (p. ej. las 3 de servicio) |
| `src/partials/` | Piezas compartidas: ilustraciones, tarjetas de servicio, arcos, CTA, footer |
| `css/styles.css` | **Único** sistema de estilos: tokens en `:root`, componentes, patrones |
| `js/main.js` | Interacción y animación |
| `js/imagenes.js` | **Todas las imágenes en un solo lugar** (también la de Open Graph) |
| `sitemap.xml`, `robots.txt` | Generados por el build |

## Rutas

| Ruta | Estado |
|---|---|
| `/` | Home |
| `/servicios/` | Los tres servicios en una sola página (datos en `src/data/servicio.json`). Las direcciones viejas `/servicios/<servicio>/` redirigen a su sección |
| `/programa/` | El programa de 3 meses |
| `/contacto/` | Evaluación gratuita en 4 pasos |
| `/trabajo/` | Grilla de casos (un elemento por caso en `src/data/caso.json`) |
| `/trabajo/caso-ejemplo/` | Caso plantilla (`src/templates/caso.html`) |
| `/nosotros/` | Pods, filosofía, equipo |
| `/out-of-the-box/` | División premium (la única página "audaz") |
| `/blog/` | Listado (`src/data/post.json`) |
| `/blog/post-ejemplo/` | Artículo plantilla (`src/templates/post.html`) |
| `/privacidad/`, `/terminos/` | Legales, texto plano |

Los links internos se escriben `{{base}}ruta/` y el build los vuelve relativos, así funcionan en `github.io/we_brand_u/` y en un dominio propio. Si cambiás de dominio, actualizá `url` en `src/site.json` (lo usan el sitemap y Open Graph).

## Sumar un caso o un artículo

1. Agregá un elemento en `src/data/caso.json` (o `post.json`) con su `slug`.
2. Sumá sus imágenes en `js/imagenes.js` (`<slug>-portada`, y para casos `<slug>-pieza-1…4`).
3. `node build.mjs`: aparece en la grilla/listado, tiene su página, y el "siguiente caso" se enlaza solo.

## Cambiar las imágenes

Todo en `js/imagenes.js`. Mientras `src` esté vacío se ve un placeholder con el nombre del slot y sus dimensiones; la caja ya tiene la proporción final. Para Open Graph, `og-default` (1200×630).

## Interacción

- **Navegación por vistas en todo el sitio** (escritorio): la página no scrollea; un gesto de rueda/trackpad, ↓/↑, Av/Re Pág o espacio desliza a la vista siguiente. Cada bloque ocupa una pantalla; si un bloque es más alto (precios, un artículo) se recorre en pasos de una pantalla sin saltear contenido. Sin barra de scroll. En mobile el scroll es normal.
- **Rail**: en el home, las 6 secciones (el brillo sigue a la vista activa) y, bajo una línea, las páginas del sitio. En las internas, la navegación del sitio con la página activa. En mobile es una barra inferior con un botón "más".
- **Tarjetas de servicio**: en el home, hover/click/tap expande (como la primera versión). En `/servicios`, hover expande y click lleva a la página del servicio (en touch: primer tap expande, segundo navega).
- **Ilustraciones de servicio** en su página: el mismo SVG del home, se expande y anima una vez al entrar en vista.
- **Timeline** (`/programa`, "How we work"): el arco se dibuja y los hitos se encienden al entrar en vista.
- `prefers-reduced-motion`: todo aparece en su estado final, sin loops.

## Copy

Todo el texto sale del documento de marca (inglés, voz directa, "partners", sin palabras prohibidas). Lo que el documento no cubre está marcado como `[FALTA CONTENIDO: …]` (clase `pending`):

- Casos reales (cliente, problema, enfoque, resultado, piezas)
- Nombres, roles y fotos del equipo
- Testimonios reales del home (los del diseño eran de relleno)
- Precios confirmados: `[PRECIO-PROGRAMA]`, `[PRECIO-SOPORTE]`, `[PRECIO-PRO]`
- Artículos del blog
- Texto legal de Privacidad y Términos
- Email, teléfono/WhatsApp y redes del footer
