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
