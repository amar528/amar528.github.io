import sys


def grid_challenge(grid):
    matrix = []
    for word in grid:
        matrix.append(list(sorted(word)))

    for col in range(len(matrix[0])):
        prev = None
        for row in matrix:
            prev = row[col] if prev is None else prev
            curr = row[col]
            if curr < prev:
                return 'NO'

    return 'YES'


memo = {}


def super_digit(s, k):
    if len(s) == 1:
        return s

    if s in memo:
        return memo[s]

    val = sum([int(i) for i in s]) * k

    memo[s] = int(super_digit(str(val), 1))
    return memo[s]


def minimumBribes(q):
    n = len(q)

    bribes = 0

    for i in reversed(range(n)):
        current_val = q[i]
        expected = i + 1
        if current_val - expected > 2:
            return 'Too chaotic'

        left_gt_count = sum(1 for _ in (left for left in q[:i] if left > current_val))
        bribes += left_gt_count

    return bribes


def truck_tour(petrolpumps):
    pump = tank = i = 0

    for petrol, distance in petrolpumps:
        tank += petrol
        tank -= distance

        if tank < 0:
            # try next pump
            tank = 0
            pump = i + 1
        i += 1

    return pump