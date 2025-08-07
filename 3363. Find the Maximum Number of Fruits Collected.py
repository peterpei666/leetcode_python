from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = sum(fruits[i][i] for i in range(n))

        def dp() -> int:
            pre = [float('-inf')] * n
            cur = [float('-inf')] * n
            pre[-1] = fruits[0][-1]
            for i in range(1, n - 1):
                for j in range(max(i + 1, n - i - 1), n):
                    best = pre[j]
                    if j >= 1:
                        best = max(best, pre[j - 1])
                    if j < n - 1:
                        best = max(best, pre[j + 1])
                    cur[j] = best + fruits[i][j]
                pre, cur = cur, pre
            return pre[-1]
        
        ans += dp()
        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
        ans += dp()
        return ans
