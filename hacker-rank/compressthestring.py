import itertools

s = input()

keys = groups = []
for k, g in itertools.groupby(s):
    keys.append(k)
    groups.append(list(g))

for i in range(0, len(groups) - 1, 2):
    print(f'({len(groups[i + 1])}, {groups[i]}) ', end='')