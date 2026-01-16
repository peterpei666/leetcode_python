from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences += [1, m]
        vFences += [1, n]
        hFences.sort()
        vFences.sort()
        mp = set()
        hs, vs = len(hFences), len(vFences)
        for i in range(hs):
            for j in range(i + 1, hs):
                mp.add(hFences[j] - hFences[i])
        ans = -1
        for i in range(vs):
            for j in range(i + 1, vs):
                if vFences[j] - vFences[i] in mp:
                    ans = max(ans, vFences[j] - vFences[i])
        return -1 if ans == -1 else (ans ** 2) % (10 ** 9 + 7)
