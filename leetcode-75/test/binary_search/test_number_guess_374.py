from unittest import TestCase

from leetcode75.binary_search.number_guess_374 import Solution


class TestSolution(TestCase):
    def test_guess_number_example1(self):
        guess = 6
        sol = Solution(guess)
        result = sol.guessNumber(10)
        self.assertEqual(guess, result)

    def test_guess_number_example2(self):
        guess = 1
        sol = Solution(guess)
        result = sol.guessNumber(1)
        self.assertEqual(guess, result)

    def test_guess_number_example3(self):
        guess = 2
        sol = Solution(guess)
        result = sol.guessNumber(2)
        self.assertEqual(guess, result)

    def test_guess_number_example4(self):
        guess = 50
        sol = Solution(guess)
        result = sol.guessNumber(1000)
        self.assertEqual(guess, result)

    def test_guess_number_example5(self):
        guess = 1702766719
        sol = Solution(guess)
        result = sol.guessNumber(2126753390)
        self.assertEqual(guess, result)