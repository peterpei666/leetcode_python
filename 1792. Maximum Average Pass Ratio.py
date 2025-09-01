from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        pq = []
        for i in range(n):
            temp = (classes[i][0] + 1) / (classes[i][1] + 1) - classes[i][0] / classes[i][1]
            heapq.heappush(pq, (-temp, i))
        while extraStudents:
            i = pq[0][1]
            heapq.heappop(pq)
            extraStudents -= 1
            classes[i][0] += 1
            classes[i][1] += 1
            temp = (classes[i][0] + 1) / (classes[i][1] + 1) - classes[i][0] / classes[i][1]
            heapq.heappush(pq, (-temp, i))
        ans = 0.0
        for i in range(n):
            ans += classes[i][0] / classes[i][1]
        return ans / n
