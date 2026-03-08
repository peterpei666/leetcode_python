from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        mp = set(nums)
        n = len(nums)
        for i in range(n + 1):
            s = bin(i)[2:]
            s = '0' * (n - len(s)) + s
            if not s in mp:
                return s
        return ''
