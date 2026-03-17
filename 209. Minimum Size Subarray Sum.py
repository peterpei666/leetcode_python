from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = 1000000
        i, j, cur = 0, -1, 0
        while i < n:
            cur += nums[i]
            while j + 1 < i and cur - nums[j + 1] >= target:
                cur -= nums[j + 1]
                j += 1
            if cur >= target:
                ans = min(ans, i - j)
            i += 1
        return 0 if ans == 1000000 else ans
