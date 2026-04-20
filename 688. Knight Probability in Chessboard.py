class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dir = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]
        cur = [[0.0] * n for _ in range(n)]
        cur[row][column] = 1.0;
        for _ in range(k):
            next = [[0.0] * n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if cur[x][y] > 0.0:
                        for d in range(8):
                            nx = x + dir[d][0]
                            ny = y + dir[d][1]
                            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                                next[nx][ny] += cur[x][y] / 8
            cur = next
        return sum(sum(cur[i]) for i in range(n))
