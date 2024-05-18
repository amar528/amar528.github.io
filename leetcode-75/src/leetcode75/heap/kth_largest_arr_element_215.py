import heapq


class Solution:
    def findKthLargest(self, nums, k):
        heap = [-num for num in nums]
        heapq.heapify(heap)

        val = None
        for i in range(k):
            val = heapq.heappop(heap)

        return -val
