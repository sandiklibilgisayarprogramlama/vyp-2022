class BagliListe:
    isaretci = None


class Dugum:
    veri = None
    isaretci = None


dugum3 = Dugum()
dugum3.veri = 30

dugum2 = Dugum()
dugum2.veri = 20
dugum2.isaretci = dugum3

dugum1 = Dugum()
dugum1.veri = 10
dugum1.isaretci = dugum2

bagli_liste = BagliListe()
bagli_liste.isaretci = dugum1

# ilk eleman
# print(bagli_liste.isaretci.veri)
# ikinci
# print(bagli_liste.isaretci.isaretci.veri)

# print(bagli_liste.isaretci.isaretci.isaretci.veri)

# tüm elemanları listeleme
eleman = bagli_liste.isaretci
while True:
    print(eleman.veri)
    if eleman.isaretci == None:
        break
    eleman = eleman.isaretci

# eleman ekleme
eleman = bagli_liste.isaretci
while True:
    if eleman.isaretci == None:
        yeni_eleman = Dugum()
        yeni_eleman.veri = 40

        eleman.isaretci = yeni_eleman
        break
    eleman = eleman.isaretci

# eleman silme


# eleman güncelleme
