# -*- coding: utf-8 -*-
"""Yasal sayfa metinleri.

Yalnizca Ingilizce ve Turkce tam yazildi; acilis sayfasi alti dilde ama
sozlesme dort dilde daha yarim cevrilmis olsa bunun kimseye faydasi olmazdi.
Diger dillerdeki altbilgi baglantilari Ingilizce surume gidiyor.

Gizlilik metni uygulamadaki `docs/store/PRIVACY_POLICY.md` ile ayni gercegi
anlatmali. Orasi degisince burasi da degisir.
"""

MAIL = "info@dozi.app"
PKG = "com.bardino.colmo"


def _p(*paras):
    return "".join("<p>%s</p>" % x for x in paras)


def _ul(*items):
    return "<ul>%s</ul>" % "".join("<li>%s</li>" % x for x in items)


PRIVACY_EN = (
    "<h2>1. Overview</h2>"
    + _p("Colmo is a number puzzle. It is playable entirely offline and "
         "requires no account. This page describes the small amount of data "
         "the game handles and why.")
    + "<h2>2. What we process</h2>"
    + _ul(
        "<strong>Game progress</strong> (levels cleared, stars, best endless "
        "score, which helper lessons you have seen): stored on your device. "
        "If the device is online, the same data is synced to Google Firebase "
        "under an anonymous identifier so it can be recovered on a new "
        "device. No name, e-mail or contact detail is part of that record.",
        "<strong>Optional Google sign-in</strong>: if you choose it, your "
        "anonymous save is linked to your Google account so it survives a "
        "change of device. We receive only the basic profile (e-mail "
        "address) Google provides for authentication. Signing in is never "
        "required to play.",
        "<strong>Settings</strong> (sound, music, language, haptics): stored "
        "on your device only.",
        "<strong>Gameplay measurement</strong> (Google Analytics for "
        "Firebase): the game records what happened, not who you are. Which "
        "level was started, won, lost or left, how many doses it took, which "
        "helper was used, whether a language was changed. This exists to "
        "answer one question: where the game is too hard or unclear. "
        "Advertising identifiers, ad personalisation and ad-related data are "
        "switched off in code.",
        "<strong>Crash reports</strong> (Firebase Crashlytics): if the game "
        "crashes, the technical details of the crash are sent (device model, "
        "OS version, the point in the code that failed). A game that crashes "
        "silently is a game nobody reports.")
    + "<h2>3. What we do not do</h2>"
    + _ul("No ads are shown at launch. The advertising library ships "
          "inside the app but is never started, so it collects nothing "
          "and requests nothing.",
          "No advertising ID, no ad personalisation, no tracking across apps "
          "or sites.",
          "No location, no contacts, no photos, no microphone.",
          "No selling or sharing of data with third parties.")
    + "<h2>4. Where the data lives</h2>"
    + _p("Cloud saves are stored in Google Firebase (Firestore) in the "
         "project <strong>colmo-bardino</strong>. Access rules restrict every "
         "record to the account that owns it. Firebase's own processing is "
         "covered by Google's privacy documentation.")
    + "<h2>5. Deletion</h2>"
    + _p("Uninstalling the app removes local data. To delete a cloud save, "
         "see <a href=\"/account-deletion.html\">Account deletion</a>.")
    + "<h2>6. Children</h2>"
    + _p("Colmo contains no chat, no user-generated content and no ads. It "
         "does not knowingly collect personal data from children; the only "
         "optional personal datum in the product is the Google e-mail used "
         "for sign-in.")
    + "<h2>7. Changes</h2>"
    + _p("Material changes to this policy will be reflected here with a new "
         "date.")
    + "<h2>8. Contact</h2>"
    + _p("<a href=\"mailto:%s\">%s</a>" % (MAIL, MAIL)))

