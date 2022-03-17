#"selam",'merhaba' -> str

print(type("selam")) # str
print(type(1)) # int
print(type(1.2)) # float
print(type(True)) # bool

""" 
List, # listeler
Dict # sözlük
Tuple # demetler
Set # Kümeler 

Matrix
Bağlı Listeler
Yığınlar
Kuyruklar
Ağaçlar
Sıralama Algoritmaları
"""

# List -> listeler

"selamlar"
print(type([]))

liste1 = []
print(type(liste1))

liste1 = [1,1.4,"selam",[],10]

str1 = "merhaba"
print(str1[0])
print(str1[4])

# belirli bir elemanı ekrana yazmak için indislerden yararlanılır.
print(liste1[0]) # 1
print(liste1[2][-1]) # m

#indis ile eleman yazdırma
# elemanları ekrana yazdırırken döngülerden yararlanılır.
for i in range(len(str1)):
    print(str1[i])

for i in range(len(liste1)): # 0,1,2,3,4
    print(liste1[i])

for e in liste1:
    print(e)


"""for eleman in liste1:
    print(eleman)
"""
