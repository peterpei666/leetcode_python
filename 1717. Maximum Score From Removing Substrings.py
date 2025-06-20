class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s.replace('a', '1').replace('b', '2').replace('1', 'b').replace('2', 'a')
            x, y = y, x
        ans = 0
        stack = []
        for c in s:
            if c == 'b' and stack and stack[-1] == 'a':
                ans += x
                stack.pop()
            else:
                stack.append(c)
        stack2 = []
        for c in stack:
            if c == 'a' and stack2 and stack2[-1] == 'b':
                ans += y
                stack2.pop()
            else:
                stack2.append(c)
        return ans
