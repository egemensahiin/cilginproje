#!/usr/bin/env python3.7

import npyscreen
import random
import os

class OldurmeUygulamasi(npyscreen.NPSAppManaged):
    def main(self):
        wid, hei = os.get_terminal_size()[0:2]
        oynat = 'E'
        while oynat == 'E':
            with open("logo.txt", "r") as logomuz:
                logoStr = logomuz.read()

            self.mesaj_taslak(f"{logoStr}\
                              \n\nTum haklari Linus Torvalds tarafindan guvenceye alinmistir.\
                              \nYapimci Egemens Games\
                              \nKurgu: Gokhan Egemen Karaca\
                              \nCode Development: Egemen Sahin\
                              \nCok sevdigimiz arkadaslarimiza hitafen :)) Onlar kendini biliyor...", relx = int(wid / 2 - 45), rely = int(hei / 2 - 19))
            self.mesaj_taslak("\nOyun içinde seçenekler arasında dolaşmak için yukarı aşağı ok tuşlarını kullanın.\
                               \nİstediğiniz seçeneği seçmek için Boşluk veya Entera basınız.\
                               \nHikayeye devam etmek için Tab+Entera basınız.\n\
                               \nUYARI!! Bu oyun olabildiğince gore, cinsellik, şiddet ve Anıl Aksu'nun saçlarını içermektedir.\
                               \n18 yaşından küçüklerin oynaması tavsiye edilmez. Ama oynarlarsa da yapabileceğimiz bir şey yok.", relx = int(wid / 2 - 47), rely = int(hei / 2 - 3))
            baslasin_mi = self.secenek_taslak(["Oyunu Baslat!",
                                               "Oyundan Cik...",
                                               "Multiplayer (Cok Yakinda!!!)"])

            if baslasin_mi == 0:
                self.oyunun_kendisi()
            elif baslasin_mi == 1:
                oynat = "H"

    def oyunun_kendisi(self):
        self.mesaj_taslak("\nUzandigin yerden yavasca kalkiyorsun...\
                           \nIcınde bulundugun oda karanlik ve nerede olduguna dair hicbir fikrin yok....\
                           \nGozlerin karanlıga yavasca alistiktan sonra, duvardaki isik anahtarini, masadaki silahi ve kapi kolunu goruyorsun...")

        appFormu2 = npyscreen.Form(name = "Olum odasina hosgeldin!!")
        aciklama2 = appFormu2.add(npyscreen.FixedText,
                                  value="\nNe yapmak istersin?..")
        secenekler = appFormu2.add(npyscreen.TitleSelectOne, max_height = 5, value = [0,], name = "Seceneklerin sunlar: ",
                                   values = ["Isik anahtarina gidip isigi ac.",
                                             "Ayaga kalkip masadaki silahi aliyorsun.",
                                             "Kapiyi acmaya calisiyorsun."])
        appFormu2.edit()

        sectigimiz = secenekler.value[0]
        # ilk secimin sonucu. secenekler: 
        # Anahtari ac = 0
        # Silahi al = 1
        # Kapiyi acamaya calis = 2

        if sectigimiz == 0:
        # Eger anahtari acmayi sectiysek:
            self.mesaj_taslak("\nZorla yerinden kalkıp anahtara ulasiyorsun.\
                               \nAnahtari actiginda oda kuvvetli bir beyaz isikla doluyor.\
                               \nIcınde bulundugun odanın duvarinda bir cam goruyorsun ve camin arkasinda sandalyeye bagli uc kisi...\
                               \nKisilerin yuzlerine baktiginda Yavuzalp Korkmaz, Anil Aksu ve Oguzhan Sahin olduklarini goruyorsun...\
                               \n\nSimdi ne yapacaksin?..")

            anahtar_secimi = self.secenek_taslak(secenekler = ["Camin arkasindakilere seslen.",
                                                               "Arkanda duran silahi al ve cama ates et.",
                                                               "Cebinden telefonu cikar ve hemen Yan Camanın basrollugundeki Pasha Fencer reklamlarini izle."])
            # anahtarda 3 secenek var:
            # Seslen = 0
            # Cama ates et = 1
            # Pasha Fencer izle = 2

            if anahtar_secimi == 0:
            # Burasi anahrarı ac --> seslen bloğu

                self.mesaj_taslak("\nArkadaslarina seslendin: Neler oluyor burada? Ne yapıyorsunuz??\
                                   \nOguzhan: 8k Yasuo var kardesim bende.\
                                   \nYavuzalp: Falcao gitsin bence.\
                                   \nAnil: Kolsuz musun abi ya?")
                self.mesaj_taslak("\nSaskinlikla arkadaslarinin yuzune baktin. Iyi olup olmadiklarini sordun ama sana cevap veren olmadı..\
                                   \nHenüz durumu anlayamamisken, daha once orada oldugunu bile farketmedigin hoparlorden cizirtili bir ses duydun...")
                hoparlor_secimi = self.secenek_taslak(secenekler = ["Hoparlore yaklaş ve soylenenleri duymaya calis.",
                                                                    "Silahı al ve hoparlore ates et."])
                # seslen blogu, hoparlor secimine yonlendiriyor. hoparlorde iki secim var:
                # Hoparloru dinle = 0
                # Hoparlore ates et = 1

                if hoparlor_secimi == 0:
                    # hoparloru dinle blogundayız.

                    self.mesaj_taslak("\nHoparlore yaklastiginda tanidik bir ses duymaya basliyorsun:\
                                       \n- Hahaha Hayrettin hoca seni burada bulabilecegimi soylemisti...\
                                       \nBi sikinti olmazsa, onumuzdeki Ocak ayinda mezunum... Hahahaha!\
                                       \nNeyse, konumuza donelim.")
                    self.mesaj_taslak("\nOnundeki cam kursun gecirmez. Birazdan bu cami indirecegim. Elindeki silahta iki kurşun var..\
                                       \nYani burdan sadece iki kişinin sag kurtulmasını istiyorum...\
                                       \nEger bir kahramanlik yapmaya kalkarsan uc arkadasin da sandalyenin altinda bulunan kaziklarla aci icinde olumu tadar. Hahahaha\
                                       \nZamanin kisitli. Kararini hemen vermen lazim.")
                    self.mesaj_taslak("\nArkadaşlarının seslerini duydun:\
                                       \n\nYavuzalp: Ben senin Kim Milyoner Olmak Isterdeki telefon jokerinim, beni olduremezsin. Futbol sorusu gelse yapabilcek misin?\
                                       \nOguzhan: Kanka ben kedisi medisi olan adamim yapma bak. Chester var mi kanka?? Yoksa baska beyaz filtre de olur.\
                                       \nAnil: Sacmalama abi tabii ki de beni seciceksin. Bi de dusunuyo musun bunu gercekten. Silahi ver abi ba...")

                    anil_aksu_secim = self.secenek_taslak(secenekler = ["Lafını bitirmesini beklemeden Anil Aksu'yu iki kez vur ve infaz et.",
                                                                        "42 dakika boyunca neden Anil Aksu'yu vurmaman gerektigini dinle."])
                    # hoparloru dinleyince ilk asamada anil aksuyla ilgili secimler goruyoruz.
                    # Anili vur = 0
                    # Anili dinle = 1

                    if anil_aksu_secim == 0:
                    # anil aksuyu infaz ettik.
                        self.mesaj_taslak("\nAnil Aksu'ya yaptigini gorunce isin arkasindaki master mind'in kani dondu...\
                                           \nNe diyecegini bilemez bir haldeki master mind'in kekeleyerek konusmaya basladigini duydun:\
                                           \n- Kanka sen ne cesit bi manyaksin? Hayrettin hoca bile tahmin edemezdi bunu seninle ugrasilmaz.")
                        self.mesaj_taslak("\nKapinin kilidinin acildigini duydun ve saskinlik icersinde master mind'in kendisini gostermesini bekledin\
                                           \nAklindan isimler gecip gidiyordu, Sefa Yalcinin bir Hayrettin hocasi vardi.\
                                           \nSalim de Hayrettin hocayı taniyordu ve yersiz sakalari severdi.\
                                           \nFakat karsinda gordugun isim bunlarin hicbiri degildi...")
                        self.mesaj_taslak("\nBu isin arkasindaki master mind,\n\
                                           \nMERTCAN YETIK'IN TA KENDISIYDI...")
                        self.mesaj_taslak("\nMertcan sana dogru yaklasti.. Elinde bir silah vardi ama sana dogru dogrultmuyordu\
                                           \nCunku silahindaki iki kursunu da Anil Aksu'ya sıktıgını gormustu...\
                                           \nOnce sana sonra da icerde Anil'in cesedi basinda donakalmis olan Yavuz ve Oguz'a bakti.\
                                           \nSonra gozlugunu duzeltti, bir seyler soylemek uzere oldugunu anlamistin...")
                        self.mesaj_taslak("\nMertcan: Aslinda kurallari cignedigin icin hepinizi oldurmem lazim...\
                                           \nUmutsuz bir sekilde bekliyordunuz. Sizi oldureceginden hic suphen yoktu...\
                                           \nMertcan: Ama canım batak istiyor. Anil pek anlamiyordu zaten. Hazır 4 kisiyiz, sunlari coz de bataga gidelim.")
                        self.mesaj_taslak("\nHepiniz donup kalmistiniz. Yavuz batak oynamayi bilmiyordu fakat Mertcan'in bundan haberi yoktu.\
                                           \nYasamak icin son firsatiniz oldugunu farkedip hemen digerlerini cozmeye basladin.\
                                           \nKapinin arkasina bakip nerede oldugunu gorunce saskinligin daha da artmisti...\
                                           \n\nBastan beri kapali olan kapi, Yeni Yildiz Kiraathanesine aciliyordu.\
                                           \nBatak masasina oturup sabaha kadar esli batak oynadiniz. Sansliydin, esin Mertcan'di.\
                                           \nAnil ise gokyuzunden bakıp soyle diyordu: Salak bunlar ya valeye as dusulur mu?...")

                        self.oyun_sonu(kazanc_durumu = "Tebrikler, kazandiniz!", ascii_resim = "tatli_kurtulus.txt")

                    else:
                    # anil aksuyu dinledin...
                        self.mesaj_taslak("\nLafini bitirene kadar Anil Aksu'yu dinlemeye calistin...\
                                           \nNiyetin yalnizca kibar olmakti.. Anil'in konusmasini bolmek istemedin..\
                                           \nAma bunu caninla odeyecegini nereden bilebilirdin ki...")
                        self.mesaj_taslak("\nDakikalar geciyordu ama Anil susmuyordu.\
                                           \nZaman kavramini yitirirken ruhunun yavasca bedenini terkettigini hissetmeye basladin.\
                                           \nBoyle bir adamin sozunu kesemeyecek kadar kibar bir insan icin bu dayanilir bir bencillik degildi...\
                                           \nGozlerini sonsuz uykuya kapatirken kulaklarinda su sozler yankilandi:\
                                           \n- Abi yani nasi asker basmadin yani senin yuzunden kaybettik bin tane altin yollamissan ne olm.....")

                        self.oyun_sonu(kazanc_durumu = "Uzgunum, kaybettiniz...", ascii_resim = "bos_olum.txt")

                else:
                # hoparlore ates et blogundayiz.
                    self.mesaj_taslak("\nHoparlore ates ettin. Mermilerinden birini çoktan harcadın...\
                                       \nNe yapacağını çözmeye çalışıyorsun fakat belki de bunu öğrenmek için tek şansını az önce harcadın...\
                                       \nKimsenin ne yapacağını bilmediği bir odada arkadaşlarının küfürleri kulağında yankılanıyordu.\
                                       \nNeden ateş ettiğine dair hiçbir fikrin yoktu ve silahta başka mermi olup olmadığını bilmiyordun...\
                                       \nAnıl Aksunun hakaretlerine, Oğuzhan Şahinin beyaz filtre sevgisine ve Yavuzalp Korkmazın umarsızlığına dayanamayıp\
                                       \nonları ölüme terkederek kafana sıktın...\
                                       \nAma artık şunu biliyordun ki,\
                                       \nHoparlore sıktığın o mermi, son mermi değildi...")
                    self.oyun_sonu('bos_olum.txt', 'Uzgunum, olabilecek en kötü şekilde kaybettiniz..')

            if anahtar_secimi == 1:
            # silahla cama ates et
                self.mesaj_taslak("\nSilahi aldin ve arkadaslarini kurtarmak umuduyla cama ates ettin...\
                                   \nFakat bilmedigin bir sey vardi...\
                                   \n\nCam kursun gecirmezdi ve seken kursun kasiklarina isabet etti..\
                                   \nCinsel organindan vurulmus halde kan kaybindan oldun...")

                self.oyun_sonu(kazanc_durumu = "Uzgunum, kaybettiniz...", ascii_resim = "bos_olum.txt")

            if anahtar_secimi == 2:
            # pasha fencer izle
                self.mesaj_taslak("\nOmrunun sonuna kadar sarji bir turlu bitmeyen telefonunda Yan Caman videolari izleyerek olumu bekledin...\
                                   \nSon duydugun sey Yan Caman'in su sozleri oldu:\
                                   \n\"Cok eglenceli oyun yha, muthis zaman geciriyorum...\"")

                self.oyun_sonu(kazanc_durumu = "Uzgunum, kaybettiniz...", ascii_resim = "bos_olum.txt")

        elif sectigimiz == 1:
        # silahi al basta.
            self.mesaj_taslak("\nKaranlikta dikkatlice yuruyerek masadaki silaha yoneliyorsun..\
                               \nSilahi eline aldiginda, bunun Oguz'un Canik silah Fabrikasinda urettigin hatali silahlardan biri oldugunu farkediyorsun...\
                               \nKapiya ates ediyorsun fakat silah tutukluk yapiyor cunku Oguz silahi o kadar kotu yapmis ki...\
                               \nBir anda isiklar aciliyor ve odadaki cami farkediyorsun...\
                               \nCamin arkasinda uc kisi... Oguzhan Sahin, Yavuzalp Korkmaz ve Anil Aksu...")
            self.mesaj_taslak("\nArkadaslarina bakarken bir ses duyuyorsun.. Onlarden gelmiyor.. Bu olayi kurgulayan Master Mind olmali..\
                               \n- Hahahahaha Hayrettin hoca burada olacagini soylemisti... Bakiyorum da silahi bulmussun.. Bir kahramanlik yapma, onundeki cam\
                               \nkursun gecirmez.. Kursunlar sana sekip seni oldurebilir HAHAHAHAHA... Elindeki silahta iki mermi var.. Buradan yalnizca iki kisi\
                               \nsag kurtulacak.. Seninle beraber gelmesini istedigin arkadasini sec ve diger ikisini infaz et.. Hayrettin Hoca sonucu cok merak\
                               \nediyor HAHAHAHAHA..")
            self.mesaj_taslak("\nCam acilir acilmaz Anil Aksu kimseye firsat vermeden konusmaya basliyor...\
                               \n- Ya abi saçmalamayın benim ölüm OMU Tip kazanir ne alaka Tekirdag!!? Neyse kanka en çok siz biliyonuz ya, Yavuz Gwent geccem gelcen\
                               \nmi, ben dunyanin en iyisiyim\
                               \nAnilin cilginca konusmalarini dinlerken gercek anlamda cildirdigini\
                               \nfarkediyorsun. Ortamin gerginligi ile bu deliye elindeki silahi vermeyi\
                               \ndusunmeye basliyorsun.. Bu dusunce giderek seni ele gecirmeye basliyor...\
                               \nNeden bunu yapmak istedigine dair hicbir fikrin yok...")

            anili_sikmek_yada_sikmemek = self.secenek_taslak(secenekler = ["Cilgin dusuncene kurban gidip silahi Anila ver..",
                                                                           "Anili sacindan tut, gotunden sik.."])
            if anili_sikmek_yada_sikmemek == 0:
                #silahi anila verdik
                self.mesaj_taslak("\nCilgin dusunceler vucudunu ele gecirirken bir anda kendini gozleri kapali elleri bos bir halde buldun...\
                                   \nGozlerini acip karsiya baktiginda Anili cozup silahi verdigini gordun.. Daha da kotusu Anil pis kahkahalar\
                                   \nicinde silahi sana dogrultuyordu..\
                                   \nAz once tutukluk yapan silah mucizevi bir sekilde calismaya baslamisti ve Anil yuzundeki pis siritmayla silahi\
                                   \nOguza dogrultup onu infaz etti.. \"Iyi LOL oynardi ama artik benden iyi degil HAHAHHAHAHAH\"")
                self.mesaj_taslak("\nAnil silahi sana dogrulttu.. Yeni ateslenmis silahin namlusundaki sicakligi hissediyordun..\
                                   \nOguzun kani yerleri kirmiziya boyamisti... Kan golundeki yansimadan kendine son bir kez baktin..")
                yalvarmak_kufretmek = self.secenek_taslak(secenekler = ["Korkusuzca Anil'a kufur et.",
                                                                        "Canin icin Anil'a yalvar."])
                if yalvarmak_kufretmek == 0:
                    # anila sovduk. haketti pust
                    self.mesaj_taslak("\nIcindeki delikanliliga guvenerek agzindan dokulen su kelimelere musade ettin: \
                                       \n- Keske seni sacindan kavrayip gotunden sikseydim amk pezevengi pust niye vuruyosun adami got!!\
                                       \n\
                                       \nKufur ederken Anil'in sana bakmadigini farkettin. Bu silahi almak icin bir firsat olabilirdi ama Anil cok uzakti..\
                                       \nBir anda bir silah sesi duydun... Havaya karisan tasak kokusuna anlam veremiyordun... Gozlerini actiginda\
                                       \nOguzun yaninda sereserpe yatan Yavuzu gordun.. Olurken bile hicbi sey dememisti...")
                    self.mesaj_taslak("\nAnlam veremiyordun.. Anil ise Yavuzun cesedine bakıp KAHKAHKAH guluyordu..\
                                       \nSana dogru dondu ve \"O beni Gwent'te yenebilirdi... Ama sen yenemezsin HAHAHAH. Hadi gidelim de Gwent oynayalım..\"\
                                       \nGwent konusundaki yeteneksizliginin hayatini kurtaracagini bilemezdin...")

                    self.oyun_sonu(kazanc_durumu = "Tebrikler, kazandiniz!", ascii_resim = "tatsiz_kurtulus.txt")

                if yalvarmak_kufretmek == 1:
                    # anila yalvardik.
                    self.mesaj_taslak("\nSilahin arkasinda duran Anil'a dogru bakarken goz yaslarina hakim olamiyordun...\
                                       \nYasamak istedigin icin dizlerinin uzerine cokerek yalvarmaya basliyorsun... \"Lutfen! Yasamak istiyorum!\"\
                                       \nSana Age of Empires'da hem odun ve altin attim, beni infaz edemezsin!!\
                                       \nAma unuttugun bir sey vardi; Anil bencil bir pusttu..\
                                       \nSon gordugun sey Anilin elindeki silahin namlusu, son duydugun sey ise Anilin su sozleriydi: Asker bassaydin...")
                    self.mesaj_taslak("\nOguzla beraber cennette \"Ne kadar bos yasadik amk al iste olduk simdi\" geyigi yaparken Anil ve Yavuzu izliyordunuz..\
                                       \nUzuntunuz bir anda gecmisti cunku onlar sizden daha bostu ve bu isin arkasinda kimin oldugunu bile sorgulamadan\
                                       \nkalkip Gwent oynamaya gittiler...")

                    self.oyun_sonu(kazanc_durumu = "Uzgunum, kaybettiniz!", ascii_resim = "bos_olum.txt")

            elif anili_sikmek_yada_sikmemek == 1:
                #anili siktik...
                self.mesaj_taslak("\nCilgin dusuncelerinin kurbani olmaya basliyorsun... Elindeki silahi yavasca yere birakip Anila yaklasiyorsun...\
                                   \nO guzel sirma saclari sana hayırlı bir sehzade verebilecegi duygusuna engel olamiyorsun...\
                                   \nAnil'in aci cigliklari senin kulagina bir muzik gibi geliyor... Anil'in sacini eline dolayip, gozlerini kapiyorsun...\
                                   \nHer sey bittiginde neler yaptiginin farkına varıyorsun... Cigliklar icinde kendini duvarlara vurmaya basliyorsun.\
                                   \nKendini yiyip bitirirken Anil'in silahi aldigini farketmiyorsun. Secde pozisyonundayken silahi alan Anil:\
                                   \n- Prostat muayenesi mi yapiyorsun pezevenk!!!\
                                   \nDiye bagirarak once seni, sonra kendini vuruyor...")
                self.mesaj_taslak("\nSiz Anil'la sarmas dolas cennetten olup biteni izlerken Master Mind odaya giriyor...\
                                   \nMaster mind'in kim olabilecegini dusunuyorsun.. Sefa Hayrettin Hocayi taniyor.. \
                                   \nSalim de oyle ayni zamanda yersiz sakalari da seviyor...\
                                   \nAma Master Mind ikisi de degil....")
                self.mesaj_taslak("\nBu isin arkasindaki ust akil.. Master Mind\
                                   \nMERTCAN YETIK.....\
                                   \n- Hayrettin Hoca bile bunu tahmin edemezdi... HAHAHAHHA. Noldu oglum orda anlatsam babamlar inanmaz yemin ediyorum.\
                                   \nSaskinlik icersinde kalan Oguz, tasaklarini koklayan Yavuza bakiyor.. \
                                   \nMertcan Oguz ve Yavuzu cozup CS atmak istiyor fakat Yavuzu kimse ikna edemiyor..\
                                   \nYavuzun bu bencil ve umursamaz tavrina dayanamayan Mertcan cebinde duran kucuk 45likle Yavuzu delik desik ediyor.\
                                   \nKapidan cikip gittiklerinde izlerini kaybediyorsun ama biliyorsun ki \
                                   \nMertcanlarin evin arkasinda sigara icip Imerin CS'de ne kadar kotu oldugundan bahsediyorlar...")

                self.oyun_sonu(kazanc_durumu = "Uzgunum, kaybettiniz!", ascii_resim = "bos_olum.txt")

        elif sectigimiz == 2:
            # basta kapıyı acmaya calisiyorsun.
            self.mesaj_taslak("\nKilitli olmasini bekleyerek kapiyi zorluyorsun fakat kapi kilitli değil...\
                               \nKapiyi aciyorsun ve yuzune vuran sigara kokusuyla bir anda kendine geliyorsun.\
                               \nIcerinin karanligina alismis olan gozlerini yavasca aciyorsun...\
                               \nYavasca icerideki ugultulari duyuyorsun:\
                               \n- Bi lira ver la bi lira odicem la\
                               \n- Oglum yancinin yedigini kaybeden oder var mi oyle bi dunya hayirdir??\
                               \n- Ya gadasim satranç mi oynuyoruz ne bekliyorsun dunyayi mi fethedicen?")
            self.mesaj_taslak("\nNerede oldugunu anlayinca, gozlerinden akan yaslara engel olamiyorsun...\
                               \nEvet... Oradasin!\
                               \n\nYENI YILDIZ KIRAATHANESI!!")
            self.mesaj_taslak("\nMasalar arasinda ceylan gibi sekip bos buldugun yere oturuyorsun..\
                               \nMasana oturan herkes dayi, ama senin umurunda degil..\
                               \nTek dusundugun yillardir hayalini kurdugun hayati yasamak..\
                               \nOmrunun sonuna kadar muz kakao icip batak oynamak...")
            self.mesaj_taslak("\nDayilarla batak masasindasin. Yerde kupa 10 var ama kagitlari saymayi unuttun...\
                               \nElinde kupa kizi ve kupa as var.. Papaz cikti mi hatırlamiyorsun..\
                               \nAs dusersen alay konusu olabilirsin, kiz dusersen de bos yere eli verebilirsin..\
                               \nNe yapacagini iyi dusunmelisin...")
            kiz_mi_as_mi = self.secenek_taslak(secenekler = ["Risk al, kızı dus.",
                                                             "Hic riske gerek yok, belki de son kupadir asi dus."])
            # kızı mı atalım ası mı??
            # Kız = 0
            # Papaz = 1

            if kiz_mi_as_mi == 0:
            # kızı dustuk
                self.mesaj_taslak("\nKizi dustun.. Yerdeki kizi gorunce sagindaki dayi kahkahalara boguldu...\
                                   \nDayinin agzindan gelen Tekel 2000 kokusu burnunu, dayinin kahkahasi ise kulanlarini senden almisti.\
                                   \nKupa papazi gelmisti.. Eli kaybetmenin yani sira bir de dayilara rezil oldun..\
                                   \nAma uzulecek bir sey yoktu cunku bunlarin hicbiri gercek degildi...")
            if kiz_mi_as_mi == 1:
            # asi dustuk
                self.mesaj_taslak("\nAsi dustun.. Bir kac kez daha kupa dondugunu hatirladin ve sagdaki dayinin sararmis biyiklari altindan guldugunu gordun..\
                                   \nAyaga kalkti, sag elinde bir kart tutuyordu... Masaya vurdu..\
                                   \nDayinin kupasi bitmisti ve asina koz cekmisti... Kupa asi maca 2'ye vermistin...\
                                   \nKoz bittikten sonra son elde dönen kagit ise seni kahretmisti...\
                                   \nKupa papaz dusmustu ama senin asin yoktu. Son eli alamadigin icin batmistin\
                                   \nAma uzulecek bir sey yoktu cunku bunlarin hicbiri gercek degildi...")

            self.mesaj_taslak("\nIlac kokan bir oda... Durmadan diiitleyen makineler... Ve yataginda haraket edemeyen sen...\
                               \nSon 25 senedir komadasin.. Her seyin farkinda olsan da bu farkindalik artik seni yoruyor ve hayal alemlerine daliyorsun..\
                               \nRuyandaki dayilarin hepsi, seninle ilgilenen laz hasta bakicinin pisirdigi Gurcu hamsileri idi...")

            self.oyun_sonu(kazanc_durumu = "Uzgunum, kaybettiniz!", ascii_resim = "bos_olum.txt")

    def mesaj_taslak(self, mesaj, relx = 5, rely = 5):
        appTaslak = npyscreen.Form(name = "Olum odasina hosgeldin!!")
        silahYanlisAciklama = appTaslak.add(npyscreen.MultiLineEdit, editable = False, value = mesaj, relx=relx, rely=rely)
        appTaslak.edit()

    def secenek_taslak(self, secenekler):
        appTaslak = npyscreen.Form(name = "Olum odasina hosgeldin!!")
        taslakSecenekler = appTaslak.add(npyscreen.TitleSelectOne, value = [0,], name = "Seceneklerin sunlar: ",
                             values = secenekler)
        appTaslak.edit()

        return taslakSecenekler.value[0]

    def oyun_sonu(self, ascii_resim, kazanc_durumu):
        with open(ascii_resim, "r") as mesaj:
            oyunsonu_mesaji = mesaj.read()
        appOyunBitti = npyscreen.Form(name = "Olum odasina hosgeldin!!")
        oyunSonuAciklama = appOyunBitti.add(npyscreen.MultiLineEdit, editable = False,
                                           value = f"\n{kazanc_durumu}\
                                            \nOynadiginiz icin tesekkurler!\
                                            \n{oyunsonu_mesaji}")
        appOyunBitti.edit()

if __name__ == '__main__':
    App = OldurmeUygulamasi()
    App.run()
