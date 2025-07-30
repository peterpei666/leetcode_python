class Solution:
    def totalNQueens(self, n: int) -> int:
        place = [0] * n
        cnt = 0

        def valid(r: int, x: int) -> bool:
            for i in range(r):
                if x == place[i] or abs(r - i) == abs(x - place[i]):
                    return False
            return True
        
        def construct(r: int):
            if r == n:
                nonlocal cnt
                cnt += 1
            else:
                nonlocal place
                for i in range(n):
                    if valid(r, i):
                        place[r] = i
                        construct(r + 1)
        
        construct(0)
        return cnt
