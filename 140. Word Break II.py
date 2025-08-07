from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mp = set(wordDict)
        ans = []
        path = ""
        n = len(s)

        def dfs(i: int) -> None:
            nonlocal path, ans
            if i == n:
                ans.append(path)
                return
            for j in range(i + 1, n + 1):
                if s[i:j] in mp:
                    m = len(path)
                    if m:
                        path += " "
                    path += s[i:j]
                    dfs(j)
                    path = path[:m]
        
        dfs(0)
        return ans
