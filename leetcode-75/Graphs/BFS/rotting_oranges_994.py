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

        minutes = -1  # start at -1

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

        while queue:

            to_add = []
            # empty the queue, this represents one level / minute
            while len(queue) > 0:
                r, c = queue.popleft()
                to_add.append((r, c))
                grid[r][c] = 2
                if (r, c) in fresh_oranges:
                    fresh_oranges.remove((r, c))

            minutes += 1

            # enqueue the neighbouring fresh oranges
            for r, c in to_add:
                for n_row, n_col in self.get_neighbours(r, c, rows, cols):
                    if grid[n_row][n_col] == 1:
                        queue.append((n_row, n_col))

        if fresh_oranges:
            return -1

        return minutes
