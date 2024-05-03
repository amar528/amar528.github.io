from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        if n == 1:
            return n

        start = 0

        # main loop, whilst the start position is valid
        while start < n:

            # find the end position, that is up to the next differing character
            # also find the number of occurrences of the current character
            end = start + 1
            count = 1

            while end < len(chars) and chars[end] == chars[start]:
                count += 1
                end += 1

            # if we need to compress (character count is greater than 1)
            if count > 1:

                # how many digits do we need to append
                digits = 0
                count_chars = str(count)

                # append each digit following the character
                for c in count_chars:
                    digits += 1
                    chars[start + digits] = c

                # delete the remaining duplicate characters after the digits
                del chars[start + digits + 1:end]

                # update the new end position
                end -= (end - (start + digits + 1))

            # reset the new starting position
            start = end

        return len(chars)
