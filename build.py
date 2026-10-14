# -*- coding: utf-8 -*-
"""colmo.bardino.app sayfalarini uretir.

    python build.py

Neden uretici: alti dil x (acilis + yasal) elle tutulunca kaciniyor. Bir
cumleyi degistirmek icin alti dosyaya dokunmak, bes tanesinin bayat kalmasi
demek. Icerik burada sozluk, HTML ciktida.

Kok dizin INGILIZCE. Diger sitelerde kok Turkce ama bu urun magazada
varsayilan olarak Ingilizce listeleniyor ve alti dilde yayina giriyor; koke
gelen ziyaretcinin cogu Turkce bilmiyor. Turkce /tr/ altinda ve dil secici
her sayfanin tepesinde.
"""
import io
import os
import re
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://colmo.bardino.app"
PKG = "com.bardino.colmo"
MAIL = "info@bardino.app"
UPDATED = "2026-08-26"
APP_STORE = "https://apps.apple.com/app/colmo-jar-puzzle/id6805859722"
GOOGLE_PLAY = "https://play.google.com/store/apps/details?id=" + PKG

# Magaza rozetleri resmi dosyalar (Decimo deposu, store_assets/badges), her
# dilin kendi rozeti. Google PNG'sinin seffaf kenari kirpildi: kirpilmadan ayni
# boya getirilince Google rozeti Apple'inkinden kucuk gorunuyor, Google'in
# kilavuzu ise esit ya da buyuk istiyor. Apple rozeti sirada once gelir.
BADGE_H = 48

# Dil kodu -> (html lang, og locale, kendi dilindeki adi, kok mu)
LANGS = [
    ("en", "en", "en_US", "English", True),
    ("tr", "tr", "tr_TR", "Türkçe", False),
    ("de", "de", "de_DE", "Deutsch", False),
    ("fr", "fr", "fr_FR", "Français", False),
    ("es", "es", "es_ES", "Español", False),
    ("pt", "pt", "pt_BR", "Português", False),
]

# Yasal metin yalnizca EN ve TR'de tam yazildi; digerleri Ingilizceye baglanir.
# Yarim cevrilmis bir sozlesme, cevrilmemis olandan kotudur.
LEGAL_LANGS = {"en", "tr"}

T = {}

T["en"] = {
    "title": "Colmo - Fill every jar to the brim",
    "desc": "A calm number puzzle set in a room full of glass jars. Free on "
            "Android and iOS.",
    "badge": "Out now",
    "h1a": "A quiet room,",
    "h1b": "a wall of jars.",
    "lead": "Colmo is a number puzzle you can play with one hand and no "
            "hurry. Jars, shelves, hundreds of levels, and the small "
            "satisfaction of one landing exactly right.",
    "small": "Free. Plays offline.",
    "bandAlt": "Colmo jars on a shelf",
    "shotsT": "From the game",
    "shotsS": "Real screenshots, not mock-ups.",
    "caps": ["The board", "Every jar has its own character",
             "The end of a level", "The shelf wall you climb"],
    "endT": "Out now.",
    "endS": "Free on the App Store and Google Play.",
    "stores": ("Colmo on the App Store", "Colmo on Google Play"),
    "legal": ("Privacy", "Terms of use", "Account deletion"),
    "aile_lead": "Colmo is made by Bardino, a small independent studio. If you like it, meet its two siblings:",
    "back": "Back to Colmo",
}

T["tr"] = {
    "title": "Colmo - Kavanozları ağzına kadar doldur",
    "desc": "Cam kavanozlarla dolu bir odada geçen sakin bir sayı bulmacası. "
            "Android ve iOS'ta ücretsiz.",
    "badge": "Yayında",
    "h1a": "Sessiz bir oda,",
    "h1b": "bir duvar dolusu kavanoz.",
    "lead": "Colmo, tek elle ve acele etmeden oynanan bir sayı bulmacası. "
            "Kavanozlar, raflar, yüzlerce bölüm ve bir tanesinin tam yerine "
            "oturmasının o küçük tatmini.",
    "small": "Ücretsiz. İnternetsiz oynanır.",
    "bandAlt": "Rafta duran Colmo kavanozları",
    "shotsT": "Oyundan kareler",
    "shotsS": "Hepsi gerçek ekran görüntüsü, temsili değil.",
    "caps": ["Tahta", "Her kavanozun kendi huyu var",
             "Bölümün sonu", "Tırmandığın raf duvarı"],
    "endT": "Çıktı.",
    "endS": "App Store ve Google Play'de ücretsiz.",
    "stores": ("App Store'da Colmo", "Google Play'de Colmo"),
    "legal": ("Gizlilik", "Kullanım koşulları", "Hesap silme"),
    "aile_lead": "Colmo'yu Bardino yapıyor, küçük ve bağımsız bir stüdyo. Sevdiysen iki kardeşiyle de tanış:",
    "back": "Colmo'ya dön",
}

