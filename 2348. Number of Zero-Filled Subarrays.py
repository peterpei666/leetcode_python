from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, temp = 0, 0
        for i in nums:
            if not i == 0:
                temp = 0
            else:
                temp += 1
                ans += temp
        return ans
