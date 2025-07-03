class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        ret = ""
        for i in range(0, n, k):
            hash = 0
            for j in range(k):
                hash += ord(s[i + j]) - ord('a')
            ret += chr(hash % 26 + ord('a'))
        return ret
