class Solution:
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')

        lst = list(s)

        start = 0
        end = len(s) - 1

        while start < end:
            if lst[start] not in vowels:
                start += 1
            elif lst[end] not in vowels:
                end -= 1
            else:
                self.swap(lst, start, end)
                start +=1
                end -= 1

        return ''.join(lst)

    def swap(self, lst, start, end):
        tmp = lst[start]
        lst[start] = lst[end]
        lst[end] = tmp


sol = Solution()
print(sol.reverseVowels('hello'))
print(sol.reverseVowels('leetcode'))  # leotcede
