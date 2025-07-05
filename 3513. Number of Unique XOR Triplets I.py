from math import log2

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        cnt = int(log2(n) + 1)
        return 1 << cnt
