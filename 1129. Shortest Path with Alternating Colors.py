from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        blue = [[] for _ in range(n)]
        red = [[] for _ in range(n)]
        for u, v in redEdges:
            red[u].append(v)
        for u, v in blueEdges:
            blue[u].append(v)
        list1 = [float('inf')] * n
        list2 = [float('inf')] * n
        list1[0] = 0
        list2[0] = 0
        queue = deque([(0, 0), (0, 1)])
        while queue:
            node, b = queue.popleft()
            if b == 0:
                for next in red[node]:
                    if list2[next] > list1[node] + 1:
                        list2[next] = list1[node] + 1
                        queue.append((next, 1))
            else:
                for next in blue[node]:
                    if list1[next] > list2[node] + 1:
                        list1[next] = list2[node] + 1
                        queue.append((next, 0))
        result = []
        for i in range(n):
            if list1[i] == float('inf') and list2[i] == float('inf'):
                result.append(-1)
            else:
                result.append(min(list1[i], list2[i]))
        return result
