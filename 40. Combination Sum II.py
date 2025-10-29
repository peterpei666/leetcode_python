from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        cnt = []
        candidates.sort()
        for i in candidates:
            if not cnt or not cnt[-1][0] == i:
                cnt.append([i, 1])
            else:
                cnt[-1][1] += 1
        n = len(cnt)

        def dfs(idx: int, cur: int) -> None:
            nonlocal temp, ans
            if cur == target:
                ans.append(temp[:])
                return
            if cur > target or idx == n:
                return
            if cnt[idx][1] > 0:
                temp.append(cnt[idx][0])
                cnt[idx][1] -= 1
                dfs(idx, cur + cnt[idx][0])
                temp.pop()
                cnt[idx][1] += 1
            dfs(idx + 1, cur)
        
        dfs(0, 0)
        return ans
