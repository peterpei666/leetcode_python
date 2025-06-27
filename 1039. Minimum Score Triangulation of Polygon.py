class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        dp = [[0] * 50 for _ in range(50)]
        n = len(values)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                for k in range(i + 1, j):
                    if dp[i][j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + values[i] * values[j] * values[k] + dp[k][j])
                    else:
                        dp[i][j] = dp[i][k] + values[i] * values[j] * values[k] + dp[k][j]
        return dp[0][n - 1]
