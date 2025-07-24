class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        cnt = 0
        sum = [0] * n
        t1, t2 = [0] * n, [0] * n

        def dfs(x: int, p: int) -> None:
            nonlocal cnt
            t1[x] = cnt
            cnt += 1
            sum[x] = nums[x]
            for next in graph[x]:
                if next != p:
                    dfs(next, x)
                    sum[x] ^= sum[next]
            t2[x] = cnt
        
        def cal(a: int, b: int, c: int) -> int:
            return max(a, b, c) - min(a, b, c)
        
        dfs(0, -1)
        ans = float('inf')
        for i in range(1, n):
            for j in range(i + 1, n):
                if t1[i] < t1[j] < t2[i]:
                    ans = min(ans, cal(sum[0] ^ sum[i], sum[i] ^ sum[j], sum[j]))
                elif t1[j] < t1[i] < t2[j]:
                    ans = min(ans, cal(sum[0] ^ sum[j], sum[i] ^ sum[j], sum[i]))
                else:
                    ans = min(ans, cal(sum[0] ^ sum[i] ^ sum[j], sum[i], sum[j]))
        return ans
