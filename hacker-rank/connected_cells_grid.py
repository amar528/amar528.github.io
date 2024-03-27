#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

neighbours = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
]


def is_valid(grid, row, col, visited):
    row_count = len(grid)
    column_count = len(grid[0]) if row_count > 0 else 0
    return (0 <= row < row_count
            and 0 <= col < column_count
            and not visited[row][col]
            and grid[row][col] == 1)


def dfs(grid, row, col, visited, count):
    visited[row][col] = True

    for neighbour in neighbours:
        n_row = row + neighbour[0]
        n_col = col + neighbour[1]

        if is_valid(grid, n_row, n_col, visited):
            count[0] += 1
            dfs(grid, n_row, n_col, visited, count)


def get_largest_region(matrix):
    rows = len(matrix)
    if rows == 0:
        raise ValueError('Invalid grid, has 0 rows')

    cols = len(matrix[0])
    if cols == 0:
        raise ValueError('Invalid grid, has 0 columns')

    result = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1 and not visited[row][col]:
                count = [1]

                dfs(matrix, row, col, visited, count)

                result = max(result, count[0])

    return result
