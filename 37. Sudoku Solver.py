from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def valid(r: int, c: int, num: int) -> bool:
            num_str = str(num)
            for i in range(9):
                if board[i][c] == num_str or board[r][i] == num_str:
                    return False
            x, y = r - r % 3, c - c % 3
            for i in range(3):
                for j in range(3):
                    if board[x + i][y + j] == num_str:
                        return False
            return True
        
        def dfs(r: int, c: int) -> bool:
            if r == 9:
                return True
            if c == 9:
                return dfs(r + 1, 0)
            if ord(board[r][c]) == ord('.'):
                for i in range(9):
                    if valid(r, c, i + 1):
                        board[r][c] = str(i + 1)
                        if dfs(r, c + 1):
                            return True
                        board[r][c] = '.'
            else:
                return dfs(r, c + 1)
            return False
        
        dfs(0, 0)
