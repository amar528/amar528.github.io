from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # initialise result as all 0's
        result = [0] * (n + 1)

        # iterate from 0 to n, inclusive
        for num in range(n + 1):
            _shift_idx = num >> 1
            _shift = result[_shift_idx]

            _and = (num & 1)

            result[num] = _shift + _and

        return result
