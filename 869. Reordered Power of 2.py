class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cnt = [0] * 10
        l = len(str(n))
        for c in str(n):
            cnt[int(c)] += 1
        def check(num: int) -> bool:
            return (num & (num - 1)) == 0
        def dfs(cur: int, len: int) -> bool:
            if len == l:
                return check(cur)
            for i in range(10):
                if cnt[i] > 0:
                    if len == 0 and i == 0:
                        continue
                    cnt[i] -= 1
                    if dfs(cur * 10 + i, len + 1):
                        return True
                    cnt[i] += 1
            return False
        return dfs(0, 0)
