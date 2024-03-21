#!/bin/python3


#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    if n > 100:
        raise ValueError('n must be less than 100')
    f = 1
    for i in range(n, 1, -1):
        f *= i
    return f


if __name__ == '__main__':
    n = int(input())
    print(extraLongFactorials(n))
