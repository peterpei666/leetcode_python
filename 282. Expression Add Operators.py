from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        n = len(num)
        s = ""

        def dfs(idx: int, pre: int, cur: int, val: int) -> None:
            nonlocal ans, s
            if idx == n:
                if val == target and cur == 0:
                    ans.append(s)
                return
            cur = cur * 10 + ord(num[idx]) - ord('0')
            s1 = str(cur)
            m = len(s)
            if cur > 0:
                dfs(idx + 1, pre, cur, val)
            s += "+" + s1
            dfs(idx + 1, cur, 0, val + cur)
            s = s[:m]
            s += "-" + s1
            dfs(idx + 1, -cur, 0, val - cur)
            s = s[:m]
            s += "*" + s1
            dfs(idx + 1, pre * cur, 0, val - pre + pre * cur)
            s = s[:m]

        pre = 0
        for i in range(1, n + 1):
            if i > 1 and num[0] == '0':
                break
            s = num[:i]
            pre = pre * 10 + ord(num[i - 1]) - ord('0')
            dfs(i, pre, 0, pre)
        return ans
