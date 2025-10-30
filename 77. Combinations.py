from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        ans = []

        def dfs(idx: int, t: int) -> None:
            nonlocal temp, ans
            if t == k:
                ans.append(temp[:])
                return
            if n - idx + 1 < k - t:
                return
            temp.append(idx)
            dfs(idx + 1, t + 1)
            temp.pop()
            dfs(idx + 1, t)

        dfs(1, 0)
        return ans
