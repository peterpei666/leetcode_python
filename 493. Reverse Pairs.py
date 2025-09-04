from typing import List
import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        fenwick = [0] * (n + 1)
        temp = nums[:]
        temp.sort()

        def query(i: int) -> int:
            ans = 0
            while i > 0:
                ans += fenwick[i]
                i -= i & (-i)
            return ans
        
        def update(i: int, x: int) -> None:
            while i <= n:
                fenwick[i] += x
                i += i & (-i)

        ans = 0
        for i in range(n):
            idx = bisect.bisect_left(temp, 2 * nums[i] + 1) + 1
            ans += query(n) - query(idx - 1)
            updateIdx = bisect.bisect_left(temp, nums[i]) + 1
            update(updateIdx, 1)
        return ans
