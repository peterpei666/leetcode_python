class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            ans |= (n & 1) << i
            n >>= 1
            if not n:
                break
        return ans
