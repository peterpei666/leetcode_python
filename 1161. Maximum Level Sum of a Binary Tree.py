from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([root])
        level = 1
        best_level = 1
        best_sum = root.val
        while q:
            size = len(q)
            s = 0
            for _ in range(size):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > best_sum:
                best_sum = s
                best_level = level
            level += 1
        return best_level
