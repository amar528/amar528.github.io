import collections


class Solution:

    def decodeString(self, s: str) -> str:

        stack = collections.deque()

        current_string = ''
        current_count = 0

        for c in s:

            if c == '[':
                # add to the stack and reset
                stack.append(current_string)
                stack.append(current_count)
                current_string = ''
                current_count = 0

            elif c == ']':
                # pop from the top of the stack
                prev_count = stack.pop()
                prev_string = stack.pop()

                # prepend to current string
                current_string = prev_string + prev_count * current_string

            elif c.isdigit():
                # update the current count
                current_count = current_count * 10 + int(c)
            else:
                # simply append the character
                current_string += c

        return current_string
