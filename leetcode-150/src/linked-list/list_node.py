class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def to_list_node(head):
    # head = [3, 2, 0, -4]
    head_node = None
    prev = None

    for val in head:
        list_node = ListNode(val)

        if not head_node:
            head_node = list_node

        if prev:
            prev.next = list_node

        prev = list_node

    return head_node
