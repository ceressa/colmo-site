# -*- coding: utf-8 -*-
"""Yasal sayfa metinleri.

Yalnizca Ingilizce ve Turkce tam yazildi; acilis sayfasi alti dilde ama
sozlesme dort dilde daha yarim cevrilmis olsa bunun kimseye faydasi olmazdi.
Diger dillerdeki altbilgi baglantilari Ingilizce surume gidiyor.

Turkce yasal metin okura "siz" diye hitap ediyor (14.10.2026 karari, uc oyun
sitesinde ayni). Tanitim sayfalari "sen" kalir.

Her cumle oyunun kodundan dogrulandi (colmo deposu, origin/main 14.10.2026):
  - giris: lib/cloud_sync.dart (anonim kimlik, Google, iOS'ta Apple)
  - uygulama ici silme: CloudSync.deleteAccount; bagli hesapta "Hesabi sil",
    sonraki surumde giris yapmamis oyuncuda "Buluttaki kaydi sil"
    (lib/ui/menu_pages.dart); onay metinleri lib/l10n/app_*.arb
    deleteAccountConfirm, deleteCloudSaveConfirm
  - satin alma: lib/billing.dart, tek urun com.bardino.colmo.remove_ads,
    docs/LAUNCH.md "remove_ads 1.0.0 ile onaylandi ve canli"
  - Firestore kurallari: firestore.rules (sahibi + salt okuma yonetim hesabi)
  - buluta giden alanlar: cloudPayload (lib/cloud_sync.dart); takma ad
    lib/nickname.dart, paylasim metni lib/daily_share.dart, kiler
    lib/kiler.dart, basarim ve tablolar lib/game_services.dart, olcum
    olaylari lib/telemetry.dart
  - Bardino: lib/bardino_api.dart (/acik tokensiz, /durum, /katil, /gunluk,
    /ad, /hediye-al, /cik) ve lib/bardino.dart (gizlilik kapisi). Merkezin
    sakladiklari burada tekrarlanmaz; bardino.app/uyelik/aydinlatma'ya
    baglanir.
Magazadaki surumde takma ad, gunun kavanozu, kiler, Bardino ve anonim silme
yok; sonraki surumde var. Bu ozellikler iki surum icin de dogru kalacak
bicimde, kosullu yazildi ("surumunuzde varsa", "yeni surumlerde").
Gizlilik metni uygulamadaki `docs/store/PRIVACY_POLICY.md` ile ayni gercegi
anlatmali. Orasi degisince burasi da degisir.
"""

MAIL = "info@bardino.app"
PKG = "com.bardino.colmo"


def _mail(subject=None):
    """E-posta baglantisi. Cloudflare'in adres gizlemesi JS'siz tarayicida
    /cdn-cgi/l/email-protection'a (404) cevirir; email_off onu durdurur."""
    href = "mailto:%s" % MAIL
    if subject:
        href += "?subject=" + subject.replace(" ", "%20")
    return ('<!--email_off--><a href="%s">%s</a><!--/email_off-->'
            % (href, MAIL))


def _p(*paras):
    return "".join("<p>%s</p>" % x for x in paras)


def _ul(*items):
    return "<ul>%s</ul>" % "".join("<li>%s</li>" % x for x in items)


def _ol(*items):
    return "<ol>%s</ol>" % "".join("<li>%s</li>" % x for x in items)


