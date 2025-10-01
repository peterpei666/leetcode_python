from collections import defaultdict

class MyCalendarTwo:
    def __init__(self):
        self.mp = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        self.mp[startTime] += 1
        self.mp[endTime] -= 1
        cnt = 0
        valid = True
        for t in sorted(self.mp):
            cnt += self.mp[t]
            if cnt > 2:
                valid = False
                break
        if not valid:
            self.mp[startTime] -= 1
            self.mp[endTime] += 1
        return valid
