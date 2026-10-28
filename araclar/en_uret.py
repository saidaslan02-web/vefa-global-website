"""index.html (TR) -> en/index.html. Yapi birebir, yalniz metinler ve yollar degisir: TR metni degisince
burada karsiligini guncelle. Her ceviri beklenen sayida gecmezse ya da gorunur metinde Turkce harf kalirsa durur."""
import re, sys, os
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(os.path.join(KOK, 'index.html'), encoding='utf-8').read()

def r(eski, yeni, adet=1):
    global s
    n = s.count(eski)
    if n != adet:
        sys.exit(f'BEKLENEN {adet}, BULUNAN {n}: {eski[:70]!r}')
    s = s.replace(eski, yeni)

# --- head ---
r('<html lang="tr"', '<html lang="en"')
r('<title>Vefa Global · Uluslararası Danışmanlık ve IT Operasyonları</title>', '<title>Vefa Global · International Consulting and IT Operations</title>')
r('content="Vefa Global olarak ithalat/ihracat süreçlerinizi, global e-ticaret hesaplarınızı ve dijital IT varlığınızı uçtan uca yönetiyoruz."',
  'content="Vefa Global manages your import/export processes, global e-commerce accounts and digital IT presence end to end."', 2)
r('content="Vefa Global · Uluslararası Danışmanlık ve IT Operasyonları"', 'content="Vefa Global · International Consulting and IT Operations"')
r('<meta property="og:url" content="https://vefaglobal.com/">', '<meta property="og:url" content="https://vefaglobal.com/en/">')
r('<meta property="og:locale" content="tr_TR">', '<meta property="og:locale" content="en_US">\n    <meta property="og:locale:alternate" content="tr_TR">')
r('<link rel="canonical" href="https://vefaglobal.com/">', '<link rel="canonical" href="https://vefaglobal.com/en/">')
# /en/ altinda goreli yollar kirilir: kok yollar
r('href="favicon.png"', 'href="/favicon.png"')
r('href="assets/site.css"', 'href="/assets/site.css"')
r('src="assets/dil.js"', 'src="/assets/dil.js"')
r('src="vefa-logo.png"', 'src="/vefa-logo.png"', 2)
r('srcset="assets/ofis/', 'srcset="/assets/ofis/', 4)
r('src="assets/ofis/', 'src="/assets/ofis/', 4)
# ofis galerisi
r('alt="Vefa Global toplantı odası, Yeni Delhi"', 'alt="Vefa Global meeting room, New Delhi"')
r('>Toplantı odası<', '>Meeting room<')
r('>Yeni Delhi</span></p>', '>New Delhi</span></p>', 3)
r('alt="Vefa Global çalışma alanı, Yeni Delhi"', 'alt="Vefa Global workspace, New Delhi"')
r('>Çalışma alanı<', '>Workspace<')
r('alt="STONA 2023 doğal taş fuarında"', 'alt="At the STONA 2023 natural stone fair"')
r('>STONA 2023 fuarı<', '>STONA 2023 fair<')
r('>Sahada</span></p>', '>On the ground</span></p>')
r('alt="Vefa Global ofisi, Yeni Delhi"', 'alt="Vefa Global office, New Delhi"')
r('>Ofisimiz<', '>Our office<')
r('href="gizlilik.html"', 'href="/en/privacy.html"', 2)

# --- ust bar ve menu ---
r('>Hizmetler</a>', '>Services</a>', 2)
r('>Süreç</a>', '>Process</a>', 2)
r('>Hakkımızda</a>', '>About</a>', 2)
r('>İletişim</a>', '>Contact</a>')
r('İşinizi konuşalım', "Let's talk", 2)
r('Menüyü aç', 'Open menu', 3)
r('Menüyü kapat', 'Close menu')

# --- giris ---
r('''              Uluslararası ticaret ve IT operasyonlarınızı<br>
              <span class="text-coral-deep sm:whitespace-nowrap">anahtar teslim</span><br>
              kuruyoruz.''', '''              Your international trade and IT operations,<br>
              <span class="text-coral-deep sm:whitespace-nowrap">set up turnkey.</span>''')
