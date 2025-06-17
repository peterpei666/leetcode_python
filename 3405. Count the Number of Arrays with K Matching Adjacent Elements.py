class Solution:
    mod = 10**9 + 7
    fact = [0] * 100001
    inv_fact = [0] * 100001
    ready = False

    def qpow(x: int, y: int) -> int:
        res = 1
        while y:
            if y & 1:
                res = res * x % Solution.mod
            x = x * x % Solution.mod
            y >>= 1
        return res
    
    def init():
        Solution.fact[0] = 1
        for i in range(1, 100001):
            Solution.fact[i] = Solution.fact[i - 1] * i % Solution.mod
        
        Solution.inv_fact[100000] = Solution.qpow(Solution.fact[100000], Solution.mod - 2)
        for i in range(99999, -1, -1):
            Solution.inv_fact[i] = Solution.inv_fact[i + 1] * (i + 1) % Solution.mod
        
    def comb(n: int, k: int) -> int:
        return Solution.fact[n] * Solution.inv_fact[k] % Solution.mod * Solution.inv_fact[n - k] % Solution.mod
    
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        if not Solution.ready:
            Solution.init()
            Solution.ready = True
        return Solution.comb(n - 1, k) * m * Solution.qpow(m - 1, n - k - 1) % Solution.mod