PRIVACY_TR = (
    "<h2>1. Genel bakış</h2>"
    + _p("Colmo bir sayı bulmacasıdır. Tamamen çevrimdışı oynanabilir ve "
         "hesap gerektirmez. Bu sayfa, oyunun işlediği az miktardaki veriyi "
         "ve nedenini açıklar.")
    + "<h2>2. İşlenen veriler</h2>"
    + _ul(
        "<strong>Oyun ilerlemesi</strong> (bölümler, yıldızlar, sonsuz mod "
        "rekoru, gördüğün joker dersleri): cihazında saklanır. Cihaz "
        "çevrimiçiyse aynı veri, yeni cihazda kurtarılabilmesi için anonim "
        "bir kimlik altında Google Firebase'e eşitlenir. Bu kayıtta isim, "
        "e-posta veya iletişim bilgisi bulunmaz.",
        "<strong>İsteğe bağlı Google girişi</strong>: seçtiğin takdirde "
        "anonim kaydın Google hesabına bağlanır ve cihaz değişse de korunur. "
        "Google'ın kimlik doğrulama için sağladığı temel profil (e-posta "
        "adresi) dışında bir şey almayız. Oynamak için giriş asla şart "
        "değildir.",
        "<strong>Ayarlar</strong> (ses, müzik, dil, titreşim): yalnızca "
        "cihazında saklanır.",
        "<strong>Oynanış ölçümü</strong> (Google Analytics for Firebase): "
        "oyun kim olduğunu değil ne olduğunu kaydeder. Hangi bölüm "
        "başlatıldı, kazanıldı, kaybedildi ya da bırakıldı; kaç doz "
        "harcandı; hangi joker kullanıldı; dil değiştirildi mi. Tek bir "
        "soruya cevap vermek için var: oyun nerede fazla zor ya da "
        "anlaşılmaz. Reklam kimliği, reklam kişiselleştirmesi ve reklamla "
        "ilgili veri kod içinde kapatılmıştır.",
        "<strong>Çökme raporları</strong> (Firebase Crashlytics): oyun "
        "çökerse çökmenin teknik ayrıntısı gönderilir (cihaz modeli, işletim "
        "sistemi sürümü, kodun hangi noktada hata verdiği). Sessizce çöken "
        "bir oyunu kimse bildirmez.")
    + "<h2>3. Yapmadıklarımız</h2>"
    + _ul("Lansmanda reklam gösterilmiyor. Reklam kütüphanesi uygulamanın "
          "içinde yer alıyor ama hiç başlatılmıyor; hiçbir şey toplamıyor "
          "ve hiçbir istek yapmıyor.",
          "Reklam kimliği, reklam kişiselleştirmesi, uygulamalar arası takip "
          "yok.",
          "Konum, rehber, fotoğraf, mikrofon yok.",
          "Üçüncü taraflara veri satışı veya paylaşımı yok.")
    + "<h2>4. Verinin yaşadığı yer</h2>"
    + _p("Bulut kayıtları Google Firebase (Firestore) üzerinde "
         "<strong>colmo-bardino</strong> projesinde tutulur. Erişim "
         "kuralları her kaydı yalnızca sahibi olan hesapla sınırlar. "
         "Firebase'in kendi işleme süreçleri Google'ın gizlilik "
         "dokümantasyonuna tabidir.")
    + "<h2>5. Silme</h2>"
    + _p("Uygulamayı kaldırmak yerel veriyi siler. Bulut kaydını sildirmek "
         "için <a href=\"/tr/account-deletion.html\">Hesap silme</a> "
         "sayfasına bak.")
    + "<h2>6. Çocuklar</h2>"
    + _p("Colmo'da sohbet, kullanıcı içeriği ve reklam yoktur. Çocuklardan "
         "bilerek kişisel veri toplanmaz; üründeki tek isteğe bağlı kişisel "
         "veri, girişte kullanılan Google e-postasıdır.")
    + "<h2>7. Değişiklikler</h2>"
    + _p("Bu politikadaki önemli değişiklikler yeni bir tarihle burada "
         "yayımlanır.")
    + "<h2>8. İletişim</h2>"
    + _p("<a href=\"mailto:%s\">%s</a>" % (MAIL, MAIL)))

