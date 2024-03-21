#!/bin/python3


#
# Complete the 'getMaxSubsequenceLen' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMaxSubsequenceLen(arr):
    arr_sorted = sorted(arr)

    result = []

    for i, v in enumerate(arr_sorted):
        left = arr_sorted[:i]
        right = arr_sorted[i:]
        if len(left) %2 and len(right) % 2:
            result.append(v)


    return result


# Write your code here

if __name__ == '__main__':

    arr_count = int(input())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input())
        arr.append(arr_item)

    result = getMaxSubsequenceLen(arr)

    print('\n'.join(map(str, result)))
    print('\n')
