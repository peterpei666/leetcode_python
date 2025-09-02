from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda p: [p[0], -p[1]])
        cnt = 0
        for i in range(n):
            y = float('-inf')
            for j in range(i + 1, n):
                if points[i][1] >= points[j][1] and y < points[j][1]:
                    cnt += 1
                    y = points[j][1]
        return cnt
