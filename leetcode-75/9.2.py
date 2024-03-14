class Solution:
    def compress(self, chars):
        print(chars)
        _dict = {}

        for c in chars:
            val = _dict.get(c, -1)
            if val == -1:
                _dict[c] = 1
            else:
                _dict[c] += 1

        del chars[:]

        for k, v in _dict.items():
            chars.append(k)
            if v > 1:
                for s in str(v):
                    chars.append(s)

        print(chars)
        return len(chars)


sol = Solution()

print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))  # ["a","2","b","2","c","3"] 6
print(sol.compress(["a"]))  # ['a'] 1
print(sol.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))  # ["a","b","1","2"] 4
print(sol.compress(["a", "a", "a", "b", "b", "a", "a"]))
