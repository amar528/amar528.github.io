#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'degreeOfArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def degreeOfArray(arr):
    # the degree is the largest number of times an element occurs in the array
    counts_arr = [(i, arr.count(i), idx) for idx, i in enumerate(arr)]
    max_element = max(counts_arr, key=lambda t: t[1])
    degree = max_element[1]

    max_elements = list(filter(lambda e: e[1] == degree, counts_arr))
    max_elements.sort(key=lambda e: e[0])

    # given the degree of arr compute all sub arrays that have the same degree
    sub_arrays = [sub_array for sub_array in arr]

    # return the minimum length of the sub arrays

    return degree


if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().split()))

    result = degreeOfArray(arr)

    print(result)
