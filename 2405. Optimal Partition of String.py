class Solution:
    def partitionString(self, s: str) -> int:
        found = 0
        cnt = 1
        for c in s:
            if (found & (1 << (ord(c) - ord('a')))) != 0:
                cnt += 1
                found = 0
            found |= (1 << (ord(c) - ord('a')))
        return cnt
