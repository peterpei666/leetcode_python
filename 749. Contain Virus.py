from typing import List

class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        regions = []
        frontiers = []
        perimeters = []

        def neighbor(r: int, c: int) -> List[int]:
            ans = []
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n:
                    ans.append((nr, nc))
            return ans
        
        def dfs(r: int, c: int) -> None:
            if (r, c) not in seen:
                seen.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in neighbor(r, c):
                    if grid[nr][nc] == 1:
                        dfs(nr, nc)
                    elif grid[nr][nc] == 0:
                        frontiers[-1].add((nr, nc))
                        perimeters[-1] += 1

        ans = 0
        while True:
            seen = set()
            regions = []
            frontiers = []
            perimeters = []
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in seen:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)
                        dfs(r, c)
            if not regions:
                break
            triage_index = frontiers.index(max(frontiers, key = len))
            ans += perimeters[triage_index]
            for i, reg in enumerate(regions):
                if i == triage_index:
                    for r, c in reg:
                        grid[r][c] = -1
                else:
                    for r, c in reg:
                        for nr, nc in neighbor(r, c):
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = 1
        return ans
