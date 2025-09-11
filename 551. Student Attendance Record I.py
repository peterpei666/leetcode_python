class Solution:
    def checkRecord(self, s: str) -> bool:
        a, l = 0, 0
        for c in s:
            if c == 'L':
                l += 1
            else:
                l = 0
            if l >= 3:
                return False
            if c == 'A':
                a += 1
        return a < 2
