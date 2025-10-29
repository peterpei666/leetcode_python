from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        candidates.sort()
        n = len(candidates)

        def dfs(idx: int, cur: int) -> None:
            nonlocal temp, ans
            if cur == target:
                ans.append(temp[:])
                return
            if cur > target or idx == n:
                return
            temp.append(candidates[idx])
            dfs(idx, cur + candidates[idx])
            temp.pop()
            dfs(idx + 1, cur)
        
        dfs(0, 0)
        return ans
