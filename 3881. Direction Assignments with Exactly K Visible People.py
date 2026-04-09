class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod = 10 ** 9 + 7
        
        def C(n: int, k: int) -> int:
            if k < 0 or k > n:
                return 0
            if k == 0 or k == n:
                return 1
            if k > n // 2:
                k = n - k
            a, b = 1, 1
            for i in range(k):
                a = (a * (n - i)) % mod
                b = (b * (i + 1)) % mod
            return (a * pow(b, mod - 2, mod)) * mod
        
        return (C(n - 1, k) * 2) % mod
