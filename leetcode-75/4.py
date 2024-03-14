class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        _length = len(flowerbed)
        placed = 0

        for i in range(_length):
            curr_val = flowerbed[i]

            if curr_val == 0:

                if _length == 1:
                    return True

                _prev = i - 1
                _next = i + 1

                has_prev = _prev >= 0
                has_next = _next < _length

                if has_prev and has_next:
                    if flowerbed[_prev] == 0 and flowerbed[_next] == 0:
                        placed += 1
                        flowerbed[i] = 1

                if not has_prev and has_next:
                    if flowerbed[_next] == 0:
                        placed += 1
                        flowerbed[i] = 1

                if has_prev and not has_next:
                    if flowerbed[_prev] == 0:
                        placed += 1
                        flowerbed[i] = 1

        if placed >= n:
            return True

        return False


sol = Solution()
# print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # true
# print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # false
# print(sol.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))  # false
# print(sol.canPlaceFlowers([0, 0, 1, 0, 1], 1))  # true
# print(sol.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))  # true
# print(sol.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))  # false
# print(sol.canPlaceFlowers([0], 1))  # false
print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 1))  # false
