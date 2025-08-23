from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] + matrix[i][j] - dp[i][j]
        ans = - 10 ** 9
        for x in range(m, 0, -1):
            for y in range(n, 0, -1):
                for i in range(x, 0, -1):
                    for j in range(y, 0, -1):
                        temp = dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1]
                        if temp <= k:
                            ans = max(ans, temp)
                if ans == k:
                    return k
        return ans
