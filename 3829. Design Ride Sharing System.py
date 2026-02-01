from collections import deque
from typing import List

class RideSharingSystem:
    def __init__(self):
        self.rider = deque()
        self.driver = deque()
        self.valid = set()

    def addRider(self, riderId: int) -> None:
        self.rider.append(riderId)
        self.valid.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driver.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.rider:
            if not self.rider[0] in self.valid:
                self.rider.popleft()
            else:
                break
        ans = [-1, -1]
        if self.rider and self.driver:
            ans = [self.driver[0], self.rider[0]]
            self.rider.popleft()
            self.driver.popleft()
            self.valid.remove(ans[1])
        return ans

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.valid:
            self.valid.remove(riderId)
