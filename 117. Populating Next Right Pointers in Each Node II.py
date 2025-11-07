from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        
        def depth(node: Optional[Node], cur: int) -> int:
            if not node:
                return cur
            return max(depth(node.left, cur + 1), depth(node.right, cur + 1))
        
        layer = [[] for _ in range(depth(root, 0))]

        def dfs(node: Optional[Node], depth: int) -> None:
            if node:
                layer[depth].append(node)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        
        dfs(root, 0)
        for l in layer:
            for i in range(1, len(l)):
                l[i - 1].next = l[i]
        return root
