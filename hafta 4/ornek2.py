#sozluk={anahtar:deger, anahtar:deger, anahtar:deger}

sozluk = {32: "ısparta", 44: "malatya"}
print(sozluk[32])

for a, d in sozluk.items():
    print(a)
    print(d)

sozluk[32] = "hatay"
sozluk[6] = "ankara"
print(sozluk)

# del
del sozluk[32]
print(sozluk)
# sozlugun kopyalanması
ss = sozluk.copy()

# elemanların temizlenmesi
sozluk.clear()

print(sozluk)


yas_sozluk = {"ahmet": 10, "veli": 37, "necmi": 83, "recai": 20}

# yukarıdaki sozlukteki yaşları 2 ye bölünmeyen kişileri
# sozlukten çıkaralım.
yas_sozluk_copy = yas_sozluk.copy()
for a, d in yas_sozluk.items():
    if d % 2 != 0:
        del yas_sozluk_copy[a]

yas_sozluk = yas_sozluk_copy
del yas_sozluk_copy
print(yas_sozluk)

deneme_sozluk = {"ankara": 300, "konya": 220,
                 "eskisehir": 120, "istanbul": 550, "ısparta": 150}

# yukarıdaki sozlukte afyon ilinin diger illere uzaklığı
# km cinsinden verilmiştir.

# en uzak ilin kmsini yazınız.
# buna göre en uzak olan ili yazınız.
# en yakın ili yazınız.

# degerleri almak için values() -> list
# anahtarları almak için keys() -> list

# en uzak km
print(max(deneme_sozluk.values()))

km = 0
en_buyuk_anahtar = ""
for a, d in deneme_sozluk.items():
    if d > km:
        en_buyuk_anahtar = a
        km = d

print(en_buyuk_anahtar)

km = max(deneme_sozluk.values())
en_kucuk_anahtar = ""
for a, d in deneme_sozluk.items():
    if d < km:
        en_kucuk_anahtar = a
        km = d

print(en_kucuk_anahtar)

"""
yukarıdaki listede bulunan illerden 
orta mesafede olan ili bulunuz
"""
