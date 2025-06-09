class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        def dfs(node, level):
            if not node:
                return
            if len(ret) == level:
                ret.append([])
            ret[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        for i in range(len(ret)):
            if i % 2 == 1:
                ret[i].reverse()
        return ret
