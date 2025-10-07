from typing import List
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * n
        full = dict()
        dry = []
        for i, lake in enumerate(rains):
            if lake == 0:
                dry.append(i)
            else:
                ans[i] = -1
                if lake in full:
                    idx = bisect.bisect_right(dry, full[lake])
                    if idx == len(dry):
                        return []
                    ans[dry.pop(idx)] = lake
                full[lake] = i
        return ans
