class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(node, lst):
            if not node:
                return
            inorder(node.left, lst)
            lst.append(node.val)
            inorder(node.right, lst)
        elements = []
        inorder(root1, elements)
        inorder(root2, elements)
        return sorted(elements)
