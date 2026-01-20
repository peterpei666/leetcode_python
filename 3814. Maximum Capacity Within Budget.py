from typing import List

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)
        t = [(costs[i] << 32) | capacity[i] for i in range(n)]
        t.sort()
        pre = [0] * n
        m = 0
        for i in range(n):
            m = max(m, t[i] & 0xFFFFFFFF)
            pre[i] = m
        ans = 0
        j = n - 1
        for i in range(n):
            c = t[i] >> 32
            v = t[i] & 0xFFFFFFFF
            if c < budget:
                ans = max(ans, v)
            while j >= 0 and (t[j] >> 32) + c >= budget:
                j -= 1
            k = min(i - 1, j)
            if k >= 0:
                ans = max(ans, v + pre[k])
        return ans
