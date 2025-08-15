class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
        ans = set()
        temp = ""
        n = len(s)

        def dfs(idx: int, l: int, r: int, open: int) -> None:
            nonlocal ans, temp
            if idx == n:
                if l == r == open == 0:
                    ans.add(temp)
                return
            m = len(temp)
            if s[idx] == '(':
                if l > 0:
                    dfs(idx + 1, l - 1, r, open)
                temp += s[idx]
                dfs(idx + 1, l, r, open + 1)
                temp = temp[:m]
            elif s[idx] == ')':
                if r > 0:
                    dfs(idx + 1, l, r - 1, open)
                if open>0:
                    temp += s[idx]
                    dfs(idx + 1, l, r, open - 1)
                    temp = temp[:m]
            else:
                temp += s[idx]
                dfs(idx + 1, l, r, open)
                temp = temp[:m]

        dfs(0, l, r, 0)
        return [k for k in ans]
