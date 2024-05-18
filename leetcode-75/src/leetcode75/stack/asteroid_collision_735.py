from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for a in asteroids:

            # while a is moving left and the top of the stack is moving right
            while a < 0 and stack and stack[-1] > 0:
                diff = a + stack[-1]

                # get the difference between the 2 asteroids
                if diff < 0:
                    # top of stack is destroyed
                    stack.pop()
                elif diff > 0:
                    # a is destroyed, set it to 0
                    a = 0
                else:
                    # equal - both disappear
                    a = 0
                    stack.pop()

            # push a onto stack if it is non-zero
            if a:
                stack.append(a)

        return stack
