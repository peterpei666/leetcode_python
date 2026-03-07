from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}

    def count(self, x: int) -> int:
        for i in range(9):
            if x >= self.arr[i]:
                return i
        return -1
    

    def add(self, x: int) -> None:
        node = self.root
        for i in range(self.count(x), 9):
            if not x // self.arr[i] in node.children:
                node.children[x // self.arr[i]] = self.TrieNode()
            node = node.children[x // self.arr[i]]
            x %= self.arr[i]

    def find(self, x: int) -> int:
        node = self.root
        ans = 0
        for i in range(self.count(x), 9):
            if not x // self.arr[i] in node.children:
                break
            node = node.children[x // self.arr[i]]
            x %= self.arr[i]
            ans += 1
        return ans
    
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        self.root = self.TrieNode()
        self.arr = [100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]
        for i in arr1:
            self.add(i)
        return max(self.find(i) for i in arr2)
