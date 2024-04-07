from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        note_counter = Counter(ransomNote)
        common = note_counter & magazine_counter
        return common == note_counter
