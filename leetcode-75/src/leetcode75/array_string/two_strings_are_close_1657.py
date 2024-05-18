import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) == set(word2):
            # they both contain the same set of chars

            # we need to check the list of frequencies match
            # one could be replaced by the other, to replace chars
            values1 = collections.Counter(word1).values()
            values2 = collections.Counter(word2).values()
            return sorted(list(values1)) == sorted(list(values2))

        return False
