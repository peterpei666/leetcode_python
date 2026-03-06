from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 2
            self.tag = False

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
            if not node.children[0] and not node.children[1]:
                return -1
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

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        m = len(nums)
        n = len(queries)
        p = [(queries[i][0], queries[i][1], i) for i in range(n)]
        nums.sort()
        p.sort(key=lambda x : x[1])
        self.root = self.TrieNode()
        j = 0
        ans = [0] * n
        for i in range(n):
            while j < m and nums[j] <= p[i][1]:
                self.add(nums[j])
                j += 1
            ans[p[i][2]] = self.get(p[i][0])
        return ans
