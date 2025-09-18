from typing import List
import heapq

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.mp = dict()
        for task in tasks:
            heapq.heappush(self.pq, (-task[2], -task[1]))
            self.mp[task[1]] = (task[0], task[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.pq, (-priority, -taskId))
        self.mp[taskId] = (userId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.pq, (-newPriority, -taskId))
        userId = self.mp[taskId][0]
        self.mp[taskId] = (userId, newPriority)

    def rmv(self, taskId: int) -> None:
        del self.mp[taskId]

    def execTop(self) -> int:
        while self.pq:
            p, t = self.pq[0]
            if not -t in self.mp or not self.mp[-t][1] == -p:
                heapq.heappop(self.pq)
            else:
                break
        if self.pq:
            _, t = self.pq[0]
            heapq.heappop(self.pq)
            ans = self.mp[-t][0]
            del self.mp[-t]
            return ans
        else:
            return -1
