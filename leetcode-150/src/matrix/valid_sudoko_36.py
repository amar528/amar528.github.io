import collections
from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = 9
        not_set = '.'

        # cache the row, column and 3*3 subgrid data collected so far
        rows = collections.defaultdict(set)  # row_number:{values in row}
        columns = collections.defaultdict(set)  # col_number:{values in column}
        sub_grids = collections.defaultdict(set)  # (row, col of 3*3 sub grid): {values in sub grid}

        for r in range(n):
            for c in range(n):
                val = board[r][c]

                # ignore unset values - skip this iteration
                if val == not_set:
                    continue

                # identify sub grid as 0, 0 through 2, 2
                sub_grid = (r // 3, c // 3)

                # check if this value occurs in any of the 3 collections
                if (val in rows[r]
                        or val in columns[c]
                        or val in sub_grids[sub_grid]):
                    return False

                # add the value to our collections
                rows[r].add(val)
                columns[c].add(val)
                sub_grids[sub_grid].add(val)

        return True
