from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        length = len(flowerbed)

        # 1 empty space
        if length == 1:
            return n == 1 and flowerbed[0] == 0

        # the flowers to plant count
        count = n

        # O(n)
        for i in range(length):

            # keep track of left and right
            left = i - 1
            right = i + 1
            val = flowerbed[i]

            # empty start plot, right is also empty
            if i == 0 and val == 0 and flowerbed[right] == 0:
                flowerbed[i] = 1
                count -= 1

            # empty end plot, left is also empty
            elif i == len(flowerbed) - 1 and val == 0 and flowerbed[left] == 0:
                flowerbed[i] = 1
                count -= 1

            # empty plot, we have plots to the left and right (within bounds)
            # and they are both also empty
            elif (val == 0 and left >= 0 and right <= len(flowerbed) - 1
                  and flowerbed[left] == 0 and flowerbed[right] == 0):
                flowerbed[i] = 1
                count -= 1

            # exit early if we have planted all flowers
            if count == 0:
                return True

        return False