r("Tedarik zincirinden Hindistan'da şirket kurulumuna, global e-ticaret yönetiminden IT altyapınıza kadar tüm operasyonel yükünüzü üstleniyoruz.",
  'From your supply chain to setting up a company in India, from global e-commerce to your IT infrastructure, we take the whole operational load off your shoulders.')
r('Projenizi Anlatın', 'Tell us about your project')
r('>Departmanlar<', '>Departments<')
r('7 bölüm aktif', '7 departments active')
r('>Tedarik Zinciri</div>', '>Supply Chain</div>')
r('global üreticiler bulundu', 'global manufacturers sourced')
r('Gümrük & Lojistik', 'Customs & Logistics')
r('ihracat belgeleri onaylandı', 'export documents approved')
r('Amazon Pazaryeri', 'Amazon Marketplace')
r('satış listeleri optimize edildi', 'listings optimized')
r('Performans Reklam', 'Performance Ads')
r('PPC kampanyası devrede', 'PPC campaign live')
r('>Sosyal Medya</div>', '>Social Media</div>')
r('haftalık içerikler paylaşıldı', 'weekly posts published')
r('IT & Altyapı', 'IT & Infrastructure')
r('sistem entegrasyonu tamamlandı', 'system integration complete')
r('Şirket Kurulumu', 'Company Setup')
r("Hindistan'da operasyon başlatıldı", 'operations launched in India')
r('>aktif</span>', '>active</span>', 7)
r('<span>bugün</span>', '<span>today</span>')
r('her şey kendi kontrolünüzde', 'everything under your control')

# --- hizmetler ---
r('· neler yapıyoruz', '· what we do')
r('Global pazarda yükünüzü aldığımız hizmetler.', 'Services that take the load off you in global markets.')
r('servis / ', 'service / ', 8)
r('Tedarik Zinciri & Lojistik', 'Supply Chain & Logistics')
r('Doğru üreticiyi bulmaktan gümrük süreçlerine kadar uçtan uca ithalat-ihracat operasyonunuzu güvenle yürütürüz.',
  'From finding the right manufacturer to customs clearance, we run your import-export operation end to end, safely.')
r('Global E-Ticaret Yönetimi', 'Global E-Commerce Management')
r("Amazon, Flipkart ve Etsy'de satıcı hesaplarınızı açar, algoritmaya uygun listelerle pazar payınızı büyütürüz.",
  'We open your seller accounts on Amazon, Flipkart and Etsy and grow your market share with algorithm-friendly listings.')
r('Performans Pazarlama (PPC)', 'Performance Marketing (PPC)')
r('Doğru kitleye ulaşarak satışlarınızı artıracak, reklam bütçenizi en verimli şekilde kullanacak kampanyalar kurgularız.',
  'We build campaigns that reach the right audience, grow your sales and get the most out of your ad budget.')
r('IT & Entegrasyon', 'IT & Integration')
r('İşletmenizin ihtiyaç duyduğu yazılım ve IT altyapısını kurarak operasyonel süreçlerinizi otomatikleştiririz.',
  'We set up the software and IT infrastructure your business needs and automate your operations.')
r('Sosyal Medya Yönetimi', 'Social Media Management')
r('B2B marka otoritenizi artıracak içerik stratejileri oluşturur ve dijital kimliğinizi global ölçekte konumlandırırız.',
  'We create content strategies that build your B2B brand authority and position your digital identity globally.')
r('Kalite Kontrol', 'Quality Control')
r('Mermer, tekstil ve tüketici ürünleri gibi spesifik sektörlerde yerinde denetim ve kalite güvencesi sağlarız.',
  'We provide on-site inspection and quality assurance in sectors such as marble, textiles and consumer goods.')
