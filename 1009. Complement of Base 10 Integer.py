class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans, i = 0, 0
        while (1 << i) <= n:
            if (n & (1 << i)) == 0:
                ans |= 1 << i
            i += 1
        return ans
