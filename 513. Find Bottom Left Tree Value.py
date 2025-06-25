class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.depth, self.ans = 0, 0
        def dfs(node: Optional[TreeNode], cur: int) -> None:
            if node.left:
                dfs(node.left, cur + 1)
            if cur > self.depth:
                self.ans = node.val
                self.depth = cur
            if node.right:
                dfs(node.right, cur + 1)

        dfs(root, 1)
        return self.ans
