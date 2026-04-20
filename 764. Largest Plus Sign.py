from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mp = [[False] * n for _ in range(n)]
        for m in mines:
            mp[m[0]][m[1]] = True
        ans = [[1000] * n for _ in range(n)]
        for i in range(n):
            cur = 0
            for j in range(n):
                if mp[i][j]:
                    cur = 0
                else:
                    cur += 1
                ans[i][j] = min(ans[i][j], cur)
            cur = 0
            for j in range(n - 1, -1, -1):
                if mp[i][j]:
                        cur = 0
                else:
                    cur += 1
                ans[i][j] = min(ans[i][j], cur)
        for j in range(n):
            cur = 0
            for i in range(n):
                if mp[i][j]:
                    cur = 0
                else:
                    cur += 1
                ans[i][j] = min(ans[i][j], cur)
            cur = 0
            for i in range(n - 1, -1, -1):
                if mp[i][j]:
                        cur = 0
                else:
                    cur += 1
                ans[i][j] = min(ans[i][j], cur)
        return max(max(ans[i]) for i in range(n))
