class Solution:
    def mirrorFrequency(self, s: str) -> int:
        def  mirror(c: int) -> int:
            if c >= ord('a') and c <= ord('z'):
                return ord('z') - (c - ord('a'))
            return ord('9') - (c - ord('0'))
        
        mp = [0] * 128
        for c in s:
            mp[ord(c)] += 1
        ans = 0
        for c in range(ord('a'), ord('z') + 1):
            ans += abs(mp[c] - mp[mirror(c)])
        for c in range(ord('0'), ord('9') + 1):
            ans += abs(mp[c] - mp[mirror(c)])
        return ans // 2;
