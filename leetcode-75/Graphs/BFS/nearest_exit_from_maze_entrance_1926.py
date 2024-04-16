import collections
from typing import List


class Solution:

    def get_all_next_steps(self, step):
        next_steps = []

        curr_row = step[0]
        curr_col = step[1]

        # up
        next_steps.append([curr_row - 1, curr_col])
        # down
        next_steps.append([curr_row + 1, curr_col])
        # left
        next_steps.append([curr_row, curr_col - 1])
        # right
        next_steps.append([curr_row, curr_col + 1])

        return next_steps

    def is_valid(self, step, maze):
        row = step[0]
        col = step[1]

        # check bounds
        if row < 0 or row >= len(maze):
            return False
        if col < 0 or col >= len(maze[row]):
            return False

        # check for wall
        if maze[row][col] == '+':
            return False

        return True

    def is_exit(self, step, maze, entrance):
        row = step[0]
        col = step[1]

        # must be an empty cell
        if maze[row][col] != '.':
            return False

        # must not be the entrance
        if step == entrance:
            return False

        # must be on the border of the maze
        if ((row == 0 or row == len(maze) - 1)
                or (col == 0 or col == len(maze[row]) - 1)):
            return True

        return False

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = collections.deque([(-1, entrance)])
        visited = []

        while queue:
            step_count, step = queue.popleft()

            if step in visited:
                continue

            visited.append(step)

            step_count += 1

            if self.is_exit(step, maze, entrance):
                return step_count

            for next_step in self.get_all_next_steps(step):
                if next_step not in visited and self.is_valid(next_step, maze):
                    queue.append((step_count, next_step))

        return -1
