import bisect

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        mod = 10 ** 9 + 7
        cnt = 0
        for i in range(1, n - 1):
            l = bisect.bisect_left(prefix, 2 * prefix[i], i + 1, n)
            r = bisect.bisect_right(prefix, (prefix[-1] + prefix[i]) // 2, i + 1, n) - 1
            if l <= r:
                cnt += r - l + 1
                cnt %= mod
        return cnt
