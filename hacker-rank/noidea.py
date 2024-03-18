import sys

n, m = map(int, input().split())

arr = list(map(int, input().split()))
if len(arr) != n:
    print('Invalid elements length')
    sys.exit(1)

a = set(map(int, input().split()))
if len(a) != m:
    print('Invalid set A length')
    sys.exit(1)

b = set(map(int, input().split()))
if len(b) != m:
    print('Invalid set B length')
    sys.exit(1)

happiness = 0

for i in arr:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1

print(happiness)
