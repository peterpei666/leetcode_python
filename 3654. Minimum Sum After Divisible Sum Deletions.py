from typing import List

class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        dp = [0] + [float('inf')] * (k - 1)
        sum = 0
        for i in nums:
            sum += i
            dp[sum % k] = min(dp[sum % k], sum)
            sum = dp[sum % k]
        return sum
