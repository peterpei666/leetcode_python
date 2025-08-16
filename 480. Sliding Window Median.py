from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        mp = defaultdict(int)
        maxheap = []
        minheap = []
        max_sz, min_sz = 0, 0
        n = len(nums)

        def prune(heap) -> None:
            while heap:
                num = heap[0]
                if heap is maxheap:
                    num = -num
                if num in mp:
                    heappop(heap)
                    mp[num] -= 1
                    if mp[num] == 0:
                        del mp[num]
                else:
                    break

        def rebalance() -> None:
            nonlocal max_sz, min_sz
            if max_sz > min_sz + 1:
                heappush(minheap, -heappop(maxheap))
                max_sz -= 1
                min_sz += 1
                prune(maxheap)
            elif min_sz > max_sz:
                heappush(maxheap, -heappop(minheap))
                min_sz -= 1
                max_sz += 1
                prune(minheap)

        for i in range(k):
            if not maxheap or nums[i] <= -maxheap[0]:
                heappush(maxheap, -nums[i])
                max_sz += 1
            else:
                heappush(minheap, nums[i])
                min_sz += 1
            rebalance()
        ans = []
        ans.append(float(-maxheap[0]) if k % 2 else (-maxheap[0] + minheap[0]) / 2.0)
        for i in range(k, n):
            if nums[i] <= -maxheap[0]:
                heappush(maxheap, -nums[i])
                max_sz += 1
            else:
                heappush(minheap, nums[i])
                min_sz += 1
            mp[nums[i - k]] += 1
            if nums[i - k] <= -maxheap[0]:
                max_sz -= 1
                if nums[i - k] == -maxheap[0]:
                    prune(maxheap)
            else:
                min_sz -= 1
                if minheap and nums[i - k] == minheap[0]:
                    prune(minheap)
            rebalance()
            ans.append(float(-maxheap[0]) if k % 2 else (-maxheap[0] + minheap[0]) / 2.0)
        return ans
