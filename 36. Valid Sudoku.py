from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            temp = 0
            for j in range(9):
                if not board[i][j] == '.':
                    if temp & (1 << (ord(board[i][j]) - ord('1'))):
                        return False
                    temp |= 1 << (ord(board[i][j]) - ord('1'))
        for i in range(9):
            temp = 0
            for j in range(9):
                if not board[j][i] == '.':
                    if temp & (1 << (ord(board[j][i]) - ord('1'))):
                        return False
                    temp |= 1 << (ord(board[j][i]) - ord('1'))
        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                temp = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if not board[i + dx][j + dy] == '.':
                            if temp & (1 << (ord(board[i + dx][j + dy]) - ord('1'))):
                                return False
                            temp |= 1 << (ord(board[i + dx][j + dy]) - ord('1'))
        return True
