class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        result = [[boxGrid[m - 1 - j][i] for j in range(m)] for i in range(n)]
        for j in range(m):
            for i in range(n - 1, -1, -1):
                if result[i][j] == '.':
                    next = -1
                    for k in range(i - 1, -1, -1):
                        if result[k][j] == '*':
                            break
                        if result[k][j] == '#':
                            next = k
                            break
                    if next != -1:
                        result[i][j], result[next][j] = result[next][j], result[i][j]
        return result
