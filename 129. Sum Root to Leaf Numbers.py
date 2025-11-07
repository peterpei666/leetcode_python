from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode], cur: int) -> None:
            if not node.left and not node.right:
                nonlocal ans
                ans += cur * 10 + node.val
            if node.left:
                dfs(node.left, cur * 10 + node.val)
            if node.right:
                dfs(node.right, cur * 10 + node.val)
        
        dfs(root, 0)
        return ans
