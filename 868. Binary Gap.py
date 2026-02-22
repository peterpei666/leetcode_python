class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        temp = -100
        while n:
            if n & 1:
                ans = max(ans, temp)
                temp = 0
            n >>= 1
            temp += 1
        return ans