r('SEO ve Optimizasyon', 'SEO & Optimization')
r('Pazaryerlerinde ve arama motorlarında daha görünür olmanız için liste ve içerik optimizasyonu yaparız.',
  'We optimize your listings and content so you are more visible on marketplaces and search engines.')
r('Aklınızda başka bir iş mi var?', 'Have something else in mind?')
r('İşiniz bunlara uymuyorsa operasyonu size özel tasarlarız. İhtiyaçlarınızı anlatın, neler yapabileceğimizi konuşalım.',
  "If your business doesn't fit these, we design the operation around you. Tell us what you need and let's talk about what we can do.")
r('Tekil hizmetlerden ziyade, Vefa Global olarak sürecin tamamını ele alırız. Sadece strateji sunmakla kalmaz, lojistikten dijital dönüşüme kadar her aşamada bizzat operasyonun içinde yer alırız.',
  "Rather than one-off services, Vefa Global takes on the whole process. We don't just hand over a strategy; we are inside the operation at every stage, from logistics to digital transformation.")

# --- kimler icin ---
r('· kimler için', "· who it's for")
r('Siz işinize odaklanın, operasyonu biz yönetelim.', 'You focus on your business, we run the operation.')
r('Üreticiler ve ihracatçılar', 'Manufacturers and exporters')
r("Hindistan'dan ürün tedarik etmek ya da Hindistan pazarına satmak isteyen firmalar. Üretici bulma, kalite kontrol, gümrük ve lojistiği tek elden yürütürüz.",
  'Companies that want to source products from India or sell into the Indian market. We handle sourcing, quality control, customs and logistics in one place.')
r('Online satışa açılan markalar', 'Brands going online')
r("Amazon, Flipkart ya da Etsy'de satış yapmak isteyen markalar. Hesap açılışından listeleme, reklam ve sosyal medyaya kadar mağazanızı biz işletiriz.",
  'Brands that want to sell on Amazon, Flipkart or Etsy. We run your store, from account setup to listings, ads and social media.')
r("Hindistan'a yatırım yapanlar", 'Investing in India')
r("Hindistan'da şirket kurmak ve operasyon başlatmak isteyen girişimciler. Kuruluştan IT altyapısına kadar sahada yanınızda oluruz.",
  'Entrepreneurs who want to set up a company and start operations in India. We are with you on the ground, from incorporation to IT infrastructure.')
r('Size uygun modeli konuşalım', "Let's find the right model for you")

# --- surec ---
r('· nasıl ilerliyor', '· how it works')
r('Dört adımda operasyonel mükemmellik.', 'Operational excellence in four steps.')
r('adım / ', 'step / ', 4)
r('Keşif ve Analiz', 'Discovery & Analysis')
r('İlk toplantımızda mevcut tedarik zincirinizi veya dijital varlıklarınızı analiz eder, dar boğazları tespit ederiz.',
  'In our first meeting we analyze your current supply chain or digital assets and pinpoint the bottlenecks.')
r('>Strateji</h3>', '>Strategy</h3>')
r('Şirketinizin hedeflerine uygun net ve uygulanabilir bir operasyon planı çıkarırız.', "We draw up a clear, workable operations plan that fits your company's goals.")
r('>İcra</h3>', '>Execution</h3>')
r('Tedarikçi görüşmelerinden e-ticaret reklam kampanyalarının yönetimine kadar kolları sıvayıp işe koyuluruz.',
  'From supplier negotiations to running your e-commerce ad campaigns, we roll up our sleeves and get to work.')
r('Büyüme & Raporlama', 'Growth & Reporting')
r('Sonuçları periyodik olarak raporlar, elde edilen veriler ışığında stratejiyi sürekli optimize ederiz.',
  'We report results regularly and keep optimizing the strategy based on the data.')

# --- neden vefa ---
r('· neden vefa', '· why vefa')
r('Neden Vefa Global?', 'Why Vefa Global?')
B = '<strong class="font-semibold text-dark-text">'
r("2016'dan bu yana Hindistan'dan dünyaya uzanan iş fırsatlarını <span class=\"text-coral\">somut sonuçlara</span> dönüştürüyoruz.",
  'Since 2016, we have been turning business opportunities that reach from India to the world into <span class="text-coral">tangible results</span>.')
