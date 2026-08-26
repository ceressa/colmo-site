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
    "title": "Colmo - Fill every jar to exactly its number",
    "desc": "A calm number puzzle. Every jar wants an exact amount: never "
            "short, never over. 60 levels plus endless. Coming soon to "
            "Android and iOS.",
    "badge": "Coming soon",
    "h1a": "Every jar wants",
    "h1b": "an exact amount.",
    "lead": "Doses arrive one at a time. A jar that reaches its number "
            "exactly bursts and is shelved. Short is fine, over is refused. "
            "The rule takes one move to learn and sixty levels to finish.",
    "small": "Free. Plays offline. No ads at launch.",
    "howT": "One rule, no tutorial",
    "howS": "Nothing is explained in words. The board is built so the rule "
            "explains itself on the first move.",
    "steps": [
        ("Fill to the number",
         "The number on the jar is what it wants in total. Reach it exactly "
         "and the jar bursts. Two doses, three, it does not matter how you "
         "get there."),
        ("Over is refused, free",
         "A dose that would overshoot never lands. Nothing is spent and "
         "nothing is lost; the jar simply shows you what would not fit."),
        ("Some jars have a temper",
         "A narrow neck takes only small doses and stamps its limit above "
         "its mouth. A waxed jar takes nothing at all until the jar beside "
         "it bursts."),
    ],
    "inT": "What is in it",
    "inS": "No energy timer, no lives, no waiting. You can finish it without "
           "paying anything, because there is nothing to pay for.",
    "feats": [
        ("60", "Hand built levels",
         "Not generated and shipped. Every board is solved by a reference "
         "bot before it ships, and its budget comes from that solution."),
        ("8", "Levels that teach",
         "The first eight introduce one idea each, with no text at all. "
         "The form of the board does the teaching."),
        ("6", "Languages",
         "English, Turkish, German, French, Spanish, Portuguese. The board "
         "itself is wordless, so nothing gets lost."),
        ("0", "Ads at launch",
         "No banners, no forced videos, no energy you have to wait for."),
    ],
    "shotsT": "From the game",
    "shotsS": "Real screenshots, not mock-ups.",
    "caps": ["A narrow neck stamps its limit",
             "A waxed jar opens when its neighbour bursts",
             "Stars come from what you did not spend",
             "The shelf wall you climb"],
    "endT": "Not out yet.",
    "endS": "Colmo is in final testing on Android, with iOS to follow. This "
            "page will carry the store links the day it is out.",
    "legal": ("Privacy", "Terms of use", "Account deletion"),
    "by": "Colmo is made by",
    "back": "Back to Colmo",
}

