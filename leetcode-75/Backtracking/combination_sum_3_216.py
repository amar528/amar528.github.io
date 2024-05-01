from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(current, total, start):

            # if we have reached the target length then stop
            if k == len(current):

                # append result if successfully reached the target
                if total == n:
                    result.append(current.copy())
                return

            # for the remaining digits
            for dig in range(start, 10):
                # store this digit in a new copy for our current combination
                new_current = current.copy()
                new_current.append(dig)

                # recurse with this new combination, total and next starting number
                backtrack(new_current, total + dig, dig + 1)

        # start backtracking, empty current and start at 1
        backtrack([], 0, 1)

        return result
