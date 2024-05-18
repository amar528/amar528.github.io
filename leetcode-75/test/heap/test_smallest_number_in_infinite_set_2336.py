from unittest import TestCase

from leetcode75.heap.smallest_number_in_infinite_set_2336 import SmallestInfiniteSet


class TestSmallestInfiniteSet(TestCase):

    def test_example1(self):
        under_test = SmallestInfiniteSet()
        under_test.addBack(2)  # 2 is already in the set, so no change is made.

        v = under_test.popSmallest()  # return 1, since 1 is the smallest number, and remove it from the set.
        self.assertEqual(1, v)

        v = under_test.popSmallest()  # return 2, and remove it from the set.
        self.assertEqual(2, v)

        v = under_test.popSmallest()  # return 3, and remove it from the set.
        self.assertEqual(3, v)

        under_test.addBack(1)  # 1 is added back to the set.

        v = under_test.popSmallest()  # return 1, since 1 was added back to the set and is the smallest number
        # and remove it from the set.
        self.assertEqual(1, v)

        v = under_test.popSmallest()  # return 4, and remove it from the set.
        self.assertEqual(4, v)

        v = under_test.popSmallest()  # return 5, and remove it from the set.
        self.assertEqual(5, v)

    def test_example2(self):
        under_test = SmallestInfiniteSet()

        v = under_test.popSmallest()
        self.assertEqual(1, v)

        under_test.addBack(1)

        v = under_test.popSmallest()
        self.assertEqual(1, v)

        v = under_test.popSmallest()
        self.assertEqual(2, v)

        v = under_test.popSmallest()
        self.assertEqual(3, v)

        under_test.addBack(2)

        under_test.addBack(3)

        v = under_test.popSmallest()
        self.assertEqual(2, v)

        v = under_test.popSmallest()
        self.assertEqual(3, v)

    def test_example3(self):
        under_test = SmallestInfiniteSet()

        v = under_test.popSmallest()
        self.assertEqual(1, v)

        v = under_test.popSmallest()
        self.assertEqual(2, v)

        under_test.addBack(3)

        v = under_test.popSmallest()
        self.assertEqual(3, v)

        under_test.addBack(2)

        v = under_test.popSmallest()
        self.assertEqual(2, v)

        v = under_test.popSmallest()
        self.assertEqual(4, v)

    def test_example4(self):
        under_test = SmallestInfiniteSet()

        v = under_test.popSmallest()
        self.assertEqual(1, v)

        under_test.addBack(608)

        v = under_test.popSmallest()
        self.assertEqual(2, v)

        under_test.addBack(4)

        v = under_test.popSmallest()
        self.assertEqual(3, v)

        under_test.addBack(384)
        under_test.addBack(975)
        under_test.addBack(692)