T["de"] = {
    "title": "Colmo - Fülle die Gläser bis zum Rand",
    "desc": "Ein ruhiges Zahlenpuzzle in einem Raum voller Gläser. Kostenlos "
            "für Android und iOS.",
    "badge": "Jetzt erhältlich",
    "h1a": "Ein stiller Raum,",
    "h1b": "eine Wand voller Gläser.",
    "lead": "Colmo ist ein Zahlenpuzzle für eine Hand und ohne Eile. Gläser, "
            "Regale, hunderte Level und die kleine Zufriedenheit, wenn "
            "eines genau passt.",
    "small": "Kostenlos. Auch offline spielbar.",
    "bandAlt": "Colmo-Gläser auf einem Regal",
    "shotsT": "Aus dem Spiel",
    "shotsS": "Echte Screenshots, keine Montagen.",
    "caps": ["Das Brett", "Jedes Glas hat seinen eigenen Charakter",
             "Das Ende eines Levels", "Die Regalwand, die du hochsteigst"],
    "endT": "Jetzt erhältlich.",
    "endS": "Kostenlos im App Store und bei Google Play.",
    "stores": ("Colmo im App Store", "Colmo bei Google Play"),
    "legal": ("Datenschutz", "Nutzungsbedingungen", "Konto löschen"),
    "aile_lead": "Colmo kommt von Bardino, einem kleinen unabhängigen Studio. Wenn es dir gefällt, lern seine zwei Geschwister kennen:",
    "back": "Zurück zu Colmo",
}

T["fr"] = {
    "title": "Colmo - Remplis les bocaux à ras bord",
    "desc": "Un puzzle de nombres apaisant dans une pièce pleine de bocaux "
            "en verre. Gratuit sur Android et iOS.",
    "badge": "Disponible",
    "h1a": "Une pièce calme,",
    "h1b": "un mur de bocaux.",
    "lead": "Colmo est un puzzle de nombres qui se joue d'une main et sans "
            "se presser. Des bocaux, des étagères, des centaines de niveaux, "
            "et la petite satisfaction d'en voir un tomber juste.",
    "small": "Gratuit. Jouable hors ligne.",
    "bandAlt": "Bocaux Colmo sur une étagère",
    "shotsT": "Images du jeu",
    "shotsS": "De vraies captures, pas des maquettes.",
    "caps": ["Le plateau", "Chaque bocal a son caractère",
             "La fin d'un niveau", "Le mur d'étagères que tu grimpes"],
    "endT": "Disponible maintenant.",
    "endS": "Gratuit sur l'App Store et Google Play.",
    "stores": ("Colmo sur l'App Store", "Colmo sur Google Play"),
    "legal": ("Confidentialité", "Conditions d'utilisation",
              "Suppression du compte"),
    "aile_lead": "Colmo est créé par Bardino, un petit studio indépendant. Si tu l'aimes, découvre les deux autres :",
    "back": "Retour à Colmo",
}

T["es"] = {
    "title": "Colmo - Llena los tarros hasta el borde",
    "desc": "Un puzle de números tranquilo en una habitación llena de tarros "
            "de cristal. Gratis en Android e iOS.",
    "badge": "Ya disponible",
    "h1a": "Una habitación tranquila,",
    "h1b": "una pared de tarros.",
    "lead": "Colmo es un puzle de números para jugar con una mano y sin "
            "prisa. Tarros, estantes, cientos de niveles y la pequeña "
            "satisfacción de ver uno encajar justo.",
    "small": "Gratis. Se juega sin conexión.",
    "bandAlt": "Tarros de Colmo en un estante",
    "shotsT": "Del juego",
    "shotsS": "Capturas reales, no montajes.",
    "caps": ["El tablero", "Cada tarro tiene su carácter",
             "El final de un nivel", "La pared de estantes que subes"],
    "endT": "Ya disponible.",
    "endS": "Gratis en el App Store y Google Play.",
    "stores": ("Colmo en el App Store", "Colmo en Google Play"),
    "legal": ("Privacidad", "Términos de uso", "Eliminar cuenta"),
    "aile_lead": "Colmo lo hace Bardino, un pequeño estudio independiente. Si te gusta, conoce a sus dos hermanos:",
    "back": "Volver a Colmo",
}

