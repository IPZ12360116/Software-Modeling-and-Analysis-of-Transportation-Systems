class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minCameraCover(root):
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return 1
        left = dfs(node.left)
        right = dfs(node.right)
        if left == 0 or right == 0:
            res += 1
            return 2
        if left == 2 or right == 2:
            return 1
        return 0
    if dfs(root) == 0:
        res += 1
    return res
