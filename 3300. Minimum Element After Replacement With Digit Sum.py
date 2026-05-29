from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(ord(c) - ord('0') for c in str(x)) for x in nums)
