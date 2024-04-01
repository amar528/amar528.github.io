#!/bin/python3
from functools import reduce


#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    pairs_it = ((arr[i], arr[j]) for i in range(len(arr)) for j in range(i + 1, len(arr)))
    result = list(filter(lambda x: x == k, list(abs(t[0] - t[1]) for t in pairs_it)))
    return len(result)


if __name__ == '__main__':
    first_multiple_input = input().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(str(result) + '\n')
