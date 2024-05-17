from typing import Optional

from listnode import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        if not head.next:
            return head

        odd = None
        even = None

        odd_head = None
        even_head = None

        current = head
        is_even = False

        while current:

            if is_even:
                if not even_head:
                    even_head = current
                    even = even_head
                else:
                    even.next = current
                    even = even.next
            else:
                if not odd_head:
                    odd_head = current
                    odd = odd_head
                else:
                    odd.next = current
                    odd = odd.next

            current = current.next

            is_even = not is_even

        # append even nodes after the last odd node
        odd.next = even_head
        even.next = None

        return odd_head
