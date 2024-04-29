class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == t or s == "":
            return True

        count = len(s)
        idx = 0

        for i in range(len(t)):

            if t[i] == s[idx]:
                count -= 1
                idx += 1

            if count == 0:
                return True

        return False
