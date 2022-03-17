# boş liste tanımlaması
"""
liste1 = []
liste2 = list() # list([])

print(liste1 == liste2)

liste3 = [1,2,3,4,""]
liste4 = list([1,2,3,4,""])
print(liste3==liste4)
        #0123456
        #-7-6-5-4-3-2-1
metin = "Merhaba"
# indis
print(metin[4])
print(metin[6])
print(metin[-7]) # ilk eleman

for ind in range(len(metin)): # 0,1,2,3,4,5,6
    print(metin[ind])

print(liste4[0])
print(liste4[-1])

for i in range(len(liste4)):
    print(liste4[i])

liste4 = list([1,2,3,4,""])
for e in liste4:
    print(e)

kelime="merhaba"
kelime_karakter_liste = list(kelime)
print(kelime_karakter_liste)

print(liste4[0:3])

print(liste4)
liste4[0]="S"
print(liste4)

kelime[0] = "M"
print(kelime)



Klavyeden girilen bir ifadenin 3. harfinin M
olması isteniyor. Bunu gerçekleştiren uygulamayı yazınız.


kelime = input("Bir kelime giriniz")
kelime_liste = list(kelime)
kelime_liste[2]="M"

son_kelime=""
for karakter in kelime_liste:
    son_kelime=son_kelime+karakter

print(son_kelime)
"""




