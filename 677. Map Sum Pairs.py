from collections import defaultdict

class MapSum:
    def __init__(self):
        self.mp = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.mp[key] = val

    def sum(self, prefix: str) -> int:
        sum = 0
        for key in self.mp:
            if key.startswith(prefix):
                sum += self.mp[key]
        return sum
