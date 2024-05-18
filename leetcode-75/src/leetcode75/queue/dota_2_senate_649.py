import collections


class Solution:

    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)

        # separate queue for D and R senators
        d_queue = collections.deque()
        r_queue = collections.deque()

        # enqueue each to their own queue
        # use the index as the value
        for i, senator in enumerate(senate):
            if senator == "D":
                d_queue.append(i)
            else:
                r_queue.append(i)

        # process both queues
        while d_queue and r_queue:

            d_senator = d_queue.popleft()
            r_senator = r_queue.popleft()

            # the lowest value has priority
            # the successful senator is added to the back of the queue with the correct offset
            # the unsuccessful senator is dropped from the next round
            if d_senator < r_senator:
                d_queue.append(d_senator + n)
            else:
                r_queue.append(r_senator + n)

        # the winning team will be non empty
        if d_queue:
            return "Dire"
        else:
            return "Radiant"