T["pt"] = {
    "title": "Colmo - Encha os potes até a borda",
    "desc": "Um puzzle de números tranquilo numa sala cheia de potes de "
            "vidro. Grátis para Android e iOS.",
    "badge": "Já disponível",
    "h1a": "Uma sala silenciosa,",
    "h1b": "uma parede de potes.",
    "lead": "Colmo é um puzzle de números para jogar com uma mão e sem "
            "pressa. Potes, prateleiras, centenas de fases e a pequena "
            "satisfação de ver um encaixar certinho.",
    "small": "Grátis. Joga-se offline.",
    "bandAlt": "Potes do Colmo numa prateleira",
    "shotsT": "Do jogo",
    "shotsS": "Capturas reais, não montagens.",
    "caps": ["O tabuleiro", "Cada pote tem o seu temperamento",
             "O fim de uma fase", "A parede de prateleiras que você sobe"],
    "endT": "Já disponível.",
    "endS": "Grátis na App Store e no Google Play.",
    "stores": ("Colmo na App Store", "Colmo no Google Play"),
    "legal": ("Privacidade", "Termos de uso", "Excluir conta"),
    "aile_lead": "Colmo é feito pela Bardino, um pequeno estúdio independente. Se você gostar, conheça os outros dois:",
    "back": "Voltar ao Colmo",
}

def path_for(code, page):
    """Kok Ingilizce, digerleri kendi klasorunde."""
    if code == "en":
        return page
    return "%s/%s" % (code, page)


def rel_root(code):
    return "" if code == "en" else "../"


def lang_bar(code, page):
    out = []
    for c, _lang, _loc, name, _root in LANGS:
        href = "/" + path_for(c, page)
        cur = ' aria-current="page"' if c == code else ""
        out.append('<a href="%s" hreflang="%s"%s>%s</a>' % (href, c, cur, name))
    return '<div class="diller">%s</div>' % "".join(out)


def head(code, page, title, desc):
    lang = dict((c, l) for c, l, _o, _n, _r in LANGS)[code]
    loc = dict((c, o) for c, _l, o, _n, _r in LANGS)[code]
    r = rel_root(code)
    alts = "\n    ".join(
        '<link rel="alternate" hreflang="%s" href="%s/%s">'
        % (c, SITE, path_for(c, page)) for c, _l, _o, _n, _r in LANGS)
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="%(desc)s">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:url" content="%(site)s/%(path)s">
    <meta property="og:title" content="%(title)s">
    <meta property="og:description" content="%(desc)s">
    <meta property="og:image" content="%(site)s/assets/colmo_share.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="%(loc)s">
    <meta property="og:site_name" content="Colmo">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="%(title)s">
    <meta name="twitter:description" content="%(desc)s">
    <meta name="twitter:image" content="%(site)s/assets/colmo_share.png">
    <meta name="theme-color" content="#FFF4FB" media="(prefers-color-scheme: light)">
    <meta name="theme-color" content="#3A2A4D" media="(prefers-color-scheme: dark)">
    <title>%(title)s</title>
    <link rel="canonical" href="%(site)s/%(path)s">
    %(alts)s
    <link rel="alternate" hreflang="x-default" href="%(site)s/">
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="apple-touch-icon" href="/assets/colmo_icon.png">
    <link rel="manifest" href="/manifest.json">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/%(css)s">
</head>
<body>
""" % dict(lang=lang, desc=esc(desc), site=SITE, path=path_for(code, page),
           title=esc(title), loc=loc, alts=alts,
           css="legal.css" if page != "index.html" else "style.css",
           r=r)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def header(code, page):
    return """<header class="ust">
    <div class="kap">
        <a class="marka" href="/%(home)s">
            <img src="/assets/colmo_icon.png" alt="Colmo" width="40" height="40">
            <b>COLMO</b>
        </a>
        %(bar)s
    </div>
