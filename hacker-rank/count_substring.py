import re


# ABCDCDC
# CDC

def count_substring(string, sub_string):
    count = 0

    n = len(string)
    m = len(sub_string)

    for i in range(n):
        j = i + m
        if j <= n:
            t = string[i:j]
            if t == sub_string:
                count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
