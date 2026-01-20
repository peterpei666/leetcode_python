import heapq
from collections import defaultdict

class AuctionSystem:
    def __init__(self):
        self.mp = defaultdict(dict)
        self.q = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.mp[itemId][userId] = bidAmount
        heapq.heappush(self.q[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.mp[itemId][userId] = newAmount
        heapq.heappush(self.q[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        if itemId in self.mp and userId in self.mp[itemId]:
            del self.mp[itemId][userId]

    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.q:
            return -1
        while self.q[itemId]:
            neg_bid, userId = self.q[itemId][0]
            bid_amount = -neg_bid
            userId = -userId
            if userId not in self.mp[itemId] or self.mp[itemId][userId] != bid_amount:
                heapq.heappop(self.q[itemId])
            else:
                return userId
        return -1
