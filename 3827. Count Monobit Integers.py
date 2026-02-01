class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 0
        for i in range(20):
            if n >= (1 << i) - 1:
                ans += 1
        return ans
