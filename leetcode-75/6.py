class Solution:
    def reverseWords(self, s):
        words = s.split(' ')
        result = []
        i = len(words) - 1
        while i >= 0:
            w = words[i]
            w.strip()
            if w:
                result.append(w)
            i -= 1
        return ' '.join(result).strip()


sol = Solution()
# print(sol.reverseWords("the sky is blue"))
print(sol.reverseWords("a good   example"))
