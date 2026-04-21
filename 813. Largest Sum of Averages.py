from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0.0] * n for _ in range(2)]
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        for i in range(n):
            dp[1][i] = (prefix[n] - prefix[i]) / (n - i)
        for group in range(2, k + 1):
            mask = group & 1
            prev = mask ^ 1
            for i in range(n):
                dp[mask][i] = 0.0
            for l in range(n - group + 1):
                for r in range(l, n - group + 1):
                    dp[mask][l] = max(dp[mask][l], dp[prev][r + 1] + (prefix[r + 1] - prefix[l]) / (r - l + 1))
        return dp[k & 1][0]
