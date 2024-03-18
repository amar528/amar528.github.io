import sys


def merge_the_tools(s, k):
    n = len(s)
    if n % k != 0:
        print('Invalid K value')
        sys.exit(1)

    for i in range(0, n, k):
        # n/k sub strings
        sub = s[i:i + k]
        removed_duplicates = dict.fromkeys(sub)
        print(''.join(removed_duplicates.keys()))


if __name__ == '__main__':
    string, _k = input(), int(input())
    merge_the_tools(string, _k)
