from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        visited = set()

        def visit(room, all_keys):
            if room >= n or room in visited or room not in all_keys:
                return False

            visited.add(room)

            keys = rooms[room]
            all_keys.update(keys)

            for key in keys:
                visit(key, all_keys)

        visit(0, {0})

        return len(rooms) == len(visited)
