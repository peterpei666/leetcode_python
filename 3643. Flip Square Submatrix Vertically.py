from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(y, y + k):
            l, r = x, x + k - 1
            while l < r:
                grid[l][i], grid[r][i] = grid[r][i], grid[l][i]
                l += 1
                r -= 1
        return grid
