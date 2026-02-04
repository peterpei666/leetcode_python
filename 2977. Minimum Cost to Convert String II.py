from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = float('inf')
        dist = [[inf] * 201 for _ in range(201)]
        id_map = {}
        sz = 0
        m = len(original)
        n = len(source)
        lengths = set()
        for i in range(m):
            if original[i] not in id_map:
                id_map[original[i]] = sz
                sz += 1
                lengths.add(len(original[i]))
            if changed[i] not in id_map:
                id_map[changed[i]] = sz
                sz += 1
            u = id_map[original[i]]
            v = id_map[changed[i]]
            dist[u][v] = min(dist[u][v], cost[i])
        for i in range(sz):
            dist[i][i] = 0
        for k in range(sz):
            for i in range(sz):
                if dist[i][k] != inf:
                    for j in range(sz):
                        if dist[k][j] != inf:
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == inf:
                continue
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            for l in lengths:
                if i + l <= n:
                    u = source[i:i + l]
                    v = target[i:i + l]
                    if u in id_map and v in id_map and dist[id_map[u]][id_map[v]] != inf:
                        dp[i + l] = min(dp[i + l], dp[i] + dist[id_map[u]][id_map[v]])
        return -1 if dp[n] == inf else dp[n]
