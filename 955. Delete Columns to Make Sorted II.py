from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs[0]), len(strs)
        ordered = [False] * (n - 1)
        unordered = n - 1
        ans = 0
        for c in range(m):
            if unordered <= 0:
                break
            f = False
            for i in range(n - 1):
                if not ordered[i] and strs[i][c] > strs[i + 1][c]:
                    f = True
                    break
            if f:
                ans += 1
            else:
                for i in range(n - 1):
                    if not ordered[i] and strs[i][c] < strs[i + 1][c]:
                        ordered[i] = True
                        unordered -= 1
        return ans