</header>
""" % dict(home="" if code == "en" else code + "/", bar=lang_bar(code, page))


# ── altbilgi: aile blogu ────────────────────────────────────────────────────
#
# Uc oyun sitesinde (decimo, colmo, palmo) altbilgi AYNI yapida: solda
# Bardino'nun kendi logosu (isaret + yazi, altinda slogan yok), sagda tek
# cumle ve iki kardes oyunun karti, en altta yasal satir. Her site bunu kendi
# kurallariyla ciziyor; yapi ortak, gorunum oyunun. Eskiden burada tek bir
# "X is made by Bardino Technology." satiri vardi ve kardes oyunlar hic
# anilmiyordu.
#
# Logo bardino.app'teki isaretin ve yazinin AYNISI (bkz. bardino-site
# index.html, bd-mark / bd-wm). Yazi currentColor; koyu temada CSS acar.
BARDINO_LOGO = (
    '<svg class="aile-logo" viewBox="0 0 600 124" role="img" aria-label="Bardino">'
    '<rect x="4.5" y="13.5" width="91" height="87" rx="21" fill="#1B2F4A" stroke="#1B2F4A" stroke-width="5"/>'
    '<rect x="4.5" y="7" width="91" height="87" rx="21" fill="#FFC83D" stroke="#1B2F4A" stroke-width="5"/>'
    '<g fill="none" stroke="#1B2F4A" stroke-width="11.2" stroke-linecap="round"><path d="M37.1 26.1V72.9"/><circle cx="51.5" cy="58.5" r="14.4"/></g>'
    '<g transform="translate(124 12) scale(.656)">'
    '<g fill="none" stroke="currentColor" stroke-width="28" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M16 19V136"/><circle cx="52" cy="100" r="36"/><circle cx="166" cy="100" r="36"/><path d="M202 64V136"/>'
    '<path d="M252 64V136M252 100A36 36 0 0 1 297.32 65.23"/><circle cx="374" cy="100" r="36"/><path d="M410 19V136"/>'
    '<path d="M460 64V136"/><path d="M510 64V136M510 100A36 36 0 0 1 582 100V136"/><circle cx="664" cy="100" r="36"/></g>'
    '<rect x="444" y="5" width="32" height="32" rx="9" fill="#FFC83D" stroke="currentColor" stroke-width="5"/></g>'
    '</svg>')

# Kardes oyunlarin kisa tanimi, her dilde. Decimo'nunki magazadaki adinin
# ikinci yarisi (Decimo deposu tools/store/listing-copy.mjs, ASC_BASLIK);
# Colmo ve Palmo'nunki kendi sitelerinin basligindaki slogan.
KARDES_TAG = {
    "decimo": {"en": "Number chain", "tr": "Sayı zinciri", "de": "Zahlenkette",
               "fr": "Chaîne de nombres", "es": "Cadena de números",
               "pt": "Corrente de números"},
    "colmo": {"en": "Fill every jar to the brim",
              "tr": "Kavanozları ağzına kadar doldur",
              "de": "Fülle die Gläser bis zum Rand",
              "fr": "Remplis les bocaux à ras bord",
              "es": "Llena los tarros hasta el borde",
              "pt": "Encha os potes até a borda"},
    "palmo": {"en": "Weave the whole board", "tr": "Bütün tahtayı doku",
              "de": "Webe das ganze Brett", "fr": "Tisse tout le plateau",
              "es": "Teje todo el tablero", "pt": "Teça o tabuleiro inteiro"},
}
KARDES_AD = {"decimo": "Decimo", "colmo": "Colmo", "palmo": "Palmo"}


def kardes_url(g, code):
    """Kardesin sitesi, ayni dilde. Decimo'nun sitesi yalniz Turkce."""
    if g == "decimo":
        return "https://decimo.bardino.app/"
    return "https://%s.bardino.app/%s" % (g, "" if code == "en" else code + "/")


