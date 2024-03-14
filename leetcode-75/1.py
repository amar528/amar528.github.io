class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''

        _len1 = len(word1)
        _len2 = len(word2)
        _max = max(_len1, _len2)

        for i in range(0, _max):
            if i < _len1:
                result += word1[i]
            if i < _len2:
                result += word2[i]

        return result


s = Solution()
print(s.mergeAlternately('abc', 'pqr'))
print(s.mergeAlternately('ab', 'pqrs'))
