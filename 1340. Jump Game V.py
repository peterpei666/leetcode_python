class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        self.cnt = [0] * n
        def dfs(i: int) -> int:
            if self.cnt[i] != 0:
                return self.cnt[i]
            self.cnt[i] = 1
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                self.cnt[i] = max(self.cnt[i], dfs(j) + 1)
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                self.cnt[i] = max(self.cnt[i], dfs(j) + 1)
            return self.cnt[i]
        for i in range(n):
            if self.cnt[i] == 0:
                dfs(i)
        return max(self.cnt)
