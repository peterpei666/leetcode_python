from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        mp = defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            mp[total] += 1
            return total
        
        dfs(root)
        cur = 0
        ans = []
        for x, n in mp.items():
            if n > cur:
                ans = []
                cur = n
            if n == cur:
                ans.append(x)
        return ans
