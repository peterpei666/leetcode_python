from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []

        def preorder(node: TreeNode, d: int) -> None:
            if not node:
                return
            if d == len(ans):
                ans.append(node.val)
            ans[d] = node.val
            preorder(node.left, d + 1)
            preorder(node.right, d + 1)

        preorder(root, 0)
        return ans
