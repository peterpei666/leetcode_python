from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None, None]
            self.cnt = 0

    def __init__(self):
        self.root = None

    def add(self, x):
        node = self.root
        for i in range(30, -1, -1):
            bit = (x >> i) & 1
            if not node.children[bit]:
                node.children[bit] = self.TrieNode()
            node = node.children[bit]
            node.cnt += 1

    def get(self, x):
        node = self.root
        ans = 0
        for i in range(30, -1, -1):
            if not node:
                return -1
            bit = (x >> i) & 1
            target = 1 - bit
            if node.children[target] and node.children[target].cnt > 0:
                ans |= (1 << i)
                node = node.children[target]
            elif node.children[bit] and node.children[bit].cnt > 0:
                node = node.children[bit]
            else:
                return -1
        return ans
    
    def remove(self, x):
        node = self.root
        for i in range(30, -1, -1):
            bit = (x >> i) & 1
            node = node.children[bit]
            node.cnt -= 1

    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        self.root = self.TrieNode()
        ans = 0
        j = 0
        for i in range(len(nums)):
            while nums[i] > nums[j] * 2:
                self.remove(nums[j])
                j += 1
            self.add(nums[i])
            ans = max(ans, self.get(nums[i]))
        return ans
