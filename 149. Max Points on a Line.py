from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = min(n, 2)
        for i in range(n - 1):
            for j in range(i + 1, n):
                temp = 2
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if (points[i][1]-points[k][1])*(points[j][0]-points[k][0])==(points[i][0]-points[k][0])*(points[j][1]-points[k][1]):
                        temp += 1
                ans = max(ans, temp)
        return ans
