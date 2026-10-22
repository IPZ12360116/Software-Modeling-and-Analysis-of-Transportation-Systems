class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    res = []
    stack = []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
        
    return res

root1 = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(inorder_traversal(root1))

root2 = None
print(inorder_traversal(root2))

root3 = TreeNode(1)
print(inorder_traversal(root3))