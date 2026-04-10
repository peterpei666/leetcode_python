from typing import List, DefaultDict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = DefaultDict(list)
        for i, x in enumerate(nums):
            mp[x].append(i)
        ans = 10 ** 9
        for _, pos in mp.items():
            if len(pos) < 3:
                continue
            for i in range(len(pos) - 2):
                ans = min(ans, 2 * (pos[i + 2] - pos[i]))
        return -1 if ans == 10 ** 9 else ans
