import string
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s.strip()) == 0:
            return True

        pattern = re.compile('[\W_]+')
        alpha_numeric = pattern.sub('', s)
        rev = ''.join(reversed(alpha_numeric.lower()))
        return alpha_numeric.lower() == rev
