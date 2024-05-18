class Solution:
    def uniquePaths(self, m, n):

        # bottom row, each cell only has one way of reaching the end,
        # i.e. you can only move right
        previous_row = [1] * n
        # the current row we are calculating
        current_row = [1] * n

        # we compute the row above by going in reverse and
        # summing for each cell, that to the right and down (previous row)
        for i in range(m - 1):
            # the last column will also only ever be 1, as you can only move down
            for j in range(n - 2, -1, -1):
                current_row[j] = current_row[j + 1] + previous_row[j]
            # update the previous row
            previous_row = current_row

        # now we can return the value at [0] which has all the possible ways of travelling to the end
        return current_row[0]

# Pascals Triangle mathematical approach
# return factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1)
