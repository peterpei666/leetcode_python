class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        cnt = [[0] * 26 for _ in range(2)]
        for i in range(len(s1)):
            cnt[i & 1][ord(s1[i]) - ord('a')] += 1
            cnt[i & 1][ord(s2[i]) - ord('a')] -= 1
        target = [0] * 26
        return cnt[0] == target and cnt[1] == target
