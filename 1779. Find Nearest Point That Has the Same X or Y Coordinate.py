class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        n = len(points)
        ans = -1
        dist = float('inf')
        for i in range(n):
            if points[i][0] == x or points[i][1] == y:
                if abs(x - points[i][0]) + abs(y - points[i][1]) < dist:
                    dist = abs(x - points[i][0]) + abs(y - points[i][1])
                    ans = i
        return ans
