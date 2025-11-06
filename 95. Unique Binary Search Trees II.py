from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i].append(TreeNode(i))
        for num in range(2, n + 1):
            for start in range(1, n - num + 2):
                end = start + num - 1
                for i in range(start, end + 1):
                    left = dp[start][i - 1] if i - 1 >= start else [None]
                    right = dp[i + 1][end] if i + 1 <= end else [None]
                    for l in left:
                        for r in right:
                            root = TreeNode(i, l, r)
                            dp[start][end].append(root)
        return dp[1][n]
