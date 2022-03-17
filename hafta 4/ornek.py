# dictinary, sozluk
"""
degisken_adi = {anahtar1:deger, anahtar2:deger2, }

* süslü parantez arasına yazılır.
* anahtar bir sozluk içinde sadece 1 kez kullanılır, aynı 
degerli başka bir anahtar olamaz.
"""
# bos sozluk
ornek_bos_sozluk = {}
# 2. yol
bos_sozluk = dict()
print(type(bos_sozluk))

il_plaka_cifti = {"afyon": 3, "ısparta": 32, "izmir": 35}
manav = {"meyveler": ["elma", "armut", "muz"],
         "sebzeler": ["marul", "salatalık"]}

# sozluk_adi["anahtar_adi"]
print(manav["meyveler"])

print(il_plaka_cifti["afyon"])

# manav' ın içindeki sebze sayısı
print(len(manav["sebzeler"]))

kisi = {"ad": "Ahmet", "soyad": "uzun", "yas": 35}
print(kisi["ad"])

plaka_il = {3: "afyon", 1: "adana", 20: "denizli"}
print(plaka_il[3])

for anahtar, deger in plaka_il.items():
    print(anahtar, " : ", deger)

print(len(plaka_il))

# eleman ekleme
# degisken[anahtar] = deger
plaka_il[32] = "Isparta"
print(plaka_il)

plaka_il[34] = "İstanbul"
print(plaka_il)

# eleman değiştirme
# degisken[anahtar] = yeni_deger
plaka_il[34] = "Ankara"
print(plaka_il)

# eleman silme
# del degisken[anahtar]
del plaka_il[34]
print(plaka_il)

"""
Soru:
Boş bir sozluk tanımlayınız ve içerisine türkiye anahtarını ve asya değerini
ekleyiniz.
"""
sozluk = dict()  # {}
sozluk["türkiye"] = "asya"
print(sozluk)

"""
liste ve sözlükleri kullanarak bir soru bankası uygulaması yapınız.
kullanıcıya 3 hak verilecek.
"""
sorular = [{"soru": "aşağıdakilerden hangisi bir döngü tipi değildir",
            "cevaplar": ["while", "for", "do while", "if"],
            "dogrusik":"if"},
           {"soru": "aşağıdakilerden hangisi ile bir listede silme amaclı kullanılır",
            "cevaplar": ["del", "for", "do while", "if"],
            "dogrusik":"del"}]

for eleman in sorular:
    print(eleman["soru"])
    print(eleman["cevaplar"])
    cevap = input("cevabı yazını")
    if eleman["dogrusik"] == cevap:
        print("dogru cevap")
    else:
        print("Yanliş cevap")
