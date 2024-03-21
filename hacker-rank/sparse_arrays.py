#!/bin/python3


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    result = [0 for _ in range(len(queries))]
    for i, q in enumerate(queries):
        result[i] = stringList.count(q)
    return result


if __name__ == '__main__':

    stringList_count = int(input())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    print('\n'.join(map(str, res)))
