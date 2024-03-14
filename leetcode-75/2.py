class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 == str2:
            return str1

        len1 = len(str1)
        len2 = len(str2)

        if len1 > len2:
            suffix1 = str1[len2-1:]
            for c in suffix1:
                if c not in str2:
                    return ""

        result = ''
        for i in range(0, min(len1, len2)):
            rlen = len(result)
            if rlen > 1 and len1 % rlen == 0 and len2 % rlen == 0:
                return result
            if str1[i] == str2[i]:
                result += str1[i]

        return result


sol = Solution()
print(sol.gcdOfStrings('ABCABC', 'ABC'))
print(sol.gcdOfStrings('ABABAB', 'ABAB'))
print(sol.gcdOfStrings('LEET', 'CODE'))
print(sol.gcdOfStrings('ABCDEC', 'ABC'))
