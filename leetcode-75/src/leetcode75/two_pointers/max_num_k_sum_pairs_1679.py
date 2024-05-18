from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        n = len(nums)
        left = 0
        right = n - 1

        num_operations = 0
        nums.sort()

        while left < right:

            test = (nums[left] + nums[right])

            if k - test == 0:
                num_operations += 1
                left += 1
                right -= 1
            elif test > k:
                right -= 1
            else:
                left += 1

        return num_operations
