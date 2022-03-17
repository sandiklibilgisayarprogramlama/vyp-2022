liste = ['selam', 10, 1.0, True, 2, 500, 10]
# yukarıda verilen listeden sayısal olmayan değerleri çıkarınız.

cikarilacak_liste = []
for eleman in liste:
    print(type(eleman))
    eleman_str = str(eleman).replace(".", "")
    if not str(eleman_str).isdecimal():
        cikarilacak_liste.append(liste.index(eleman))
print(cikarilacak_liste)
for cikarilacak in cikarilacak_liste:
    del liste[cikarilacak]

print(liste)


# liste=[1,2,3,4,6,-100,40]
# yukarıdaki listedeki tüm sayıları toplayıp ekrana yazan
# programı kodlayınız.


# yukarıdaki listedeki en küçük sayıyı ekrana yazan kodu
# yazınız.

# yukarıdakş listedeki 2 ye bölünen sayıları
# listeden çıkarınız.

liste = [1, 2, 3, 4, 6, -100, 40]
# 1. yol
toplam = 0
for eleman in liste:
    toplam = toplam + eleman
print(toplam)
# 2. yol
print(sum(liste))

# yukarıdaki listedeki en büyük sayısı ekrana yazdıran kodu
# yazınız

en_buyuk = liste[0]
for eleman in liste:
    if eleman > en_buyuk:
        en_buyuk = eleman
print(en_buyuk)
# 2.yol
print(max(liste))

# yukarıdaki listedeki en küçük sayısı ekrana yazdıran kodu
# yazınız

en_kucuk = liste[0]
for eleman in liste:
    if eleman < en_kucuk:
        en_kucuk = eleman
print(en_kucuk)
# 2.yol
print(min(liste))

# listedeki 2 ye bölünen sayıları listeden çıkartan kodu yazınız.
cikarilacak_liste = []
for e in liste:
    if e % 2 == 0:
        cikarilacak_liste.append(e)

for c in cikarilacak_liste:
    liste.remove(c)

print(liste)

# Veli listelerde kullanılan sort fonksiyonunu bilmiyor. Buna
# göre yukarıdaki listeyi küçükten büyüğe sıralayan kodu yazınız.

liste = [-10, 0, 90, 100, -30, 40]
siralanmis_hal = [-30, 10, 0, 40, 90, 100]
# bouble sort (kabarcık) sıralama algoritması
for i in range(len(liste)):
    for j in range(i+1, len(liste)):
        eleman = liste[i]
        if liste[j] < liste[i]:
            gecici = liste[i]
            liste[i] = liste[j]
            liste[j] = gecici

print(liste)
# liste = [-30, 0, 90, 100, -10, 40]

orn_liste = [10, 30, 40, 60, [30, 40, 50, 90], [-100, 30, 40]]

# yukarıdaki listede iç içe listeler bulunmaktadır.
# listedeki tüm sayıların toplamını ekrana yazdırınız.

toplam = 0
for k in orn_liste:
    if type(k) == int:
        toplam = k + toplam
    else:
        for e in k:
            toplam = e+toplam

print(toplam)


liste = [1, 10, -10, [20, 30, 0]]

# yukarıdaki liste için aşağıdaki soruları cevaplayınız

# tüm sayıların toplamını bulunuz.

# içerideki listenin içine 10 değerini ilk eleman olarak
# ekleyiniz.

liste[3].insert(0, 10)
print(liste)

# listenin içine tüm elemanların toplam değerini 0 yapacak
# sayıyı ekleyiniz.

liste.append(-1*toplam)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# listenin elemanları içindeki boş elemanları çıkarınız
cikarilacak_list = []
for i in range(len(list1)):
    if list1[i] == "":
        cikarilacak_list.append(list1[i])

for k in cikarilacak_list:
    list1.remove(k)

print(list1)

list1 = [5, 20, 15, 20, 25, 25, 20]
# liste içindeki tekrarları teke düşürün
# cevap : [5,20,15,25]

# in, not in
sonuc = []
for eleman in list1:
    if eleman not in sonuc:
        sonuc.append(eleman)

print(sonuc)
