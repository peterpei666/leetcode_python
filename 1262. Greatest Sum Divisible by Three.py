from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        t = [[float('inf')] * 2 for _ in range(2)]
        ans = sum(nums)
        for i in nums:
            if i % 3:
                if i < t[i % 3 - 1][0]:
                    t[i % 3 - 1][1] = t[i % 3 - 1][0]
                    t[i % 3 - 1][0] = i
                elif i < t[i % 3 - 1][1]:
                    t[i % 3 - 1][1] = i
        if ans % 3 == 1:
            ans -= min(t[0][0], t[1][0] + t[1][1])
        elif ans % 3 == 2:
            ans -= min(t[1][0], t[0][0] + t[0][1])
        return int(ans)
