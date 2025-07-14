from collections import defaultdict

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        mp = defaultdict(int)
        cur = 0
        for t in tasks:
            if t in mp and mp[t] > cur:
                cur = mp[t]
            cur += 1
            mp[t] = cur + space
        return cur
