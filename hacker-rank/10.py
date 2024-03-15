import itertools
import sys

k, m = map(int, input().split())
i_lists = []
for _ in range(k):
    i_list = list(map(int, input().split()))
    i_len = i_list[0]
    if i_len != len(i_list) - 1:
        print(f'Invalid line: {i_list}', sys.stderr)
        sys.exit(1)
    i_lists.append(i_list[1:])

possibles = itertools.product(*i_lists)

moduli = [sum(map(lambda x: int(x) ** 2, possible)) % m for possible in possibles]
print(max(moduli))
