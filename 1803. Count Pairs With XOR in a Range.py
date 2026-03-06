from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 2
            self.cnt = 0

    def add(self, x) -> None:
        node = self.root
        for i in range(30, -1, -1):
            if x & (1 << i):
                if not node.children[1]:
                    node.children[1] = self.TrieNode()
                node = node.children[1]
            else:
                if not node.children[0]:
                    node.children[0] = self.TrieNode()
                node = node.children[0]
            node.cnt += 1

    def dfs(self, x: int, bound: int, cur: int, node: TrieNode, bit: int) -> int:
        if not node:
            return 0
        if bit == -1:
            return node.cnt
        if (cur + (1 << bit)) > bound:
            if x & (1 << bit):
                return self.dfs(x, bound, cur, node.children[1], bit - 1)
            else:
                return self.dfs(x, bound, cur, node.children[0], bit - 1)
        if (cur + (1 << (bit + 1))) <= bound:
            return node.cnt
        if x & (1 << bit):
            return self.dfs(x, bound, cur, node.children[1], bit - 1) + self.dfs(x, bound, cur | (1 << bit), node.children[0], bit - 1)
        else:
            return self.dfs(x, bound, cur, node.children[0], bit - 1) + self.dfs(x, bound, cur | (1 << bit), node.children[1], bit - 1)
        
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        self.root = self.TrieNode()
        ans = 0
        for i in nums:
            ans += self.dfs(i, high, 0, self.root, 30) - self.dfs(i, low - 1, 0, self.root, 30)
            self.add(i)
        return ans
