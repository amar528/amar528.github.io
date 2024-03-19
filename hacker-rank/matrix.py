#!/bin/python3
import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = []

for j in range(m):
    for i, row in enumerate(matrix):
        decoded.append(row[j])

string = ''.join(decoded)
regex = r'(?<=\w)[^A-Za-z0-9]{1,}(?=\w)'
print(re.sub(regex, ' ', string))
