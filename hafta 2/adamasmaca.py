import random
kelime_listesi = ["istanbul","ankara","izmir","sakarya"]

kelime_say = int(random.uniform(0,len(kelime_listesi)))
soru = kelime_listesi[kelime_say]

bosluk = int(random.uniform(0,len(soru)))
bosluk_2 = int(random.uniform(0,len(soru)))
while bosluk==bosluk_2:
    bosluk_2 = int(random.uniform(0,len(soru)))

orj_soru = soru
soru = list(soru)
soru[bosluk] = "_"
soru[bosluk_2] = "_"

soru_kelime = ""
for k in soru:
    soru_kelime=soru_kelime+k

print(soru_kelime)
hak=3
while hak>0:
    hak=hak-1
    girilen = input("doğru kelimeyi giriniz")
    if girilen == orj_soru:
        print("tebrikler")
        break
    else:
        print("tekrar deneyiniz")
        if hak==2:
            print("/\\")
        elif hak == 1:
            print("/|\\")
            print("/\\")
else:
    print("hakkınız bitti")
    print(" O")
    print("/|\\")
    print("/\\")