PRIVACY_EN = (
    "<h2>1. Overview</h2>"
    + _p("Colmo is a number puzzle. It can be played entirely offline, and "
         "signing in is never required. This page describes the small amount "
         "of data the game handles and why.")
    + "<h2>2. What we process</h2>"
    + _ul(
        "<strong>Game progress</strong> (levels cleared, stars, best endless "
        "score, coins and lives, which helper lessons you have seen and, in "
        "versions that have them, daily jar results and streak, how you "
        "arranged your pantry and jokers received as gifts): stored on your "
        "device. If the device is online, the same data is synced to Google "
        "Firebase under an anonymous identifier that the game creates on "
        "first launch, so it can be recovered on a new device. No e-mail or "
        "contact detail is part of that record; if your version has a "
        "nickname, that is the only name in it.",
        "<strong>Nickname</strong>: if your version of the game shows a "
        "nickname in Profile, it is a made-up name built from pantry words "
        "(for example &ldquo;Honeyed Jar 482&rdquo;) that you can change to "
        "anything you like. It is stored and synced with your game progress, "
        "so it follows you to a new device. It is never taken from your "
        "Google or Apple account, it is not shown to other players, and it "
        "is not sent to analytics or to the ad network. Apart from your save, "
        "it appears only in reminders on your device, in a daily jar result "
        "you choose to share, and, if you join Bardino membership, as your "
        "shared nickname (section 7).",
        "<strong>Sharing the daily jar</strong>: if you share a daily jar "
        "result, the game hands a short text to your device's share sheet: "
        "the date, your stars, the doses you used, your streak, your nickname "
        "and the game's web address. You choose where it goes; the game sends "
        "nothing on its own.",
        "<strong>Optional sign-in</strong>: if you choose Sign in with Google "
        "in Settings, or Sign in with Apple on iPhone and iPad, your anonymous "
        "save is linked to that account so it survives a change of device. "
        "We receive only the basic profile the provider gives for "
        "authentication: your e-mail address, or with Apple the relay address "
        "Apple provides if you choose to hide yours. If that account already "
        "has a Colmo save, your progress is merged into it, and newer "
        "versions of the game delete the anonymous copy at that moment. "
        "Signing in is never required to play.",
        "<strong>Purchase</strong>: the only item Colmo sells is "
        "<strong>Remove ads</strong>, a one-time purchase. The App Store or "
        "Google Play processes the payment; we do not receive your payment "
        "details. The game records on the device that ads are removed and "
        "can ask the store to restore the purchase.",
        "<strong>Achievements and leaderboards</strong> (Google Play Games on "
        "Android, Game Center on iPhone and iPad): if you are signed in to "
        "that service on your device, the game reports the achievements you "
        "unlock and your scores for two leaderboards, total stars and endless "
        "mode. Those services show leaderboards to other players under your "
        "profile there, not under a Colmo nickname.",
        "<strong>Settings</strong> (sound, music, language, haptics, "
        "reminders): stored on your device only.",
        "<strong>Gameplay measurement</strong> (Google Analytics for "
        "Firebase): the game records what happened, not who you are. Which "
        "level was started, won, lost or left, how many doses it took, which "
        "helper was used, whether a language was changed and, in versions "
        "that have them, whether the daily jar was played or shared (never "
        "what was shared) and the steps of Bardino membership (card seen, "
        "joined, gift claimed, left). Your e-mail address and nickname are "
        "never part of it. This exists to answer one question: where the game "
        "is too hard or unclear. Firebase's ad signals are switched off in "
        "code, so this measurement never feeds an advertising profile.",
        "<strong>Ads</strong> (Google AdMob): from level 11 onwards the game "
        "shows an occasional full-screen ad between levels, never after a "
        "loss. There is also an ad you may choose to watch to earn one life; "
        "it is always optional and nothing is taken if you skip it. To select "
        "and measure ads, Google receives the device's advertising ID and "
        "standard request data (approximate region, device type). In the EEA, "
        "the UK and Switzerland you are asked for consent before any of this "
        "happens, and your answer is stored on the device.",
        "<strong>Crash reports</strong> (Firebase Crashlytics): if the game "
        "crashes, the technical details of the crash are sent (device model, "
        "OS version, the point in the code that failed). A game that crashes "
        "silently is a game nobody reports.")
    + "<h2>3. What we do not do</h2>"
    + _ul("No banner ads, no ad on the loss screen, and no ad before "
          "level 11.",
          "No account, no name, no nickname and no e-mail is ever sent to "
          "the ad network.",
          "No location, no contacts, no photos, no microphone.",
          "We do not sell your data. Apart from the Google services listed "
          "above, the only other company involved is Apple, and only if you "
          "sign in with Apple, use Game Center or buy on the App Store.")
    + "<h2>4. Where the data lives</h2>"
    + _p("Cloud saves are stored in Google Firebase (Firestore) in the "
         "project <strong>colmo-bardino</strong>. Access rules restrict every "
         "record to the account that owns it; the only other access is "
         "read-only access for Bardino's own administration account. "
         "Firebase's own processing is covered by Google's privacy "
         "documentation.")
    + "<h2>5. Deletion</h2>"
    + _p("Uninstalling the app removes the data stored on the device; it does "
         "not delete the cloud save. You can delete the cloud save in the "
         "game, under <strong>Menu &rarr; Settings</strong>: <strong>Delete "
         "account</strong> if you have signed in, which also deletes your "
         "sign-in record, or, in newer versions of the game, <strong>Delete "
         "cloud save</strong> if you never signed in, which also deletes the "
         "anonymous identifier the save was kept under. The other routes, and "
         "what is kept afterwards, are described on the "
         "<a href=\"/account-deletion.html\">Account deletion</a> page.")
    + "<h2>6. Children</h2>"
    + _p("Colmo contains no chat, and the game never shows anything a player "
         "writes to other players. It is not directed at children and does "
         "not knowingly collect personal data from them; the only optional "
         "personal data in the product are the e-mail address of the Google "
         "or Apple account used for sign-in and, in versions that have one, "
         "a nickname the player chooses to type. Bardino membership is only "
         "for players aged 13 or over. The game does show ads, so it is rated "
         "for a general audience rather than declared a children's app.")
    + "<h2>7. Bardino membership (optional)</h2>"
    + _p("Colmo, Decimo and Palmo are made by the same developer. Bardino "
         "membership is a free, optional way to use one account across them: "
         "one nickname, a daily streak shared by the three games, and small "
         "gifts. It needs a Google or Apple sign-in and is only for players "
         "aged 13 or over. What the membership service stores, how long it "
         "keeps it and how to use your rights are set out in its own "
         "<a href=\"https://bardino.app/uyelik/aydinlatma#en\">privacy "
         "notice</a>. If your version of Colmo offers the membership, this is "
         "what the game itself sends to it:")
    + _ul("<strong>Before you join</strong>: the game asks whether membership "
          "is open, without any identity. Only if it is open (or you have "
          "already joined from this device) and you are signed in with Google "
          "or Apple does the game also ask whether your account is a member, "
          "to show the right card; that request carries your sign-in token, "
          "which includes your e-mail address. Unless you join, nothing about "
          "you is stored apart from the technical logs described in the "
          "notice.",
          "<strong>If you join</strong>: your consent with the 13+ "
          "confirmation and, for a new membership, your Colmo nickname. After "
          "that, the date of each daily jar you win, nickname changes and the "
          "gifts you claim. Gifts arrive in your Colmo save as coins and "
          "jokers.",
          "<strong>Leaving</strong>: <strong>Leave Bardino "
          "membership</strong> in Settings ends the membership in one step, "
          "for all three games. Signing out of Colmo or deleting your Colmo "
          "account removes the membership's traces from the device but does "
          "not end the membership.")
    + "<h2>8. Changes</h2>"
    + _p("Material changes to this policy will be reflected here with a new "
         "date.")
    + "<h2>9. Contact</h2>"
    + _p(_mail()))

