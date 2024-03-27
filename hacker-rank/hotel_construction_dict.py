#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY roads as parameter.
#
from collections import defaultdict


def numberOfWays(roads):
    ways = 0

    # There are n ways to build exactly 3 hotels, each in a
    # different city, so that the distance between every pair
    # of hotels is equal
    #

    # 1
    # 2
    # ([1, 2], [2, 5], [3, 4], [4, 5], [5, 6], [7, 6])
    # 3 hotels
    # 2, 4, 6 == 2
    # 1, 3, 7 == 3
    # answer is 2 ways

    cache = defaultdict(list)

    for start, dest in roads:
        start_entry = cache[start]
        start_entry.append(dest)
        end_entry = cache[dest]
        end_entry.append(start)

    counts = [len(v) for k, v in cache.items()]
    unique_counts = {counts.count(n) for n in counts}
    ways = len(unique_counts)

    # group by size of value
    # if count of common values is 3, that is a way
    return ways


if __name__ == '__main__':

    roads_rows = int(input())
    roads_columns = int(input())

    roads = []

    for _ in range(roads_rows):
        roads.append(tuple(map(int, input().split())))

    result = numberOfWays(roads)

    print(str(result) + '\n')
