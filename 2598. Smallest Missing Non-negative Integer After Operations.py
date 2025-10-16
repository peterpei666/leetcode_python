from typing import List
from collections import defaultdict

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mp = defaultdict(int)
        for i in nums:
            mp[(i % value + value) % value] += 1
        ans = 0
        while mp[ans % value]:
            mp[ans % value] -= 1
            ans += 1
        return ans