def aile(code, t, kardesler):
    kart = "".join(
        '<li><a href="%s"><img src="/assets/aile/%s.webp" alt="" width="44" '
        'height="44" loading="lazy"><span><b>%s</b><small>%s</small></span></a></li>'
        % (kardes_url(g, code), g, KARDES_AD[g], esc(KARDES_TAG[g][code]))
        for g in kardesler)
    return """    <div class="kap aile-ust">
        <a class="aile-marka" href="%(studyo)s">%(logo)s</a>
        <div class="aile-kardes">
            <p>%(lead)s</p>
            <ul>%(kart)s</ul>
        </div>
    </div>
""" % dict(studyo="https://bardino.app/tr/" if code == "tr" else "https://bardino.app/",
           logo=BARDINO_LOGO, lead=esc(t["aile_lead"]), kart=kart)



def footer(code, t):
    p, tm, ad = t["legal"]
    return """<footer class="aile">
%(aile)s    <div class="kap aile-alt">
        <div class="f-baglantilar">
            <a href="/%(lp)s">%(p)s</a>
            <a href="/%(lt)s">%(tm)s</a>
            <a href="/%(la)s">%(ad)s</a>
        </div>
        <span>&copy; 2026 Bardino Technology</span>
    </div>
</footer>

</body>
</html>
""" % dict(aile=aile(code, t, ("decimo", "palmo")), p=esc(p), tm=esc(tm), ad=esc(ad),
           lp=path_for(code if code in LEGAL_LANGS else "en", "privacy.html"),
           lt=path_for(code if code in LEGAL_LANGS else "en", "terms.html"),
           la=path_for(code if code in LEGAL_LANGS else "en",
                       "account-deletion.html"))


def badge_width(rel):
    """Rozetin BADGE_H yuksekligindeki genisligi (img width/height icin)."""
    p = os.path.join(HERE, rel.replace("/", os.sep))
    if rel.endswith(".svg"):
        m = re.search(r'<svg[^>]*?\swidth="([\d.]+)"[^>]*?\sheight="([\d.]+)"',
                      io.open(p, encoding="utf-8").read())
        w, h = float(m.group(1)), float(m.group(2))
    else:
        w, h = struct.unpack(">II", io.open(p, "rb").read(24)[16:24])
    return round(w * BADGE_H / h)


def stores(code, t):
    a_alt, g_alt = t["stores"]
    a_img = "assets/badges/%s/app_store.svg" % code
    g_img = "assets/badges/%s/google_play.png" % code
    return ('<div class="magaza">'
            '<a href="%s"><img src="/%s" alt="%s" width="%d" height="%d"></a>'
            '<a href="%s"><img src="/%s" alt="%s" width="%d" height="%d"></a>'
            '</div>'
            % (APP_STORE, a_img, esc(a_alt), badge_width(a_img), BADGE_H,
               GOOGLE_PLAY, g_img, esc(g_alt), badge_width(g_img), BADGE_H))


def landing(code, t):
    """Acilis sayfasi.

    Kural ANLATILMIYOR ve sayi VERILMIYOR. Onceki surumde ikisi de vardi:
    CSS ile cizilmis kavanozlar kurali adim adim anlatiyordu ve "60 bolum",
    "0 reklam" gibi sayilar sayfayi bir ozellik listesine ceviriyordu. Oyunun
    kendisi kurali yaziyla anlatmiyor; sitesi de anlatmamali. Gorunen her
    kavanoz oyunun kendi karesinden geliyor, hicbiri siteye cizilmedi.
    """
    caps = t["caps"]
    shots = "".join(
        '<figure><img src="/assets/shots/%s" alt="%s" width="800" height="1422" loading="lazy"><figcaption>%s</figcaption></figure>'
        % (f, esc(c), esc(c))
        for f, c in zip(["01_board.webp", "02_wax.webp", "03_result.webp",
                         "04_map.webp"], caps))
    return (head(code, "index.html", t["title"], t["desc"])
            + header(code, "index.html")
            + """
<section class="kahraman">
    <div class="kap">
        <div>
            <span class="rozet">%(badge)s</span>
            <h1>%(h1a)s<br><em>%(h1b)s</em></h1>
            <p class="alt">%(lead)s</p>
            <p class="kucuk">%(small)s</p>
            %(stores)s
        </div>
        <div class="telefon">
            <img src="/assets/shots/01_board.webp" alt="%(cap0)s" width="800" height="1422" loading="eager">
        </div>
    </div>
</section>

<section class="bant">
    <img src="/assets/colmo_share.png" alt="%(bandAlt)s" width="1200" height="630" loading="lazy">
</section>

<section class="duvar-bolum">
    <div class="kap">
        <h2>%(shotsT)s</h2>
        <p class="bolum-alt">%(shotsS)s</p>
        <div class="vitrin">%(shots)s</div>
    </div>
</section>

<section class="kapanis">
    <div class="kap">
        <div class="kutu">
            <h2>%(endT)s</h2>
            <p class="bolum-alt">%(endS)s</p>
            %(stores)s
        </div>
    </div>
</section>
""" % dict(badge=esc(t["badge"]), h1a=esc(t["h1a"]), h1b=esc(t["h1b"]),
           lead=esc(t["lead"]), small=esc(t["small"]), cap0=esc(caps[0]),
           bandAlt=esc(t["bandAlt"]),
           shotsT=esc(t["shotsT"]), shotsS=esc(t["shotsS"]), shots=shots,
           endT=esc(t["endT"]), endS=esc(t["endS"]),
           stores=stores(code, t))
            + """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MobileApplication",
  "name": "Colmo",
  "applicationCategory": "GameApplication",
  "operatingSystem": "Android, iOS",
  "url": "%(site)s/",
  "image": "%(site)s/assets/colmo_share.png",
  "offers": {"@type": "Offer", "price": "0", "priceCurrency": "TRY"},
  "publisher": {"@type": "Organization", "name": "Bardino Technology"}
}
</script>
""" % dict(site=SITE)
            + footer(code, t))

