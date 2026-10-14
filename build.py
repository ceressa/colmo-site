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

Yazi tipi sitenin kendi dosyasi (assets/fonts, tools/build-fonts.py). Sayfa
baska hicbir sunucudan bir sey yuklemiyor; altbilgideki "cerez yok, baska
sunucu yok" cumlesi bunu soyluyor ve bir Google Fonts baglantisi geri gelirse
yalan olur.
"""
import io
import os
import re
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://colmo.bardino.app"
PKG = "com.bardino.colmo"
MAIL = "info@bardino.app"
APP_STORE = "https://apps.apple.com/app/colmo-jar-puzzle/id6805859722"
GOOGLE_PLAY = "https://play.google.com/store/apps/details?id=" + PKG

# Magaza rozetleri resmi dosyalar (Decimo deposu, store_assets/badges), her
# dilin kendi rozeti. Google PNG'sinin seffaf kenari kirpildi: kirpilmadan ayni
# boya getirilince Google rozeti Apple'inkinden kucuk gorunuyor, Google'in
# kilavuzu ise esit ya da buyuk istiyor. Apple rozeti sirada once gelir.
BADGE_H = 48

# Dil kodu -> (html lang + hreflang, og locale, kendi dilindeki adi, kisa kod).
# Portekizce metin Brezilya Portekizcesi (voce, magaza listesi pt-BR), o yuzden
# lang pt-BR; klasor /pt/ kaliyor, adresi degistirmek baglantilari kirardi.
LANGS = [
    ("en", "en", "en_US", "English", "EN"),
    ("tr", "tr", "tr_TR", "Türkçe", "TR"),
    ("de", "de", "de_DE", "Deutsch", "DE"),
    ("fr", "fr", "fr_FR", "Français", "FR"),
    ("es", "es", "es_ES", "Español", "ES"),
    ("pt", "pt-BR", "pt_BR", "Português", "PT"),
]
ALL_CODES = [c for c, _l, _o, _n, _k in LANGS]
LANG_ATTR = dict((c, l) for c, l, _o, _n, _k in LANGS)

# Yasal metin yalnizca EN ve TR'de tam yazildi; digerleri Ingilizceye baglanir.
# Yarim cevrilmis bir sozlesme, cevrilmemis olandan kotudur. Yasal sayfanin dil
# secicisi ve hreflang'i de yalniz bu ikisini listeler: eskiden alti dili
# listeliyordu ve /de|fr|es|pt/ altindaki 12 yasal adres 404 donuyordu.
LEGAL_LANGS = ["en", "tr"]

FONT_WEIGHTS = (400, 900)  # on yukleme: govde ve baslik

MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"],
    "tr": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
           "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"],
}

NBSP = " "

T = {}

T["en"] = {
    "title": "Colmo - Fill every jar to the brim",
    "desc": "A calm number puzzle: pour numbers into glass jars until each "
            "one is exactly full. 120 levels. Free on Android and iOS.",
    "h1a": "Fill every jar",
    "h1b": "to the brim.",
    "lead": "Colmo is a number puzzle you can play with one hand and no "
            "hurry. You pour numbers into jars until each one is exactly "
            "full. 120 levels, an endless mode, and the small satisfaction "
            "of every jar filled exactly.",
    "small": "Free. Plays offline.",
    "howT": "How to play",
    "how": [
        ("Fill each jar exactly",
         "Every jar has a capacity. Pour the numbers you are dealt until it "
         "is exactly full: a full jar bursts and goes to the shelf. A number "
         "that would overflow is refused."),
        ("Starred jars are the goal",
         "Burst the starred jars to win the level. Some jars have their own "
         "rules: a narrow neck only takes small numbers, and a wax-sealed jar "
         "stays shut until a starred jar next to it bursts."),
        ("Three jokers, no clock",
         "<b>Hold</b> keeps the number in hand for later, <b>Undo</b> takes "
         "back your last move, <b>Swap</b> trades the number in hand for a "
         "new one. No level is timed. Finish with numbers to spare for more "
         "stars."),
    ],
    "bandAlt": "Colmo jars on a shelf",
    "shotsT": "From the game",
    "caps": ["The board", "A wax-sealed jar", "The end of a level",
             "The level map"],
    "endT": "Fill your first jar.",
    "endS": "Free on the App Store and Google Play.",
    "stores": ("Colmo on the App Store", "Colmo on Google Play"),
    "legal": ("Privacy policy", "Terms of use", "Account deletion"),
    "support": "Support",
    "studio": "A Bardino game",
    "nocookie": "This site sets no cookies and loads nothing from other "
                "servers.",
    "aile_lead": "More from Bardino:",
    "back": "Back to Colmo",
    "upd": "Last updated",
}

T["tr"] = {
    "title": "Colmo - Kavanozları ağzına kadar doldur",
    "desc": "Sakin bir sayı bulmacası: sayıları cam kavanozlara dök, her biri "
            "tam dolsun. 120 bölüm. Android ve iOS'ta ücretsiz.",
    "h1a": "Her kavanozu",
    "h1b": "ağzına kadar doldur.",
    "lead": "Colmo, tek elle ve acele etmeden oynanan bir sayı bulmacası: "
            "sayıları kavanozlara, her biri tam dolana kadar dökersin. 120 "
            "bölüm, bir sonsuz mod ve tam dolan her kavanozun verdiği o "
            "küçük keyif.",
    "small": "Ücretsiz. İnternetsiz oynanır.",
    "howT": "Nasıl oynanır",
    "how": [
        ("Her kavanozu tam doldur",
         "Her kavanozun bir kapasitesi var. Eline gelen sayıları dökerek onu "
         "tam doldur: tam dolan kavanoz patlar ve rafa kaldırılır. Taşıracak "
         "sayıyı kavanoz kabul etmez."),
        ("Hedef: yıldızlı kavanozlar",
         "Bölümü kazanmak için yıldızlı kavanozları patlat. Bazı kavanozların "
         "kendi huyu var: dar boyunlu kavanoz yalnızca küçük sayıları alır, "
         "mühürlü kavanoz yanındaki yıldızlı kavanoz patlayana kadar "
         "açılmaz."),
        ("Üç joker, saat yok",
         "<b>Beklet</b> elindeki sayıyı sonraya saklar, <b>Geri al</b> son "
         "hamleni geri alır, <b>Değiştir</b> elindeki sayıyı yenisiyle "
         "değiştirir. Hiçbir bölüm süreli değil. Az sayıyla bitir, çok "
         "yıldız al."),
    ],
    "bandAlt": "Rafta duran Colmo kavanozları",
    "shotsT": "Oyundan kareler",
    "caps": ["Tahta", "Mühürlü kavanoz", "Bölümün sonu", "Bölüm haritası"],
    "endT": "İlk kavanozunu doldur.",
    "endS": "App Store ve Google Play'de ücretsiz.",
    "stores": ("App Store'da Colmo", "Google Play'de Colmo"),
    "legal": ("Gizlilik politikası", "Kullanım koşulları", "Hesap silme"),
    "support": "Destek",
    "studio": "Bir Bardino oyunu",
    "nocookie": "Bu site çerez kullanmaz ve başka sunuculardan hiçbir şey "
                "yüklemez.",
    "aile_lead": "Bardino'nun diğer oyunları:",
    "back": "Colmo'ya dön",
    "upd": "Son güncelleme",
}

T["de"] = {
    "title": "Colmo - Fülle die Gläser bis zum Rand",
    "desc": "Ein ruhiges Zahlenpuzzle: Gieß Zahlen in Gläser, bis jedes genau "
            "voll ist. 120 Level. Kostenlos für Android und iOS.",
    "h1a": "Fülle jedes Glas",
    "h1b": "bis zum Rand.",
    "lead": "Colmo ist ein Zahlenpuzzle für eine Hand und ohne Eile. Du "
            "gießt Zahlen in Gläser, bis jedes genau voll ist. 120 Level, "
            "ein Endlosmodus und die kleine Zufriedenheit jedes genau "
            "gefüllten Glases.",
    "small": "Kostenlos. Offline spielbar.",
    "howT": "So wird gespielt",
    "how": [
        ("Jedes Glas genau füllen",
         "Jedes Glas hat ein Fassungsvermögen. Gieß die Zahlen, die du "
         "bekommst, hinein, bis es genau voll ist: Ein volles Glas zerplatzt "
         "und kommt ins Regal. Eine Zahl, die es überlaufen ließe, wird "
         "abgelehnt."),
        ("Sterngläser sind das Ziel",
         "Lass die Gläser mit Stern zerplatzen, um das Level zu gewinnen. "
         "Manche Gläser haben eigene Regeln: Ein enger Hals nimmt nur kleine "
         "Zahlen, und ein mit Wachs versiegeltes Glas bleibt zu, bis ein "
         "Sternglas daneben zerplatzt."),
        ("Drei Joker, keine Uhr",
         "<b>Halten</b> hebt die Zahl in deiner Hand für später auf, "
         "<b>Zurück</b> nimmt deinen letzten Zug zurück, <b>Tauschen</b> "
         "tauscht die Zahl in deiner Hand gegen eine neue. Kein Level läuft "
         "gegen die Zeit. Mit übrigen Zahlen abschließen bringt mehr "
         "Sterne."),
    ],
    "bandAlt": "Colmo-Gläser auf einem Regal",
    "shotsT": "Aus dem Spiel",
    "caps": ["Das Brett", "Ein mit Wachs versiegeltes Glas",
             "Das Ende eines Levels", "Die Levelkarte"],
    "endT": "Fülle dein erstes Glas.",
    "endS": "Kostenlos im App Store und bei Google Play.",
    "stores": ("Colmo im App Store", "Colmo bei Google Play"),
    "legal": ("Datenschutz", "Nutzungsbedingungen", "Konto löschen"),
    "support": "Support",
    "studio": "Ein Spiel von Bardino",
    "nocookie": "Diese Website setzt keine Cookies und lädt nichts von "
                "anderen Servern.",
    "aile_lead": "Mehr von Bardino:",
    "back": "Zurück zu Colmo",
}

T["fr"] = {
    "title": "Colmo - Remplis les bocaux à ras bord",
    "desc": "Un puzzle de nombres apaisant" + NBSP + ": verse des nombres "
            "dans des bocaux jusqu'à ce que chacun soit exactement plein. 120 "
            "niveaux. Gratuit sur Android et iOS.",
    "h1a": "Remplis chaque bocal",
    "h1b": "à ras bord.",
    "lead": "Colmo est un puzzle de nombres qui se joue d'une main et sans "
            "se presser. Tu verses des nombres dans des bocaux jusqu'à ce "
            "que chacun soit exactement plein. 120 niveaux, un mode infini "
            "et la petite satisfaction de chaque bocal rempli pile.",
    "small": "Gratuit. Jouable hors ligne.",
    "howT": "Comment jouer",
    "how": [
        ("Remplis chaque bocal exactement",
         "Chaque bocal a une capacité. Verse les nombres que tu reçois "
         "jusqu'à ce qu'il soit exactement plein" + NBSP + ": un bocal plein "
         "éclate et rejoint l'étagère. Un nombre qui le ferait déborder est "
         "refusé."),
        ("Les bocaux étoilés sont l'objectif",
         "Fais éclater les bocaux étoilés pour gagner le niveau. Certains "
         "bocaux ont leurs propres règles" + NBSP + ": un col étroit "
         "n'accepte que les petits nombres, et un bocal scellé à la cire "
         "reste fermé jusqu'à ce qu'un bocal étoilé voisin éclate."),
        ("Trois jokers, pas d'horloge",
         "<b>Garder</b> met le nombre en main de côté pour plus tard, "
         "<b>Annuler</b> annule ton dernier coup, <b>Échanger</b> échange le "
         "nombre en main contre un nouveau. Aucun niveau n'est chronométré. "
         "Finir avec des nombres d'avance donne plus d'étoiles."),
    ],
    "bandAlt": "Bocaux Colmo sur une étagère",
    "shotsT": "Images du jeu",
    "caps": ["Le plateau", "Un bocal scellé à la cire", "La fin d'un niveau",
             "La carte des niveaux"],
    "endT": "Remplis ton premier bocal.",
    "endS": "Gratuit sur l'App Store et Google Play.",
    "stores": ("Colmo sur l'App Store", "Colmo sur Google Play"),
    "legal": ("Confidentialité", "Conditions d'utilisation",
              "Suppression du compte"),
    "support": "Assistance",
    "studio": "Un jeu Bardino",
    "nocookie": "Ce site ne dépose aucun cookie et ne charge rien depuis "
                "d'autres serveurs.",
    "aile_lead": "Aussi chez Bardino" + NBSP + ":",
    "back": "Retour à Colmo",
}

T["es"] = {
    "title": "Colmo - Llena los tarros hasta el borde",
    "desc": "Un puzle de números tranquilo: vierte números en tarros hasta "
            "que cada uno quede exactamente lleno. 120 niveles. Gratis en "
            "Android e iOS.",
    "h1a": "Llena cada tarro",
    "h1b": "hasta el borde.",
    "lead": "Colmo es un puzle de números para jugar con una mano y sin "
            "prisa. Viertes números en tarros hasta que cada uno quede "
            "exactamente lleno. 120 niveles, un modo infinito y la pequeña "
            "satisfacción de cada tarro lleno justo.",
    "small": "Gratis. Se juega sin conexión.",
    "howT": "Cómo se juega",
    "how": [
        ("Llena cada tarro exactamente",
         "Cada tarro tiene una capacidad. Vierte los números que te llegan "
         "hasta llenarlo exactamente: un tarro lleno estalla y sube a la "
         "estantería. Un número que lo desbordaría se rechaza."),
        ("Los tarros con estrella son el objetivo",
         "Haz estallar los tarros con estrella para ganar el nivel. Algunos "
         "tarros tienen sus propias reglas: un cuello estrecho solo admite "
         "números pequeños, y un tarro sellado con cera no se abre hasta que "
         "estalla un tarro con estrella a su lado."),
        ("Tres comodines, sin reloj",
         "<b>Guardar</b> guarda el número de tu mano para después, "
         "<b>Deshacer</b> deshace tu último movimiento, <b>Cambiar</b> "
         "cambia el número de tu mano por uno nuevo. Ningún nivel va contra "
         "el tiempo. Terminar con números de sobra da más estrellas."),
    ],
    "bandAlt": "Tarros de Colmo en un estante",
    "shotsT": "Del juego",
    "caps": ["El tablero", "Un tarro sellado con cera",
             "El final de un nivel", "El mapa de niveles"],
    "endT": "Llena tu primer tarro.",
    "endS": "Gratis en el App Store y Google Play.",
    "stores": ("Colmo en el App Store", "Colmo en Google Play"),
    "legal": ("Privacidad", "Términos de uso", "Eliminar cuenta"),
    "support": "Soporte",
    "studio": "Un juego de Bardino",
    "nocookie": "Este sitio no usa cookies y no carga nada desde otros "
                "servidores.",
    "aile_lead": "Más de Bardino:",
    "back": "Volver a Colmo",
}

T["pt"] = {
    "title": "Colmo - Encha os potes até a borda",
    "desc": "Um puzzle de números tranquilo: despeje números nos potes até "
            "cada um ficar exatamente cheio. 120 fases. Grátis para Android "
            "e iOS.",
    "h1a": "Encha cada pote",
    "h1b": "até a borda.",
    "lead": "Colmo é um puzzle de números para jogar com uma mão e sem "
            "pressa. Você despeja números nos potes até cada um ficar "
            "exatamente cheio. 120 fases, um modo infinito e a pequena "
            "satisfação de cada pote cheio na medida.",
    "small": "Grátis. Funciona offline.",
    "howT": "Como jogar",
    "how": [
        ("Encha cada pote exatamente",
         "Cada pote tem uma capacidade. Despeje os números que você recebe "
         "até enchê-lo exatamente: um pote cheio estoura e vai para a "
         "prateleira. Um número que transbordaria é recusado."),
        ("Os potes estrelados são o objetivo",
         "Estoure os potes estrelados para vencer a fase. Alguns potes têm "
         "regras próprias: um gargalo estreito só aceita números pequenos, e "
         "um pote selado com cera só abre quando um pote estrelado ao lado "
         "estoura."),
        ("Três curingas, sem relógio",
         "<b>Guardar</b> guarda o número da mão para depois, "
         "<b>Desfazer</b> desfaz a sua última jogada, <b>Trocar</b> troca o "
         "número da mão por um novo. Nenhuma fase é cronometrada. Terminar "
         "com números sobrando vale mais estrelas."),
    ],
    "bandAlt": "Potes do Colmo numa prateleira",
    "shotsT": "Do jogo",
    "caps": ["O tabuleiro", "Um pote selado com cera", "O fim de uma fase",
             "O mapa de fases"],
    "endT": "Encha seu primeiro pote.",
    "endS": "Grátis na App Store e no Google Play.",
    "stores": ("Colmo na App Store", "Colmo no Google Play"),
    "legal": ("Privacidade", "Termos de uso", "Excluir conta"),
    "support": "Suporte",
    "studio": "Um jogo da Bardino",
    "nocookie": "Este site não usa cookies e não carrega nada de outros "
                "servidores.",
    "aile_lead": "Mais da Bardino:",
    "back": "Voltar ao Colmo",
}


def path_for(code, page):
    """Dosya yolu: kok Ingilizce, digerleri kendi klasorunde."""
    if code == "en":
        return page
    return "%s/%s" % (code, page)


def href_for(code, page):
    """Baglanti yolu. Acilis sayfasi klasor adresiyle (/, /tr/): canonical
    ve og:url eskiden /index.html'i gosteriyordu, ayni sayfa iki adresle
    indeksleniyordu."""
    p = "/" + path_for(code, page)
    if p.endswith("index.html"):
        p = p[:-len("index.html")]
    return p


def url_for(code, page):
    return SITE + href_for(code, page)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def mail_link():
    """Cloudflare'in adres gizlemesi mailto'yu JS'siz tarayicida 404 veren
    /cdn-cgi/l/email-protection adresine ceviriyor; email_off durduruyor."""
    return ('<!--email_off--><a href="mailto:%s">%s</a><!--/email_off-->'
            % (MAIL, MAIL))


def lang_bar(code, page, codes):
    """Dil secici. Dar ekranda kisa kod (EN, TR...), genis ekranda tam ad;
    tam ad ekran okuyucu icin her zaman yerinde."""
    out = []
    for c, lang, _loc, name, short in LANGS:
        if c not in codes:
            continue
        cur = ' aria-current="page"' if c == code else ""
        out.append('<a href="%s" hreflang="%s" lang="%s"%s>'
                   '<span class="dil-ad">%s</span>'
                   '<span class="dil-kod" aria-hidden="true">%s</span></a>'
                   % (href_for(c, page), lang, lang, cur, name, short))
    return '<div class="diller">%s</div>' % "".join(out)


def head(code, page, title, desc, codes, noindex=False):
    lang = LANG_ATTR[code]
    loc = dict((c, o) for c, _l, o, _n, _k in LANGS)[code]
    if noindex:
        links = ""
        robots = "noindex"
    else:
        alts = ['<link rel="alternate" hreflang="%s" href="%s">'
                % (LANG_ATTR[c], url_for(c, page)) for c in codes]
        alts.append('<link rel="alternate" hreflang="x-default" href="%s">'
                    % url_for("en", page))
        links = ('<link rel="canonical" href="%s">\n    %s\n    '
                 % (url_for(code, page), "\n    ".join(alts)))
        robots = "index, follow"
    preload = "\n    ".join(
        '<link rel="preload" href="/assets/fonts/nunito-%d.woff2" as="font" '
        'type="font/woff2" crossorigin>' % w for w in FONT_WEIGHTS)
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="%(desc)s">
    <meta name="robots" content="%(robots)s">
    <meta property="og:type" content="website">
    <meta property="og:url" content="%(url)s">
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
    %(links)s<link rel="icon" type="image/png" href="/favicon.png">
    <link rel="apple-touch-icon" href="/assets/colmo_icon.png">
    <link rel="manifest" href="/manifest.json">
    %(preload)s
    <link rel="stylesheet" href="/css/%(css)s">
</head>
<body>
""" % dict(lang=lang, desc=esc(desc), site=SITE, url=url_for(code, page),
           title=esc(title), loc=loc, links=links, robots=robots,
           preload=preload,
           css="style.css" if page == "index.html" else "legal.css")


