# colmo-site

[colmo.bardino.app](https://colmo.bardino.app) - Colmo'nun tanitim sayfasi, gizlilik
politikasi, kullanim kosullari ve hesap silme sayfasi.

Oyun deposu ayri ve ozeldir: `ceressa/colmo` (`com.bardino.colmo`).

## Sayfalar elle yazilmaz, uretilir

```
python build.py
```

Alti dil x (acilis + yasal) elle tutulunca kaciniyor: bir cumleyi
degistirmek icin alti dosyaya dokunmak, beş tanesinin bayat kalmasi demek.
Icerik `build.py` icinde sozluk, yasal metinler `legal_text.py` icinde, HTML
yalnizca cikti. **Uretilen `.html` dosyalarini elle duzenleme**, bir sonraki
derlemede geri gider.

- Acilis sayfasi alti dilde: en (kok), tr, de, fr, es, pt.
- Yasal sayfalar Ingilizce ve Turkce. Yarim cevrilmis bir sozlesme
  cevrilmemis olandan kotudur; diger dillerin altbilgisi Ingilizceye gider.

## Gorseller de uretilir

`assets/` altindaki her sey oyunun kendi varliklarindan cikti: ikon
`assets/brand/icon-1024.png`, ekran goruntuleri `docs/store/shots/`,
paylasim gorseli feature graphic'ten. Siteye ozel gorsel uydurulmuyor.

## Iki kural

**Palet oyunun kendisinden.** `lib/theme.dart` ne diyorsa CSS de onu diyor.
Siteyi gorup uygulamayi acan kisi ayni urune bakmali.

**Golge asla bulanik degil.** Oyunun tasarim sisteminde derinlik kati bir
ofset kabartmadir ("a blur is a bug"). Sitede de hicbir yerde blur yok.

## Yayin

GitHub Pages, `main` dali, kok dizin. `CNAME` dosyasi alan adini tasiyor;
DNS tarafinda `colmo` icin `ceressa.github.io` CNAME kaydi gerekir.

## Magaza baglantilari

Colmo Eylul 2026'dan beri iki magazada. Baglantilar `build.py` basindaki
`APP_STORE` / `GOOGLE_PLAY`, rozetler `assets/badges/<dil>/` altinda: Decimo
deposundaki `store_assets/badges` klasorunden, her dilin resmi rozeti. Google
PNG'sinin seffaf kenari kirpildi ki iki rozet ayni gorunen boyda dursun.
Rozete golge ya da cerceve eklenmez (Apple ve Google kilavuzu).