PRIVACY_TR = (
    "<h2>1. Genel bakış</h2>"
    + _p("Colmo bir sayı bulmacasıdır. Tamamen çevrimdışı oynanabilir ve "
         "giriş yapmanız hiçbir zaman gerekmez. Bu sayfa, oyunun işlediği az "
         "miktardaki veriyi ve nedenini açıklar.")
    + "<h2>2. İşlenen veriler</h2>"
    + _ul(
        "<strong>Oyun ilerlemesi</strong> (geçilen bölümler, yıldızlar, "
        "sonsuz mod rekoru, coin ve canlar, gördüğünüz joker dersleri ve, "
        "sürümünüzde varsa, günün kavanozu sonuçları ve seriniz, kilerinizi "
        "nasıl dizdiğiniz ve hediye olarak gelen jokerler): cihazınızda "
        "saklanır. Cihaz çevrimiçiyse aynı veri, yeni bir cihazda "
        "kurtarılabilmesi için oyunun ilk açılışta oluşturduğu anonim bir "
        "kimlik altında Google Firebase'e eşitlenir. Bu kayıtta e-posta veya "
        "iletişim bilgisi bulunmaz; sürümünüzde takma ad varsa, içindeki tek "
        "ad odur.",
        "<strong>Takma ad</strong>: oyununuzun sürümü Profil'de bir takma ad "
        "gösteriyorsa bu, kiler sözcüklerinden uydurulmuş ve dilediğiniz gibi "
        "değiştirebileceğiniz bir addır (örneğin &ldquo;Ballı Kavanoz "
        "482&rdquo;). Yeni bir cihazda da sizinle gelsin diye oyun "
        "ilerlemesiyle birlikte saklanır ve eşitlenir. Google ya da Apple "
        "hesabınızdan asla alınmaz, başka oyunculara gösterilmez, ölçüme ve "
        "reklam ağına gönderilmez. Kaydınız dışında yalnızca cihazınızdaki "
        "hatırlatmalarda, paylaşmayı seçtiğiniz günün kavanozu sonucunda ve "
        "Bardino üyeliğine katılırsanız ortak takma adınız olarak (7. bölüm) "
        "görünür.",
        "<strong>Günün kavanozunu paylaşma</strong>: günün kavanozu sonucunu "
        "paylaşırsanız oyun, cihazınızın paylaşım ekranına kısa bir metin "
        "verir: tarih, yıldızlarınız, harcadığınız doz, seriniz, takma adınız "
        "ve oyunun web adresi. Nereye gideceğini siz seçersiniz; oyun "
        "kendiliğinden hiçbir şey göndermez.",
        "<strong>İsteğe bağlı giriş</strong>: Ayarlar'dan Google ile ya da "
        "iPhone ve iPad'de Apple ile giriş yapmayı seçerseniz anonim kaydınız "
        "o hesaba bağlanır ve cihaz değiştirdiğinizde de korunur. Sağlayıcının "
        "kimlik doğrulama için verdiği temel bilgi dışında bir şey almayız: "
        "e-posta adresiniz ya da, Apple'da adresinizi gizlemeyi seçerseniz, "
        "Apple'ın verdiği aktarma adresi. O hesabın zaten bir Colmo kaydı "
        "varsa ilerlemeniz onunla birleştirilir; oyunun yeni sürümleri anonim "
        "kopyayı o anda siler. Oynamak için giriş yapmanız hiçbir zaman "
        "gerekmez.",
        "<strong>Satın alma</strong>: Colmo'da satılan tek ürün, bir kerelik "
        "bir satın alma olan <strong>Reklamları kaldır</strong> seçeneğidir. "
        "Ödemeyi App Store ya da Google Play işler; ödeme bilgileriniz bize "
        "ulaşmaz. Oyun, reklamların kaldırıldığını cihazda kaydeder ve satın "
        "almayı mağazadan geri yükleyebilir.",
        "<strong>Başarımlar ve liderlik tabloları</strong> (Android'de Google "
        "Play Games, iPhone ve iPad'de Game Center): cihazınızda o hizmete "
        "giriş yaptıysanız oyun, açtığınız başarımları ve iki liderlik tablosu "
        "için skorlarınızı (toplam yıldız ve sonsuz mod) bildirir. Bu "
        "hizmetler liderlik tablolarını diğer oyunculara bir Colmo takma "
        "adıyla değil, oradaki profilinizle gösterir.",
        "<strong>Ayarlar</strong> (ses, müzik, dil, titreşim, "
        "hatırlatmalar): yalnızca cihazınızda saklanır.",
        "<strong>Oynanış ölçümü</strong> (Google Analytics for Firebase): "
        "oyun kim olduğunuzu değil, ne olduğunu kaydeder: hangi bölümün "
        "başlatıldığı, kazanıldığı, kaybedildiği ya da bırakıldığı; kaç doz "
        "harcandığı; hangi jokerin kullanıldığı; dilin değiştirilip "
        "değiştirilmediği ve, sürümünüzde varsa, günün kavanozunun oynanıp "
        "oynanmadığı ya da paylaşılıp paylaşılmadığı (paylaşılan metin değil) "
        "ile Bardino üyeliğinin adımları (kartın görülmesi, katılma, hediye "
        "alma, ayrılma). E-posta adresiniz ve takma adınız bu ölçüme hiçbir "
        "zaman girmez. Bu ölçüm tek bir soruyu yanıtlamak için vardır: oyun "
        "nerede fazla zor ya da anlaşılmaz. Firebase'in reklam sinyalleri kod "
        "içinde kapalıdır; bu ölçüm hiçbir zaman bir reklam profiline "
        "dönüşmez.",
        "<strong>Reklamlar</strong> (Google AdMob): 11. bölümden itibaren "
        "bölüm aralarında ara sıra tam ekran reklam gösterilir; kaybedilen "
        "bir bölümün ardından asla gösterilmez. Ayrıca, izlemeyi kendiniz "
        "seçerseniz bir can kazandıran bir reklam vardır; izlemezseniz hiçbir "
        "şey eksilmez. Reklamı seçmek ve ölçmek için Google, cihazın reklam "
        "kimliğini ve standart istek verisini (yaklaşık bölge, cihaz tipi) "
        "alır. AEA, Birleşik Krallık ve İsviçre'de bunların hiçbiri olmadan "
        "önce rızanız sorulur ve yanıtınız cihazda saklanır.",
        "<strong>Çökme raporları</strong> (Firebase Crashlytics): oyun "
        "çökerse çökmenin teknik ayrıntıları gönderilir (cihaz modeli, "
        "işletim sistemi sürümü, kodun hangi noktada hata verdiği). Sessizce "
        "çöken bir oyunu kimse bildirmez.")
    + "<h2>3. Yapmadıklarımız</h2>"
    + _ul("Banner reklam yok, kaybedilen bölümün ardından reklam yok, 11. "
          "bölümden önce reklam yok.",
          "Reklam ağına hesap, isim, takma ad veya e-posta gönderilmez.",
          "Konum, rehber, fotoğraf ve mikrofon kullanılmaz.",
          "Verinizi satmıyoruz. Yukarıda sayılan Google hizmetleri dışında "
          "işin içinde olan tek şirket Apple'dır; o da yalnızca Apple ile "
          "giriş yaparsanız, Game Center kullanırsanız ya da App Store'dan "
          "satın alırsanız.")
    + "<h2>4. Verinin tutulduğu yer</h2>"
    + _p("Bulut kayıtları Google Firebase (Firestore) üzerinde "
         "<strong>colmo-bardino</strong> projesinde tutulur. Erişim "
         "kuralları her kaydı yalnızca sahibi olan hesapla sınırlar; bunun "
         "dışındaki tek erişim, Bardino'nun kendi yönetim hesabının salt "
         "okuma erişimidir. Firebase'in kendi işleme süreçleri Google'ın "
         "gizlilik belgelerine tabidir.")
    + "<h2>5. Silme</h2>"
    + _p("Uygulamayı kaldırmak cihazda saklanan veriyi siler; bulut kaydını "
         "silmez. Bulut kaydınızı oyunun içinden, <strong>Menü &rarr; "
         "Ayarlar</strong> altında silebilirsiniz: giriş yaptıysanız "
         "<strong>Hesabı sil</strong> ile (giriş kaydınız da silinir), hiç "
         "giriş yapmadıysanız oyunun yeni sürümlerinde <strong>Buluttaki "
         "kaydı sil</strong> ile (kaydın tutulduğu anonim kimlik de silinir). "
         "Diğer yollar ve sonrasında neyin kaldığı "
         "<a href=\"/tr/account-deletion.html\">Hesap silme</a> sayfasında "
         "anlatılır.")
    + "<h2>6. Çocuklar</h2>"
    + _p("Colmo'da sohbet yoktur ve oyun, bir oyuncunun yazdığı hiçbir şeyi "
         "başka oyunculara göstermez. Uygulama çocuklara yönelik değildir ve "
         "çocuklardan bilerek kişisel veri toplamaz; üründeki isteğe bağlı "
         "kişisel veriler, giriş için kullanılan Google ya da Apple hesabının "
         "e-posta adresi ve, sürümünüzde varsa, oyuncunun kendi yazmayı "
         "seçtiği takma addır. Bardino üyeliği yalnızca 13 yaş ve "
         "üstündekiler içindir. Oyunda reklam gösterildiği için genel kitleye "
         "uygun olarak derecelendirilmiştir, çocuk uygulaması olarak beyan "
         "edilmemiştir.")
    + "<h2>7. Bardino üyeliği (isteğe bağlı)</h2>"
    + _p("Colmo, Decimo ve Palmo aynı geliştiricinin oyunlarıdır. Bardino "
         "üyeliği, üçünde tek hesap kullanmanın ücretsiz ve isteğe bağlı "
         "yoludur: tek takma ad, üç oyunun ortak günlük serisi ve küçük "
         "hediyeler. Google ya da Apple girişi gerektirir ve yalnızca 13 yaş "
         "ve üstündekiler içindir. Üyelik hizmetinin neyi sakladığı, ne kadar "
         "süre tuttuğu ve haklarınızı nasıl kullanabileceğiniz kendi "
         "<a href=\"https://bardino.app/uyelik/aydinlatma\">aydınlatma "
         "metninde</a> yazılıdır. Colmo sürümünüz üyeliği sunuyorsa oyunun "
         "kendisinin bu hizmete gönderdikleri şunlardır:")
    + _ul("<strong>Katılmadan önce</strong>: oyun, üyeliğin açık olup "
          "olmadığını hiçbir kimlik eklemeden sorar. Yalnızca üyelik açıksa "
          "(ya da bu cihazdan zaten katıldıysanız) ve Google ya da Apple ile "
          "giriş yaptıysanız, doğru kartı gösterebilmek için hesabınızın üye "
          "olup olmadığını da sorar; bu istek, e-posta adresinizi içeren "
          "giriş jetonunu taşır. Katılmadığınız sürece, aydınlatma metninde "
          "anlatılan teknik kayıtlar dışında sizinle ilgili hiçbir şey "
          "saklanmaz.",
          "<strong>Katılırsanız</strong>: onayınız ve 13 yaş beyanınız, yeni "
          "bir üyelikte ise Colmo takma adınız. Sonrasında kazandığınız her "
          "günün kavanozunun tarihi, takma ad değişiklikleriniz ve aldığınız "
          "hediyeler. Hediyeler Colmo kaydınıza coin ve joker olarak gelir.",
          "<strong>Ayrılma</strong>: Ayarlar'daki <strong>Bardino "
          "üyeliğinden çık</strong> satırı üyeliği tek adımda, üç oyun için "
          "birden sonlandırır. Colmo'dan çıkış yapmak ya da Colmo hesabınızı "
          "silmek üyeliğin cihazdaki izlerini siler, ama üyeliği "
          "sonlandırmaz.")
    + "<h2>8. Değişiklikler</h2>"
    + _p("Bu politikadaki önemli değişiklikler yeni bir tarihle burada "
         "yayımlanır.")
    + "<h2>9. İletişim</h2>"
    + _p(_mail()))

