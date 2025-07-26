class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stk = [-1]
        ans = 0
        for i in range(n):
            if s[i] == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                ans = max(ans, i - stk[-1])
        return ans
