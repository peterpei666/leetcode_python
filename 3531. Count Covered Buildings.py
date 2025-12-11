from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x1 = [float('inf')] * (n + 1)
        x2 = [0] * (n + 1)
        y1 = x1[:]
        y2 = x2[:]
        for x, y in buildings:
            x1[y] = min(x1[y], x)
            x2[y] = max(x2[y], x)
            y1[x] = min(y1[x], y)
            y2[x] = max(y2[x], y)
        ans = 0
        for x, y in buildings:
            if x1[y] < x < x2[y] and y1[x] < y < y2[x]:
                ans += 1
        return ans
