from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)])
        ans = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                p, v = q.popleft()
                if p + v == target:
                    return ans
                q.append((p + v, v * 2))
                if (p + v > target and v > 0) or (p + v < target and v < 0):
                    q.append((p, -v // abs(v)))
            ans += 1
        return -1
