from unittest import TestCase

from journey_to_the_moon import journeyToMoon


class Test(TestCase):
    def test_journey_to_moon_4_2pairs(self):
        n = 4
        astronauts = [[1, 2], [2, 3]]

        result = journeyToMoon(n, astronauts)

        self.assertEqual(3, result)

    def test_journey_to_moon_case0(self):
        n = 5
        astronauts = [[0, 1], [2, 3], [0, 4]]

        result = journeyToMoon(n, astronauts)

        self.assertEqual(6, result)

    def test_journey_to_moon_case1(self):
        n = 10
        astronauts = [
                      [0, 2],
                      [1, 8],
                      [1, 4],
                      [2, 8],
                      [2, 6],
                      [3, 5],
                      [6, 9]]

        result = journeyToMoon(n, astronauts)

        self.assertEqual(23, result)
