from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        answer[0] = list(nums1_set.difference(nums2_set))
        answer[1] = list(nums2_set.difference(nums1_set))

        return answer
