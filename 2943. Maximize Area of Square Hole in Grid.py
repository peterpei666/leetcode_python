from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        hs = len(hBars)
        vs = len(vBars)
        h = 1
        v = 1
        temp = 1
        for i in range(1, hs):
            if hBars[i] == hBars[i - 1] + 1:
                temp += 1
            else:
                temp = 1
            h = max(h, temp)
        temp = 1
        for i in range(1, vs):
            if vBars[i] == vBars[i - 1] + 1:
                temp += 1
            else:
                temp = 1
            v = max(v, temp)
        return (min(h, v) + 1) ** 2
