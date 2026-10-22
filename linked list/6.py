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

def double_it(head):
    if head.val >= 5:
        head = ListNode(0, head)
        
    curr = head
    while curr:
        curr.val = (curr.val * 2) % 10
        if curr.next and curr.next.val >= 5:
            curr.val += 1
        curr = curr.next
        
    return head

head1 = build_list([1, 8, 9])
print(to_list(double_it(head1)))

head2 = build_list([9, 9, 9])
print(to_list(double_it(head2)))