TERMS_EN = (
    "<h2>1. Summary</h2>"
    + "<div class=\"vurgu\">"
    + _p("Colmo is free to download and play. It sells one optional item: "
         "<strong>Remove ads</strong>, a one-time purchase. You may play the "
         "game on your own devices; you may not copy, modify or resell it.")
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
    + "<h2>4. Purchases</h2>"
    + _p("<strong>Remove ads</strong> is a one-time purchase that turns off "
         "all ads in the game, including the optional ad that earns a life. "
         "It is processed by the App Store or Google Play, whose terms govern "
         "payment and refunds; refund requests go to the store you bought "
         "from. The purchase belongs to your store account, not to a Colmo "
         "account: deleting your Colmo account does not cancel it, and "
         "<strong>Restore purchases</strong> in Settings brings it back on a "
         "new device or after reinstalling.",
         "Coins are earned by playing. They cannot be bought, have no cash "
         "value and cannot be exchanged for money.")
    + "<h2>5. Your saved progress</h2>"
    + _p("Cloud saving is a convenience, not a guarantee. We take reasonable "
         "care, but a lost save is not a compensable loss. Linking a Google "
         "or Apple account makes a save far more durable and is the best "
         "protection available.")
    + "<h2>6. Availability and changes</h2>"
    + _p("The game may change. Levels can be rebalanced, features added or "
         "removed, and the service behind cloud saving can be discontinued "
         "with reasonable notice. Nothing here promises that a specific "
         "feature will exist forever.")
    + "<h2>7. No warranty</h2>"
    + _p("Colmo is provided as is. To the extent permitted by law, we make no "
         "warranty that it will be uninterrupted or error free, and we are "
         "not liable for indirect or consequential loss arising from its "
         "use.")
    + "<h2>8. Governing law</h2>"
    + _p("These terms are governed by the laws of the Republic of Türkiye. "
         "Nothing in them limits the consumer rights you have under the law "
         "of the country you live in.")
    + "<h2>9. Contact</h2>"
    + _p(_mail()))

