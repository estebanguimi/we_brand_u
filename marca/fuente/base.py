"""Piezas compartidas de los documentos de marca de We Brand U.

Cada página es una lámina 16:9 (1600×900 px) con el mismo sistema que el
sitio: negro pleno, losas charcoal, un solo acento verde, Inter 600 y
Inter 900 italic, arcos orbitales e íconos de la librería del sitio.
"""
import html
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, 'src', 'partials')


def partial(name):
    with open(os.path.join(SRC, name + '.html'), encoding='utf-8') as f:
        return f.read()


ACCENT = '#00CA71'
ACCENT_DARK = '#006337'

LOGO_PATHS = (
    '<path d="M0 20Q0 0 20 0H155Q175 0 175 20V432A127.5 127.5 0 0 0 424 470L610 410V425A305 305 0 0 1 0 425Z"/>'
    '<path d="M430 20Q430 0 450 0H590Q610 0 610 20V120L430 50Z"/>'
    '<path d="M430 150L430 215L525 182Z"/>'
    '<path d="M430 310L430 380L525 345Z"/>'
    '<path d="M570 265L610 250V280Z"/>'
)


def logo(w, color=ACCENT, extra=''):
    h = w * 730 / 610
    return f'<svg viewBox="0 0 610 730" width="{w:.0f}" height="{h:.0f}" fill="{color}" {extra}>{LOGO_PATHS}</svg>'


def lockup(size, color=ACCENT, text='#FFFFFF'):
    """Símbolo + nombre. size = alto del símbolo en px."""
    w = size * 610 / 730
    return (f'<span class="d-lockup" style="--s:{size}px">{logo(w, color)}'
            f'<span style="color:{text}">We Brand U</span></span>')


def icon(sym, size=28, color='currentColor'):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="{color}"><use href="#{sym}"/></svg>'


