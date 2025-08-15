class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n & 3:
                return False
            n >>= 2
        return n == 1
