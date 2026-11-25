# We Brand U — landing

Landing estática (HTML + CSS + JS vanilla, sin build ni dependencias) implementada desde las capturas de Figma en [`diseno/`](diseno/).

## Levantarlo local

Desde esta carpeta (`we-brand-u/`):

```bash
python3 -m http.server 8000
```

Abrir http://localhost:8000. Cualquier servidor estático sirve (`npx serve .`, Live Server de VS Code, etc.). Abrir `index.html` con doble clic también funciona.

## Estructura

| Archivo | Qué es |
|---|---|
| `index.html` | Las 6 secciones, con las ilustraciones como SVG inline (animables) |
| `css/styles.css` | Sistema visual, layout, estados y animaciones |
| `js/main.js` | Interacción: estados de Servicios y Why, carrusel, rail, disparo con IntersectionObserver |
| `js/imagenes.js` | **Todas las imágenes en un solo lugar** (ver abajo) |
| `diseno/` | Capturas de referencia del Figma |

## Cambiar las imágenes

Todo está en `js/imagenes.js`. Mientras `src` esté vacío se ve un placeholder claro con el nombre del slot y las dimensiones. Para poner la final, completar `src` (p. ej. `'img/trabajo-1.jpg'`). La caja del slot ya tiene la proporción final, así que el layout no se mueve.

Slots: `hero-bg` (2480×1400), `trabajo-1…5` (1080×1080), `testimonio-1…3` (480×480).

## Interacción

- **Navegación por vistas** (escritorio): la página no scrollea. Cada sección ocupa una pantalla y un gesto de rueda o trackpad (o ↓ / ↑, Re Pág / Av Pág, espacio, swipe) desliza a la vista siguiente o anterior con una transición de 1 s. Sin barra de scroll. En mobile el scroll es normal.
- **Servicios** y **Why work with Us?**: hover en desktop, tap en mobile/touch. La tarjeta activa se expande con descripción e ilustración y las otras se contraen. Al sacar el mouse de la sección vuelve al estado base.
- **Why**: rueda cíclica sobre el arco (arriba = anterior, centro = activo, abajo = siguiente), como en las 3 capturas.
- **Testimonios**: clic/tap en un lateral, swipe o flechas del teclado. Avanza solo cada 7 s cuando está en pantalla (se pausa con hover o foco).
- Las animaciones de entrada se disparan una sola vez con IntersectionObserver. Con `prefers-reduced-motion` todo aparece directamente en su estado final, sin animaciones en loop.

## Pendientes (copy y decisiones a confirmar)

Están marcados en el HTML con `<!-- COPY PENDIENTE -->` / clase `pending`.

1. Descripciones de los 3 servicios: no se leen en la captura.
2. Cargos de los 3 testimonios: no se leen.
3. Textos de Why: en la captura, *Fast Execution* muestra "We tailor every strategy…" y *Customized Solutions* muestra "Speed matters…". Acá están asignados según el sentido de cada uno (invertidos respecto de la captura).
4. Cita de Alejandro Torres: transcripta de una captura de baja resolución.
5. Valores del inspector (Customized Solutions): las etiquetas se leen a medias; usé los hex de la paleta.
6. Envío del formulario: dispara el evento `wbu:submit` con los datos; falta definir a dónde se manda.
