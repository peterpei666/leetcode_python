class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        ans, i = 0, 1
        while temp:
            if temp % 10 == 6:
                ans = 3 * i
            i *= 10
            temp //= 10
        return num + ans
