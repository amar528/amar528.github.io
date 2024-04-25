class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len1 = len(word1)
        len2 = len(word2)

        # empty result of combined length
        result = ['' * (len1 + len2)]

        i = j = 0
        chars_left = i < len1 or j < len2

        while chars_left:

            if i < len1:
                result.append(word1[i])

            if j < len2:
                result.append(word2[j])

            i += 1
            j += 1

            chars_left = i < len1 or j < len2

        return ''.join(result)
