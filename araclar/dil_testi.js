// assets/dil.js davranis testi: saat dilimi + tarayici dili + secim. Yerelde ya da canlida calisir.
//   node araclar/dil_testi.js                         -> yerel (kendi sunucusunu 127.0.0.1:8766'da acar)
//   node araclar/dil_testi.js https://vefaglobal.com  -> canli
const http = require('http'), fs = require('fs'), path = require('path');
const puppeteer = require('puppeteer-core');
const KOK = path.join(__dirname, '..');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const HEDEF = process.argv[2] || 'http://127.0.0.1:8766';
const SENARYO = [   // ad, saat dilimi, tarayici dili, beklenen yol
  ['Turkiye, Ingilizce tarayici', 'Europe/Istanbul', 'en-US', '/'],
  ['Almanya, Turkce tarayici', 'Europe/Berlin', 'tr-TR', '/'],
  ['ABD', 'America/New_York', 'en-US', '/en/'],
  ['Hindistan', 'Asia/Kolkata', 'en-IN', '/en/'],
];
let sunucu = null;
if (!process.argv[2]) sunucu = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
  const d = path.join(KOK, p); if (!d.startsWith(KOK) || !fs.existsSync(d)) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { 'Content-Type': p.endsWith('.js') ? 'text/javascript' : p.endsWith('.css') ? 'text/css' : 'text/html' }); fs.createReadStream(d).pipe(r);
}).listen(8766, '127.0.0.1');

(async () => {
  const b = await puppeteer.launch({ executablePath: CHROME, headless: 'new' }); let hata = 0;
  try {
    for (const [ad, tz, dil, beklenen] of SENARYO) {
      const ctx = await b.createBrowserContext(); const p = await ctx.newPage();
      await p.emulateTimezone(tz);
      await p.evaluateOnNewDocument((d) => { Object.defineProperty(navigator, 'languages', { get: () => [d] }); }, dil);
      await p.goto(HEDEF + '/', { waitUntil: 'networkidle0' }); await new Promise((r) => setTimeout(r, 300));
      const yol = await p.evaluate(() => location.pathname);
      const ok = yol === beklenen; if (!ok) hata++;
      console.log(`${ok ? 'ok  ' : 'HATA'} ${ad.padEnd(28)} -> ${yol} (beklenen ${beklenen})`);
      await ctx.close();
    }
    // dugme ile secim kalici
    const ctx = await b.createBrowserContext(); const p = await ctx.newPage();
    await p.emulateTimezone('Europe/Istanbul'); await p.goto(HEDEF + '/', { waitUntil: 'networkidle0' });
    await Promise.all([p.waitForNavigation(), p.click('a[data-dil="en"]')]);
    await p.goto(HEDEF + '/', { waitUntil: 'networkidle0' }); await new Promise((r) => setTimeout(r, 300));
    const yol = await p.evaluate(() => location.pathname); const ok = yol === '/en/'; if (!ok) hata++;
    console.log(`${ok ? 'ok  ' : 'HATA'} ${'EN dugmesi kalici'.padEnd(28)} -> ${yol}`);
  } finally { await b.close(); if (sunucu) sunucu.close(); }
  process.exit(hata ? 1 : 0);
})().catch((e) => { console.error(e); process.exit(1); });
