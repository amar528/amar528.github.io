from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        l = len(flowerbed)

        if l == 1:
            return n == 1 and flowerbed[0] == 0

        count = n

        for i in range(l):

            prev = i - 1
            after = i + 1

            val = flowerbed[i]

            # start
            if i == 0 and val == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count -= 1

            # end
            elif i == len(flowerbed) - 1 and val == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                count -= 1

            elif val == 0 and prev >= 0 and after <= len(flowerbed) - 1:
                if flowerbed[prev] == 0 and flowerbed[after] == 0:
                    flowerbed[i] = 1
                    count -= 1

            if count == 0:
                return True

        return False
