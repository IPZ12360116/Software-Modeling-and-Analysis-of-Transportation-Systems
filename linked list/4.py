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

def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def reorder_list(head):
    if not head or not head.next:
        return
        
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    prev = None
    curr = slow.next
    slow.next = None
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    first = head
    second = prev
    while second:
        t1 = first.next
        t2 = second.next
        first.next = second
        second.next = t1
        first = t1
        second = t2

head1 = build_list([1, 2, 3, 4])
reorder_list(head1)
print(to_list(head1))

head2 = build_list([1, 2, 3, 4, 5])
reorder_list(head2)
print(to_list(head2))