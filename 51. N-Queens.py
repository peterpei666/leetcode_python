from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        ans = []

        def valid(r: int, c: int) -> bool:
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
            for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            for i, j in zip(range(r, -1, -1), range(c, n, 1)):
                if board[i][j] == 'Q':
                    return False
            return True
        
        def construct(r: int) -> None:
            nonlocal board
            if r == n:
                ans.append(["".join(row) for row in board])
                return
            for i in range(n):
                if valid(r, i):
                    board[r][i] = 'Q'
                    construct(r + 1)
                    board[r][i] = '.'
        
        construct(0)
        return ans
