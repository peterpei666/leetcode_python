from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = pre[i + 1][j] + pre[i][j + 1] - pre[i][j] + mat[i][j]
        l = 1
        r = min(m, n)
        ans = 0
        while l <= r:
            valid = False
            mid = (l + r + 1) // 2
            for i in range(1, m + 1):
                if valid:
                    break
                for j in range(1, n + 1):
                    if i + mid - 1 <= m and j + mid - 1 <= n:
                        if pre[i + mid - 1][j + mid - 1] - pre[i + mid - 1][j - 1] - pre[i - 1][j + mid - 1] + pre[i - 1][j - 1] <= threshold:
                            valid = True
                            break
            if valid:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