TERMS_TR = (
    "<h2>1. Özet</h2>"
    + "<div class=\"vurgu\">"
    + _p("Colmo ücretsiz indirilir ve oynanır. Satılan tek ürün isteğe "
         "bağlıdır: bir kerelik bir satın alma olan <strong>Reklamları "
         "kaldır</strong>. Oyunu kendi cihazlarınızda oynayabilirsiniz; "
         "kopyalayamaz, değiştiremez ve yeniden satamazsınız.")
    + "</div>"
    + "<h2>2. Lisans</h2>"
    + _p("Bardino Technology, Colmo'yu kendi kontrolünüzdeki cihazlara kurup "
         "oynamanız için size kişisel, münhasır olmayan ve devredilemez bir "
         "lisans verir. Oyun, görselleri, bölümleri, sesleri ve kodu bize "
         "aittir.")
    + "<h2>3. Yapmamayı kabul ettikleriniz</h2>"
    + _ul("Kanunen hariç tutulamayan haller dışında, uygulamaya tersine "
          "mühendislik uygulamak, onu kaynak koda çevirmek ya da "
          "değiştirmek.",
          "Uygulamayı ya da varlıklarını yeniden dağıtmak veya başka bir "
          "adla yayımlamak.",
          "Bulut kayıt hizmetine müdahale etmek ya da onu kendi oyun "
          "ilerlemeniz dışında bir şey saklamak için kullanmak.")
    + "<h2>4. Satın almalar</h2>"
    + _p("<strong>Reklamları kaldır</strong>, can kazandıran isteğe bağlı "
         "reklam dahil oyundaki bütün reklamları kapatan bir kerelik bir "
         "satın almadır. Satın almayı App Store ya da Google Play işler; "
         "ödeme ve iade onların koşullarına tabidir ve iade talepleri satın "
         "aldığınız mağazaya yapılır. Satın alma bir Colmo hesabına değil, "
         "mağaza hesabınıza aittir: Colmo hesabınızı silmeniz onu iptal "
         "etmez; Ayarlar'daki <strong>Satın alımları geri yükle</strong> "
         "satırı onu yeni bir cihazda ya da oyunu yeniden kurduğunuzda geri "
         "getirir.",
         "Coinler oynayarak kazanılır. Parayla satın alınamaz, nakit değeri "
         "yoktur ve paraya çevrilemez.")
    + "<h2>5. Kayıtlı ilerlemeniz</h2>"
    + _p("Bulut kaydı bir kolaylıktır, garanti değildir. Makul özeni "
         "gösteriyoruz, ancak kaybolan bir kayıt tazmin edilebilir bir zarar "
         "değildir. Bir Google ya da Apple hesabı bağlamak kaydı çok daha "
         "dayanıklı kılar ve mevcut en iyi korumadır.")
    + "<h2>6. Süreklilik ve değişiklikler</h2>"
    + _p("Oyun değişebilir. Bölümler yeniden dengelenebilir, özellikler "
         "eklenebilir ya da kaldırılabilir ve bulut kaydının dayandığı hizmet "
         "makul bir bildirimle sonlandırılabilir. Burada hiçbir özelliğin "
         "süresiz olarak var olacağı vaat edilmez.")
    + "<h2>7. Garanti yoktur</h2>"
    + _p("Colmo olduğu gibi sunulur. Kanunun izin verdiği ölçüde, kesintisiz "
         "ya da hatasız çalışacağına dair bir garanti vermiyoruz ve "
         "kullanımından doğan dolaylı zararlardan sorumlu değiliz.")
    + "<h2>8. Uygulanacak hukuk</h2>"
    + _p("Bu koşullar Türkiye Cumhuriyeti kanunlarına tabidir. Bu "
         "koşullardaki hiçbir hüküm, yaşadığınız ülkenin kanunlarından doğan "
         "tüketici haklarınızı sınırlamaz.")
    + "<h2>9. İletişim</h2>"
    + _p(_mail()))

