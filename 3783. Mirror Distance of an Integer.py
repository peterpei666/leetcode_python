class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp = n
        rev = 0
        while temp:
            rev = rev * 10 + temp % 10
            temp //= 10
        return abs(rev - n)
