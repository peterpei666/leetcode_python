from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 2
            self.tag = False

    def findMaximumXOR(self, nums: List[int]) -> int:
        self.root = self.TrieNode()
        for i in nums:
            self.add(i)
        return max(self.get(i) for i in nums)

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

    def get(self, x) -> int:
        node = self.root
        ans = 0
        for i in range(30, -1, -1):
            if x & (1 << i):
                if node.children[0]:
                    ans |= 1 << i
                    node = node.children[0]
                else:
                    node = node.children[1]
            else:
                if node.children[1]:
                    ans |= 1 << i
                    node = node.children[1]
                else:
                    node = node.children[0]
        return ans
