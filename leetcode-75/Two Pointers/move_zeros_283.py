from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        if n <= 1:
            return

        i = j = 0
        while i < n:
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)
            else:
                j += 1
            i += 1







