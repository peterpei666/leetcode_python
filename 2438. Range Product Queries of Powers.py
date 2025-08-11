from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        k, i = 0, 0
        bit = [0] * 32
        while n:
            if n & 1:
                bit[k] = 1 << i
                k += 1
            i += 1
            n >>= 1
        p = [[0] * k for _ in range(k)]
        mod = 10 ** 9 + 7
        for i in range(k):
            p[i][i] = bit[i]
            for j in range(i + 1, k):
                p[i][j] = p[i][j - 1] * bit[j] % mod
        ans = [0] * len(queries)
        for i in range(len(queries)):
            ans[i] = p[queries[i][0]][queries[i][1]]
        return ans
