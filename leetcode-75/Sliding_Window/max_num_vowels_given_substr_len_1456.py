from collections import Counter


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        n = len(s)
        left = 0
        right = left + k

        sub_string = s[left:right]
        counter = Counter(sub_string)
        max_so_far = sum(map(lambda item: item[1] if item[0] in vowels else 0, counter.items()))

        # left += 1
        # right += 1
        max_count = max_so_far

        while right < n:
            if s[left] in vowels:
                max_count -= 1

            if s[right] in vowels:
                max_count += 1

            max_so_far = max(max_so_far, max_count)

            left += 1
            right += 1

        return max_so_far
