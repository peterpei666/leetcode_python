from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def rebalance(self) -> None:
        while len(self.q1) > len(self.q2):
            self.q2.appendleft(self.q1.pop())
        while len(self.q2) > len(self.q1) + 1:
            self.q1.append(self.q2.popleft())

    def pushFront(self, val: int) -> None:
        self.q1.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        self.q1.append(val)
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.q2.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if not self.q1 and not self.q2:
            return -1
        if not self.q1:
            ans = self.q2[0]
            self.q2.popleft()
        else:
            ans = self.q1[0]
            self.q1.popleft()
        self.rebalance()
        return ans

    def popMiddle(self) -> int:
        if not self.q1 and not self.q2:
            return -1
        if len(self.q2) > len(self.q1):
            ans = self.q2[0]
            self.q2.popleft()
        else:
            ans = self.q1[-1]
            self.q1.pop()
        self.rebalance()
        return ans

    def popBack(self) -> int:
        if not self.q2:
            return -1
        ans = self.q2[-1]
        self.q2.pop()
        self.rebalance()
        return ans
