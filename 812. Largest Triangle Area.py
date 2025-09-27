from typing import List
from math import sqrt

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def line(a: List[int], b: List[int], c: List[int]) -> bool:
            return (b[1] - a[1]) * (c[0] - b[0]) == (c[1] - b[1]) * (b[0] - a[0])
        
        def area(a: List[int], b: List[int], c: List[int]) -> float:
            l1 = sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
            l2 = sqrt(pow(a[0] - c[0], 2) + pow(a[1] - c[1], 2))
            l3 = sqrt(pow(b[0] - c[0], 2) + pow(b[1] - c[1], 2))
            p = (l1 + l2 + l3) / 2
            return sqrt(p * (p - l1) * (p - l2) * (p - l3))

        s = 0
        n = len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if not line(points[i], points[j], points[k]):
                        s = max(s, area(points[i], points[j], points[k]))
        return s
