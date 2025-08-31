from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        wid = max(nums).bit_length()
        mask = 1 << wid
        dp = [0] * mask
        for i in nums:
            dp[i] = i
        for i in range(mask):
            if dp[i]:
                continue
            for j in range(wid):
                if i & (1 << j):
                    dp[i] = max(dp[i], dp[i ^ (1 << j)])
        return max(i * dp[(mask - 1) ^ i] for i in nums)
