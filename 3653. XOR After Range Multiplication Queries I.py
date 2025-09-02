from typing import List
from math import floor, sqrt
from collections import defaultdict

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        B = max(1, floor(sqrt(n)))
        small = defaultdict(list)
        for q in queries:
            l, r, k, v = q[0], q[1], q[2], q[3]
            if k > B:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % mod
            else:
                small[k].append([l, r, k, v])
        for k in small:
            prod = [[] for _ in range(k)]
            zero = [[] for _ in range(k)]
            for rem in range(k):
                l = 0
                if rem < n:
                    l = (n - 1 - rem) // k + 1
                prod[rem] = [1] * (l + 1)
                zero[rem] = [0] * (l + 1)
            for arr in small[k]:
                l, r, v = arr[0], arr[1], arr[3]
                rem = l % k
                j0, j1 = (l - rem) // k, (r - rem) // k
                sz = len(prod[rem])
                vm = (v % mod + mod) % mod
                if vm == 0:
                    zero[rem][j0] += 1
                    if j1 + 1 < sz:
                        zero[rem][j1 + 1] -= 1
                else:
                    prod[rem][j0] = prod[rem][j0] * vm % mod
                    if j1 + 1 < sz:
                        inv = pow(vm, mod - 2, mod)
                        prod[rem][j1 + 1] = prod[rem][j1 + 1] * inv % mod
            for rem in range(k):
                l = len(prod[rem]) - 1
                cur = 1
                cnt = 0
                for j in range(l):
                    cnt += zero[rem][j]
                    cur = cur * prod[rem][j] % mod
                    idx = rem + j * k
                    if idx >= n:
                        break
                    mult = 0 if cnt > 0 else cur
                    nums[idx] = nums[idx] * mult % mod
        ans = 0
        for x in nums:
            ans ^= x
        return ans
