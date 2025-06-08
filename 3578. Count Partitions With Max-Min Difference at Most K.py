from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        pre = [0] * (n + 1)
        pre[0] = 1
        minq = deque()
        maxq = deque()
        j = 0
        for i in range(0, n):
            while minq and nums[minq[-1]] > nums[i]:
                minq.pop()
            minq.append(i)
            while maxq and nums[maxq[-1]] < nums[i]:
                maxq.pop()
            maxq.append(i)
            while minq and maxq and nums[maxq[0]] - nums[minq[0]] > k:
                if minq[0] == j:
                    minq.popleft()
                if maxq[0] == j:
                    maxq.popleft()
                j += 1
            if j > 0:
                dp[i + 1] = ((pre[i] - pre[j - 1]) % mod) % mod
            else:
                dp[i + 1] = pre[i] % mod
            pre[i + 1] = (pre[i] + dp[i + 1]) % mod
        return dp[n]
            
