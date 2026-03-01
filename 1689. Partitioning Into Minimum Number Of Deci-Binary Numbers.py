class Solution:
    def minPartitions(self, n: str) -> int:
        return ord(max(c for c in n)) - ord('0')
