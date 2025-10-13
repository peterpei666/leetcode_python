from typing import List
from collections import defaultdict

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        ans = 0
        for x, cnt in mp.items:
            if cnt % k == 0:
                ans += x * cnt
        return ans
