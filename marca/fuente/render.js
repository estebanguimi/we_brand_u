// Convierte un HTML de láminas 1600×900 a PDF con Chromium (Playwright).
// Uso: node render.js entrada.html salida.pdf
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [, , input, output] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });
  await page.goto('file://' + path.resolve(input), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  await page.pdf({ path: output, width: '1600px', height: '900px', printBackground: true, preferCSSPageSize: true });
  await browser.close();
})();
