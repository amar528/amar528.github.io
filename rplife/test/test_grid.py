from unittest import TestCase, mock

from rplife.grid import LifeGrid
from rplife.patterns import Pattern


class TestGrid(TestCase):
    def test_evolve(self):
        mock_pattern = mock.Mock()
        mock_pattern.alive_cells = {(2,0), (2,1), (2,2)}

        under_test = LifeGrid(mock_pattern)
        under_test.evolve()

