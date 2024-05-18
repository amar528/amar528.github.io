from unittest import TestCase

from leetcode75.stack.remove_stars_from_string_2390 import Solution


class TestSolution(TestCase):
    def test_remove_stars_example1(self):
        s = "leet**cod*e"

        sol = Solution()
        result = sol.removeStars(s)

        self.assertEqual('lecoe', result)

    def test_remove_stars_example2(self):
        s = "erase*****"

        sol = Solution()
        result = sol.removeStars(s)

        self.assertEqual('', result)
