class Solution:
    def findIntegers(self, n: int) -> int:
        f = [0] * 32
        f[0], f[1] = 1, 2
        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]
        i, ans, prev = 30, 0, 0
        while i >= 0:
            if n & (1 << i):
                ans += f[i]
                if prev:
                    ans -= 1
                    break
                prev = 1
            else:
                prev = 0
            i -= 1
        return ans
