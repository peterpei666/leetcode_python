class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        memo = set()
        start = '0' * (n - 1)
        ans = ''

        def dfs(node: str):
            nonlocal ans
            for i in range(k):
                edge = node + str(i)
                if not edge in memo:
                    memo.add(edge)
                    dfs(edge[1:])
                    ans += str(i)
        
        dfs(start)
        return start + ans[::-1]
