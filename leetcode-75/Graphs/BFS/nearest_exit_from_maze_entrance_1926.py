import collections
from typing import List


class Solution:

    def get_next_steps(self, step, maze):

        curr_row = step[0]
        curr_col = step[1]

        up = [curr_row - 1, curr_col]
        if self.is_valid(up, maze):
            yield up

        down = [curr_row + 1, curr_col]
        if self.is_valid(down, maze):
            yield down

        left = [curr_row, curr_col - 1]
        if self.is_valid(left, maze):
            yield left

        right = [curr_row, curr_col + 1]
        if self.is_valid(right, maze):
            yield right

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

        # entrance does not contribute to step count
        queue = collections.deque([(-1, entrance)])

        while queue:
            step_count, step = queue.popleft()

            # check visited steps / wall
            if maze[step[0]][step[1]] == '+':
                continue

            step_count += 1

            if self.is_exit(step, maze, entrance):
                return step_count

            # mark as visited
            maze[step[0]][step[1]] = '+'

            for next_step in self.get_next_steps(step, maze):
                queue.append((step_count, next_step))

        return -1
