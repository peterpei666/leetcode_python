class Solution:
    def removeZeros(self, n: int) -> int:
        ans, temp = 0, 1
        while n:
            if n % 10:
                ans += (n % 10) * temp
                temp *= 10
            n //= 10
        return ans
