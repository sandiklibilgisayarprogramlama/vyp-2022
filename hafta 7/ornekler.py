"""
1.
Bir liste oluşturarak 20 ile 50 arasındaki
bütün tek sayıları bir listeye koyan kodu yazınız.
"""
import random
print(int(random.uniform(1, 41)))
"""
2.
Bir liste tanımlayarak içerisine 10 rastgele sayılar koyunuz.
Daha sonra bu listedeki elemanları toplayarak toplamı döndüren kodu yazınız.
"""
# 3.
liste_1 = [2, 4, 9, 20, -10, 67]
liste_2 = [1, 6, 30, 90]
# bu iki listeyi birleştirip sıralı bir şekilde yazınız.

# 4.
vize_notlar = {"veli": 90, "necmi": 30}
final_notlar = {"veli": 30, "necmi": 80}

"""vize ve final notları sözlüklerde verilen kişilerin dersten kalıp 
kalmadıklarını ekrana yazınız"""

# 1.
liste = []
for k in range(20, 51):
    if k % 2 == 1:
        liste.append(k)
print(liste)

# 2.
liste = []
for i in range(10):
    sayi = int(random.uniform(0, 100))
    liste.append(sayi)

print(sum(liste))

# 3.
tum_liste = liste_1+liste_2
tum_liste.sort(reverse=True)
print(tum_liste)

# 4.
veli = vize_notlar["veli"]*0.4 + final_notlar["veli"]*0.6
necmi = vize_notlar["necmi"]*0.4 + final_notlar["necmi"]*0.6

if veli > 60:
    print("veli geçti")
else:
    print("veli kaldı")

if necmi > 60:
    print("necmi geçti")
else:
    print("necmi kaldı")
