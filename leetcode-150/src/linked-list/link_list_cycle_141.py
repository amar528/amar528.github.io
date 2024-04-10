from typing import Optional

from list_node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        visited = set()
        node = head
        while node.next:
            if id(node) in visited:
                return True
            visited.add(id(node))
            node = node.next

        return False
