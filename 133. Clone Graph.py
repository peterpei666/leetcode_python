from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        memo = [None] * 101
        if not node:
            return None
        
        def dfs(node: Optional['Node']) -> Optional['Node']:
            if memo[node.val]:
                return memo[node.val]
            memo[node.val] = Node(node.val)
            for next in node.neighbors:
                memo[node.val].neighbors.append(dfs(next))
            return memo[node.val]
        
        dfs(node)
        return memo[node.val]
