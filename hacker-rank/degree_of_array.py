#!/bin/python3
import array


def degreeOfArray(input_arr):
    lengths = []
    number_dict = {}

    for i, v in enumerate(input_arr):
        data = number_dict.get(v)
        if data:
            indices = data[1]
            indices.append(i)
            new_data = (data[0] + 1, indices)
            number_dict[v] = new_data
        else:
            indices = array.array('I')
            indices.append(i)
            new_data = (1, indices)
            number_dict[v] = new_data

    data_it = (item for item in number_dict.items())
    degree = 0
    degree_items = []
    for k, v in data_it:
        if v[0] > degree:
            degree = v[0]
            degree_items.clear()
            degree_items.append(v)
        elif v[0] == degree:
            degree_items.append(v)

    for tup in degree_items:
        indices = tup[1]
        _min = min(indices)
        _max = max(indices)
        lengths.append(_max - _min + 1)

    return min(lengths)


if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().split()))

    result = degreeOfArray(arr)

    print(result)
