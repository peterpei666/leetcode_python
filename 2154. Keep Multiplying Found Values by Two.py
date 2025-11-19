from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mp = [False] * 1001
        for i in nums:
            mp[i] = True
        while original <= 1000 and mp[original]:
            original <<= 1
        return original
