from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        queue = deque([("0000", 0)])
        visited = {"0000"}
        while queue:
            curr, steps = queue.popleft()
            if curr == target:
                return steps
            for i in range(4):
                digit = int(curr[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    neighbor = curr[:i] + str(new_digit) + curr[i+1:]
                    if neighbor not in visited and neighbor not in dead_set:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
        return -1