def header(code, page, codes):
    return """<header class="ust">
    <div class="kap">
        <a class="marka" href="%(home)s">
            <img src="/assets/colmo_icon.png" alt="Colmo" width="40" height="40">
            <b>COLMO</b>
        </a>
        %(bar)s
    </div>
</header>
""" % dict(home=href_for(code, "index.html"), bar=lang_bar(code, page, codes))


# ── altbilgi: aile blogu ────────────────────────────────────────────────────
#
# Uc oyun sitesinde (decimo, colmo, palmo) altbilgi AYNI yapida: solda
# Bardino'nun kendi logosu (isaret + yazi, altinda slogan yok), sagda tek
# cumle ve iki kardes oyunun karti, en altta yasal satir. Her site bunu kendi
# kurallariyla ciziyor; yapi ortak, gorunum oyunun.
#
# Logo uc oyunun acilisindaki tasli kilit (isaret + yazi + taslar), ayni
# geometri; gorunur olunca ayni filmi oynar (assets/bardino-intro.js, dort
# sitede birebir ayni). Yazi currentColor; kontur --bi-edge.
BARDINO_LOGO = (
    '<svg class="aile-logo bardino-intro" viewBox="0 0 600 150" data-bardino-intro role="img" aria-label="Bardino"><g class="bi-mark"><g transform="translate(0 6) scale(1.12)"><rect x="4.5" y="9.5" width="91" height="87" rx="21" class="bi-ef bi-es" stroke-width="5"/><rect x="4.5" y="3" width="91" height="87" rx="21" fill="#FFC83D" class="bi-es" stroke-width="5"/><g fill="none" stroke="#1B2F4A" stroke-width="11.2" stroke-linecap="round"><path d="M37.1 22.1V68.9"/><circle cx="51.5" cy="54.5" r="14.4"/></g></g></g><g class="bi-word"><g transform="translate(134 8) scale(.62)" fill="none" stroke="currentColor" stroke-width="28" stroke-linecap="round" stroke-linejoin="round"><path d="M16 19V136"/><circle cx="52" cy="100" r="36"/><circle cx="166" cy="100" r="36"/><path d="M202 64V136"/><path d="M252 64V136M252 100A36 36 0 0 1 297.32 65.23"/><circle cx="374" cy="100" r="36"/><path d="M410 19V136"/><path d="M460 64V136"/><path d="M510 64V136M510 100A36 36 0 0 1 582 100V136"/><circle cx="664" cy="100" r="36"/></g></g><g transform="translate(139 112) scale(.65)"><g class="bi-stone"><rect x="2" y="6" width="32" height="32" rx="9" class="bi-ef bi-es" stroke-width="3.5"/><rect x="2" y="2" width="32" height="32" rx="9" fill="#2E2C7A" class="bi-es" stroke-width="3.5"/></g><g class="bi-stone"><rect x="44" y="6" width="32" height="32" rx="9" class="bi-ef bi-es" stroke-width="3.5"/><rect x="44" y="2" width="32" height="32" rx="9" fill="#FF5BA3" class="bi-es" stroke-width="3.5"/></g><g class="bi-stone"><rect x="86" y="6" width="32" height="32" rx="9" class="bi-ef bi-es" stroke-width="3.5"/><rect x="86" y="2" width="32" height="32" rx="9" fill="#ABD7B6" class="bi-es" stroke-width="3.5"/></g></g><g class="bi-dot" transform="translate(419.2 30.94)"><rect x="-9.92" y="-19.84" width="19.84" height="19.84" rx="5.58" fill="#FFC83D" class="bi-es" stroke-width="3.1"/></g></svg>')

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


