from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node: Optional[TreeNode], cur: int) -> int:
            if not node:
                return cur
            return max(depth(node.left, cur + 1), depth(node.right, cur + 1))
        
        return depth(root, 0)
