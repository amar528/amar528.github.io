class Solution:
    def compress(self, chars):
        n = len(chars)
        current_idx = write_idx = 0

        while current_idx < n:
            counter = 0
            current_char = chars[current_idx]

            while current_idx < n and chars[current_idx] == current_char:
                counter += 1
                current_idx += 1

            chars[write_idx] = current_char
            write_idx += 1

            if counter > 1:
                for s in str(counter):
                    chars[write_idx] = s
                    write_idx += 1

        chars = chars[:write_idx]
        return len(chars)


sol = Solution()

print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))  # ["a","2","b","2","c","3"] 6
print(sol.compress(["a"]))  # ['a'] 1
print(sol.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))  # ["a","b","1","2"] 4
print(sol.compress(["a", "a", "a", "b", "b", "a", "a"]))
