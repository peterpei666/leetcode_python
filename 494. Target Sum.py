from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [[0] * 2001 for _ in range(2)]
        bias = 1000
        dp[0][nums[0] + bias] += 1
        dp[0][-nums[0] + bias] += 1
        total = nums[0]
        for i in range(1, len(nums)):
            mask = i & 1
            prev = mask ^ 1
            dp[mask] = [0] * 2001
            for j in range(-total + bias, total + bias + 1):
                dp[mask][j + nums[i]] += dp[prev][j]
                dp[mask][j - nums[i]] += dp[prev][j]
            total += nums[i]
        return dp[(len(nums) - 1) & 1][target + bias]
