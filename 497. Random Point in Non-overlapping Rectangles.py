from typing import List
from bisect import bisect_right
import random

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.pre = []
        cur = 0
        for r in rects:
            cur += (r[2] - r[0] + 1) * (r[3] - r[1] + 1)
            self.pre.append(cur)

    def pick(self) -> List[int]:
        t = random.randint(0, self.pre[-1] - 1)
        idx = bisect_right(self.pre, t)
        offset = t if idx == 0 else t - self.pre[idx - 1]
        wid = self.rects[idx][2] - self.rects[idx][0] + 1
        return [self.rects[idx][0] + (offset % wid), self.rects[idx][1] + (offset // wid)]
