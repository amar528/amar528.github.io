import itertools

n = (int(input()))
chars = input().split()
k = (int(input()))

combinations = []
divisor = 0  # count how many combinations contain the letter 'a'
for comb in itertools.combinations(chars, r=k):
    combinations.append(comb)
    if 'a' in comb:
        divisor += 1

denominator = len(combinations)

print('%.4f' % (divisor / denominator))
