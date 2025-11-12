from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        memo = dict()
        memo[None] = None

        def build(node: Optional[Node]) -> Optional[Node]:
            if node in memo:
                return memo[node]
            memo[node] = Node(x=node.val)
            memo[node].next = build(node.next)
            memo[node].random = build(node.random)
            return memo[node]

        return build(head)
