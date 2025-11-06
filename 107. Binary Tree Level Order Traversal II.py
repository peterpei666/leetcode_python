from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        def depth(node: Optional[TreeNode], cur: int) -> int:
            if not node:
                return cur
            return max(depth(node.left, cur + 1), depth(node.right, cur + 1))
        
        ans = [[] for _ in range(depth(root, 0))]

        def dfs(node: Optional[TreeNode], cur: int) -> None:
            if not node:
                return
            ans[cur].append(node.val)
            dfs(node.left, cur + 1)
            dfs(node.right, cur + 1)

        dfs(root, 0)
        return ans[::-1]
