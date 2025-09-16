from typing import List
from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = nums[i]
            while ans:
                if gcd(ans[-1], temp) == 1:
                    break
                temp = temp * ans[-1] // gcd(ans[-1], temp)
                ans.pop()
            ans.append(temp)
        return ans
