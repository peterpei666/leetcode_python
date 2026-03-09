from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        def preorder(cur: str, node: TreeNode) -> None:
            if not node:
                return
            if len(cur):
                cur += '->'
            cur += str(node.val)
            if not node.left and not node.right:
                ans.append(cur[:])
                return
            preorder(cur, node.left)
            preorder(cur, node.right)

        preorder('', root)
        return ans
