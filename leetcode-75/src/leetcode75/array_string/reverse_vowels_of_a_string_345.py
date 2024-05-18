class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'a', 'e', 'i', 'o', 'u'}

        arr = list(s)
        n = len(arr)
        left = 0
        right = n - 1

        while left < right:

            while left < n and arr[left].lower() not in vowels:
                left += 1

            while right > 0 and arr[right].lower() not in vowels:
                right -= 1

            if left < right:
                arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        return ''.join(arr)
