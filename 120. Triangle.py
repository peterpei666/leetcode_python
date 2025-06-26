from collections import deque

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = [[10 ** 9] * n for _ in range(n)]
        q = deque()
        q.append([0, 0])
        memo[0][0] = triangle[0][0]
        while q:
            temp = q.popleft()
            if temp[0] + 1 == n:
                continue
            if memo[temp[0] + 1][temp[1]] > memo[temp[0]][temp[1]] + triangle[temp[0] + 1][temp[1]]:
                memo[temp[0] + 1][temp[1]] = memo[temp[0]][temp[1]] + triangle[temp[0] + 1][temp[1]]
                q.append([temp[0] + 1, temp[1]])
            if memo[temp[0] + 1][temp[1] + 1] > memo[temp[0]][temp[1]] + triangle[temp[0] + 1][temp[1] + 1]:
                memo[temp[0] + 1][temp[1] + 1] = memo[temp[0]][temp[1]] + triangle[temp[0] + 1][temp[1] + 1]
                q.append([temp[0] + 1, temp[1] + 1])
        return min(memo[-1])
