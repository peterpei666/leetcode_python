from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        mp = set()
        for p in obstacles:
            mp.add((p[0], p[1]))
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = 0
        d = 0
        x, y = 0, 0
        for cmd in commands:
            if cmd == -2:
                d = (d + 3) & 3
            elif cmd == -1:
                d = (d + 1) & 3
            else:
                for _ in range(cmd):
                    nx = x + dir[d][0]
                    ny = y + dir[d][1]
                    if not (nx, ny) in mp:
                        x = nx
                        y = ny
                        ans = max(ans, x * x + y * y)
                    else:
                        break
        return ans
