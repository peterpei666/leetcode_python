from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        n = len(original)
        m = len(source)
        dis = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dis[i][i] = 0
        for i in range(n):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            dis[u][v] = min(dis[u][v], cost[i])
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        ans = 0
        for i in range(m):
            x = ord(source[i]) - ord('a')
            y = ord(target[i]) - ord('a')
            if dis[x][y] == INF:
                return -1
            ans += dis[x][y]
        return ans
