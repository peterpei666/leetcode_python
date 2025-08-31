from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dif = nums[i] - nums[j]
                dp[i][dif] += dp[j][dif] + 1
                ans += dp[j][dif]
        return ans
