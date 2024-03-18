import sys

n = int(input())

words = []
for _ in range(n):
    words.append(input())

if len(words) != n:
    print('Invalid number of words', sys.stderr)
    sys.exit(1)

cache = {}

for w in words:
    count = cache.get(w, 0)
    count += 1
    cache[w] = count

print(len(cache.keys()))

for count in cache.values():
    print(count, end='')
    print(' ', end='')
