from typing import List

class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for b in range(29, -1, -1):
            temp = ans | ((1 << b) - 1)
            p = True
            for i in range(m):
                valid = False
                for j in range(n):
                    if (grid[i][j] | temp) == temp:
                        valid = True
                        break
                if not valid:
                    p = False
                    break
            if not p:
                ans |= 1 << b
        return ans
