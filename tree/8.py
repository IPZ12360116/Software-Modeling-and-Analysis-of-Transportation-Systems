class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    nodes = []
    def dfs(node, r, c):
        if not node:
            return
        nodes.append((c, r, node.val))
        dfs(node.left, r + 1, c - 1)
        dfs(node.right, r + 1, c + 1)
    dfs(root, 0, 0)
    nodes.sort()
    res = []
    curr_col = []
    last_c = None
    for c, r, val in nodes:
        if c != last_c:
            if last_c is not None:
                res.append(curr_col)
            curr_col = [val]
            last_c = c
        else:
            curr_col.append(val)
    if curr_col:
        res.append(curr_col)
    return res