def studio_url(code):
    return "https://bardino.app/tr/" if code == "tr" else "https://bardino.app/"


def kardes_url(g, code):
    """Kardesin sitesi, ayni dilde. Uc site de ayni yapida: kok Ingilizce,
    digerleri /<kod>/ (Decimo'nun sitesi Ekim 2026'da alti dile gecti)."""
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
""" % dict(studyo=studio_url(code), logo=BARDINO_LOGO,
           lead=esc(t["aile_lead"]), kart=kart)


SEP = '<span class="f-ayrac" aria-hidden="true"> · </span>'


def footer(code, t):
    """Uc oyun sitesinde ayni sira: Gizlilik politikasi · Kullanim kosullari
    · Hesap silme · Destek: e-posta; altinda studyo satiri ve cerez notu.
    EN ve TR disindaki diller Ingilizce yasal sayfalara baglanir."""
    p, tm, ad = t["legal"]
    lc = code if code in LEGAL_LANGS else "en"
    links = SEP.join([
        '<a href="%s">%s</a>' % (href_for(lc, "privacy.html"), esc(p)),
        '<a href="%s">%s</a>' % (href_for(lc, "terms.html"), esc(tm)),
        '<a href="%s">%s</a>' % (href_for(lc, "account-deletion.html"), esc(ad)),
        # Fransizca iki noktadan once bosluk ister (bolunmez).
        '%s%s: %s' % (esc(t["support"]), NBSP if code == "fr" else "",
                      mail_link()),
    ])
    return """<footer class="aile">
