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

def merge_two(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

def merge_k_lists(lists):
    if not lists:
        return None
        
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged.append(merge_two(l1, l2))
        lists = merged
        
    return lists[0]

lists1 = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
print(to_list(merge_k_lists(lists1)))

lists2 = []
print(to_list(merge_k_lists(lists2)))

lists3 = [build_list([])]
print(to_list(merge_k_lists(lists3)))