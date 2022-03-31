# tuple - demet
import turtle


liste1 = [1, "asd", 23, 2, "dasd", [2, "ad"]]
tuple1 = (1, 2, 3, 4)
print(type(tuple1))

# tuple(demetler) aynı listelerde olduğu gibi sıralı
# veri tiplerindendir. normal parantezler arasına yazılır ve
# elemanları arasında virgül vardır.

# Listelerden farklı elemanların değiştirilmez olmasıdır.

# boş tuple
orn_tuple = ()  # tuple()

# veriler değiştirilemez
"""
tuple2 = (1, 2, 3, 5, 7)
tuple2[0] = 100 # hata verir
print(tuple2)
"""

yeni_tuple = tuple([1, 2, 3, 4, 5])
print(yeni_tuple)

# tuple elemanları indisler aracılığıyla erişilebilir.

print(yeni_tuple[0])
print(yeni_tuple[-1])
print(len(yeni_tuple))  # eleman sayısı
print(yeni_tuple[0:4])

for k in yeni_tuple:
    print(k)

# eleman değeri değiştirilemez, ama tuplelar genişletilebilir.

liste1 = [2, 4, 1, 2]
liste2 = [1, 2, 4]
print(liste1+liste2)

tuple1 = (1, 2, 3, 4)
tuple2 = (1, 5, 3, 6)
print(tuple1+tuple2)

# del tuple1
# print(tuple1) # hata verir

# tuple'larda silinmede desteklenmez
# del tuple1[0] # hata verir

tuplex = (1, 3, 5, -10, 3, 5)

""" 
1- tuple içindeki elemanların toplam değerlerini ve çarpım
değerini yeni bir tuple' a yazınız.
2- tuple içindeki en büyük elemanı bulunuz.
3- tuple içindeki elemanları büyükten küçüğe sıralayınız ve
tekrar aynı tuple' a yazınız.
"""

# Ödev : tuplex içerisinde en çok geçen elemanı ve
# kaç kez tekrar ettiklerini bulunuz.
# 1.
toplam = sum(tuplex)
carpim = 1
for k in tuplex:
    carpim = carpim*k
print((toplam, carpim))
# 2.
print(max(tuplex))
# 3.
liste = list(tuplex)
liste.sort(reverse=True)
print(tuple(liste))


# Ödev : tuplex içerisinde en çok geçen elemanı ve
# kaç kez tekrar ettiklerini bulunuz.

tuplex = (1, 3, 5, -10, 3, 5)

# .count()
# 1. yol
encoktekraredenler = {}
for t in tuplex:
    encoktekraredenler[t] = tuplex.count(t)

tekrarsay = 0
tekrareleman = ""
for a, d in encoktekraredenler.items():
    if (d > tekrarsay):
        tekrarsay = d
        tekrareleman = a

print(tekrarsay)
print(tekrareleman)
# 2. yol
encoktekraredenler = {}
for t in tuplex:
    encoktekraredenler[t] = 0

print(encoktekraredenler)

for t in tuplex:
    encoktekraredenler[t] = encoktekraredenler[t]+1

print(encoktekraredenler)


# Örnekler
tuple1 = (1, 2, 3, 4)
tuple2 = (0, 1, 2, 3)

# yukarıdaki 2 tuple'da elemanların farklarından yeni bir
# tuple oluşturunuz. (1,1,1,1)
"""
liste = []
for i in range(len(tuple1)):
    x = tuple1[i]-tuple2[i]
    liste.append(x)
print(tuple(liste))
"""
t = ()
for i in range(len(tuple1)):
    x = tuple1[i]-tuple2[i]
    t = t+(x,)
print(t)


new_tuple = (10, 1, 4, 9, 4, 1, 5)
# yukarıdaki tuple'da tekrar eden verilerin sadece 1 kez görünmesi
# ni sağlayınız.

liste = []

for t in new_tuple:
    if t not in liste:
        liste.append(t)
print(tuple(liste))


tup = (10, 3, 100, -3, (5, 3, 1), (-10, 20))

# yukarıda iç içe tuple bulunmaktadır. içteki tuple' ın eleman
# değerleri toplamını içteki tuple yerine yazınız.

# sonuc : (10,3,100,-3,9,10)

liste = []
for k in tup:
    if type(k) == tuple:
        liste.append(sum(k))
    else:
        liste.append(k)

print(tuple(liste))
