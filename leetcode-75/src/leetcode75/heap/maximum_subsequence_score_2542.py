import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # min heap to store values from n1
        # we use this to decide which value to remove when we are trying
        # a new element, and we have exceeded k elements
        min_heap = []

        # we want to maximize the values from nums2
        # so we will sort the pairs of n1, n2 in descending order by n2
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs.sort(key=lambda v: v[1], reverse=True)

        max_score = 0
        n1_total = 0

        for n1, n2 in pairs:

            n1_total += n1
            heapq.heappush(min_heap, n1)

            if len(min_heap) > k:
                # pop and subtract n1 value from total
                n1_removed = heapq.heappop(min_heap)
                n1_total -= n1_removed

            if len(min_heap) == k:
                # reached k so calculate our max so far
                max_score = max(max_score, n1_total * n2)

        return max_score
