class Solution:

    def grp_len(self, group_length):
        if group_length > 9:
            return [int(i) for i in str(group_length)]
        else:
            return [group_length]

    def compress(self, chars):

        #  for single length list, simply return 1 and leaved unaltered
        if len(chars) == 1:
            print(chars)
            return 1

        # Keep track of the group length and the current matching character
        group_length = 0
        curr_match = chars[0]  # starting with the first character

        for i, c in enumerate(chars):

            if c == curr_match:
                group_length += 1

                print(f'matched existing char {c} index {i} group length is {group_length} chars is {chars}')
                #  if this is the last character in the array
                if i == len(chars) - 1:
                    #  delete the 'duplicate' chars
                    print(f'this is the last char at index {i}')
                    for d in range(i, i - group_length + 1, -1):
                        print(f'deleting char at index {d} chars is {chars}')
                        del chars[d]
                    print(f'chars before {chars}')
                    # append the group length, 1 digit per 0-9 values
                    for g in self.grp_len(group_length):
                        print(f'appending group length {g}')
                        chars.append(str(g))
                    print(f'chars after {chars}')

            else:
                # we found a new character, so terminate this group length if it is > 1
                curr_match = c
                print(f'terminating group at index {i} chars {chars}')
                if group_length > 1:
                    for d in range(i - group_length, i - 1):
                        print(f'deleting char at {d} chars is {chars}')
                        del chars[d]
                    print(f'chars before {chars}')
                    grp_chars = self.grp_len(group_length)
                    idx = i - 1
                    for g in grp_chars:
                        print(f'inserting {g} at index {idx}')
                        chars.insert(idx, str(g))
                        idx += 1
                    print(f'chars after {chars}')
                    #  reset the group length
                    group_length = 1
                    print('')

        print(chars)
        return len(chars)


sol = Solution()

# print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))  # ["a","2","b","2","c","3"] 6
# print(sol.compress(["a"]))  # ['a'] 1
# print(sol.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))  # ["a","b","1","2"] 4
print(sol.compress(["a", "a", "a", "b", "b", "a", "a"]))
