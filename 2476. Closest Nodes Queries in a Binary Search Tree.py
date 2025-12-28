from typing import List
import bisect

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        mp = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                mp.append(node.val)
                dfs(node.right)
        
        dfs(root)
        ans = []
        for q in queries:
            
            idx = bisect.bisect_left(mp, q)
            if idx < len(mp) and mp[idx] == q:
                ans.append([q, q])
            else:
                left = mp[idx - 1] if idx > 0 else -1
                right = mp[idx] if idx < len(mp) else -1
                ans.append([left, right])
        return ans
