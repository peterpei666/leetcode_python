from math import ceil

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        m = int(n)
        k = m.bit_length()

        def cal(base: int, k: int) -> int:
            ans = 1
            cur = 1
            for i in range(1, k):
                if cur > m // base:
                    return m + 1
                cur *= base
                if ans > m - cur:
                    return m + 1
                ans += cur
            return ans
        
        for i in range(k, 1, -1):
            l = 2
            r = ceil(pow(m, 1 / (i - 1))) + 1
            while l <= r:
                mid = (l + r) // 2
                sum = cal(mid, i)
                if sum == m:
                    return str(mid)
                elif sum < m:
                    l = mid + 1
                else:
                    r = mid - 1
        return str(m - 1) 
