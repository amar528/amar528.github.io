from collections import defaultdict


class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern

    # determine the cells that will pass to the next generation as living cells
    def evolve(self):
        # check currently alive cells and their neighbours
        # to determine the number of neighbours
        # decide which cells stay alive, which die, which comes alive

        # 1. alive cells die IF they have:
        #   < 2 living neighbours (underpopulation
        #   > 3 living neighbours (overpopulation)
        # 2. alive cells stay alive IF they have:
        #   2 OR 3 living neighbours
        # 3. dead cells become alive IF they have:
        #   exactly 3 living neighbours (reproduction)

        # the neighbours of a given cell (1,1) are defined as:
        neighbours = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # default dict with int type
        neighbour_count = defaultdict(int)

        # increment the deltas of the neighbours for each alive cell
        for row, col in self.pattern.alive_cells:
            for n_row, n_col in neighbours:
                key = (row + n_row, col + n_col)
                neighbour_count[key] += 1

        # determine the set of cells to stay alive (2 or 3 alive neighbours)
        # intersect with the set of alive cells
        stay_alive = {cell for cell, alive_count in neighbour_count.items()
                      if alive_count in {2, 3}} & self.pattern.alive_cells

        # determine the set of cells that will come alive (exactly 3 alive neighbours)
        # union with the set of alive cells

        come_alive = {cell for cell, alive_count in neighbour_count.items()
                      if alive_count == 3} - self.pattern.alive_cells

        # alive cells = union of cells that stay alive and come alive
        self.pattern.alive_cells = stay_alive | come_alive


def as_string(self, bbox):
    pass


def __str__(self):
    return (f'Pattern: {self.pattern.name}\n'
            f'Alive Cells: {sorted(self.pattern.alive_cells)}')
