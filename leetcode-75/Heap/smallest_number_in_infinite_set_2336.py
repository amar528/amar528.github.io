import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        heapq.heappush(self.heap, 1)

    def popSmallest(self) -> int:
        val = heapq.heappop(self.heap)
        if not self.heap:
            heapq.heappush(self.heap, val + 1)
        return val

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)
