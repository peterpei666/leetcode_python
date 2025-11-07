class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = []
        for c in s:
            if c.isupper():
                t.append(c.lower())
            elif c.islower() or c.isdigit():
                t.append(c)
        return t == t[::-1]
