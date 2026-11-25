#!/usr/bin/env node
/* =====================================================================
   We Brand U — build del sitio (sin dependencias: solo Node).

   Uso:   node build.mjs

   Toma src/ y genera las páginas estáticas en la raíz del repo, con rutas
   limpias (servicios/index.html → /servicios/). Lo generado se sube al
   repo tal cual, así GitHub Pages lo sirve sin configuración.

   Sintaxis de las plantillas (src/pages, src/templates, src/partials):
     <!--page {...json...} -->   metadatos de la página (1ª línea)
     {{> nombre}}                incluye src/partials/nombre.html
     {{clave}} / {{a.b}}         variable (de la página, del sitio o de datos)
     {{base}}                    prefijo relativo a la raíz ("", "../", …)

   Los links internos se escriben siempre como {{base}}ruta/ para que
   funcionen igual en estebanguimi.github.io/we_brand_u/ y en un dominio.
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const SRC = path.join(ROOT, 'src');
const read = (p) => fs.readFileSync(p, 'utf8');
const site = JSON.parse(read(path.join(SRC, 'site.json')));

/* Imágenes: el único lugar es js/imagenes.js (también para Open Graph) */
const imgCtx = { window: {} };
vm.runInNewContext(read(path.join(ROOT, 'js/imagenes.js')), imgCtx);
const IMAGES = imgCtx.window.WBU_IMAGES;

/* Versión para que el navegador no use CSS/JS viejos de la caché */
const version = crypto.createHash('sha1')
  .update(read(path.join(ROOT, 'css/styles.css')))
  .update(read(path.join(ROOT, 'js/main.js')))
  .update(read(path.join(ROOT, 'js/imagenes.js')))
  .digest('hex').slice(0, 8);

/* ---------- motor de plantillas mínimo ---------- */
const partials = {};
for (const f of fs.readdirSync(path.join(SRC, 'partials'))) {
  partials[f.replace(/\.html$/, '')] = read(path.join(SRC, 'partials', f));
}
const lookup = (ctx, key) => key.split('.').reduce((o, k) => (o == null ? undefined : o[k]), ctx);

function render(tpl, ctx) {
  let out = tpl;
  for (let pass = 0; pass < 8; pass++) {
    const before = out;
    out = out.replace(/\{\{>\s*([\w-]+)\s*\}\}/g, (m, name) => {
      if (!(name in partials)) throw new Error(`partial inexistente: ${name}`);
      return partials[name];
    });
    out = out.replace(/\{\{\s*([\w.-]+)\s*\}\}/g, (m, key) => {
      const v = lookup(ctx, key);
      if (v === undefined) throw new Error(`variable sin valor: ${key}`);
      return String(v);
    });
    if (out === before) return out;
  }
  return out;
}

function parsePage(file) {
  const raw = read(file);
  const m = raw.match(/^<!--page\s+([\s\S]*?)\s*-->\n?/);
  if (!m) throw new Error(`falta <!--page {...} --> en ${file}`);
  return { meta: JSON.parse(m[1]), body: raw.slice(m[0].length) };
}

/* ---------- navegación (rail + footer) ---------- */
function railHtml(active) {
  const link = (n, extra = '') => {
    const on = n.key === active;
    return `<a href="{{base}}${n.path}" class="rail-link${on ? ' is-active' : ''}"`
      + ` data-nav="${n.key}"${n.primary ? ' data-primary' : ''}`
      + `${on ? ' aria-current="page"' : ''} aria-label="${n.label}">`
      + `<svg viewBox="${n.viewBox || '0 0 24 24'}" class="rail-ico${n.key === 'home' ? ' rail-ico--u' : ''}" aria-hidden="true">${n.icon}</svg>`
      + `${extra}</a>`;
  };
  const items = site.nav.map((n) => link(n, `<span class="rail-tip">${n.label}</span>`)).join('\n    ');
  const sheet = site.nav.map((n) => link(n, `<span class="rail-sheet-label">${n.label}</span>`)).join('\n      ');
  return `<nav class="rail" aria-label="Site">
  <span class="rail-glow-wrap" aria-hidden="true"><span class="rail-glow"></span></span>
    ${items}
  <button type="button" class="rail-more" aria-expanded="false" aria-controls="rail-sheet" aria-label="More pages">
    <svg viewBox="0 0 24 24" class="rail-ico" aria-hidden="true"><circle cx="5" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19" cy="12" r="2"/></svg>
  </button>
  <div class="rail-sheet" id="rail-sheet" hidden>
      ${sheet}
  </div>
</nav>`;
}

/* ---------- páginas ---------- */
const pages = [];
function addPage(meta, body, extraCtx = {}) {
  pages.push({ meta, body, extraCtx });
}
// páginas sueltas: src/pages/**.html
(function walk(dir) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) walk(p);
    else if (f.endsWith('.html')) { const { meta, body } = parsePage(p); addPage(meta, body); }
  }
})(path.join(SRC, 'pages'));
// páginas desde plantilla + datos: src/templates/<t>.html + src/data/<t>.json
for (const f of fs.readdirSync(path.join(SRC, 'templates'))) {
  const name = f.replace(/\.html$/, '');
  const { meta, body } = parsePage(path.join(SRC, 'templates', f));
  const items = JSON.parse(read(path.join(SRC, 'data', `${name}.json`)));
  for (const item of items) {
    const m = JSON.parse(render(JSON.stringify(meta), { item }));
    addPage(m, body, { item });
  }
}

const layout = read(path.join(SRC, 'layout.html'));
const abs = (p) => site.url.replace(/\/$/, '') + '/' + p;

function ogImage() {
  const cfg = IMAGES['og-default'];
  return { src: cfg.src || 'img/placeholders/og-default.png', w: cfg.w, h: cfg.h };
}

const written = [];
for (const { meta, body, extraCtx } of pages) {
  const depth = meta.path ? meta.path.split('/').filter(Boolean).length : 0;
  const base = '../'.repeat(depth);
  const og = ogImage();
  const ctx = {
    ...extraCtx,
    site, version, base,
    page: {
      ...meta,
      fullTitle: meta.path ? `${meta.title} — ${site.name}` : meta.title,
      url: abs(meta.path),
      ogType: meta.ogType || 'website',
      ogImage: abs(og.src), ogImageW: og.w, ogImageH: og.h,
      htmlClass: meta.paged ? 'page-home' : 'page-inner',
      paged: meta.paged ? ' data-paged' : '',
    },
    rail: railHtml(meta.nav),
  };
  ctx.content = render(body, ctx);
  const html = render(layout, ctx);
  const outDir = path.join(ROOT, meta.path);
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(path.join(outDir, 'index.html'), html);
  written.push(meta.path);
}

/* ---------- sitemap.xml + robots.txt ---------- */
const today = new Date().toISOString().slice(0, 10);
fs.writeFileSync(path.join(ROOT, 'sitemap.xml'),
  '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
  + written.sort().map((p) => `  <url><loc>${abs(p)}</loc><lastmod>${today}</lastmod></url>`).join('\n')
  + '\n</urlset>\n');
fs.writeFileSync(path.join(ROOT, 'robots.txt'), `User-agent: *\nAllow: /\n\nSitemap: ${abs('sitemap.xml')}\n`);

console.log(`✓ ${written.length} páginas · versión ${version}`);
written.sort().forEach((p) => console.log('  /' + p));
