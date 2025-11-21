class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        valid = [False] * 26
        mp = [[0] * 26 for _ in range(26)]
        last = [-1] * 26
        n = len(s)
        cnt = 0
        for i in range(n - 1, -1, -1):
            if last[ord(s[i]) - ord('a')] == -1:
                cnt += 1
                last[ord(s[i]) - ord('a')] = i
                if cnt == 26:
                    break
        for i in range(n):
            if i == last[ord(s[i]) - ord('a')]:
                valid[ord(s[i]) - ord('a')] = False
            for k in range(26):
                if valid[k]:
                    mp[k][ord(s[i]) - ord('a')] = 1
            if not i == last[ord(s[i]) - ord('a')]:
                valid[ord(s[i]) - ord('a')] = True
        return sum(sum(a) for a in mp)
