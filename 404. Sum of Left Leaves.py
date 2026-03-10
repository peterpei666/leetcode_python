from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, isLeft):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                if isLeft:
                    ans += node.val
                return
            dfs(node.left, True)
            dfs(node.right, False)
        
        dfs(root, False)
        return ans
