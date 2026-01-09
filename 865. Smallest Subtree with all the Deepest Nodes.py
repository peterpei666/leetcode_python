from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def depth(cur, node):
            return cur if not node else max(depth(cur + 1, node.left), depth(cur + 1, node.right))
        
        l, r = depth(0, root.left), depth(0, root.right)
        if l > r:
            return self.subtreeWithAllDeepest(root.left)
        elif l < r:
            return self.subtreeWithAllDeepest(root.right)
        else:
            return root
