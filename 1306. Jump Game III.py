from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        q.append(start)
        visited = 0
        while q:
            cur = q.popleft()
            if cur < 0 or cur >= len(arr) or (visited & (1 << cur)):
                continue
            visited |= (1 << cur)
            if arr[cur] == 0:
                return True
            q.append(cur + arr[cur])
            q.append(cur - arr[cur])
        return False
