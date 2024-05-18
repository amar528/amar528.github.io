from unittest import TestCase

from leetcode75.stack.asteroid_collision_735 import Solution


class TestSolution(TestCase):
    def test_asteroid_collision_example1(self):
        asteroids = [5, 10, -5]

        sol = Solution()
        result = sol.asteroidCollision(asteroids)

        self.assertListEqual([5, 10], result)

    def test_asteroid_collision_example2(self):
        asteroids = [8, -8]

        sol = Solution()
        result = sol.asteroidCollision(asteroids)

        self.assertListEqual([], result)

    def test_asteroid_collision_example3(self):
        asteroids = [10, 2, -5]

        sol = Solution()
        result = sol.asteroidCollision(asteroids)

        self.assertListEqual([10], result)

    def test_asteroid_collision_example4(self):
        asteroids = [-2, -1, 1, 2]

        sol = Solution()
        result = sol.asteroidCollision(asteroids)

        self.assertListEqual([-2, -1, 1, 2], result)

    def test_asteroid_collision_example5(self):
        asteroids = [-2, -2, 1, -2]

        sol = Solution()
        result = sol.asteroidCollision(asteroids)

        self.assertListEqual([-2, -2, -2], result)

    def test_asteroid_collision_example6(self):
        asteroids = [-2, -2, -1, -2]

        sol = Solution()
        result = sol.asteroidCollision(asteroids)

        self.assertListEqual([-2, -2, -1, -2], result)
