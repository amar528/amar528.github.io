import collections
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # store hash of row/column -> count
        row_counts = collections.defaultdict(int)

        # resulting overall count
        count = 0

        # process each entire row
        for row in grid:
            row_hash = hash(tuple(row))

            # store the count of this row combination
            row_counts[row_hash] += 1

        # process each entire set of columns
        for cols in zip(*grid):
            col_hash = hash(tuple(cols))

            # if an exact matching row was found, add it to the count
            if col_hash in row_counts:
                count += row_counts[col_hash]

        return count
