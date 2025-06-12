class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        j = 0
        count = [0] * 26
        for i in range(n):
            count[ord(s[i]) - ord('a')] += 1
            while count[ord(s[i]) - ord('a')] > 2:
                count[ord(s[j]) - ord('a')] -= 1
                j += 1
            ans = max(ans, i - j + 1)
        return ans