DELETE_EN = (
    "<h2>How accounts work in Colmo</h2>"
    + "<div class=\"vurgu\">"
    + _p("On first launch the game creates an anonymous identifier, without "
         "asking you for anything, and stores your cloud save under it. "
         "Signing in is optional: in Settings you can link the save to a "
         "<strong>Google</strong> account, or on iPhone and iPad to an "
         "<strong>Apple</strong> account, so that it can be restored on "
         "another device.")
    + "</div>"
    + "<h2>1. Delete your account in the game</h2>"
    + _p("This option is shown once you have signed in with Google or Apple.")
    + _ol("Open <strong>Menu</strong> &rarr; <strong>Settings</strong>.",
          "Tap <strong>Delete account</strong>.",
          "The confirmation reads <em>Your account and its cloud save are "
          "deleted. Progress on this device stays.</em> Tap <strong>Delete "
          "account</strong> again to confirm.")
    + _p("The game deletes your cloud save and then your sign-in record. If "
         "your last sign-in was not recent, it asks you to sign in once more "
         "first. Progress on this device is kept, and the game continues "
         "under a new anonymous identifier, as it does for every player who "
         "has not signed in.")
    + "<h2>2. If you never signed in</h2>"
    + _p("Newer versions of the game show a delete option to players who "
         "never signed in as well:")
    + _ol("Open <strong>Menu</strong> &rarr; <strong>Settings</strong>.",
          "Tap <strong>Delete cloud save</strong>.",
          "The confirmation reads <em>Your cloud save and its anonymous ID "
          "are deleted. Progress on this device stays; if you keep playing, "
          "it is backed up again under a new ID.</em> Tap <strong>Delete "
          "cloud save</strong> again to confirm.")
    + _p("The game deletes your cloud save and then the anonymous identifier "
         "it was kept under. If your version does not show this option, you "
         "can sign in with Google, or with Apple on iPhone and iPad, and then "
         "delete the account as in step 1. A save that was never linked "
         "contains no e-mail address, so we cannot locate it from a "
         "message.")
    + "<h2>3. Reset progress on this device</h2>"
    + _ol("Open <strong>Menu</strong> &rarr; <strong>Settings</strong>.",
          "Tap <strong>Reset progress</strong>.",
          "The confirmation reads <em>Every level, star and record will be "
          "erased. This cannot be undone.</em> Tap <strong>Reset "
          "progress</strong> again to confirm.")
    + _p("This erases levels, stars, records and coins on the device and "
         "keeps your sound and language settings. It is not a way to delete "
         "your cloud save; use step 1 or 2 for that.")
    + "<h2>4. By e-mail</h2>"
    + _p("If you can no longer open the game, for example because you no "
         "longer have the device, write to %s with the subject "
         "<strong>Colmo account deletion</strong>, from the e-mail address of "
         "the Google or Apple account you linked. This lets us verify the "
         "request. We process requests within 30 days."
         % _mail("Colmo account deletion"),
         "A save that was never linked to an account cannot be identified "
         "from an e-mail.")
    + "<h2>What is deleted</h2>"
    + _p("Your cloud save, with everything listed under Game progress in the "
         "<a href=\"/privacy.html\">privacy policy</a>, and the sign-in "
         "record that links it to your Google or Apple account, or for a "
         "save that was never linked, the anonymous identifier. No backup "
         "copy is kept.")
    + "<h2>What is not deleted</h2>"
    + _ul("<strong>Progress on this device</strong>: it stays until you reset "
          "it (step 3) or uninstall the app.",
          "<strong>Bardino membership</strong>, if you joined it: it is "
          "ended separately with <strong>Leave Bardino membership</strong> "
          "in Settings, as described in its "
          "<a href=\"https://bardino.app/uyelik/aydinlatma#en\">privacy "
          "notice</a>.",
          "<strong>The Remove ads purchase</strong>: it belongs to your App "
          "Store or Google Play account, not to your Colmo account. Deleting "
          "the account does not cancel it, and <strong>Restore "
          "purchases</strong> in Settings brings it back.",
          "<strong>Crash reports and gameplay measurement</strong>: these are "
          "not tied to your identity and cannot be located per person; they "
          "contain no name, no e-mail address and no advertising ID.",
          "<strong>E-mail correspondence</strong>: anything you sent us by "
          "e-mail stays in our mailbox unless you ask us to delete it as "
          "well.")
    + "<h2>Uninstalling</h2>"
    + _p("Uninstalling removes everything stored on the device, including the "
         "anonymous identifier. It does not delete the cloud save, so delete "
         "it first: step 1 if you have signed in, step 2 if you have not. A "
         "save left behind stays on our servers without any e-mail address, "
         "and afterwards neither the app nor we can match it to you.")
    + "<h2>Contact</h2>"
    + _p("%s &middot; %s" % (_mail(), PKG)))

