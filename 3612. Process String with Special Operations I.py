class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for c in s:
            if c == '*':
                if ans:
                    ans.pop()
            elif c == '#':
                ans = ans + ans
            elif c == '%':
                ans = ans[::-1]
            else:
                ans.append(c)
        return ''.join(ans)
