from typing import List


class Solution:
    def findCircleNum(self, provinces: List[List[int]]) -> int:

        n = len(provinces)
        regions = 0
        visited = set()

        def dfs(city):

            if city in visited:
                return False

            # add to visited inside the recursion
            visited.add(city)

            for neighbour in range(n):
                # if we have a connection and it has not been visited
                if provinces[city][neighbour] == 1:
                    dfs(neighbour)

        for city in range(n):

            if city not in visited:
                # we haven't seen this city before
                # so we found a new province / set of components
                # increment the region count
                # visit the city and its neighbours
                regions += 1
                dfs(city)

        return regions
