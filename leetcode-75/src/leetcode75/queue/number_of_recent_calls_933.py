import collections


class RecentCounter:

    def __init__(self):
        self.threshold = 3000
        self.q = collections.deque()

    def age_requests(self, t):
        # pop all elements whose value is older than t - threshold
        while self.q[0] < (t - self.threshold):
            self.q.popleft()
            
    def ping(self, t: int) -> int:
        self.q.append(t)
        self.age_requests(t)

        return len(self.q)
