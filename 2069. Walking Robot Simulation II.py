from typing import List

class Robot:
    def __init__(self, width: int, height: int):
        self.c = 2 * (width + height - 2)
        self.d = 0
        self.direction = ["East", "North", "West", "South"]
        self.w, self.h = width, height
        self.x, self.y = 0, 0

    def step(self, num: int) -> None:
        if self.c == 0:
            return
        num %= self.c
        if num == 0 and (self.x or self.y):
            return
        if num == 0 and self.x == 0 and self.y == 0:
            self.d = 3
            return
        while num > 0:
            if self.d == 0:
                move = min(num, self.w - 1 - self.x)
                self.x += move
                num -= move
                if num > 0:
                    self.d = (self.d + 1) & 3
            elif self.d == 1:
                move = min(num, self.h - 1 - self.y)
                self.y += move
                num -= move
                if num > 0:
                    self.d = (self.d + 1) & 3
            elif self.d == 2:
                move = min(num, self.x)
                self.x -= move
                num -= move
                if num > 0:
                    self.d = (self.d + 1) & 3
            else:
                move = min(num, self.y)
                self.y -= move
                num -= move
                if num > 0:
                    self.d = (self.d + 1) & 3

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.direction[self.d]