r('Yeni Delhi merkezli ' + B + 'Vefa Global Consultancy Pvt. Ltd.</strong> olarak, şu alanlarda şirketlere ' + B + 'uçtan uca iş desteği</strong> sunuyoruz:',
  'As ' + B + 'Vefa Global Consultancy Pvt. Ltd.</strong>, based in New Delhi, we provide companies with ' + B + 'end-to-end business support</strong> in:')
r('>Uluslararası ticaret</li>', '>International trade</li>')
r('>İthalat ve ihracat</li>', '>Import and export</li>')
r('>İş geliştirme</li>', '>Business development</li>')
r('>Pazar araştırması</li>', '>Market research</li>')
r('>IT çözümleri</li>', '>IT solutions</li>')
r(B + 'Hindistan ile Türkiye</strong> başta olmak üzere farklı pazarlardaki iş bağlantılarımızı, yerel pazar bilgimizi ve saha deneyimimizi bir araya getirerek işletmelerin ' + B + 'yeni pazarlara açılmasına</strong>, ' + B + 'doğru iş ortaklarına ulaşmasına</strong> ve ticari fırsatlarını geliştirmesine yardımcı oluyoruz.',
  'By combining our business connections across markets, ' + B + 'India and Turkey</strong> above all, with local market knowledge and field experience, we help businesses ' + B + 'enter new markets</strong>, ' + B + 'reach the right partners</strong> and grow their commercial opportunities.')
r('Bizim için danışmanlık, yalnızca öneriler sunmakla sınırlı değildir. Tedarikçi araştırmasından iş ortaklarının belirlenmesine, ticari görüşmelerden operasyonel koordinasyona, dokümantasyondan dijital süreçlerin geliştirilmesine kadar projenin ihtiyaç duyduğu aşamalarda ' + B + 'aktif rol alıyoruz.</strong>',
  'For us, consulting is not limited to giving advice. From supplier research to identifying partners, from commercial negotiations to operational coordination, from documentation to building digital processes, we ' + B + 'take an active role</strong> at every stage the project needs.')
r('Bizi farklı kılan, yalnızca ne yapılması gerektiğini anlatmamız değil, <span class="text-coral">işin uygulanma sürecinde de sorumluluk almamızdır.</span>',
  'What sets us apart is that we don\'t just tell you what needs to be done; <span class="text-coral">we also take responsibility for getting it done.</span>')
r('Her işletmenin hedeflerinin, kaynaklarının ve ihtiyaçlarının farklı olduğunun bilinciyle, standart çözümler yerine ' + B + 'ihtiyaca özel yaklaşımlar</strong> geliştiriyoruz. Amacımız yalnızca yeni fırsatlar yaratmak değil, bu fırsatların ' + B + 'sürdürülebilir iş ilişkilerine ve uzun vadeli ticari değere</strong> dönüşmesine katkıda bulunmaktır.',
  'Knowing that every business has different goals, resources and needs, we develop ' + B + 'tailored approaches</strong> instead of standard solutions. Our aim is not only to create new opportunities, but to help them grow into ' + B + 'sustainable business relationships and long-term commercial value</strong>.')
r('Vefa Global: <span class="text-coral">Yerel uzmanlık, uluslararası bağlantılar ve uygulamaya dayalı iş ortaklığı.</span>',
  'Vefa Global: <span class="text-coral">local expertise, international connections and a hands-on business partnership.</span>')

r('Uluslararası Ağ', 'International Network')
r('Yeni Delhi · İstanbul · Milano · Londra', 'New Delhi · Istanbul · Milan · London')

# --- iletisim ---
r('sıradaki iş: <span class="font-medium text-coral-deep">sizinki</span>', 'next up: <span class="font-medium text-coral-deep">yours</span>')
r('''              Global büyümenizde<br>
              <span class="text-coral-deep">yerinizi ayırtın.</span>''', '''              Claim your place<br>
              <span class="text-coral-deep">in global growth.</span>''')
