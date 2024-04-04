from unittest import TestCase

from prep_kit_1week.day_3 import find_zig_zag_sequence, caesar_cypher, tower_breakers, palindrome_index


class Test(TestCase):
    def test_find_zig_zag_sequence_case0(self):
        a = [1, 2, 3, 4, 5, 6, 7]
        n = len(a)
        result = find_zig_zag_sequence(a, n)
        self.assertListEqual([1, 2, 3, 7, 6, 5, 4], result)

    def test_tower_breakers_case0(self):
        num_towers = 2
        tower_height = 6
        result = tower_breakers(num_towers, tower_height)
        self.assertEqual(2, result)

    def test_tower_breakers_case1(self):
        num_towers = 2
        tower_height = 6
        result = tower_breakers(num_towers, tower_height)
        self.assertEqual(2, result)

    def test_caesar_cypher_case0(self):
        s = 'middle-Outz'
        k = 2
        result = caesar_cypher(s, k)
        self.assertEqual('okffng-Qwvb', result)

    def test_caesar_cypher_case3(self):
        s = 'www.abc.xy'
        k = 87
        result = caesar_cypher(s, k)
        self.assertEqual('fff.jkl.gh', result)

    def test_pali_index_case0(self):
        s = 'bcbc'
        result = palindrome_index(s)
        self.assertEqual(0, result)

    def test_pali_index_case1(self):
        s = 'aaab'
        result = palindrome_index(s)
        self.assertEqual(3, result)

    def test_pali_index_case2(self):
        s = 'baa'
        result = palindrome_index(s)
        self.assertEqual(0, result)

    def test_pali_index_case3(self):
        s = 'aaa'
        result = palindrome_index(s)
        self.assertEqual(-1, result)
