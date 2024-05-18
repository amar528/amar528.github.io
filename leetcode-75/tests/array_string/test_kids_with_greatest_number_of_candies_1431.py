from unittest import TestCase

from leetcode75.array_string.kids_with_greatest_number_of_candies_1431 import Solution


class TestSolution(TestCase):
    def test_kids_with_candies_example1(self):
        candies = [2, 3, 5, 1, 3]
        extra_candies = 3

        sol = Solution()
        result = sol.kidsWithCandies(candies, extra_candies)

        self.assertListEqual([True, True, True, False, True], result)

    def test_kids_with_candies_example2(self):
        candies = [4, 2, 1, 1, 2]
        extra_candies = 1

        sol = Solution()
        result = sol.kidsWithCandies(candies, extra_candies)

        self.assertListEqual([True, False, False, False, False], result)

    def test_kids_with_candies_example3(self):
        candies = [12, 1, 12]
        extra_candies = 10

        sol = Solution()
        result = sol.kidsWithCandies(candies, extra_candies)

        self.assertListEqual([True, False, True], result)
