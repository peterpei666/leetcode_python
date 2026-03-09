class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode) -> tuple[int, int]:
            if not node:
                return (0, 0)
            l1, l2 = dfs(node.left)
            r1, r2 = dfs(node.right)
            t1 = max(l1, l2) + max(r1, r2)
            t2 = node.val + l1 + r1
            return (t1, t2)
        
        return max(dfs(root))
