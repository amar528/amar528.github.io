from typing import Optional

from listnode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr, prev = head, None

        while curr:

            # remember the next node
            temp = curr.next

            # reassign next to the previous (reverse)
            curr.next = prev

            # update our prev and current pointers to the next nodes
            prev = curr
            curr = temp

        # prev will end up at the end of the original list, which is the new head
        return prev
