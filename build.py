# -*- coding: utf-8 -*-
"""colmo.dozi.app sayfalarini uretir.

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

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://colmo.dozi.app"
PKG = "com.bardino.colmo"
MAIL = "info@dozi.app"
UPDATED = "2026-08-26"

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
    "desc": "A calm number puzzle set in a room full of glass jars. Coming "
            "soon to Android and iOS.",
    "badge": "Coming soon",
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
    "endT": "Not out yet.",
    "endS": "Colmo is in final testing on Android, with iOS to follow. This "
            "page will carry the store links the day it is out.",
    "legal": ("Privacy", "Terms of use", "Account deletion"),
    "by": "Colmo is made by",
    "back": "Back to Colmo",
}

T["tr"] = {
    "title": "Colmo - Kavanozları ağzına kadar doldur",
    "desc": "Cam kavanozlarla dolu bir odada geçen sakin bir sayı bulmacası. "
            "Android ve iOS'ta çok yakında.",
    "badge": "Çok yakında",
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
    "endT": "Henüz çıkmadı.",
    "endS": "Colmo Android'de son testlerinde, ardından iOS geliyor. Çıktığı "
            "gün mağaza bağlantıları bu sayfada olacak.",
    "legal": ("Gizlilik", "Kullanım koşulları", "Hesap silme"),
    "by": "Colmo,",
    "back": "Colmo'ya dön",
}

T["de"] = {
    "title": "Colmo - Fülle die Gläser bis zum Rand",
    "desc": "Ein ruhiges Zahlenpuzzle in einem Raum voller Gläser. Bald für "
            "Android und iOS.",
    "badge": "Bald verfügbar",
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
    "endT": "Noch nicht erschienen.",
    "endS": "Colmo ist auf Android im letzten Test, iOS folgt. Am Tag der "
            "Veröffentlichung stehen die Store-Links hier.",
    "legal": ("Datenschutz", "Nutzungsbedingungen", "Konto löschen"),
    "by": "Colmo stammt von",
    "back": "Zurück zu Colmo",
}

T["fr"] = {
    "title": "Colmo - Remplis les bocaux à ras bord",
    "desc": "Un puzzle de nombres apaisant dans une pièce pleine de bocaux "
            "en verre. Bientôt sur Android et iOS.",
    "badge": "Bientôt disponible",
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
    "endT": "Pas encore sorti.",
    "endS": "Colmo est en phase de test final sur Android, iOS suivra. Les "
            "liens vers les stores seront ici le jour de la sortie.",
    "legal": ("Confidentialité", "Conditions d'utilisation",
              "Suppression du compte"),
    "by": "Colmo est réalisé par",
    "back": "Retour à Colmo",
}

T["es"] = {
    "title": "Colmo - Llena los tarros hasta el borde",
    "desc": "Un puzle de números tranquilo en una habitación llena de tarros "
            "de cristal. Muy pronto en Android e iOS.",
    "badge": "Muy pronto",
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
    "endT": "Todavía no ha salido.",
    "endS": "Colmo está en pruebas finales en Android, y iOS vendrá después. "
            "El día del lanzamiento los enlaces estarán aquí.",
    "legal": ("Privacidad", "Términos de uso", "Eliminar cuenta"),
    "by": "Colmo es de",
    "back": "Volver a Colmo",
}

T["pt"] = {
    "title": "Colmo - Encha os potes até a borda",
    "desc": "Um puzzle de números tranquilo numa sala cheia de potes de "
            "vidro. Em breve para Android e iOS.",
    "badge": "Em breve",
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
    "endT": "Ainda não lançado.",
    "endS": "Colmo está em teste final no Android, com iOS a seguir. No dia "
            "do lançamento os links das lojas estarão aqui.",
    "legal": ("Privacidade", "Termos de uso", "Excluir conta"),
    "by": "Colmo é feito por",
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
    <meta name="theme-color" content="#FFF4FB">
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


def footer(code, t):
    p, tm, ad = t["legal"]
    return """<footer>
    <div class="kap">
        <span>%(by)s <a href="https://dozi.app">Bardino Technology</a>.</span>
        <div class="f-baglantilar">
            <a href="/%(lp)s">%(p)s</a>
            <a href="/%(lt)s">%(tm)s</a>
            <a href="/%(la)s">%(ad)s</a>
        </div>
    </div>
    <div class="kap f-alt">&copy; 2026 Bardino Technology &middot; %(pkg)s</div>
</footer>

</body>
</html>
""" % dict(by=esc(t["by"]), p=esc(p), tm=esc(tm), ad=esc(ad), pkg=PKG,
           lp=path_for(code if code in LEGAL_LANGS else "en", "privacy.html"),
           lt=path_for(code if code in LEGAL_LANGS else "en", "terms.html"),
           la=path_for(code if code in LEGAL_LANGS else "en",
                       "account-deletion.html"))


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
        </div>
    </div>
</section>
""" % dict(badge=esc(t["badge"]), h1a=esc(t["h1a"]), h1b=esc(t["h1b"]),
           lead=esc(t["lead"]), small=esc(t["small"]), cap0=esc(caps[0]),
           bandAlt=esc(t["bandAlt"]),
           shotsT=esc(t["shotsT"]), shotsS=esc(t["shotsS"]), shots=shots,
           endT=esc(t["endT"]), endS=esc(t["endS"]))
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
    write("CNAME", "colmo.dozi.app\n")
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
