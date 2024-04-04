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


def countingSort(arr):
    result = [0 for _ in range(100)]

    for i in arr:
        result[i] += 1

    return result


def reverse_row(matrix, row):
    matrix[row].reverse()


def reverse_col(matrix, col):
    strt = 0
    end = len(matrix) - 1
    while strt < end:
        matrix[strt][col], matrix[end][col] = matrix[end][col], matrix[strt][col]
        strt += 1
        end -= 1


def flipping_the_matrix(matrix):
    n = len(matrix)
    quad = n // 2

    for row in matrix:
        print(row)

    max_sum = 0
    for r in range(quad):
        for c in range(quad):
            print()
            print(f'[{r}][{c}]')
            print(f'[{matrix[r][c]}], [{matrix[r][n - c - 1]}]')
            print(f'[{matrix[n - r - 1][c]}], [{matrix[n - r - 1][n - c - 1]}]')

            biggest = max(
                matrix[r][c],
                matrix[r][n - c - 1],
                matrix[n - r - 1][c],
                matrix[n - r - 1][n - c - 1]
            )
            max_sum += biggest

    return max_sum
