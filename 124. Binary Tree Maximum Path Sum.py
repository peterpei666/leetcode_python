from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            nonlocal ans
            l = dfs(node.left)
            r = dfs(node.right)
            ans = max(ans, node.val + max(0, l) + max(0, r))
            return max(0, node.val + max(0, l, r))
        
        dfs(root)
        return ans
