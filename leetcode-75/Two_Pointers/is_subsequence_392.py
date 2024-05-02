class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == t or s == "":
            return True

        count = len(s)
        idx = 0

        for i in range(len(t)):

            if t[i] == s[idx]:
                # a match is found, so reduce the count and move to the next index to be checked
                count -= 1
                idx += 1

            # if we have matched all chars of s then we are done
            if count == 0:
                return True

        return False
