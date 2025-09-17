from typing import List

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * 2 for _ in range(2)]
        for i in nums:
            if i & 1:
                dp[0][1] = (dp[0][1] + dp[0][0]) % mod
                dp[0][0] = (dp[0][0] + dp[1][0] + dp[1][1] + 1) % mod
            else:
                dp[1][1] = (dp[1][1] + dp[1][0]) % mod
                dp[1][0] = (dp[1][0] + dp[0][0] + dp[0][1] + 1) % mod
        return (sum(dp[0]) + sum(dp[1])) % mod
