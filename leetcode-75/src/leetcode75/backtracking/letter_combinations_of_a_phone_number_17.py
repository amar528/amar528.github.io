from typing import List


class Solution:

    def __init__(self):
        self.mappings = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []

        def backtrack(i, s):
            # base case if we have reached the desired string length
            if i == len(digits):
                result.append(s)
                return result

            # recurse for each mapping for the current digit at i
            for c in self.mappings[digits[i]]:
                backtrack(i + 1, s + c)

            return result

        # start with index 0, and empty string
        return backtrack(0, "")
