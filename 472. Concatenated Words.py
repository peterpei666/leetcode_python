class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        mp = set()
        for w in words:
            mp.add(w)
        ans = []
        dp = []

        def dfs(s: str, l: int, cnt: int) -> bool:
            nonlocal dp
            if l == len(s):
                return cnt > 1
            if not dp[l] == -1:
                return True if dp[l] == 1 else False
            temp = ""
            for i in range(l, len(s)):
                temp += s[i]
                if temp in mp:
                    if dfs(s, i + 1, cnt + 1):
                        dp[l] = 1
                        return True
            dp[l] = 0
            return False
        
        for w in words:
            dp = [-1] * len(w)
            if dfs(w, 0, 0):
                ans.append(w)
        return ans
