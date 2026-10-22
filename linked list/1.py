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

def merge_two_lists(list1, list2):
    dummy = ListNode()
    curr = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
        
    curr.next = list1 if list1 else list2
    return dummy.next

l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])
print(to_list(merge_two_lists(l1, l2)))

l3 = build_list([])
l4 = build_list([])
print(to_list(merge_two_lists(l3, l4)))

l5 = build_list([])
l6 = build_list([0])
print(to_list(merge_two_lists(l5, l6)))