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
| `/servicios/` | Hub |
| `/servicios/branding-marketing/`, `/tech-automation/`, `/business-growth/` | Plantilla única (`src/templates/servicio.html`) |
| `/programa/` | El programa de 3 meses |
| `/contacto/` | Evaluación gratuita en 4 pasos |
| `/out-of-the-box/`, `/trabajo/`, `/nosotros/` | Provisorias (Fase 2) |
| `/blog/`, `/privacidad/`, `/terminos/` | Provisorias (Fase 3) |

Los links internos se escriben `{{base}}ruta/` y el build los vuelve relativos, así funcionan en `github.io/we_brand_u/` y en un dominio propio. Si cambiás de dominio, actualizá `url` en `src/site.json` (lo usan el sitemap y Open Graph).

## Cambiar las imágenes

Todo en `js/imagenes.js`. Mientras `src` esté vacío se ve un placeholder con el nombre del slot y sus dimensiones; la caja ya tiene la proporción final. Para Open Graph, `og-default` (1200×630).

## Interacción

- **Home**: navegación por vistas en escritorio (un gesto = una vista, sin barra de scroll). Las páginas internas tienen scroll normal.
- **Rail**: navegación del sitio; marca la página activa y muestra el nombre al pasar el mouse. En mobile es una barra inferior con Home, Services, The Program, Contact y un botón "más" con el resto.
- **Tarjetas de servicio** (home y `/servicios`): hover/tap expande; click lleva a la página del servicio (en touch: primer tap expande, segundo navega).
- **Ilustraciones de servicio** en su página: el mismo SVG del home, se expande y anima una vez al entrar en vista.
- **Timeline** (`/programa`, "How we work"): el arco se dibuja y los hitos se encienden al entrar en vista.
- `prefers-reduced-motion`: todo aparece en su estado final, sin loops.

## Contenido pendiente

Todo lo que falta está marcado en el texto como `[FALTA CONTENIDO: …]` (clase `pending`) y los precios como `[PRECIO-PROGRAMA]`, `[PRECIO-SOPORTE]`, `[PRECIO-PRO]`.
