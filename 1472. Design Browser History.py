from collections import deque

class BrowserHistory:
    def __init__(self, homepage: str):
        self.q1 = deque()
        self.q2 = deque()
        self.q1.append(homepage)

    def visit(self, url: str) -> None:
        self.q1.append(url)
        if self.q2:
            self.q2 = deque()

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.q1) == 1:
                break
            self.q2.appendleft(self.q1.pop())
        return self.q1[-1]

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.q2:
                break
            self.q1.append(self.q2.popleft())
        return self.q1[-1]
