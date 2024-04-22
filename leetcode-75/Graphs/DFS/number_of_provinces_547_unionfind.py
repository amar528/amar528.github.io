from typing import List


class Solution:
    def findCircleNum(self, provinces: List[List[int]]) -> int:

        n = len(provinces)
        regions = n

        parent = [i for i in range(n)]
        rank = [1] * n

        def find_root_parent_and_compress_path(node):
            # parent is itself initially
            root_parent = node

            # loop until node is not the parent of itself
            while root_parent != parent[root_parent]:
                # path compression - set parent equal to its grandparent
                # i.e. linked list to tree
                parent[root_parent] = parent[parent[root_parent]]

                # go up the parent chain
                root_parent = parent[root_parent]

            return root_parent

        def union(node1, node2):
            # find rot parents of both nodes
            parent1 = find_root_parent_and_compress_path(node1)
            parent2 = find_root_parent_and_compress_path(node2)

            # if they're the same, we do not perform a union
            if parent1 == parent2:
                return 0

            # merge them together - using rank
            if rank[parent1] > rank[parent2]:
                # parent1 becomes parent
                parent[parent2] = parent1

                # add parent2 (child) rankings to new parent
                rank[parent1] += rank[parent2]
            else:
                # parent2 becomes parent
                parent[parent1] = parent2

                # add parent1 (child) rankings to new parent
                rank[parent2] += rank[parent1]

            # we performed a union
            return 1

        for city in range(n):
            for neighbour in range(n):
                if provinces[city][neighbour] == 1:
                    regions -= union(city, neighbour)

        return regions
