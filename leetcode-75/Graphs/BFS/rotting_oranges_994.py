import collections
from typing import List


class Solution:

    def get_neighbours(self, r, c, rows, cols):
        if r < rows - 1:
            yield r + 1, c  # down

        if c < cols - 1:
            yield r, c + 1  # right

        if r >= 1:
            yield r - 1, c  # up

        if c >= 1:
            yield r, c - 1  # left

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = collections.deque()
        fresh_oranges = set()

        # enqueue all the rotten apples initially
        # also track all fresh oranges
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges.add((row, col))

        if not queue and not fresh_oranges:
            return 0
        elif not queue and fresh_oranges:
            return -1

        minutes = 0

        while queue:

            level_count = len(queue)

            # empty the queue, this represents one level / minute
            for i in range(level_count):

                r, c = queue.popleft()

                grid[r][c] = 2

                if (r, c) in fresh_oranges:
                    fresh_oranges.remove((r, c))

                if not fresh_oranges:
                    return minutes

                # enqueue the neighbouring fresh oranges
                for n_row, n_col in self.get_neighbours(r, c, rows, cols):
                    if grid[n_row][n_col] == 1:
                        queue.append((n_row, n_col))

            minutes += 1

        return -1
