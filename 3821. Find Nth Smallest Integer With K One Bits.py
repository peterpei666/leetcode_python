class Solution:
    def __init__(self):
        self.C = [[0] * 51 for _ in range(51)]
        for i in range(51):
            self.C[i][0] = 1
            for j in range(1, i + 1):
                self.C[i][j] = self.C[i - 1][j - 1] + self.C[i - 1][j]
    
    def nthSmallest(self, n: int, k: int) -> int:
        ans = 0
        for i in range(49, -1, -1):
            if n > self.C[i][k]:
                n -= self.C[i][k]
                k -= 1
                ans |= 1 << i
                if k == 0:
                    break
        return ans
