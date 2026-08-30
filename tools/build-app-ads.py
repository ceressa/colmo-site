# -*- coding: utf-8 -*-
"""Colmo'nun sarilmis app-ads.txt dosyasini yerinde onarir.

    python tools/build-app-ads.py            # kuru calisma, raporla
    python tools/build-app-ads.py --write    # ../app-ads.txt uzerine yaz
    python tools/build-app-ads.py --src X    # baska bir kaynaktan uret

Dosya bir web sayfasindan kopyalanirken 45 karakterde SERT sarilmis; kendi
DIRECT satiri bile ikiye bolunmus:

    google.com, pub-1767292468741192, DIRECT, f08
    c47fec0942fa0

Ayristirici boyle bir dosyayi okuyamaz, envanter yetkisiz sayilir. Sarma
satir sonu EKLEYEREK bozdugu icin onarim mumkun: yorumlar atilir, kalan her
sey aralarina hicbir sey konmadan tek bir dizeye yapistirilir, sonra kayit
dilbilgisiyle yeniden bolunur.

Kayit dilbilgisi (IAB app-ads.txt): alanadi, yayinciKimligi, DIRECT|RESELLER
[, sertifikaKimligi]. Kayit sonu bu uc sozcukten biriyle ya da onu izleyen
onaltilik kimlikle bittigi icin sinirlar belirsiz degil.

Kaynak ve hedef ayni dosya oldugu icin once tamami bellege okunur, cozumleme
biter ve dogrulamadan gecerse gecici dosyaya yazilip yerine tasinir. Artik ya
da bicimi bozuk kayit varsa hic yazilmaz: yarim onarilmis bir app-ads.txt,
bozuk olandan daha tehlikelidir cunku bakildiginda duzgun gorunur.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DST = os.path.join(os.path.dirname(HERE), "app-ads.txt")

PUB = "pub-1767292468741192"
DIRECT = "google.com, %s, DIRECT, f08c47fec0942fa0" % PUB

RECORD = re.compile(
    r"[a-z0-9][a-z0-9.\-]*\.[a-z]{2,},"      # satici alan adi
    r"[^,]{1,80},"                            # yayinci kimligi
    r"(?:DIRECT|RESELLER)"                    # iliski
    # Sertifika kimligi TAM 16 onaltilik: TAG-ID boyu. Araligi {16,32} yapmak
    # sonraki kaydin ilk harfini yutuyor ve "e-planning.net" kaydi
    # "planning.net" olarak cikiyor - alan adi degistigi icin satir sessizce
    # yanlis, bicim kontrolunden de geciyor.
    r"(?:,[0-9a-fA-F]{16})?",
    re.IGNORECASE)

HEADER = [
    "# Colmo - app-ads.txt",
    "#",
    "# Yayinci: Bardino Technology / AdMob %s." % PUB,
    "# Yetkili satici listesi hesap duzeyinde, o yuzden Decimo ve Palmo ile",
    "# ayni. Magaza kaydindaki web sitesi alani colmo.dozi.app oldugu icin",
    "# dogrulama bu dosyadan yapiliyor.",
    "#",
    "# Reklam ACIK (2026-08-26). Android app id ...~4254427973,",
    "# iOS ...~3512191947; ikisi de bu yayincinin altinda.",
    "#",
    "# Bu dosya tools/build-app-ads.py ile uretildi. ELLE DUZENLEME: kopyala",
    "# yapistir satirlari sarar ve DIRECT satirini ikiye boler; ayristirici",
    "# o dosyayi okuyamaz ve envanter yetkisiz sayilir.",
    "#",
    "# Yayina aldiktan SONRA https://colmo.dozi.app/app-ads.txt adresini GET",
    "# ile geri oku. Yazma isleminin \"basarili\" demesi yetmez.",
    "",
]


def parse(raw):
    # Yorum ve bos satirlari at, kalani BOSLUKSUZ yapistir: sarma yalnizca
    # satir sonu ekledi, karakter silmedi.
    blob = "".join(l.strip() for l in raw
                   if l.strip() and not l.lstrip().startswith("#"))
    blob = blob.replace(" ", "")

    records, pos, gaps = [], 0, []
    for m in RECORD.finditer(blob):
        if m.start() != pos:
            gaps.append(blob[pos:m.start()])
        records.append(m.group(0))
        pos = m.end()
    if pos != len(blob):
        gaps.append(blob[pos:])
    return records, gaps


def main():
    argv = sys.argv[1:]
    src = DST
    if "--src" in argv:
        src = argv[argv.index("--src") + 1]

    with open(src, encoding="utf-8", errors="replace") as f:
        raw = f.readlines()

    records, gaps = parse(raw)

    seen, out = set(), []
    for r in records:
        line = ", ".join(p.strip() for p in r.split(","))
        k = line.lower()
        if k not in seen:
            seen.add(k)
            out.append(line)

    # Kendi DIRECT satirimiz her zaman bassa ve DOGRU olmali.
    out = [DIRECT] + [l for l in out if PUB not in l]
    bad = [l for l in out if not RECORD.fullmatch(l.replace(" ", ""))]

    print("kaynak            :", src)
    print("kaynak satir      :", len(raw))
    print("cozulen kayit     :", len(records))
    print("tekillestirilmis  :", len(out))
    print("artik (cozulemeyen):", len(gaps))
    for g in gaps[:5]:
        print("   ->", g[:90])
    print("bicimi bozuk      :", len(bad))
    for b in bad[:5]:
        print("   ->", b[:90])
    print("ilk satir         :", out[0])
    print("e-planning        :", next(
        (l for l in out if l.startswith("e-planning.")), "YOK"))

    if gaps or bad:
        print("\nArtik ya da bicimi bozuk kayit var, yazilmadi.")
        return 1

    if "--write" not in argv:
        print("\nKuru calisma. Yazmak icin: --write")
        return 0

    tmp = DST + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(HEADER + out) + "\n")
    os.replace(tmp, DST)
    print("\nyazildi:", DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
