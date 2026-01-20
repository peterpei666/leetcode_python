class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        n = len(s)
        v = 0
        c = 0
        for i in range(n):
            if s[i] in 'aeiou':
                v += 1
            elif s[i].isalpha() and s[i].islower():
                c += 1
        return v // c if c else 0
