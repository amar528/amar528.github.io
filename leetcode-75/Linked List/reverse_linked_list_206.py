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

            # update our prev and current pointers
            prev = curr
            curr = temp

        return prev
