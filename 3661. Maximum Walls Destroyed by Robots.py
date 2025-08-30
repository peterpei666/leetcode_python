from typing import List
import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        temp = []
        for i in range(n):
            temp.append([robots[i], distance[i]])
        temp.sort()
        walls.sort()
        dp = [[0] * 2 for _ in range(2)]

        def count(l: int, r: int) -> int:
            if l > r:
                return 0
            return bisect.bisect_right(walls, r) - bisect.bisect_left(walls, l)
        
        dp[0][0] = count(temp[0][0] - temp[0][1], temp[0][0])
        dp[0][1] = count(temp[0][0], min(temp[0][0] + temp[0][1], (temp[1][0] - 1 if n > 1 else 10 ** 10)))
        for i in range(1, n - 1):
            res = 0
            res = max(res, dp[(i - 1) % 2][0] + count(max(temp[i - 1][0] + 1, temp[i][0] - temp[i][1]), temp[i][0]))
            res = max(res, dp[(i - 1) % 2][1] + count(max(temp[i - 1][0] + temp[i - 1][1] + 1, temp[i][0] - temp[i][1]), temp[i][0]))
            dp[i % 2][0] = res
            res = 0
            res = max(res, dp[(i - 1) % 2][0] + count(temp[i][0], min(temp[i][0] + temp[i][1], temp[i + 1][0] - 1)))
            res = max(res, dp[(i - 1) % 2][1] + count(temp[i][0], min(temp[i][0] + temp[i][1], temp[i + 1][0] - 1)))
            dp[i % 2][1] = res
        if n > 1:
            res = 0
            res = max(res, dp[(n - 2) % 2][0] + count(max(temp[n - 2][0] + 1, temp[n - 1][0] - temp[n - 1][1]), temp[n - 1][0]))
            res = max(res, dp[(n - 2) % 2][1] + count(max(temp[n - 2][0] + temp[n - 2][1] + 1, temp[n - 1][0] - temp[n - 1][1]), temp[n - 1][0]))
            dp[(n - 1) % 2][0] = res
            res = 0
            res = max(res, dp[(n - 2) % 2][0] + count(temp[n - 1][0], temp[n - 1][0] + temp[n - 1][1]))
            res = max(res, dp[(n - 2) % 2][1] + count(temp[n - 1][0], temp[n - 1][0] + temp[n - 1][1]))
            dp[(n - 1) % 2][1] = res
        return max(dp[(n - 1) % 2][0], dp[(n - 1) % 2][1])
