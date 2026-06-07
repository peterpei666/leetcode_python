from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node = [None] * 100002
        child = [False] * 100002
        for d in descriptions:
            if not node[d[0]]:
                node[d[0]] = TreeNode(d[0])
            if not node[d[1]]:
                node[d[1]] = TreeNode(d[1])
            child[d[1]] = True
            if d[2]:
                node[d[0]].left = node[d[1]]
            else:
                node[d[0]].right = node[d[1]]
        for i in range(100001):
            if node[i] and not child[i]:
                return node[i]
        return None
