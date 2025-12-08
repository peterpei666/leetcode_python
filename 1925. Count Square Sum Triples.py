class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n):
            for b in range(a + 1, n):
                for c in range(b + 1, n + 1):
                    if a ** 2 + b ** 2 == c ** 2:
                        ans += 2
        return ans