def arcs(cx=1200, cy=450, radii=(260, 430, 640), opacity=.3, thick=None, glow=True, w=1600, h=900):
    """Arcos orbitales (mismo motivo del sitio)."""
    out = [f'<svg class="d-arcs" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice">']
    if glow:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{radii[0]}" fill="url(#g-glow)" opacity=".45"/>')
    for i, r in enumerate(radii):
        circ = 2 * 3.14159 * r
        dash = circ * (0.62 if i % 2 == 0 else 0.48)
        rot = [20, 140, 260, 60][i % 4]
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{ACCENT}" stroke-opacity="{opacity}" '
                   f'stroke-width="1.6" stroke-dasharray="{dash:.0f} {circ - dash:.0f}" transform="rotate({rot} {cx} {cy})"/>')
    if thick:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{thick}" fill="none" stroke="url(#g-ring)" stroke-width="44" transform="rotate(200 {cx} {cy})"/>')
    out.append('</svg>')
    return ''.join(out)


CSS = r"""
@page { size: 1600px 900px; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #000; }
body { font-family: 'Inter', sans-serif; font-weight: 600; color: #fff; -webkit-font-smoothing: antialiased; }
.pg {
  position: relative; width: 1600px; height: 900px; overflow: hidden;
  background: #000; padding: 64px 88px 72px;
  page-break-after: always; break-after: page;
  display: flex; flex-direction: column;
}
.pg:last-child { page-break-after: auto; break-after: auto; }
.d-arcs { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }
.d-head { position: relative; z-index: 2; display: flex; justify-content: space-between; align-items: center;
  font-size: 13px; color: #6B6B6B; letter-spacing: .02em; }
.d-head b { color: #fff; font-weight: 600; display: inline-flex; align-items: center; gap: 10px; }
.d-foot { position: absolute; z-index: 2; left: 88px; right: 88px; bottom: 32px; display: flex; justify-content: space-between;
  font-size: 12px; color: #6B6B6B; }
.d-body { position: relative; z-index: 1; flex: 1; display: flex; flex-direction: column; justify-content: center; }
.d-k { color: #00CA71; font-size: 15px; letter-spacing: .02em; }
.d-num { color: #00CA71; font-size: 15px; font-variant-numeric: tabular-nums; }
.d-h1 { font-size: 104px; line-height: 1.08; margin: 0; letter-spacing: .002em; }
.d-h2 { font-size: 58px; line-height: 1.12; margin: 0; }
.d-h3 { font-size: 28px; line-height: 1.22; margin: 0; }
.d-h4 { font-size: 20px; line-height: 1.3; margin: 0; }
.d-lead { font-size: 22px; line-height: 1.5; color: #C9C9C9; margin: 0; max-width: 900px; }
.d-p { font-size: 17px; line-height: 1.6; color: #C9C9C9; margin: 0; }
.d-p + .d-p { margin-top: 14px; }
.d-small { font-size: 14px; line-height: 1.5; color: #C9C9C9; margin: 0; }
.d-micro { font-size: 12px; line-height: 1.4; color: #6B6B6B; margin: 0; }
.d-it { font-style: italic; font-weight: 900; }
.d-dim { color: #6B6B6B; }
.d-acc { color: #00CA71; }
.d-slab { position: relative; background: #0B0B0B; border-radius: 28px; overflow: hidden; }
.d-card { border: 1px solid rgba(0,202,113,.16); border-radius: 22px; padding: 26px 28px;
  background: linear-gradient(to bottom, transparent, rgba(255,255,255,.012)); }
.d-card--strong { border-color: rgba(0,202,113,.5); }
.d-grid { display: grid; gap: 22px; }
.d-g2 { grid-template-columns: repeat(2, minmax(0,1fr)); }
.d-g3 { grid-template-columns: repeat(3, minmax(0,1fr)); }
.d-g4 { grid-template-columns: repeat(4, minmax(0,1fr)); }
.d-g5 { grid-template-columns: repeat(5, minmax(0,1fr)); }
.d-row { display: flex; gap: 48px; align-items: center; }
.d-col { display: flex; flex-direction: column; gap: 18px; }
.d-split { display: grid; grid-template-columns: 1fr 1.15fr; gap: 72px; align-items: center; }
.d-split--even { grid-template-columns: 1fr 1fr; }
.d-line { height: 1px; background: rgba(0,202,113,.16); }
.d-list { list-style: none; padding: 0; margin: 0; display: grid; }
.d-list li { font-size: 17px; line-height: 1.5; color: #C9C9C9; padding: 12px 0; border-top: 1px solid rgba(0,202,113,.16); }
.d-list li:last-child { border-bottom: 1px solid rgba(0,202,113,.16); }
.d-list li b { color: #fff; font-weight: 600; }
.d-pill { display: inline-flex; align-items: center; justify-content: center; white-space: nowrap; padding: 18px 34px;
  border-radius: 999px; border: 1px solid rgba(255,255,255,.28); background: #0B0B0B; color: #fff; font-size: 18px; line-height: 1; }
.d-pill--accent { background: #00CA71; color: #0B0B0B; border-color: #00CA71; }
.d-lockup { display: inline-flex; align-items: center; gap: calc(var(--s) * .32); font-size: calc(var(--s) * .62); line-height: 1; }
.d-tag { display: inline-flex; padding: 7px 14px; border-radius: 999px; border: 1px solid rgba(0,202,113,.3); font-size: 13px; color: #C9C9C9; }
.d-do, .d-dont { font-size: 13px; display: inline-flex; gap: 8px; align-items: center; }
.d-do { color: #00CA71; }
.d-dont { color: #fff; }
.d-x { position: relative; }
.d-x::before, .d-x::after { content: ""; position: absolute; left: -6%; right: -6%; top: 50%; height: 2px; background: #fff;
  transform: rotate(-24deg); z-index: 3; }
.d-x::after { transform: rotate(24deg); }
.d-shot { width: 100%; display: block; border-radius: 18px; border: 1px solid rgba(0,202,113,.16); }
.d-sw { border-radius: 22px; height: 210px; display: flex; flex-direction: column; justify-content: flex-end; padding: 22px;
  border: 1px solid rgba(255,255,255,.08); }
.d-sw b { font-size: 20px; font-weight: 600; }
.d-sw span { font-size: 13px; line-height: 1.5; opacity: .8; font-variant-numeric: tabular-nums; }
.d-toc { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); column-gap: 80px; }
.d-toc div { display: flex; gap: 22px; align-items: baseline; padding: 15px 0; border-top: 1px solid rgba(0,202,113,.16);
  font-size: 21px; }
.d-toc div span:first-child { color: #00CA71; font-size: 15px; width: 34px; font-variant-numeric: tabular-nums; }
.d-toc div span:last-child { margin-left: auto; color: #6B6B6B; font-size: 14px; }
.d-quote { font-size: 44px; line-height: 1.2; margin: 0; }
.d-ill { width: 100%; height: auto; overflow: visible; }
.d-cover-meta { display: flex; gap: 56px; font-size: 14px; color: #6B6B6B; }
.d-cover-meta b { display: block; color: #fff; font-weight: 600; font-size: 16px; margin-top: 6px; }
.d-spec { font-variant-numeric: tabular-nums; }
.d-table { width: 100%; border-collapse: collapse; }
.d-table td, .d-table th { text-align: left; padding: 14px 12px 14px 0; border-top: 1px solid rgba(0,202,113,.16); font-size: 16px;
  color: #C9C9C9; vertical-align: top; font-weight: 600; }
.d-table th { color: #6B6B6B; font-size: 13px; }
.d-table td:first-child { color: #fff; }
"""


class Doc:
    def __init__(self, title, short):
        self.title = title          # p. ej. "Línea gráfica"
        self.short = short
        self.pages = []

    def page(self, body, section='', bare=False, bg='', klass=''):
        self.pages.append((body, section, bare, bg, klass))

    def render(self, svg_defs):
        n = len(self.pages)
        out = []
        for i, (body, section, bare, bg, klass) in enumerate(self.pages, 1):
            head = '' if bare else (
                f'<div class="d-head"><b>{logo(15)} We Brand U</b><span>{html.escape(self.title)}'
                f'{" · " + html.escape(section) if section else ""}</span></div>')
            foot = '' if bare else (
                f'<div class="d-foot"><span>We Brand U — {html.escape(self.title)}</span>'
                f'<span class="d-spec">{i:02d} / {n:02d}</span></div>')
            style = f' style="background:{bg}"' if bg else ''
            out.append(f'<section class="pg {klass}"{style}>{head}{body}{foot}</section>')
        return (
            '<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<title>We Brand U — {html.escape(self.title)}</title>'
            '<link rel="stylesheet" href="../../css/styles.css">'
            f'<style>{CSS}</style></head><body>'
            f'{svg_defs}{"".join(out)}</body></html>'
        )