%(aile)s    <div class="kap aile-alt">
        <p class="f-baglantilar">%(links)s</p>
        <p class="f-imza"><a href="%(studio_url)s">%(studio)s</a>%(sep)s&copy; 2026 Bardino Technology</p>
        <p class="f-not">%(nocookie)s</p>
    </div>
</footer>

<script src="/assets/bardino-intro.js" defer></script>
</body>
</html>
""" % dict(aile=aile(code, t, ("decimo", "palmo")), links=links, sep=SEP,
           studio_url=studio_url(code), studio=esc(t["studio"]),
           nocookie=esc(t["nocookie"]))


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

    Agustos 2026'daki surum kurali hic anlatmiyordu ("oyunun kendisi kurali
    yaziyla anlatmiyor; sitesi de anlatmamali"). Ekim 2026 denetimi bunun
    bedelini gosterdi: sayfa oyunun ne oldugunu soylemiyordu. Simdi uc kisa
    kartta kural var. Her cumle oyunun magaza metninden (android/fastlane/
    metadata/android/<dil>/full_description.txt) ve koddan dogrulandi: mum
    muhur yalniz komsu YILDIZLI kavanoz patlayinca erir (lib/engine/game.dart),
    joker adlari oyunun kendi etiketleri (lib/l10n/app_*.arb jokerPark/Undo/
    Swap), bolum sayisi lib/engine/level.dart totalLevels = 120.

    Gorunen her kavanoz hala oyunun kendi karesinden geliyor, hicbiri siteye
    cizilmedi.
    """
    caps = t["caps"]
    shots = "".join(
        '<figure><img src="/assets/shots/%s" alt="%s" width="800" height="1422" loading="lazy"><figcaption>%s</figcaption></figure>'
        % (f, esc(c), esc(c))
        for f, c in zip(["01_board.webp", "02_wax.webp", "03_result.webp",
                         "04_map.webp"], caps))
    how = "".join(
        '<li class="adim"><h3>%s</h3><p>%s</p></li>' % (esc(h), p)
        for h, p in t["how"])
    return (head(code, "index.html", t["title"], t["desc"], ALL_CODES)
            + header(code, "index.html", ALL_CODES)
            + """
<section class="kahraman">
    <div class="kap">
        <div>
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

<section class="nasil">
    <div class="kap">
        <h2>%(howT)s</h2>
        <ol class="adimlar">%(how)s</ol>
    </div>
</section>

<section class="bant">
    <img src="/assets/colmo_share.png" alt="%(bandAlt)s" width="1200" height="630" loading="lazy">
</section>

<section class="duvar-bolum">
    <div class="kap">
        <h2>%(shotsT)s</h2>
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
""" % dict(h1a=esc(t["h1a"]), h1b=esc(t["h1b"]),
           lead=esc(t["lead"]), small=esc(t["small"]), cap0=esc(caps[0]),
           howT=esc(t["howT"]), how=how,
           bandAlt=esc(t["bandAlt"]),
           shotsT=esc(t["shotsT"]), shots=shots,
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


def human_date(code, iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return "%d %s %d" % (d, MONTHS[code][m - 1], y)


def legal(code, t, page, title, desc, date, body):
    return (head(code, page, "%s - Colmo" % title, desc, LEGAL_LANGS)
            + header(code, page, LEGAL_LANGS)
            + """
<section class="yasal">
    <div class="kap">
        <a class="geri" href="%(home)s">&larr; %(back)s</a>
        <h1>%(title)s</h1>
        <p class="tarih">%(upd)s: <time datetime="%(iso)s">%(date)s</time></p>
        <div class="govde">%(body)s</div>
    </div>
</section>
""" % dict(home=href_for(code, "index.html"), back=esc(t["back"]),
           title=esc(title), iso=date, date=human_date(code, date),
           body=body, upd=t["upd"])
            + footer(code, t))


def write(rel, text):
    p = os.path.join(HERE, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(p) else None
    io.open(p, "w", encoding="utf-8", newline="\n").write(text)
    return rel


if __name__ == "__main__":
    import legal_text

    made = []
    for code in ALL_CODES:
        t = T[code]
        made.append(write(path_for(code, "index.html"), landing(code, t)))
        if code in LEGAL_LANGS:
            for page, title, desc, date, body in legal_text.pages(code):
                made.append(write(path_for(code, page),
                                  legal(code, t, page, title, desc, date,
                                        body)))

    # ── sabit dosyalar ──────────────────────────────────────────────────
    write("CNAME", "colmo.bardino.app\n")
    write("robots.txt",
          "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
    urls = "".join(
        "  <url><loc>%s</loc></url>\n" % url_for(c, p)
        for c in ALL_CODES
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
    write("404.html", head("en", "index.html", "Colmo", T["en"]["desc"],
                           ALL_CODES, noindex=True)
          + header("en", "index.html", ALL_CODES)
          + '\n<section class="kapanis"><div class="kap"><div class="kutu">'
            '<h2>Nothing here.</h2>'
            '<p class="bolum-alt">That page does not exist. '
            '<a href="/">Back to Colmo</a>.</p>'
            '</div></div></section>\n'
          + footer("en", T["en"]))

    print("uretilen sayfa: %d" % len(made))
    for m in sorted(made):
        print("  " + m)
