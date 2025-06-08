class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        list = dict()
        def dfs(node, cur, list):
            if not node:
                return 0
            cur += node.val
            count = list.get(cur - targetSum, 0)
            list[cur] = list.get(cur, 0) + 1
            count += dfs(node.left, cur, list)
            count += dfs(node.right, cur, list)
            list[cur] -= 1
            return count
        list[0] = 1
        return dfs(root, 0, list)

