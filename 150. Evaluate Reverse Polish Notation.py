from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        op = ['+', '-', '*', '/']
        for s in tokens:
            if s in op:
                t2 = stk.pop()
                t1 = stk.pop()
                if s == '+':
                    stk.append(t1 + t2)
                elif s == '-':
                    stk.append(t1 - t2)
                elif s == '*':
                    stk.append(t1 * t2)
                else:
                    stk.append(int(t1 / t2))
            else:
                stk.append(int(s))
        return stk[-1]
