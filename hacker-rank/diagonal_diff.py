#!/bin/python3


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    primary = []
    secondary = []
    for i in range(n):
        # print(i,i)
        # print(i,n - i - 1)
        primary.append(arr[i][i])
        secondary.append(arr[i][n - i - 1])

    p_sum = sum(primary)
    s_sum = sum(secondary)
    return abs(p_sum - s_sum)


if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
