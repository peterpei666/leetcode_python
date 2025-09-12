class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def construct(h: int, even: bool) -> int:
            ans = h
            if not even:
                h //= 10
            while h > 0:
                ans = ans * 10 + h % 10
                h //= 10
            return ans
        
        l = len(n)
        fh = int(n[:(l + 1) // 2])
        pos = []
        pos.append(construct(fh, l % 2 == 0))
        if fh > 0:
            pos.append(construct(fh - 1, l % 2 == 0))
        pos.append(construct(fh + 1, l % 2 == 0))
        pos.append(10 ** (l - 1) - 1)
        pos.append(10 ** l + 1)
        dif = float('inf')
        ans = 0
        n_val = int(n)
        for p in pos:
            if p == n_val:
                continue
            if abs(p - n_val) < dif:
                dif = abs(p - n_val)
                ans = p
            elif abs(p - n_val) == dif:
                ans = min(ans, p)
        return str(ans)
