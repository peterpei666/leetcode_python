from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i in range(n):
            if i != headID:
                graph[manager[i]].append(i)
        time = [-1] * n
        q = deque()
        q.append(headID)
        time[headID] = 0
        while q:
            cur = q.popleft()
            for i in graph[cur]:
                if time[i] == -1 or time[i] > time[cur] + informTime[cur]:
                    time[i] = time[cur] + informTime[cur]
                    if informTime[i] != 0:
                        q.append(i)
        return max(time)
