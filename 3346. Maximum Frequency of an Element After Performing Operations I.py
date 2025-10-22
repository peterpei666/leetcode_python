from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        N = 10 ** 5 + 2
        freq = [0] * N
        sweep = [0] * N
        l, r = N, 1
        for x in nums:
            freq[x] += 1
            t1, t2 = max(1, x - k), min(N - 1, x + k + 1)
            sweep[t1] += 1
            sweep[t2] -= 1
            l = min(l, t1)
            r = max(r, t2)
        ans, cnt = 0, 0
        for x in range(l, r + 1):
            cnt += sweep[x]
            ans = max(ans, freq[x] + min(cnt - freq[x], numOperations))
        return ans
