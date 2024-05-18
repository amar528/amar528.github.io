import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr)

        count_set = set()
        for count in counts.values():
            if count in count_set:
                return False
            count_set.add(count)

        return True
