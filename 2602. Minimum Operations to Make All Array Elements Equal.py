import bisect

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        ret = []
        for q in queries:
            p = bisect.bisect_left(nums, q)
            ret.append(q * (2 * p - n) + prefix[n] - 2 * prefix[p])
        return ret
