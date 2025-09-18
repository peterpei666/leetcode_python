from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        n = len(nums)
        sz = [0] * n
        col = [1] * n
        r = float('-inf')
        for i in range(n):
            r = max(r, nums[i][0])
            sz[i] = len(nums[i])
            heapq.heappush(pq, (nums[i][0], i))
        ans_l, ans_r = 0, 0
        dif = float('inf')
        while len(pq) == n:
            l = pq[0][0]
            row = pq[0][1]
            if r - l < dif:
                ans_l = l
                ans_r = r
                dif = r - l
            heapq.heappop(pq)
            if col[row] < sz[row]:
                r = max(r, nums[row][col[row]])
                heapq.heappush(pq, (nums[row][col[row]], row))
                col[row] += 1
        return [ans_l, ans_r]
