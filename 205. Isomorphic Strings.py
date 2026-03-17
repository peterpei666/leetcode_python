class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = [0] * 128
        for i in range(len(s)):
            if mp[ord(s[i])] == 0:
                mp[ord(s[i])] = ord(t[i])
            if not mp[ord(s[i])] == ord(t[i]):
                return False
        found = [False] * 128
        for i in mp:
            if i and found[i]:
                return False
            found[i] = True
        return True
