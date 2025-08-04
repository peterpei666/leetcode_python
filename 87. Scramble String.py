class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        mp = dict()

        def valid(s1: str, s2: str) -> bool:
            cnt = [0] * 26
            for c in s1:
                cnt[ord(c) - ord('a')] += 1
            for c in s2:
                cnt[ord(c) - ord('a')] -= 1
            for i in cnt:
                if i != 0:
                    return False
            return True
        
        def func(s1: str, s2: str) -> bool:
            if (s1, s2) in mp:
                return mp[(s1, s2)]
            if not valid(s1, s2):
                mp[(s1, s2)] = False
                return False
            if len(s1) == 1:
                mp[(s1, s2)] = True
                return True
            for i in range(1, len(s1)):
                if (func(s1[:i], s2[-i:]) and func(s1[i:], s2[:-i])) or (func(s1[i:], s2[i:]) and func(s1[:i], s2[:i])):
                    mp[(s1, s2)] = True
                    return True
            mp[(s1, s2)] = False
            return False
        
        return func(s1, s2)
