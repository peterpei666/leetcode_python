class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        def dfs(node: TreeNode, cur: int) -> None:
            if node.val >= cur:
                cur = node.val
                self.cnt += 1
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
        
        dfs(root, float('-inf'))
        return self.cnt
