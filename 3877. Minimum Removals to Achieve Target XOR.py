from typing import List

class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[] for _ in range(2)]
        dp[0] = [float('-inf')] * 16384
        dp[0][0] = 0
        dp[0][nums[0]] = 1
        for i in range(1, n):
            t = i & 1
            p = t ^ 1
            dp[t] = [float('-inf')] * 16384
            for k in range(16384):
                if dp[p][k] >= 0:
                    dp[t][k ^ nums[i]] = max(dp[t][k ^ nums[i]], dp[p][k] + 1)
                    dp[t][k] = max(dp[t][k], dp[p][k])
        if dp[(n - 1) & 1][target] < 0:
            return -1
        return n - dp[(n - 1) & 1][target]
