class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        pq = []
        for x, n in mp.items():
            heappush(pq, (n, x))
            if len(pq) > k:
                heappop(pq)
        ans = []
        while pq:
            ans.append(heappop(pq)[1])
        return ans[::-1]
