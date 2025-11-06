from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node: Optional[TreeNode], cur: int) -> int:
            if not node:
                return cur
            return max(depth(node.left, cur + 1), depth(node.right, cur + 1))
        
        return not root or (abs(depth(root.left, 0) - depth(root.right, 0)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right))
