from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        dp = [1] + [0] * total
        dp[nums[0]] = 2
        for i in range(1, n):
            for j in range(total - nums[i], -1, -1):
                dp[j + nums[i]] |= dp[j] << 1
        for i in range(1, n):
            if (total * i) % n == 0 and dp[total * i // n] & (1 << i):
                return True
        return False