DELETE_TR = (
    "<h2>Colmo'da hesap nasıl işler</h2>"
    + "<div class=\"vurgu\">"
    + _p("Oyun ilk açılışta, sizden hiçbir şey istemeden anonim bir kimlik "
         "oluşturur ve bulut kaydınızı bu kimlik altında saklar. Giriş yapmak "
         "isteğe bağlıdır: Ayarlar'dan kaydınızı bir <strong>Google</strong> "
         "hesabına ya da iPhone ve iPad'de bir <strong>Apple</strong> "
         "hesabına bağlayabilir, böylece başka bir cihazda geri "
         "yükleyebilirsiniz.")
    + "</div>"
    + "<h2>1. Hesabınızı oyunun içinden silin</h2>"
    + _p("Bu seçenek, Google ya da Apple ile giriş yaptıktan sonra görünür.")
    + _ol("<strong>Menü</strong> &rarr; <strong>Ayarlar</strong>'ı açın.",
          "<strong>Hesabı sil</strong> satırına dokunun.",
          "Onay penceresinde şu yazar: <em>Hesabın ve buluttaki kaydın "
          "silinir. Bu cihazdaki ilerleme kalır.</em> Onaylamak için yeniden "
          "<strong>Hesabı sil</strong>'e dokunun.")
    + _p("Oyun önce bulut kaydınızı, ardından giriş kaydınızı siler. Son "
         "girişiniz yeni değilse silmeden önce bir kez daha giriş yapmanız "
         "istenir. Bu cihazdaki ilerlemeniz korunur ve oyun, giriş yapmamış "
         "her oyuncuda olduğu gibi yeni bir anonim kimlikle devam eder.")
    + "<h2>2. Hiç giriş yapmadıysanız</h2>"
    + _p("Oyunun yeni sürümleri, hiç giriş yapmamış oyunculara da bir silme "
         "seçeneği gösterir:")
    + _ol("<strong>Menü</strong> &rarr; <strong>Ayarlar</strong>'ı açın.",
          "<strong>Buluttaki kaydı sil</strong> satırına dokunun.",
          "Onay penceresinde şu yazar: <em>Buluttaki kaydın ve anonim "
          "kimliğin silinir. Bu cihazdaki ilerleme kalır; oynamaya devam "
          "edersen yeni bir kimlikle yeniden yedeklenir.</em> Onaylamak için "
          "yeniden <strong>Buluttaki kaydı sil</strong>'e dokunun.")
    + _p("Oyun önce bulut kaydınızı, ardından onun tutulduğu anonim kimliği "
         "siler. Sürümünüz bu seçeneği göstermiyorsa Ayarlar'dan Google ile "
         "ya da iPhone ve iPad'de Apple ile giriş yapıp ardından 1. adımdaki "
         "gibi hesabı silebilirsiniz. Hiçbir hesaba bağlanmamış bir kayıt "
         "e-posta adresi içermez; bu nedenle onu bir e-postadan bulamayız.")
    + "<h2>3. Bu cihazdaki ilerlemeyi sıfırlayın</h2>"
    + _ol("<strong>Menü</strong> &rarr; <strong>Ayarlar</strong>'ı açın.",
          "<strong>İlerlemeyi sıfırla</strong> satırına dokunun.",
          "Onay penceresinde şu yazar: <em>Bütün bölümler, yıldızlar ve "
          "rekorlar silinecek. Bu geri alınamaz.</em> Onaylamak için yeniden "
          "<strong>İlerlemeyi sıfırla</strong>'ya dokunun.")
    + _p("Bu işlem cihazdaki bölümleri, yıldızları, rekorları ve coinleri "
         "siler; ses ve dil ayarlarınız kalır. Bulut kaydınızı silmenin yolu "
         "bu değildir; bunun için 1. ya da 2. adımı kullanın.")
    + "<h2>4. E-postayla</h2>"
    + _p("Oyunu artık açamıyorsanız, örneğin cihaz artık elinizde değilse, "
         "bağladığınız Google ya da Apple hesabının e-posta adresinden %s "
         "adresine <strong>Colmo hesap silme</strong> konusuyla yazın. "
         "Talebinizi bu şekilde doğrularız. Talepleri 30 gün içinde işleme "
         "alırız." % _mail("Colmo hesap silme"),
         "Hiçbir hesaba bağlanmamış bir kayıt e-postadan tanımlanamaz.")
    + "<h2>Neler silinir</h2>"
    + _p("Bulut kaydınız (<a href=\"/tr/privacy.html\">gizlilik "
         "politikasında</a> Oyun ilerlemesi başlığı altında sayılan her şey) "
         "ve onu Google ya da Apple hesabınıza bağlayan giriş kaydı; hiçbir "
         "hesaba bağlanmamış bir kayıtta ise anonim kimlik. Sonrasında yedek "
         "bir kopya tutulmaz.")
    + "<h2>Neler silinmez</h2>"
    + _ul("<strong>Bu cihazdaki ilerleme</strong>: siz sıfırlayana (3. adım) "
          "ya da uygulamayı kaldırana kadar kalır.",
          "<strong>Bardino üyeliği</strong>, katıldıysanız: Ayarlar'daki "
          "<strong>Bardino üyeliğinden çık</strong> satırıyla ayrıca "
          "sonlandırılır; ayrıntılar "
          "<a href=\"https://bardino.app/uyelik/aydinlatma\">aydınlatma "
          "metnindedir</a>.",
          "<strong>Reklamları kaldır satın alması</strong>: Colmo hesabınıza "
          "değil, App Store ya da Google Play hesabınıza aittir. Hesabı "
          "silmek satın almayı iptal etmez; Ayarlar'daki <strong>Satın "
          "alımları geri yükle</strong> satırı onu geri getirir.",
          "<strong>Çökme raporları ve oynanış ölçümü</strong>: kimliğinize "
          "bağlı değildir ve kişi bazında bulunamaz; içlerinde isim, e-posta "
          "adresi ve reklam kimliği yoktur.",
          "<strong>E-posta yazışmaları</strong>: bize e-postayla "
          "gönderdikleriniz, silmemizi istemediğiniz sürece posta kutumuzda "
          "kalır.")
    + "<h2>Uygulamayı kaldırmak</h2>"
    + _p("Uygulamayı kaldırmak, anonim kimlik dahil cihazda saklanan her şeyi "
         "siler; bulut kaydını silmez. Bu yüzden önce onu silin: giriş "
         "yaptıysanız 1. adım, yapmadıysanız 2. adım. Geride kalan bir kayıt, "
         "hiçbir e-posta adresi olmadan sunucularımızda kalır ve sonrasında "
         "ne uygulama ne de biz onu sizinle eşleştirebiliriz.")
    + "<h2>İletişim</h2>"
    + _p("%s &middot; %s" % (_mail(), PKG)))


