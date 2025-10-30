class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 0, x
        ans = 0
        while l < r:
            mid = (l + r) // 2
            temp = mid * mid
            if temp > x:
                r = mid
            else:
                ans = mid
                l = mid + 1
        return ans
