import collections
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        n = len(nums)
        ranges = []

        i = 0
        while i < n:
            j = i + 1 if i < n - 1 else n - 1
            start = nums[i]
            end = nums[i]

            while j < n and nums[j] - nums[j - 1] == 1:
                end += 1
                j += 1
                i += 1

            ranges.append((start, end))
            i += 1

        return list(map(lambda t: str(t[0]) + '->' + str(t[1]) if t[0] != t[1] else str(t[0]), ranges))
