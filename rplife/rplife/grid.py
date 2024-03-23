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

        pass

    def as_string(self, bbox):
        pass

    def __str__(self):
        pass
