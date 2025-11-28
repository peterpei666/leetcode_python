from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        mp = [[] for _ in range(n)]
        for e in edges:
            mp[e[0]].append(e[1])
            mp[e[1]].append(e[0])
        ans = 0

        def dfs(node: int, parent: int) -> int:
            sum = values[node] % k
            valid = False
            for next in mp[node]:
                if next == parent:
                    continue
                sum = (sum + dfs(next, node)) % k
                valid = True
            if (sum == 0 and valid) or (values[node] % k == 0 and not valid):
                nonlocal ans
                ans += 1
            return sum
        
        dfs(0, -1)
        return ans