# (dosya, baslik, meta aciklama, tarih, govde). Meta aciklama sayfa basina:
# eskiden dort sayfa da acilis sayfasinin oyun tanitimini tasiyordu. Tarih
# metnin ozu degistiginde degisir; 14.10.2026'da uc metin de degisti (satin
# alma, Apple girisi, uygulama ici silme, yonetim hesabinin okuma erisimi),
# ayni gun gizlilik ve silme metni bir kez daha (takma ad, paylasim, kiler,
# Bardino uyeligi, Play Games ve Game Center, anonim silme).
_PAGES = {
    "en": [
        ("privacy.html", "Privacy policy",
         "What Colmo stores on your device, what it syncs to the cloud save, "
         "what it measures and what the ad network receives.",
         "2026-10-14", PRIVACY_EN),
        ("terms.html", "Terms of use",
         "The licence to play Colmo, the one optional purchase (Remove ads), "
         "cloud saves and the law that applies.",
         "2026-10-14", TERMS_EN),
        ("account-deletion.html", "Account deletion",
         "How to delete your Colmo account and cloud save in the game or by "
         "e-mail, and what is kept afterwards.",
         "2026-10-14", DELETE_EN),
    ],
    "tr": [
        ("privacy.html", "Gizlilik politikası",
         "Colmo'nun cihazınızda neyi sakladığı, bulut kaydına neyi eşitlediği, "
         "neyi ölçtüğü ve reklam ağının neyi aldığı.",
         "2026-10-14", PRIVACY_TR),
        ("terms.html", "Kullanım koşulları",
         "Colmo'yu oynama lisansı, isteğe bağlı tek satın alma (Reklamları "
         "kaldır), bulut kaydı ve uygulanacak hukuk.",
         "2026-10-14", TERMS_TR),
        ("account-deletion.html", "Hesap silme",
         "Colmo hesabınızı ve bulut kaydınızı oyunun içinden ya da e-postayla "
         "nasıl sildirebileceğiniz ve sonrasında neyin kaldığı.",
         "2026-10-14", DELETE_TR),
    ],
}


def pages(code):
    """(dosya, baslik, meta aciklama, tarih, govde) beslilerini dondurur."""
    return _PAGES[code]
