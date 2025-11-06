from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        idx = n - 1
        mp = dict()
        for i in range(n):
            mp[inorder[i]] = i
        
        def build(l: int, r: int) -> Optional[TreeNode]:
            nonlocal idx
            if l > r:
                return None
            root = TreeNode(postorder[idx])
            idx -= 1
            root.right = build(mp[root.val] + 1, r)
            root.left = build(l, mp[root.val] - 1)
            return root
        
        return build(0, n - 1)
