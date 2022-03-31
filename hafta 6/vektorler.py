import numpy

v1 = [1, 2, 3]
v2 = [2, 3, 4]
print(v1+v2)
#vt = [3, 5, 7]

# numpy -> vektör ve matris işlemlerinin
# kolaylıkla gerçekleştirilmesini sağlar

# pip install numpy
# pip3 install numpy
# python -m pip install numpy
# py -m pip install

v1 = numpy.array([1, 2, 3])
v2 = numpy.array([3, 4, 5])

print(type(v1))
print(v1+v2)
print(v1-v2)

# en küçük eleman
print(min(v1))
# en büyük eleman
print(max(v1))

print(v1.shape)
# bölme
print(v1/v2)
# carpma
print(v1*v2)
# vektörler elemanlarına indisler aracılığı ile erişilebilri.
print(v1[0])
