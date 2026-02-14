class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * 101 for _ in range(2)]
        dp[0][0] = poured
        for i in range(1, query_row + 1):
            dp[i & 1][0] = max(dp[(i - 1) & 1][0] - 1, 0) / 2
            for j in range(1, query_row  +1):
                dp[i & 1][j] = max(dp[(i - 1) & 1][j - 1] - 1.0, 0.0) / 2 + max(dp[(i - 1) & 1][j] - 1.0, 0.0) / 2
        return min(1.0, dp[query_row & 1][query_glass])
