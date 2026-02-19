class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        stk = [1]
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                stk[-1] += 1
            else:
                stk.append(1)
        return sum(min(stk[i - 1], stk[i]) for i in range(1, len(stk)))
