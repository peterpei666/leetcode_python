class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pos = [[-1] for _ in range(26)]
        n = len(s)
        for i in range(n):
            pos[ord(s[i]) - ord('A')].append(i)
        for i in range(26):
            pos[i].append(n)
        return sum(sum((p[i] - p[i - 1]) * (p[i + 1] - p[i]) for i in range(1, len(p) - 1)) for p in pos)
