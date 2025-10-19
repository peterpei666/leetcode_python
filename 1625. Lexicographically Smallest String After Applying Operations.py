class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        mp = set()
        mp.add(s)
        stk = [s]

        def add(s1: str) -> str:
            ans = ''
            for i in range(len(s1)):
                if i % 2:
                    ans += str((int(s1[i]) + a) % 10)
                else:
                    ans += s1[i]
            return ans
        
        def rotate(s1: str) -> str:
            t = b % len(s1)
            return s1[-t:] + s1[:-t]
        
        while stk:
            temp = stk[-1]
            stk.pop()
            t = add(temp)
            if not t in mp:
                mp.add(t)
                stk.append(t)
            t = rotate(temp)
            if not t in mp:
                mp.add(t)
                stk.append(t)
        return sorted(list(mp))[0]
