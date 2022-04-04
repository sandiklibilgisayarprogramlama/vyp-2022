import random
import numpy

m1 = numpy.array(
    [
        [1, 10],
        [90, 20],
        [30, 40],
        [1, 2]
    ]
)
print(m1)
print(m1.shape)

m2 = numpy.array(
    [
        [11, -20],
        [15, 9],
        [42, 40],
        [1, 2]
    ]
)
mtoplam = m1+m2
print(mtoplam)
print(mtoplam.shape)


print(m2[0][1])  # -20
print(m2[2][0])  # 42
print(m2[0])  # m2 in 1. satırı
print(m2[:, 1])  # m2 nin 2. sutunu

# 2. sutunun tüm elemanlarını getiriniz.
sutun_list = []
for k in m2:
    sutun_list.append(k[1])
print(sutun_list)

# yeniden boyutlandırma reshape

k = numpy.reshape(m2, (2, 4))
print(k)
print(k.shape)


m = numpy.array([[1,  2,  3,  4,  5,  6, ],
                [2,  3,  4,  5,  7,  5.4]])

# m matrisinin 1. satır 4. sutunu ile 2. satır 5 sutunu çarpımını ekrana
# yazan python kodunu yazınız.

print(m[0][3] * m[1][4])


# m matrisinin 1 satır 6 sutunundaki elemanı 10 yapın

m[0][5] = 10

print(m)

# Soru=0 ile 20 arasındaki sayılardan 5,6 boyutundaki bir matrisi oluşturunuz.
#  (sayı sırası önemli değildir,
# sadece degerlerin 0 ile 20 arasında olmasına dikkat ediniz.)

print("-------------------------------------")
liste = []

for k in range(30):
    uretilen = int(random.uniform(0, 20))
    liste.append(uretilen)

print(liste)

v = numpy.array(liste)
v = numpy.reshape(v, (5, 6))

print(v)
