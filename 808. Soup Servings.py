from math import ceil

class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = dict()

        def cal(i: int, j: int) -> float:
            return (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][j - 1] + dp[max(0, i - 2)][max(0, j - 2)] + dp[i - 1][max(0, j - 3)]) / 4
        
        dp[0] = {0: 0.5}
        for i in range(1, m + 1):
            dp[0][i] = 1.0
            dp[i] = {0: 0.0}
            for j in range(1, i + 1):
                dp[j][i] = cal(j, i)
                dp[i][j] = cal(i, j)
            if dp[i][i] > 1 - 1e-5:
                return 1.0
        return dp[m][m]
