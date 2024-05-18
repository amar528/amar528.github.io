from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        if n == 1:
            return nums[0] / k

        if k == 1:
            return max(nums) / k

        left = 0
        right = left + k

        # our initial subarray sum window
        max_so_far = sum(nums[left:right])

        pre_sum = 0
        post_sum = 0

        while right <= n - 1:
            pre_sum += nums[left]
            post_sum += nums[right]

            test = max_so_far
            test -= pre_sum
            test += post_sum

            if test > max_so_far:
                max_so_far = test
                pre_sum = 0
                post_sum = 0

            left += 1
            right += 1

        return round((max_so_far / k), 5)
