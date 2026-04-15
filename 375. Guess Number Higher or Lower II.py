class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[10 ** 9] * (n + 1) for _ in range(n + 1)]

        def help(l: int, r: int) -> int:
            if l >= r:
                return 0
            if not dp[l][r] == 10 ** 9:
                return dp[l][r]
            for i in range(l, r + 1):
                dp[l][r] = min(dp[l][r], max(help(l, i - 1), help(i + 1, r)) + i)
            return dp[l][r]
    
        return help(1, n)
