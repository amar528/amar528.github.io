from unittest import TestCase

from ransom_note_383 import Solution


class TestSolution(TestCase):
    def test_can_construct_example1(self):
        ransom_note = "a"
        magazine = "b"

        sol = Solution()
        result = sol.canConstruct(ransom_note, magazine)

        self.assertFalse(result)

    def test_can_construct_example2(self):
        ransom_note = "aa"
        magazine = "ab"

        sol = Solution()
        result = sol.canConstruct(ransom_note, magazine)

        self.assertFalse(result)

    def test_can_construct_example3(self):
        ransom_note = "aa"
        magazine = "aab"

        sol = Solution()
        result = sol.canConstruct(ransom_note, magazine)

        self.assertTrue(result)
