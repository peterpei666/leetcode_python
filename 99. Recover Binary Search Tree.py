from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev = None
        p1, p2 = None, None

        def find(node: Optional[TreeNode]) -> None:
            nonlocal prev, p1, p2
            if not node:
                return
            find(node.left)
            if prev and node.val < prev.val:
                if not p1:
                    p1 = prev
                p2 = node
            prev = node
            find(node.right)
        
        find(root)
        p1.val, p2.val = p2.val, p1.val
