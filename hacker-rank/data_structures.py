from collections import defaultdict

inputs = [
    [3, 1], [1, 2], [3, 4], [4, 2], [7, 3], [5, 6]
]
print(inputs)


def it(lst):
    for a, b in lst:
        yield a, b


def build_dict(lst):
    _dict = defaultdict(set)
    for k, v in it(inputs):
        _dict[k].add(v)
        _dict[v].add(k)
    return _dict


def collect_nodes_dfs_recursion(graph, node, visited):
    if node is None: return []
    if node in visited: return []

    visited.add(node)

    result = [node]
    for neighbour in graph[node]:
        subtree = collect_nodes_dfs_recursion(graph, neighbour, visited)
        result.extend(subtree)

    return result


node_dict = build_dict(inputs)

print(node_dict)

visited = set()
for node in node_dict:
    subtree = collect_nodes_dfs_recursion(node_dict, node, visited)
    if subtree: print(f'subtree {subtree}')
