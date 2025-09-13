class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        t1, t2 = 0, 0
        vowel = [ord('a'), ord('e'), ord('i'), ord('o'), ord('u')]
        for i in range(26):
            if i + ord('a') in vowel:
                t1 = max(t1, cnt[i])
            else:
                t2 = max(t2, cnt[i])
        return t1 + t2
