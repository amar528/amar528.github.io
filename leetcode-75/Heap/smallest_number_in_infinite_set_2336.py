import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

        self.sequence = 1
        heapq.heappush(self.heap, self.sequence)

    def popSmallest(self) -> int:

        if self.heap:
            return heapq.heappop(self.heap)
        else:
            self.sequence += 1
            return self.sequence

    def addBack(self, num: int) -> None:
        if num not in self.heap and num <= self.sequence:
            heapq.heappush(self.heap, num)

