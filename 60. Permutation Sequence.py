class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = [''] * n
        used = 0
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        k -= 1
        for i in range(n):
            m = k // factorial[n - i - 1]
            k %= factorial[n - i - 1]
            for j in range(1, n + 1):
                if used & (1 << (j - 1)):
                    continue
                if m == 0:
                    ans[i] = str(j)
                    used |= 1 << (j - 1)
                    break
                else:
                    m -= 1
        return "".join(ans)
