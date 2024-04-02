import collections


def lonelyinteger(a):
    count_map = collections.defaultdict(int)
    for i in a:
        count_map[i] += 1

    lam = (lambda item: item[0] if item[1] == 1 else None)
    for unique in map(lam, count_map.items()):
        if unique:
            return unique
    raise ValueError


def diagonalDifference(arr):
    rows = len(arr)
    if rows == 0:
        return 0
    cols = len(arr[0])

    row = 0
    forward = 0
    backward = -1
    f_sum = b_sum = 0
    while row < rows and forward < cols:
        f_sum += arr[row][forward]
        b_sum += arr[row][backward]
        row += 1
        forward += 1
        backward -= 1

    return abs(f_sum - b_sum)
