from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in nums:
            i = abs(i)
            if i >= a:
                b = a
                a = i
            elif i > b:
                b = i
        return a * b * 100000
