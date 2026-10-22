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

def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    
    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
                
        group_next = kth.next
        
        prev = group_next
        curr = group_prev.next
        while curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        old_head = group_prev.next
        group_prev.next = kth
        group_prev = old_head

head1 = build_list([1, 2, 3, 4, 5])
print(to_list(reverse_k_group(head1, 2)))

head2 = build_list([1, 2, 3, 4, 5])
print(to_list(reverse_k_group(head2, 3)))