from unittest import TestCase
from leetcode75.queue.number_of_recent_calls_933 import RecentCounter


class TestRecentCounter(TestCase):
    def test_ping_example1(self):
        under_test = RecentCounter()

        result = under_test.ping(1)
        self.assertEqual(1, result)

        result = under_test.ping(100)
        self.assertEqual(2, result)

        result = under_test.ping(3001)
        self.assertEqual(3, result)

        result = under_test.ping(3002)
        self.assertEqual(3, result)

    def test_ping_example2(self):
        under_test = RecentCounter()

        result = under_test.ping(642)
        self.assertEqual(1, result)

        result = under_test.ping(1849)
        self.assertEqual(2, result)

        result = under_test.ping(4921)
        self.assertEqual(1, result)

        result = under_test.ping(5936)
        self.assertEqual(2, result)

        result = under_test.ping(5957)
        self.assertEqual(3, result)
