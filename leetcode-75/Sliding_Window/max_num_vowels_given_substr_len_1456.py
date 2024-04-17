from collections import Counter
from functools import reduce


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        n = len(s)
        left = 0
        right = left + k
        max_count = 0

        while right <= n:
            sub_string = s[left:right]
            counter = Counter(sub_string)

            vowel_count = sum(map(lambda item: item[1] if item[0] in vowels else 0, counter.items()))

            max_count = max(max_count, vowel_count)

            left += 1
            right += 1

        return max_count
