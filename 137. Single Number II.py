from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t1, t2 = 0, 0
        for i in nums:
            t1 = (t1 ^ i) & (~t2)
            t2 = (t2 ^ i) & (~t1)
        return t1
