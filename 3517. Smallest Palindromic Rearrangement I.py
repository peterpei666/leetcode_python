class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        mp = [0] * 26
        for i in range(n):
            mp[ord(s[i]) - ord('a')] += 1
        ans = ""
        odd = -1
        for i in range(26):
            while mp[i] > 1:
                mp[i] -= 2
                ans += chr(ord('a') + i)
            if mp[i]:
                odd = i
        temp = ans[::-1]
        if odd == -1:
            return ans + temp
        return ans + chr(ord('a') + odd) + temp