T["tr"] = {
    "title": "Colmo - Her kavanozu tam sayısına kadar doldur",
    "desc": "Sakin bir sayı bulmacası. Her kavanoz tam bir miktar istiyor: "
            "eksik olur, fazla olmaz. 60 bölüm ve sonsuz mod. Android ve "
            "iOS'ta çok yakında.",
    "badge": "Çok yakında",
    "h1a": "Her kavanoz",
    "h1b": "tam bir miktar istiyor.",
    "lead": "Dozlar tek tek geliyor. Sayısına tam ulaşan kavanoz patlıyor ve "
            "rafa kalkıyor. Eksik kalmak serbest, taşmak reddediliyor. Kural "
            "bir hamlede öğreniliyor, altmış bölümde bitiyor.",
    "small": "Ücretsiz. İnternetsiz oynanır. Lansmanda reklam yok.",
    "howT": "Tek kural, sıfır eğitim",
    "howS": "Hiçbir şey yazıyla anlatılmıyor. Tahta, kuralı ilk hamlede kendi "
            "anlatacak şekilde kuruldu.",
    "steps": [
        ("Sayısına kadar doldur",
         "Kavanozun üzerindeki sayı toplamda ne istediği. Tam o sayıya "
         "ulaşınca kavanoz patlıyor. İki dozla mı üç dozla mı, fark etmiyor."),
        ("Taşan doz bedava reddedilir",
         "Taşıracak bir doz hiç yerleşmiyor. Ne harcanıyor ne kaybediliyor; "
         "kavanoz sadece neyin sığmayacağını gösteriyor."),
        ("Bazı kavanozların huyu var",
         "Dar boyunlu olan yalnızca küçük dozları alıyor ve sınırını ağzının "
         "üstüne damgalıyor. Mühürlü olan, yanındaki kavanoz patlayana kadar "
         "hiçbir şey almıyor."),
    ],
    "inT": "İçinde neler var",
    "inS": "Enerji sayacı yok, can yok, bekleme yok. Hiçbir şey ödemeden "
           "sonuna kadar gidiyorsun, çünkü ödenecek bir şey yok.",
    "feats": [
        ("60", "Elle kurulmuş bölüm",
         "Üretilip bırakılmadı. Her tahta yayına girmeden önce referans bir "
         "çözücüyle çözülüyor ve bütçesi o çözümden geliyor."),
        ("8", "Öğreten bölüm",
         "İlk sekizi tek tek birer fikir tanıtıyor, hem de hiç yazı "
         "kullanmadan. Öğreten şey tahtanın biçimi."),
        ("6", "Dil",
         "İngilizce, Türkçe, Almanca, Fransızca, İspanyolca, Portekizce. "
         "Tahta zaten dilsiz, o yüzden hiçbir şey kaybolmuyor."),
        ("0", "Lansmanda reklam",
         "Banner yok, zorunlu video yok, beklemen gereken enerji yok."),
    ],
    "shotsT": "Oyundan kareler",
    "shotsS": "Hepsi gerçek ekran görüntüsü, temsili değil.",
    "caps": ["Dar boyun sınırını damgalıyor",
             "Mühür, komşusu patlayınca açılıyor",
             "Yıldız harcamadığından geliyor",
             "Tırmandığın raf duvarı"],
    "endT": "Henüz çıkmadı.",
    "endS": "Colmo Android'de son testlerinde, ardından iOS geliyor. Çıktığı "
            "gün mağaza bağlantıları bu sayfada olacak.",
    "legal": ("Gizlilik", "Kullanım koşulları", "Hesap silme"),
    "by": "Colmo,",
    "back": "Colmo'ya dön",
}

T["de"] = {
    "title": "Colmo - Fülle jedes Glas exakt bis zu seiner Zahl",
    "desc": "Ein ruhiges Zahlenpuzzle. Jedes Glas will eine exakte Menge: "
            "nie zu wenig, nie zu viel. 60 Level und Endlosmodus. Bald für "
            "Android und iOS.",
    "badge": "Bald verfügbar",
    "h1a": "Jedes Glas will",
    "h1b": "eine exakte Menge.",
    "lead": "Die Dosen kommen einzeln. Ein Glas, das seine Zahl genau "
            "erreicht, platzt und kommt ins Regal. Zu wenig ist erlaubt, zu "
            "viel wird abgelehnt. Die Regel lernt man in einem Zug.",
    "small": "Kostenlos. Auch offline spielbar. Zum Start ohne Werbung.",
    "howT": "Eine Regel, kein Tutorial",
    "howS": "Nichts wird in Worten erklärt. Das Brett ist so gebaut, dass die "
            "Regel sich im ersten Zug selbst erklärt.",
    "steps": [
        ("Bis zur Zahl füllen",
         "Die Zahl auf dem Glas ist, was es insgesamt will. Genau treffen, "
         "und das Glas platzt. Ob mit zwei oder drei Dosen, ist egal."),
        ("Zu viel wird gratis abgelehnt",
         "Eine Dose, die überlaufen würde, landet gar nicht erst. Nichts wird "
         "verbraucht und nichts geht verloren."),
        ("Manche Gläser haben Eigenheiten",
         "Ein enger Hals nimmt nur kleine Dosen und zeigt seine Grenze über "
         "der Öffnung. Ein versiegeltes Glas nimmt gar nichts, bis das Glas "
         "daneben platzt."),
    ],
    "inT": "Was drin ist",
    "inS": "Keine Energieanzeige, keine Leben, kein Warten. Du kommst bis zum "
           "Ende, ohne etwas zu bezahlen.",
    "feats": [
        ("60", "Handgebaute Level",
         "Nicht einfach generiert. Jedes Brett wird vor der Auslieferung von "
         "einem Referenzlöser gelöst."),
        ("8", "Level, die lehren",
         "Die ersten acht führen je eine Idee ein, ganz ohne Text. Es lehrt "
         "die Form des Bretts."),
        ("6", "Sprachen",
         "Englisch, Türkisch, Deutsch, Französisch, Spanisch, "
         "Portugiesisch. Das Brett selbst ist wortlos."),
        ("0", "Werbung zum Start",
         "Keine Banner, keine Pflichtvideos, keine Energie zum Abwarten."),
    ],
    "shotsT": "Aus dem Spiel",
    "shotsS": "Echte Screenshots, keine Montagen.",
    "caps": ["Ein enger Hals zeigt seine Grenze",
             "Das Siegel öffnet sich beim Nachbarn",
             "Sterne kommen vom Nichtverbrauchen",
             "Die Regalwand, die du hochsteigst"],
    "endT": "Noch nicht erschienen.",
    "endS": "Colmo ist auf Android im letzten Test, iOS folgt. Am Tag der "
            "Veröffentlichung stehen die Store-Links hier.",
    "legal": ("Datenschutz", "Nutzungsbedingungen", "Konto löschen"),
    "by": "Colmo stammt von",
    "back": "Zurück zu Colmo",
}

