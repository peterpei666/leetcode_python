class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(60):
            x = num1 - num2 * i
            if x < i:
                break
            if x.bit_count() <= i:
                return i
        return -1
