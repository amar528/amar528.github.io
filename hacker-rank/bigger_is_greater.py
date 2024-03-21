#!/bin/python3
import itertools


#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def biggerIsGreater(w):
    n = len(w)
    if n <= 1:
        return 'no answer'

    n = len(w)
    i = len(w) - 2
    j = 0

    arr = list(w)

    while i >= 0:
        if arr[i] < arr[i + 1]:
            break
        i = i - 1

    # Check if pivot is not found
    if i < 0:
        arr.reverse()
    else:
        # Find for the successor of pivot in suffix
        for j in range(n - 1, i, -1):
            if arr[j] > arr[i]:
                break

        # Swap the pivot and successor
        swapPositions(arr, i, j)

        # Minimise the suffix part
        # initializing range
        strt, end = i + 1, len(arr)

        # Third arg. of split with -1 performs reverse
        arr[strt:end] = arr[strt:end][::-1]

    answer = ''.join(arr)

    if answer == w or answer < w:
        return 'no answer'

    return answer


# Write your code here

if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)
