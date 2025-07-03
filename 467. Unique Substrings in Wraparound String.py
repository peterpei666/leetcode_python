class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        mp = [0] * 26
        max_len = 0
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) + 26) % 26 == 1:
                max_len += 1
            else:
                max_len = 1
            index = ord(s[i]) - ord('a')
            mp[index] = max(mp[index], max_len)
        return sum(mp)
