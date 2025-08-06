class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = dict()

        def cost(i: int, j: int) -> int:
            c = 0
            while i < j:
                if s[i] != s[j]:
                    c += 1
                i += 1
                j -= 1
            return c
        
        def dfs(i: int, k: int) -> int:
            nonlocal memo
            if (i, k) in memo:
                return memo[(i, k)]
            if n - i == k:
                return 0
            if k == 1:
                memo[(i,k)] = cost(i, n - 1)
                return memo[(i, k)]
            res = float('inf')
            for j in range(i + 1, n - k + 2):
                res = min(res, cost(i, j - 1) + dfs(j, k - 1))
            memo[(i, k)] = res
            return res
        
        return dfs(0, k)
