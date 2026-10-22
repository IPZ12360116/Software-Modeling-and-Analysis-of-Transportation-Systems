class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next = next_node


def swap_pairs(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    first = head
    second = head.next
    
    first.next = swap_pairs(second.next)
    
    second.next = first
    
    return second

def build_linked_list(arr: list) -> ListNode:
    if not arr:
        return None
    return ListNode(arr[0], build_linked_list(arr[1:]))

def linked_list_to_list(head: ListNode) -> list:
    if head is None:
        return []
    return [head.val] + linked_list_to_list(head.next)

head1 = build_linked_list([1, 2, 3, 4])
print(linked_list_to_list(swap_pairs(head1)))

head2 = build_linked_list([])
print(linked_list_to_list(swap_pairs(head2)))

head3 = build_linked_list([1])
print(linked_list_to_list(swap_pairs(head3)))