T["fr"] = {
    "title": "Colmo - Remplis chaque bocal exactement à son nombre",
    "desc": "Un puzzle de nombres apaisant. Chaque bocal veut une quantité "
            "exacte : jamais trop peu, jamais trop. 60 niveaux et un mode "
            "infini. Bientôt sur Android et iOS.",
    "badge": "Bientôt disponible",
    "h1a": "Chaque bocal veut",
    "h1b": "une quantité exacte.",
    "lead": "Les doses arrivent une par une. Un bocal qui atteint son nombre "
            "exactement éclate et rejoint l'étagère. En dessous, c'est "
            "permis ; au dessus, c'est refusé.",
    "small": "Gratuit. Jouable hors ligne. Sans publicité au lancement.",
    "howT": "Une règle, aucun tutoriel",
    "howS": "Rien n'est expliqué avec des mots. Le plateau est construit pour "
            "que la règle s'explique au premier coup.",
    "steps": [
        ("Remplir jusqu'au nombre",
         "Le nombre sur le bocal est ce qu'il veut au total. Atteins-le "
         "exactement et le bocal éclate. Deux doses ou trois, peu importe."),
        ("Le trop-plein est refusé, gratuitement",
         "Une dose qui déborderait ne se pose jamais. Rien n'est dépensé et "
         "rien n'est perdu."),
        ("Certains bocaux ont un caractère",
         "Un col étroit n'accepte que de petites doses et affiche sa limite "
         "au-dessus de son ouverture. Un bocal scellé n'accepte rien tant que "
         "son voisin n'a pas éclaté."),
    ],
    "inT": "Ce qu'il contient",
    "inS": "Pas de jauge d'énergie, pas de vies, pas d'attente. Tu vas "
           "jusqu'au bout sans rien payer.",
    "feats": [
        ("60", "Niveaux construits à la main",
         "Pas simplement générés. Chaque plateau est résolu par un solveur de "
         "référence avant publication."),
        ("8", "Niveaux qui enseignent",
         "Les huit premiers introduisent une idée chacun, sans aucun texte."),
        ("6", "Langues",
         "Anglais, turc, allemand, français, espagnol, portugais. Le plateau "
         "lui-même est sans mots."),
        ("0", "Publicité au lancement",
         "Pas de bannière, pas de vidéo obligatoire, pas d'énergie à "
         "attendre."),
    ],
    "shotsT": "Images du jeu",
    "shotsS": "De vraies captures, pas des maquettes.",
    "caps": ["Un col étroit affiche sa limite",
             "Le sceau s'ouvre quand le voisin éclate",
             "Les étoiles viennent du non-dépensé",
             "Le mur d'étagères que tu grimpes"],
    "endT": "Pas encore sorti.",
    "endS": "Colmo est en phase de test final sur Android, iOS suivra. Les "
            "liens vers les stores seront ici le jour de la sortie.",
    "legal": ("Confidentialité", "Conditions d'utilisation",
              "Suppression du compte"),
    "by": "Colmo est réalisé par",
    "back": "Retour à Colmo",
}

