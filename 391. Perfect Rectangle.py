from typing import List
from collections import defaultdict

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        mp = defaultdict(int)
        for rec in rectangles:
            mp[(rec[0], rec[1])] += 1
            mp[(rec[0], rec[3])] -= 1
            mp[(rec[2], rec[1])] -= 1
            mp[(rec[2], rec[3])] += 1
        cnt = 0
        for x in mp.values():
            if not x == 0:
                if not abs(x) == 1:
                    return False
                cnt += 1
        return cnt == 4
