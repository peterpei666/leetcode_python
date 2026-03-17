from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0], [0, 0]]
        n = len(nums)
        dp[0][0] = dp[0][1] = dp[1][0] = dp[1][1] = nums[0]
        for i in range(2, n - 1):
            dp[i & 1][0] = max(dp[(i & 1) ^ 1][0], dp[(i & 1) ^ 1][1])
            dp[i & 1][1] = dp[(i & 1) ^ 1][0] + nums[i]
        ans = max(dp[n & 1][0], dp[n & 1][1])
        dp[0][0] = dp[0][1] = 0
        for i in range(1, n):
            dp[i & 1][0] = max(dp[(i & 1) ^ 1][0], dp[(i & 1) ^ 1][1])
            dp[i & 1][1] = dp[(i & 1) ^ 1][0] + nums[i]
        ans = max(ans, max(dp[(n & 1) ^ 1][0], dp[(n & 1) ^ 1][1]))
        return ans
