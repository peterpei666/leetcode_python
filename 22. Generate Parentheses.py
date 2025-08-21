from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = ""
        ans = []

        def dfs(l: int, r: int) -> None:
            nonlocal temp, ans
            if l == 0 and r == 0:
                ans.append(temp)
                return
            if l > 0:
                temp += "("
                dfs(l - 1, r + 1)
                temp = temp[:-1]
            if r > 0:
                temp += ")"
                dfs(l, r - 1)
                temp = temp[:-1]
        
        dfs(n ,0)
        return ans
