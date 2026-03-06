from collections import deque

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

    def maxXor(self, nums, k):
        self.root = self.TrieNode()
        self.add(0)
        q1 = deque()
        q2 = deque()
        n = len(nums)
        pre = [0] * n
        ans = 0
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] ^ nums[i]
        j = 0
        for i in range(n):
            while q1 and q1[-1] < nums[i]:
                q1.pop()
            q1.append(nums[i])
            while q2 and q2[-1] > nums[i]:
                q2.pop()
            q2.append(nums[i])
            while q1[0] - q2[0] > k:
                if nums[j] == q1[0]:
                    q1.popleft()
                if nums[j] == q2[0]:
                    q2.popleft()
                self.remove(pre[j - 1] if j > 0 else 0)
                j += 1
            ans = max(ans, self.get(pre[i]))
            self.add(pre[i])
        return ans
