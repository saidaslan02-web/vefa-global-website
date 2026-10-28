// Dil seçimi (28 Ekim 2026). Sıra: ziyaretçinin dil düğmesiyle seçtiği dil > Türkiye saat dilimi ya da Türkçe
// tarayıcı > İngilizce. Site GitHub Pages'te olduğu için sunucu ülkeyi bilemez; IP'den ülke sorgusu da yapılmaz
// (çerez onayından önce ziyaretçi verisi üçüncü tarafa gitmesin). Yurt dışındaki Türkçe tarayıcılar da Türkçe görür.
// Her sayfa karşı dildeki sürümünü <link rel="alternate" hreflang="..."> ile bildirir; bu betik o linklerden sonra yüklenmeli.
(function () {
  var ANAHTAR = 'vefa-dil';
  var mevcut = document.documentElement.lang === 'en' ? 'en' : 'tr';

  // dil düğmesine basılınca seçim kalıcı olur
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('[data-dil]') : null;
    if (a) { try { localStorage.setItem(ANAHTAR, a.getAttribute('data-dil')); } catch (_) {} }
  });

  // arama motorları ve önizleme botları yönlendirilmez: her dil kendi adresinde dizine girsin
  if (/bot|crawl|spider|slurp|facebookexternalhit|whatsapp|linkedin|preview|lighthouse/i.test(navigator.userAgent || '')) return;

  function turkiyeMi() {
    try {
      var tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
      if (tz === 'Europe/Istanbul' || tz === 'Asia/Istanbul') return true;
    } catch (_) {}
    var diller = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ''];
    for (var i = 0; i < diller.length; i++) if (/^tr(-|$)/i.test(diller[i])) return true;
    return false;
  }

  var tercih = null;
  try { tercih = localStorage.getItem(ANAHTAR); } catch (_) {}
  var hedef = tercih === 'tr' || tercih === 'en' ? tercih : (turkiyeMi() ? 'tr' : 'en');
  if (hedef === mevcut) return;
  var link = document.querySelector('link[rel="alternate"][hreflang="' + hedef + '"]');
  // yalnız yol kullanılır: ziyaretçi hangi adresteyse (www., yerel önizleme) orada kalır
  if (link) location.replace(new URL(link.href).pathname + location.hash);
})();