r('İşinizi anlatın, dönelim.', "Tell us about your business, we'll get back to you.")
r('Operasyonlarınızı nasıl daha ileriye taşıyabileceğimizi görmek için formu doldurun. Uzman ekibimiz 24 saat içinde dönüş yapsın.',
  'Fill in the form to see how we can take your operations further. Our team will get back to you within 24 hours.')
r('value="vefaglobal.com — yeni iletişim formu"', 'value="vefaglobal.com — yeni iletişim formu (İngilizce sayfa)"')
r('>Adınız</span>', '>Your name</span>')
r('>E-posta ya da telefon</span>', '>Email or phone</span>')
r('>İşiniz ne, hangi alanda desteğe ihtiyacınız var?</span>', '>What is your business, and where do you need support?</span>')
r('                    Gönder\n', '                    Send\n')

# --- alt bilgi, whatsapp, cerez ---
r('                İşinizi anlatın\n', '                Tell us about your business\n')
r('>Gizlilik ve Çerez Politikası</a>', '>Privacy & Cookie Policy</a>')
r('aria-label="WhatsApp ile İletişime Geçin"', 'aria-label="Contact us on WhatsApp"')
r('aria-label="Çerez tercihi"', 'aria-label="Cookie preference"')
r("Sitemizi geliştirmek ve reklamlarımızı ölçmek için Google Analytics ve Meta çerezlerini kullanmak istiyoruz. Ayrıntılar <a href=\"/en/privacy.html\" class=\"font-medium text-coral-deep underline\">Gizlilik Politikası</a>'nda.",
  "We'd like to use Google Analytics and Meta cookies to improve our site and measure our ads. Details are in our <a href=\"/en/privacy.html\" class=\"font-medium text-coral-deep underline\">Privacy Policy</a>.")
r('>Kabul et</button>', '>Accept</button>')
r('>Reddet</button>', '>Decline</button>')
r("'gönderilemedi'", "'not sent'")
r("'Teşekkürler, mesajınız bize ulaştı. 24 saat içinde dönüş yapacağız.'", "'Thank you, we have received your message. We will get back to you within 24 hours.'")
r("'Mesaj gönderilemedi. Lütfen info@vefaglobal.com adresine yazın ya da WhatsApp’tan ulaşın.'",
  "'Your message could not be sent. Please email info@vefaglobal.com or reach us on WhatsApp.'")

# --- dil dugmesi: Ingilizce sayfada Turkceye gecer (etiketi Turkce okuyan icin Turkce) ---
r('<a href="/en/" hreflang="en" lang="en" data-dil="en"', '<a href="/" hreflang="tr" lang="tr" data-dil="tr"')
r('aria-label="Switch to English" title="English"', 'aria-label="Türkçe sayfaya geç" title="Türkçe"')
r('<span>EN</span>', '<span>TR</span>')

# gorunur metinde Turkce harf kaldi mi (yorumlar ve form konusu haric)
gorunur = re.sub(r'<!--.*?-->', '', s, flags=re.S)
gorunur = re.sub(r'^\s*//.*$', '', gorunur, flags=re.M)
for bilerek_turkce in ('vefaglobal.com — yeni iletişim formu (İngilizce sayfa)', 'aria-label="Türkçe sayfaya geç" title="Türkçe"'):
    gorunur = gorunur.replace(bilerek_turkce, '')
kalan = [l.strip()[:110] for l in gorunur.splitlines() if re.search(r'[çğıöşüÇĞİÖŞÜ]', l)]
if kalan:
    sys.exit('TURKCE KALDI:\n' + '\n'.join(kalan))
os.makedirs(os.path.join(KOK, 'en'), exist_ok=True)
open(os.path.join(KOK, 'en', 'index.html'), 'w', encoding='utf-8').write(s)
print('en/index.html yazildi,', len(s), 'karakter')
