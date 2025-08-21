from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def is_pal(s: str, m: int) -> bool:
            for i in range(m // 2):
                if not s[i] == s[m - i - 1]:
                    return False
            return True
        
        mp = dict()
        n = len(words)
        for i in range(n):
            mp[words[i][::-1]] = i
        ans = []
        if "" in mp:
            temp = mp[""]
            for i in range(n):
                if temp == i:
                    continue
                if is_pal(words[i], len(words[i])):
                    ans.append([i, temp])
        for i in range(n):
            left = ""
            m = len(words[i])
            for j in range(m):
                left += words[i][j]
                if left in mp and not mp[left] == i and is_pal(words[i][j+1:], m - j - 1):
                    ans.append([i, mp[left]])
                if words[i][j+1:] in mp and not mp[words[i][j+1:]] == i and is_pal(left, j + 1):
                    ans.append([mp[words[i][j+1:]], i])
        return ans