TERMS_EN = (
    "<h2>1. The short version</h2>"
    + "<div class=\"vurgu\">"
    + _p("Colmo is a free game. Play it, enjoy it, do not try to break it or "
         "resell it. There is nothing to buy, so there is nothing to refund.")
    + "</div>"
    + "<h2>2. Licence</h2>"
    + _p("Bardino Technology grants you a personal, non-exclusive, "
         "non-transferable licence to install and play Colmo on devices you "
         "control. The game, its artwork, its levels, its sounds and its "
         "code remain ours.")
    + "<h2>3. What you agree not to do</h2>"
    + _ul("Reverse engineer, decompile or modify the app, except where that "
          "right cannot be excluded by law.",
          "Redistribute the app or its assets, or publish it under another "
          "name.",
          "Interfere with the cloud save service, or use it to store "
          "anything other than your own game progress.")
    + "<h2>4. Your saved progress</h2>"
    + _p("Cloud saving is a convenience, not a guarantee. We take reasonable "
         "care, but a lost save is not a compensable loss. Linking a Google "
         "account makes a save far more durable and is the best protection "
         "available.")
    + "<h2>5. Availability and changes</h2>"
    + _p("The game may change. Levels can be rebalanced, features added or "
         "removed, and the service behind cloud saving can be discontinued "
         "with reasonable notice. Nothing here promises a specific feature "
         "will exist forever.")
    + "<h2>6. No warranty</h2>"
    + _p("Colmo is provided as is. To the extent permitted by law, we make no "
         "warranty that it will be uninterrupted or error free, and we are "
         "not liable for indirect or consequential loss arising from its "
         "use.")
    + "<h2>7. Governing law</h2>"
    + _p("These terms are governed by the laws of the Republic of Turkiye. "
         "Nothing in them limits consumer rights you have under the law of "
         "the country you live in.")
    + "<h2>8. Contact</h2>"
    + _p("<a href=\"mailto:%s\">%s</a>" % (MAIL, MAIL)))

TERMS_TR = (
    "<h2>1. Kısa hali</h2>"
    + "<div class=\"vurgu\">"
    + _p("Colmo ücretsiz bir oyundur. Oyna, keyfini çıkar, kırmaya ve "
         "yeniden satmaya çalışma. Satın alınacak bir şey yok, dolayısıyla "
         "iade edilecek bir şey de yok.")
    + "</div>"
    + "<h2>2. Lisans</h2>"
    + _p("Bardino Technology, Colmo'yu kendi kontrolündeki cihazlara kurup "
         "oynaman için kişisel, münhasır olmayan ve devredilemez bir lisans "
         "verir. Oyun, görselleri, bölümleri, sesleri ve kodu bize aittir.")
    + "<h2>3. Yapmamayı kabul ettiklerin</h2>"
    + _ul("Uygulamayı tersine mühendislik yapmak, kaynak koda çevirmek ya da "
          "değiştirmek (kanunen hariç tutulamayan haller dışında).",
          "Uygulamayı ya da varlıklarını yeniden dağıtmak, başka bir adla "
          "yayımlamak.",
          "Bulut kayıt hizmetine müdahale etmek ya da onu kendi oyun "
          "ilerlemen dışında bir şey saklamak için kullanmak.")
    + "<h2>4. Kayıtlı ilerlemen</h2>"
    + _p("Bulut kaydı bir kolaylık, garanti değil. Makul özeni gösteriyoruz "
         "ama kaybolan bir kayıt tazmin edilebilir bir zarar değildir. "
         "Google hesabı bağlamak kaydı çok daha dayanıklı kılar ve mevcut en "
         "iyi korumadır.")
    + "<h2>5. Erişilebilirlik ve değişiklikler</h2>"
    + _p("Oyun değişebilir. Bölümler yeniden dengelenebilir, özellikler "
         "eklenebilir ya da kaldırılabilir, bulut kaydının arkasındaki hizmet "
         "makul bir bildirimle sonlandırılabilir. Burada hiçbir özelliğin "
         "sonsuza kadar var olacağı vaat edilmiyor.")
    + "<h2>6. Garanti yok</h2>"
    + _p("Colmo olduğu gibi sunulur. Kanunun izin verdiği ölçüde, kesintisiz "
         "ya da hatasız çalışacağına dair bir garanti vermiyoruz ve "
         "kullanımından doğan dolaylı zararlardan sorumlu değiliz.")
    + "<h2>7. Uygulanacak hukuk</h2>"
    + _p("Bu koşullar Türkiye Cumhuriyeti kanunlarına tabidir. Buradaki "
         "hiçbir hüküm, yaşadığın ülkenin kanunlarından doğan tüketici "
         "haklarını sınırlamaz.")
    + "<h2>8. İletişim</h2>"
    + _p("<a href=\"mailto:%s\">%s</a>" % (MAIL, MAIL)))

