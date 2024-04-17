from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        if n == 1:
            return nums[0] / k

        if k == 1:
            return max(nums) / k

        i = 0
        j = i + k - 1

        max_so_far = sum(nums[i:j + 1])

        j += 1
        presum = 0
        postsum = 0

        while j <= n - 1:
            presum += nums[i]
            postsum += nums[j]
            test = max_so_far
            test -= presum
            test += postsum

            if test > max_so_far:
                max_so_far = test
                presum = 0
                postsum = 0

            i += 1
            j += 1

        return round((max_so_far / k), 5)
