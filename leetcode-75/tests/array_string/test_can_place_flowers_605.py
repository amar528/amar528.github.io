from unittest import TestCase

from leetcode75.array_string.can_place_flowers_605 import Solution


class TestSolution(TestCase):
    def test_can_place_flowers_example1(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 1

        sol = Solution()
        result = sol.canPlaceFlowers(flowerbed, n)

        self.assertTrue(result)

    def test_can_place_flowers_example2(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 2

        sol = Solution()
        result = sol.canPlaceFlowers(flowerbed, n)

        self.assertFalse(result)

    def test_can_place_flowers_example3(self):
        flowerbed = [1, 0, 0, 0, 1, 0, 0]
        n = 2

        sol = Solution()
        result = sol.canPlaceFlowers(flowerbed, n)

        self.assertTrue(result)
