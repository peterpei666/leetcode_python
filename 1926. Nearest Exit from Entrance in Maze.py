from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append([entrance[0], entrance[1], 0])
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            x, y, step = q.popleft()
            
            for d in range(4):
                nx, ny = x + dir[d][0], y + dir[d][1]
                if (nx < 0 or nx >= len(maze) or ny < 0 or ny >= len(maze[0])) and step:
                    return step
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'
                    q.append([nx, ny, step + 1])
        return -1
