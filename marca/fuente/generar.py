"""Genera los dos documentos de marca en PDF.

Uso (desde la raíz del repo):
    python3 marca/fuente/generar.py

Necesita Node + Playwright (Chromium) para convertir HTML a PDF, y la
fuente Inter instalada en el sistema.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from base import partial  # noqa: E402
import linea_grafica  # noqa: E402
import guia_marca  # noqa: E402
from pypdf import PdfReader, PdfWriter  # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, '..'))
svg_defs = partial('svg-defs')

docs = [
    (linea_grafica.DOC, 'linea-grafica', 'We Brand U — Línea gráfica', 'Sistema visual de We Brand U'),
    (guia_marca.DOC, 'guia-de-marca', 'We Brand U — Guía de marca', 'Esencia, oferta, audiencia y voz de We Brand U'),
]
jobs = []
for doc, slug, title, subject in docs:
    html_path = os.path.join(HERE, f'{slug}.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(doc.render(svg_defs))
    jobs.append((html_path, os.path.join(OUT, f'WeBrandU-{slug}.pdf'), title, subject))

render_js = os.path.join(HERE, 'render.js')
for html_path, pdf_path, title, subject in jobs:
    subprocess.run(['node', render_js, html_path, pdf_path + '.tmp'], check=True)
    # metadatos limpios: solo la marca
    reader = PdfReader(pdf_path + '.tmp')
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata({'/Title': title, '/Author': 'We Brand U', '/Subject': subject,
                         '/Creator': 'We Brand U', '/Producer': 'We Brand U'})
    with open(pdf_path, 'wb') as f:
        writer.write(f)
    os.unlink(pdf_path + '.tmp')
    print(f'✓ {os.path.relpath(pdf_path)} · {len(reader.pages)} páginas')
