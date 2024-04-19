class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode val:{self.val}'


def build_list(arr):
    head = None
    prev = None
    for num in arr:
        node = ListNode(num)

        if prev:
            prev.next = node
            prev = node
        else:
            head = node
            prev = head

    return head


def build_arr(head):
    arr = []

    node = head
    while node.next:
        arr.append(node.val)
        node = node.next
    arr.append(node.val)

    return arr
