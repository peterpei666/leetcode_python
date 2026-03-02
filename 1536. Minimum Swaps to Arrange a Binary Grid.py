from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        arr = [0] * n
        for i in range(n):
            j = 0
            while j < n and grid[i][n - 1 - j] == 0:
                j += 1
            arr[i] = j
        ans = 0
        for i in range(n):
            if arr[i] < n - i - 1:
                p = -1
                for j in range(i + 1, n):
                    if arr[j] >= n - i - 1:
                        p = j
                        break
                if p == -1:
                    return -1
                for k in range(p, i, -1):
                    arr[k], arr[k - 1] = arr[k - 1], arr[k]
                    ans += 1
        return ans
