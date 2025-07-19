class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        j, cur = 0, 0
        n = len(skills)
        for i in range(1, n):
            if skills[i] > skills[j]:
                j = i
                cur = 0
            cur += 1
            if cur == k:
                break
        return j
