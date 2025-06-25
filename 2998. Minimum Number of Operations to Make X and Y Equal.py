from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        memo = [-1] * 10001
        memo[x] = 0
        q = deque()
        q.append(x)
        while q:
            t = q[0]
            q.popleft()
            if t == y:
                return memo[y]
            if t - 1 > 0 and (memo[t - 1] == -1 or memo[t - 1] > memo[t] + 1):
                memo[t - 1] = memo[t] + 1
                q.append(t - 1)
            if t + 1 <= 10000 and (memo[t + 1] == -1 or memo[t - 1] > memo[t] + 1):
                memo[t + 1] = memo[t] + 1
                q.append(t + 1)
            if t % 5 ==0 and (memo[t // 5] == -1 or memo[t // 5] > memo[t] + 1):
                memo[t // 5] = memo[t] + 1
                q.append(t // 5)
            if t % 11 ==0 and (memo[t // 11] == -1 or memo[t // 11] > memo[t] + 1):
                memo[t // 11] = memo[t] + 1
                q.append(t // 11)
        return memo[y]
