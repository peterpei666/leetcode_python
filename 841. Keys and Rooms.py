from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        stk = [0]
        while stk:
            cur = stk[-1]
            stk.pop()
            for next in rooms[cur]:
                if not visited[next]:
                    visited[next] = True
                    stk.append(next)
        return all(visited)
