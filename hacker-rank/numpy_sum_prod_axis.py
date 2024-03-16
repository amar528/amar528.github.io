import numpy

#  n rows m columns
n, m = map(int, input().split())

_a = []
for row in range(n):
    _a.append(list(map(int, input().split())))

a = numpy.array(_a)

a_sum = numpy.sum(a, 0)
product = numpy.prod(a_sum)

print(product)
