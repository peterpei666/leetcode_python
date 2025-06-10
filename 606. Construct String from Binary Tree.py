class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if not left and not right:
            return str(root.val)
        if not right:
            return f"{root.val}({left})"
        return f"{root.val}({left})({right})"
