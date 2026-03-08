from typing import List
from collections import defaultdict

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

    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        graph = [[] for _ in range(n)]
        start = -1
        for i in range(n):
            if parents[i] == -1:
                start = i
            else:
                graph[parents[i]].append(i)
        q = len(queries)
        query = defaultdict(list)
        for i in range(q):
            query[queries[i][0]].append((i, queries[i][1]))
        self.root = self.TrieNode()
        ans = [0] * q

        def dfs(cur: int) -> None:
            self.add(cur)
            if cur in query:
                for i, x in query[cur]:
                    ans[i] = self.get(x)
            for next in graph[cur]:
                dfs(next)
            self.remove(cur)

        dfs(start)
        return ans
