class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left or not root.right:
                return root.left if root.left else root.right
            temp = root.left
            while temp.right:
                temp = temp.right
            root.val = temp.val
            root.left = self.deleteNode(root.left, temp.val)
        return root
