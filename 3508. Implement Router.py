from typing import List
from collections import defaultdict, deque
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.exist = set()
        self.dq = deque()
        self.mp = defaultdict(list)
        self.cnt = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.exist:
            return False
        if len(self.dq) == self.limit:
            self.forwardPacket()
        self.exist.add((source, destination, timestamp))
        self.dq.append((source, destination, timestamp))
        self.mp[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.dq:
            return []
        source, destination, timestamp = self.dq[0]
        self.dq.popleft()
        self.exist.remove((source, destination, timestamp))
        self.cnt[destination] += 1
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return bisect.bisect_right(self.mp[destination], endTime, self.cnt[destination]) - bisect.bisect_left(self.mp[destination], startTime, self.cnt[destination]) if destination in self.mp else 0
