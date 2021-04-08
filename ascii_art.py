import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

def boyutlandir(resim, yeni_genislik=90):
    genislik, uzunluk = resim.size
    oran = (uzunluk / genislik)/2
    yeni_uzunluk = int(yeni_genislik * oran)
    boyutlandirilmis_resim = resim.resize((yeni_genislik, yeni_uzunluk))
    return boyutlandirilmis_resim

def grilestir(resim):
    grilesmis_resim = resim.convert('L')
    return grilesmis_resim

def pixelden_asciiye(resim):
    pixeller = resim.getdata()
    karakterler = "".join([ASCII_CHARS[pixel // 25] for pixel in pixeller])
    return karakterler

def main(yeni_genislik=90):
    yol = input("Cevirilecek resim icin yol giriniz: ")
    resim = PIL.Image.open(yol)

    yeni_resim = pixelden_asciiye(grilestir(boyutlandir(resim)))
    pixel_sayisi = len(yeni_resim)
    ascii_resim = "\n".join(yeni_resim[i:(i+yeni_genislik)] for i in range(0, pixel_sayisi, yeni_genislik))

    print(ascii_resim)
    with open("ascii_resim.txt", "w") as f:
        f.write(ascii_resim)

if __name__ == "__main__":
    main()
