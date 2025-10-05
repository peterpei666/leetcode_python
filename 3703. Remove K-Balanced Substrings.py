class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if not stk or not stk[-1][0] == c:
                stk.append((c, 1))
            else:
                stk[-1] = (stk[-1][0], stk[-1][1] + 1)
            while len(stk) >= 2:
                t1 = stk.pop()
                t2 = stk.pop()
                if t1[0] == ')' and t2[0] == '(' and t1[1] >= k and t2[1] >= k:
                    t1 = (t1[0], t1[1] - k)
                    t2 = (t2[0], t2[1] - k)
                    if t2[1] > 0:
                        stk.append(t2)
                    if t1[1] > 0:
                        stk.append(t1)
                else:
                    stk.append(t2)
                    stk.append(t1)
                    break
        return ''.join(c * cnt for c, cnt in stk)
