from collections import deque
from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        map = defaultdict(list)
        for i in range(n):
            map[arr[i]].append(i)
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        cnt = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == n - 1:
                    return cnt
                for next in map[arr[cur]]:
                    if visited[next] == False:
                        q.append(next)
                        visited[next] = True
                map[arr[cur]] = []
                if cur + 1 < n and visited[cur + 1] == False:
                    visited[cur + 1] = True
                    q.append(cur + 1)
                if cur - 1 >= 0 and visited[cur - 1] == False:
                    visited[cur - 1] = True
                    q.append(cur - 1)
            cnt += 1
        return -1
