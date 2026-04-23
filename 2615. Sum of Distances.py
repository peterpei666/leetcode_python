from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)
        cur = defaultdict(int)
        for i, x in enumerate(nums):
            cur[x] += i
            cnt[x] += 1
        ans = [0] * n
        pos = defaultdict(int)
        for i, x in enumerate(nums):
            cur[x] -= (i - pos[x]) * cnt[x]
            pos[x] = i
            cnt[x] -= 2
            ans[i] = cur[x]
        return ans
