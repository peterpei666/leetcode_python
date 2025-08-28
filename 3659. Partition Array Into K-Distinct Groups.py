from typing import List
from collections import defaultdict

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        for _, cnt in mp.items():
            if cnt > n // k:
                return False
        return True
