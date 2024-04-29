from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n <= 0:
            return [0]

        result = []
        for num in range(n + 1):
            b = bin(num)
            result.append(b.count('1'))

        return result
