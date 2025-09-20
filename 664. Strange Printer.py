class Solution:
    def strangePrinter(self, ori: str) -> int:
        n = len(ori)
        s = ori[0]
        for i in range(1, n):
            if not ori[i] == ori[i - 1]:
                s += ori[i]
        n = len(s)
        memo = [[-1] * n for _ in range(n)]

        def dfs(l: int, r: int) -> int:
            nonlocal memo
            if l > r:
                return 0
            if not memo[l][r] == -1:
                return memo[l][r]
            ans = 1 + dfs(l + 1, r)
            for i in range(l + 1, r + 1):
                if s[l] == s[i]:
                    ans = min(ans, dfs(l, i - 1) + dfs(i + 1, r))
            memo[l][r] = ans
            return ans
        
        return dfs(0, n - 1)
