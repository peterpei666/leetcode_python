from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        m, n = len(factory), len(robot)
        dp = [[0] * (m + 1)] + [[10 ** 18] * (m + 1) for _ in range(n)]
        for j in range(1, m + 1):
            pos, limit = factory[j - 1]
            for i in range(n + 1):
                dp[i][j] = dp[i][j - 1]
                dis = 0
                for k in range(1, min(i, limit) + 1):
                    dis += abs(robot[i - k] - pos)
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + dis)
        return dp[-1][-1]
