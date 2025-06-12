class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return True, 0
            left_valid, left_size = dfs(node.left)
            right_valid, right_size = dfs(node.right)
            if left_valid and right_valid and left_size == right_size:
                size = left_size + right_size + 1
                self.sizes.append(size)
                return True, size
            return False, 0
        self.sizes = []
        dfs(root)
        self.sizes.sort(reverse=True)
        return self.sizes[k - 1] if k <= len(self.sizes) else -1
