class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while not n == 1:
            ans += 1
            if n & 1:
                if not n == 3 and (n & 3) == 3:
                    n += 1
                else:
                    n -= 1
            else:
                n >>= 1
        return ans
