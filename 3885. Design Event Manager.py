from heapq import heappush, heappop

class EventManager:
    def __init__(self, events: list[list[int]]):
        self.mp = dict()
        self.pq = []
        for id, p in events:
            self.mp[id] = p
            heappush(self.pq, (-p, id))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        if eventId in self.mp:
            self.mp[eventId] = newPriority
            heappush(self.pq, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.pq:
            p, id = heappop(self.pq)
            if id in self.mp and self.mp[id] == -p:
                del self.mp[id]
                return id
        return -1
