from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = [False] * n
        temp = 0
        for i in range(n):
            temp = ((temp << 1) + nums[i]) % 5
            ans[i] = not temp
        return ans
