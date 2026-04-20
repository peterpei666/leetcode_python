from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def swap(ori: tuple[int, int, int, int, int, int]) -> List[tuple[int, int, int, int, int, int]]:
            a, b, c, d, e, f = ori
            if a == 0:
                return [(b, a, c, d, e, f), (d, b, c, a, e, f)]
            elif b == 0:
                return [(b, a, c, d, e, f), (a, e, c, d, b, f), (a, c, b, d, e, f)]
            elif c == 0:
                return [(a, c, b, d, e, f), (a, b, f, d, e, c)]
            elif d == 0:
                return [(d, b, c, a, e, f), (a, b, c, e, d, f)]
            elif e == 0:
                return [(a, e, c, d, b, f), (a, b, c, e, d, f), (a, b, c, d, f, e)]
            else:
                return [(a, b, f, d, e, c), (a, b, c, d, f, e)]
            
        memo = set()
        q = deque()
        q.append(tuple(board[0] + board[1]))
        memo.add(q[0])
        ans = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q[0]
                q.popleft()
                if cur == (1, 2, 3, 4, 5, 0):
                    return ans
                for next in swap(cur):
                    if not next in memo:
                        memo.add(next)
                        q.append(next)
            ans += 1
        return -1
