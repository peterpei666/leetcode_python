from collections import defaultdict

class MyCalendarThree:
    def __init__(self):
        self.mp = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.mp[startTime] += 1
        self.mp[endTime] -= 1
        cnt = 0
        ans = 0
        for t in sorted(self.mp):
            cnt += self.mp[t]
            ans = max(ans, cnt)
        return ans
