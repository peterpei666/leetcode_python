class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        k = -1
        while n:
            if k == n & 1:
                return False
            k = n & 1
            n >>= 1
        return True
