#!/bin/python3


#
# Complete the 'degreeOfArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def degreeOfArray(arr):
    # the degree is the largest number of times an element occurs in the array
    # tuple is (number, count, index)
    counts_arr = [(i, arr.count(i), idx) for idx, i in enumerate(arr)]
    max_element = max(counts_arr, key=lambda t: t[1])
    degree = max_element[1]

    elements_with_degree = list(filter(lambda e: e[1] == degree, counts_arr))
    elements_with_degree.sort(key=lambda e: e[0])

    # given the degree of arr compute all sub arrays that have the same degree

    # key numbers by their indices
    number_indices = {}
    for e in elements_with_degree:
        k = e[0]
        index_to_add = e[2]
        v = number_indices.get(k)
        if v is not None:
            v.append(index_to_add)
        else:
            number_indices[k] = [index_to_add]

    # construct sub arrays for each key (number) using the min, max indices
    lengths = []
    for v in number_indices.values():
        lengths.append((max(v) - min(v)) + 1)

    # return the minimum length of the sub arrays
    return min(lengths)


if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().split()))

    result = degreeOfArray(arr)

    print(result)
