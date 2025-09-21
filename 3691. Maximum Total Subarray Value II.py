import math
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        logn = int(math.log2(n)) + 1
        min_table = [[0]*logn for _ in range(n)]
        max_table = [[0]*logn for _ in range(n)]
        for i in range(n):
            min_table[i][0] = max_table[i][0] = nums[i]
        for j in range(1, logn):
            for i in range(n - (1 << j) + 1):
                min_table[i][j] = min(min_table[i][j - 1], min_table[i + (1 << (j - 1))][j - 1])
                max_table[i][j] = max(max_table[i][j - 1], max_table[i + (1 << (j - 1))][j - 1])

        def query_min(l,r):
            j = int(math.log2(r - l + 1))
            return min(min_table[l][j], min_table[r - (1 << j) + 1][j])
    
        def query_max(l,r):
            j = int(math.log2(r - l + 1))
            return max(max_table[l][j], max_table[r - (1 << j) + 1][j])
    
        visited = set()
        pq = []
        val = query_max(0, n - 1) - query_min(0, n - 1)
        heapq.heappush(pq, (-val, 0, n - 1))
        visited.add((0, n - 1))
        ans = 0
        count = 0
        while pq and count < k:
            neg_val, l, r = heapq.heappop(pq)
            value = -neg_val
            ans += value
            count += 1
            if count == k:
                break
            if l < r and (l+1,r) not in visited:
                new_val = query_max(l + 1, r) - query_min(l + 1, r)
                heapq.heappush(pq, (-new_val, l+1, r))
                visited.add((l + 1,r))
            if l < r and (l, r - 1) not in visited:
                new_val = query_max(l, r - 1) - query_min(l, r - 1)
                heapq.heappush(pq, (-new_val, l, r - 1))
                visited.add((l, r - 1))
        return ans
