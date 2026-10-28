"""Galeri fotografi hazirlar: kare kirpma + 1000x1000 + jpg/webp, EXIF/GPS yazilmaz. Renk/isik DOKUNULMAZ
(29 Eki 2026: tonlama begenilmedi). Kirpma karesi orijinal piksellerde verilir.
  python3 araclar/foto_kare.py <kaynak> <ad> [sol ust kenar]
  ornek: python3 araclar/foto_kare.py ~/Downloads/ofis.png ofis 362 0 1086   -> assets/ofis/ofis.{jpg,webp}
Kirpma verilmezse ortadan en buyuk kare alinir."""
import os, sys
from PIL import Image, ImageOps
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
kaynak, ad = sys.argv[1], sys.argv[2]
im = ImageOps.exif_transpose(Image.open(os.path.expanduser(kaynak))).convert('RGB')
if len(sys.argv) >= 6:
    x, y, k = map(int, sys.argv[3:6])
else:
    k = min(im.size); x, y = (im.width - k) // 2, (im.height - k) // 2
assert x + k <= im.width and y + k <= im.height, f'kare tasiyor: {im.size}, {x}+{k}, {y}+{k}'
im = im.crop((x, y, x + k, y + k)).resize((1000, 1000), Image.LANCZOS)
hedef = os.path.join(KOK, 'assets', 'ofis'); os.makedirs(hedef, exist_ok=True)
im.save(os.path.join(hedef, ad + '.jpg'), 'JPEG', quality=86, optimize=True, progressive=True)
im.save(os.path.join(hedef, ad + '.webp'), 'WEBP', quality=82, method=6)
print(f'assets/ofis/{ad}.jpg + .webp  (kaynak {os.path.basename(kaynak)}, kare {x},{y},{k})')
