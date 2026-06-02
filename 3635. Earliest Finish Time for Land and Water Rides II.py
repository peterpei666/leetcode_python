from typing import List

class Solution:
    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
        n = len(ls)
        m = len(ws)
        first1 = min(ls[i] + ld[i] for i in range(n))
        ans1 = min(max(first1, ws[i]) + wd[i] for i in range(m))
        first2 = min(ws[i] + wd[i] for i in range(m))
        ans2 = min(max(first2, ls[i]) + ld[i] for i in range(n))
        return min(ans1, ans2)
