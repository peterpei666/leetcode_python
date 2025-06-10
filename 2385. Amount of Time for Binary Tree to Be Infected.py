class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        res = [0]
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == start:
                res[0] = max(l, r)
                return -1
            if l >= 0 and r >= 0:
                return max(l, r) + 1
            else:
                res[0] = max(res[0], abs(l) + abs(r))
                return min(l, r) - 1
        dfs(root)
        return res[0]
