from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)

        if n == 2:
            if 0 in height:
                return 0
            else:
                return 1

        max_vol_found = 0

        for i, v in enumerate(height):

            for j in reversed(range(i + 1, n)):
                distance = j - i
                u = height[j]

                vol = distance * min(v, u)
                # print(f'vol for {v} - {u} : {vol}')
                max_vol_found = max(max_vol_found, vol)

        return max_vol_found
