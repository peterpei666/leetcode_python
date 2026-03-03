from collections import deque

class TextEditor:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def addText(self, text: str) -> None:
        for c in text:
            self.q1.append(c)

    def deleteText(self, k: int) -> int:
        ans = min(k, len(self.q1))
        for i in range(ans):
            self.q1.pop()
        return ans

    def cursorLeft(self, k: int) -> str:
        for i in range(k):
            if not self.q1:
                break
            c = self.q1.pop()
            self.q2.appendleft(c)
        l = min(10, len(self.q1))
        s = []
        for i in range(l):
            s.append(self.q1.pop())
        s.reverse()
        for c in s:
            self.q1.append(c)
        return ''.join(s)

    def cursorRight(self, k: int) -> str:
        for i in range(k):
            if not self.q2:
                break
            c = self.q2.popleft()
            self.q1.append(c)
        l = min(10, len(self.q1))
        s = []
        for i in range(l):
            s.append(self.q1.pop())
        s.reverse()
        for c in s:
            self.q1.append(c)
        return ''.join(s)
