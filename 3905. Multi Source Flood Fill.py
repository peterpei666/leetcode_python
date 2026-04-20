from collections import deque

class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        sources.sort(key=lambda x : x[2], reverse=True)
        q = deque()
        mp = [[-1] * m for _ in range(n)]
        for x, y, c in sources:
            mp[x][y] = c
            q.append((x, y))
        dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        while q:
            x, y = q[0]
            q.popleft()
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and mp[nx][ny] == -1:
                    mp[nx][ny] = mp[x][y]
                    q.append((nx, ny))
        return mp