T["es"] = {
    "title": "Colmo - Llena cada tarro justo hasta su número",
    "desc": "Un puzle de números tranquilo. Cada tarro quiere una cantidad "
            "exacta: nunca de menos, nunca de más. 60 niveles y modo "
            "infinito. Muy pronto en Android e iOS.",
    "badge": "Muy pronto",
    "h1a": "Cada tarro quiere",
    "h1b": "una cantidad exacta.",
    "lead": "Las dosis llegan de una en una. Un tarro que alcanza su número "
            "exacto estalla y pasa al estante. Quedarse corto vale; pasarse, "
            "no.",
    "small": "Gratis. Se juega sin conexión. Sin anuncios en el lanzamiento.",
    "howT": "Una regla, ningún tutorial",
    "howS": "Nada se explica con palabras. El tablero está hecho para que la "
            "regla se explique sola en la primera jugada.",
    "steps": [
        ("Llenar hasta el número",
         "El número del tarro es lo que quiere en total. Alcánzalo exacto y "
         "el tarro estalla. Con dos dosis o con tres, da igual."),
        ("Pasarse se rechaza, y es gratis",
         "Una dosis que se pasaría no llega a caer. No se gasta nada ni se "
         "pierde nada."),
        ("Algunos tarros tienen carácter",
         "Uno de cuello estrecho solo acepta dosis pequeñas y marca su límite "
         "sobre la boca. Uno sellado no acepta nada hasta que estalla el de "
         "al lado."),
    ],
    "inT": "Qué trae",
    "inS": "Sin barra de energía, sin vidas, sin esperas. Llegas al final sin "
           "pagar nada.",
    "feats": [
        ("60", "Niveles hechos a mano",
         "No solo generados. Cada tablero lo resuelve un solucionador de "
         "referencia antes de publicarse."),
        ("8", "Niveles que enseñan",
         "Los ocho primeros presentan una idea cada uno, sin nada de texto."),
        ("6", "Idiomas",
         "Inglés, turco, alemán, francés, español y portugués. El tablero es "
         "mudo de por sí."),
        ("0", "Anuncios al lanzar",
         "Sin banners, sin vídeos obligatorios, sin energía que esperar."),
    ],
    "shotsT": "Del juego",
    "shotsS": "Capturas reales, no montajes.",
    "caps": ["El cuello estrecho marca su límite",
             "El sello se abre cuando estalla el vecino",
             "Las estrellas salen de lo no gastado",
             "La pared de estantes que subes"],
    "endT": "Todavía no ha salido.",
    "endS": "Colmo está en pruebas finales en Android, y iOS vendrá después. "
            "El día del lanzamiento los enlaces estarán aquí.",
    "legal": ("Privacidad", "Términos de uso", "Eliminar cuenta"),
    "by": "Colmo es de",
    "back": "Volver a Colmo",
}