DELETE_EN = (
    "<h2>Deleting local progress</h2>"
    + _p("Uninstalling Colmo removes everything stored on the device. You can "
         "also reset without uninstalling: <strong>Menu &rarr; Settings &rarr; "
         "Reset progress</strong>. That clears levels, stars, records and the "
         "helper lessons, and keeps your sound and language preferences.")
    + "<h2>Deleting a cloud save</h2>"
    + "<div class=\"vurgu\">"
    + _p("Write to <a href=\"mailto:%s?subject=Colmo%%20account%%20deletion\">"
         "%s</a> with the subject <strong>Colmo account deletion</strong>."
         % (MAIL, MAIL))
    + "</div>"
    + _ul("<strong>If you signed in with Google</strong>: send the mail from "
          "that same Google address. That is all the proof we need.",
          "<strong>If you never signed in</strong>: your save is under an "
          "anonymous identifier we cannot look up from an e-mail. Uninstall "
          "the app instead; the orphaned record is removed in the routine "
          "clean-up described below.")
    + "<h2>What gets deleted</h2>"
    + _p("The whole record: level progress, stars, endless best score, the "
         "list of lessons you have seen, and the link to your Google "
         "account. Nothing is kept in a backup copy afterwards.")
    + "<h2>How long it takes</h2>"
    + _p("We action requests within 30 days and normally much sooner. "
         "Anonymous records with no activity are cleared periodically, so a "
         "save you abandon does not sit there forever.")
    + "<h2>What we cannot delete</h2>"
    + _p("Crash reports and gameplay measurement are not tied to your "
         "identity and cannot be located per person; they carry no name, no "
         "e-mail and no advertising ID. Anything you sent us by e-mail stays "
         "in the mailbox unless you ask us to remove it too.")
    + "<h2>Contact</h2>"
    + _p("<a href=\"mailto:%s\">%s</a> &middot; %s" % (MAIL, MAIL, PKG)))

DELETE_TR = (
    "<h2>Cihazdaki ilerlemeyi silme</h2>"
    + _p("Colmo'yu kaldırmak cihazda saklanan her şeyi siler. Kaldırmadan da "
         "sıfırlayabilirsin: <strong>Menü &rarr; Ayarlar &rarr; İlerlemeyi "
         "sıfırla</strong>. Bu; bölümleri, yıldızları, rekorları ve joker "
         "derslerini temizler, ses ve dil tercihlerin kalır.")
    + "<h2>Bulut kaydını silme</h2>"
    + "<div class=\"vurgu\">"
    + _p("<a href=\"mailto:%s?subject=Colmo%%20hesap%%20silme\">%s</a> "
         "adresine <strong>Colmo hesap silme</strong> konusuyla yaz."
         % (MAIL, MAIL))
    + "</div>"
    + _ul("<strong>Google ile giriş yaptıysan</strong>: postayı aynı Google "
          "adresinden gönder. İhtiyacımız olan kanıt bu kadar.",
          "<strong>Hiç giriş yapmadıysan</strong>: kaydın, bir e-postadan "
          "bulamayacağımız anonim bir kimlik altında. Bu durumda uygulamayı "
          "kaldırman yeterli; sahipsiz kalan kayıt aşağıdaki rutin "
          "temizlikte siliniyor.")
    + "<h2>Ne siliniyor</h2>"
    + _p("Kaydın tamamı: bölüm ilerlemesi, yıldızlar, sonsuz mod rekoru, "
         "gördüğün derslerin listesi ve Google hesabınla olan bağ. "
         "Sonrasında yedek bir kopya tutulmuyor.")
    + "<h2>Ne kadar sürer</h2>"
    + _p("Talepleri 30 gün içinde, çoğunlukla çok daha erken işliyoruz. "
         "Hiçbir hareketi olmayan anonim kayıtlar periyodik olarak "
         "temizleniyor; bıraktığın bir kayıt orada sonsuza kadar durmuyor.")
    + "<h2>Silemediklerimiz</h2>"
    + _p("Çökme raporları ve oynanış ölçümü kimliğine bağlı değildir ve kişi "
         "bazında bulunamaz; içinde isim, e-posta ve reklam kimliği yoktur. "
         "Bize e-postayla gönderdiğin her şey, sen istemediğin sürece posta "
         "kutusunda kalır.")
    + "<h2>İletişim</h2>"
    + _p("<a href=\"mailto:%s\">%s</a> &middot; %s" % (MAIL, MAIL, PKG)))

def pages(code):
    """(dosya, baslik, govde) uclulerini dondurur."""
    if code == "en":
        return [
            ("privacy.html", "Privacy policy", PRIVACY_EN),
            ("terms.html", "Terms of use", TERMS_EN),
            ("account-deletion.html", "Account deletion", DELETE_EN),
        ]
    return [
        ("privacy.html", "Gizlilik politikasi", PRIVACY_TR),
        ("terms.html", "Kullanim kosullari", TERMS_TR),
        ("account-deletion.html", "Hesap silme", DELETE_TR),
    ]
