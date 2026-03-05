class Solution:
    def minOperations(self, s: str) -> int:
        return min(sum((ord(s[i]) - ord('0')) ^ (i & 1) for i in range(len(s))), sum((ord(s[i]) - ord('0')) ^ (i & 1) ^ 1 for i in range(len(s))))
