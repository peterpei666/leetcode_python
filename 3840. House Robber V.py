from typing import List

class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        dp = [[nums[0], 0], [0, 0]]
        n = len(nums)
        for i in range(1, n):
            if not colors[i] == colors[i - 1]:
                dp[i & 1][0] = max(dp[(i - 1) & 1][0], dp[(i - 1) & 1][1]) + nums[i]
            else:
                dp[i & 1][0] = dp[(i - 1) & 1][1] + nums[i]
            dp[i & 1][1] = max(dp[(i - 1) & 1][0], dp[(i - 1) & 1][1])
        return max(dp[(n - 1) & 1][0], dp[(n - 1) & 1][1])
