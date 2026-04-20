from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        m = max(nums)
        cnt = [0] * (m + 1)
        for i in range(n):
            cnt[nums[i]] += 1
        dp = [[0, 0] for _ in range(m + 1)]
        dp[1][1] = cnt[1] * 1
        for i in range(2, m + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + cnt[i] * i
        return max(dp[m])
