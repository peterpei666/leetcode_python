class Solution:
    def checkTwoChessboards(self, s1: str, s2: str) -> bool:
       return not ((((ord(s1[0]) - ord('a')) & 1) ^ ((ord(s1[1]) - ord('0')) & 1)) ^ (((ord(s2[0]) - ord('a')) & 1) ^ ((ord(s2[1]) - ord('0')) & 1)))
