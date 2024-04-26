class Solution:

    def tribonacci(self, n: int) -> int:
        tribs = [0, 1, 1]

        for n in range(3, n + 1):
            tribs.append(tribs[n - 3] + tribs[n - 2] + tribs[n - 1])

        return tribs[n]
