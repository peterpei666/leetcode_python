import bisect

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        temp = []

        def dfs1(t, cur):
            complete = True
            for i in range(1, 8):
                if t[i] > 0:
                    complete = False
                    t[i] -= 1
                    dfs1(t, cur * 10 + i)
                    t[i] += 1
            if complete:
                temp.append(cur)

        def dfs(t, cur, s):
            for i in range(cur, 8):
                if s + i <= 7:
                    t[i] = i
                    dfs1(t, 0)
                    dfs(t, i + 1, s + i)
                    t[i] = 0
        t = [0] * 8
        dfs(t, 1, 0)
        temp.sort()
        idx = bisect.bisect_right(temp, n)
        return temp[idx]
