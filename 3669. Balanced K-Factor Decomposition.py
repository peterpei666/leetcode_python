from typing import List

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        factor = []
        for i in range(1, n + 1):
            if n % i == 0:
                factor.append(i)
        sz = len(factor)
        ans = []
        path = [0] * k

        def dfs(idx: int, m: int, prod: int) -> None:
            nonlocal ans, path
            if idx == k:
                if (not ans or path > ans) and prod == n:
                    ans = path[:]
                return
            for i in range(m, sz):
                if (n // prod) % factor[i]:
                    continue
                path[idx] = factor[i]
                dfs(idx + 1, i, prod * factor[i])

        dfs(0, 0, 1)
        return ans
