from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mp =set(wordDict)
        n = len(s)
        memo = [False] * n
        valid = [False] * n

        def dfs(i: int) -> bool:
            nonlocal memo, valid
            if i == n:
                return True
            if valid[i]:
                return memo[i]
            valid[i] = True
            for j in range(i + 1, n + 1):
                if s[i:j] in mp and dfs(j):
                    memo[i] = True
                    return True
            return False
        
        return dfs(0)
