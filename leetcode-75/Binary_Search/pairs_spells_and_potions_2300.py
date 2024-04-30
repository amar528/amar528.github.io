from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        result = []  # count for each successful spell

        potions.sort()

        # for each spell, find the potion with the minimum value that satisfies success
        m = len(potions)

        for spell in spells:

            left = 0
            right = m - 1
            leftmost_idx = m

            while left <= right:
                mid = (left + right) // 2

                if spell * potions[mid] >= success:
                    leftmost_idx = mid
                    # now try smaller
                    right = mid - 1
                else:
                    # too small
                    left = mid + 1

            successful_potions = m - leftmost_idx
            result.append(successful_potions)

        return result
