from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        path = []

        def dfs(node: Optional[TreeNode], cur: int) -> None:
            path.append(node.val)
            if not node.left and not node.right:
                if cur + node.val == targetSum:
                    ans.append(path[:])
                path.pop()
                return
            if node.left:
                dfs(node.left, cur + node.val)
            if node.right:
                dfs(node.right, cur + node.val)
            path.pop()
        
        dfs(root, 0)
        return ans
