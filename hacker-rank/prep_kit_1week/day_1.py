#!/bin/python3
import collections
import datetime
import math
import os
import random
import re
import sys
from time import strptime, strftime


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = negative = zero = 0.0

    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            positive += 1
        elif i < 0:
            negative += 1

    n = len(arr)
    print(f'{positive / n:.6f}')
    print(f'{negative / n:.6f}')
    print(f'{zero / n:.6f}')


def miniMaxSum(arr):
    n = len(arr)
    arr.sort()
    print(sum(arr[:n - 1]), sum(arr[1:]))


def timeConversion(s):
    t = strptime(s, '%I:%M:%S%p')
    return strftime('%H:%M:%S', t)

def find_median(arr):
    arr.sort()
    n = len(arr)
    mid = n // 2
    return arr[mid]
