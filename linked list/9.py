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

def partition(head, x):
    less_dummy = ListNode()
    greater_dummy = ListNode()
    
    less = less_dummy
    greater = greater_dummy
    
    curr = head
    while curr:
        if curr.val < x:
            less.next = curr
            less = less.next
        else:
            greater.next = curr
            greater = greater.next
        curr = curr.next
        
    greater.next = None
    less.next = greater_dummy.next
    
    return less_dummy.next

head1 = build_list([1, 4, 3, 2, 5, 2])
print(to_list(partition(head1, 3)))

head2 = build_list([2, 1])
print(to_list(partition(head2, 2)))