// Yerel onizleme ve ekran goruntusu. Siteyi 127.0.0.1:8765'te sunar, Mac'teki Chrome ile sayfayi/bolumu ceker.
// Kullanim:
//   node araclar/onizle.js                       -> TR + EN, masaustu + telefon, tam sayfa
//   node araclar/onizle.js '#nedenbiz'           -> yalniz o bolum
//   node araclar/onizle.js '#nedenbiz' /en/      -> yalniz o bolum, yalniz EN
// Cikti: onizleme/<ad>.png (git'e girmez). Tasarim degisikligini yayina almadan once kullaniciya bunlarla goster.
const http = require('http'), fs = require('fs'), path = require('path');
const puppeteer = require('puppeteer-core');
const KOK = path.join(__dirname, '..'), CIKTI = path.join(KOK, 'onizleme'), PORT = 8765;
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const TUR = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.xml': 'application/xml' };
const [secici = null, ...yollar] = process.argv.slice(2);
const SAYFALAR = yollar.length ? yollar : ['/', '/en/'];
const EKRANLAR = [['masaustu', 1280, 900, false], ['telefon', 390, 844, true]];

const sunucu = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
  const d = path.join(KOK, p);
  if (!d.startsWith(KOK) || !fs.existsSync(d)) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { 'Content-Type': TUR[path.extname(d)] || 'application/octet-stream' }); fs.createReadStream(d).pipe(r);
}).listen(PORT, '127.0.0.1');

(async () => {
  fs.mkdirSync(CIKTI, { recursive: true });
  const b = await puppeteer.launch({ executablePath: CHROME, headless: 'new' });
  try {
    for (const sayfa of SAYFALAR) for (const [ekran, w, h, mobil] of EKRANLAR) {
      const ctx = await b.createBrowserContext(); const p = await ctx.newPage();
      // dil yonlendirmesi ve cerez bandi onizlemeyi bozmasin
      await p.evaluateOnNewDocument(() => { try { localStorage.setItem('vefa-dil', location.pathname.startsWith('/en') ? 'en' : 'tr'); localStorage.setItem('vefa-cerez', 'red'); } catch (e) {} });
      await p.setViewport({ width: w, height: h, isMobile: mobil, deviceScaleFactor: 1 });
      await p.goto(`http://127.0.0.1:${PORT}${sayfa}`, { waitUntil: 'networkidle0' });
      await p.evaluate(() => { document.querySelectorAll('img[loading=lazy]').forEach((i) => { i.loading = 'eager'; }); });
      await new Promise((r) => setTimeout(r, 800));
      const ad = `${sayfa === '/' ? 'tr' : sayfa.replace(/\W+/g, '_').replace(/^_|_$/g, '')}_${ekran}${secici ? '_' + secici.replace(/\W+/g, '') : ''}`;
      if (secici) {
        await p.evaluate(() => { const h = document.querySelector('header'); if (h) h.style.display = 'none'; });
        await (await p.$(secici)).screenshot({ path: path.join(CIKTI, ad + '.png') });
      } else await p.screenshot({ path: path.join(CIKTI, ad + '.png'), fullPage: true });
      const tasma = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth);
      console.log(`${ad}.png${tasma ? '  YATAY TASMA!' : ''}`);
      await ctx.close();
    }
  } finally { await b.close(); sunucu.close(); }
})().catch((e) => { console.error(e); process.exit(1); });
