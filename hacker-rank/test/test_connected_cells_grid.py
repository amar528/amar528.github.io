from unittest import TestCase

from connected_cells_grid import get_largest_region


class Test(TestCase):
    def test_get_largest_region_4by4(self):
        grid = [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0]
        ]

        result = get_largest_region(grid)
        self.assertEqual(5, result)

    def test_get_largest_region_5by5(self):
        grid = [
            [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1]
        ]

        result = get_largest_region(grid)
        self.assertEqual(5, result)
