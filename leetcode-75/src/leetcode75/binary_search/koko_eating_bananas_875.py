from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k - eats k bananas per hour
        # find minimum k such that all piles are eaten within h hours

        # perform a binary search on all possible eating speeds
        # the range is (1, max(piles))
        # we will search for the minimum speed that results in all
        # piles being eaten
        min_speed = 1
        max_speed = max(piles)
        result = max_speed

        while min_speed <= max_speed:

            # eating speed is the mid value
            eating_speed = (min_speed + max_speed) // 2

            # given this speed, calculate the total hours it will take
            # to eat all piles of bananas
            hours_taken = 0
            for banana_pile in piles:
                # always round up to the nearest hour
                hours_taken += ceil(banana_pile / eating_speed)

            if hours_taken <= h:
                # we've eaten all bananas, so a valid speed was found
                # update the minimum result so far
                result = min(result, eating_speed)

                # try a lower speed (left half of array, move right pointer right <-- mid)
                max_speed = eating_speed - 1
            else:
                # try a faster speed (move left pointer  mid --> left)
                min_speed = eating_speed + 1

        return result
