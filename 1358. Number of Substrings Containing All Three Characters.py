class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        r = 0
        freq = [0] * 3
        for l in range(n):
            while r < n and (freq[0] == 0 or freq[1] == 0 or freq[2] == 0):
                freq[ord(s[r]) - ord('a')] += 1
                r += 1
            if freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                count += n - r + 1
            freq[ord(s[l]) - ord('a')] -= 1
        return count
