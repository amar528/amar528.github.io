import numpy

#  n rows m columns
n, m = map(int, input().split())

_a = []
for row in range(n):
    _a.append(list(map(int, input().split())))

_b = []
for row in range(n):
    _b.append(list(map(int, input().split())))

a = numpy.array(_a)
b = numpy.array(_b)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))
