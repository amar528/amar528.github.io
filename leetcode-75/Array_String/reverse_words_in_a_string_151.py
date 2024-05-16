class Solution:
    def reverseWords(self, s: str) -> str:

        if not s: return ''

        stack = []

        for sub in s.strip().split():
            stack.append(sub.strip())

        result = []
        while stack:
            result.append(stack.pop())
            result.append(' ')

        result.pop()

        return ''.join(result)
