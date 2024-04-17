from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        visited = set()

        def dfs(room, all_keys):
            if room >= n or room in visited or room not in all_keys:
                return False

            visited.add(room)

            keys = rooms[room]
            all_keys.update(keys)

            for key in keys:
                dfs(key, all_keys)

        dfs(0, {0})

        return len(rooms) == len(visited)
