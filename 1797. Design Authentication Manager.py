from collections import deque

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.q = deque()
        self.mp = dict()
        self.time = timeToLive
        self.live = 0

    def clear(self, cur: int) -> None:
        while self.q and self.q[0][1] <= cur:
            if self.mp[self.q[0][0]] == self.q[0][1]:
                del self.mp[self.q[0][0]]
                self.live -= 1
            self.q.popleft()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.clear(currentTime)
        self.live += 1
        self.mp[tokenId] = currentTime + self.time
        self.q.append((tokenId, self.mp[tokenId]))

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.clear(currentTime)
        if tokenId in self.mp:
            self.mp[tokenId] = currentTime + self.time
            self.q.append((tokenId, self.mp[tokenId]))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.clear(currentTime)
        return self.live
