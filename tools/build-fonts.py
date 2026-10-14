# -*- coding: utf-8 -*-
"""Nunito'yu siteye gomulu woff2 olarak uretir.

    python tools/build-fonts.py [kaynak_klasor]

Neden: site Nunito'yu fonts.googleapis.com'dan yukluyordu, yani her ziyaretcinin
IP adresi Google'a gidiyordu. Simdi yazi tipi sitenin kendi dosyasi.

Kaynak oyunun kendi TTF'leri (colmo deposu, assets/fonts). Varsayilan yol bu
deponun yanindaki ../../mobile/colmo/assets/fonts. Internetten hicbir sey
indirilmiyor.

Alt kume: Latin + Latin Extended-A (Turkce, Almanca, Fransizca, Ispanyolca,
Portekizce harfler), genel noktalama (tirnaklar, uc nokta, orta nokta), euro
ve ticari marka isareti. Yalnizca CSS'in kullandigi bes kalinlik.
"""
import os
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
DEFAULT_SRC = os.path.normpath(os.path.join(
    SITE, "..", "..", "mobile", "colmo", "assets", "fonts"))
OUT = os.path.join(SITE, "assets", "fonts")

WEIGHTS = {400: "Regular", 600: "SemiBold", 700: "Bold", 800: "ExtraBold",
           900: "Black"}

UNICODES = ("U+0020-007E,U+00A0-00FF,U+0100-017F,U+2010-2027,U+2030-203A,"
            "U+2044,U+20AC,U+2122")

# Turkcenin dort zor harfi; alt kumede yoksa uretim durur.
MUST = [0x0131, 0x0130, 0x015F, 0x015E, 0x011F, 0x011E]


def main(src):
    os.makedirs(OUT, exist_ok=True)
    unicodes = subset.parse_unicodes(UNICODES)
    for w, name in sorted(WEIGHTS.items()):
        ttf = os.path.join(src, "Nunito-%s.ttf" % name)
        out = os.path.join(OUT, "nunito-%d.woff2" % w)
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.hinting = False
        opts.desubroutinize = True
        opts.name_IDs = ["*"]
        opts.name_languages = ["*"]
        font = subset.load_font(ttf, opts)
        sub = subset.Subsetter(opts)
        sub.populate(unicodes=unicodes)
        sub.subset(font)
        subset.save_font(font, out, opts)

        cmap = TTFont(out).getBestCmap()
        missing = [hex(c) for c in MUST if c not in cmap]
        if missing:
            sys.exit("%s: eksik harf %s" % (out, missing))
        print("%s  %6d bayt  %d karakter" % (os.path.relpath(out, SITE),
                                              os.path.getsize(out), len(cmap)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SRC)
