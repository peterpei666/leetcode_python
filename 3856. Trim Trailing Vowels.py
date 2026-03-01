class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        n = len(s) - 1
        while n >= 0 and s[n] in 'aeiou':
            n -= 1
        return s[:n + 1]