T["pt"] = {
    "title": "Colmo - Encha cada pote exatamente até o seu número",
    "desc": "Um puzzle de números tranquilo. Cada pote quer uma quantidade "
            "exata: nunca de menos, nunca demais. 60 fases e modo infinito. "
            "Em breve para Android e iOS.",
    "badge": "Em breve",
    "h1a": "Cada pote quer",
    "h1b": "uma quantidade exata.",
    "lead": "As doses chegam uma a uma. Um pote que atinge o seu número "
            "exatamente estoura e vai para a prateleira. Ficar aquém pode; "
            "passar, não.",
    "small": "Grátis. Joga-se offline. Sem anúncios no lançamento.",
    "howT": "Uma regra, nenhum tutorial",
    "howS": "Nada é explicado por palavras. O tabuleiro foi feito para a "
            "regra se explicar sozinha na primeira jogada.",
    "steps": [
        ("Encher até o número",
         "O número do pote é o que ele quer no total. Acerte exato e o pote "
         "estoura. Com duas doses ou três, tanto faz."),
        ("Passar é recusado, de graça",
         "Uma dose que ultrapassaria nem chega a cair. Nada é gasto e nada é "
         "perdido."),
        ("Alguns potes têm temperamento",
         "O de gargalo estreito só aceita doses pequenas e carimba o limite "
         "acima da boca. O lacrado não aceita nada até o vizinho estourar."),
    ],
    "inT": "O que tem dentro",
    "inS": "Sem barra de energia, sem vidas, sem espera. Você chega ao fim "
           "sem pagar nada.",
    "feats": [
        ("60", "Fases feitas à mão",
         "Não apenas geradas. Cada tabuleiro é resolvido por um solucionador "
         "de referência antes de sair."),
        ("8", "Fases que ensinam",
         "As oito primeiras trazem uma ideia cada, sem nenhum texto."),
        ("6", "Idiomas",
         "Inglês, turco, alemão, francês, espanhol e português. O tabuleiro "
         "em si não tem palavras."),
        ("0", "Anúncios no lançamento",
         "Sem banners, sem vídeos obrigatórios, sem energia para esperar."),
    ],
    "shotsT": "Do jogo",
    "shotsS": "Capturas reais, não montagens.",
    "caps": ["O gargalo estreito carimba o limite",
             "O lacre abre quando o vizinho estoura",
             "As estrelas vêm do que não foi gasto",
             "A parede de prateleiras que você sobe"],
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


def jars(a, b, c):
    """Kuralin kendisi: tam dolan patlar, tasan reddedilir."""
    def one(cap, fill, kind):
        pct = min(100, int(round(100.0 * fill / cap)))
        return ('<div class="kvz %(k)s"><div class="cam">'
                '<i style="height:%(p)d%%"></i></div>'
                '<div class="kaide"></div><b>%(c)d</b></div>'
                % dict(k=kind, p=pct, c=cap))
    return '<div class="kavanozlar">%s%s%s</div>' % (
        one(*a), one(*b), one(*c))


def landing(code, t):
    caps = t["caps"]
    steps = "".join(
        '<div class="adim">%s<h3>%s</h3><p>%s</p></div>'
        % (art, esc(h), esc(p))
        for (h, p), art in zip(t["steps"], [
            jars((6, 6, "tam hedef"), (9, 4, ""), (4, 1, "")),
            jars((6, 5, ""), (9, 9, "tam"), (4, 4, "tam")),
            jars((6, 2, "hedef"), (9, 3, ""), (4, 0, "")),
        ]))
    feats = "".join(
        '<div class="ozellik"><div class="sayi">%s</div><h3>%s</h3><p>%s</p></div>'
        % (esc(n), esc(h), esc(p)) for n, h, p in t["feats"])
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

<section class="duvar-bolum">
    <div class="kap">
        <h2>%(howT)s</h2>
        <p class="bolum-alt">%(howS)s</p>
        <div class="adimlar">%(steps)s</div>
    </div>
</section>

<section>
    <div class="kap">
        <h2>%(inT)s</h2>
        <p class="bolum-alt">%(inS)s</p>
        <div class="ozellikler">%(feats)s</div>
    </div>
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
           howT=esc(t["howT"]), howS=esc(t["howS"]), steps=steps,
           inT=esc(t["inT"]), inS=esc(t["inS"]), feats=feats,
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