def legal(code, t, page, title, body):
    return (head(code, page, "%s - Colmo" % title, t["desc"])
            + header(code, page)
            + """
<section class="yasal">
    <div class="kap">
        <a class="geri" href="/%(home)s">&larr; %(back)s</a>
        <h1>%(title)s</h1>
        <p class="tarih">%(upd)s: %(date)s</p>
        <div class="govde">%(body)s</div>
    </div>
</section>
""" % dict(home="" if code == "en" else code + "/", back=esc(t["back"]),
           title=esc(title), date=UPDATED, body=body,
           upd="Last updated" if code == "en" else "Son guncelleme")
            + footer(code, t))


def write(rel, text):
    p = os.path.join(HERE, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(p) else None
    io.open(p, "w", encoding="utf-8", newline="\n").write(text)
    return rel


if __name__ == "__main__":
    import legal_text

    made = []
    for code, _l, _o, _n, _r in LANGS:
        t = T[code]
        made.append(write(path_for(code, "index.html"), landing(code, t)))
        if code in LEGAL_LANGS:
            for page, title, body in legal_text.pages(code):
                made.append(write(path_for(code, page),
                                  legal(code, t, page, title, body)))

    # ── sabit dosyalar ──────────────────────────────────────────────────
    write("CNAME", "colmo.bardino.app\n")
    write("robots.txt",
          "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
    urls = "".join(
        "  <url><loc>%s/%s</loc></url>\n" % (SITE, path_for(c, p))
        for c, _l, _o, _n, _r in LANGS
        for p in (["index.html"] + (["privacy.html", "terms.html",
                                     "account-deletion.html"]
                                    if c in LEGAL_LANGS else [])))
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          '%s</urlset>\n' % urls)
    write("manifest.json",
          '{\n  "name": "Colmo",\n  "short_name": "Colmo",\n'
          '  "start_url": "/",\n  "display": "standalone",\n'
          '  "background_color": "#FFF4FB",\n  "theme_color": "#FFF4FB",\n'
          '  "icons": [\n'
          '    {"src": "/assets/colmo_icon_192.png", "sizes": "192x192", "type": "image/png"},\n'
          '    {"src": "/assets/colmo_icon_512.png", "sizes": "512x512", "type": "image/png"}\n'
          '  ]\n}\n')
    write("404.html", head("en", "index.html", "Colmo", T["en"]["desc"])
          + header("en", "index.html")
          + '\n<section class="kapanis"><div class="kap"><div class="kutu">'
            '<h2>Nothing here.</h2>'
            '<p class="bolum-alt">That page does not exist. '
            '<a href="/">Back to Colmo</a>.</p>'
            '</div></div></section>\n'
          + footer("en", T["en"]))

    print("uretilen sayfa: %d" % len(made))
    for m in sorted(made):
        print("  " + m)
