class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total_skill = sum(skill)
        if total_skill % (n // 2) != 0:
            return -1
        target_skill = total_skill // (n // 2)
        ans = 0
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target_skill:
                return -1
            ans += skill[i] * skill[n - 1 - i]
        return ans
        
