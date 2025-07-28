from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans |= i
        n = len(nums)
        cnt = 0
        
        def dfs(cur: int, idx: int) -> None:
            nonlocal cnt
            if cur == ans:
                cnt += 1 << (n - idx)
            elif idx < n:
                dfs(cur | nums[idx], idx + 1)
                dfs(cur, idx + 1)

        dfs(0, 0)
        return cnt
