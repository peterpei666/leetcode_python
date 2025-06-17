class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = mat[i][0]
            for j in range(1, n):
                if mat[i][j] == 1:
                    dp[i][j] = dp[i][j - 1] + 1
                else:
                    dp[i][j] = 0
        ans = 0
        for j in range(n):
            for i in range(m):
                temp = dp[i][j]
                for k in range(i, -1, -1):
                    if dp[k][j] == 0:
                        break
                    temp = min(temp, dp[k][j])
                    ans += temp
        return ans
