class Solution:

    def gcd(self, a, b):

        # once a has reached zero, b is the gcd
        if a == 0:
            return b

        # otherwise, recurse with a = b mod a, b = a
        return self.gcd(b % a, a)

    def divides(self, n, s, gcd, prefix):
        if s == prefix:
            return True
        elif len(prefix) == n:
            return False

        start = 0
        end = gcd
        while end <= n:
            if s[start:end] != prefix:
                return False
            start += gcd
            end += gcd
        return True

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if not str1 or not str2:
            return ""

        # get the gcd length of both strings
        length_1 = len(str1)
        length_2 = len(str2)

        gcd = self.gcd(length_1, length_2)
        prefix = str1[:gcd]

        if self.divides(length_1, str1, gcd, prefix) and self.divides(length_2, str2, gcd, prefix):
            return str1[:gcd]

        return ""
