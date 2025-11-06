class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not len(s1) + len(s2) == len(s3):
            return False
        memo = dict()
        n, n1, n2 = len(s3), len(s1), len(s2)

        def dfs(i1: int, i2: int) -> bool:
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            idx = i1 + i2
            if idx == n:
                return True
            ans = False
            if i1 < n1 and s1[i1] == s3[idx]:
                ans |= dfs(i1 + 1, i2)
            if i2 < n2 and s2[i2] == s3[idx]:
                ans |= dfs(i1, i2 + 1)
            memo[(i1, i2)] = ans
            return ans
        
        return dfs(0, 0)
