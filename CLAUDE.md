# vefaglobal.com — çalışma kuralları

Statik site, GitHub Pages (`saidaslan02-web/vefa-global-website`, dal `main`). `main`'e push = birkaç dakikada canlı.
DNS Cloudflare'de (yalnız DNS, proxy yok), yani sunucu tarafı kod / ülke bilgisi yok.

## Önce göster, sonra yayınla (kullanıcı kuralı)
- Tasarım değişikliğinde **yayına almadan önce** `node araclar/onizle.js '<bölüm>'` ile ekran görüntüsü al, gerekirse
  2–3 seçeneği yan yana göster, kullanıcı seçsin. Kullanıcı düzeni net söylediyse birebir uygula.
- İstenmeyen süs ekleme: logo rozeti, renk/ışık tonlaması, kademeli (stagger) ızgara — üçü de reddedildi (29 Eki 2026).
- Kullanıcının verdiği görsellerde renk/ışık değiştirme; yalnız kırp ve boyutla (`araclar/foto_kare.py`).

## Dosyalar
| | |
|---|---|
| `index.html`, `gizlilik.html` | Türkçe sayfalar (kaynak) |
| `en/index.html`, `en/privacy.html` | İngilizce. `en/index.html` **elle düzenlenmez**: `python3 araclar/en_uret.py` TR'den üretir |
| `assets/dil.js` | Dil seçimi: kayıtlı tercih > İstanbul saat dilimi ya da Türkçe tarayıcı > EN. IP sorgusu yok, botlar yönlendirilmez |
| `assets/site.css` | Derlenmiş Tailwind. HTML'de yeni sınıf kullanınca `npm run css` |
| `assets/ofis/` | Hakkımızda galerisi: 4 kare görsel, 2×2 (ofis, toplanti, calisma, fuar) |
| `araclar/` | `en_uret.py`, `onizle.js`, `dil_testi.js`, `foto_kare.py` |

## Değişiklik akışı
1. TR sayfayı düzenle (`index.html`).
2. Metin değiştiyse `araclar/en_uret.py`'ye çevirisini ekle/güncelle, sonra `python3 araclar/en_uret.py`
   (bir TR metni bulunamazsa ya da EN'de Türkçe harf kalırsa durur: bu bir uyarı, düzelt).
3. Yeni Tailwind sınıfı varsa `npm run css`.
4. `node araclar/onizle.js '#bölüm'` → `onizleme/*.png`'yi kullanıcıya göster, onay al.
5. Dil mantığına dokunduysan `node araclar/dil_testi.js`.
6. Commit + push; canlıda `curl` ile dosyanın yeni sürümünü doğrula, sonra `node araclar/dil_testi.js https://vefaglobal.com`.
   Kullanıcıya Cmd+Shift+R ile yenilemesini söyle.

## Sabitler
- Resmi unvan: **Vefa Global Consultancy Pvt. Ltd.** (her yerde, schema dahil).
- Konumlar: Yeni Delhi · İstanbul · Milano · Londra (EN: New Delhi · Istanbul · Milan · London).
- İletişim formu Web3Forms üzerinden şirket e-postasına gider; GA4 ve Meta Pixel yalnız çerez onayıyla yüklenir.
- Bilinen: 320 px ekranda giriş başlığı sağdan kesiliyor (eskiden beri, düzeltilmedi).
