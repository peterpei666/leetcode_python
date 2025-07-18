import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        sum1 = sum(nums[:n])
        pq1 = [-x for x in nums[:n]]
        heapq.heapify(pq1)
        left = [0] * (n + 1)
        left[0] = sum1
        for i in range(n, 2 * n):
            sum1 += nums[i]
            heapq.heappush(pq1, -nums[i])
            sum1 -= -heapq.heappop(pq1)
            left[i - n + 1] = sum1
        sum2 = sum(nums[2 * n:])
        pq2 = nums[2 * n:]
        heapq.heapify(pq2)
        ans = left[n] -sum2
        for i in range(2 * n - 1, n - 1, -1):
            sum2 += nums[i]
            heapq.heappush(pq2, nums[i])
            sum2 -= heapq.heappop(pq2)
            ans = min(ans, left[i - n] - sum2)
        return ans
