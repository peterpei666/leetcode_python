from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        m = len(skill)
        dp = [0] * (m + 1)
        for k in mana:
            for i in range(m):
                dp[i + 1] = max(dp[i], dp[i + 1]) + k * skill[i]
            for i in range(m - 1, -1, -1):
                dp[i] = dp[i + 1] - k * skill[i]
        return dp[m]
