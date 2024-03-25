from unittest import TestCase

from rplife.patterns import Pattern


class TestPatterns(TestCase):
    def test_pattern(self):
        under_test = Pattern('pattern', {(2, 0), (2, 1), (2, 2)})
        self.assertEqual('pattern', under_test.name)
        self.assertIsNotNone(under_test.alive_cells)
        self.assertEqual(3, len(under_test.alive_cells))
        self.assertSetEqual({(2, 0), (2, 1), (2, 2)}, under_test.alive_cells)
