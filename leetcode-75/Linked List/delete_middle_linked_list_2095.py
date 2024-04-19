from typing import Optional

from listnode import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        slow_p = head
        fast_p = head.next.next if head.next.next else head.next

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        slow_p.next = slow_p.next.next

        return head
