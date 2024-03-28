#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
from collections import defaultdict
from functools import reduce


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        visited.add(node)

        for i in graph[node]:
            dfs(graph, i, visited)

    return visited


def journeyToMoon(n, astronaut):
    astro_map = defaultdict(set)

    for a, b in astronaut:
        astro_map[a].add(b)
        astro_map[b].add(a)

    visited = set()
    lengths = []

    for a in {i for i in range(n)}:
        if a not in visited:
            subtree = set()
            dfs(astro_map, a, subtree)
            visited.update(subtree)

            lengths.append(len(subtree))

    result = 0
    for l in range(len(lengths) - 1):
        v = lengths[l]
        rhs = lengths[l + 1:]
        for other in rhs:
            result += v * other

    return result
