import collections


class Solution:
    opening_brackets = {'(', '[', '{'}

    open_to_close = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    close_to_open = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    def isValid(self, s: str) -> bool:
        n = len(s)

        if n % 2 != 0:
            return False

        stack = collections.deque()

        for c in s:
            # opening brackets expected closing match are put on the stack
            if c in self.opening_brackets:
                stack.append(self.open_to_close[c])
            else:
                # close bracket, check it matches the stack
                if not stack:
                    return False

                expected_close = stack.pop()
                if c != expected_close:
                    return False

        # any elements remaining on the stack mean we have non matching brackets
        if stack:
            return False

        return True
