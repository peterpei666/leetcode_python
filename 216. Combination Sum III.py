from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        temp = []
        cur = 0

        def dfs() -> None:
            nonlocal cur
            if len(temp) == k and cur == n:
                ans.append(temp[:])
                return
            start = temp[-1] + 1 if temp else 1
            for i in range(start, 10):
                temp.append(i)
                cur += i
                dfs()
                temp.pop()
                cur -= i
        
        dfs()
        return ans
