class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

head1 = build_list([3, 2, 0, -4])
head1.next.next.next.next = head1.next
print(has_cycle(head1))

head2 = build_list([1, 2])
head2.next.next = head2
print(has_cycle(head2))

head3 = build_list([1])
print(has_cycle(head3))