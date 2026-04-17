from typing import List, DefaultDict, Deque

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = Deque()
        n = len(watchedVideos)
        visited = [False] * n
        visited[id] = True
        q.append(id)
        for _ in range(level):
            sz = len(q)
            for _ in range(sz):
                cur = q[0]
                q.popleft()
                for next in friends[cur]:
                    if not visited[next]:
                        visited[next] = True
                        q.append(next)
        mp = DefaultDict(int)
        while q:
            cur = q[0]
            q.popleft()
            for v in watchedVideos[cur]:
                mp[v] += 1
        temp = sorted(list(mp.items()), key=lambda x : (x[1], x[0]))
        return [t[0] for t in temp]
