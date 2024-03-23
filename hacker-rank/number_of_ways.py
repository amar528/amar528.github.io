#!/bin/python3
import itertools


#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY roads as parameter.
#

def numberOfWays(roads):
    ways = 0

    # ([1, 2], [2, 5], [3, 4], [4, 5], [5, 6], [7, 6])
    # 7 cities
    # 2, 4, 6 == 2
    # 1, 3, 7 == 3
    # answer is 2 ways
    for c in itertools.combinations(roads, r=len(roads)):
        print(c)

    return ways


# Write your code here

if __name__ == '__main__':

    roads_rows = int(input())
    roads_columns = int(input())

    roads = []

    for _ in range(roads_rows):
        roads.append(list(map(int, input().rstrip().split())))

    result = numberOfWays(roads)

    print(str(result) + '\n')
