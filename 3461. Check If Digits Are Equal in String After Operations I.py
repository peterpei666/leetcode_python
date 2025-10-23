class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def nCr_mod2(n: int, r: int) -> int:
            return ((r & ~n) == 0)
        
        def nCr_mod5(n: int, r: int) -> int:
            p = 5
            fact = [1, 1, 2, 1, 4]
            invfact = [1, 1, 3, 1, 4]
            res = 1
            while n > 0 or r > 0:
                ni = n % p
                ri = r % p
                if ri > ni:
                    return 0
                val = fact[ni] * invfact[ri] % p * invfact[ni - ri] % p
                res = res * val % p
                n //= p
                r //= p
            return res
        
        def nCr_mod10(n: int, r: int) -> int:
            a2 = nCr_mod2(n, r)
            a5 = nCr_mod5(n, r)
            for i in range(10):
                if i % 2 == a2 and i % 5 == a5:
                    return i
            return 0
        
        n = len(s)
        memo = [0] * (n // 2 + 1)
        if n <= 1:
            return True
        m = n - 2
        memo[0] = 1
        for i in range(1, m // 2 + 2):
            memo[i] = nCr_mod10(m, i)
        temp1, temp2 = 0, 0
        for i in range(n - 1):
            temp1 = (temp1 + (ord(s[i]) - ord('0')) * memo[min(i, m - i)]) % 10
            temp2 = (temp2 + (ord(s[i + 1]) - ord('0')) * memo[min(i, m - i)]) % 10
        return temp1 == temp2
