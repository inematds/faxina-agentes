// Mede o guia publicado: rolagem lateral (scrollWidth - innerWidth) de 390 a 1920 px e imagens carregadas, PT/EN/ES.
// Uso: node tests/medir_guia.mjs [url-base]   (padrão: https://inematds.github.io/faxina-agentes/guia/)
import { chromium } from 'playwright';
const base = process.argv[2] || 'https://inematds.github.io/faxina-agentes/guia/';
const larguras = [390, 768, 800, 1024, 1280, 1440, 1920];
const b = await chromium.launch();
let falhas = 0;
for (const l of ['', 'en/', 'es/']) {
  for (const w of larguras) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    const r = await p.goto(base + l, { waitUntil: 'networkidle' });
    await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } });
    await p.waitForTimeout(600);
    const m = await p.evaluate(() => ({
      over: document.documentElement.scrollWidth - innerWidth,
      quebradas: [...document.images].filter(i => !(i.complete && i.naturalWidth > 0)).map(i => i.getAttribute('src')),
    }));
    const ok = r.status() === 200 && m.over <= 0 && m.quebradas.length === 0;
    if (!ok) falhas++;
    console.log(`${l || 'pt/'} ${w}px status=${r.status()} over=${m.over} quebradas=${m.quebradas.join(',') || 0} ${ok ? 'OK' : 'FALHA'}`);
    await p.close();
  }
}
await b.close();
console.log(falhas ? `FALHAS ${falhas}` : 'TUDO OK');
process.exit(falhas ? 1 : 0);
