import collections


class Solution:

    def decodeString(self, s: str) -> str:

        stack = collections.deque()

        for c in s:

            if c == ']':

                # pop from the stack until the corresponding open bracket '['
                sub_string = ''
                while stack[-1] != '[':
                    sub_string = stack.pop() + sub_string

                # also pop the closing bracket
                stack.pop()

                # pop the digits
                digits = ''
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits

                # push back to the stack in the expanded form
                stack.append(sub_string * int(digits))

            else:
                stack.append(c)

        return ''.join(stack)
