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

def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next

head1 = build_list([4, 5, 1, 9])
node_to_delete = head1.next
delete_node(node_to_delete)
print(to_list(head1))

head2 = build_list([4, 5, 1, 9])
node_to_delete = head2.next.next
delete_node(node_to_delete)
print(to_list(head2))