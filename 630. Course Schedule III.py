from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        pq = []
        total = 0
        for i in range(len(courses)):
            if total + courses[i][0] <= courses[i][1]:
                total += courses[i][0]
                heapq.heappush(pq, -courses[i][0])
            else:
                if pq and -pq[0] > courses[i][0]:
                    total += pq[0]
                    heapq.heappop(pq)
                    total += courses[i][0]
                    heapq.heappush(pq, -courses[i][0])
        return len(pq)
