# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:

    def __init__(self, val):
        self.val = val

    def guess(self, g):
        if g == self.val:
            return 0

        if g > self.val:
            return -1
        elif g < self.val:
            return 1

    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:
            mid = l + (r - l) // 2
            response = self.guess(mid)

            if response == 0:
                return mid
            elif response < 0:
                # too high
                r = mid - 1
            elif response > 0:
                # too low
                l = mid + 1
