class Solution:
    def clumsy(self, n: int) -> int:
        ans = [1, 2 ,2, -1, 0, 0, 3, 3]
        return n + (ans[n % 4]  if n > 4 else ans[n + 3])
