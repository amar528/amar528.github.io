from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        if n == 1:
            return n

        start = 0

        while start < n:
            end = start + 1
            count = 1

            while end < len(chars) and chars[end] == chars[start]:
                count += 1
                end += 1

            if 1 < count < 10:

                chars[start + 1] = str(count)
                del chars[start + 2:end]
                end -= (end - (start + 2))

            elif 1 < count >= 10:
                digits = 0
                count_chars = str(count)
                for c in count_chars:
                    digits += 1
                    chars[start + digits] = c

                del chars[start + digits + 1:end]
                end -= (end - (start + digits))

            start = end

        return len(chars)
