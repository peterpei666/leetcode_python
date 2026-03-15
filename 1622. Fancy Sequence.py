class Fancy:
    def __init__(self):
        self.v = []
        self.a = [1]
        self.b = [0]
        self.mod = 10 ** 9 + 7

    def append(self, val: int) -> None:
        self.v.append(val)
        self.a.append(self.a[-1])
        self.b.append(self.b[-1])

    def addAll(self, inc: int) -> None:
        self.b[-1] = (self.b[-1] + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a[-1] = (self.a[-1] * m) % self.mod
        self.b[-1] = (self.b[-1] * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx < 0 or idx >= len(self.v):
            return -1
        ta = pow(self.a[idx], self.mod - 2, self.mod) * self.a[-1] % self.mod
        tb = (self.b[-1] - self.b[idx] * ta % self.mod + self.mod) % self.mod
        return (ta * self.v[idx] % self.mod + tb) % self.mod
