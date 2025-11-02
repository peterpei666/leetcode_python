from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mp = [0] * (m * n)
        for g in guards:
            mp[g[0] * n + g[1]] = 2
        for w in walls:
            mp[w[0] * n + w[1]] = 2
        for g in guards:
            x, y = g[0], g[1]
            i = x - 1
            while i >= 0 and not mp[i * n + y] == 2:
                mp[i * n + y] = 1
                i -= 1
            i = x + 1
            while i < m and not mp[i * n + y] == 2:
                mp[i * n + y] = 1
                i += 1
            j = y - 1
            while j >= 0 and not mp[x * n + j] == 2:
                mp[x * n + j] = 1
                j -= 1
            j = y + 1
            while j < n and not mp[x * n + j] == 2:
                mp[x * n + j] = 1
                j += 1
        return mp.count(0)
