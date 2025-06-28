class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        mp = [0] * (m * n + 1)
        for i in range(m * n):
            mp[arr[i]] = i
        ans = m * n
        for i in range(m):
            temp = 0
            for j in range(n):
                temp = max(temp, mp[mat[i][j]])
            ans = min(ans, temp)
        for j in range(n):
            temp = 0
            for i in range(m):
                temp = max(temp, mp[mat[i][j]])
            ans = min(ans, temp)
        return ans
